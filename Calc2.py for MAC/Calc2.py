#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LibreOffice Calc Formel Helper
─────────────────────────────────────────────────────────────────────────────
Version:  1.0.2  |  Datum: 2026-05-27
─────────────────────────────────────────────────────────────────────────────
Datei-Struktur:

  Calc2.py             ← Hauptprogramm (diese Datei)
  language/
    languages.json            ← UI-Übersetzungen aller Sprachen
    formula_explanations.json ← Formelerklärungen je Sprache
  services/
    language_tool.py     ← Wizard: neue Sprache hinzufügen
    LangSync_Tool.py     ← Sprachcode-Abgleich gegen LO-Master
  settings.json        ← wird automatisch erstellt
  favoriten.json       ← lokale Kopie der Favoriten (automatisch erstellt)

  README_de.md / README_en.md / ...      ← Hilfe je Sprache
  REFERENZ_de.md / REFERENZ_en.md / ...  ← Funktionsreferenz je Sprache

Namenskonvention:
  README_{sprachcode}.md    z.B. README_de.md, README_en.md
  REFERENZ_{sprachcode}.md  z.B. REFERENZ_de.md, REFERENZ_en.md

Wenn eine Sprachdatei fehlt, wird automatisch auf Englisch zurückgegriffen.

─────────────────────────────────────────────────────────────────────────────
Team-Favoriten (Netzlaufwerk-Synchronisation)
─────────────────────────────────────────────────────────────────────────────
Über Einstellungen → Netzpfad konfigurieren lässt sich ein Netzlaufwerkpfad
(z.B. \\\\Server\\Freigabe\\formeln oder /mnt/nfs/formeln) eintragen.

Verhalten:
  • Beim Start:  Netz-favoriten.json  →  lokal  (Netz hat Vorrang, Offline-Fallback)
  • Beim Laden:  immer aus der lokalen Kopie (schnell, offline-fähig)
  • Beim Speichern / Löschen (eigene Formel):
      – lokal sofort schreiben
      – Netz-Datei lesen → eigene Formel ergänzen/entfernen → Netz schreiben
        (Team-Formeln [team]=True bleiben dabei unangetastet)
  • Team-Formeln sind mit [TEAM] gekennzeichnet und schreibgeschützt für
    normale Nutzer; ein Admin kann sie über den 🛠-Button im Admin-Panel
    verwalten (Passwort-geschützt mit PBKDF2-SHA256).

Admin-Passwort:
  Beim ersten Klick auf 🛠 wird ein Passwort festgelegt und lokal in
  admin.json gespeichert (nur Hash + Salt, nie das Klartext-Passwort).
  Jeder Admin-Rechner braucht sein eigenes admin.json (oder kopiert es).

JSON-Format  favoriten.json:
  [
    {"formel": "=SVERWEIS(A1;B1:C10;2;0)", "team": true,  "label": "SVERWEIS Standard"},
    {"formel": "=SUMME(A1:A10)",            "team": false, "label": ""}
  ]
  Altes Format (einfache String-Liste) wird automatisch migriert.
