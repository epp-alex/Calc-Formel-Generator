"""
services/favorites_service.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Favoriten-CRUD, Formel-Verlauf und Datenmigration.
Kein PyQt5-Import – vollständig UI-unabhängig.
"""
import json
from typing import Dict, List
from pathlib import Path

from .settings_service import (
    FAV_FILE, HISTORY_FILE, Config,
    atomic_write, log_exc,
)


# ---------------------------------------------------------------------------
# Favorite-Klasse  (kapselt Validierung, Serialisierung und Vergleich)
# ---------------------------------------------------------------------------
class Favorite:
    """
    Repräsentiert einen einzelnen Favoriten-Eintrag.

    Felder:
        formel  – die Calc-Formel (Pflicht, nicht leer)
        label   – optionaler Anzeigename
        team    – True = Team-Formel (schreibgeschützt für normale Nutzer)

    Vorteile gegenüber rohen dicts:
        • Validierung zentral (formel darf nicht leer sein)
        • Typsicherheit (team ist immer bool)
        • Migration von alten Formaten an einer Stelle
        • Einfache Erweiterung (z.B. Datum, Tags, DB-ID)
        • Vergleich via == funktioniert direkt
    """

    __slots__ = ("formel", "label", "team")

    def __init__(self, formel: str, label: str = "", team: bool = False) -> None:
        formel = formel.strip()
        if not formel:
            raise ValueError("Favorite.formel darf nicht leer sein")
        self.formel: str  = formel
        self.label:  str  = label.strip()
        self.team:   bool = bool(team)

    # ------------------------------------------------------------------
    # Serialisierung
    # ------------------------------------------------------------------
    def to_dict(self) -> dict:
        """Gibt ein JSON-serialisierbares Dict zurück."""
        return {"formel": self.formel, "label": self.label, "team": self.team}

    @classmethod
    def from_dict(cls, data: dict) -> "Favorite":
        """Erstellt einen Favorite aus einem Dict (inkl. altem String-Format)."""
        if isinstance(data, str):
            return cls(formel=data)
        if not isinstance(data, dict) or "formel" not in data:
            raise ValueError(f"Ungültiges Favoriten-Format: {data!r}")
        return cls(
            formel=data["formel"],
            label=data.get("label", ""),
            team=bool(data.get("team", False)),
        )

    # ------------------------------------------------------------------
    # Vergleich & Darstellung
    # ------------------------------------------------------------------
    def __eq__(self, other: object) -> bool:
        if isinstance(other, Favorite):
            return self.formel == other.formel
        return NotImplemented

    def __hash__(self) -> int:
        return hash(self.formel)

    def __repr__(self) -> str:
        tag = "[TEAM] " if self.team else ""
        name = f" ({self.label})" if self.label else ""
        return f"Favorite({tag}{self.formel!r}{name})"

    def display_text(self) -> str:
        """Anzeigetext für QListWidget-Einträge."""
        prefix = "[TEAM] " if self.team else ""
        suffix = f"  ▸ {self.label}" if self.label else ""
        return f"{prefix}{self.formel}{suffix}"


# ---------------------------------------------------------------------------
# Migration  (altes Format → Favorite-Objekte)
# ---------------------------------------------------------------------------
def migrate(raw: list) -> "list[Favorite]":
    """Konvertiert eine rohe JSON-Liste (Strings oder Dicts) in Favorite-Objekte."""
    result: List[Favorite] = []
    for item in raw:
        try:
            result.append(Favorite.from_dict(item))
        except (ValueError, TypeError) as e:
            log_exc(f"Ungültiger Favoriten-Eintrag übersprungen: {item!r}", e)
    return result


# ---------------------------------------------------------------------------
# Lesen / Schreiben
# ---------------------------------------------------------------------------
def read_fav_file(path: "Path | str") -> "list[Favorite]":
    """Liest eine favoriten.json und gibt eine Liste von Favorite-Objekten zurück."""
    try:
        raw = json.loads(Path(path).read_text(encoding="utf-8"))
        return migrate(raw)
    except Exception as e:
        log_exc(f"Favoriten-Datei konnte nicht gelesen werden: {path}", e)
        return []


