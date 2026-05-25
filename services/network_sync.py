"""
services/network_sync.py
~~~~~~~~~~~~~~~~~~~~~~~~~
Netzwerk-Synchronisation der Favoriten-Datei.

Race-Condition-Schutz:
  • Dateibasiertes Locking  (O_CREAT | O_EXCL, SMB-kompatibel)
  • Content-Hash-Vergleich  (SHA-256, robuster als mtime auf FAT32/SMB)
  • Automatischer Retry     (max. 2 Versuche)
  • Atomares Schreiben      (via atomic_write aus settings_service)

Kein PyQt5-Import in den reinen Sync-Funktionen.
SyncWorker (QThread) am Ende der Datei ist der einzige UI-Berührungspunkt.
"""
import hashlib
from typing import List, Optional
import json
import os
import socket
import time
from pathlib import Path

from .settings_service import FAV_FILE, NET_FAV_NAME, FALLBACK_MESSAGES, log_exc
from .favorites_service import read_fav_file, write_fav_file
from .favorites_service import Favorite

# QThread-Import ist optional – erst beim Import des Workers nötig
try:
    from PyQt5.QtCore import QThread, pyqtSignal
    _QT_AVAILABLE = True
except ImportError:
    _QT_AVAILABLE = False


# ---------------------------------------------------------------------------
# Hilfsfunktionen: mtime + Content-Hash
# ---------------------------------------------------------------------------
def net_mtime(path) -> float:
    """Gibt mtime der Datei zurück, oder 0.0 wenn nicht vorhanden."""
    try:
        return Path(path).stat().st_mtime
    except OSError:
        return 0.0


def content_hash(path) -> "Optional[str]":
    """
    SHA-256-Hash des Datei-Inhalts.
    Gibt None zurück wenn die Datei nicht lesbar ist.
    """
    try:
        return hashlib.sha256(Path(path).read_bytes()).hexdigest()
    except OSError:
        return None


