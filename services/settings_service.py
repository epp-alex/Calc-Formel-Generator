"""
services/settings_service.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Pfade, Logging, atomares Schreiben, Einstellungen, Theme.
Kein PyQt5-Import – vollständig UI-unabhängig.
"""
import hashlib
from typing import Dict
import json
import logging
import os
import sys
import traceback
from pathlib import Path

# ---------------------------------------------------------------------------
# Konstanten
# ---------------------------------------------------------------------------
APP_NAME      = "CalcFormelHelper"
FALLBACK_LANG = "en"


class Config:
    """Zentrale Stelle für alle Dateinamen und unveränderliche App-Parameter."""
    INSTALL_MARKER = ".installed"
    LANGUAGES_FILE   = "languages.json"
    SETTINGS_FILE    = "settings.json"
    FAVORITES_FILE   = "favoriten.json"
    NET_FAV_FILENAME = "favoriten.json"
    ADMIN_FILE       = "admin.json"
    HISTORY_FILE     = "verlauf.json"
    HISTORY_MAX      = 20
    UNDO_MAX         = 50

    SHORTCUT_NAME    = "Calc Formel Helper"
    SHORTCUT_COMMENT = "LibreOffice Calc Formula Generator"
    APP_FILE_LINUX   = "Calc"
    APP_BUNDLE_MAC   = "Calc.app"

    HASH_ITERATIONS     = 260_000
    MIN_PASSWORD_LENGTH = 8

    FONT_UI     = "Arial"
    FONT_MONO   = "Courier New"
    FONT_OUTPUT = "Consolas"

    MSG_SHORT  = 2000
    MSG_NORMAL = 3000
    MSG_LONG   = 4000
    FLASH_MS   = 1500

    WIN_W           = 880
    WIN_H           = 940
    DLG_DOC_W       = 820
    DLG_DOC_H       = 680
    DLG_LOGIN_W     = 380
    DLG_SETPW_W     = 400
    DLG_ADMIN_W     = 720
    DLG_ADMIN_H     = 560
    DLG_NET_MIN_W   = 520
    ICON_BTN_W      = 32
    BTN_CLOSE_W     = 120
    LANG_COMBO_W    = 160
    CELL_FIELD_W    = 72
    OP_BTN_W        = 46
    OUTPUT_H        = 60
    FAV_TABS_H      = 130


FALLBACK_MESSAGES: Dict[str, str] = {
    "err_local_save":             "Local save failed:\n{e}",
    "net_err_conflict":           "The network file was changed by another user.",
    "net_err_lock_timeout":       "Could not acquire write lock on the network file (timeout).",
    "err_no_write_net":           "No write access to the network drive.",
    "err_net_unreachable":        "Network drive unreachable:\n{e}",
    "doc_load_error":             "Error loading:\n{path}\n\n{e}",
    "doc_not_found":              "File not found:\n  {prefix}_{lang}.md",
    "msg_langfile_missing_title": "Error",
    "msg_langfile_missing_body":  "Language file not found:\n{path}",
    "msg_langfile_invalid_title": "Error",
    "msg_langfile_invalid_body":  "Error in languages.json:\n{error}",
    "install_error_title":        "Installation",
    "install_error_exe_copy":     "Program file could not be copied:\n{error}",
    "install_error_app_copy":     "Application could not be copied:\n{error}",
    "msg_shortcut_title":         "Desktop Shortcut",
    "msg_shortcut_body":          "The desktop shortcut could not be created.",
    "tooltip_dark_mode":          "Toggle Dark Mode",
    "err_invalid_cell":           "Invalid – expected e.g. A1 or BC42",
    "err_col_overflow":           "Column '{col}' exceeds maximum XFD ({max:,})",
    "err_row_zero":               "Row 0 does not exist – first row is 1",
    "err_row_overflow":           "Row {row:,} exceeds maximum {max:,}",
    "err_invalid_range":          "Invalid – expected e.g. A1:B10",
    "err_range_col_overflow":     "Column '{col}' exceeds maximum XFD ({max:,})",
    "err_range_row_zero":         "Row 0 does not exist – first row is 1",
    "err_range_row_overflow":     "Row {row:,} exceeds maximum {max:,}",
    "err_range_col_order":        "Start column '{c1}' is after end column '{c2}'",
    "err_range_row_order":        "Start row {r1:,} is after end row {r2:,}",
}

# ---------------------------------------------------------------------------
# Pfade
# ---------------------------------------------------------------------------
def get_app_data_dir() -> Path:
    if sys.platform == "win32":
        base = Path(os.environ.get("APPDATA", "~")).expanduser()
    elif sys.platform == "darwin":
        base = Path("~/Library/Application Support").expanduser()
    else:
        base = Path(os.environ.get("XDG_CONFIG_HOME", "~/.config")).expanduser()
    return base / APP_NAME


def get_resource_dir() -> Path:
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        return Path(sys._MEIPASS)
    # services/ ist ein Unterordner → eine Ebene hoch
    return Path(__file__).resolve().parent.parent


RESOURCE_DIR  = get_resource_dir()
DATA_DIR      = get_app_data_dir()
DATA_DIR.mkdir(parents=True, exist_ok=True)