─────────────────────────────────────────────────────────────────────────────
"""
import datetime
import hashlib
import json
import logging
import os
import re
import secrets
import shutil
import socket
import subprocess
import sys
import tempfile
import time
import traceback
from pathlib import Path

# ---------------------------------------------------------------------------
# sys.path absichern: services/ muss neben Calc2.py liegen.
# ---------------------------------------------------------------------------

def _get_base_dir() -> Path:
    """
    Gibt immer den Ordner zurück wo Calc2.app / Calc2.py liegt.
    Funktioniert als .py Script, als --onedir .app und als frozen App.
    """
    if getattr(sys, "frozen", False):
        # PyInstaller --onedir:
        # sys.executable = .../Calc2.app/Contents/MacOS/Calc2
        # 3x .parent = Calc2_App/ (neben der .app)
        return Path(sys.executable).resolve().parent.parent.parent.parent
    else:
        # Normaler Python-Start
        return Path(__file__).resolve().parent

_here = _get_base_dir()

# WICHTIG: Das Arbeitsverzeichnis auf den Installationspfad festlegen
try:
    os.chdir(str(_here))
except Exception as e:
    print(f"Fehler beim Setzen des Arbeitsverzeichnisses: {e}")

if not (_here / "services").exists():
    _env_base = os.environ.get("CALC2_BASE", "")
    if _env_base:
        _here = Path(_env_base).resolve()
        os.chdir(str(_here)) # Auch hier das Verzeichnis wechseln

if str(_here) not in sys.path:
    sys.path.insert(0, str(_here))


from PyQt5.QtCore import QMimeData, QObject, Qt, QTimer, QThread, pyqtSignal
from PyQt5.QtGui import (
    QBrush, QColor, QFont, QPalette,
    QSyntaxHighlighter, QTextCharFormat, QFontDatabase,
)
from PyQt5.QtWidgets import (
    QAbstractItemView, QApplication, QComboBox, QDialog,
    QFileDialog, QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QInputDialog, QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QMessageBox, QPushButton, QScrollArea, QSizePolicy,
    QSplitter, QStackedWidget, QStatusBar, QTabWidget, QTextEdit,
    QVBoxLayout, QWidget,
)

# ---------------------------------------------------------------------------
# Services  (Business-Logik, UI-unabhängig)
# ---------------------------------------------------------------------------
from services.settings_service import (
    APP_NAME, FALLBACK_LANG, FALLBACK_MESSAGES,
    Config, THEME, THEME_LIGHT, THEME_DARK,
    RESOURCE_DIR, DATA_DIR,
    LANG_FILE, SETTINGS_FILE, FAV_FILE, HISTORY_FILE, ADMIN_FILE,
    get_app_data_dir, get_resource_dir,
    atomic_write, log_exc as _log_exc, _get_logger,
    load_settings, save_settings,
)
from services.auth_service import (
    admin_password_is_set, check_admin_password,
    set_admin_password, load_admin_config, save_admin_config,
)
from services.favorites_service import (
    Favorite,
    migrate as _migrate,
    read_fav_file as _read_fav_file,
    write_fav_file as _write_fav_file,
    load_history, save_history,
    add_to_history, add_favorite, remove_favorite, reorder_own_favorites,
    load_local_favorites,
)
from services.network_sync import (
    net_fav_path, sync_from_network, sync_to_network, SyncWorker,
    net_mtime as _net_mtime, safe_net_write as _safe_net_write,
)
from services.install_service import (
    first_run_install as _first_run_install, _load_early_lang,
    create_desktop_shortcut as _create_desktop_shortcut,
    get_desktop_path as _get_desktop_path,
)
from services.plugin_loader import load_all_plugins, resolve_formulas, get_plugin_text

# ---------------------------------------------------------------------------
# Version
# ---------------------------------------------------------------------------
_FONTS_RC_OK = False

def _pt(size: int) -> int:
    """Skaliert Schriftgrössen auf Mac automatisch hoch (96 DPI → 72 DPI Ausgleich)."""
    import platform
    if platform.system() == "Darwin":
        return round(size * 1.35)
    return size

def _system_ui_font_family() -> str:
    """Gibt die beste UI-Schrift für das aktuelle Betriebssystem zurück."""
    import platform
    system = platform.system()
    if system == "Darwin":
        return ".AppleSystemUIFont"  # KORREKT FÜR MAC: Verhindert den Absturz und den 2-Sekunden-Scan!
    elif system == "Windows":
        return "Segoe UI"
    else:
        return "Ubuntu"

def _system_ui_font_family() -> str:
    import platform
    s = platform.system()
    if s == "Darwin": 
        # ".AppleSystemUIFont" ist der offizielle macOS-System-Token.
        # Qt erkennt das sofort, bricht die Suche ab und nutzt die perfekte Mac-Schriftart.
        return ".AppleSystemUIFont" 
    if s == "Windows": 
        return "Segoe UI"
    return "Ubuntu"

def _register_hindi_font() -> bool:
    if not _FONTS_RC_OK:
        return False
    families = QFontDatabase().families()
    if any("Kohinoor Devanagari" in f for f in families):
        return True
    fid = QFontDatabase.addApplicationFont(":/fonts/NotoSansDevanagari-Regular.ttf")
    return fid >= 0

_LANG_FONTS = {
    "hi": ("Kohinoor Devanagari", 13),
}

# ---------------------------------------------------------------------------
# RTL-Unterstützung  (Arabisch, Hebräisch, Persisch, Urdu, …)
# ---------------------------------------------------------------------------
def _load_rtl_codes() -> set:
    """
    Liest alle Sprachcodes mit "rtl": true aus languages.json.
    Damit wird RTL zentral in der JSON verwaltet – kein Hardcoding nötig.
    Wenn die JSON nicht vorhanden ist, wird ein leeres Set zurückgegeben.
    """
    json_path = _here / "language" / "languages.json"
    if not json_path.exists():
        return set()
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return {code for code, val in data.items()
                if isinstance(val, dict)
                and isinstance(val.get("_meta"), dict)
                and val["_meta"].get("rtl", False)}
    except Exception:
        return set()

# Einmal beim Start laden – bei Sprachumschaltung neu geladen via _apply_rtl_layout
_RTL_CODES: set = _load_rtl_codes()


def _apply_rtl_layout(window: "QMainWindow", lang_code: str) -> None:
    """
    Schaltet das gesamte Fenster (und die QApplication) auf RTL oder LTR um.
    Wird beim Start und bei jedem Sprachwechsel aufgerufen.
    """
    global _RTL_CODES
    # Bei Sprachwechsel neu laden (falls language_tool eine neue RTL-Sprache ergänzt hat)
    _RTL_CODES = _load_rtl_codes()

    is_rtl = lang_code in _RTL_CODES
    direction = Qt.RightToLeft if is_rtl else Qt.LeftToRight

    # QApplication: beeinflusst alle neuen Widgets
    app = QApplication.instance()
    if app:
        app.setLayoutDirection(direction)

    # Hauptfenster selbst
    window.setLayoutDirection(direction)

    # Central Widget + alle Kinder rekursiv
    central = window.centralWidget()
    if central:
        central.setLayoutDirection(direction)

def _get_font_for_lang(lang_code):
    if lang_code in _LANG_FONTS:
        family, size = _LANG_FONTS[lang_code]
        return QFont(family, size)
    return None

def _install_font_if_needed(font_path: str, font_name: str) -> bool:
    """Font-Installation: Windows → Registry, macOS → ~/Library/Fonts, Linux → ~/.local/share/fonts"""
    import platform, shutil
    system = platform.system()
    src = Path(font_path)
    if system == "Windows":
        import ctypes
        win_fonts = Path(os.environ.get("WINDIR", "C:/Windows")) / "Fonts"
        dest = win_fonts / src.name
        if dest.exists():
            return True
        try:
            is_admin = ctypes.windll.shell32.IsUserAnAdmin()
            if not is_admin:
                result = ctypes.windll.shell32.ShellExecuteW(
                    None, "runas", sys.executable,
                    f'"{Path(__file__).resolve()}" --install-font "{font_path}"',
                    None, 1
                )
                return result > 32
            shutil.copy2(font_path, dest)
            import winreg
            key_path = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts"
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path,
                                0, winreg.KEY_SET_VALUE) as key:
                winreg.SetValueEx(key, f"{font_name} (TrueType)", 0, winreg.REG_SZ, src.name)
            ctypes.windll.gdi32.AddFontResourceW(str(dest))
            ctypes.windll.user32.SendMessageW(0xFFFF, 0x001D, 0, 0)
            return True
        except Exception as e:
            print(f"Font-Installation fehlgeschlagen (Windows): {e}")
            return False
    elif system == "Darwin":
        dest_dir = Path.home() / "Library" / "Fonts"
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest = dest_dir / src.name
        if dest.exists():
            return True
        try:
            shutil.copy2(font_path, dest)
            return True
        except Exception as e:
            print(f"Font-Installation fehlgeschlagen (macOS): {e}")
            return False
    else:
        dest_dir = Path.home() / ".local" / "share" / "fonts"
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest = dest_dir / src.name
        if dest.exists():
            return True
        try:
            shutil.copy2(font_path, dest)
            subprocess.run(["fc-cache", "-f", str(dest_dir)], capture_output=True, timeout=10)
            return True
        except Exception as e:
            print(f"Font-Installation fehlgeschlagen (Linux): {e}")
            return False

def _ensure_hindi_font(app) -> None:
    import platform
    font_file = _here / "fonts" / "NotoSansDevanagari-Regular.ttf"
    if not font_file.exists():
        return
    families = QFontDatabase().families()
    already_ok = any("Kohinoor Devanagari" in f for f in families)
    if already_ok:
        return
    system = platform.system()
    if system == "Darwin":
        hint = "Der Font wird in ~/Library/Fonts/ installiert.\nKein Administratorkennwort nötig."
    elif system == "Windows":
        hint = "Windows fragt möglicherweise nach Administrator-Rechten."
    else:
        hint = "Der Font wird in ~/.local/share/fonts/ installiert."
    msg = QMessageBox()
    msg.setWindowTitle("Hindi-Schrift installieren")
    msg.setText(
        "Für die Hindi-Schrift muss einmalig der Font\n"
        "'Kohinoor Devanagari' installiert werden.\n\n" + hint
    )
    msg.setIcon(QMessageBox.Information)
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    if msg.exec_() != QMessageBox.Ok:
        return
    ok = _install_font_if_needed(str(font_file), "Kohinoor Devanagari")
    if ok:
        QFontDatabase.addApplicationFont(str(font_file))
        QMessageBox.information(None, "Fertig",
            "Font erfolgreich installiert!\nDie Schrift wird ab jetzt korrekt angezeigt.")
    else:
        if system == "Darwin":
            anleitung = "fonts/NotoSansDevanagari-Regular.ttf\nin ~/Library/Fonts/ kopieren."
        elif system == "Windows":
            anleitung = "fonts/NotoSansDevanagari-Regular.ttf\nmanuell per Rechtsklick → Für alle Benutzer installieren."
        else:
            anleitung = "fonts/NotoSansDevanagari-Regular.ttf\nnach ~/.local/share/fonts/ kopieren,\ndann fc-cache -f im Terminal ausführen."
        QMessageBox.warning(None, "Hinweis",
            "Font konnte nicht installiert werden.\n\nManuell:\n" + anleitung)

def _ui_font(lang_code, size=9, bold=False):
    if lang_code in _LANG_FONTS:
        family, _ = _LANG_FONTS[lang_code]
        font = QFont(family, size)
        font.setWeight(700 if bold else 300)
        font.setStyleStrategy(QFont.PreferAntialias)
        font.setHintingPreference(QFont.PreferNoHinting)
    else:
        font = QFont(_system_ui_font_family(), size, QFont.Bold if bold else QFont.Normal)
    return font

def _build_lang_font(lang_code):
    if lang_code in _LANG_FONTS:
        family, size = _LANG_FONTS[lang_code]
        font = QFont(family, size)
        font.setWeight(300)
        font.setStyleStrategy(QFont.PreferAntialias)
        font.setHintingPreference(QFont.PreferNoHinting)
        return font
    return QFont(_system_ui_font_family(), _pt(11))

def _apply_font_recursive(widget, font):
    widget.setFont(font)
    for child in widget.findChildren(QWidget):
        child.setFont(font)

def _apply_font_to_app(app, lang_code):
    if lang_code in _LANG_FONTS:
        family, size = _LANG_FONTS[lang_code]
        font = QFont(family, size)
        font.setWeight(300)
        font.setStyleStrategy(QFont.PreferAntialias)
        font.setHintingPreference(QFont.PreferNoHinting)
        app.setFont(font)
        for w in app.allWidgets():
            w.setFont(font)
    else:
        app.setStyleSheet("")
        app.setFont(QFont(_system_ui_font_family(), _pt(11)))

# ---------------------------------------------------------------------------
APP_VERSION      = "1.0.1"
APP_VERSION_DATE = "2025-05-08"

# ---------------------------------------------------------------------------
# Pfad zum language/-Ordner
# ---------------------------------------------------------------------------
LANGUAGE_DIR   = _here / "language"
_lang_file_new = LANGUAGE_DIR / "languages.json"
CALC_TR_FILE   = LANGUAGE_DIR / "libreoffice_calc_translations.json"

if _lang_file_new.exists():
    LANG_FILE = _lang_file_new
    import services.settings_service as _ss
    _ss.LANG_FILE = _lang_file_new
    import services.install_service as _is
    if hasattr(_is, "LANG_FILE"):
        _is.LANG_FILE = _lang_file_new
elif not LANG_FILE.exists():
    _tmp_app = QApplication.instance() or QApplication(sys.argv)
    _mb = QMessageBox()
    _mb.setIcon(QMessageBox.Critical)
    _mb.setWindowTitle("Calc2 – Fehler")
    _mb.setText(
        f"languages.json nicht gefunden!\n\nErwartet unter:\n  {_lang_file_new}\n\n"
        f"Bitte sicherstellen dass der language/ Ordner\nneben Calc2.py liegt."
    )
    _mb.exec_()
    sys.exit(1)


class FormulaHighlighter(QSyntaxHighlighter):
    SYNTAX_PATTERNS: "dict[str, tuple[str, int]]" = {
        "cell_range": (r"\b[A-Z]+[0-9]+:[A-Z]+[0-9]+\b", 0),
        "cell_ref":   (r"\b[A-Z]+[0-9]+\b",               0),
        "string":     (r'"[^"]*"',                         0),
        "number":     (r"\b\d+(\.\d+)?\b",                 0),
        "operator":   (r"[+\-*/=;(),]",                    0),
    }

    _THEME_MAP: "dict[str, str]" = {
        "cell_range": "hl_cell",
        "cell_ref":   "hl_cell",
        "string":     "hl_string",
        "number":     "hl_number",
        "operator":   "hl_operator",
    }

    def __init__(self, document, functions=None):
        super().__init__(document)
        self.rules: "list[tuple[re.Pattern, QTextCharFormat]]" = []
        func_fmt = QTextCharFormat()
        func_fmt.setForeground(QColor(THEME["hl_function"]))
        func_fmt.setFontWeight(QFont.Bold)
        for f in (functions or []):
            pat = re.compile(r"\b" + re.escape(f) + r"\b", re.IGNORECASE)
            self.rules.append((pat, func_fmt))
        for key, (raw, flags) in self.SYNTAX_PATTERNS.items():
            fmt = QTextCharFormat()
            fmt.setForeground(QColor(THEME[self._THEME_MAP[key]]))
            self.rules.append((re.compile(raw, flags), fmt))

    def highlightBlock(self, text: str) -> None:
        for pattern, fmt in self.rules:
            for match in pattern.finditer(text):
                start, end = match.span()
                self.setFormat(start, end - start, fmt)


# ---------------------------------------------------------------------------
# Theme
# ---------------------------------------------------------------------------
def apply_theme(app: "QApplication", dark: bool) -> None:
    import services.settings_service as _ss
    _ss.THEME = _ss.THEME_DARK if dark else _ss.THEME_LIGHT
    global THEME
    THEME = _ss.THEME

    if dark:
        palette = QPalette()
        palette.setColor(QPalette.Window,          QColor(30,  30,  30))
        palette.setColor(QPalette.WindowText,      QColor(220, 220, 220))
        palette.setColor(QPalette.Base,            QColor(42,  42,  42))
        palette.setColor(QPalette.AlternateBase,   QColor(50,  50,  50))
        palette.setColor(QPalette.ToolTipBase,     QColor(50,  50,  50))
        palette.setColor(QPalette.ToolTipText,     QColor(220, 220, 220))
        palette.setColor(QPalette.Text,            QColor(220, 220, 220))
        palette.setColor(QPalette.Button,          QColor(55,  55,  55))
        palette.setColor(QPalette.ButtonText,      QColor(220, 220, 220))
        palette.setColor(QPalette.BrightText,      QColor(255, 100, 100))
        palette.setColor(QPalette.Highlight,       QColor(42,  100, 180))
        palette.setColor(QPalette.HighlightedText, QColor(255, 255, 255))
        palette.setColor(QPalette.Link,            QColor(100, 160, 240))
        palette.setColor(QPalette.Disabled, QPalette.Text,       QColor(120, 120, 120))
        palette.setColor(QPalette.Disabled, QPalette.ButtonText, QColor(120, 120, 120))
        app.setPalette(palette)
    else:
        app.setPalette(app.style().standardPalette())


def load_languages() -> dict:
    lang = _load_early_lang()
    if not LANG_FILE.exists():
        title = lang.get("msg_langfile_missing_title", FALLBACK_MESSAGES["msg_langfile_missing_title"])
        body  = lang.get("msg_langfile_missing_body",  FALLBACK_MESSAGES["msg_langfile_missing_body"]
                         ).format(path=LANG_FILE)
        QMessageBox.critical(None, title, body)
        return {}
    try:
        raw = json.loads(LANG_FILE.read_text(encoding="utf-8"))
        return {k: v for k, v in raw.items() if not k.startswith("_")}
    except json.JSONDecodeError as e:
        title = lang.get("msg_langfile_invalid_title", FALLBACK_MESSAGES["msg_langfile_invalid_title"])
        body  = lang.get("msg_langfile_invalid_body",  FALLBACK_MESSAGES["msg_langfile_invalid_body"]
                         ).format(error=e)
        QMessageBox.critical(None, title, body)
        return {}


# ---------------------------------------------------------------------------
# Markdown-Datei laden
# ---------------------------------------------------------------------------
def load_doc_file(prefix: str, lang: str, lang_func=None) -> str:
    def _t(key, **kwargs):
        if lang_func:
            msg = lang_func(key)
        else:
            msg = FALLBACK_MESSAGES.get(key, key)
        return msg.format(**kwargs) if kwargs else msg

    data_dir = _here / "data"
    for code in [lang, FALLBACK_LANG]:
        for search_dir in [data_dir, _here, DATA_DIR, RESOURCE_DIR]:
            path = search_dir / f"{prefix}_{code}.md"
            if path.exists():
                try:
                    return path.read_text(encoding="utf-8")
                except Exception as e:
                    return _t("doc_load_error", path=path, e=e)
    return _t("doc_not_found", prefix=prefix, lang=lang, data_dir=data_dir)


# ---------------------------------------------------------------------------
# Markdown-Viewer Dialog (Angepasst für Noto Sans Hindi)
# ---------------------------------------------------------------------------
class DocDialog(QDialog):
    def __init__(self, parent, title: str, content: str, tr_func=None):
        super().__init__(parent)
        self._tr = tr_func or (lambda k: k)
        
        # Sprache vom Hauptfenster abrufen
        self.current_lang = getattr(parent, "current_lang", "de")
        
        self.setWindowTitle(title)
        self.resize(Config.DLG_DOC_W, Config.DLG_DOC_H)
        self.setModal(False)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(8)

        # Header Bereich
        header = QHBoxLayout()
        lbl = QLabel(title)
        
        # Überschrift-Schriftart setzen
        lbl.setFont(_ui_font(self.current_lang, _pt(11), bold=True))
        
        header.addWidget(lbl)
        header.addStretch()

        btn_close = QPushButton(f"✖ {self._tr('btn_close')}")
        btn_close.setFixedWidth(Config.BTN_CLOSE_W)
        btn_close.clicked.connect(self.close)
        header.addWidget(btn_close)
        layout.addLayout(header)

        # Text-Bereich
        txt = QTextEdit()
        txt.setReadOnly(True)

        # --- SPEZIAL-LOGIK FÜR HINDI SCHRIFTART ---
        if self.current_lang == "hi":
            # Kohinoor Devanagari erzwingen
            # Größe 13 oder 14 ist für Hindi oft besser lesbar als 10
            hindi_font = QFont("Kohinoor Devanagari", _pt(13))
            txt.setFont(hindi_font)
            
            # CSS nutzen, um das "fette" Aussehen von Windows-Standard-Fonts zu verhindern
            txt.setStyleSheet("""
                QTextEdit { 
                    font-family: 'Kohinoor Devanagari'; 
                    line-height: 1.5; 
                }
            """)
        else:
            # Standard für alle anderen Sprachen
            txt.setFont(QFont(Config.FONT_MONO, _pt(10)))

        # Inhalt setzen (Nutze setMarkdown, falls deine Dateien Formatierungen haben)
        txt.setPlainText(content) 
        
        txt.setLineWrapMode(QTextEdit.WidgetWidth)
        layout.addWidget(txt)

# ---------------------------------------------------------------------------
# Dialog: Admin-Login
# ---------------------------------------------------------------------------
class AdminLoginDialog(QDialog):
    def __init__(self, parent, tr=None):
        super().__init__(parent)
        self._tr = tr or (lambda k: k)
        self.setWindowTitle(self._tr("adm_login_title"))
        self.setFixedWidth(Config.DLG_LOGIN_W)
        self.setModal(True)
        layout = QVBoxLayout(self)
        layout.setSpacing(12)
        lbl = QLabel(self._tr("adm_login_header"))
        lbl.setWordWrap(True)
        layout.addWidget(lbl)
        self._pw_edit = QLineEdit()
        self._pw_edit.setEchoMode(QLineEdit.Password)
        self._pw_edit.setPlaceholderText(self._tr("adm_login_placeholder"))
        self._pw_edit.returnPressed.connect(self._try_login)
        layout.addWidget(self._pw_edit)
        self._err_lbl = QLabel("")
        self._err_lbl.setStyleSheet(f"color: {THEME['ui_net_err']};")
        layout.addWidget(self._err_lbl)
        btn_row = QHBoxLayout()
        btn_row.addStretch()
        btn_ok = QPushButton(self._tr("adm_login_btn"))
        btn_ok.setDefault(True)
        btn_ok.clicked.connect(self._try_login)
        btn_row.addWidget(btn_ok)
        btn_cancel = QPushButton(self._tr("adm_btn_close"))
        btn_cancel.clicked.connect(self.reject)
        btn_row.addWidget(btn_cancel)
        layout.addLayout(btn_row)

    def _try_login(self):
        pw = self._pw_edit.text()
        if not pw:
            self._err_lbl.setText(self._tr("adm_login_empty"))
            return
        if check_admin_password(pw):
            self.accept()
        else:
            self._err_lbl.setText(self._tr("adm_login_wrong"))
            self._pw_edit.clear()
            self._pw_edit.setFocus()


# ---------------------------------------------------------------------------
# Dialog: Admin-Passwort setzen / ändern
# ---------------------------------------------------------------------------
class SetPasswordDialog(QDialog):
    def __init__(self, parent, is_first_time: bool = False, tr=None):
        super().__init__(parent)
        self._tr = tr or (lambda k: k)
        self.setWindowTitle(
            self._tr("adm_pw_title_new") if is_first_time else self._tr("adm_pw_title_change")
        )
        self.setFixedWidth(Config.DLG_SETPW_W)
        self.setModal(True)
        layout = QVBoxLayout(self)
        layout.setSpacing(10)
        info = QLabel(
            self._tr("adm_pw_info_new") if is_first_time else self._tr("adm_pw_info_change")
        )
        info.setWordWrap(True)
        layout.addWidget(info)
        if not is_first_time:
            layout.addWidget(QLabel(self._tr("adm_pw_lbl_old")))
            self._old_pw = QLineEdit()
            self._old_pw.setEchoMode(QLineEdit.Password)
            layout.addWidget(self._old_pw)
        else:
            self._old_pw = None
        layout.addWidget(QLabel(self._tr("adm_pw_lbl_new")))
        self._new_pw = QLineEdit()
        self._new_pw.setEchoMode(QLineEdit.Password)
        self._new_pw.setPlaceholderText(self._tr("adm_pw_placeholder"))
        layout.addWidget(self._new_pw)
        layout.addWidget(QLabel(self._tr("adm_pw_lbl_confirm")))
        self._confirm_pw = QLineEdit()
        self._confirm_pw.setEchoMode(QLineEdit.Password)
        layout.addWidget(self._confirm_pw)
        self._err_lbl = QLabel("")
        self._err_lbl.setStyleSheet(f"color: {THEME['ui_net_err']};")
        layout.addWidget(self._err_lbl)
        btn_row = QHBoxLayout()
        btn_row.addStretch()
        btn_ok = QPushButton(self._tr("adm_pw_btn_save"))
        btn_ok.setDefault(True)
        btn_ok.clicked.connect(self._save)
        btn_row.addWidget(btn_ok)
        btn_cancel = QPushButton(self._tr("adm_btn_close"))
        btn_cancel.clicked.connect(self.reject)
        btn_row.addWidget(btn_cancel)
        layout.addLayout(btn_row)

    def _save(self):
        new_pw  = self._new_pw.text()
        confirm = self._confirm_pw.text()
        if self._old_pw is not None:
            if not check_admin_password(self._old_pw.text()):
                self._err_lbl.setText(self._tr("adm_pw_wrong_old"))
                return
        if len(new_pw) < Config.MIN_PASSWORD_LENGTH:
            self._err_lbl.setText(self._tr("adm_pw_too_short").format(min=Config.MIN_PASSWORD_LENGTH))
            return
        if new_pw != confirm:
            self._err_lbl.setText(self._tr("adm_pw_mismatch"))
            return
        set_admin_password(new_pw)
        self.accept()


# ---------------------------------------------------------------------------
# Dialog: Admin-Panel
# ---------------------------------------------------------------------------
class AdminPanelDialog(QDialog):
    def __init__(self, parent, settings: dict, favoriten: list, tr=None):
        super().__init__(parent)
        self._tr = tr or (lambda k: k)
        self.setWindowTitle(self._tr("adm_panel_title"))
        self.resize(Config.DLG_ADMIN_W, Config.DLG_ADMIN_H)
        self.setModal(True)
        self._settings  = settings
        self._entries   = [e if isinstance(e, Favorite) else Favorite.from_dict(e) for e in favoriten]
        _net = net_fav_path(settings)
        self._net_mtime_on_open: float = _net_mtime(_net) if _net else 0.0
        layout = QVBoxLayout(self)
        layout.setSpacing(8)
        net = net_fav_path(settings)
        net_info = net if net else self._tr("adm_panel_no_net")
        info_lbl = QLabel(f"<small>{self._tr('adm_netzpfad_lbl')}: <code>{net_info}</code></small>")
        info_lbl.setWordWrap(True)
        layout.addWidget(info_lbl)
        self._list = QListWidget()
        self._list.setFont(QFont(Config.FONT_MONO, _pt(10)))
        self._list.setSelectionMode(QAbstractItemView.SingleSelection)
        self._list.itemDoubleClicked.connect(self._edit_entry)
        layout.addWidget(self._list, stretch=1)
        form_group = QGroupBox(self._tr("adm_form_group"))
        form_layout = QGridLayout(form_group)
        form_layout.setSpacing(6)
        form_layout.addWidget(QLabel(self._tr("adm_form_formel")), 0, 0)
        self._f_formel = QLineEdit()
        self._f_formel.setFont(QFont(Config.FONT_MONO, _pt(10)))
        self._f_formel.setPlaceholderText(self._tr("placeholder_example_formula"))
        form_layout.addWidget(self._f_formel, 0, 1)
        form_layout.addWidget(QLabel(self._tr("adm_form_label")), 1, 0)
        self._f_label = QLineEdit()
        self._f_label.setPlaceholderText(self._tr("adm_hint_label_ph"))
        form_layout.addWidget(self._f_label, 1, 1)
        form_layout.addWidget(QLabel(self._tr("adm_form_type")), 2, 0)
        self._f_team = QComboBox()
        self._f_team.addItem(self._tr("adm_form_team"), True)
        self._f_team.addItem(self._tr("adm_form_own"), False)
        form_layout.addWidget(self._f_team, 2, 1)
        layout.addWidget(form_group)
        btn_row = QHBoxLayout()
        btn_add = QPushButton(self._tr("adm_btn_add"))
        btn_add.setToolTip(self._tr("tooltip_add_formula"))
        btn_add.clicked.connect(self._add_entry)
        btn_row.addWidget(btn_add)
        btn_upd = QPushButton(self._tr("adm_btn_upd"))
        btn_upd.clicked.connect(self._update_entry)
        btn_row.addWidget(btn_upd)
        btn_del = QPushButton(self._tr("adm_btn_del"))
        btn_del.clicked.connect(self._delete_entry)
        btn_row.addWidget(btn_del)
        btn_row.addStretch()
        btn_pw = QPushButton(self._tr("adm_btn_pw"))
        btn_pw.clicked.connect(self._change_password)
        btn_row.addWidget(btn_pw)
        btn_net = QPushButton("🌐 " + self._tr("net_path_title"))
        btn_net.clicked.connect(self._configure_net_path_admin)
        btn_row.addWidget(btn_net)
        layout.addLayout(btn_row)
        line = QFrame(); line.setFrameShape(QFrame.HLine); line.setFrameShadow(QFrame.Sunken)
        layout.addWidget(line)
        bottom_row = QHBoxLayout()
        self._save_lbl = QLabel("")
        bottom_row.addWidget(self._save_lbl, stretch=1)
        btn_save = QPushButton(self._tr("adm_btn_save_net"))
        btn_save.setStyleSheet("font-weight: bold;")
        btn_save.clicked.connect(self._save_to_network)
        bottom_row.addWidget(btn_save)
        btn_close = QPushButton(self._tr("adm_btn_close"))
        btn_close.clicked.connect(self.reject)
        bottom_row.addWidget(btn_close)
        layout.addLayout(bottom_row)
        self._list.currentRowChanged.connect(self._on_select)
        self._refresh_list()

    def _refresh_list(self):
        self._list.clear()
        for e in self._entries:
            prefix  = "👥" if e.team else "⭐"
            display = f"{prefix}  {e.label + '  │  ' if e.label else ''}{e.formel}"
            item = QListWidgetItem(display)
            item.setData(Qt.UserRole, e.formel)
            if e.team:
                item.setForeground(QBrush(QColor(THEME["ui_team_fg"])))
            self._list.addItem(item)

    def _on_select(self, row: int):
        if row < 0 or row >= len(self._entries):
            return
        e = self._entries[row]
        self._f_formel.setText(e.formel)
        self._f_label.setText(e.label)
        self._f_team.setCurrentIndex(0 if e.team else 1)

    def _mark_unsaved(self) -> None:
        self._save_lbl.setText(
            f'<span style="color:{THEME["ui_warning"]}">● {self._tr("adm_unsaved")}</span>'
        )

    def _add_entry(self):
        formel = self._f_formel.text().strip()
        if not formel:
            QMessageBox.warning(self, self._tr("adm_warn_empty_title"), self._tr("adm_warn_empty"))
            return
        if any(e.formel == formel for e in self._entries):
            QMessageBox.warning(self, self._tr("adm_warn_dup_title"), self._tr("adm_warn_dup"))
            return
        self._entries.append(Favorite(
            formel=formel, label=self._f_label.text().strip(),
            team=bool(self._f_team.currentData()),
        ))
        self._refresh_list()
        self._list.setCurrentRow(len(self._entries) - 1)
        self._mark_unsaved()

    def _update_entry(self):
        row = self._list.currentRow()
        if row < 0:
            QMessageBox.information(self, self._tr("adm_info_title"), self._tr("adm_hint_select"))
            return
        formel = self._f_formel.text().strip()
        if not formel:
            QMessageBox.warning(self, self._tr("adm_warn_empty_title"), self._tr("adm_warn_empty"))
            return
        self._entries[row] = Favorite(
            formel=formel, label=self._f_label.text().strip(),
            team=bool(self._f_team.currentData()),
        )
        self._refresh_list()
        self._list.setCurrentRow(row)
        self._mark_unsaved()

    def _edit_entry(self, item: QListWidgetItem):
        self._on_select(self._list.currentRow())

    def _delete_entry(self):
        row = self._list.currentRow()
        if row < 0:
            return
        e = self._entries[row]
        ans = QMessageBox.question(
            self, self._tr("adm_del_title"),
            f"{self._tr('adm_del_msg')}\n\n{e.label or e.formel}",
            QMessageBox.Yes | QMessageBox.No
        )
        if ans == QMessageBox.Yes:
            self._entries.pop(row)
            self._refresh_list()
            self._mark_unsaved()

    def _save_to_network(self):
        net = net_fav_path(self._settings)
        if not net:
            QMessageBox.warning(self, self._tr("adm_no_net_title"), self._tr("adm_no_net_msg"))
            return
        try:
            net.parent.mkdir(parents=True, exist_ok=True)
            from services.network_sync import content_hash
            hash_before = content_hash(net) if net.exists() else None
            err_key = _safe_net_write(str(net), self._entries, hash_before, self._net_mtime_on_open)
            if err_key == "net_err_conflict":
                QMessageBox.warning(self, self._tr("msg_warn"), self._tr("net_err_conflict"))
                return
            if err_key == "net_err_lock_timeout":
                QMessageBox.warning(self, self._tr("msg_warn"), self._tr("net_err_lock_timeout"))
                return
            _write_fav_file(FAV_FILE, self._entries)
            self._net_mtime_on_open = _net_mtime(net)
            self._save_lbl.setText(f'<span style="color:{THEME["ui_net_ok"]}">✓ {net}</span>')
            self._saved_entries = self._entries[:]
        except PermissionError:
            QMessageBox.critical(self, self._tr("msg_warn"), self._tr("adm_err_no_write"))
        except OSError as e:
            QMessageBox.critical(self, self._tr("msg_warn"), f"{self._tr('adm_err_save')}\n{e}")

    def _change_password(self):
        dlg = SetPasswordDialog(self, is_first_time=False, tr=self._tr)
        if dlg.exec_() == QDialog.Accepted:
            QMessageBox.information(self, self._tr("adm_pw_changed_title"), self._tr("adm_pw_changed_msg"))

    def _configure_net_path_admin(self):
        current = self._settings.get("net_fav_dir", "")
        dlg = NetPathDialog(self, current, tr=self._tr)
        if dlg.exec_() == QDialog.Accepted:
            new_path = dlg.get_path()
            self._settings["net_fav_dir"] = new_path
            save_settings(self._settings)
            if hasattr(self.parent(), "_update_net_label"):
                self.parent()._update_net_label()

    def get_entries(self) -> list:
        return getattr(self, "_saved_entries", [])[:]


# ---------------------------------------------------------------------------
# Dialog: Backup / Restore
# ---------------------------------------------------------------------------
class BackupRestoreDialog(QDialog):
    """
    Backup  – sichert favoriten.json, plugins/, settings.json, admin.json,
               history.json in einen passwortgeschützten Unterordner auf dem
               Netzlaufwerk:  <netzpfad>/calc2_backups/<username>/
    Restore – spielt ein vorhandenes Backup wieder ein.

    Authentifizierung: einfaches PBKDF2-SHA256-Passwort, gespeichert in
    <backup_ordner>/backup_auth.json  (nur Hash + Salt, kein Klartext).
    """

    _BACKUP_SUBDIR = "calc2_backups"
    _AUTH_FILE     = "backup_auth.json"
    _MANIFEST_FILE = "backup_manifest.json"

    # Dateien relativ zu _here die gesichert werden
    _FILES_TO_BACKUP = [
        "favoriten.json",
        "settings.json",
        "admin.json",
        "history.json",
    ]
    # Ordner relativ zu _here die gesichert werden
    _DIRS_TO_BACKUP = [
        "plugins",
    ]

    def __init__(self, parent, mode: str, net_base: "Path | None", base_dir: Path):
        """
        mode     : "backup" oder "restore"
        net_base : Netzlaufwerk-Basispfad (aus settings["net_path"])
        base_dir : _here (Verzeichnis von Calc2.py)
        """
        super().__init__(parent)
        self._mode     = mode
        self._net_base = net_base
        self._base_dir = base_dir
        self.setWindowTitle("💾 Backup" if mode == "backup" else "🔄 Restore")
        self.setMinimumWidth(420)
        self.setModal(True)
        self._build_ui()

    # ── UI ──────────────────────────────────────────────────────────────────
    def _build_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(10)

        # Info-Label
        if self._mode == "backup":
            info_text = (
                "<b>Backup to network</b><br>"
                "Enter a username and password to protect your backup.<br>"
                "The following data will be saved:<br>"
                "• Favorites &nbsp;• Plugins &nbsp;• Settings &nbsp;• History"
            )
        else:
            info_text = (
                "<b>Restore from network</b><br>"
                "Enter your username and password to restore your backup.<br>"
                "<span style='color:#cc4444;'>⚠ Current data will be overwritten.</span>"
            )
        lbl_info = QLabel(info_text)
        lbl_info.setWordWrap(True)
        layout.addWidget(lbl_info)

        # Netzpfad-Status
        if self._net_base and Path(self._net_base).is_dir():
            net_status = f'<span style="color:green">✓ Network: {self._net_base}</span>'
        else:
            net_status = (
                f'<span style="color:red">✗ Network not reachable: '
                f'{self._net_base or "not configured"}</span>'
            )
        self._net_lbl = QLabel(net_status)
        self._net_lbl.setWordWrap(True)
        layout.addWidget(self._net_lbl)

        # Benutzername / Passwort
        form_layout = QGridLayout()
        form_layout.setSpacing(6)
        form_layout.addWidget(QLabel("Username:"), 0, 0)
        self._user_edit = QLineEdit()
        self._user_edit.setPlaceholderText("e.g. john.doe")
        form_layout.addWidget(self._user_edit, 0, 1)
        form_layout.addWidget(QLabel("Password:"), 1, 0)
        self._pw_edit = QLineEdit()
        self._pw_edit.setEchoMode(QLineEdit.Password)
        self._pw_edit.setPlaceholderText("at least 4 characters")
        form_layout.addWidget(self._pw_edit, 1, 1)
        layout.addLayout(form_layout)

        # Fehlermeldung
        self._err_lbl = QLabel("")
        self._err_lbl.setStyleSheet("color: red;")
        self._err_lbl.setWordWrap(True)
        layout.addWidget(self._err_lbl)

        # Buttons
        btn_row = QHBoxLayout()
        btn_row.addStretch()
        action_label = "💾 Save Backup" if self._mode == "backup" else "🔄 Restore"
        self._btn_ok = QPushButton(action_label)
        self._btn_ok.setDefault(True)
        self._btn_ok.clicked.connect(self._run)
        btn_row.addWidget(self._btn_ok)
        btn_cancel = QPushButton("Cancel")
        btn_cancel.clicked.connect(self.reject)
        btn_row.addWidget(btn_cancel)
        layout.addLayout(btn_row)

    # ── Hilfsmethoden ───────────────────────────────────────────────────────
    def _backup_dir(self, username: str) -> Path:
        return Path(self._net_base) / self._BACKUP_SUBDIR / username

    def _auth_path(self, username: str) -> Path:
        return self._backup_dir(username) / self._AUTH_FILE

    def _hash_password(self, password: str, salt: str) -> str:
        dk = hashlib.pbkdf2_hmac(
            "sha256", password.encode("utf-8"),
            salt.encode("utf-8"), 260_000
        )
        return dk.hex()

    def _check_net(self) -> bool:
        if not self._net_base or not Path(self._net_base).is_dir():
            self._err_lbl.setText(
                "❌ Network drive not reachable.\n"
                "Please configure the network path in Settings first."
            )
            return False
        return True

    def _validate_inputs(self) -> "tuple[str,str] | None":
        user = self._user_edit.text().strip()
        pw   = self._pw_edit.text()
        if not user:
            self._err_lbl.setText("❌ Please enter a username.")
            return None
        if len(pw) < 4:
            self._err_lbl.setText("❌ Password must be at least 4 characters.")
            return None
        # Ungültige Zeichen im Benutzernamen abfangen
        if not re.match(r'^[\w.\-]{1,64}$', user):
            self._err_lbl.setText("❌ Username may only contain letters, digits, dots and hyphens.")
            return None
        return user, pw

    # ── Backup ──────────────────────────────────────────────────────────────
    def _run_backup(self, user: str, pw: str):
        bdir = self._backup_dir(user)
        auth_path = self._auth_path(user)

        if bdir.exists() and auth_path.exists():
            # Passwort prüfen
            try:
                auth = json.loads(auth_path.read_text(encoding="utf-8"))
                if self._hash_password(pw, auth["salt"]) != auth["hash"]:
                    self._err_lbl.setText("❌ Wrong password for this username.")
                    return
            except Exception:
                self._err_lbl.setText("❌ Could not read backup authentication file.")
                return
            # Überschreiben fragen
            ans = QMessageBox.question(
                self, "Overwrite Backup",
                f"A backup for user '{user}' already exists.\n\nOverwrite it?",
                QMessageBox.Yes | QMessageBox.No,
            )
            if ans != QMessageBox.Yes:
                return
        else:
            # Neuer Backup – Passwort setzen
            bdir.mkdir(parents=True, exist_ok=True)
            salt = secrets.token_hex(16)
            auth_data = {"salt": salt, "hash": self._hash_password(pw, salt)}
            auth_path.write_text(json.dumps(auth_data), encoding="utf-8")

        # Dateien sichern
        errors = []
        backed_up = []
        for fname in self._FILES_TO_BACKUP:
            src = self._base_dir / fname
            if src.exists():
                try:
                    shutil.copy2(str(src), str(bdir / fname))
                    backed_up.append(fname)
                except Exception as e:
                    errors.append(f"{fname}: {e}")

        for dname in self._DIRS_TO_BACKUP:
            src = self._base_dir / dname
            dst = bdir / dname
            if src.is_dir():
                try:
                    if dst.exists():
                        shutil.rmtree(str(dst))
                    shutil.copytree(str(src), str(dst))
                    backed_up.append(f"{dname}/")
                except Exception as e:
                    errors.append(f"{dname}/: {e}")

        # Manifest schreiben
        manifest = {
            "created": datetime.datetime.now().isoformat(timespec="seconds"),
            "files": backed_up,
        }
        (bdir / self._MANIFEST_FILE).write_text(
            json.dumps(manifest, indent=2), encoding="utf-8"
        )

        if errors:
            QMessageBox.warning(
                self, "Backup – Partial",
                "Backup completed with errors:\n\n" + "\n".join(errors)
            )
        else:
            QMessageBox.information(
                self, "Backup – Done",
                f"✅ Backup saved successfully!\n\n"
                f"Location: {bdir}\n"
                f"Files: {', '.join(backed_up)}"
            )
        self.accept()

    # ── Restore ─────────────────────────────────────────────────────────────
    def _run_restore(self, user: str, pw: str):
        bdir      = self._backup_dir(user)
        auth_path = self._auth_path(user)

        if not bdir.exists() or not auth_path.exists():
            self._err_lbl.setText(f"❌ No backup found for user '{user}'.")
            return

        # Passwort prüfen
        try:
            auth = json.loads(auth_path.read_text(encoding="utf-8"))
            if self._hash_password(pw, auth["salt"]) != auth["hash"]:
                self._err_lbl.setText("❌ Wrong password.")
                return
        except Exception:
            self._err_lbl.setText("❌ Could not read backup authentication file.")
            return

        # Manifest lesen
        manifest_path = bdir / self._MANIFEST_FILE
        created_info  = ""
        if manifest_path.exists():
            try:
                m = json.loads(manifest_path.read_text(encoding="utf-8"))
                created_info = f"\nBackup date: {m.get('created', 'unknown')}"
            except Exception:
                pass

        ans = QMessageBox.question(
            self, "Confirm Restore",
            f"Restore backup for user '{user}'?{created_info}\n\n"
            "⚠ Current favorites, plugins and settings will be overwritten.",
            QMessageBox.Yes | QMessageBox.No,
        )
        if ans != QMessageBox.Yes:
            return

        errors = []
        restored = []
        for fname in self._FILES_TO_BACKUP:
            src = bdir / fname
            if src.exists():
                try:
                    shutil.copy2(str(src), str(self._base_dir / fname))
                    restored.append(fname)
                except Exception as e:
                    errors.append(f"{fname}: {e}")

        for dname in self._DIRS_TO_BACKUP:
            src = bdir / dname
            dst = self._base_dir / dname
            if src.is_dir():
                try:
                    if dst.exists():
                        shutil.rmtree(str(dst))
                    shutil.copytree(str(src), str(dst))
                    restored.append(f"{dname}/")
                except Exception as e:
                    errors.append(f"{dname}/: {e}")

        if errors:
            QMessageBox.warning(
                self, "Restore – Partial",
                "Restore completed with errors:\n\n" + "\n".join(errors)
            )
        else:
            QMessageBox.information(
                self, "Restore – Done",
                f"✅ Restore successful!\n\n"
                f"Files restored: {', '.join(restored)}\n\n"
                "Please restart the application for all changes to take effect."
            )
        self.accept()

    # ── Dispatcher ──────────────────────────────────────────────────────────
    def _run(self):
        self._err_lbl.clear()
        if not self._check_net():
            return
        result = self._validate_inputs()
        if result is None:
            return
        user, pw = result
        if self._mode == "backup":
            self._run_backup(user, pw)
        else:
            self._run_restore(user, pw)


# ---------------------------------------------------------------------------
# Dialog: Netzpfad konfigurieren
# ---------------------------------------------------------------------------
class NetPathDialog(QDialog):
    def __init__(self, parent, current_path: str = "", tr=None):
        super().__init__(parent)
        self._tr = tr or (lambda k: k)
        self.setWindowTitle(self._tr("net_path_title"))
        self.setMinimumWidth(Config.DLG_NET_MIN_W)
        self.setModal(True)
        layout = QVBoxLayout(self)
        layout.setSpacing(10)
        info = QLabel(self._tr("net_path_info"))
        info.setWordWrap(True)
        layout.addWidget(info)
        path_row = QHBoxLayout()
        self._path_edit = QLineEdit(current_path)
        self._path_edit.setPlaceholderText(self._tr("net_path_placeholder"))
        path_row.addWidget(self._path_edit, stretch=1)
        btn_browse = QPushButton(self._tr("btn_browse"))
        btn_browse.clicked.connect(self._browse)
        path_row.addWidget(btn_browse)
        layout.addLayout(path_row)
        self._status_lbl = QLabel("")
        self._status_lbl.setWordWrap(True)
        layout.addWidget(self._status_lbl)
        self._path_edit.textChanged.connect(self._check_path)
        self._check_path(current_path)
        btn_row = QHBoxLayout()
        btn_row.addStretch()
        btn_clear = QPushButton(self._tr("btn_clear_path"))
        btn_clear.clicked.connect(self._clear)
        btn_row.addWidget(btn_clear)
        btn_ok = QPushButton(self._tr("btn_apply"))
        btn_ok.setDefault(True)
        btn_ok.clicked.connect(self.accept)
        btn_row.addWidget(btn_ok)
        btn_cancel = QPushButton(self._tr("btn_cancel"))
        btn_cancel.clicked.connect(self.reject)
        btn_row.addWidget(btn_cancel)
        layout.addLayout(btn_row)

    def _browse(self):
        path = QFileDialog.getExistingDirectory(self, self._tr("net_folder_select"))
        if path:
            self._path_edit.setText(path)

    def _clear(self):
        self._path_edit.clear()

    def _check_path(self, text: str):
        text = text.strip()
        if not text:
            self._status_lbl.setText(f'<span style="color:{THEME["ui_info"]}">ℹ {self._tr("net_path_removed")}</span>')
        elif Path(text).is_dir():
            self._status_lbl.setText(f'<span style="color:{THEME["ui_net_ok"]}">{self._tr("net_status_ready")}</span>')
        else:
            self._status_lbl.setText(f'<span style="color:{THEME["ui_net_err"]}">{self._tr("net_status_not_found")}</span>')

    def get_path(self) -> str:
        return self._path_edit.text().strip()


# ---------------------------------------------------------------------------
# Haupt-Fenster
# ---------------------------------------------------------------------------
from PyQt5.QtGui import QIcon
class CalcFormelHelper(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(1024, 950)
        self.langs    = load_languages()
        self._calc_tr = self._load_calc_translations()
        self._expl_strings = self._load_expl_strings()
        self.settings = load_settings()
        if self.settings["language"] not in self.langs:
            self.settings["language"] = next(iter(self.langs), FALLBACK_LANG)
        self.current_lang = self.settings["language"]
        self._dark_mode   = bool(self.settings.get("dark_mode", False))
        self.favoriten: list = sync_from_network(self.settings)
        self._verlauf: "list[str]" = load_history()
        self._init_undo()
        self._sync_workers: "set[SyncWorker]" = set()
        self._plugins = load_all_plugins(
            plugins_dir   = _here / "plugins",
            lang          = self.current_lang,
            fallback_lang = FALLBACK_LANG,
            app_version   = APP_VERSION,
        )
        self._status_bar = QStatusBar()
        self.setStatusBar(self._status_bar)
        _shortcut_hint = QLabel("  Ctrl+X: Minimize / Restore  ")
        _shortcut_hint.setStyleSheet("color: #888; font-size: 11pt;")
        self._status_bar.addPermanentWidget(_shortcut_hint)
        central = QWidget()
        self.setCentralWidget(central)
        self._root_layout = QVBoxLayout(central)
        self._root_layout.setContentsMargins(10, 10, 10, 10)
        self._root_layout.setSpacing(6)
        self._erstelle_ui()
        _apply_font_to_app(QApplication.instance(), self.current_lang)
        _apply_rtl_layout(self, self.current_lang)

    def _icon(self, name: str) -> QIcon:
        """Lädt ein Icon plattformunabhängig aus dem 'Icon'-Ordner"""
        import sys
        
        # Prüfen, ob das Programm als fertige .app kompilierte wurde
        if getattr(sys, 'frozen', False):
            # sys.executable zeigt auf Calc2.app/Contents/MacOS/Calc2
            # Wir gehen 4 Ebenen nach oben, um direkt NEBEN die Calc2.app zu kommen
            app_dir = os.path.dirname(os.path.abspath(sys.executable))
            base_dir = os.path.dirname(os.path.dirname(os.path.dirname(app_dir)))
        else:
            # Normaler Start im Editor (Skript-Modus)
            base_dir = os.path.dirname(os.path.abspath(__file__))
            
        icon_path = os.path.join(base_dir, "Icon", name)
        return QIcon(icon_path)

    # -----------------------------------------------------------------------
    # Tastaturkürzel
    # -----------------------------------------------------------------------
    def keyPressEvent(self, event) -> None:
        focused    = QApplication.focusWidget()
        in_input   = isinstance(focused, (QLineEdit, QTextEdit))
        mod        = event.modifiers()
        ctrl       = mod == Qt.ControlModifier
        ctrl_shift = mod == (Qt.ControlModifier | Qt.ShiftModifier)
        if ctrl:
            if event.key() == Qt.Key_S:
                self.formel_speichern(); return
            if event.key() == Qt.Key_C and not in_input:
                self.kopieren(); return
            if event.key() == Qt.Key_Z and not in_input:
                self._undo(); return
            if event.key() == Qt.Key_Y and not in_input:
                self._redo(); return
        if ctrl_shift and event.key() == Qt.Key_Z and not in_input:
            self._redo(); return
        if ctrl and event.key() == Qt.Key_F12:
            self._toggle_minimize(); return
        super().keyPressEvent(event)

    def _toggle_minimize(self) -> None:
        """
        Minimieren / Wiederherstellen.
        Eigener _is_minimized-Flag weil isMinimized() auf Windows
        beim globalen Hotkey-Thread nicht immer zuverlässig ist.
        """
        # Fensterzustand direkt von Qt abfragen
        state = self.windowState()
        is_min = bool(state & Qt.WindowMinimized)

        if is_min or not self.isVisible():
            # Wiederherstellen
            def _restore():
                self.setWindowState(
                    (state & ~Qt.WindowMinimized) | Qt.WindowActive
                )
                self.showNormal()
                self.activateWindow()
                self.raise_()
                self.setFocus()
            QTimer.singleShot(0, _restore)
        else:
            self.showMinimized()

    # -----------------------------------------------------------------------
    # Übersetzung
    # -----------------------------------------------------------------------
    # Mapping from internal f_key → English function name (key in libreoffice_calc_translations.json)
    _F_KEY_TO_EN: "dict[str, str]" = {
        "f_sum":       "SUM",
        "f_avg":       "AVERAGE",
        "f_min":       "MIN",
        "f_max":       "MAX",
        "f_count":     "COUNT",
        "f_count2":    "COUNTA",
        "f_sumprod":   "SUMPRODUCT",
        "f_median":    "MEDIAN",
        "f_if":        "IF",
        "f_and":       "AND",
        "f_or":        "OR",
        "f_not":       "NOT",
        "f_sumif":     "SUMIF",
        "f_countif":   "COUNTIF",
        "f_avgif":     "AVERAGEIF",
        "f_sumifs":    "SUMIFS",
        "f_stdev":     "STDEV",
        "f_var":       "VAR",
        "f_countblank":"COUNTBLANK",
        "f_large":     "LARGE",
        "f_today":     "TODAY",
        "f_now":       "NOW",
        "f_year":      "YEAR",
        "f_month":     "MONTH",
        "f_day":       "DAY",
        "f_date":      "DATE",
        "f_datedif":   "DATEDIF",
        "f_weekday":   "WEEKDAY",
        "f_concat":    "CONCATENATE",
        "f_len":       "LEN",
        "f_left":      "LEFT",
        "f_right":     "RIGHT",
        "f_mid":       "MID",
        "f_upper":     "UPPER",
        "f_lower":     "LOWER",
        "f_trim":      "TRIM",
        "f_vlookup":   "VLOOKUP",
        "f_hlookup":   "HLOOKUP",
        "f_index":     "INDEX",
        "f_match":     "MATCH",
        "f_round":     "ROUND",
        "f_roundup":   "ROUNDUP",
        "f_rounddown": "ROUNDDOWN",
        "f_int":       "INT",
        "f_trunc":     "TRUNC",
        "f_abs":       "ABS",
        "f_mod":       "MOD",
        "f_sqrt":      "SQRT",
        "f_rand":      "RAND",
    }

    def _load_calc_translations(self) -> dict:
        """Load libreoffice_calc_translations.json once at startup.

        Structure: { "SUM": { "en": "SUM", "de": "SUMME", "fr": "SOMME", ... }, ... }
        Shows a warning dialog if the file is missing or cannot be parsed.
        """
        if not CALC_TR_FILE.exists():
            QMessageBox.warning(
                None,
                "libreoffice_calc_translations.json not found",
                f"Expected at:\n  {CALC_TR_FILE}\n\n"
                "Formula names cannot be translated without this file.\n"
                "Place the file in the language/ folder to fix this."
            )
            return {}
        try:
            return json.loads(CALC_TR_FILE.read_text(encoding="utf-8"))
        except Exception as e:
            QMessageBox.warning(
                None,
                "libreoffice_calc_translations.json – parse error",
                f"Could not parse the file:\n{e}\n\n"
                "Formula names cannot be translated without this file."
            )
            return {}

    def tr(self, key: str) -> str:
        # Formula keys (f_*) → official names from libreoffice_calc_translations.json
        if key.startswith("f_") and self._calc_tr:
            en_name = self._F_KEY_TO_EN.get(key)
            if en_name:
                entry = self._calc_tr.get(en_name, {})
                # 1. current language  2. English fallback  3. English name itself
                return entry.get(self.current_lang) or entry.get("en") or en_name
        # All other keys → UI strings from languages.json
        return self.langs.get(self.current_lang, {}).get(key, key)

    def _get_function_names(self) -> "list[str]":
        if self._calc_tr:
            return [
                entry.get(self.current_lang) or entry.get("en", "")
                for entry in self._calc_tr.values()
                if isinstance(entry, dict)
                and (entry.get(self.current_lang) or entry.get("en"))
            ]
        # Fallback: libreoffice_calc_translations.json not loaded – returns empty list
        lang_data = self.langs.get(self.current_lang, {})
        return [v for k, v in lang_data.items() if k.startswith("f_")]

    # -----------------------------------------------------------------------
    # Eingabe-Helfer
    # -----------------------------------------------------------------------
    @staticmethod
    def _apply_mode(ref: str, mode: int) -> str:
        m = re.fullmatch(r'([A-Za-z]+)([0-9]+)', ref.strip())
        if not m:
            return ref
        col, row = m.group(1).upper(), m.group(2)
        if mode == 0: return f"{col}{row}"
        if mode == 1: return f"${col}{row}"
        if mode == 2: return f"{col}${row}"
        if mode == 3: return f"${col}${row}"
        return ref

    @staticmethod
    def _apply_mode_range(ref: str, mode: int) -> str:
        if ":" in ref:
            l, r = ref.split(":", 1)
            return (CalcFormelHelper._apply_mode(l, mode)
                    + ":"
                    + CalcFormelHelper._apply_mode(r, mode))
        return CalcFormelHelper._apply_mode(ref, mode)

    def _combo_mode(self, attr: str) -> int:
        ddl = getattr(self, attr, None)
        return ddl.currentIndex() if ddl else 0

    def _z1_mode(self)  -> int: return self._combo_mode("_ddl_z1")
    def _z2_mode(self)  -> int: return self._combo_mode("_ddl_z2")
    def _br_mode(self)  -> int: return self._combo_mode("_ddl_br")
    def _br2_mode(self) -> int: return self._combo_mode("_ddl_br2")

    def z1(self) -> str:
        return self._apply_mode(self.zelle1_entry.text() or "A1", self._z1_mode())
    def z2(self) -> str:
        return self._apply_mode(self.zelle2_entry.text() or "B1", self._z2_mode())
    def br(self) -> str:
        return self._apply_mode_range(self.bereich_entry.text() or "A1:A10", self._br_mode())
    def br2(self) -> str:
        return self._apply_mode_range(self.bereich2_entry.text() or "B1:B10", self._br2_mode())
    def pa(self) -> str:
        return self.param_entry.text() or "2"

    # -----------------------------------------------------------------------
    # Undo / Redo
    # -----------------------------------------------------------------------
    _last_formula_fn: "callable | None" = None
    _undo_stack:  "list[str]"
    _redo_stack:  "list[str]"
    _undo_ignore: bool

    def _init_undo(self) -> None:
        self._undo_stack  = []
        self._redo_stack  = []
        self._undo_ignore = False

    def set_o(self, val: str) -> None:
        if not self._undo_ignore:
            current = getattr(self, "output_entry", None)
            if current is not None:
                old = current.toPlainText()
                if old != val:
                    self._undo_stack.append(old)
                    if len(self._undo_stack) > Config.UNDO_MAX:
                        self._undo_stack.pop(0)
                    self._redo_stack.clear()
                    self._update_undo_buttons()
        self.output_entry.setPlainText(val)

    def _undo(self) -> None:
        if not self._undo_stack: return
        current = self.output_entry.toPlainText()
        self._redo_stack.append(current)
        prev = self._undo_stack.pop()
        self._undo_ignore = True
        self.output_entry.setPlainText(prev)
        self._undo_ignore = False
        self._update_undo_buttons()

    def _redo(self) -> None:
        if not self._redo_stack: return
        current = self.output_entry.toPlainText()
        self._undo_stack.append(current)
        nxt = self._redo_stack.pop()
        self._undo_ignore = True
        self.output_entry.setPlainText(nxt)
        self._undo_ignore = False
        self._update_undo_buttons()

    def _update_undo_buttons(self) -> None:
        if hasattr(self, "_btn_undo"):
            self._btn_undo.setEnabled(bool(self._undo_stack))
        if hasattr(self, "_btn_redo"):
            self._btn_redo.setEnabled(bool(self._redo_stack))

    # -----------------------------------------------------------------------
    # Live-Update
    # -----------------------------------------------------------------------
    def _register_and_set(self, fn: "callable") -> None:
        if not self._inputs_valid():
            self._status_bar.showMessage(self.tr("err_invalid_cell"), Config.MSG_NORMAL)
            return
        self._last_formula_fn = fn
        fn()
        formel = self.output_entry.toPlainText().strip()
        if formel:
            self._add_to_history(formel)

    def _live_refresh(self, *_) -> None:
        if self._last_formula_fn is not None:
            self._undo_ignore = True
            self._last_formula_fn()
            self._undo_ignore = False

    def _enter_generieren(self) -> None:
        if self._last_formula_fn is None: return
        self._register_and_set(self._last_formula_fn)
        self._status_bar.showMessage(self.tr("status_generated"), Config.MSG_SHORT)

    def _add_to_history(self, formel: str) -> None:
        self._verlauf = [f for f in self._verlauf if f != formel]
        self._verlauf.insert(0, formel)
        self._verlauf = self._verlauf[:Config.HISTORY_MAX]
        save_history(self._verlauf)
        self._update_history_list()

    # -----------------------------------------------------------------------
    # UI aufbauen
    # -----------------------------------------------------------------------
    def _erstelle_ui(self) -> None:
        self.setWindowTitle(f"{self.tr('win_title')}  v{APP_VERSION}")
        header = QHBoxLayout()
        header.setSpacing(6)
        title_lbl = QLabel(self.tr("main_title"))
        title_lbl.setFont(_ui_font(self.current_lang, _pt(16), bold=True))
        header.addWidget(title_lbl)
        header.addStretch()
        btn_plugin_mgr = QPushButton() # ⬅️ Das Emoji in den Anführungszeichen wird gelöscht
        btn_plugin_mgr.setIcon(self._icon("Plagin_Manager.png")) # ⬅️ Hier wird dein Icon geladen
        btn_plugin_mgr.setFixedWidth(Config.ICON_BTN_W)
        btn_plugin_mgr.setToolTip("Plugin Manager")
        btn_plugin_mgr.clicked.connect(self._open_plugin_manager)
        header.addWidget(btn_plugin_mgr)
        header.addWidget(btn_plugin_mgr)
        btn_backup = QPushButton()  # ⬅️ Emoji "💾" entfernt
        btn_backup.setIcon(self._icon("backup.png"))  # ⬅️ Backup-Icon zugewiesen
        btn_backup.setFixedWidth(Config.ICON_BTN_W)
        btn_backup.setToolTip("Backup")
        btn_backup.clicked.connect(self._open_backup)
        header.addWidget(btn_backup)

        btn_restore = QPushButton()  # ⬅️ Emoji "🔄" entfernt
        btn_restore.setIcon(self._icon("restore.png"))  # ⬅️ Restore-Icon zugewiesen
        btn_restore.setFixedWidth(Config.ICON_BTN_W)
        btn_restore.setToolTip("Restore")
        btn_restore.clicked.connect(self._open_restore)
        header.addWidget(btn_restore)
        btn_lang_tool = QPushButton()  # ⬅️ Emoji "🌍" entfernt
        btn_lang_tool.setIcon(self._icon("language.png"))  # ⬅️ Neues Icon geladen
        btn_lang_tool.setFixedWidth(Config.ICON_BTN_W)
        btn_lang_tool.setToolTip("Add new language")
        btn_lang_tool.clicked.connect(self._open_language_tool)
        header.addWidget(btn_lang_tool)

        btn_lang_sync = QPushButton()  # ⬅️ Emoji "🔍" entfernt
        btn_lang_sync.setIcon(self._icon("Control_Language.png"))  # ⬅️ Neues Icon geladen
        btn_lang_sync.setFixedWidth(Config.ICON_BTN_W)
        btn_lang_sync.setToolTip("Language code sync check")
        btn_lang_sync.clicked.connect(self._open_lang_sync)
        header.addWidget(btn_lang_sync)
        self._btn_dark = QPushButton()  # ⬅️ Emojis komplett entfernt
        # Wählt das richtige Icon für den Startzustand aus:
        start_icon = "Dark_Mode.png" if not self._dark_mode else "brightness.png"
        self._btn_dark.setIcon(self._icon(start_icon))  # ⬅️ Icon wird geladen
        
        self._btn_dark.setFixedWidth(Config.ICON_BTN_W)
        self._btn_dark.setToolTip(self.tr("tooltip_dark_mode"))
        self._btn_dark.clicked.connect(self._toggle_dark_mode)
        header.addWidget(self._btn_dark)
        btn_admin = QPushButton()  # ⬅️ Emoji "🛠" entfernt
        btn_admin.setIcon(self._icon("admin_Panel.png"))  # ⬅️ Admin-Panel-Icon zugewiesen
        btn_admin.setFixedWidth(Config.ICON_BTN_W)
        btn_admin.setToolTip(self.tr("tooltip_admin_panel"))
        btn_admin.clicked.connect(self._open_admin_panel)
        header.addWidget(btn_admin)
        btn_ref = QPushButton()  # ⬅️ Text entfernt für einheitliches Design
        btn_ref.setIcon(self._icon("Referenz.png"))  # ⬅️ Referenz-Icon geladen
        btn_ref.setFixedWidth(Config.ICON_BTN_W)  # ⬅️ Gleiche Breite wie die anderen Buttons
        btn_ref.setToolTip(self.tr("btn_ref"))  # ⬅️ Text als Tooltip weiterverwenden
        btn_ref.clicked.connect(self.zeige_referenz)
        header.addWidget(btn_ref)

        btn_help = QPushButton()  # ⬅️ Text entfernt
        btn_help.setIcon(self._icon("help.png"))  # ⬅️ Hilfe-Icon geladen
        btn_help.setFixedWidth(Config.ICON_BTN_W)  # ⬅️ Gleiche Breite
        btn_help.setToolTip(self.tr("btn_help"))  # ⬅️ Text als Tooltip weiterverwenden
        btn_help.clicked.connect(self.zeige_hilfe)
        header.addWidget(btn_help)
        lang_codes = list(self.langs.keys())
        lang_names = [self.langs[c]["_meta"]["name"] for c in lang_codes]
        # NEUER BLOCK: Lädt Flaggen-Bilder statt Emojis
        from PyQt5.QtGui import QIcon, QPixmap
        import os
        
        self.lang_combo = QComboBox()
        self.lang_combo.setStyleSheet("QComboBox { font-size: 12px; } QComboBox QAbstractItemView { font-size: 12px; }")
        mapping = {
            "en": "us",    "cs": "cz",    "da": "dk",    "el": "gr",
            "nn": "no",    "nb": "no",    "uk": "ua",    "zh-CN": "cn",
            "ja": "jp",    "ko": "kr",    "hi": "in",    "pt-BR": "br",
            "he": "il",    "fa": "ir"
        }
        # Pfad zu deinen Flaggen-Bildern (Ordner: assets/flags/)
        # Stelle sicher, dass die Bilder so heißen wie deine Sprachcodes (de.png, en.png, etc.)
        base_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Dynamische Suche nach Bildern
        for code in lang_codes:
            image_code = mapping.get(code, code)
            name = self.langs[code]["_meta"]["name"]
            
            display_name = name.partition(" ")[2] or name
            
            
            icon_path = os.path.join(base_dir, "assets", "flags", f"{image_code}.png")
            if os.path.exists(icon_path):
                pixmap = QPixmap(icon_path)
                icon = QIcon(pixmap)
            else:
                # Fallback: Falls mal ein Bild fehlt, kein Fehler, sondern ein leeres Icon
                icon = QIcon() 
            
            self.lang_combo.addItem(icon, display_name)
            parts = name.split(" ", 1)
            display_name = parts[1] if len(parts) > 1 else name
        
        # Den aktuellen Index wie gewohnt setzen
        current_idx = lang_codes.index(self.current_lang) if self.current_lang in lang_codes else 0
        self.lang_combo.setCurrentIndex(current_idx)
        
        # Breite dynamisch anpassen, damit genug Platz für Bild + Text ist
        self.lang_combo.setMinimumWidth(_pt(150))
        self.lang_combo.currentIndexChanged.connect(self._on_lang_change)
        header.addWidget(self.lang_combo)
        self._root_layout.addLayout(header)
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        self._root_layout.addWidget(line)
        grid = QGridLayout()
        grid.setSpacing(6)
        grid.setColumnStretch(1, 1)
        grid.addWidget(QLabel(self.tr("lbl_range")), 0, 0)
        br_row = QHBoxLayout()
        br_row.setSpacing(4)
        self.bereich_entry = QLineEdit("A1:A10")
        br_row.addWidget(self.bereich_entry)
        self._ddl_br = QComboBox()
        self._ddl_br.addItems(["A1", "$A1", "A$1", "$A$1"])
        self._ddl_br.setFixedWidth(Config.CELL_FIELD_W)
        self._ddl_br.setToolTip(self.tr("ddl_abs_tooltip"))
        br_row.addWidget(self._ddl_br)
        br_container = QWidget(); br_container.setLayout(br_row)
        grid.addWidget(br_container, 0, 1, 1, 2)
        grid.addWidget(QLabel(self.tr("lbl_range2")), 1, 0)
        br2_row = QHBoxLayout()
        br2_row.setSpacing(4)
        self.bereich2_entry = QLineEdit("B1:B10")
        br2_row.addWidget(self.bereich2_entry)
        self._ddl_br2 = QComboBox()
        self._ddl_br2.addItems(["B1", "$B1", "B$1", "$B$1"])
        self._ddl_br2.setFixedWidth(Config.CELL_FIELD_W)
        self._ddl_br2.setToolTip(self.tr("ddl_abs_tooltip2"))
        br2_row.addWidget(self._ddl_br2)
        br2_container = QWidget(); br2_container.setLayout(br2_row)
        grid.addWidget(br2_container, 1, 1, 1, 2)
        grid.addWidget(QLabel(self.tr("lbl_cell1")), 2, 0)
        cell_row = QHBoxLayout()
        cell_row.setSpacing(4)
        self.zelle1_entry = QLineEdit("A1")
        self.zelle1_entry.setFixedWidth(Config.CELL_FIELD_W)
        cell_row.addWidget(self.zelle1_entry)
        self._ddl_z1 = QComboBox()
        self._ddl_z1.addItems(["A1", "$A1", "A$1", "$A$1"])
        self._ddl_z1.setFixedWidth(Config.CELL_FIELD_W)
        self._ddl_z1.setToolTip(self.tr("ddl_abs_tooltip"))
        cell_row.addWidget(self._ddl_z1)
        cell_row.addStretch()
        lbl_c2 = QLabel(self.tr("lbl_cell2"))
        cell_row.addWidget(lbl_c2)
        self.zelle2_entry = QLineEdit("B1")
        self.zelle2_entry.setFixedWidth(Config.CELL_FIELD_W)
        cell_row.addWidget(self.zelle2_entry)
        self._ddl_z2 = QComboBox()
        self._ddl_z2.addItems(["B1", "$B1", "B$1", "$B$1"])
        self._ddl_z2.setFixedWidth(Config.CELL_FIELD_W)
        self._ddl_z2.setToolTip(self.tr("ddl_abs_tooltip2"))
        cell_row.addWidget(self._ddl_z2)
        cell_container = QWidget(); cell_container.setLayout(cell_row)
        grid.addWidget(cell_container, 2, 1, 1, 2)
        self.param_entry = self._add_field(grid, self.tr("lbl_param"), 3, "2")
        self._root_layout.addLayout(grid)
        self.notebook = QTabWidget()
        self.notebook.currentChanged.connect(self._update_explanation)
        self._root_layout.addWidget(self.notebook, stretch=1)
        self._tab_grundfunktionen()
        self._tab_erweitert()
        self._tab_datum_text()
        self._tab_nachschlagen_runden()
        self._tab_plugins()
        self._setup_footer()
        self._attach_validators()

    def _add_field(self, grid: QGridLayout, txt: str, row: int, default: str) -> QLineEdit:
        grid.addWidget(QLabel(txt), row, 0)
        entry = QLineEdit(default)
        grid.addWidget(entry, row, 1, 1, 2)
        return entry

    # -----------------------------------------------------------------------
    # Eingabe-Validierung
    # -----------------------------------------------------------------------
    _COL_MAX  = 16_384
    _ROW_MAX  = 1_048_576
    _CELL_RE  = re.compile(r'([A-Za-z]{1,3})([0-9]{1,7})')
    _RANGE_RE = re.compile(r'([A-Za-z]{1,3})([0-9]{1,7}):([A-Za-z]{1,3})([0-9]{1,7})')

    @staticmethod
    def _err_style(widget: str = "QLineEdit") -> str:
        return (
            f"{widget} {{ "
            f"background-color: {THEME['ui_err_bg']}; "
            f"border: 1.5px solid {THEME['ui_err_border']}; "
            f"}}"
        )

    @classmethod
    def _col_to_num(cls, col: str) -> int:
        num = 0
        for ch in col.upper():
            num = num * 26 + (ord(ch) - ord('A') + 1)
        return num

    @classmethod
    def _valid_cell(cls, text: str, tr=None) -> "tuple[bool, str]":
        def _t(key, **kwargs):
            if tr:
                msg = tr(key)
                return msg.format(**kwargs) if kwargs else msg
            msg = FALLBACK_MESSAGES.get(key, key)
            return msg.format(**kwargs) if kwargs else msg
        m = cls._CELL_RE.fullmatch(text.strip().upper())
        if not m: return False, _t("err_invalid_cell")
        col, row = m.group(1), int(m.group(2))
        col_num = cls._col_to_num(col)
        if col_num > cls._COL_MAX: return False, _t("err_col_overflow", col=col, max=cls._COL_MAX)
        if row == 0: return False, _t("err_row_zero")
        if row > cls._ROW_MAX: return False, _t("err_row_overflow", row=row, max=cls._ROW_MAX)
        return True, ""

    @classmethod
    def _valid_range(cls, text: str, tr=None) -> "tuple[bool, str]":
        def _t(key, **kwargs):
            if tr:
                msg = tr(key)
                return msg.format(**kwargs) if kwargs else msg
            msg = FALLBACK_MESSAGES.get(key, key)
            return msg.format(**kwargs) if kwargs else msg
        m = cls._RANGE_RE.fullmatch(text.strip().upper())
        if not m: return False, _t("err_invalid_range")
        col1, row1 = m.group(1), int(m.group(2))
        col2, row2 = m.group(3), int(m.group(4))
        col1_num = cls._col_to_num(col1)
        col2_num = cls._col_to_num(col2)
        if col1_num > cls._COL_MAX or col2_num > cls._COL_MAX:
            bad = col1 if col1_num > cls._COL_MAX else col2
            return False, _t("err_range_col_overflow", col=bad, max=cls._COL_MAX)
        if row1 == 0 or row2 == 0: return False, _t("err_range_row_zero")
        if row1 > cls._ROW_MAX or row2 > cls._ROW_MAX:
            return False, _t("err_range_row_overflow", row=max(row1, row2), max=cls._ROW_MAX)
        if col1_num > col2_num: return False, _t("err_range_col_order", c1=col1, c2=col2)
        if row1 > row2: return False, _t("err_range_row_order", r1=row1, r2=row2)
        return True, ""

    def _set_preview_tooltip(self, btn: "QPushButton", formula_fn: "callable") -> None:
        class _HoverFilter(QObject):
            def __init__(self_, parent_btn, fn, outer):
                super().__init__()
                self_._fn = fn; self_._btn = parent_btn; self_._outer = outer
            def eventFilter(self_, obj, event):
                from PyQt5.QtCore import QEvent
                if obj is self_._btn and event.type() == QEvent.Enter:
                    try: preview = self_._fn()
                    except Exception as e:
                        _get_logger().debug("Formel-Vorschau: %s", e); preview = "–"
                    self_._btn.setToolTip(f"<b>{self_._outer.tr('tooltip_preview')}</b><br><code>{preview}</code>")
                return False
        filt = _HoverFilter(btn, formula_fn, self)
        btn.installEventFilter(filt)
        if not hasattr(btn, "_hover_filters"):
            btn._hover_filters = []
        btn._hover_filters.append(filt)

    def _inputs_valid(self) -> bool:
        checks = [
            (self._valid_range, self.bereich_entry.text()),
            (self._valid_range, self.bereich2_entry.text()),
            (self._valid_cell,  self.zelle1_entry.text()),
            (self._valid_cell,  self.zelle2_entry.text()),
        ]
        for check_fn, text in checks:
            t = text.strip()
            if t:
                ok, _ = check_fn(t)
                if not ok: return False
        return True

    def _attach_validators(self) -> None:
        def _make(check_fn, field):
            def _on_change(text):
                t = text.strip()
                if not t:
                    field.setStyleSheet(""); field.setToolTip(""); return
                ok, msg = check_fn(t)
                field.setStyleSheet("" if ok else self._err_style("QLineEdit"))
                field.setToolTip("" if ok else f"⚠ {msg}")
            return _on_change
        self.bereich_entry .textChanged.connect(_make(lambda t: self._valid_range(t, self.tr), self.bereich_entry))
        self.bereich2_entry.textChanged.connect(_make(lambda t: self._valid_range(t, self.tr), self.bereich2_entry))
        self.zelle1_entry  .textChanged.connect(_make(lambda t: self._valid_cell(t, self.tr),  self.zelle1_entry))
        self.zelle2_entry  .textChanged.connect(_make(lambda t: self._valid_cell(t, self.tr),  self.zelle2_entry))
        self.bereich_entry .textChanged.connect(self._live_refresh)
        self.bereich2_entry.textChanged.connect(self._live_refresh)
        self.zelle1_entry  .textChanged.connect(self._live_refresh)
        self.zelle2_entry  .textChanged.connect(self._live_refresh)
        self.param_entry   .textChanged.connect(self._live_refresh)
        self._ddl_br .currentIndexChanged.connect(self._live_refresh)
        self._ddl_br2.currentIndexChanged.connect(self._live_refresh)
        self._ddl_z1 .currentIndexChanged.connect(self._live_refresh)
        self._ddl_z2 .currentIndexChanged.connect(self._live_refresh)
        for field in (self.bereich_entry, self.bereich2_entry,
                      self.zelle1_entry, self.zelle2_entry, self.param_entry):
            field.returnPressed.connect(self._enter_generieren)

    # -----------------------------------------------------------------------
    # Formel-Validierung im Output-Feld
    # -----------------------------------------------------------------------
    _RANGE_CANDIDATE = re.compile(r'[\$A-Za-z0-9]+:[\$A-Za-z0-9]+')
    _VALID_RANGE_OUT = re.compile(r'\$?[A-Za-z]+\$?[0-9]+:\$?[A-Za-z]+\$?[0-9]+')

    @classmethod
    def _formula_ok(cls, text: str) -> bool:
        text = text.strip()
        if not text: return True
        depth = 0; in_str = False
        for ch in text:
            if ch == '"': in_str = not in_str
            if in_str: continue
            if ch == '(': depth += 1
            elif ch == ')':
                depth -= 1
                if depth < 0: return False
        if depth != 0 or in_str: return False
        clean = re.sub(r'"[^"]*"', '"', text)
        for m in cls._RANGE_CANDIDATE.finditer(clean):
            token = m.group()
            if not cls._VALID_RANGE_OUT.fullmatch(token): return False
            plain = token.replace("$", "")
            ok, _ = cls._valid_range(plain)
            if not ok: return False
        return True

    def _validate_output_brackets(self):
        ok = self._formula_ok(self.output_entry.toPlainText())
        self.output_entry.setStyleSheet("" if ok else self._err_style("QTextEdit"))

    # -----------------------------------------------------------------------
    # TAB 1: Grundfunktionen
    # -----------------------------------------------------------------------
    def _tab_grundfunktionen(self):
        t = QWidget()
        layout = QVBoxLayout(t)
        layout.setSpacing(8)
        lbl_arith = QLabel(self.tr("sec_arithmetic"))
        lbl_arith.setFont(_ui_font(self.current_lang, _pt(9), bold=True))
        layout.addWidget(lbl_arith)
        row_arith = QHBoxLayout()
        for op in ["+", "-", "*", "/", "^"]:
            btn = QPushButton(op)
            btn.setFixedWidth(Config.OP_BTN_W)
            btn.clicked.connect(lambda checked, o=op: self.op_einfach(o))
            self._set_preview_tooltip(btn, lambda o=op: f"={self.z1()}{o}{self.z2()}")
            row_arith.addWidget(btn)
        row_arith.addStretch()
        layout.addLayout(row_arith)
        lbl_stat = QLabel(self.tr("sec_statistics"))
        lbl_stat.setFont(_ui_font(self.current_lang, _pt(9), bold=True))
        layout.addWidget(lbl_stat)
        stat_grid = QGridLayout()
        stat_grid.setSpacing(4)
        stat_keys = ["f_sum", "f_avg", "f_min", "f_max", "f_count", "f_count2", "f_median"]
        for i, k in enumerate(stat_keys):
            btn = QPushButton(self.tr(k))
            btn.clicked.connect(lambda checked, key=k: self.op_bereich(self.tr(key)))
            self._set_preview_tooltip(btn, lambda key=k: f"={self.tr(key)}({self.br()})")
            stat_grid.addWidget(btn, i // 4, i % 4)
        btn_sp = QPushButton(self.tr("f_sumprod"))
        btn_sp.clicked.connect(self.op_sumprod)
        self._set_preview_tooltip(btn_sp, lambda: f"={self.tr('f_sumprod')}({self.br()};{self.br2()})")
        stat_grid.addWidget(btn_sp, 1, 3)
        layout.addLayout(stat_grid)
        layout.addStretch()
        self.notebook.addTab(t, self.tr("tab_basic"))

    # -----------------------------------------------------------------------
    # TAB 2: Erweitert
    # -----------------------------------------------------------------------
    def _tab_erweitert(self):
        t = QWidget()
        layout = QVBoxLayout(t)
        layout.setSpacing(8)
        lbl_logic = QLabel(self.tr("sec_logic"))
        lbl_logic.setFont(_ui_font(self.current_lang, _pt(9), bold=True))
        layout.addWidget(lbl_logic)
        row_logic = QHBoxLayout()
        _logic_previews = {
            "f_if":  lambda: f'={self.tr("f_if")}({self.z1()}>0;"{self.tr("formula_ok")}";"{self.tr("formula_fehler")}")',
            "f_and": lambda: f'={self.tr("f_and")}({self.z1()}>0;{self.z2()}>0)',
            "f_or":  lambda: f'={self.tr("f_or")}({self.z1()}>0;{self.z2()}>0)',
            "f_not": lambda: f'={self.tr("f_not")}({self.z1()}>0)',
        }
        for k in ["f_if", "f_and", "f_or", "f_not"]:
            btn = QPushButton(self.tr(k))
            btn.clicked.connect(getattr(self, "call_" + k))
            self._set_preview_tooltip(btn, _logic_previews[k])
            row_logic.addWidget(btn)
        row_logic.addStretch()
        layout.addLayout(row_logic)
        lbl_cond = QLabel(self.tr("sec_conditional"))
        lbl_cond.setFont(_ui_font(self.current_lang, _pt(9), bold=True))
        layout.addWidget(lbl_cond)
        _cond_previews = {
            "f_sumif":      lambda: f'={self.tr("f_sumif")}({self.br()};">10";{self.br()})',
            "f_countif":    lambda: f'={self.tr("f_countif")}({self.br()};"{self.tr("formula_value")}")',
            "f_avgif":      lambda: f'={self.tr("f_avgif")}({self.br()};">0";{self.br()})',
            "f_sumifs":     lambda: f'={self.tr("f_sumifs")}({self.br()};{self.br2()};">10")',
            "f_stdev":      lambda: f'={self.tr("f_stdev")}({self.br()})',
            "f_var":        lambda: f'={self.tr("f_var")}({self.br()})',
            "f_countblank": lambda: f'={self.tr("f_countblank")}({self.br()})',
            "f_large":      lambda: f'={self.tr("f_large")}({self.br()};{self.pa()})',
        }
        cond_grid = QGridLayout()
        cond_grid.setSpacing(4)
        cond_keys = ["f_sumif", "f_countif", "f_avgif", "f_sumifs",
                     "f_stdev", "f_var", "f_countblank", "f_large"]
        for i, k in enumerate(cond_keys):
            btn = QPushButton(self.tr(k))
            btn.clicked.connect(getattr(self, "call_" + k))
            self._set_preview_tooltip(btn, _cond_previews[k])
            cond_grid.addWidget(btn, i // 4, i % 4)
        layout.addLayout(cond_grid)
        layout.addStretch()
        self.notebook.addTab(t, self.tr("tab_adv"))

    # -----------------------------------------------------------------------
    # TAB 3: Datum & Text
    # -----------------------------------------------------------------------
    def _tab_datum_text(self):
        t = QWidget()
        layout = QVBoxLayout(t)
        layout.setSpacing(8)
        date_grid = QGridLayout()
        date_grid.setSpacing(4)
        _date_previews = {
            "f_today":   lambda: f'={self.tr("f_today")}()',
            "f_now":     lambda: f'={self.tr("f_now")}()',
            "f_year":    lambda: f'={self.tr("f_year")}({self.z1()})',
            "f_month":   lambda: f'={self.tr("f_month")}({self.z1()})',
            "f_day":     lambda: f'={self.tr("f_day")}({self.z1()})',
            "f_date":    lambda: f'={self.tr("f_date")}({datetime.date.today().year};1;1)',
            "f_datedif": lambda: f'={self.tr("f_datedif")}({self.z1()};{self.z2()};"D")',
            "f_weekday": lambda: f'={self.tr("f_weekday")}({self.z1()};2)',
        }
        date_keys = ["f_today", "f_now", "f_year", "f_month",
                     "f_day", "f_date", "f_datedif", "f_weekday"]
        for i, k in enumerate(date_keys):
            btn = QPushButton(self.tr(k))
            btn.clicked.connect(getattr(self, "call_" + k))
            self._set_preview_tooltip(btn, _date_previews[k])
            date_grid.addWidget(btn, i // 4, i % 4)
        layout.addLayout(date_grid)
        lbl_text = QLabel(self.tr("sec_text"))
        lbl_text.setFont(_ui_font(self.current_lang, _pt(9), bold=True))
        layout.addWidget(lbl_text)
        text_grid = QGridLayout()
        text_grid.setSpacing(4)
        _text_previews = {
            "f_concat": lambda: f'={self.tr("f_concat")}({self.z1()};" ";{self.z2()})',
            "f_len":    lambda: f'={self.tr("f_len")}({self.z1()})',
            "f_left":   lambda: f'={self.tr("f_left")}({self.z1()};{self.pa()})',
            "f_right":  lambda: f'={self.tr("f_right")}({self.z1()};{self.pa()})',
            "f_mid":    lambda: f'={self.tr("f_mid")}({self.z1()};1;{self.pa()})',
            "f_upper":  lambda: f'={self.tr("f_upper")}({self.z1()})',
            "f_lower":  lambda: f'={self.tr("f_lower")}({self.z1()})',
            "f_trim":   lambda: f'={self.tr("f_trim")}({self.z1()})',
        }
        text_keys = ["f_concat", "f_len", "f_left", "f_right",
                     "f_mid", "f_upper", "f_lower", "f_trim"]
        for i, k in enumerate(text_keys):
            btn = QPushButton(self.tr(k))
            btn.clicked.connect(getattr(self, "call_" + k))
            self._set_preview_tooltip(btn, _text_previews[k])
            text_grid.addWidget(btn, i // 4, i % 4)
        layout.addLayout(text_grid)
        layout.addStretch()
        self.notebook.addTab(t, self.tr("tab_dt"))

    # -----------------------------------------------------------------------
    # TAB 4: Nachschlagen & Runden
    # -----------------------------------------------------------------------
    def _tab_nachschlagen_runden(self):
        t = QWidget()
        layout = QVBoxLayout(t)
        layout.setSpacing(8)
        look_row = QHBoxLayout()
        _look_previews = {
            "f_vlookup": lambda: f'={self.tr("f_vlookup")}({self.z1()};{self.br()};{self.pa()};0)',
            "f_hlookup": lambda: f'={self.tr("f_hlookup")}({self.z1()};{self.br()};{self.pa()};0)',
            "f_index":   lambda: f'={self.tr("f_index")}({self.br()};{self.pa()};1)',
            "f_match":   lambda: f'={self.tr("f_match")}({self.z1()};{self.br()};0)',
        }
        for k in ["f_vlookup", "f_hlookup", "f_index", "f_match"]:
            btn = QPushButton(self.tr(k))
            btn.clicked.connect(getattr(self, "call_" + k))
            self._set_preview_tooltip(btn, _look_previews[k])
            look_row.addWidget(btn)
        layout.addLayout(look_row)
        btn_idxm = QPushButton(self.tr("btn_idx_match"))
        btn_idxm.clicked.connect(self.call_idx_match)
        self._set_preview_tooltip(btn_idxm,
            lambda: f'={self.tr("f_index")}({self.br2()};{self.tr("f_match")}({self.z1()};{self.br()};0))')
        layout.addWidget(btn_idxm)
        lbl_round = QLabel(self.tr("sec_round"))
        lbl_round.setFont(_ui_font(self.current_lang, _pt(9), bold=True))
        layout.addWidget(lbl_round)
        math_grid = QGridLayout()
        math_grid.setSpacing(4)
        _math_previews = {
            "f_round":     lambda: f'={self.tr("f_round")}({self.z1()};{self.pa()})',
            "f_roundup":   lambda: f'={self.tr("f_roundup")}({self.z1()};{self.pa()})',
            "f_rounddown": lambda: f'={self.tr("f_rounddown")}({self.z1()};{self.pa()})',
            "f_int":       lambda: f'={self.tr("f_int")}({self.z1()})',
            "f_trunc":     lambda: f'={self.tr("f_trunc")}({self.z1()};{self.pa()})',
            "f_abs":       lambda: f'={self.tr("f_abs")}({self.z1()})',
            "f_mod":       lambda: f'={self.tr("f_mod")}({self.z1()};{self.pa()})',
            "f_sqrt":      lambda: f'={self.tr("f_sqrt")}({self.z1()})',
            "f_rand":      lambda: f'={self.tr("f_rand")}()',
        }
        math_keys = ["f_round", "f_roundup", "f_rounddown", "f_int",
                     "f_trunc", "f_abs", "f_mod", "f_sqrt", "f_rand"]
        for i, k in enumerate(math_keys):
            btn = QPushButton(self.tr(k))
            btn.clicked.connect(getattr(self, "call_" + k))
            self._set_preview_tooltip(btn, _math_previews[k])
            math_grid.addWidget(btn, i // 4, i % 4)
        layout.addLayout(math_grid)
        layout.addStretch()
        self.notebook.addTab(t, self.tr("tab_look"))

    # -----------------------------------------------------------------------
    # Plugin-Tabs
    # -----------------------------------------------------------------------
    def _tab_plugins(self) -> None:
        if not self._plugins:
            return
        container = QWidget()
        outer = QVBoxLayout(container)
        outer.setContentsMargins(6, 6, 6, 6)
        outer.setSpacing(4)
        splitter = QSplitter(Qt.Horizontal)
        splitter.setHandleWidth(4)
        left = QWidget()
        left_layout = QVBoxLayout(left)
        left_layout.setContentsMargins(0, 0, 0, 0)
        left_layout.setSpacing(2)
        list_lbl = QLabel(self.tr("plugin_manager_list") or "Plugins")
        list_lbl.setFont(_ui_font(self.current_lang, _pt(9), bold=True))
        left_layout.addWidget(list_lbl)
        self._plugin_list_widget = QListWidget()
        self._plugin_list_widget.setFixedWidth(170)
        self._plugin_list_widget.setSpacing(2)
        for plugin in self._plugins:
            label = f"{plugin.icon}  {plugin.name}" if plugin.icon else plugin.name
            item = QListWidgetItem(label)
            item.setToolTip(plugin.description)
            self._plugin_list_widget.addItem(item)
        left_layout.addWidget(self._plugin_list_widget)
        splitter.addWidget(left)
        self._plugin_stack = QStackedWidget()
        for plugin in self._plugins:
            page = self._build_plugin_page(plugin)
            self._plugin_stack.addWidget(page)
        splitter.addWidget(self._plugin_stack)
        splitter.setStretchFactor(0, 0)
        splitter.setStretchFactor(1, 1)
        outer.addWidget(splitter)
        self._plugin_tab_index = self.notebook.count()
        self.notebook.addTab(container, self._icon("Plugin.png"), self.tr("plugin_manager_tab") or "Plugins")
        self._plugin_list_widget.setCurrentRow(0)
        self._plugin_list_widget.currentRowChanged.connect(
            self._plugin_stack.setCurrentIndex
        )

    def _build_plugin_page(self, plugin) -> "QWidget":
        from collections import defaultdict
        container = QWidget()
        outer = QVBoxLayout(container)
        outer.setContentsMargins(8, 6, 8, 6)
        outer.setSpacing(6)
        header_lbl = QLabel(
            f"<b>{plugin.icon} {plugin.name}</b>" if plugin.icon
            else f"<b>{plugin.name}</b>"
        )
        header_lbl.setTextFormat(Qt.RichText)
        outer.addWidget(header_lbl)
        if plugin.description:
            desc_lbl = QLabel(plugin.description)
            desc_lbl.setWordWrap(True)
            desc_lbl.setStyleSheet("color: gray; font-style: italic;")
            outer.addWidget(desc_lbl)
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        outer.addWidget(line)
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.NoFrame)
        inner_widget = QWidget()
        inner = QVBoxLayout(inner_widget)
        inner.setSpacing(4)
        inner.setContentsMargins(0, 0, 0, 0)
        kategorien: dict = defaultdict(list)
        no_cat = self.tr("plugin_no_category") or "Allgemein"
        for f in plugin.formulas:
            kat = f.category if f.category else no_cat
            kategorien[kat].append(f)

        for kat_name, formeln in kategorien.items():
            # ── Kategorie-Label MIT Anzahl ──────────────────────────────────
            kat_lbl = QLabel(f"── {kat_name} ({len(formeln)}) ──")
            kat_lbl.setFont(_ui_font(self.current_lang, _pt(9), bold=True))
            kat_lbl.setStyleSheet(
                f"color: {THEME.get('hl_function', '#4a90d9')};"
            )
            inner.addWidget(kat_lbl)
            for formel_entry in formeln:
                inner.addWidget(self._build_formula_row(formel_entry))

        inner.addStretch()
        scroll.setWidget(inner_widget)
        outer.addWidget(scroll)
        info_parts = []
        if plugin.author:
            info_parts.append(f"✍ {plugin.author}")
        info_parts.append(f"v{plugin.version}")
        footer_lbl = QLabel("  |  ".join(info_parts))
        footer_lbl.setStyleSheet("color: gray; font-size: 8pt;")
        outer.addWidget(footer_lbl)
        return container

    def _build_formula_row(self, formel_entry) -> "QWidget":
        """
        Formel-Zeile mit Name (fett) + Beschreibung (darunter, grau) + Formel + Button.
        """
        outer = QWidget()
        outer_l = QVBoxLayout(outer)
        outer_l.setContentsMargins(4, 3, 4, 3)
        outer_l.setSpacing(2)

        # ── Obere Zeile: Name | Formel | Button ──────────────────────────────
        row = QWidget()
        hl = QHBoxLayout(row)
        hl.setContentsMargins(0, 0, 0, 0)
        hl.setSpacing(8)

        name_lbl = QLabel(f"<b>{formel_entry.name}</b>")
        name_lbl.setMinimumWidth(160)
        name_lbl.setTextFormat(Qt.RichText)
        hl.addWidget(name_lbl, stretch=1)

        formel_lbl = QLineEdit(formel_entry.formula)
        formel_lbl.setReadOnly(True)
        formel_lbl.setFont(QFont(Config.FONT_MONO, _pt(9)))
        formel_lbl.setStyleSheet(
            "background: rgba(128,128,128,0.12);"
            "padding: 2px 6px; border-radius: 3px; border: none;"
        )
        formel_lbl.setCursorPosition(0)
        formel_lbl.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        hl.addWidget(formel_lbl, stretch=2)

        use_label = self.tr("plugin_use_formula") or "Übernehmen"
        btn = QPushButton(f"▶ {use_label}")
        btn.setFixedWidth(120)
        btn.setToolTip(self.tr("plugin_use_formula_tooltip") or "Formel ins Ausgabefeld übernehmen")
        btn.clicked.connect(
            lambda _, f=formel_entry.formula: self._plugin_formel_uebernehmen(f)
        )
        hl.addWidget(btn)
        outer_l.addWidget(row)

        # ── Untere Zeile: Beschreibung (nur wenn vorhanden) ──────────────────
        if formel_entry.description:
            desc_lbl = QLabel(formel_entry.description)
            desc_lbl.setWordWrap(True)
            desc_lbl.setStyleSheet(
                f"color: {'#aaaaaa' if self._dark_mode else '#666666'};"
                "font-size: 8pt; padding-left: 4px;"
            )
            desc_lbl.setTextInteractionFlags(Qt.TextSelectableByMouse)
            outer_l.addWidget(desc_lbl)

        return outer

    def _plugin_formel_uebernehmen(self, formel: str) -> None:
        self.set_o(formel)
        self._add_to_history(formel)
        msg = self.tr("plugin_formula_used") or "Plugin-Formel übernommen"
        self._status_bar.showMessage(msg, Config.MSG_SHORT)

    # -----------------------------------------------------------------------
    # Formel-Erklärung
    # -----------------------------------------------------------------------
    _EXAMPLE_VALS: "list[int] | None" = None

    def _get_example_vals(self, n: int) -> list:
        import random
        if CalcFormelHelper._EXAMPLE_VALS is None or len(CalcFormelHelper._EXAMPLE_VALS) < n:
            rng = random.Random(42 + n)
            CalcFormelHelper._EXAMPLE_VALS = [rng.randint(1, 9) for _ in range(20)]
        return CalcFormelHelper._EXAMPLE_VALS[:n]

    def _parse_range(self, ref: str) -> "tuple[str,int,str,int] | None":
        plain = ref.replace("$", "").upper().strip()
        m = re.fullmatch(r'([A-Z]{1,3})([0-9]{1,7}):([A-Z]{1,3})([0-9]{1,7})', plain)
        if not m: return None
        return m.group(1), int(m.group(2)), m.group(3), int(m.group(4))

    def _expl(self, key: str, **kwargs) -> str:
        lang_data = self._expl_strings.get(self.current_lang) or self._expl_strings.get("de", {})
        text = lang_data.get(key, self._expl_strings.get("de", {}).get(key, key))
        return text.format(**kwargs) if kwargs else text

    def _load_expl_strings(self) -> dict:
        for search_dir in [LANGUAGE_DIR, DATA_DIR, RESOURCE_DIR]:
            path = search_dir / "formula_explanations.json"
            if path.exists():
                try:
                    raw = json.loads(path.read_text(encoding="utf-8"))
                    return {k: v for k, v in raw.items() if not k.startswith("_")}
                except Exception:
                    pass
        return {"de": {}}

    def _build_explanation(self, formula: str) -> str:
        f = formula.strip()
        if not f.startswith("="): return ""
        body = f[1:]
        arith = re.fullmatch(
            r'\$?([A-Z]{1,3})\$?([0-9]{1,7})'
            r'([+\-*/^])'
            r'\$?([A-Z]{1,3})\$?([0-9]{1,7})',
            body.upper()
        )
        if arith:
            c1 = arith.group(1) + arith.group(2)
            op = arith.group(3)
            c2 = arith.group(4) + arith.group(5)
            v1, v2 = self._get_example_vals(2)
            op_symbols = {'+': '+', '-': '-', '*': '×', '/': '÷', '^': '^'}
            try:
                if   op == '+': res = v1 + v2
                elif op == '-': res = v1 - v2
                elif op == '*': res = v1 * v2
                elif op == '/': res = f"{v1/v2:.2f}".rstrip('0').rstrip('.')
                elif op == '^': res = v1 ** v2
                else:           res = "?"
            except ZeroDivisionError:
                res = "∞"
            sym = op_symbols.get(op, op)
            return (self._expl("arith_line1", c1=c1, v1=v1, c2=c2, v2=v2) + "\n"
                    + self._expl("arith_line2", v1=v1, sym=sym, v2=v2, res=res))
        m_fn = re.match(r'([\w]{2,20})\((.+)\)$', body.upper(), re.UNICODE)
        if not m_fn: return ""
        func_raw = m_fn.group(1)
        args_raw = m_fn.group(2)
        lang_data = self.langs.get(self.current_lang, {})
        func_canon = None
        for key in ("f_sum","f_avg","f_min","f_max","f_count","f_count2",
                    "f_median","f_sumprod",
                    "f_if","f_and","f_or","f_not",
                    "f_sumif","f_countif","f_avgif","f_sumifs",
                    "f_stdev","f_var","f_countblank","f_large",
                    "f_today","f_now","f_year","f_month","f_day",
                    "f_date","f_datedif","f_weekday",
                    "f_concat","f_len","f_left","f_right",
                    "f_mid","f_upper","f_lower","f_trim",
                    "f_vlookup","f_hlookup","f_index","f_match",
                    "f_round","f_roundup","f_rounddown","f_int",
                    "f_trunc","f_abs","f_mod","f_sqrt","f_rand"):
            translated = self.tr(key).upper()
            if translated and func_raw == translated:
                func_canon = key; break
        if func_canon is None: return ""
        _DT_FUNCS = ("f_today","f_now","f_year","f_month","f_day",
                     "f_date","f_datedif","f_weekday",
                     "f_concat","f_len","f_left","f_right",
                     "f_mid","f_upper","f_lower","f_trim")
        if func_canon in _DT_FUNCS:
            return self._build_explanation_dt(func_canon, body)
        _LOOK_FUNCS = ("f_vlookup","f_hlookup","f_index","f_match",
                       "f_round","f_roundup","f_rounddown","f_int",
                       "f_trunc","f_abs","f_mod","f_sqrt","f_rand")
        if func_canon in _LOOK_FUNCS:
            return self._build_explanation_lookup(func_canon, body)
        if func_canon in ("f_if", "f_and", "f_or", "f_not"):
            v1, v2 = self._get_example_vals(2)
            c1 = self.zelle1_entry.text().strip().upper().replace("$", "") or "A1"
            c2 = self.zelle2_entry.text().strip().upper().replace("$", "") or "B1"
            _t  = self._expl("bool_true")
            _f  = self._expl("bool_false")
            if func_canon == "f_if":
                cond = v1 > 0
                result = lang_data.get("formula_ok", "OK") if cond else lang_data.get("formula_fehler", "Fehler")
                bool_val = _t if cond else _f
                return (f"{c1}={v1}\n"
                        + self._expl("if_cond", c1=c1, bool_val=bool_val) + "\n"
                        + self._expl("if_result", result=result))
            elif func_canon == "f_and":
                c1_ok = v1 > 0; c2_ok = v2 > 0
                result = _t if (c1_ok and c2_ok) else _f
                return (self._expl("and_cond",  c1=c1, v1=v1, bool1=_t if c1_ok else _f) + "\n"
                        + self._expl("and_cond2", c2=c2, v2=v2, bool2=_t if c2_ok else _f) + "\n"
                        + self._expl("and_result", result=result))
            elif func_canon == "f_or":
                c1_ok = v1 > 0; c2_ok = v2 > 0
                result = _t if (c1_ok or c2_ok) else _f
                return (self._expl("or_cond",  c1=c1, v1=v1, bool1=_t if c1_ok else _f) + "\n"
                        + self._expl("or_cond2", c2=c2, v2=v2, bool2=_t if c2_ok else _f) + "\n"
                        + self._expl("or_result", result=result))
            elif func_canon == "f_not":
                cond = v1 > 0
                result = _f if cond else _t
                bool_val = _t if cond else _f
                return (f"{c1}={v1}\n"
                        + self._expl("not_cond", c1=c1, bool_val=bool_val) + "\n"
                        + self._expl("not_result", result=result))
        first_arg = args_raw.split(";")[0].strip()
        parsed = self._parse_range(first_arg)
        if parsed is None: return ""
        col1, row1, col2, row2 = parsed
        same_col = (col1 == col2)
        n_cells  = (row2 - row1 + 1) if row2 >= row1 else 0
        if n_cells <= 0 or n_cells > 20: return ""
        vals = self._get_example_vals(n_cells)
        if same_col:
            cell_lines = "\n".join(f"{col1}{row1 + i}={vals[i]}" for i in range(n_cells))
        else:
            cell_lines = f"{col1}{row1}..{col2}{row2} = [{', '.join(str(v) for v in vals)}]"
        if func_canon == "f_sum":
            calc = " + ".join(str(v) for v in vals)
            return f"{cell_lines}\n" + self._expl("sum_line", calc=calc, result=sum(vals))
        elif func_canon == "f_avg":
            avg = sum(vals) / len(vals)
            res_str = f"{avg:.2f}".rstrip('0').rstrip('.')
            return f"{cell_lines}\n" + self._expl("avg_line", terms=' + '.join(str(v) for v in vals), n=n_cells, result=res_str)
        elif func_canon == "f_min":
            return f"{cell_lines}\n" + self._expl("min_line", result=min(vals))
        elif func_canon == "f_max":
            return f"{cell_lines}\n" + self._expl("max_line", result=max(vals))
        elif func_canon == "f_count":
            return f"{cell_lines}\n" + self._expl("count_line", result=n_cells)
        elif func_canon == "f_count2":
            return f"{cell_lines}\n" + self._expl("count2_line", result=n_cells)
        elif func_canon == "f_median":
            s = sorted(vals); mid = n_cells // 2
            med = s[mid] if n_cells % 2 == 1 else f"{(s[mid-1]+s[mid])/2:.1f}".rstrip('0').rstrip('.')
            return (f"{cell_lines}\n"
                    + self._expl("median_sorted", sorted_vals=', '.join(str(v) for v in s)) + "\n"
                    + self._expl("median_line", result=med))
        elif func_canon == "f_sumprod":
            args_list = args_raw.split(";")
            if len(args_list) < 2: return ""
            parsed2 = self._parse_range(args_list[1].strip())
            if parsed2 is None: return ""
            _, row1b, _, row2b = parsed2
            n2 = row2b - row1b + 1
            if n2 <= 0 or n2 > 20: return ""
            vals2 = list(reversed(self._get_example_vals(max(n_cells, n2))))[:n2]
            pairs = list(zip(vals[:n2], vals2))
            prod_str = " + ".join(f"{a}×{b}" for a, b in pairs)
            return (self._expl("sumprod_range1", vals1=', '.join(str(v) for v in vals[:n2])) + "\n"
                    + self._expl("sumprod_range2", vals2=', '.join(str(v) for v in vals2)) + "\n"
                    + self._expl("sumprod_line", prod_str=prod_str, result=sum(a*b for a,b in pairs)))
        elif func_canon == "f_sumif":
            threshold = 3
            matching = [v for v in vals if v > threshold]
            match_str = ", ".join(str(v) for v in matching) or self._expl("sumif_none")
            total = sum(matching)
            return (f"{cell_lines}\n"
                    + self._expl("sumif_cond") + "\n"
                    + self._expl("sumif_match", match_str=match_str) + "\n"
                    + self._expl("sumif_result", total=total))
        elif func_canon == "f_countif":
            target = vals[0]; count = vals.count(target)
            return (f"{cell_lines}\n"
                    + self._expl("countif_search", target=target) + "\n"
                    + self._expl("countif_result", count=count))
        elif func_canon == "f_avgif":
            avg = sum(vals) / len(vals)
            res_str = f"{avg:.2f}".rstrip('0').rstrip('.')
            return (f"{cell_lines}\n"
                    + self._expl("avgif_cond", n=n_cells) + "\n"
                    + self._expl("avgif_result", result=res_str))
        elif func_canon == "f_sumifs":
            vals2_demo = list(reversed(self._get_example_vals(n_cells + 3)))[:n_cells]
            matching = [vals[i] for i in range(n_cells) if vals2_demo[i] > 5]
            total = sum(matching)
            return (self._expl("sumifs_sum_range",  vals=', '.join(str(v) for v in vals)) + "\n"
                    + self._expl("sumifs_crit_range", vals2=', '.join(str(v) for v in vals2_demo)) + "\n"
                    + self._expl("sumifs_cond") + "\n"
                    + self._expl("sumifs_match", matching=str(matching)) + "\n"
                    + self._expl("sumifs_result", total=total))
        elif func_canon == "f_stdev":
            import math
            mean = sum(vals) / n_cells
            variance = sum((v - mean) ** 2 for v in vals) / (n_cells - 1)
            stdev = math.sqrt(variance)
            return (f"{cell_lines}\n"
                    + self._expl("stdev_mean", mean=f"{mean:.2f}") + "\n"
                    + self._expl("stdev_result", result=f"{stdev:.2f}"))
        elif func_canon == "f_var":
            mean = sum(vals) / n_cells
            variance = sum((v - mean) ** 2 for v in vals) / (n_cells - 1)
            return (f"{cell_lines}\n"
                    + self._expl("var_mean", mean=f"{mean:.2f}") + "\n"
                    + self._expl("var_result", result=f"{variance:.2f}"))
        elif func_canon == "f_countblank":
            return (f"{cell_lines}\n"
                    + self._expl("countblank_all", n=n_cells) + "\n"
                    + self._expl("countblank_result"))
        elif func_canon == "f_large":
            try: k = int(self.param_entry.text().strip())
            except ValueError: k = 2
            k = max(1, min(k, n_cells))
            s = sorted(vals, reverse=True)
            return (f"{cell_lines}\n"
                    + self._expl("large_sorted", sorted_vals=', '.join(str(v) for v in s)) + "\n"
                    + self._expl("large_result", k=k, result=s[k-1]))
        return ""

    def _build_explanation_dt(self, func_canon: str, body: str) -> str:
        import math as _math
        today = datetime.date.today()
        c1 = self.zelle1_entry.text().strip().upper().replace("$", "") or "A1"
        c2 = self.zelle2_entry.text().strip().upper().replace("$", "") or "B1"
        try: k = int(self.param_entry.text().strip())
        except ValueError: k = 3
        example_date = datetime.date(today.year - 1, 3, 15)
        example_date2 = today
        WOCHENTAGE = [
            self._expl("weekday_mon"), self._expl("weekday_tue"),
            self._expl("weekday_wed"), self._expl("weekday_thu"),
            self._expl("weekday_fri"), self._expl("weekday_sat"),
            self._expl("weekday_sun"),
        ]
        example_str = self._expl("example_str")
        if func_canon == "f_today":
            return (self._expl("today_desc") + "\n"
                    + self._expl("today_result", date=today.strftime('%d.%m.%Y')))
        elif func_canon == "f_now":
            import datetime as _dt
            now = _dt.datetime.now()
            return (self._expl("now_desc") + "\n"
                    + self._expl("now_result", datetime=now.strftime('%d.%m.%Y %H:%M')))
        elif func_canon == "f_year":
            return (self._expl("year_cell", c1=c1, date=example_date.strftime('%d.%m.%Y')) + "\n"
                    + self._expl("year_result", year=example_date.year))
        elif func_canon == "f_month":
            return (self._expl("month_cell", c1=c1, date=example_date.strftime('%d.%m.%Y')) + "\n"
                    + self._expl("month_result", month=example_date.month))
        elif func_canon == "f_day":
            return (self._expl("day_cell", c1=c1, date=example_date.strftime('%d.%m.%Y')) + "\n"
                    + self._expl("day_result", day=example_date.day))
        elif func_canon == "f_date":
            return (self._expl("date_desc") + "\n"
                    + self._expl("date_example", year=today.year) + "\n"
                    + self._expl("date_result", year=today.year))
        elif func_canon == "f_datedif":
            delta = (example_date2 - example_date).days
            return (self._expl("datedif_c1", c1=c1, date1=example_date.strftime('%d.%m.%Y')) + "\n"
                    + self._expl("datedif_c2", c2=c2, date2=example_date2.strftime('%d.%m.%Y')) + "\n"
                    + self._expl("datedif_result", delta=delta))
        elif func_canon == "f_weekday":
            wd = example_date.weekday()
            return (self._expl("weekday_cell", c1=c1, date=example_date.strftime('%d.%m.%Y')) + "\n"
                    + self._expl("weekday_result", num=wd+1, weekday_name=WOCHENTAGE[wd]))
        elif func_canon == "f_concat":
            v1 = self._expl("concat_example_v1"); v2 = self._expl("concat_example_v2")
            return (self._expl("concat_c1", c1=c1, v1=v1) + "\n"
                    + self._expl("concat_c2", c2=c2, v2=v2) + "\n"
                    + self._expl("concat_result", v1=v1, v2=v2))
        elif func_canon == "f_len":
            return (self._expl("len_cell", c1=c1, text=example_str) + "\n"
                    + self._expl("len_result", count=len(example_str)))
        elif func_canon == "f_left":
            k = max(1, min(k, len(example_str)))
            return (self._expl("left_cell", c1=c1, text=example_str) + "\n"
                    + self._expl("left_desc", k=k) + "\n"
                    + self._expl("left_result", result=example_str[:k]))
        elif func_canon == "f_right":
            k = max(1, min(k, len(example_str)))
            return (self._expl("right_cell", c1=c1, text=example_str) + "\n"
                    + self._expl("right_desc", k=k) + "\n"
                    + self._expl("right_result", result=example_str[-k:]))
        elif func_canon == "f_mid":
            start = 1; k = max(1, min(k, len(example_str)))
            return (self._expl("mid_cell", c1=c1, text=example_str) + "\n"
                    + self._expl("mid_desc", start=start, k=k) + "\n"
                    + self._expl("mid_result", result=example_str[start-1:start-1+k]))
        elif func_canon == "f_upper":
            return (self._expl("upper_cell", c1=c1, text=example_str) + "\n"
                    + self._expl("upper_result", result=example_str.upper()))
        elif func_canon == "f_lower":
            return (self._expl("lower_cell", c1=c1, text=example_str.upper()) + "\n"
                    + self._expl("lower_result", result=example_str.lower()))
        elif func_canon == "f_trim":
            padded = "  " + example_str + "  "
            return (self._expl("trim_cell", c1=c1, text=padded) + "\n"
                    + self._expl("trim_desc") + "\n"
                    + self._expl("trim_result", result=padded.strip()))
        return ""

    def _build_explanation_lookup(self, func_canon: str, body: str) -> str:
        import math as _math
        c1 = self.zelle1_entry.text().strip().upper().replace("$", "") or "A1"
        try: k = int(self.param_entry.text().strip())
        except ValueError: k = 2
        example_num = 3.14159; example_neg = -7.6; example_int = 17
        if func_canon == "f_vlookup":
            return (self._expl("vlookup_c1", c1=c1) + "\n"
                    + self._expl("vlookup_desc1", range=self.br()) + "\n"
                    + self._expl("vlookup_desc2", k=k) + "\n"
                    + self._expl("vlookup_desc3"))
        elif func_canon == "f_hlookup":
            return (self._expl("hlookup_c1", c1=c1) + "\n"
                    + self._expl("hlookup_desc1", range=self.br()) + "\n"
                    + self._expl("hlookup_desc2", k=k) + "\n"
                    + self._expl("hlookup_desc3"))
        elif func_canon == "f_match":
            return (self._expl("match_c1", c1=c1) + "\n"
                    + self._expl("match_desc1", range=self.br()) + "\n"
                    + self._expl("match_desc2") + "\n"
                    + self._expl("match_desc3") + "\n"
                    + self._expl("match_desc4"))
        elif func_canon == "f_index":
            br_ref = self.br()
            return (self._expl("index_desc1", k=k, range=br_ref) + "\n"
                    + self._expl("index_desc2") + "\n"
                    + self._expl("index_desc3", k=k, range=br_ref))
        elif func_canon == "f_round":
            rounded = round(example_num, k)
            return (self._expl("round_cell", c1=c1, num=example_num) + "\n"
                    + self._expl("round_desc", k=k) + "\n"
                    + self._expl("round_result", result=rounded))
        elif func_canon == "f_roundup":
            factor = 10 ** k
            result = _math.ceil(example_num * factor) / factor
            return (self._expl("roundup_cell", c1=c1, num=example_num) + "\n"
                    + self._expl("roundup_desc", k=k) + "\n"
                    + self._expl("roundup_result", result=result))
        elif func_canon == "f_rounddown":
            factor = 10 ** k
            result = _math.floor(example_num * factor) / factor
            return (self._expl("rounddown_cell", c1=c1, num=example_num) + "\n"
                    + self._expl("rounddown_desc", k=k) + "\n"
                    + self._expl("rounddown_result", result=result))
        elif func_canon == "f_int":
            return (self._expl("int_cell", c1=c1, num=example_neg) + "\n"
                    + self._expl("int_desc") + "\n"
                    + self._expl("int_result", result=int(_math.floor(example_neg))))
        elif func_canon == "f_trunc":
            factor = 10 ** k
            result = int(example_num * factor) / factor
            return (self._expl("trunc_cell", c1=c1, num=example_num) + "\n"
                    + self._expl("trunc_desc", k=k) + "\n"
                    + self._expl("trunc_result", result=result))
        elif func_canon == "f_abs":
            return (self._expl("abs_cell", c1=c1, num=example_neg) + "\n"
                    + self._expl("abs_desc") + "\n"
                    + self._expl("abs_result", result=abs(example_neg)))
        elif func_canon == "f_mod":
            result = example_int % k if k != 0 else "∞"
            return (self._expl("mod_cell", c1=c1, num=example_int) + "\n"
                    + self._expl("mod_desc", k=k) + "\n"
                    + self._expl("mod_line", num=example_int, k=k,
                                 quotient=example_int // k if k != 0 else "?", result=result))
        elif func_canon == "f_sqrt":
            val = self._get_example_vals(1)[0] ** 2
            return (self._expl("sqrt_cell", c1=c1, num=val) + "\n"
                    + self._expl("sqrt_desc") + "\n"
                    + self._expl("sqrt_result", num=val, result=int(_math.sqrt(val))))
        elif func_canon == "f_rand":
            import random
            ex = f"{random.uniform(0, 1):.4f}"
            return (self._expl("rand_desc1") + "\n"
                    + self._expl("rand_desc2") + "\n"
                    + self._expl("rand_example", value=ex))
        return ""

    def _update_explanation(self) -> None:
        if not hasattr(self, "_explanation_lbl"): return
        _scroll = getattr(self, "_explanation_scroll", None)
        formula = self.output_entry.toPlainText()
        text = self._build_explanation(formula)
        lbl2 = getattr(self, "_explanation_lbl2", None)
        if text:
            lines = [l for l in text.split("\n") if l.strip()]
            # Alle Zeilen gleichmäßig auf genau 3 Reihen verteilen
            # Aufteilung nach kumulierter Zeichenlänge → beide Hälften gleich breit
            total = sum(len(l) for l in lines)
            rows   = ["", "", ""]
            thirds = [total / 3, 2 * total / 3]
            running = 0
            r = 0
            for l in lines:
                if r < 2 and running >= thirds[r]:
                    r += 1
                rows[r] = (rows[r] + "   │   " + l) if rows[r] else l
                running += len(l)
            display = "\n".join(row for row in rows if row)
            self._explanation_lbl.setText(display)
            self._explanation_lbl.show()
            if lbl2 is not None:
                lbl2.hide()
            if _scroll:
                _scroll.show()
        else:
            self._explanation_lbl.hide()
            if lbl2 is not None:
                lbl2.hide()
            if _scroll:
                _scroll.hide()

    def _setup_footer(self):
        lbl_out = QLabel(self.tr("lbl_gen_formel"))
        lbl_out.setFont(_ui_font(self.current_lang, _pt(10), bold=True))
        self._root_layout.addWidget(lbl_out)
        out_row = QHBoxLayout()
        self.output_entry = QTextEdit()
        self.output_entry.setFont(QFont(Config.FONT_OUTPUT, _pt(11)))
        self.output_entry.setFixedHeight(Config.OUTPUT_H)
        self.output_entry.setLineWrapMode(QTextEdit.NoWrap)
        self.output_entry.setReadOnly(False)
        self.output_entry.setUndoRedoEnabled(False)
        self.highlighter = FormulaHighlighter(
            self.output_entry.document(),
            functions=self._get_function_names()
        )
        self.output_entry.textChanged.connect(self._validate_output_brackets)
        self.output_entry.textChanged.connect(self._update_explanation)
        out_row.addWidget(self.output_entry, stretch=1)
        self._btn_undo = QPushButton(self.tr("btn_undo"))
        self._btn_undo.setToolTip(self.tr("tooltip_undo"))
        self._btn_undo.setEnabled(False)
        self._btn_undo.clicked.connect(self._undo)
        out_row.addWidget(self._btn_undo)
        self._btn_redo = QPushButton(self.tr("btn_redo"))
        self._btn_redo.setToolTip(self.tr("tooltip_redo"))
        self._btn_redo.setEnabled(False)
        self._btn_redo.clicked.connect(self._redo)
        out_row.addWidget(self._btn_redo)
        self._btn_copy = QPushButton(self.tr("btn_copy"))
        self._btn_copy.setIcon(self._icon("copy.png"))  # ⬅️ Hier wird das Kopieren-Icon geladen
        self._btn_copy.clicked.connect(self.kopieren)
        out_row.addWidget(self._btn_copy)
        
        btn_save = QPushButton(self.tr("btn_save"))
        btn_save.setIcon(self._icon("saved.png"))  # ⬅️ Hier wird das Speichern-Icon geladen
        btn_save.clicked.connect(self.formel_speichern)
        out_row.addWidget(btn_save)
        self._root_layout.addLayout(out_row)
        # Erklärung: WordWrap an → Qt bricht an der Fensterbreite um,
        # kein Fenster-Wachstum, kein Überlaufen
        _expl_style = (
            "QLabel { color: #555555; padding: 2px 6px; "
            "border-left: 3px solid #aaaaaa; }"
        )
        self._explanation_lbl = QLabel("")
        self._explanation_lbl.setFont(QFont(Config.FONT_MONO, _pt(9)))
        self._explanation_lbl.setWordWrap(False)        # jede Reihe bleibt eine Zeile
        self._explanation_lbl.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self._explanation_lbl.setStyleSheet(_expl_style)
        self._explanation_lbl.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed)
        self._explanation_lbl.setFixedHeight(_pt(9) * 5 + 12)  # 3 Zeilen + Padding
        self._explanation_lbl.hide()
        self._explanation_scroll = None

        # 🚨 HIER IST DIE SPERRE DIREKT IM ORIGINALEN LABEL 🚨
        # Wir merken uns die echten Qt-Befehle
        qt_original_setText = self._explanation_lbl.setText
        qt_original_show = self._explanation_lbl.show

        # Wir bauen eine Prüfung: Sind wir im Plugins-Tab?
        def ist_plugin_aktiv():
            if hasattr(self, "notebook"):
                idx = self.notebook.currentIndex()
                if idx >= 0:
                    tab_text = self.notebook.tabText(idx).strip().lower()
                    plugin_var_idx = getattr(self, "_plugin_tab_index", -1)
                    # Wenn "plugin" im Namen steht oder der Index stimmt: JA!
                    if "plugin" in tab_text or idx == plugin_var_idx:
                        return True
            return False

        # Wir biegen den "Text-Schreiben" Befehl um
        def sicheres_setText(text):
            if ist_plugin_aktiv():
                qt_original_setText("")  # Text sofort löschen
                self._explanation_lbl.hide()  # Unsichtbar machen
            else:
                qt_original_setText(text)  # Normal schreiben in anderen Tabs

        # Wir biegen den "Anzeigen" Befehl um
        def sicheres_show():
            if ist_plugin_aktiv():
                self._explanation_lbl.hide()  # Bleibt versteckt
            else:
                qt_original_show()  # Normal anzeigen in anderen Tabs

        # Jetzt überschreiben wir die Funktionen des Labels mit unseren sicheren Varianten
        self._explanation_lbl.setText = sicheres_setText
        self._explanation_lbl.show = sicheres_show
        # ─────────────────────────────────────────────────────────────────

        self._root_layout.addWidget(self._explanation_lbl)
        
        fav_group = QGroupBox(self.tr("fav_title"))
        fav_layout = QVBoxLayout(fav_group)
        fav_layout.setSpacing(4)
        search_row = QHBoxLayout()
        self._fav_search = QLineEdit()
        self._fav_search.setPlaceholderText(self.tr("adm_search_ph"))
        self._fav_search.setClearButtonEnabled(True)
        self._fav_search.textChanged.connect(self._filter_fav_list)
        search_row.addWidget(self._fav_search)
        fav_layout.addLayout(search_row)
        self.fav_tabs = QTabWidget()
        self.fav_tabs.setFixedHeight(Config.FAV_TABS_H)
        self.fav_tabs.currentChanged.connect(lambda _: self._filter_fav_list(self._fav_search.text()))
        team_widget = QWidget()
        team_layout = QVBoxLayout(team_widget)
        team_layout.setContentsMargins(2, 2, 2, 2)
        self.team_listbox = QListWidget()
        self.team_listbox.setFont(QFont(Config.FONT_MONO, _pt(10)))
        self.team_listbox.setSelectionMode(QAbstractItemView.SingleSelection)
        self.team_listbox.itemDoubleClicked.connect(self._team_formel_laden)
        team_layout.addWidget(self.team_listbox)
        
        # HIER WIRD DAS TEAM-ICON EINGEBAUT:
        self.fav_tabs.addTab(team_widget, self._icon("Team.png"), self.tr("fav_tab_team"))

        eigene_widget = QWidget()
        eigene_layout = QVBoxLayout(eigene_widget)
        eigene_layout.setContentsMargins(2, 2, 2, 2)
        self.fav_listbox = QListWidget()
        self.fav_listbox.setFont(QFont(Config.FONT_MONO, _pt(10)))
        self.fav_listbox.setSelectionMode(QAbstractItemView.SingleSelection)
        self.fav_listbox.setDragDropMode(QAbstractItemView.InternalMove)
        self.fav_listbox.setDefaultDropAction(Qt.MoveAction)
        self.fav_listbox.model().rowsMoved.connect(self._on_fav_rows_moved)
        self.fav_listbox.installEventFilter(self)
        eigene_layout.addWidget(self.fav_listbox)
        
        # HIER WIRD DAS ICON FÜR GESPEICHERTE FORMELN EINGEBAUT (Emoji "⭐ " entfernt):
        self.fav_tabs.addTab(eigene_widget, self._icon("Formul_saved.png"), self.tr("fav_title"))

        verlauf_widget = QWidget()
        verlauf_layout = QVBoxLayout(verlauf_widget)
        verlauf_layout.setContentsMargins(2, 2, 2, 2)
        self.verlauf_listbox = QListWidget()
        self.verlauf_listbox.setFont(QFont(Config.FONT_MONO, _pt(10)))
        self.verlauf_listbox.setSelectionMode(QAbstractItemView.SingleSelection)
        self.verlauf_listbox.installEventFilter(self)
        self.verlauf_listbox.itemDoubleClicked.connect(
            lambda item: self.set_o(item.data(Qt.UserRole))
        )
        verlauf_layout.addWidget(self.verlauf_listbox)
        
        # HIER WIRD DAS VERLAUF-ICON EINGEBAUT (Emoji "🕐 " entfernt):
        self.fav_tabs.addTab(verlauf_widget, self._icon("history.png"), self.tr("tab_history"))

        fav_layout.addWidget(self.fav_tabs)
        fav_btns = QHBoxLayout()
        btn_load = QPushButton(self.tr("btn_load"))
        btn_load.clicked.connect(self.formel_laden)
        fav_btns.addWidget(btn_load)
        btn_del = QPushButton(self.tr("btn_del"))
        btn_del.clicked.connect(self.formel_loeschen)
        fav_btns.addWidget(btn_del)
        self._btn_clear_history = QPushButton("🗑 " + self.tr("btn_clear_history"))
        self._btn_clear_history.clicked.connect(self._verlauf_loeschen)
        self._btn_clear_history.setVisible(False)
        fav_btns.addWidget(self._btn_clear_history)
        self.fav_tabs.currentChanged.connect(self._on_fav_tab_changed)
        self._net_lbl = QLabel()
        self._net_lbl.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        fav_btns.addStretch()
        fav_btns.addWidget(self._net_lbl)
        fav_layout.addLayout(fav_btns)
        self._root_layout.addWidget(fav_group)
        self._update_fav_list()
        self._update_history_list()
        self._update_net_label()

    # -----------------------------------------------------------------------
    # Sprache wechseln
    # -----------------------------------------------------------------------
    def _on_lang_change(self, index: int):
        lang_codes = list(self.langs.keys())
        if index < 0 or index >= len(lang_codes): return
        saved = {
            "bereich":  self.bereich_entry.text(),
            "bereich2": self.bereich2_entry.text(),
            "z1":       self.zelle1_entry.text(),
            "z2":       self.zelle2_entry.text(),
            "param":    self.param_entry.text(),
            "output":   self.output_entry.toPlainText(),
            "ddl_z1":   self._ddl_z1.currentIndex(),
            "ddl_z2":   self._ddl_z2.currentIndex(),
            "ddl_br":   self._ddl_br.currentIndex(),
            "ddl_br2":  self._ddl_br2.currentIndex(),
        }
        favs = self.favoriten[:]; verlauf = self._verlauf[:]
        self.current_lang = lang_codes[index]
        self.settings["language"] = self.current_lang
        save_settings(self.settings)
        if self.current_lang == "hi":
            _ensure_hindi_font(QApplication.instance())
        self.favoriten = favs; self._verlauf = verlauf
        for plugin in self._plugins:
            plugin.name        = get_plugin_text(plugin.raw_meta.get("name"),        self.current_lang, FALLBACK_LANG)
            plugin.description = get_plugin_text(plugin.raw_meta.get("description"), self.current_lang, FALLBACK_LANG)
            plugin.formulas    = resolve_formulas(plugin.raw_formulas, self.current_lang, FALLBACK_LANG)
        central = QWidget()
        self.setCentralWidget(central)
        self._root_layout = QVBoxLayout(central)
        self._root_layout.setContentsMargins(10, 10, 10, 10)
        self._root_layout.setSpacing(6)
        self._erstelle_ui()
        self.bereich_entry.setText(saved["bereich"])
        self.bereich2_entry.setText(saved["bereich2"])
        self.zelle1_entry.setText(saved["z1"])
        self.zelle2_entry.setText(saved["z2"])
        self.param_entry.setText(saved["param"])
        self.output_entry.setPlainText(saved["output"])
        self._ddl_z1.setCurrentIndex(saved["ddl_z1"])
        self._ddl_z2.setCurrentIndex(saved["ddl_z2"])
        self._ddl_br.setCurrentIndex(saved["ddl_br"])
        self._ddl_br2.setCurrentIndex(saved["ddl_br2"])
        #self._btn_dark.setText("☀️" if self._dark_mode else "🌙")
        self.highlighter = FormulaHighlighter(
            self.output_entry.document(),
            functions=self._get_function_names()
        )
        self.highlighter.rehighlight()
        self._update_fav_list()
        self._update_history_list()
        self._update_net_label()
        _apply_font_to_app(QApplication.instance(), self.current_lang)
        _apply_rtl_layout(self, self.current_lang)

    # -----------------------------------------------------------------------
    # Formel-Operationen
    # -----------------------------------------------------------------------
    def op_einfach(self, op): self._register_and_set(lambda: self.set_o(f"={self.z1()}{op}{self.z2()}"))
    def op_bereich(self, f):  self._register_and_set(lambda: self.set_o(f"={f}({self.br()})"))
    def op_sumprod(self):     self._register_and_set(lambda: self.set_o(f"={self.tr('f_sumprod')}({self.br()};{self.br2()})"))

    def call_f_if(self):    self._register_and_set(lambda: self.set_o(f'={self.tr("f_if")}({self.z1()}>0;"{self.tr("formula_ok")}";"{self.tr("formula_fehler")}")'))
    def call_f_and(self):   self._register_and_set(lambda: self.set_o(f'={self.tr("f_and")}({self.z1()}>0;{self.z2()}>0)'))
    def call_f_or(self):    self._register_and_set(lambda: self.set_o(f'={self.tr("f_or")}({self.z1()}>0;{self.z2()}>0)'))
    def call_f_not(self):   self._register_and_set(lambda: self.set_o(f'={self.tr("f_not")}({self.z1()}>0)'))
    def call_f_sumif(self):      self._register_and_set(lambda: self.set_o(f'={self.tr("f_sumif")}({self.br()};">10";{self.br()})'))
    def call_f_countif(self):    self._register_and_set(lambda: self.set_o(f'={self.tr("f_countif")}({self.br()};"{self.tr("formula_value")}")'))
    def call_f_avgif(self):      self._register_and_set(lambda: self.set_o(f'={self.tr("f_avgif")}({self.br()};">0";{self.br()})'))
    def call_f_sumifs(self):     self._register_and_set(lambda: self.set_o(f'={self.tr("f_sumifs")}({self.br()};{self.br2()};">10")'))
    def call_f_stdev(self):      self._register_and_set(lambda: self.set_o(f'={self.tr("f_stdev")}({self.br()})'))
    def call_f_var(self):        self._register_and_set(lambda: self.set_o(f'={self.tr("f_var")}({self.br()})'))
    def call_f_countblank(self): self._register_and_set(lambda: self.set_o(f'={self.tr("f_countblank")}({self.br()})'))
    def call_f_large(self):      self._register_and_set(lambda: self.set_o(f'={self.tr("f_large")}({self.br()};{self.pa()})'))
    def call_f_today(self):   self._register_and_set(lambda: self.set_o(f'={self.tr("f_today")}()'))
    def call_f_now(self):     self._register_and_set(lambda: self.set_o(f'={self.tr("f_now")}()'))
    def call_f_year(self):    self._register_and_set(lambda: self.set_o(f'={self.tr("f_year")}({self.z1()})'))
    def call_f_month(self):   self._register_and_set(lambda: self.set_o(f'={self.tr("f_month")}({self.z1()})'))
    def call_f_day(self):     self._register_and_set(lambda: self.set_o(f'={self.tr("f_day")}({self.z1()})'))
    def call_f_date(self):
        year = datetime.date.today().year
        self._register_and_set(lambda: self.set_o(f'={self.tr("f_date")}({year};1;1)'))
    def call_f_datedif(self):
        self._register_and_set(lambda: self.set_o(f'={self.tr("f_datedif")}({self.z1()};{self.z2()};"D")'))
    def call_f_weekday(self): self._register_and_set(lambda: self.set_o(f'={self.tr("f_weekday")}({self.z1()};2)'))
    def call_f_concat(self):  self._register_and_set(lambda: self.set_o(f'={self.tr("f_concat")}({self.z1()};" ";{self.z2()})'))
    def call_f_len(self):     self._register_and_set(lambda: self.set_o(f'={self.tr("f_len")}({self.z1()})'))
    def call_f_left(self):    self._register_and_set(lambda: self.set_o(f'={self.tr("f_left")}({self.z1()};{self.pa()})'))
    def call_f_right(self):   self._register_and_set(lambda: self.set_o(f'={self.tr("f_right")}({self.z1()};{self.pa()})'))
    def call_f_mid(self):     self._register_and_set(lambda: self.set_o(f'={self.tr("f_mid")}({self.z1()};1;{self.pa()})'))
    def call_f_upper(self):   self._register_and_set(lambda: self.set_o(f'={self.tr("f_upper")}({self.z1()})'))
    def call_f_lower(self):   self._register_and_set(lambda: self.set_o(f'={self.tr("f_lower")}({self.z1()})'))
    def call_f_trim(self):    self._register_and_set(lambda: self.set_o(f'={self.tr("f_trim")}({self.z1()})'))
    def call_f_vlookup(self): self._register_and_set(lambda: self.set_o(f'={self.tr("f_vlookup")}({self.z1()};{self.br()};{self.pa()};0)'))
    def call_f_hlookup(self): self._register_and_set(lambda: self.set_o(f'={self.tr("f_hlookup")}({self.z1()};{self.br()};{self.pa()};0)'))
    def call_f_index(self):   self._register_and_set(lambda: self.set_o(f'={self.tr("f_index")}({self.br()};{self.pa()};1)'))
    def call_f_match(self):   self._register_and_set(lambda: self.set_o(f'={self.tr("f_match")}({self.z1()};{self.br()};0)'))
    def call_idx_match(self): self._register_and_set(lambda: self.set_o(
        f'={self.tr("f_index")}({self.br2()};{self.tr("f_match")}({self.z1()};{self.br()};0))'))
    def call_f_round(self):     self._register_and_set(lambda: self.set_o(f'={self.tr("f_round")}({self.z1()};{self.pa()})'))
    def call_f_roundup(self):   self._register_and_set(lambda: self.set_o(f'={self.tr("f_roundup")}({self.z1()};{self.pa()})'))
    def call_f_rounddown(self): self._register_and_set(lambda: self.set_o(f'={self.tr("f_rounddown")}({self.z1()};{self.pa()})'))
    def call_f_int(self):       self._register_and_set(lambda: self.set_o(f'={self.tr("f_int")}({self.z1()})'))
    def call_f_trunc(self):     self._register_and_set(lambda: self.set_o(f'={self.tr("f_trunc")}({self.z1()};{self.pa()})'))
    def call_f_abs(self):       self._register_and_set(lambda: self.set_o(f'={self.tr("f_abs")}({self.z1()})'))
    def call_f_mod(self):       self._register_and_set(lambda: self.set_o(f'={self.tr("f_mod")}({self.z1()};{self.pa()})'))
    def call_f_sqrt(self):      self._register_and_set(lambda: self.set_o(f'={self.tr("f_sqrt")}({self.z1()})'))
    def call_f_rand(self):      self._register_and_set(lambda: self.set_o(f'={self.tr("f_rand")}()'))

    # -----------------------------------------------------------------------
    # Hilfe & Referenz
    # -----------------------------------------------------------------------
    def zeige_hilfe(self):
        content = load_doc_file("README", self.current_lang, lang_func=self.tr)
        dlg = DocDialog(self, self.tr("help_title"), content, tr_func=self.tr)
        dlg.show()

    def zeige_referenz(self):
        content = load_doc_file("REFERENZ", self.current_lang, lang_func=self.tr)
        dlg = DocDialog(self, self.tr("ref_title"), content, tr_func=self.tr)
        dlg.show()

    def _repair_shortcut(self):
        ok = _create_desktop_shortcut(
            shortcut_name=self.tr("desktop_shortcut_name"),
            shortcut_comment=self.tr("desktop_shortcut_comment")
        )
        title = self.tr("msg_shortcut_title")
        if ok:
            QMessageBox.information(self, title, f"✓ {_get_desktop_path()}")
        else:
            QMessageBox.critical(self, title, self.tr("msg_shortcut_body"))

    # -----------------------------------------------------------------------
    # Dark Mode
    # -----------------------------------------------------------------------
    def _toggle_dark_mode(self) -> None:
        self._dark_mode = not self._dark_mode
        self.settings["dark_mode"] = self._dark_mode
        save_settings(self.settings)
        apply_theme(QApplication.instance(), self._dark_mode)
        
        # Icon wechseln
        aktuelles_icon = "Dark_Mode.png" if not self._dark_mode else "brightness.png"
        self._btn_dark.setIcon(self._icon(aktuelles_icon))
        
        # -------------------------------------------------------------------
        # BUGFIX: Alle Fenster und Unterfenster (z.B. Sprachfenster) live aktualisieren
        # -------------------------------------------------------------------
        for widget in QApplication.topLevelWidgets():
            # Aktualisiert das Fenster selbst
            widget.style().unpolish(widget)
            widget.style().polish(widget)
            widget.update()
            # Aktualisiert jedes einzelne Element (Dropdowns, Knöpfe) im Fenster
            for child in widget.findChildren(QWidget):
                child.style().unpolish(child)
                child.style().polish(child)
                child.update()
        # -------------------------------------------------------------------

        self.highlighter = FormulaHighlighter(
            self.output_entry.document(),
            functions=self._get_function_names()
        )
        self.highlighter.rehighlight()
        self._update_net_label()
        self._update_fav_list()
        if hasattr(self, "_explanation_lbl"):
            fg = "#bbbbbb" if self._dark_mode else "#555555"
            border = "#666666" if self._dark_mode else "#aaaaaa"
            self._explanation_lbl.setStyleSheet(
                f"QLabel {{ color: {fg}; padding: 4px 6px; "
                f"border-left: 3px solid {border}; margin-top: 2px; }}"
            )

        self._reapply_validation_styles()

    def _reapply_validation_styles(self) -> None:
        for field, check_fn in [
            (self.bereich_entry,  lambda t: self._valid_range(t, self.tr)),
            (self.bereich2_entry, lambda t: self._valid_range(t, self.tr)),
            (self.zelle1_entry,   lambda t: self._valid_cell(t, self.tr)),
            (self.zelle2_entry,   lambda t: self._valid_cell(t, self.tr)),
        ]:
            t = field.text().strip()
            if t:
                ok, _ = check_fn(t)
                field.setStyleSheet("" if ok else self._err_style("QLineEdit"))
        self._validate_output_brackets()

    # -----------------------------------------------------------------------
    # Netzpfad konfigurieren
    # -----------------------------------------------------------------------
    def _configure_net_path(self):
        current = self.settings.get("net_fav_dir", "")
        dlg = NetPathDialog(self, current, tr=self.tr)
        if dlg.exec_() == QDialog.Accepted:
            new_path = dlg.get_path()
            self.settings["net_fav_dir"] = new_path
            save_settings(self.settings)
            self.favoriten = sync_from_network(self.settings)
            self._update_fav_list()
            self._update_net_label()
            if new_path:
                self._status_bar.showMessage(f"{self.tr('net_path_set')}{new_path}", Config.MSG_LONG)
            else:
                self._status_bar.showMessage(self.tr("net_path_removed"), Config.MSG_LONG)

    # -----------------------------------------------------------------------
    # Admin-Panel
    # -----------------------------------------------------------------------
    def _open_admin_panel(self):
        if not admin_password_is_set():
            ans = QMessageBox.question(
                self, self.tr("adm_set_pw_title"), self.tr("adm_set_pw_msg"),
                QMessageBox.Yes | QMessageBox.No
            )
            if ans != QMessageBox.Yes: return
            pw_dlg = SetPasswordDialog(self, is_first_time=True, tr=self.tr)
            if pw_dlg.exec_() != QDialog.Accepted: return
            QMessageBox.information(self, self.tr("adm_set_pw_ok_title"), self.tr("adm_set_pw_ok_msg"))
        else:
            login = AdminLoginDialog(self, tr=self.tr)
            if login.exec_() != QDialog.Accepted: return
        panel = AdminPanelDialog(self, self.settings, self.favoriten, tr=self.tr)
        panel.exec_()
        updated = panel.get_entries()
        if updated and updated != self.favoriten:
            self.favoriten = updated
            self._update_fav_list()
            self._status_bar.showMessage(self.tr("adm_team_updated"), Config.MSG_NORMAL)

    def _open_plugin_manager(self):
        try:
            import importlib.util
            pm_path = _here / "plugin_manager.py"
            if not pm_path.exists():
                QMessageBox.critical(self, "Plugin Manager",
                                     f"plugin_manager.py nicht gefunden:\n{pm_path}")
                return
            spec = importlib.util.spec_from_file_location("plugin_manager", pm_path)
            pm = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(pm)
            dlg = pm.PluginManagerWindow()
            dlg.setWindowModality(Qt.ApplicationModal)
            dlg.show()
            self._plugin_manager_win = dlg
            dlg.destroyed.connect(self._reload_plugins)
        except Exception as e:
            QMessageBox.critical(self, "Plugin Manager", f"Fehler beim Öffnen:\n{e}")

    def _reload_plugins(self):
        self._plugins = load_all_plugins(
            plugins_dir   = _here / "plugins",
            lang          = self.current_lang,
            fallback_lang = FALLBACK_LANG,
            app_version   = APP_VERSION,
        )
        if hasattr(self, "_build_plugin_tab"):
            try: self._build_plugin_tab()
            except Exception: pass

    def _open_language_tool(self):
        try:
            from services.language_tool import LanguageTool
        except ImportError as e:
            QMessageBox.critical(self, "Error", f"language_tool.py not found in services/:\n{e}")
            return
        tool = LanguageTool(base_dir=_here)
        tool.run()
        self.langs    = load_languages()
        self._calc_tr = self._load_calc_translations()
        lang_codes = list(self.langs.keys())
        lang_names = [self.langs[c]["_meta"]["name"] for c in lang_codes]
        # blockSignals verhindert, dass clear()/addItems() _on_lang_change auslösen
        # und dabei die aktuelle Sprache auf den ersten Eintrag zurücksetzen.
        self.lang_combo.blockSignals(True)
        self.lang_combo.clear()
        self.lang_combo.addItems(lang_names)
        idx = lang_codes.index(self.current_lang) if self.current_lang in lang_codes else 0
        self.lang_combo.setCurrentIndex(idx)
        self.lang_combo.blockSignals(False)


    def _open_lang_sync(self):
        try:
            from services.LangSync_Tool import LangSyncTool
        except ImportError as e:
            QMessageBox.critical(self, "Error", f"LangSync_Tool.py not found in services/:\n{e}")
            return
        dlg = LangSyncTool(parent=self)
        dlg.exec_()
    def _get_net_base(self) -> "Path | None":
        """
        Gibt den konfigurierten Netzlaufwerk-Basispfad zurück, oder None.

        settings["net_fav_dir"] enthält den Pfad zum Netzordner (z.B.
        \\\\Server\\Freigabe\\formeln). net_fav_path() hängt intern
        "favoriten.json" dran – wir wollen aber nur das Verzeichnis.
        """
        net_fav_dir = self.settings.get("net_fav_dir", "").strip()
        if not net_fav_dir:
            return None
        p = Path(net_fav_dir)
        # Falls jemand den vollen Dateipfad eingetragen hat, Elternverzeichnis nehmen
        return p.parent if p.suffix == ".json" else p

    def _open_backup(self):
        net_base = self._get_net_base()
        dlg = BackupRestoreDialog(self, mode="backup", net_base=net_base, base_dir=_here)
        dlg.exec_()

    def _open_restore(self):
        net_base = self._get_net_base()
        dlg = BackupRestoreDialog(self, mode="restore", net_base=net_base, base_dir=_here)
        if dlg.exec_() == QDialog.Accepted:
            # Favoriten und Plugins nach Restore neu laden
            self.favoriten = load_local_favorites()
            self._update_fav_list()
            self._reload_plugins()
            self._status_bar.showMessage(
                "Restore complete – please restart for full effect.", 6000
            )

    def _update_net_label(self):
        net = net_fav_path(self.settings)
        if net:
            erreichbar = net.parent.is_dir()
            if erreichbar:
                self._net_lbl.setText(f'<span style="color:{THEME["ui_net_ok"]}">🌐 {net.parent}</span>')
                self._net_lbl.setToolTip(f"{self.tr('net_tooltip_connected')}: {net}")
            else:
                self._net_lbl.setText(f'<span style="color:{THEME["ui_net_err"]}">{self.tr("net_status_no_reach")}</span>')
                self._net_lbl.setToolTip(f"{self.tr('net_tooltip_path')}: {net}\n{self.tr('net_tooltip_offline')}")
        else:
            self._net_lbl.setText(f'<span style="color:{THEME["ui_net_off"]}">{self.tr("net_status_only_local")}</span>')
            self._net_lbl.setToolTip(self.tr("adm_panel_no_net"))

    # -----------------------------------------------------------------------
    # Favoriten – Anzeige
    # -----------------------------------------------------------------------
    def _update_fav_list(self):
        self.team_listbox.clear()
        self.fav_listbox.clear()
        for entry in self.favoriten:
            formel = entry.formel; label = entry.label; is_team = entry.team
            display = f"[TEAM]  {label + '  ' if label else ''}{formel}" if is_team else (
                      f"{label}  {formel}" if label else formel)
            item = QListWidgetItem(display)
            item.setData(Qt.UserRole, formel)
            if is_team:
                item.setForeground(QBrush(QColor(THEME["ui_team_fg"])))
                item.setToolTip(self.tr("fav_team_tooltip"))
                self.team_listbox.addItem(item)
            else:
                self.fav_listbox.addItem(item)
        query = getattr(self, "_fav_search", None)
        if query is not None:
            self._filter_fav_list(query.text())

    def _on_fav_rows_moved(self, _parent, src, _end, _dest, dst) -> None:
        neue_eigene_formeln = [
            self.fav_listbox.item(i).data(Qt.UserRole)
            for i in range(self.fav_listbox.count())
        ]
        team_entries = [e for e in self.favoriten if e.team]
        eigene_map   = {e.formel: e for e in self.favoriten if not e.team}
        neue_eigene  = [eigene_map[f] for f in neue_eigene_formeln if f in eigene_map]
        self.favoriten = team_entries + neue_eigene
        self._status_bar.showMessage(self.tr("fav_order_saved"), Config.MSG_SHORT)
        self._start_sync()

    def _filter_fav_list(self, text: str):
        query = text.strip().lower()
        for attr in ["team_listbox", "fav_listbox", "verlauf_listbox"]:
            listbox = getattr(self, attr, None)
            if listbox is None: continue
            for i in range(listbox.count()):
                item = listbox.item(i)
                visible = (not query) or (query in item.text().lower())
                item.setHidden(not visible)

    # -----------------------------------------------------------------------
    # Favoriten – Aktionen
    # -----------------------------------------------------------------------
    def _team_formel_laden(self, item: QListWidgetItem):
        self.set_o(item.data(Qt.UserRole))
        self._status_bar.showMessage(self.tr("msg_team_loaded"), Config.MSG_SHORT)

    def formel_laden(self):
        tab = self.fav_tabs.currentIndex()
        if tab == 0: listbox = self.team_listbox
        elif tab == 1: listbox = self.fav_listbox
        else: listbox = self.verlauf_listbox
        items = listbox.selectedItems()
        if items:
            self.set_o(items[0].data(Qt.UserRole))

    def formel_loeschen(self):
        tab = self.fav_tabs.currentIndex()
        if tab == 0:
            QMessageBox.information(self, self.tr("adm_team_readonly_title"), self.tr("adm_team_readonly_msg"))
            return
        if tab == 2:
            self._verlauf_loeschen(); return
        row = self.fav_listbox.currentRow()
        if row < 0: return
        eigene = [e for e in self.favoriten if not e.team]
        if row >= len(eigene): return
        to_remove = eigene[row].formel
        self.favoriten = [e for e in self.favoriten if e.formel != to_remove]
        self._update_fav_list()
        self._status_bar.showMessage(self.tr("msg_deleted"), Config.MSG_SHORT)
        self._start_sync()

    # -----------------------------------------------------------------------
    # Verlauf
    # -----------------------------------------------------------------------
    def _update_history_list(self) -> None:
        if not hasattr(self, "verlauf_listbox"): return
        self.verlauf_listbox.clear()
        for i, formel in enumerate(self._verlauf, start=1):
            item = QListWidgetItem(f"{i:2}.  {formel}")
            item.setData(Qt.UserRole, formel)
            item.setToolTip(formel)
            self.verlauf_listbox.addItem(item)

    def _verlauf_loeschen(self) -> None:
        ans = QMessageBox.question(
            self, self.tr("history_clear_title"), self.tr("history_clear_msg"),
            QMessageBox.Yes | QMessageBox.No
        )
        if ans == QMessageBox.Yes:
            self._verlauf = []
            save_history(self._verlauf)
            self._update_history_list()
            self._status_bar.showMessage(self.tr("history_cleared"), Config.MSG_SHORT)

    def _on_fav_tab_changed(self, index: int) -> None:
        if hasattr(self, "_btn_clear_history"):
            self._btn_clear_history.setVisible(index == 2)

    def eventFilter(self, obj, event) -> bool:
        from PyQt5.QtCore import QEvent
        if event.type() == QEvent.KeyPress and event.key() in (Qt.Key_Delete, Qt.Key_Backspace):
            if obj is self.fav_listbox:
                self._fav_eintrag_loeschen(); return True
            if obj is self.verlauf_listbox:
                self._verlauf_eintrag_loeschen(); return True
        return super().eventFilter(obj, event)

    def _fav_eintrag_loeschen(self) -> None:
        row = self.fav_listbox.currentRow()
        if row < 0: return
        eigene = [e for e in self.favoriten if not e.team]
        if row >= len(eigene): return
        to_remove = eigene[row].formel
        self.favoriten = remove_favorite(self.favoriten, to_remove)
        self._update_fav_list()
        neue_eigene = [e for e in self.favoriten if not e.team]
        if neue_eigene:
            self.fav_listbox.setCurrentRow(min(row, self.fav_listbox.count() - 1))
        self._status_bar.showMessage(self.tr('msg_deleted'), Config.MSG_SHORT)
        self._start_sync()

    def _verlauf_eintrag_loeschen(self) -> None:
        row = self.verlauf_listbox.currentRow()
        if row < 0 or row >= len(self._verlauf): return
        del self._verlauf[row]
        save_history(self._verlauf)
        self._update_history_list()
        if self._verlauf:
            self.verlauf_listbox.setCurrentRow(min(row, self.verlauf_listbox.count() - 1))
        self._status_bar.showMessage(self.tr('msg_deleted'), Config.MSG_SHORT)

    def kopieren(self):
        doc = self.output_entry.document()
        plain_text = self.output_entry.toPlainText()
        html_parts = []
        block = doc.begin()
        while block.isValid():
            it = block.begin()
            while not it.atEnd():
                fragment = it.fragment()
                if fragment.isValid():
                    text = fragment.text()
                    fmt = fragment.charFormat()
                    color = fmt.foreground().color()
                    bold = fmt.fontWeight() == QFont.Bold
                    if color.isValid() and color != QColor(0, 0, 0) and color.alpha() > 0:
                        hex_color = color.name()
                        style = f"color:{hex_color};"
                        if bold: style += "font-weight:bold;"
                        html_parts.append(f'<span style="{style}">{text}</span>')
                    else:
                        html_parts.append(text)
                it += 1
            html_parts.append("<br>")
            block = block.next()
        html_body = "".join(html_parts)
        html_text = (
            f'<html><body style="font-family:{Config.FONT_OUTPUT};font-size:11pt;">'
            f'{html_body}</body></html>'
        )
        mime_data = QMimeData()
        mime_data.setHtml(html_text)
        mime_data.setText(plain_text)
        QApplication.clipboard().setMimeData(mime_data)
        self._status_bar.showMessage(self.tr("status_copy"), Config.MSG_NORMAL)
        self._flash_copy_button()

    def _flash_copy_button(self):
        original_text  = self._btn_copy.text()
        original_style = self._btn_copy.styleSheet()
        self._btn_copy.setText(f"✓ {self.tr('btn_copy_done')}")
        self._btn_copy.setStyleSheet(
            "QPushButton {"
            f"  background-color: {THEME['ui_net_ok']};"
            "  color: white; font-weight: bold; border-radius: 4px; }"
        )
        self._btn_copy.setEnabled(False)
        def _restore():
            self._btn_copy.setText(original_text)
            self._btn_copy.setStyleSheet(original_style)
            self._btn_copy.setEnabled(True)
        QTimer.singleShot(Config.FLASH_MS, _restore)

    def formel_speichern(self):
        formel = self.output_entry.toPlainText().strip()
        if not formel: return
        if formel in {e.formel for e in self.favoriten}:
            QMessageBox.information(self, self.tr("fav_exists_title"), self.tr("fav_save_exists"))
            return
        label, ok = QInputDialog.getText(
            self, self.tr("fav_save_label_dlg"), self.tr("fav_save_label_msg")
        )
        if not ok: return
        self.favoriten.append(Favorite(formel=formel, label=label.strip(), team=False))
        self._status_bar.showMessage(self.tr("fav_save_ok"), Config.MSG_NORMAL)
        self._update_fav_list()
        self.fav_tabs.setCurrentIndex(1)
        self._start_sync()

    # -----------------------------------------------------------------------
    # Hintergrund-Sync
    # -----------------------------------------------------------------------
    def _start_sync(self):
        worker = SyncWorker(self.settings, self.favoriten, lang_func=self.tr, parent=self)
        self._sync_workers.add(worker)
        def _on_done(): self._sync_workers.discard(worker)
        def _on_error(msg: str):
            self._sync_workers.discard(worker)
            QMessageBox.warning(self, self.tr("msg_warn"), msg)
        worker.finished.connect(_on_done)
        worker.error.connect(_on_error)
        worker.start()

    def _lade_favoriten(self) -> list:
        return sync_from_network(self.settings)

    def _save_favs(self):
        self._start_sync()


# ---------------------------------------------------------------------------
# Globaler Hotkey-Thread
# ---------------------------------------------------------------------------
class _GlobalHotkeyThread(QThread):
    triggered = pyqtSignal()

    def __init__(self):
        super().__init__()
        self._listener = None

    def _emit(self):
        self.triggered.emit()

    def run(self):
        import platform as _plat
        # 1. MAC-ABSTURZ-STOPPER:
        # macOS Catalina blockiert globale Tastatur-Hooks im Hintergrund rigide.
        # Wir beenden den Thread hier für den Mac sofort. Kein pynput-Start = NIE WIEDER CRASH.
        if _plat.system() == "Darwin":
            print("Mac-Sicherheit: Globale F12-Überwachung deaktiviert.")
            return

        try:
            from pynput import keyboard as _kb
            CTRL = [_kb.Key.ctrl, _kb.Key.ctrl_l, _kb.Key.ctrl_r, _kb.Key.cmd, _kb.Key.cmd_l, _kb.Key.cmd_r]
            pressed = set()

            def _on_press(key):
                pressed.add(key)
                if any(k in pressed for k in CTRL) and key == _kb.Key.f12:
                    self._emit()

            def _on_release(key):
                pressed.discard(key)

            with _kb.Listener(on_press=_on_press, on_release=_on_release) as listener:
                self._listener = listener
                listener.join()
        except Exception:
            pass

    def stop(self):
        try:
            if self._listener is not None:
                self._listener.stop()
        except Exception:
            pass
        try:
            import platform as _plat
            if _plat.system() == "Windows":
                import keyboard as _keyboard
                _keyboard.unhook_all()
        except Exception:
            pass
        self.quit()
        self.wait(1000)


# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    import platform as _plat
    if _plat.system() == "Darwin":
        os.environ.setdefault("QT_MAC_WANTS_LAYER", "1")

    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = CalcFormelHelper()
    apply_theme(app, window._dark_mode)
    window.show()
    _apply_font_to_app(app, window.current_lang)
    
    # --- INTELLIGENTE SHORTCUT-STEUERUNG NACH BETRIEBSSYSTEM ---
    if _plat.system() == "Darwin":
        # MAC-VERSION: Reagiert NUR NOCH auf Ctrl+X (Cmd+X bleibt für das System frei)
        try:
            from pynput import keyboard as _kb
            from PyQt5.QtCore import QObject, pyqtSignal
            
            class MacHotkeyBridge(QObject):
                triggered = pyqtSignal()

            bridge = MacHotkeyBridge()
            bridge.triggered.connect(window._toggle_minimize)

            pressed_modifiers = set()
            
            # KORREKTUR: Hier wurden alle _kb.Key.cmd Einträge gelöscht!
            # Jetzt wird ausschließlich die CONTROL-Taste überwacht.
            MODIFIERS = [_kb.Key.ctrl, _kb.Key.ctrl_l, _kb.Key.ctrl_r]
            
            def on_press(key):
                if key in MODIFIERS:
                    pressed_modifiers.add(key)
                
                # Prüfen auf die Taste 'X'
                is_x = False
                if hasattr(key, 'char') and key.char in ['x', 'X', '\x18']: # \x18 ist das Mac-Signal für Ctrl+X
                    is_x = True
                elif hasattr(key, 'vk') and key.vk == 7: # Interner Mac-Tastencode für 'X'
                    is_x = True
                    
                # Nur ausführen, wenn die CONTROL-Taste aktiv gehalten wird und X gedrückt wird
                if pressed_modifiers and is_x:
                    bridge.triggered.emit()
                    
            def on_release(key):
                if key in MODIFIERS:
                    pressed_modifiers.discard(key)
                    
            # Startet den Mac-Hintergrund-Listener
            mac_listener = _kb.Listener(on_press=on_press, on_release=on_release)
            mac_listener.start()
            
        except Exception as e:
            print(f"Mac Hotkey Fehler: {e}")
            
    else:
        # WINDOWS-VERSION: Bleibt völlig unverändert auf F12
        _hotkey_thread = _GlobalHotkeyThread()
        _hotkey_thread.triggered.connect(window._toggle_minimize)
        _hotkey_thread.start()

    sys.exit(app.exec_())