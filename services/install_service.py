"""
services/install_service.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Erster-Start-Setup und Desktop-Verknüpfungen.

_first_run_install() verwendet QMessageBox für Fehlermeldungen –
das ist der einzige UI-Berührungspunkt in dieser Datei.
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from .settings_service import (
    RESOURCE_DIR, DATA_DIR, SETTINGS_FILE, LANG_FILE,
    FALLBACK_LANG, FALLBACK_MESSAGES, Config, log_exc,
)


# ---------------------------------------------------------------------------
# Hilfsfunktionen: Desktop-Pfad ermitteln
# ---------------------------------------------------------------------------
def get_desktop_path() -> str:
    if sys.platform == "win32":
        try:
            import winreg
            key = winreg.OpenKey(
                winreg.HKEY_CURRENT_USER,
                r"Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders",
            )
            desktop, _ = winreg.QueryValueEx(key, "Desktop")
            winreg.CloseKey(key)
            return desktop
        except Exception as e:
            log_exc("Registry-Abfrage für Desktop-Pfad fehlgeschlagen", e)
        return os.path.join(
            os.environ.get("USERPROFILE", os.path.expanduser("~")), "Desktop"
        )
    elif sys.platform == "darwin":
        return os.path.join(os.path.expanduser("~"), "Desktop")
    else:
        try:
            result = subprocess.run(
                ["xdg-user-dir", "DESKTOP"], capture_output=True, text=True
            )
            path = result.stdout.strip()
            if path and os.path.isdir(path):
                return path
        except Exception as e:
            log_exc("xdg-user-dir konnte Desktop-Pfad nicht ermitteln", e)
        return os.path.join(os.path.expanduser("~"), "Desktop")


# ---------------------------------------------------------------------------
# Plattform-spezifische Verknüpfungs-Erstellung
# ---------------------------------------------------------------------------
def _create_shortcut_windows(exe: str, desktop: str,
                              name: str, comment: str) -> bool:
    lnk = os.path.join(desktop, f"{name}.lnk")
    ps  = (
        f'$ws = New-Object -ComObject WScript.Shell\n'
        f'$sc = $ws.CreateShortcut("{lnk}")\n'
        f'$sc.TargetPath = "{exe}"\n'
        f'$sc.WorkingDirectory = "{os.path.dirname(exe)}"\n'
        f'$sc.Description = "{comment}"\n'
        f'$sc.Save()\n'
    )
    tmp = tempfile.NamedTemporaryFile(
        mode="w", suffix=".ps1", delete=False, encoding="utf-8"
    )
    tmp.write(ps)
    tmp.close()
    try:
        result = subprocess.run(
            ["powershell", "-NoProfile", "-NonInteractive",
             "-ExecutionPolicy", "Bypass", "-File", tmp.name],
            capture_output=True, text=True, timeout=15,
        )
        return result.returncode == 0
    except Exception as e:
        log_exc("PowerShell-Verknüpfung konnte nicht erstellt werden", e)
        return False
    finally:
        try:
            os.unlink(tmp.name)
        except Exception as e:
            log_exc("Temp-Datei konnte nicht gelöscht werden", e)


def _create_shortcut_macos(exe: str, desktop: str, name: str) -> bool:
    cmd_file = os.path.join(desktop, f"{name}.command")
    try:
        with open(cmd_file, "w", encoding="utf-8") as f:
            f.write("#!/bin/bash\n")
            f.write(f'"{exe}"\n')
        os.chmod(cmd_file, 0o755)
        return True
    except Exception as e:
        log_exc("macOS-Verknüpfung konnte nicht erstellt werden", e)
        return False


def _create_shortcut_linux(exe: str, desktop: str,
                            name: str, comment: str) -> bool:
    desktop_file = os.path.join(desktop, "CalcFormelHelper.desktop")
    try:
        content = (
            "[Desktop Entry]\nVersion=1.0\nType=Application\n"
            f"Name={name}\nComment={comment}\nExec={exe}\n"
            f"Path={os.path.dirname(exe)}\nIcon=libreoffice-calc\n"
            "Terminal=false\nCategories=Office;Utility;\n"
        )
        with open(desktop_file, "w", encoding="utf-8") as f:
            f.write(content)
        os.chmod(desktop_file, 0o755)
        return True
    except Exception as e:
        log_exc("Linux .desktop-Datei konnte nicht erstellt werden", e)
        return False


def create_desktop_shortcut(name: str = Config.SHORTCUT_NAME,
                             comment: str = Config.SHORTCUT_COMMENT) -> bool:
    exe     = sys.executable
    desktop = get_desktop_path()
    os.makedirs(desktop, exist_ok=True)
    if sys.platform == "win32":
        return _create_shortcut_windows(exe, desktop, name, comment)
    elif sys.platform == "darwin":
        return _create_shortcut_macos(exe, desktop, name)
    else:
        return _create_shortcut_linux(exe, desktop, name, comment)


# ---------------------------------------------------------------------------
# Sprachtext für Pre-UI-Meldungen
# ---------------------------------------------------------------------------
def _load_early_lang() -> dict:
    try:
        lang_code = FALLBACK_LANG
        if SETTINGS_FILE.exists():
            lang_code = json.loads(
                SETTINGS_FILE.read_text(encoding="utf-8")
            ).get("language", FALLBACK_LANG)
        if LANG_FILE.exists():
            all_langs = json.loads(LANG_FILE.read_text(encoding="utf-8"))
            return all_langs.get(lang_code) or all_langs.get(FALLBACK_LANG) or {}
    except Exception as e:
        log_exc("Frühe Sprachdatei konnte nicht geladen werden", e)
    return {}


# ---------------------------------------------------------------------------
# Erster-Start-Setup
# ---------------------------------------------------------------------------
def first_run_install() -> None:
    """
    Wird nur einmal (beim ersten Start des frozen Builds) ausgeführt.
    Kopiert Ressourcen, erstellt Desktop-Verknüpfung, schreibt .installed-Marker.
    """
    marker = DATA_DIR / Config.INSTALL_MARKER
    if marker.exists():
        return

    # Import hier – QMessageBox nur wenn wirklich nötig
    from PyQt5.QtWidgets import QMessageBox

    lang          = _load_early_lang()
    sc_name       = lang.get("desktop_shortcut_name",    Config.SHORTCUT_NAME)
    sc_comment    = lang.get("desktop_shortcut_comment", Config.SHORTCUT_COMMENT)
    install_title = lang.get("install_error_title",
                             FALLBACK_MESSAGES["install_error_title"])

    desktop = Path(get_desktop_path())
    desktop.mkdir(parents=True, exist_ok=True)
    shortcut_ok = False

    if sys.platform == "win32":
        exe_src = Path(sys.executable)
        exe_dst = DATA_DIR / exe_src.name
        try:
            if not exe_dst.exists():
                shutil.copy2(exe_src, exe_dst)
        except Exception as e:
            msg = lang.get(
                "install_error_exe_copy",
                FALLBACK_MESSAGES["install_error_exe_copy"],
            ).format(error=e)
            QMessageBox.critical(None, install_title, msg)
            return
        for src in RESOURCE_DIR.iterdir():
            dst = DATA_DIR / src.name
            if src.is_file() and not dst.exists():
                try:
                    shutil.copy2(src, dst)
                except Exception as e:
                    log_exc(f"Ressource konnte nicht kopiert werden: {src.name}", e)
        shortcut_ok = _create_shortcut_windows(
            str(exe_dst), str(desktop), sc_name, sc_comment
        )

    elif sys.platform == "darwin":
        app_src = RESOURCE_DIR / Config.APP_BUNDLE_MAC
        app_dst = desktop      / Config.APP_BUNDLE_MAC
        try:
            if app_src.exists() and not app_dst.exists():
                shutil.copytree(app_src, app_dst)
        except Exception as e:
            msg = lang.get(
                "install_error_app_copy",
                FALLBACK_MESSAGES["install_error_app_copy"],
            ).format(error=e)
            QMessageBox.critical(None, install_title, msg)
            return
        cmd_file = desktop / f"{sc_name}.command"
        try:
            cmd_file.write_text(f'#!/bin/bash\nopen "{app_dst}"\n', encoding="utf-8")
            cmd_file.chmod(0o755)
            shortcut_ok = True
        except Exception as e:
            log_exc("macOS Start-Script konnte nicht erstellt werden", e)
            shortcut_ok = False

    else:
        bin_src = Path(sys.executable)
        bin_dst = desktop / Config.APP_FILE_LINUX
        try:
            if not bin_dst.exists():
                shutil.copy2(bin_src, bin_dst)
                bin_dst.chmod(0o755)
        except Exception as e:
            msg = lang.get(
                "install_error_exe_copy",
                FALLBACK_MESSAGES["install_error_exe_copy"],
            ).format(error=e)
            QMessageBox.critical(None, install_title, msg)
            return
        shortcut_ok = _create_shortcut_linux(
            str(bin_dst), str(desktop), sc_name, sc_comment
        )

    try:
        marker.write_text("1", encoding="utf-8")
    except Exception as e:
        log_exc("Install-Marker konnte nicht geschrieben werden", e)

    if not shortcut_ok:
        sc_title = lang.get("msg_shortcut_title", FALLBACK_MESSAGES["msg_shortcut_title"])
        sc_body  = lang.get("msg_shortcut_body",  FALLBACK_MESSAGES["msg_shortcut_body"])
        QMessageBox.warning(None, sc_title, sc_body)