LANG_FILE     = RESOURCE_DIR / Config.LANGUAGES_FILE
SETTINGS_FILE = DATA_DIR     / Config.SETTINGS_FILE
FAV_FILE      = DATA_DIR     / Config.FAVORITES_FILE
NET_FAV_NAME  = Config.NET_FAV_FILENAME
ADMIN_FILE    = DATA_DIR     / Config.ADMIN_FILE
HISTORY_FILE  = DATA_DIR     / Config.HISTORY_FILE

# ---------------------------------------------------------------------------
# Logging  (lazy – get_app_data_dir muss zuerst definiert sein)
# ---------------------------------------------------------------------------
def _get_logger() -> logging.Logger:
    logger = logging.getLogger("CalcFormelHelper")
    if logger.handlers:
        return logger
    logger.setLevel(logging.DEBUG)
    try:
        from logging.handlers import RotatingFileHandler
        log_dir = get_app_data_dir()
        log_dir.mkdir(parents=True, exist_ok=True)
        fh = RotatingFileHandler(
            log_dir / "calc_helper.log",
            maxBytes=1_048_576, backupCount=3, encoding="utf-8",
        )
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(logging.Formatter(
            "%(asctime)s  %(levelname)-8s  %(name)s  %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        ))
        logger.addHandler(fh)
    except Exception:
        pass
    try:
        if sys.stderr and sys.stderr.fileno() >= 0:
            ch = logging.StreamHandler(sys.stderr)
            ch.setLevel(logging.WARNING)
            ch.setFormatter(logging.Formatter("%(levelname)s  %(message)s"))
            logger.addHandler(ch)
    except Exception:
        pass
    return logger


def log_exc(msg: str, exc: "BaseException | None" = None) -> None:
    """Strukturiertes Exception-Logging: WARNING + vollständiger Traceback als DEBUG."""
    logger = _get_logger()
    if exc is not None:
        logger.warning("%s: %s", msg, exc)
        logger.debug(traceback.format_exc())
    else:
        logger.warning(msg)
        logger.debug(traceback.format_exc())


# ---------------------------------------------------------------------------
# Atomic Write
# ---------------------------------------------------------------------------
def atomic_write(path: Path, content: str) -> None:
    """Schreibt eine Datei atomar unter Verwendung einer temporären Datei,
    vollständig kompatibel mit Python 3.8 (ohne mit_stem)."""
    path = Path(path)
    
    # Python 3.8 kompatibler Ersatz für path.with_stem():
    # Wir nehmen den alten Namen ohne Endung, hängen '._tmp_' an und fügen den Suffix wieder an.
    tmp = path.with_name(path.stem + "._tmp_" + path.suffix)
    
    try:
        tmp.write_text(content, encoding="utf-8")
        if tmp.exists():
            if path.exists():
                try:
                    path.unlink()
                except Exception:
                    pass
            tmp.replace(path)
    except Exception as e:
        if tmp.exists():
            try:
                tmp.unlink()
            except Exception:
                pass
        raise e


# ---------------------------------------------------------------------------
# Einstellungen
# ---------------------------------------------------------------------------
def load_settings() -> dict:
    if SETTINGS_FILE.exists():
        try:
            return json.loads(SETTINGS_FILE.read_text(encoding="utf-8"))
        except Exception as e:
            log_exc("settings.json konnte nicht geladen werden – Standardwerte werden verwendet", e)
    return {"language": FALLBACK_LANG}


def save_settings(settings: dict) -> None:
    atomic_write(SETTINGS_FILE, json.dumps(settings, indent=2, ensure_ascii=False))


# ---------------------------------------------------------------------------
# Theme  (UI-Farben – wird von apply_theme() in Calc2.py verwendet)
# ---------------------------------------------------------------------------
THEME_LIGHT: Dict[str, str] = {
    "hl_function":  "#2E86C1",
    "hl_cell":      "#1E8449",
    "hl_string":    "#7B241C",
    "hl_number":    "#D68910",
    "hl_operator":  "#8E44AD",
    "ui_team_fg":   "#1a4a8a",
    "ui_net_ok":    "#2a7a2a",
    "ui_net_err":   "#c00000",
    "ui_net_off":   "#888888",
    "ui_warning":   "#c06000",
    "ui_info":      "#888888",
    "ui_err_bg":    "#ffe0e0",
    "ui_err_border":"#c00000",
}

THEME_DARK: Dict[str, str] = {
    "hl_function":  "#6ab0f5",
    "hl_cell":      "#5dba7d",
    "hl_string":    "#f28b82",
    "hl_number":    "#ffb74d",
    "hl_operator":  "#ce93d8",
    "ui_team_fg":   "#90caf9",
    "ui_net_ok":    "#66bb6a",
    "ui_net_err":   "#ef5350",
    "ui_net_off":   "#aaaaaa",
    "ui_warning":   "#ffb74d",
    "ui_info":      "#aaaaaa",
    "ui_err_bg":    "#4a1a1a",
    "ui_err_border":"#ef5350",
}

THEME: Dict[str, str] = THEME_LIGHT