def write_fav_file(path: "Path | str", entries: "list[Favorite]") -> None:
    """Schreibt eine Liste von Favorite-Objekten atomar als JSON."""
    atomic_write(
        path,
        json.dumps([f.to_dict() for f in entries], indent=2, ensure_ascii=False),
    )


# ---------------------------------------------------------------------------
# Lokale Favoriten
# ---------------------------------------------------------------------------
def load_local_favorites() -> "list[Favorite]":
    """Lädt die lokale Favoriten-Kopie (Offline-Fallback)."""
    if FAV_FILE.exists():
        return read_fav_file(FAV_FILE)
    return []


def save_local_favorites(entries: "list[Favorite]") -> None:
    """Speichert die Favoriten lokal (ohne Netz-Sync)."""
    try:
        write_fav_file(FAV_FILE, entries)
    except Exception as e:
        log_exc("Lokale Favoriten konnten nicht gespeichert werden", e)


# ---------------------------------------------------------------------------
# Verlauf
# ---------------------------------------------------------------------------
def load_history() -> List[str]:
    """Lädt den Formel-Verlauf aus verlauf.json."""
    if HISTORY_FILE.exists():
        try:
            data = json.loads(HISTORY_FILE.read_text(encoding="utf-8"))
            if isinstance(data, list):
                return [str(e) for e in data if e]
        except Exception as e:
            log_exc("verlauf.json konnte nicht geladen werden", e)
    return []


def save_history(history: List[str]) -> None:
    """Speichert den Verlauf atomar."""
    try:
        atomic_write(HISTORY_FILE, json.dumps(history, indent=2, ensure_ascii=False))
    except Exception as e:
        log_exc("Verlauf konnte nicht gespeichert werden", e)


def add_to_history(history: List[str], formula: str) -> List[str]:
    """
    Fügt ``formula`` am Anfang des Verlaufs ein, entfernt Duplikate
    und schneidet auf HISTORY_MAX. Mutiert die Original-Liste nicht.
    """
    history = [f for f in history if f != formula]
    history.insert(0, formula)
    return history[: Config.HISTORY_MAX]


# ---------------------------------------------------------------------------
# Favoriten-CRUD  (reine Datenoperationen, kein I/O)
# ---------------------------------------------------------------------------
def add_favorite(entries: "list[Favorite]", formel: str,
                 label: str = "") -> "list[Favorite]":
    """Fügt eine eigene Formel hinzu (falls noch nicht vorhanden)."""
    try:
        new = Favorite(formel=formel, label=label, team=False)
    except ValueError as e:
        log_exc("Ungültige Formel – Favorit wird nicht hinzugefügt", e)
        return entries
    if new in entries:   # nutzt Favorite.__eq__ (Vergleich via formel)
        return entries
    return entries + [new]


def remove_favorite(entries: "list[Favorite]",
                    formel: str) -> "list[Favorite]":
    """Entfernt eigene Formeln mit dem gegebenen Text (Team-Formeln bleiben)."""
    return [e for e in entries if not (e.formel == formel and not e.team)]


def reorder_own_favorites(entries, new_order):
    """
    Sortiert eigene Formeln gemäß ``new_order`` (Liste von Formel-Strings).
    Team-Formeln bleiben an ihrer relativen Position.
    """
    own_map = {e.formel: e for e in entries if not e.team}

    # Reihenfolge aus new_order, fehlende anhängen
    new_own = [own_map[f] for f in new_order if f in own_map]
    remaining = [e for f, e in own_map.items() if f not in new_order]
    new_own.extend(remaining)

    result = []
    own_iter = iter(new_own)
    for e in entries:
        if e.team:
            result.append(e)
        else:
            result.append(next(own_iter))
    return result