# ---------------------------------------------------------------------------
# Dateibasiertes Locking
# ---------------------------------------------------------------------------
def acquire_lockfile(lock_path: str, timeout: float = 15.0,
                     stale_after: float = 120.0) -> bool:
    """
    Exklusives dateibasiertes Lock für Netzlaufwerke (SMB / NFS / UNC).

    • O_CREAT | O_EXCL – atomar auf POSIX und den meisten SMB-Implementierungen
    • Veraltete Locks (> stale_after s) werden überschrieben
    • Retry mit 300 ms + Jitter (verhindert Thundering Herd)
    • Fallback wenn O_EXCL nicht unterstützt wird (ältere NAS)

    Gibt True zurück wenn der Lock erworben wurde, False bei Timeout.
    """
    deadline  = time.time() + timeout
    lock_info = json.dumps({
        "pid":  os.getpid(),
        "host": socket.gethostname(),
        "ts":   time.time(),
    }).encode("utf-8")

    while time.time() < deadline:
        if os.path.exists(lock_path):
            try:
                if time.time() - os.path.getmtime(lock_path) > stale_after:
                    os.remove(lock_path)
            except OSError:
                pass  # Paralleler Schreiber hat Lock gerade selbst entfernt

        try:
            fd = os.open(lock_path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            try:
                os.write(fd, lock_info)
            finally:
                os.close(fd)
            return True
        except FileExistsError:
            jitter = 0.05 * (hash(os.getpid()) % 5)
            time.sleep(0.3 + jitter)
        except OSError:
            try:
                with open(lock_path, "w", encoding="utf-8") as f:
                    json.dump({"pid": os.getpid(), "host": socket.gethostname()}, f)
                return True
            except OSError:
                return False

    return False


def release_lockfile(lock_path: str) -> None:
    """Entfernt die Lock-Datei. Fehler werden ignoriert (idempotent)."""
    try:
        os.remove(lock_path)
    except OSError:
        pass


# ---------------------------------------------------------------------------
# Gesichertes Netz-Schreiben
# ---------------------------------------------------------------------------
def safe_net_write(net_path: str, entries: list,
                   hash_before: "Optional[str]",
                   mtime_before: float = 0.0) -> "Optional[str]":
    """
    Schreibt ``entries`` gesichert in die Netz-Datei (innerhalb des Locks).

    Schutzebenen:
      1. Lock-Datei          → verhindert gleichzeitige Schreiber
      2. Content-Hash-Check  → erkennt Fremd-Änderungen zuverlässig
      3. mtime-Fallback      → wenn Hash nicht berechnet werden kann

    Rückgabe: None bei Erfolg, sonst ein i18n-Key als str.
    """
    lock_path = net_path + ".lock"

    if not acquire_lockfile(lock_path):
        return "net_err_lock_timeout"

    try:
        current_hash  = content_hash(net_path)
        current_mtime = net_mtime(net_path)

        conflict = False
        if hash_before is not None and current_hash is not None:
            conflict = current_hash != hash_before
        elif mtime_before != 0.0 and current_mtime != 0.0:
            conflict = current_mtime != mtime_before

        if conflict:
            return "net_err_conflict"

        write_fav_file(net_path, entries)
        return None
    finally:
        release_lockfile(lock_path)


# ---------------------------------------------------------------------------
# Merge-Logik
# ---------------------------------------------------------------------------
def merge_entries(net_entries: list, all_entries: list) -> list:
    """
    Mischt Team-Formeln (aus Netz) mit eigenen Formeln (aus all_entries).
    Eigene Formeln, die inzwischen zum Team-Eintrag wurden, werden entfernt.
    Unterstützt sowohl Favorite-Objekte als auch rohe dicts (Übergangszeit).
    """
    def is_team(e) -> bool:
        return e.team if hasattr(e, "team") else bool(e.get("team"))

    def get_formel(e) -> str:
        return e.formel if hasattr(e, "formel") else e["formel"]

    team_formeln   = [e for e in net_entries if is_team(e)]
    eigene_formeln = [e for e in all_entries if not is_team(e)]
    team_texte     = {get_formel(e) for e in team_formeln}
    return team_formeln + [e for e in eigene_formeln if get_formel(e) not in team_texte]


def net_fav_path(settings: dict) -> "Optional[Path]":
    """Gibt den vollständigen Netzpfad zur favoriten.json zurück, oder None."""
    base = settings.get("net_fav_dir", "").strip()
    if not base:
        return None
    return Path(base) / NET_FAV_NAME


# ---------------------------------------------------------------------------
# Sync-Funktionen (reine Business-Logik, kein UI)
# ---------------------------------------------------------------------------
def sync_from_network(settings: dict) -> List[dict]:
    """
    Beim Programmstart:
      1. Netz-Datei unter Lock lesen  →  lokal speichern  →  zurückgeben
      2. Netz nicht erreichbar        →  lokale Kopie (Offline-Fallback)
      3. Beides fehlt                 →  leere Liste
    """
    net = net_fav_path(settings)
    if net and net.exists():
        lock_path = str(net) + ".lock"
        locked = acquire_lockfile(lock_path, timeout=5.0)
        try:
            entries = read_fav_file(net)
        finally:
            if locked:
                release_lockfile(lock_path)
        try:
            write_fav_file(FAV_FILE, entries)
        except Exception as e:
            log_exc("Lokale Favoriten-Kopie konnte nicht aktualisiert werden", e)
        return entries

    if FAV_FILE.exists():
        return read_fav_file(FAV_FILE)
    return []


def sync_to_network(settings: dict, all_entries: List[dict],
                    lang_func=None) -> None:
    """
    Nach jeder Änderung:
      1. Lokal sofort speichern.
      2. Netz-Datei unter Lock lesen → mergen → schreiben.

    Bis zu 2 Versuche (1× Retry nach Hash-Konflikt).
    Wirft IOError bei nicht behebbaren Fehlern.
    """
    def _t(key, **kwargs):
        msg = lang_func(key) if lang_func else FALLBACK_MESSAGES.get(key, key)
        return msg.format(**kwargs) if kwargs else msg

    # --- Normalisiere eingehende Einträge zu Favorite-Objekten ---
    normalized_all_entries: List[Favorite] = []
    for e in all_entries:
        if isinstance(e, Favorite):
            normalized_all_entries.append(e)
        else:
            try:
                normalized_all_entries.append(Favorite.from_dict(e))
            except Exception as ex:
            # Ungültige Einträge überspringen und loggen
                log_exc(f"Ungültiger Favoriten-Eintrag beim Sync übersprungen: {e!r}", ex)

    # Lokal sofort speichern (write_fav_file erwartet Favorite-Objekte / dicts via to_dict)
    try:
        write_fav_file(FAV_FILE, normalized_all_entries)
    except Exception as e:
        raise IOError(_t("err_local_save", e=e)) from e

    net = net_fav_path(settings)
    if not net:
        return

    try:
        merged = normalized_all_entries  # Fallback falls die Schleife nicht läuft
        for attempt in range(2):
            hash_before  = content_hash(net)
            mtime_before = net_mtime(net)

            net_entries = read_fav_file(net) if net.exists() else []
            merged      = merge_entries(net_entries, normalized_all_entries)

            err_key = safe_net_write(str(net), merged,
                                     hash_before=hash_before,
                                     mtime_before=mtime_before)
            if err_key is None:
                break
            if err_key == "net_err_conflict" and attempt == 0:
                time.sleep(0.1)
                continue
            if err_key == "net_err_lock_timeout":
                raise IOError(_t("err_net_unreachable", e="Lock-Timeout"))
            raise IOError(_t(err_key))

        write_fav_file(FAV_FILE, merged)

    except PermissionError:
        raise IOError(_t("err_no_write_net"))
    except OSError as e:
        raise IOError(_t("err_net_unreachable", e=e))


# ---------------------------------------------------------------------------
# SyncWorker  (QThread – einziger PyQt5-Berührungspunkt in dieser Datei)
# ---------------------------------------------------------------------------
if _QT_AVAILABLE:
    class SyncWorker(QThread):
        """
        Führt sync_to_network() in einem eigenen Thread aus, damit die UI
        nicht einfriert, wenn das Netzlaufwerk langsam ist.

        Signale:
            finished()   – Sync erfolgreich abgeschlossen
            error(str)   – IOError mit Fehlermeldung
        """
        finished = pyqtSignal()
        error    = pyqtSignal(str)

        def __init__(self, settings: dict, entries: list,
                     lang_func=None, parent=None):
            super().__init__(parent)
            self._settings  = settings
            self._entries   = list(entries)   # Kopie – nie Live-Daten der UI
            self._lang_func = lang_func

        def run(self):
            try:
                sync_to_network(self._settings, self._entries,
                                lang_func=self._lang_func)
                self.finished.emit()
            except IOError as e:
                self.error.emit(str(e))
