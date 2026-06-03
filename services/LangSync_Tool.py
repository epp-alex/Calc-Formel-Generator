"""
LangSync Tool – Language code sync against libreoffice_calc_translations.json
Run from the Calc2 project folder: python LangSync_Tool.py python LangSync_Tool.py
Nutzt PyQt5.

Prüft:
  • languages.json
  • formula_explanations.json
  • rtl_languages.json
  gegen die Sprachcodes in libreoffice_calc_translations.json (Master).

Zeigt:
  • Codes die in lokalen Dateien vorhanden sind, aber NICHT im Master  → mögliche Tippfehler / veraltete Codes
  • Ähnliche Codes aus dem Master als Vorschlag
  • Möglichkeit: Code in ALLEN Dateien gleichzeitig umbenennen
"""

import sys
from typing import Dict, Optional, Union
import json
from pathlib import Path
from difflib import get_close_matches

from PyQt5.QtCore    import Qt, QTimer
from PyQt5.QtGui     import QFont, QColor
from PyQt5.QtWidgets import (
    QApplication, QDialog, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QTreeWidget, QTreeWidgetItem,
    QMessageBox, QFileDialog, QSplitter, QWidget,
    QLineEdit, QGroupBox, QAbstractItemView, QFrame,
    QHeaderView, QTextEdit
)

# ──────────────────────────────────────────────────────────────────────────────
# Pfad-Konstanten  (relativ zum Skript)
# ──────────────────────────────────────────────────────────────────────────────
# Direkt gestartet: services/LangSync_Tool.py → zwei Ebenen hoch zu Calc2/
# Aus Calc2.py gestartet: base_dir=_here wird übergeben → _HERE wird nicht genutzt
_HERE = Path(__file__).resolve().parent.parent
LANG_DIR = _HERE / "language"

FILE_LO     = LANG_DIR / "libreoffice_calc_translations.json"   # Master
FILE_LANG   = LANG_DIR / "languages.json"
FILE_EXPL   = LANG_DIR / "formula_explanations.json"
FILE_RTL    = LANG_DIR / "rtl_languages.json"

# ──────────────────────────────────────────────────────────────────────────────
# Hilfsfunktionen
# ──────────────────────────────────────────────────────────────────────────────

def _load(path: Path) -> Optional[Union[dict, list]]:
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        return None


def _save(path: Path, data) -> Optional[str]:
    """Speichert JSON, gibt Fehlermeldung zurück oder None bei Erfolg."""
    try:
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        return None
    except Exception as e:
        return str(e)


def _lo_lang_codes(lo_data: dict) -> set:
    """Alle Sprachcodes aus dem ersten Eintrag von libreoffice_calc_translations.json."""
    if not lo_data:
        return set()
    return set(next(iter(lo_data.values())).keys())


def _lang_codes_from_dict(data: dict) -> set:
    """Top-Level-Keys einer JSON-Dict die keine _ haben (= Sprachcodes)."""
    return {k for k in data if not k.startswith("_")}


def _lang_codes_from_rtl(data: dict) -> set:
    return set(data.get("codes", []))


def _similar(code: str, master: set, n: int = 6) -> list:
    """Ähnliche Codes aus dem Master per difflib + Präfix-Suche."""
    close = get_close_matches(code, master, n=n, cutoff=0.6)
    prefix = [c for c in sorted(master) if c.startswith(code[:2]) and c not in close]
    combined = close + prefix
    # deduplizieren, Reihenfolge behalten
    seen = set()
    result = []
    for c in combined:
        if c not in seen:
            seen.add(c)
            result.append(c)
    return result[:8]


# ──────────────────────────────────────────────────────────────────────────────
# Haupt-Dialog
# ──────────────────────────────────────────────────────────────────────────────

class LangSyncTool(QDialog):
    def __init__(self, parent=None, base_dir: Optional[Path] = None):
        super().__init__(parent)
        # Pfade überschreiben wenn base_dir übergeben wird (Aufruf aus Calc2)
        if base_dir:
            global LANG_DIR, FILE_LO, FILE_LANG, FILE_EXPL, FILE_RTL
            LANG_DIR  = base_dir / "language"
            FILE_LO   = LANG_DIR / "libreoffice_calc_translations.json"
            FILE_LANG = LANG_DIR / "languages.json"
            FILE_EXPL = LANG_DIR / "formula_explanations.json"
            FILE_RTL  = LANG_DIR / "rtl_languages.json"
        self.setWindowTitle("LangSync Tool  –  Language Code Sync")
        self.setMinimumSize(860, 600)
        self.resize(980, 680)
        self.setWindowFlags(self.windowFlags() | Qt.WindowMaximizeButtonHint)

        # Daten
        self._lo_data:   dict = {}
        self._lo_codes:  set  = set()
        self._issues:    list = []   # Liste von Problem-Dicts

        self._build_ui()
        QTimer.singleShot(100, self._run_check)

    # ── UI ────────────────────────────────────────────────────────────────────

    def _build_ui(self):
        root = QVBoxLayout(self)
        root.setSpacing(8)
        root.setContentsMargins(12, 12, 12, 12)

        # ── Kopf ──────────────────────────────────────────────────────────────
        header = QLabel(
            "<b>LangSync Tool</b> – All local JSON files are cross-checked against "
            "<code>libreoffice_calc_translations.json</code>."
        )
        header.setWordWrap(True)
        root.addWidget(header)

        # ── Pfad-Anzeige ──────────────────────────────────────────────────────
        pbox = QGroupBox("Verified Files")
        pbox_lay = QVBoxLayout(pbox)
        self._path_labels: Dict[str, QLabel] = {}
        for name, path in [
            ("Master (LO)",          FILE_LO),
            ("languages.json",       FILE_LANG),
            ("formula_explanations", FILE_EXPL),
        ]:
            row = QHBoxLayout()
            lbl_name = QLabel(f"<b>{name}</b>")
            lbl_name.setFixedWidth(170)
            lbl_path = QLabel(str(path))
            lbl_path.setStyleSheet("color: #555; font-size: 11px;")
            lbl_path.setWordWrap(True)
            self._status_lbl = QLabel()
            row.addWidget(lbl_name)
            row.addWidget(lbl_path, 1)
            pbox_lay.addLayout(row)
        root.addWidget(pbox)

        # ── Ergebnis-Baum ─────────────────────────────────────────────────────
        self._tree = QTreeWidget()
        self._tree.setHeaderLabels(["File / Code", "Issue", "Similar Codes in Master"])
        self._tree.header().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self._tree.header().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self._tree.header().setSectionResizeMode(2, QHeaderView.Stretch)
        self._tree.setAlternatingRowColors(True)
        self._tree.setSelectionMode(QAbstractItemView.SingleSelection)
        self._tree.itemSelectionChanged.connect(self._on_select)
        root.addWidget(self._tree, 1)

        # ── Aktionsbereich ────────────────────────────────────────────────────
        act_box = QGroupBox("Action – Correct Selected Code")
        act_lay = QHBoxLayout(act_box)

        self._lbl_selected = QLabel("No code selected.")
        self._lbl_selected.setFixedWidth(220)
        act_lay.addWidget(self._lbl_selected)

        act_lay.addWidget(QLabel("Rename to:"))
        self._inp_new = QLineEdit()
        self._inp_new.setPlaceholderText("e.g.  pt-BR")
        self._inp_new.setFixedWidth(130)
        act_lay.addWidget(self._inp_new)

        self._btn_rename = QPushButton("✔  Rename in all files")
        self._btn_rename.setStyleSheet(
            "background:#2e7d32; color:white; font-weight:bold; padding:6px 14px;")
        self._btn_rename.setEnabled(False)
        self._btn_rename.clicked.connect(self._do_rename)
        act_lay.addWidget(self._btn_rename)

        act_lay.addStretch()

        self._btn_recheck = QPushButton("🔄  Re-check")
        self._btn_recheck.clicked.connect(self._run_check)
        act_lay.addWidget(self._btn_recheck)

        root.addWidget(act_box)

        # ── Statuszeile ───────────────────────────────────────────────────────
        self._status = QLabel("Checking …")
        self._status.setStyleSheet("color:#555; font-size:11px;")
        root.addWidget(self._status)

    # ── Prüflogik ─────────────────────────────────────────────────────────────

    def _run_check(self):
        self._tree.clear()
        self._issues.clear()
        self._inp_new.clear()
        self._btn_rename.setEnabled(False)
        self._lbl_selected.setText("No code selected.")

        # Load master
        lo_raw = _load(FILE_LO)
        if not lo_raw:
            self._status.setText(
                f"❌  libreoffice_calc_translations.json not found: {FILE_LO}")
            return
        self._lo_data  = lo_raw
        self._lo_codes = _lo_lang_codes(lo_raw)

        checks = [
            ("languages.json",       FILE_LANG,  "dict"),
            ("formula_explanations", FILE_EXPL,  "dict"),
            # rtl_languages.json is NOT checked against LO master –
            # it only defines text direction, not LO language support.
        ]

        total_issues = 0

        for label, path, kind in checks:
            data = _load(path)
            if data is None:
                item = QTreeWidgetItem(self._tree, [label, "⚠️  File not found", ""])
                item.setForeground(1, QColor("#e65100"))
                continue

            if kind == "dict":
                local_codes = _lang_codes_from_dict(data)
            else:
                local_codes = _lang_codes_from_rtl(data)

            not_in_master = sorted(local_codes - self._lo_codes)

            if not not_in_master:
                item = QTreeWidgetItem(self._tree, [label, "✅  All codes OK", ""])
                item.setForeground(1, QColor("#2e7d32"))
                continue

            parent = QTreeWidgetItem(self._tree,
                [label,
                 f"⚠️  {len(not_in_master)} code(s) not in Master", ""])
            parent.setForeground(1, QColor("#c62828"))
            fnt = parent.font(0)
            fnt.setBold(True)
            parent.setFont(0, fnt)

            for code in not_in_master:
                similar = _similar(code, self._lo_codes)
                sim_str = ",  ".join(similar) if similar else "–"
                child = QTreeWidgetItem(parent,
                    [f"  {code}", "Not found in LO", sim_str])
                child.setForeground(1, QColor("#c62828"))
                child.setForeground(2, QColor("#1565c0"))
                # Metadata for action
                child.setData(0, Qt.UserRole, {
                    "code":    code,
                    "file":    path,
                    "kind":    kind,
                    "similar": similar,
                })
                self._issues.append({
                    "code": code, "file": path, "kind": kind})
                total_issues += 1

            parent.setExpanded(True)

        if total_issues == 0:
            self._status.setText(
                f"✅  All codes in all files match the master. "
                f"({len(self._lo_codes)} codes in Master)")
        else:
            self._status.setText(
                f"⚠️  {total_issues} issue(s) found.  "
                f"Select a code → enter new code → Rename.")

    # ── Auswahl ───────────────────────────────────────────────────────────────

    def _on_select(self):
        items = self._tree.selectedItems()
        if not items:
            self._btn_rename.setEnabled(False)
            self._lbl_selected.setText("No code selected.")
            return
        item = items[0]
        meta = item.data(0, Qt.UserRole)
        if not meta:
            self._btn_rename.setEnabled(False)
            self._lbl_selected.setText("Please select a code entry.")
            return

        code    = meta["code"]
        similar = meta["similar"]
        self._selected_meta = meta
        self._lbl_selected.setText(f"Selected::  <b>{code}</b>")
        self._btn_rename.setEnabled(True)

        # Suggest closest match
        if similar:
            self._inp_new.setPlaceholderText(f"e.g.  {similar[0]}")
        else:
            self._inp_new.setPlaceholderText("New code …")

    # ── Umbenennen ────────────────────────────────────────────────────────────

    def _do_rename(self):
        meta     = getattr(self, "_selected_meta", None)
        if not meta:
            return

        old_code = meta["code"]
        new_code = self._inp_new.text().strip()

        if not new_code:
            QMessageBox.warning(self, "No code", "Please enter a new code.")
            return

        if new_code == old_code:
            QMessageBox.information(self, "No change", "Old and new code are identical.")
            return

        # Check if new code exists in master
        if self._lo_codes and new_code not in self._lo_codes:
            similar = _similar(new_code, self._lo_codes)
            hint = f"\n\nSimilar codes in Master: {', '.join(similar)}" if similar else ""
            ans = QMessageBox.warning(self, "⚠️  New code not in Master",
                f'"{new_code}" is ALSO not in libreoffice_calc_translations.json.{hint}\n\n'
                f'Rename anyway?',
                QMessageBox.Yes | QMessageBox.No)
            if ans != QMessageBox.Yes:
                return

        # Confirmation
        ans = QMessageBox.question(self, "Confirm rename",
            f'Code  "{old_code}"  →  "{new_code}"\n\n'
            f'will be renamed in ALL JSON files.\n'
            f'Proceed?',
            QMessageBox.Yes | QMessageBox.No)
        if ans != QMessageBox.Yes:
            return

        errors  = []
        changed = []

        # ── languages.json ────────────────────────────────────────────────────
        lang_data = _load(FILE_LANG)
        if isinstance(lang_data, dict) and old_code in lang_data:
            lang_data[new_code] = lang_data.pop(old_code)
            err = _save(FILE_LANG, lang_data)
            if err:
                errors.append(f"languages.json: {err}")
            else:
                changed.append("languages.json")

        # ── formula_explanations.json ─────────────────────────────────────────
        expl_data = _load(FILE_EXPL)
        if isinstance(expl_data, dict) and old_code in expl_data:
            expl_data[new_code] = expl_data.pop(old_code)
            err = _save(FILE_EXPL, expl_data)
            if err:
                errors.append(f"formula_explanations.json: {err}")
            else:
                changed.append("formula_explanations.json")

        # ── rtl_languages.json ────────────────────────────────────────────────
        rtl_data = _load(FILE_RTL)
        if isinstance(rtl_data, dict):
            codes = rtl_data.get("codes", [])
            if old_code in codes:
                codes[codes.index(old_code)] = new_code
                rtl_data["codes"] = codes
                err = _save(FILE_RTL, rtl_data)
                if err:
                    errors.append(f"rtl_languages.json: {err}")
                else:
                    changed.append("rtl_languages.json")

        # ── Ergebnis ──────────────────────────────────────────────────────────
        if errors:
            QMessageBox.critical(self, "Error",
                "The following files could not be saved:\n\n" +
                "\n".join(errors))
        else:
            summary = "\n".join(f"  ✅  {f}" for f in changed) if changed else "  (no changes)"
            QMessageBox.information(self, "Done",
                f'"{old_code}"  was renamed to  "{new_code}"\n\n'
                f'Changed files:\n{summary}')

        # Re-check
        self._run_check()


# ──────────────────────────────────────────────────────────────────────────────
# Einstiegspunkt
# ──────────────────────────────────────────────────────────────────────────────

def run(base_dir: Optional[Path] = None):
    """Kann aus Calc2.py aufgerufen werden: LangSyncTool.run(base_dir=_HERE)"""
    global LANG_DIR, FILE_LO, FILE_LANG, FILE_EXPL, FILE_RTL
    if base_dir:
        LANG_DIR  = base_dir / "language"
        FILE_LO   = LANG_DIR / "libreoffice_calc_translations.json"
        FILE_LANG = LANG_DIR / "languages.json"
        FILE_EXPL = LANG_DIR / "formula_explanations.json"
        FILE_RTL  = LANG_DIR / "rtl_languages.json"
    app = QApplication.instance() or QApplication(sys.argv)
    dlg = LangSyncTool()
    dlg.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg = LangSyncTool()
    dlg.show()
    sys.exit(app.exec_())
