#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Plugin Manager for Calc2
═══════════════════════════════════════════════════════════════════════════════
A standalone tool for creating and editing Calc2 plugins.

Features:
  1. Create a new plugin (step-by-step wizard)
  2. Add formulas to an existing plugin
  3. Add/edit language translations for a plugin

Usage:
  python plugin_manager.py

Place this file in the same folder as Calc2.py.
═══════════════════════════════════════════════════════════════════════════════
"""

import json
from typing import Dict, List, Optional, Tuple
import os
import re
import shutil
import sys
import zipfile
from pathlib import Path

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont, QColor, QPalette, QIcon
from PyQt5.QtWidgets import (
    QApplication, QComboBox, QDialog, QDialogButtonBox,
    QFormLayout, QFrame, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QMessageBox, QPushButton, QScrollArea, QSizePolicy,
    QStackedWidget, QStatusBar, QTabWidget, QTextEdit,
    QVBoxLayout, QWidget, QInputDialog, QSplitter,
    QAbstractItemView,
)

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

APP_NAME    = "Calc2 Plugin Manager"
APP_VERSION = "1.0.0"

# All languages supported by Calc2
HERE         = Path(__file__).resolve().parent
def load_languages_from_json():
    """Lädt Sprachen dynamisch aus dem Unterordner 'language/languages.json'."""
    # Pfad: ./language/languages.json
    json_path = HERE / "language" / "languages.json"
    
    # Standard-Fallback
    default_langs = [("de", "🇩🇪 Deutsch"), ("en", "🇺🇸 English")]
    
    if not json_path.exists():
        print(f"Hinweis: {json_path} nicht gefunden.")
        return default_langs

    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        langs = []
        for code, content in data.items():
            # Wir extrahieren den Anzeigenamen aus dem _meta-Block
            if isinstance(content, dict) and "_meta" in content:
                display_name = content["_meta"].get("name", code)
                langs.append((code, display_name))
        
        # Sortierung für eine schönere Liste im UI
        langs.sort(key=lambda x: x[1])
        
        return langs if langs else default_langs
    except Exception as e:
        print(f"Fehler beim Parsen der languages.json: {e}")
        return default_langs

# Automatische Zuweisung
ALL_LANGUAGES = load_languages_from_json()
LANG_CODES = [c for c, _ in ALL_LANGUAGES]

# Plugins folder: same directory as this script
PLUGINS_DIR  = HERE / "plugins"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _plugins_dir() -> Path:
    PLUGINS_DIR.mkdir(exist_ok=True)
    return PLUGINS_DIR


def _plugin_id_from_name(name: str) -> str:
    """Convert display name to safe folder id: 'My Plugin 1' → 'my_plugin_1'"""
    s = name.lower().strip()
    s = re.sub(r"[^\w\s]", "", s)
    s = re.sub(r"\s+", "_", s)
    return s or "plugin"


def _load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None


def _save_json(path: Path, data) -> bool:
    try:
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        return True
    except Exception as e:
        QMessageBox.critical(None, "Save Error", f"Could not save file:\n{path}\n\n{e}")
        return False


def _normalize_formula(formula: str) -> str:
    """
    Ensure formula uses the =@ prefix for cross-language compatibility.
    =SUM(...)  →  =@SUM(...)
    =@SUM(...) stays unchanged.
    Strings without leading '=' are returned as-is.
    """
    f = formula.strip()
    if f.startswith("=@"):
        return f          # already correct
    if f.startswith("="):
        return "=@" + f[1:]
    return f              # not a formula expression


def _get_formula_display(formula_field) -> str:
    """Return English formula string for display (formula field may be str or dict)."""
    if isinstance(formula_field, dict):
        return formula_field.get("en", "")
    return str(formula_field) if formula_field else ""


def _scan_plugins() -> List[Path]:
    """Return list of plugin directories that contain plugin.json."""
    base = _plugins_dir()
    result = []
    for entry in sorted(base.iterdir()):
        if entry.is_dir() and not entry.name.startswith(("_", ".")):
            if (entry / "plugin.json").exists():
                result.append(entry)
    return result


def _hr() -> QFrame:
    """Horizontal separator line."""
    f = QFrame()
    f.setFrameShape(QFrame.HLine)
    f.setFrameShadow(QFrame.Sunken)
    return f


def _bold_label(text: str, size: int = 10) -> QLabel:
    lbl = QLabel(text)
    font = QFont()
    font.setPointSize(size)
    font.setBold(True)
    lbl.setFont(font)
    return lbl


def _info_label(text: str) -> QLabel:
    lbl = QLabel(text)
    lbl.setWordWrap(True)
    lbl.setStyleSheet("color: #666; font-style: italic;")
    return lbl


# ---------------------------------------------------------------------------
# Step indicator widget
# ---------------------------------------------------------------------------

class StepIndicator(QWidget):
    """Shows numbered step circles: ①──②──③"""

    def __init__(self, steps: List[str], parent=None):
        super().__init__(parent)
        self.steps   = steps
        self.current = 0
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 4, 0, 4)
        self._labels: List[QLabel] = []
        for i, title in enumerate(steps):
            if i > 0:
                sep = QLabel("──")
                sep.setStyleSheet("color: #aaa;")
                layout.addWidget(sep)
            lbl = QLabel(f"  {i+1}. {title}  ")
            lbl.setAlignment(Qt.AlignCenter)
            lbl.setFixedHeight(28)
            layout.addWidget(lbl)
            self._labels.append(lbl)
        self._refresh()

    def set_step(self, index: int):
        self.current = index
        self._refresh()

    def _refresh(self):
        for i, lbl in enumerate(self._labels):
            if i < self.current:
                lbl.setStyleSheet(
                    "background:#4CAF50; color:white; border-radius:4px; font-weight:bold;"
                )
            elif i == self.current:
                lbl.setStyleSheet(
                    "background:#2196F3; color:white; border-radius:4px; font-weight:bold;"
                )
            else:
                lbl.setStyleSheet(
                    "background:#ddd; color:#888; border-radius:4px;"
                )


# ---------------------------------------------------------------------------
# Wizard page base
# ---------------------------------------------------------------------------

class WizardPage(QWidget):
    """Base class for wizard pages."""

    title       = "Page"
    description = ""

    def is_valid(self) -> Tuple[bool, str]:
        """Return (True, '') if page data is valid, else (False, error_message)."""
        return True, ""

    def get_data(self) -> dict:
        return {}


# ---------------------------------------------------------------------------
# Wizard: Create New Plugin
# ---------------------------------------------------------------------------

class NewPlugin_Step1_Meta(WizardPage):
    title       = "Basic Info"
    description = "Enter the basic information about your plugin. English is required – other languages are optional."

    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.setSpacing(12)

        layout.addWidget(_bold_label("Plugin Identity", 10))
        layout.addWidget(_info_label(
            "The plugin ID is the folder name (auto-generated from English name). "
            "Use a clear, descriptive English name."
        ))

        form = QFormLayout()
        form.setSpacing(8)

        self.name_en    = QLineEdit()
        self.name_en.setPlaceholderText("e.g. Finance Formulas")
        self.desc_en    = QTextEdit()
        self.desc_en.setPlaceholderText("e.g. Useful formulas for financial calculations.")
        self.desc_en.setFixedHeight(60)
        self.version    = QLineEdit("1.0")
        self.author     = QLineEdit()
        self.author.setPlaceholderText("e.g. Your Name")
        self.icon       = QLineEdit()
        self.icon.setPlaceholderText("e.g. 💰  (optional emoji)")
        self.icon.setFixedWidth(80)

        form.addRow("Name (English) *", self.name_en)
        form.addRow("Description (English)", self.desc_en)
        form.addRow("Version", self.version)
        form.addRow("Author", self.author)
        form.addRow("Icon (emoji)", self.icon)

        layout.addLayout(form)
        layout.addStretch()

    def is_valid(self):
        if not self.name_en.text().strip():
            return False, "Please enter an English name for the plugin."
        return True, ""

    def get_data(self):
        return {
            "name_en":  self.name_en.text().strip(),
            "desc_en":  self.desc_en.toPlainText().strip(),
            "version":  self.version.text().strip() or "1.0",
            "author":   self.author.text().strip(),
            "icon":     self.icon.text().strip(),
        }


class NewPlugin_Step2_Formulas(WizardPage):
    title       = "Add Formulas"
    description = "Add at least one formula. You can add more later."

    def __init__(self, parent=None):
        super().__init__(parent)
        self._formulas: List[dict] = []

        layout = QVBoxLayout(self)
        layout.setSpacing(8)

        layout.addWidget(_bold_label("Formulas", 10))
        layout.addWidget(_info_label(
            "Add formulas for your plugin. Each formula needs a LibreOffice Calc formula string "
            "and an English name. Category and description are optional but recommended."
        ))

        # Formula list
        self._list = QListWidget()
        self._list.setAlternatingRowColors(True)
        self._list.setSelectionMode(QAbstractItemView.SingleSelection)
        self._list.itemDoubleClicked.connect(self._edit_formula)
        layout.addWidget(self._list)

        # Buttons
        btn_row = QHBoxLayout()
        self._btn_add  = QPushButton("➕  Add Formula")
        self._btn_edit = QPushButton("✏️  Edit")
        self._btn_del  = QPushButton("🗑  Remove")
        self._btn_add.clicked.connect(self._add_formula)
        self._btn_edit.clicked.connect(self._edit_formula)
        self._btn_del.clicked.connect(self._delete_formula)
        btn_row.addWidget(self._btn_add)
        btn_row.addWidget(self._btn_edit)
        btn_row.addWidget(self._btn_del)
        btn_row.addStretch()
        layout.addLayout(btn_row)

    def _add_formula(self):
        dlg = FormulaEditDialog(self)
        if dlg.exec_() == QDialog.Accepted:
            data = dlg.get_data()
            self._formulas.append(data)
            self._refresh_list()

    def _edit_formula(self, _item=None):
        row = self._list.currentRow()
        if row < 0:
            return
        dlg = FormulaEditDialog(self, self._formulas[row])
        if dlg.exec_() == QDialog.Accepted:
            self._formulas[row] = dlg.get_data()
            self._refresh_list()

    def _delete_formula(self):
        row = self._list.currentRow()
        if row < 0:
            return
        ans = QMessageBox.question(self, "Remove", "Remove this formula?")
        if ans == QMessageBox.Yes:
            self._formulas.pop(row)
            self._refresh_list()

    def _refresh_list(self):
        self._list.clear()
        for f in self._formulas:
            name = f.get("name", {}).get("en", "?")
            formula = _get_formula_display(f.get("formula", ""))
            cat = f.get("category", {}).get("en", "")
            text = f"[{cat}]  {name}  →  {formula}" if cat else f"{name}  →  {formula}"
            self._list.addItem(text)

    def is_valid(self):
        if not self._formulas:
            return False, "Please add at least one formula."
        return True, ""

    def get_data(self):
        return {"formulas": self._formulas}


class NewPlugin_Step3_Languages(WizardPage):
    title       = "Translations"
    description = "Add translations for the plugin name and description. English is already set."

    def __init__(self, parent=None):
        super().__init__(parent)
        self._translations: dict = {}   # { lang_code: {name, description} }

        layout = QVBoxLayout(self)
        layout.setSpacing(8)

        layout.addWidget(_bold_label("Plugin Translations", 10))
        layout.addWidget(_info_label(
            "English is the required fallback. Add other languages here. "
            "Formula translations can be added later via 'Edit Translations'."
        ))

        # Translation list
        self._list = QListWidget()
        self._list.setAlternatingRowColors(True)
        self._list.itemDoubleClicked.connect(self._edit_lang)
        layout.addWidget(self._list)

        btn_row = QHBoxLayout()
        self._btn_add  = QPushButton("➕  Add Language")
        self._btn_edit = QPushButton("✏️  Edit")
        self._btn_del  = QPushButton("🗑  Remove")
        self._btn_add.clicked.connect(self._add_lang)
        self._btn_edit.clicked.connect(self._edit_lang)
        self._btn_del.clicked.connect(self._delete_lang)
        btn_row.addWidget(self._btn_add)
        btn_row.addWidget(self._btn_edit)
        btn_row.addWidget(self._btn_del)
        btn_row.addStretch()
        layout.addLayout(btn_row)

    def _add_lang(self):
        used = set(self._translations.keys()) | {"en"}
        available = [(c, n) for c, n in ALL_LANGUAGES if c not in used]
        if not available:
            QMessageBox.information(self, "All Added", "All supported languages have been added.")
            return
        dlg = PluginTranslationDialog(available, self)
        if dlg.exec_() == QDialog.Accepted:
            code, name, desc = dlg.get_data()
            self._translations[code] = {"name": name, "description": desc}
            self._refresh_list()

    def _edit_lang(self, _item=None):
        row = self._list.currentRow()
        if row < 0:
            return
        code = list(self._translations.keys())[row]
        lang_name = dict(ALL_LANGUAGES).get(code, code)
        data = self._translations[code]
        dlg = PluginTranslationDialog(
            [(code, lang_name)], self,
            prefill_name=data.get("name", ""),
            prefill_desc=data.get("description", ""),
        )
        if dlg.exec_() == QDialog.Accepted:
            _, name, desc = dlg.get_data()
            self._translations[code] = {"name": name, "description": desc}
            self._refresh_list()

    def _delete_lang(self):
        row = self._list.currentRow()
        if row < 0:
            return
        code = list(self._translations.keys())[row]
        ans = QMessageBox.question(self, "Remove", f"Remove translation for '{code}'?")
        if ans == QMessageBox.Yes:
            del self._translations[code]
            self._refresh_list()

    def _refresh_list(self):
        self._list.clear()
        lang_map = dict(ALL_LANGUAGES)
        for code, data in self._translations.items():
            flag_name = lang_map.get(code, code)
            self._list.addItem(f"{flag_name}  –  {data.get('name', '')}")

    def get_data(self):
        return {"translations": self._translations}


class NewPlugin_Step4_Summary(WizardPage):
    title       = "Summary"
    description = "Review your plugin before saving."

    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.setSpacing(8)
        layout.addWidget(_bold_label("Plugin Summary", 10))
        self._text = QTextEdit()
        self._text.setReadOnly(True)
        layout.addWidget(self._text)

    def set_summary(self, meta: dict, formulas: list, translations: dict):
        lang_list = ", ".join(translations.keys()) if translations else "none"
        lines = [
            f"<b>Name:</b> {meta.get('name_en', '')}",
            f"<b>Folder ID:</b> {_plugin_id_from_name(meta.get('name_en', ''))}",
            f"<b>Version:</b> {meta.get('version', '1.0')}",
            f"<b>Author:</b> {meta.get('author', '–')}",
            f"<b>Icon:</b> {meta.get('icon', '–')}",
            f"<b>Formulas:</b> {len(formulas)}",
            f"<b>Extra languages:</b> {lang_list}",
            "",
            "<b>Formulas:</b>",
        ]
        for i, f in enumerate(formulas, 1):
            name = f.get("name", {}).get("en", "?")
            formula = _get_formula_display(f.get("formula", ""))
            lines.append(f"  {i}. {name}  →  <code>{formula}</code>")
        self._text.setHtml("<br>".join(lines))


# ---------------------------------------------------------------------------
# New Plugin Wizard
# ---------------------------------------------------------------------------

class NewPluginWizard(QDialog):
    """Step-by-step wizard to create a new plugin."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Create New Plugin")
        self.setMinimumSize(620, 500)
        self.resize(780, 600)

        self._pages: List[WizardPage] = [
            NewPlugin_Step1_Meta(),
            NewPlugin_Step2_Formulas(),
            NewPlugin_Step3_Languages(),
            NewPlugin_Step4_Summary(),
        ]
        self._current = 0

        root = QVBoxLayout(self)
        root.setSpacing(8)
        root.setContentsMargins(16, 12, 16, 12)

        # Title
        self._title_lbl = _bold_label("", 12)
        root.addWidget(self._title_lbl)

        self._desc_lbl = _info_label("")
        root.addWidget(self._desc_lbl)

        # Step indicator
        step_names = [p.title for p in self._pages]
        self._indicator = StepIndicator(step_names)
        root.addWidget(self._indicator)
        root.addWidget(_hr())

        # Page stack
        self._stack = QStackedWidget()
        for page in self._pages:
            self._stack.addWidget(page)
        root.addWidget(self._stack, stretch=1)

        root.addWidget(_hr())

        # Navigation buttons
        nav = QHBoxLayout()
        self._btn_back   = QPushButton("◀  Back")
        self._btn_next   = QPushButton("Next  ▶")
        self._btn_finish = QPushButton("✅  Create Plugin")
        self._btn_cancel = QPushButton("Cancel")
        self._btn_finish.setVisible(False)
        self._btn_back.clicked.connect(self._go_back)
        self._btn_next.clicked.connect(self._go_next)
        self._btn_finish.clicked.connect(self._finish)
        self._btn_cancel.clicked.connect(self.reject)
        nav.addWidget(self._btn_cancel)
        nav.addStretch()
        nav.addWidget(self._btn_back)
        nav.addWidget(self._btn_next)
        nav.addWidget(self._btn_finish)
        root.addLayout(nav)

        self._refresh()

    # ── Navigation ──────────────────────────────────────────────────────────

    def _refresh(self):
        page = self._pages[self._current]
        self._title_lbl.setText(f"Step {self._current + 1}: {page.title}")
        self._desc_lbl.setText(page.description)
        self._stack.setCurrentIndex(self._current)
        self._indicator.set_step(self._current)
        self._btn_back.setEnabled(self._current > 0)
        is_last = self._current == len(self._pages) - 1
        self._btn_next.setVisible(not is_last)
        self._btn_finish.setVisible(is_last)

    def _go_back(self):
        if self._current > 0:
            self._current -= 1
            self._refresh()

    def _go_next(self):
        page = self._pages[self._current]
        ok, msg = page.is_valid()
        if not ok:
            QMessageBox.warning(self, "Required", msg)
            return
        self._current += 1
        # Update summary on last page
        if self._current == len(self._pages) - 1:
            meta         = self._pages[0].get_data()
            formulas     = self._pages[1].get_data().get("formulas", [])
            translations = self._pages[2].get_data().get("translations", {})
            self._pages[3].set_summary(meta, formulas, translations)
        self._refresh()

    def _finish(self):
        """Build and save the plugin files."""
        meta         = self._pages[0].get_data()
        formulas     = self._pages[1].get_data().get("formulas", [])
        translations = self._pages[2].get_data().get("translations", {})

        plugin_id  = _plugin_id_from_name(meta["name_en"])
        plugin_dir = _plugins_dir() / plugin_id

        # Warn if folder already exists
        if plugin_dir.exists():
            ans = QMessageBox.question(
                self, "Overwrite?",
                f"Folder '{plugin_id}' already exists.\nOverwrite plugin.json and formulas.json?"
            )
            if ans != QMessageBox.Yes:
                return
        plugin_dir.mkdir(parents=True, exist_ok=True)

        # ── Build plugin.json ───────────────────────────────────────────────
        name_dict = {"en": meta["name_en"]}
        desc_dict = {"en": meta["desc_en"]} if meta["desc_en"] else {"en": ""}
        for code, t in translations.items():
            if t.get("name"):
                name_dict[code] = t["name"]
            if t.get("description"):
                desc_dict[code] = t["description"]

        plugin_json = {
            "id":      plugin_id,
            "enabled": True,
            "version": meta["version"],
            "author":  meta["author"],
            "icon":    meta["icon"],
            "min_app_version": "1.0.0",
            "name":        name_dict,
            "description": desc_dict,
        }
        if not _save_json(plugin_dir / "plugin.json", plugin_json):
            return

        # ── Build formulas.json ─────────────────────────────────────────────
        if not _save_json(plugin_dir / "formulas.json", formulas):
            return

        QMessageBox.information(
            self, "Plugin Created",
            f"Plugin '{meta['name_en']}' created successfully!\n\nLocation:\n{plugin_dir}"
        )
        self.accept()


# ---------------------------------------------------------------------------
# Formula Edit Dialog  – with per-language formula tab
# ---------------------------------------------------------------------------

class FormulaEditDialog(QDialog):
    """
    Dialog for adding or editing a single formula entry.

    Tab 1 – English (required):  formula, name, description, category
    Tab 2 – Translations:        per-language formula + name + description
                                 with Copy-EN / Paste workflow for AI translation
    """

    def __init__(self, parent=None, prefill: dict = None):
        super().__init__(parent)
        self.setWindowTitle("Edit Formula")
        self.setMinimumSize(640, 700)
        self.resize(700, 780)

        root = QVBoxLayout(self)
        root.setContentsMargins(12, 10, 12, 10)
        root.setSpacing(8)

        root.addWidget(_bold_label("Formula Entry", 10))

        tabs = QTabWidget()
        root.addWidget(tabs, stretch=1)

        # ── Tab 1: English ───────────────────────────────────────────────────
        tab_en = QWidget()
        en_layout = QVBoxLayout(tab_en)
        en_layout.setSpacing(8)
        en_layout.setContentsMargins(10, 10, 10, 10)
        en_layout.addWidget(_info_label(
            "English is required and serves as fallback for all languages. "
            "Add translations in the next tab."
        ))
        form_en = QFormLayout()
        form_en.setSpacing(8)

        self.formula     = QLineEdit()
        self.formula.setPlaceholderText("e.g. =SUM(A1:A10)")
        self.name_en     = QLineEdit()
        self.name_en.setPlaceholderText("e.g. Sum of range")
        self.desc_en     = QTextEdit()
        self.desc_en.setPlaceholderText("e.g. Adds all values in A1:A10.")
        self.desc_en.setFixedHeight(60)
        self.category_en = QLineEdit()
        self.category_en.setPlaceholderText("e.g. Basic")

        form_en.addRow("Formula *", self.formula)
        form_en.addRow("Name (EN) *", self.name_en)
        form_en.addRow("Description (EN)", self.desc_en)
        form_en.addRow("Category (EN)", self.category_en)
        en_layout.addLayout(form_en)

        # Copy-EN button
        btn_copy_en = QPushButton("📋  Copy English block for AI translation")
        btn_copy_en.setToolTip(
            "Copies formula, name, description and category to clipboard.\n"
            "Paste into an AI translator, translate, then use 'Paste translations' in Tab 2."
        )
        btn_copy_en.clicked.connect(self._copy_en_block)
        en_layout.addWidget(btn_copy_en)
        en_layout.addStretch()
        tabs.addTab(tab_en, "🇬🇧  English")

        # ── Tab 2: Translations ──────────────────────────────────────────────
        tab_tr = QWidget()
        tr_layout = QVBoxLayout(tab_tr)
        tr_layout.setSpacing(6)
        tr_layout.setContentsMargins(10, 8, 10, 8)
        tr_layout.addWidget(_info_label(
            "Enter the formula, name and description for each language. "
            "Formula must use the function names of that language "
            "(e.g. =SUMME for German, =SOMME for French). "
            "Leave blank to fall back to English."
        ))

        # Paste button
        btn_paste = QPushButton("📥  Paste AI translations")
        btn_paste.setToolTip(
            "Paste the translated block produced by your AI tool.\n"
            "Format: LANG: de\nFormula: =SUMME(A1:A10)\nName: ...\nDescription: ..."
        )
        btn_paste.clicked.connect(self._paste_translations)
        tr_layout.addWidget(btn_paste)

        # Scroll area with one row per language
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.NoFrame)
        inner = QWidget()
        self._lang_layout = QFormLayout(inner)
        self._lang_layout.setSpacing(6)
        self._lang_layout.setContentsMargins(4, 4, 4, 4)
        scroll.setWidget(inner)
        tr_layout.addWidget(scroll, stretch=1)
        _non_en_count = len([c for c, _ in ALL_LANGUAGES if c != "en"])
        tabs.addTab(tab_tr, f"🌐  Translations ({_non_en_count} languages)")

        # _lang_fields[code] = {"formula": QLineEdit, "name": QLineEdit, "description": QLineEdit}
        self._lang_fields: Dict[str, dict] = {}
        self._build_lang_rows()

        # ── Buttons ──────────────────────────────────────────────────────────
        btns = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        btns.accepted.connect(self._on_accept)
        btns.rejected.connect(self.reject)
        root.addWidget(btns)

        # Pre-fill if editing
        if prefill:
            f = prefill.get("formula", "")
            self.formula.setText(f if isinstance(f, str) else f.get("en", ""))
            n = prefill.get("name", {})
            self.name_en.setText(n.get("en", "") if isinstance(n, dict) else str(n))
            d = prefill.get("description", {})
            self.desc_en.setPlainText(d.get("en", "") if isinstance(d, dict) else str(d))
            c = prefill.get("category", {})
            self.category_en.setText(c.get("en", "") if isinstance(c, dict) else str(c))
            # Fill translation fields
            for code, fields in self._lang_fields.items():
                fv = prefill.get("formula", {})
                fields["formula"].setText(fv.get(code, "") if isinstance(fv, dict) else "")
                nv = prefill.get("name", {})
                fields["name"].setText(nv.get(code, "") if isinstance(nv, dict) else "")
                dv = prefill.get("description", {})
                fields["description"].setText(dv.get(code, "") if isinstance(dv, dict) else "")

    def _build_lang_rows(self):
        """Add one row group per non-English language."""
        for code, lang_name in ALL_LANGUAGES:
            if code == "en":
                continue
            grp = QGroupBox(f"{lang_name}  [{code}]")
            grp_l = QFormLayout(grp)
            grp_l.setSpacing(4)

            f_formula = QLineEdit()
            f_formula.setPlaceholderText("Formula in this language (leave blank = use English)")
            f_name = QLineEdit()
            f_name.setPlaceholderText("Name in this language (leave blank = use English)")
            f_desc = QLineEdit()
            f_desc.setPlaceholderText("Description (optional)")

            grp_l.addRow("Formula:", f_formula)
            grp_l.addRow("Name:", f_name)
            grp_l.addRow("Description:", f_desc)

            self._lang_layout.addRow(grp)
            self._lang_fields[code] = {
                "formula":     f_formula,
                "name":        f_name,
                "description": f_desc,
            }

    def _copy_en_block(self):
        """Copy the English content as a block ready for AI translation."""
        lines = [
            "Translate the following LibreOffice Calc formula entry into all 32 languages listed below.",
            "For each language output a block in EXACTLY this format (one block per language):",
            "",
            "LANG: <language_code>",
            "Formula: <translated formula — use the correct function names for that language>",
            "Name: <translated name>",
            "Description: <translated description>",
            "",
            "Languages to translate to:",
        ]
        for code, name in ALL_LANGUAGES:
            if code != "en":
                lines.append(f"  {code}  ({name})")
        lines += [
            "",
            "--- ENGLISH SOURCE ---",
            f"Formula: {self.formula.text().strip()}",
            f"Name: {self.name_en.text().strip()}",
            f"Description: {self.desc_en.toPlainText().strip()}",
            f"Category: {self.category_en.text().strip()}",
        ]
        QApplication.clipboard().setText("\n".join(lines))
        QMessageBox.information(
            self, "Copied",
            "English block copied to clipboard.\n\n"
            "Paste it into an AI tool (e.g. ChatGPT, Claude, Gemini),\n"
            "then copy the result and click '📥 Paste AI translations'."
        )

    def _paste_translations(self):
        """Parse AI-translated block and fill all language fields."""
        dlg = QDialog(self)
        dlg.setWindowTitle("Paste AI Translations")
        dlg.setMinimumSize(580, 420)
        lay = QVBoxLayout(dlg)
        lay.setContentsMargins(12, 10, 12, 10)
        lay.addWidget(_bold_label("Paste translated block here", 10))
        lay.addWidget(_info_label(
            "Paste the AI output. Expected format per language:\n"
            "LANG: de\nFormula: =SUMME(A1:A10)\nName: Summe\nDescription: ..."
        ))
        txt = QTextEdit()
        txt.setPlaceholderText("LANG: de\nFormula: =SUMME(A1:A10)\nName: ...\n\nLANG: fr\n...")
        clip = QApplication.clipboard().text()
        if "LANG:" in clip:
            txt.setPlainText(clip)
        lay.addWidget(txt, stretch=1)
        btns = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        btns.accepted.connect(dlg.accept)
        btns.rejected.connect(dlg.reject)
        lay.addWidget(btns)
        if dlg.exec_() != QDialog.Accepted:
            return

        raw = txt.toPlainText()
        # Parse blocks — split on LANG: <code>
        blocks = re.split(r'(?im)^LANG:\s*', raw)
        filled = 0
        for block in blocks:
            if not block.strip():
                continue
            lines = block.strip().splitlines()
            if not lines:
                continue
            code = lines[0].strip().lower()
            if code not in self._lang_fields:
                continue
            fields = self._lang_fields[code]
            for line in lines[1:]:
                if ":" not in line:
                    continue
                key, _, val = line.partition(":")
                key = key.strip().lower()
                val = val.strip()
                if key == "formula":
                    fields["formula"].setText(val)
                elif key == "name":
                    fields["name"].setText(val)
                elif key in ("description", "desc"):
                    fields["description"].setText(val)
            filled += 1

        QMessageBox.information(
            self, "Done",
            f"{filled} language(s) filled.\nPlease review the fields, then click OK."
        )

    def _on_accept(self):
        if not self.formula.text().strip():
            QMessageBox.warning(self, "Required", "Please enter a formula.")
            return
        if not self.name_en.text().strip():
            QMessageBox.warning(self, "Required", "Please enter an English name.")
            return
        self.accept()

    def get_data(self) -> dict:
        # formula dict: en + all languages that have a value
        formula_dict: dict = {"en": self.formula.text().strip()}
        name_dict:    dict = {"en": self.name_en.text().strip()}
        desc_dict:    dict = {"en": self.desc_en.toPlainText().strip()}
        cat_dict:     dict = {"en": self.category_en.text().strip()}

        for code, fields in self._lang_fields.items():
            fv = fields["formula"].text().strip()
            nv = fields["name"].text().strip()
            dv = fields["description"].text().strip()
            if fv:
                formula_dict[code] = fv
            if nv:
                name_dict[code] = nv
            if dv:
                desc_dict[code] = dv

        return {
            "formula":     formula_dict,
            "name":        name_dict,
            "description": desc_dict,
            "category":    cat_dict,
        }


# ---------------------------------------------------------------------------
# Plugin Translation Dialog  (plugin-level: name + description)
# ---------------------------------------------------------------------------

class PluginTranslationDialog(QDialog):
    """Dialog for adding/editing a plugin-level translation (name + description)."""

    def __init__(self, available_langs: list, parent=None,
                 prefill_name="", prefill_desc=""):
        super().__init__(parent)
        self.setWindowTitle("Add / Edit Translation")
        self.setMinimumWidth(420)

        layout = QVBoxLayout(self)
        layout.setSpacing(10)
        layout.setContentsMargins(16, 12, 16, 12)

        form = QFormLayout()
        form.setSpacing(8)

        self._lang_combo = QComboBox()
        for code, name in available_langs:
            self._lang_combo.addItem(name, code)

        self._name = QLineEdit()
        self._name.setPlaceholderText("Plugin name in this language")
        self._name.setText(prefill_name)

        self._desc = QTextEdit()
        self._desc.setPlaceholderText("Plugin description in this language")
        self._desc.setFixedHeight(60)
        self._desc.setPlainText(prefill_desc)

        form.addRow("Language", self._lang_combo)
        form.addRow("Name *", self._name)
        form.addRow("Description", self._desc)
        layout.addLayout(form)

        btns = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        btns.accepted.connect(self._on_accept)
        btns.rejected.connect(self.reject)
        layout.addWidget(btns)

    def _on_accept(self):
        if not self._name.text().strip():
            QMessageBox.warning(self, "Required", "Please enter the plugin name.")
            return
        self.accept()

    def get_data(self) -> tuple:
        return (
            self._lang_combo.currentData(),
            self._name.text().strip(),
            self._desc.toPlainText().strip(),
        )


# ---------------------------------------------------------------------------
# Formula Translation Dialog
# ---------------------------------------------------------------------------

class FormulaTranslationDialog(QDialog):
    """
    Dialog for adding/editing translations for ALL formulas in a plugin at once.
    Shows one language at a time, all formulas as a form.
    """

    def __init__(self, plugin_dir: Path, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Edit Formula Translations")
        self.setMinimumSize(700, 540)
        self.resize(760, 580)
        self._plugin_dir = plugin_dir

        formulas_path = plugin_dir / "formulas.json"
        self._formulas: List[dict] = _load_json(formulas_path) or []

        layout = QVBoxLayout(self)
        layout.setSpacing(8)
        layout.setContentsMargins(16, 12, 16, 12)

        layout.addWidget(_bold_label("Edit Formula Translations", 11))
        layout.addWidget(_info_label(
            "Select a language and fill in the translations for each formula. "
            "English is shown as reference. Save when done."
        ))

        # Language selector
        lang_row = QHBoxLayout()
        lang_row.addWidget(QLabel("Language:"))
        self._lang_combo = QComboBox()
        for code, name in ALL_LANGUAGES:
            if code != "en":
                self._lang_combo.addItem(name, code)
        lang_row.addWidget(self._lang_combo)

        # Current language indicator label
        self._lang_indicator = QLineEdit()
        self._lang_indicator.setReadOnly(True)
        self._lang_indicator.setFixedWidth(180)
        self._lang_indicator.setStyleSheet(
            "QLineEdit { background: #e8f4e8; color: #2e7d32; font-weight: bold; "
            "border: 1px solid #a5d6a7; border-radius: 4px; padding: 2px 6px; }"
        )
        lang_row.addWidget(self._lang_indicator)

        lang_row.addStretch()
        self._btn_load = QPushButton("Load / Refresh")
        self._btn_load.clicked.connect(self._load_language)
        lang_row.addWidget(self._btn_load)
        layout.addLayout(lang_row)

        # Auto-reload when language changes
        self._lang_combo.currentIndexChanged.connect(self._load_language)

        layout.addWidget(_hr())

        # Scroll area with formula translation fields
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.NoFrame)
        self._form_widget = QWidget()
        self._form_layout = QVBoxLayout(self._form_widget)
        self._form_layout.setSpacing(12)
        scroll.setWidget(self._form_widget)
        layout.addWidget(scroll, stretch=1)

        # Stores translation widgets per formula index
        # { formula_index: { "name": QLineEdit, "description": QLineEdit, "category": QLineEdit } }
        self._fields: List[dict] = []

        # Bottom buttons
        layout.addWidget(_hr())
        btn_row = QHBoxLayout()
        self._btn_copy_en      = QPushButton("📋  Alle EN-Texte kopieren")
        self._btn_paste        = QPushButton("📥  Übersetzung einfügen")
        self._btn_missing_only = QPushButton("🤖  Nur Fehlende übersetzen")
        self._btn_missing_only.setToolTip(
            "Erstellt einen KI-Prompt NUR für Formeln, die noch keine\n"
            "Übersetzung in der gewählten Sprache haben."
        )
        self._btn_missing_only.setStyleSheet(
            "QPushButton { background: #E3F2FD; color: #1565C0; border: 1px solid #90CAF9;"
            " border-radius: 4px; padding: 4px 10px; font-weight: bold; }"
            "QPushButton:hover { background: #BBDEFB; }"
        )
        self._btn_save    = QPushButton("💾  Save Translations")
        btn_close         = QPushButton("Close")
        self._btn_copy_en.clicked.connect(self._copy_en_texts)
        self._btn_paste.clicked.connect(self._paste_translations)
        self._btn_missing_only.clicked.connect(self._copy_missing_only)
        self._btn_save.clicked.connect(self._save_translations)
        btn_close.clicked.connect(self.accept)
        btn_row.addWidget(self._btn_copy_en)
        btn_row.addWidget(self._btn_paste)
        btn_row.addWidget(self._btn_missing_only)
        btn_row.addStretch()
        btn_row.addWidget(self._btn_save)
        btn_row.addWidget(btn_close)
        layout.addLayout(btn_row)

        # Load first language automatically
        self._load_language()

    def _clear_form(self):
        while self._form_layout.count():
            item = self._form_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        self._fields = []

    def _load_language(self):
        self._clear_form()
        lang = self._lang_combo.currentData()
        lang_name = self._lang_combo.currentText()
        if not lang:
            self._lang_indicator.setText("")
            return
        self._lang_indicator.setText(f"Aktiv: {lang_name}")

        for i, formula in enumerate(self._formulas):
            formula_str = _get_formula_display(formula.get("formula", ""))
            en_name = formula.get("name", {}).get("en", "")
            en_desc = formula.get("description", {}).get("en", "")
            en_cat  = formula.get("category", {}).get("en", "")

            # Current translations
            cur_name = formula.get("name", {}).get(lang, "")
            cur_desc = formula.get("description", {}).get(lang, "")
            cur_cat  = formula.get("category", {}).get(lang, "")

            grp = QGroupBox(f"Formula {i+1}: {formula_str}")
            grp_layout = QFormLayout(grp)
            grp_layout.setSpacing(6)

            # English reference (read-only)
            ref = QLabel(f"EN: {en_name}  |  cat: {en_cat}")
            ref.setStyleSheet("color: #888; font-style: italic;")
            grp_layout.addRow("Reference:", ref)

            # Translation fields
            f_name = QLineEdit(cur_name)
            f_name.setPlaceholderText(f"→ {en_name}")
            f_desc = QLineEdit(cur_desc)
            f_desc.setPlaceholderText(f"→ {en_desc}" if en_desc else "optional")
            f_cat  = QLineEdit(cur_cat)
            f_cat.setPlaceholderText(f"→ {en_cat}" if en_cat else "optional")

            grp_layout.addRow("Name:", f_name)
            grp_layout.addRow("Description:", f_desc)
            grp_layout.addRow("Category:", f_cat)

            self._form_layout.addWidget(grp)
            self._fields.append({"name": f_name, "description": f_desc, "category": f_cat})

        self._form_layout.addStretch()

    def _copy_en_texts(self):
        """
        Build a plain-text block of all English formula texts and copy it to clipboard.
        Format:
          ---FORMULA 1---
          Name: Average
          Description: Calculates the arithmetic mean...
          Category: Mean values
          ...
        The user can paste this into any translator and then paste the result back.
        """
        lines = []
        for i, formula in enumerate(self._formulas):
            en_name = formula.get("name", {}).get("en", "")
            en_desc = formula.get("description", {}).get("en", "")
            en_cat  = formula.get("category", {}).get("en", "")
            lines.append(f"---FORMULA {i+1}---")
            lines.append(f"Name: {en_name}")
            lines.append(f"Description: {en_desc}")
            lines.append(f"Category: {en_cat}")
        text = "\n".join(lines)
        QApplication.clipboard().setText(text)
        QMessageBox.information(
            self, "Kopiert",
            f"{len(self._formulas)} Formel(n) wurden in die Zwischenablage kopiert.\n\n"
            "Füge den Text in ein Übersetzungsprogramm ein,\n"
            "übersetze ihn, und klicke dann auf '📥 Übersetzung einfügen'."
        )

    def _copy_missing_only(self):
        """
        Copies an AI prompt only for formulas that are MISSING a translation
        in the currently selected language.
        """
        lang = self._lang_combo.currentData()
        lang_name = self._lang_combo.currentText()
        if not lang:
            return

        missing_indices = []
        for i, formula in enumerate(self._formulas):
            cur_name = formula.get("name", {}).get(lang, "").strip()
            if not cur_name:
                missing_indices.append(i)

        if not missing_indices:
            QMessageBox.information(
                self, "Nichts fehlt ✅",
                f"Alle Formeln haben bereits eine Übersetzung für '{lang_name}'."
            )
            return

        lines = [
            f"Übersetze die folgenden LibreOffice-Calc-Formel-Einträge ins {lang_name} [{lang}].",
            "Gib für jeden Eintrag GENAU dieses Format aus:",
            "",
            "---FORMULA <N>---",
            "Name: <übersetzter Name>",
            "Description: <übersetzte Beschreibung>",
            "Category: <übersetzte Kategorie>",
            "",
            "Behalte die Formelnummern (---FORMULA N---) exakt bei.",
            "Lass Felder leer wenn kein sinnvoller Inhalt vorhanden ist.",
            "",
            "--- ENGLISCHE QUELLTEXTE (nur fehlende) ---",
        ]
        for i in missing_indices:
            formula = self._formulas[i]
            en_name = formula.get("name", {}).get("en", "")
            en_desc = formula.get("description", {}).get("en", "")
            en_cat  = formula.get("category", {}).get("en", "")
            lines.append(f"---FORMULA {i+1}---")
            lines.append(f"Name: {en_name}")
            lines.append(f"Description: {en_desc}")
            lines.append(f"Category: {en_cat}")

        QApplication.clipboard().setText("\n".join(lines))
        QMessageBox.information(
            self, "Prompt kopiert 📋",
            f"{len(missing_indices)} fehlende Formel(n) für '{lang_name}' in die\n"
            "Zwischenablage kopiert.\n\n"
            "Füge den Text in ein KI-Tool ein (Claude, ChatGPT …),\n"
            "kopiere das Ergebnis und klicke auf '📥 Übersetzung einfügen'."
        )

    def _paste_translations(self):
        """
        Open a dialog where the user pastes the translated block.
        Parses the same ---FORMULA N--- format and fills all fields at once.
        """
        dlg = QDialog(self)
        dlg.setWindowTitle("Übersetzung einfügen")
        dlg.setMinimumSize(560, 400)
        dlg_layout = QVBoxLayout(dlg)
        dlg_layout.setSpacing(8)
        dlg_layout.setContentsMargins(14, 10, 14, 10)

        dlg_layout.addWidget(_bold_label("Übersetzten Text einfügen", 10))
        dlg_layout.addWidget(_info_label(
            "Füge hier den übersetzten Text ein (gleiche Struktur wie beim Kopieren). "
            "Die Felder werden automatisch befüllt."
        ))

        text_edit = QTextEdit()
        text_edit.setPlaceholderText(
            "---FORMULA 1---\nName: ...\nDescription: ...\nCategory: ..."
        )
        # Pre-fill clipboard content if it looks like our format
        clip = QApplication.clipboard().text()
        if re.search(r"-{2,}\s*\S+\s+\d+\s*-{2,}", clip):
            text_edit.setPlainText(clip)
        dlg_layout.addWidget(text_edit, stretch=1)

        btns = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        btns.accepted.connect(dlg.accept)
        btns.rejected.connect(dlg.reject)
        dlg_layout.addWidget(btns)

        if dlg.exec_() != QDialog.Accepted:
            return

        raw = text_edit.toPlainText()
        # Parse blocks — accept any language: "---FORMULA 1---", "--- FORMEL 1 ---", "--- ФОРМУЛА 1 ---" etc.
        import re as _re
        blocks = _re.split(r'-{2,}\s*\S+\s+(\d+)\s*-{2,}', raw)
        # blocks = ['', '1', '<content1>', '2', '<content2>', ...]
        parsed: Dict[int, dict] = {}
        it = iter(blocks)
        next(it)  # skip leading empty string
        for num_str, content in zip(it, it):
            idx = int(num_str) - 1  # 0-based
            entry: dict = {}
            for line in content.strip().splitlines():
                line = line.strip()
                if not line:
                    continue
                low = line.lower()
                # Split on first colon
                if ":" not in line:
                    continue
                key_raw, _, val = line.partition(":")
                key_raw = key_raw.strip().lower()
                val = val.strip()
                # Name field — all supported languages
                if key_raw in ("name", "ime", "имя", "ime", "nom", "naam",
                               "navn", "nimi", "ονομα", "нэр", "nev", "الاسم",
                               "名前", "이름", "naam"):
                    entry["name"] = val
                # Description field
                elif key_raw in ("description", "beschreibung", "opisanie",
                                 "описание", "описание", "popis", "beschrijving",
                                 "descrizione", "descripción", "description",
                                 "kuvaus", "περιγραφή", "açıklama", "leírás",
                                 "説明", "설명"):
                    entry["description"] = val
                # Category field
                elif key_raw in ("category", "kategorie", "kategoriya",
                                 "категория", "kategori", "categorie",
                                 "categoria", "categoría", "catégorie",
                                 "luokka", "κατηγορία", "kategória",
                                 "カテゴリ", "카테고리"):
                    entry["category"] = val
                # Generic positional fallback: first unknown key → name, second → description, third → category
                else:
                    if "name" not in entry:
                        entry["name"] = val
                    elif "description" not in entry:
                        entry["description"] = val
                    elif "category" not in entry:
                        entry["category"] = val
            parsed[idx] = entry

        if not parsed:
            QMessageBox.warning(self, "Fehler",
                "Kein gültiges Format erkannt.\n"
                "Bitte verwende das Format aus '📋 Alle EN-Texte kopieren'.")
            return

        filled = 0
        for idx, entry in parsed.items():
            if idx < len(self._fields):
                fields = self._fields[idx]
                if "name" in entry:
                    fields["name"].setText(entry["name"])
                if "description" in entry:
                    fields["description"].setText(entry["description"])
                if "category" in entry:
                    fields["category"].setText(entry["category"])
                filled += 1

        QMessageBox.information(self, "Eingefügt",
            f"{filled} Formel(n) wurden befüllt.\n"
            "Bitte prüfe die Felder und klicke dann auf '💾 Save Translations'.")

    def _save_translations(self):
        lang = self._lang_combo.currentData()
        if not lang:
            return

        for i, fields in enumerate(self._fields):
            if i >= len(self._formulas):
                break
            for key in ("name", "description", "category"):
                val = fields[key].text().strip()
                if val:
                    if not isinstance(self._formulas[i].get(key), dict):
                        self._formulas[i][key] = {"en": ""}
                    self._formulas[i][key][lang] = val
                else:
                    # Remove empty translation
                    if isinstance(self._formulas[i].get(key), dict):
                        self._formulas[i][key].pop(lang, None)

        if _save_json(self._plugin_dir / "formulas.json", self._formulas):
            QMessageBox.information(self, "Saved",
                f"Translations for '{lang}' saved successfully.")


# ---------------------------------------------------------------------------
# Add Formulas to Existing Plugin
# ---------------------------------------------------------------------------

class AddFormulasDialog(QDialog):
    """Dialog for adding formulas to an existing plugin."""

    def __init__(self, plugin_dir: Path, parent=None):
        super().__init__(parent)
        self._plugin_dir = plugin_dir
        plugin_name = (_load_json(plugin_dir / "plugin.json") or {}).get("name", {})
        name = plugin_name.get("en", plugin_dir.name) if isinstance(plugin_name, dict) else str(plugin_name)
        self.setWindowTitle(f"Add Formulas – {name}")
        self.setMinimumSize(620, 500)

        self._formulas: List[dict] = _load_json(plugin_dir / "formulas.json") or []

        layout = QVBoxLayout(self)
        layout.setSpacing(8)
        layout.setContentsMargins(16, 12, 16, 12)

        layout.addWidget(_bold_label(f"Formulas in: {name}", 11))
        layout.addWidget(_info_label(
            "Add, edit or remove formulas. Changes are saved when you click 'Save'."
        ))

        self._list = QListWidget()
        self._list.setAlternatingRowColors(True)
        self._list.itemDoubleClicked.connect(self._edit)
        layout.addWidget(self._list)
        self._refresh_list()

        btn_row = QHBoxLayout()
        btn_add  = QPushButton("➕  Add Formula")
        btn_edit = QPushButton("✏️  Edit Selected")
        btn_del  = QPushButton("🗑  Remove Selected")
        btn_add.clicked.connect(self._add)
        btn_edit.clicked.connect(self._edit)
        btn_del.clicked.connect(self._delete)
        btn_row.addWidget(btn_add)
        btn_row.addWidget(btn_edit)
        btn_row.addWidget(btn_del)
        btn_row.addStretch()
        layout.addLayout(btn_row)

        layout.addWidget(_hr())

        btns = QHBoxLayout()
        btn_save  = QPushButton("💾  Save")
        btn_close = QPushButton("Cancel")
        btn_save.clicked.connect(self._save)
        btn_close.clicked.connect(self.reject)
        btns.addStretch()
        btns.addWidget(btn_save)
        btns.addWidget(btn_close)
        layout.addLayout(btns)

    def _refresh_list(self):
        self._list.clear()
        for f in self._formulas:
            name    = f.get("name", {}).get("en", "?")
            formula = _get_formula_display(f.get("formula", ""))
            cat     = f.get("category", {}).get("en", "")
            text = f"[{cat}]  {name}  →  {formula}" if cat else f"{name}  →  {formula}"
            self._list.addItem(text)

    def _add(self):
        dlg = FormulaEditDialog(self)
        if dlg.exec_() == QDialog.Accepted:
            self._formulas.append(dlg.get_data())
            self._refresh_list()

    def _edit(self, _item=None):
        row = self._list.currentRow()
        if row < 0:
            return
        dlg = FormulaEditDialog(self, self._formulas[row])
        if dlg.exec_() == QDialog.Accepted:
            self._formulas[row] = dlg.get_data()
            self._refresh_list()

    def _delete(self):
        row = self._list.currentRow()
        if row < 0:
            return
        ans = QMessageBox.question(self, "Remove", "Remove this formula?")
        if ans == QMessageBox.Yes:
            self._formulas.pop(row)
            self._refresh_list()

    def _save(self):
        if _save_json(self._plugin_dir / "formulas.json", self._formulas):
            QMessageBox.information(self, "Saved", "Formulas saved successfully.")
            self.accept()


# ---------------------------------------------------------------------------
# Missing Translations Dialog  –  "🔍 Fehlende Einträge prüfen"
# ---------------------------------------------------------------------------

class MissingTranslationsDialog(QDialog):
    """
    Scans ALL plugins and shows which language/formula combinations are missing.
    Also offers a quick-jump to translate them directly.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("🔍 Fehlende Übersetzungen prüfen")
        self.setMinimumSize(760, 540)
        self.resize(820, 580)

        layout = QVBoxLayout(self)
        layout.setSpacing(8)
        layout.setContentsMargins(16, 12, 16, 12)

        layout.addWidget(_bold_label("Fehlende Übersetzungen – Übersicht", 11))
        layout.addWidget(_info_label(
            "Zeigt alle Plugins und Sprachen, für die noch Übersetzungen fehlen. "
            "Grün = vollständig, Orange = fehlend."
        ))

        # Filter row
        filter_row = QHBoxLayout()
        filter_row.addWidget(QLabel("Sprache filtern:"))
        self._lang_filter = QComboBox()
        self._lang_filter.addItem("(Alle Sprachen)", "")
        for code, name in ALL_LANGUAGES:
            if code != "en":
                self._lang_filter.addItem(name, code)
        self._lang_filter.currentIndexChanged.connect(self._refresh)
        filter_row.addWidget(self._lang_filter)
        filter_row.addStretch()
        btn_scan = QPushButton("🔄  Neu scannen")
        btn_scan.clicked.connect(self._refresh)
        filter_row.addWidget(btn_scan)
        layout.addLayout(filter_row)

        layout.addWidget(_hr())

        # Results list
        self._result_list = QListWidget()
        self._result_list.setAlternatingRowColors(True)
        self._result_list.setFont(QFont("Monospace", 9))
        layout.addWidget(self._result_list, stretch=1)

        # Summary label
        self._summary_lbl = QLabel("")
        self._summary_lbl.setStyleSheet("font-weight: bold; color: #555;")
        layout.addWidget(self._summary_lbl)

        layout.addWidget(_hr())
        btn_row = QHBoxLayout()
        btn_close = QPushButton("Schließen")
        btn_close.clicked.connect(self.accept)
        btn_row.addStretch()
        btn_row.addWidget(btn_close)
        layout.addLayout(btn_row)

        self._refresh()

    def _refresh(self):
        self._result_list.clear()
        filter_lang = self._lang_filter.currentData()
        plugins = _scan_plugins()
        lang_map = dict(ALL_LANGUAGES)

        total_missing = 0
        total_ok      = 0

        for plugin_dir in plugins:
            formulas = _load_json(plugin_dir / "formulas.json") or []
            meta     = _load_json(plugin_dir / "plugin.json") or {}
            name_raw = meta.get("name", {})
            pname    = name_raw.get("en", plugin_dir.name) if isinstance(name_raw, dict) else str(name_raw)

            langs_to_check = [
                (c, n) for c, n in ALL_LANGUAGES
                if c != "en" and (not filter_lang or c == filter_lang)
            ]

            plugin_has_issues = False
            for lang_code, lang_name in langs_to_check:
                missing = []
                for i, formula in enumerate(formulas):
                    nm = formula.get("name", {})
                    val = nm.get(lang_code, "").strip() if isinstance(nm, dict) else ""
                    if not val:
                        en_name = nm.get("en", f"Formula {i+1}") if isinstance(nm, dict) else f"Formula {i+1}"
                        missing.append(f"#{i+1} {en_name}")

                if missing:
                    plugin_has_issues = True
                    total_missing += len(missing)
                    item = QListWidgetItem(
                        f"⚠️  {pname}  │  {lang_name} [{lang_code}]  │  "
                        f"{len(missing)} fehlend:  {', '.join(missing[:4])}"
                        + (" …" if len(missing) > 4 else "")
                    )
                    item.setForeground(QColor("#B26A00"))
                    item.setData(Qt.UserRole, (plugin_dir, lang_code))
                    self._result_list.addItem(item)
                else:
                    total_ok += 1

            if not plugin_has_issues and not filter_lang:
                item = QListWidgetItem(f"✅  {pname}  │  Alle Sprachen vollständig")
                item.setForeground(QColor("#2e7d32"))
                self._result_list.addItem(item)

        if total_missing == 0:
            self._summary_lbl.setText(
                f"✅  Keine fehlenden Übersetzungen gefunden  ({total_ok} Sprache/Plugin-Kombis geprüft)"
            )
            self._summary_lbl.setStyleSheet("font-weight: bold; color: #2e7d32;")
        else:
            self._summary_lbl.setText(
                f"⚠️  {total_missing} fehlende Formel-Übersetzung(en) gefunden"
            )
            self._summary_lbl.setStyleSheet("font-weight: bold; color: #B26A00;")


# ---------------------------------------------------------------------------
# Bulk Translate Dialog  –  "🌍 Alle Fehlenden für eine Sprache übersetzen"
# ---------------------------------------------------------------------------

class BulkTranslateDialog(QDialog):
    """
    Collects ALL missing formula translations for ONE chosen language
    across ALL plugins, builds a single AI prompt, and after paste
    writes results back to every plugin.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("🌍 Bulk-Übersetzung – alle Plugins")
        self.setMinimumSize(680, 520)
        self.resize(740, 560)

        # { plugin_dir: [formula_list] }
        self._plugin_formulas: dict = {}
        # { plugin_dir: [(original_index, formula_dict), ...] }  only missing ones
        self._missing_map: dict = {}

        layout = QVBoxLayout(self)
        layout.setSpacing(8)
        layout.setContentsMargins(16, 12, 16, 12)

        layout.addWidget(_bold_label("Bulk-Übersetzung für eine fehlende Sprache", 11))
        layout.addWidget(_info_label(
            "Wähle eine Sprache. Der Manager sammelt dann ALLE fehlenden Formeln "
            "aus ALLEN Plugins in einem einzigen KI-Prompt. "
            "Nach dem Einfügen werden alle Plugins automatisch gespeichert."
        ))

        # Language selector + Scan
        lang_row = QHBoxLayout()
        lang_row.addWidget(QLabel("Sprache:"))
        self._lang_combo = QComboBox()
        for code, name in ALL_LANGUAGES:
            if code != "en":
                self._lang_combo.addItem(name, code)
        lang_row.addWidget(self._lang_combo)
        lang_row.addStretch()
        btn_scan = QPushButton("🔍  Fehlende scannen")
        btn_scan.setStyleSheet(
            "QPushButton { background:#E3F2FD; color:#1565C0; border:1px solid #90CAF9;"
            " border-radius:4px; padding:4px 10px; font-weight:bold; }"
            "QPushButton:hover { background:#BBDEFB; }"
        )
        btn_scan.clicked.connect(self._scan)
        lang_row.addWidget(btn_scan)
        layout.addLayout(lang_row)

        layout.addWidget(_hr())

        # Scan result info
        self._info_lbl = QLabel("→ Klicke auf '🔍 Fehlende scannen' um zu starten.")
        self._info_lbl.setStyleSheet("color: #555; font-style: italic;")
        layout.addWidget(self._info_lbl)

        # Preview list
        self._preview = QListWidget()
        self._preview.setAlternatingRowColors(True)
        layout.addWidget(self._preview, stretch=1)

        layout.addWidget(_hr())

        # Action buttons
        btn_row = QHBoxLayout()
        self._btn_copy  = QPushButton("📋  KI-Prompt kopieren")
        self._btn_paste = QPushButton("📥  Übersetzung einfügen & speichern")
        btn_close       = QPushButton("Schließen")
        self._btn_copy.setEnabled(False)
        self._btn_paste.setEnabled(False)
        self._btn_copy.clicked.connect(self._copy_prompt)
        self._btn_paste.clicked.connect(self._paste_and_save)
        btn_close.clicked.connect(self.accept)
        btn_row.addWidget(self._btn_copy)
        btn_row.addWidget(self._btn_paste)
        btn_row.addStretch()
        btn_row.addWidget(btn_close)
        layout.addLayout(btn_row)

    # ── Internal ─────────────────────────────────────────────────────────────

    def _scan(self):
        """Find all formulas missing a translation for the chosen language."""
        lang = self._lang_combo.currentData()
        self._missing_map = {}
        self._plugin_formulas = {}
        self._preview.clear()

        plugins = _scan_plugins()
        total_missing = 0

        for plugin_dir in plugins:
            formulas = _load_json(plugin_dir / "formulas.json") or []
            self._plugin_formulas[plugin_dir] = formulas
            meta     = _load_json(plugin_dir / "plugin.json") or {}
            name_raw = meta.get("name", {})
            pname    = name_raw.get("en", plugin_dir.name) if isinstance(name_raw, dict) else str(name_raw)

            missing = []
            for i, formula in enumerate(formulas):
                nm  = formula.get("name", {})
                val = nm.get(lang, "").strip() if isinstance(nm, dict) else ""
                if not val:
                    missing.append((i, formula))

            if missing:
                self._missing_map[plugin_dir] = missing
                total_missing += len(missing)
                item = QListWidgetItem(
                    f"📦  {pname}  →  {len(missing)} fehlende Formel(n)"
                )
                item.setForeground(QColor("#B26A00"))
                self._preview.addItem(item)
            else:
                item = QListWidgetItem(f"✅  {pname}  →  vollständig")
                item.setForeground(QColor("#2e7d32"))
                self._preview.addItem(item)

        lang_name = self._lang_combo.currentText()
        if total_missing:
            self._info_lbl.setText(
                f"⚠️  {total_missing} fehlende Formel(n) für '{lang_name}' in "
                f"{len(self._missing_map)} Plugin(s) gefunden."
            )
            self._info_lbl.setStyleSheet("color: #B26A00; font-weight: bold;")
            self._btn_copy.setEnabled(True)
            self._btn_paste.setEnabled(True)
        else:
            self._info_lbl.setText(
                f"✅  Alle Formeln sind bereits für '{lang_name}' übersetzt!"
            )
            self._info_lbl.setStyleSheet("color: #2e7d32; font-weight: bold;")
            self._btn_copy.setEnabled(False)
            self._btn_paste.setEnabled(False)

    def _copy_prompt(self):
        """Build and copy the combined AI prompt for all missing entries."""
        lang      = self._lang_combo.currentData()
        lang_name = self._lang_combo.currentText()

        lines = [
            f"Übersetze die folgenden LibreOffice-Calc-Formel-Einträge ins {lang_name} [{lang}].",
            "Gib für jeden Eintrag GENAU dieses Format aus (Nummern exakt beibehalten):",
            "",
            "---PLUGIN <plugin_id> FORMULA <N>---",
            "Name: <übersetzter Name>",
            "Description: <übersetzte Beschreibung>",
            "Category: <übersetzte Kategorie>",
            "",
            "Lass Felder leer wenn kein sinnvoller Inhalt vorhanden ist.",
            "",
            "=== ENGLISCHE QUELLTEXTE ===",
        ]

        for plugin_dir, missing_list in self._missing_map.items():
            lines.append(f"\n--- Plugin: {plugin_dir.name} ---")
            for orig_idx, formula in missing_list:
                en_name = formula.get("name", {}).get("en", "")
                en_desc = formula.get("description", {}).get("en", "")
                en_cat  = formula.get("category", {}).get("en", "")
                lines.append(f"---PLUGIN {plugin_dir.name} FORMULA {orig_idx+1}---")
                lines.append(f"Name: {en_name}")
                lines.append(f"Description: {en_desc}")
                lines.append(f"Category: {en_cat}")

        QApplication.clipboard().setText("\n".join(lines))
        QMessageBox.information(
            self, "Prompt kopiert 📋",
            "Der KI-Prompt wurde in die Zwischenablage kopiert.\n\n"
            "1. Füge ihn in ein KI-Tool ein (Claude, ChatGPT …)\n"
            "2. Kopiere das Ergebnis\n"
            "3. Klicke hier auf '📥 Übersetzung einfügen & speichern'"
        )

    def _paste_and_save(self):
        """Open paste dialog, parse result and write to all affected plugins."""
        lang = self._lang_combo.currentData()

        dlg = QDialog(self)
        dlg.setWindowTitle("Übersetzung einfügen")
        dlg.setMinimumSize(580, 420)
        dlg_l = QVBoxLayout(dlg)
        dlg_l.addWidget(_bold_label("KI-Übersetzung einfügen", 10))
        dlg_l.addWidget(_info_label(
            "Füge die Antwort des KI-Tools hier ein.\n"
            "Format: ---PLUGIN <id> FORMULA <N>---"
        ))
        txt = QTextEdit()
        clip = QApplication.clipboard().text()
        if "---PLUGIN" in clip:
            txt.setPlainText(clip)
        dlg_l.addWidget(txt, stretch=1)
        btns = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        btns.accepted.connect(dlg.accept)
        btns.rejected.connect(dlg.reject)
        dlg_l.addWidget(btns)
        if dlg.exec_() != QDialog.Accepted:
            return

        raw = txt.toPlainText()

        # Parse: ---PLUGIN <id> FORMULA <N>---
        blocks = re.split(r'-{3}PLUGIN\s+(\S+)\s+FORMULA\s+(\d+)-{3}', raw)
        # blocks: ['', plugin_id, formula_num, content, plugin_id2, ...]
        parsed: Dict[str, Dict[int, dict]] = {}  # {plugin_id: {0-based-idx: entry}}
        it = iter(blocks)
        next(it)  # skip leading empty
        for pid, fnum, content in zip(it, it, it):
            idx = int(fnum) - 1
            entry: dict = {}
            for line in content.strip().splitlines():
                if ":" not in line:
                    continue
                key_raw, _, val = line.partition(":")
                key_raw = key_raw.strip().lower()
                val = val.strip()
                if key_raw == "name":
                    entry["name"] = val
                elif key_raw in ("description", "beschreibung", "açıklama"):
                    entry["description"] = val
                elif key_raw in ("category", "kategorie", "kategori"):
                    entry["category"] = val
            if pid not in parsed:
                parsed[pid] = {}
            parsed[pid][idx] = entry

        saved_plugins = 0
        saved_entries = 0

        for plugin_dir, formulas in self._plugin_formulas.items():
            pid = plugin_dir.name
            if pid not in parsed:
                continue
            changed = False
            for idx, entry in parsed[pid].items():
                if idx >= len(formulas):
                    continue
                for key in ("name", "description", "category"):
                    val = entry.get(key, "").strip()
                    if val:
                        if not isinstance(formulas[idx].get(key), dict):
                            formulas[idx][key] = {"en": ""}
                        formulas[idx][key][lang] = val
                        changed = True
                        saved_entries += 1
            if changed:
                _save_json(plugin_dir / "formulas.json", formulas)
                saved_plugins += 1

        QMessageBox.information(
            self, "Gespeichert ✅",
            f"{saved_entries} Einträge in {saved_plugins} Plugin(s) gespeichert.\n\n"
            "Klicke auf '🔍 Fehlende scannen' um den Status zu aktualisieren."
        )
        self._scan()


# ---------------------------------------------------------------------------
# Main Window
# ---------------------------------------------------------------------------

class PluginManagerWindow(QMainWindow):
    """Main window: shows plugin list + action buttons."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle(f"{APP_NAME}  v{APP_VERSION}")
        self.setMinimumSize(700, 650)
        self.resize(820, 680)

        central = QWidget()
        self.setCentralWidget(central)
        root = QVBoxLayout(central)
        root.setContentsMargins(12, 10, 12, 10)
        root.setSpacing(8)

        # ── Header ──────────────────────────────────────────────────────────
        header = QHBoxLayout()
        title = _bold_label(f"🔌  {APP_NAME}", 13)
        header.addWidget(title)
        header.addStretch()
        btn_notice = QPushButton("⚠️  Important Notice")
        btn_notice.setFixedHeight(30)
        btn_notice.setStyleSheet(
            "QPushButton { background: #FFF3CD; color: #856404; border: 1px solid #FFEAA7;"
            " border-radius: 4px; font-weight: bold; padding: 0 10px; }"
            "QPushButton:hover { background: #FFE69C; }"
        )
        btn_notice.clicked.connect(self._show_notice)
        header.addWidget(btn_notice)
        btn_refresh = QPushButton("🔄  Refresh")
        btn_refresh.clicked.connect(self._load_plugins)
        header.addWidget(btn_refresh)
        root.addLayout(header)

        # ── Scan-Button: fehlende Übersetzungen ──────────────────────────────
        self._btn_scan_missing = QPushButton(
            "🔍  Alle Plugins nach fehlenden Übersetzungen durchsuchen"
        )
        self._btn_scan_missing.setFixedHeight(36)
        self._btn_scan_missing.setStyleSheet(
            "QPushButton { background: #E8F5E9; color: #1B5E20; border: 1.5px solid #66BB6A;"
            " border-radius: 6px; font-weight: bold; font-size: 11px; padding: 0 14px; }"
            "QPushButton:hover { background: #C8E6C9; border-color: #388E3C; }"
            "QPushButton:pressed { background: #A5D6A7; }"
        )
        self._btn_scan_missing.clicked.connect(self._scan_missing_translations)
        root.addWidget(self._btn_scan_missing)

        root.addWidget(_info_label(
            f"Plugins folder:  {PLUGINS_DIR}"
        ))
        root.addWidget(_hr())

        # ── Splitter: list | detail ──────────────────────────────────────────
        splitter = QSplitter(Qt.Horizontal)

        # Left: plugin list
        left = QWidget()
        left_l = QVBoxLayout(left)
        left_l.setContentsMargins(0, 0, 6, 0)
        left_l.addWidget(_bold_label("Installed Plugins", 9))
        self._plugin_list = QListWidget()
        self._plugin_list.setFixedWidth(200)
        self._plugin_list.currentRowChanged.connect(self._on_select)
        self._plugin_list.itemDoubleClicked.connect(self._add_formulas)
        left_l.addWidget(self._plugin_list)
        splitter.addWidget(left)

        # Right: detail + actions
        right = QWidget()
        right_l = QVBoxLayout(right)
        right_l.setContentsMargins(6, 0, 0, 0)
        right_l.setSpacing(8)

        right_l.addWidget(_bold_label("Plugin Details", 9))
        self._detail = QTextEdit()
        self._detail.setReadOnly(True)
        self._detail.setMinimumHeight(160)
        right_l.addWidget(self._detail)

        right_l.addWidget(_hr())
        right_l.addWidget(_bold_label("Actions", 9))

        # Action buttons
        self._btn_new   = QPushButton("🆕  Create New Plugin")
        self._btn_add   = QPushButton("➕  Add Formulas to Plugin")
        self._btn_trans = QPushButton("🌍  Edit Formula Translations")
        self._btn_open  = QPushButton("📂  Open Plugin Folder")
        self._btn_del   = QPushButton("🗑  Delete Plugin")

        for btn in (self._btn_new, self._btn_add, self._btn_trans,
                    self._btn_open, self._btn_del):
            btn.setFixedHeight(34)
            right_l.addWidget(btn)

        self._btn_new.clicked.connect(self._create_new)
        self._btn_add.clicked.connect(self._add_formulas)
        self._btn_trans.clicked.connect(self._edit_translations)
        self._btn_open.clicked.connect(self._open_folder)
        self._btn_del.clicked.connect(self._delete_plugin)

        right_l.addWidget(_hr())
        right_l.addWidget(_bold_label("Import / Export", 9))

        self._btn_export = QPushButton("📦  Export Plugin (.zip)")
        self._btn_import = QPushButton("📥  Import Plugin (.zip)")
        for btn in (self._btn_export, self._btn_import):
            btn.setFixedHeight(34)
            right_l.addWidget(btn)
        self._btn_export.clicked.connect(self._export_plugin)
        self._btn_import.clicked.connect(self._import_plugin)

        right_l.addStretch()
        splitter.addWidget(right)
        splitter.setStretchFactor(0, 0)
        splitter.setStretchFactor(1, 1)

        root.addWidget(splitter, stretch=1)

        # Status bar
        self._status = QStatusBar()
        self.setStatusBar(self._status)

        self._plugins: List[Path] = []
        self._load_plugins()

    # ── Plugin list ──────────────────────────────────────────────────────────

    def _load_plugins(self):
        self._plugins = _scan_plugins()
        self._plugin_list.clear()
        for p in self._plugins:
            meta = _load_json(p / "plugin.json") or {}
            name_raw = meta.get("name", p.name)
            name = name_raw.get("en", p.name) if isinstance(name_raw, dict) else str(name_raw)
            icon = meta.get("icon", "")
            self._plugin_list.addItem(f"{icon}  {name}" if icon else name)
        if self._plugins:
            self._plugin_list.setCurrentRow(0)
        else:
            self._detail.setHtml("<i>No plugins found. Create one!</i>")
        self._status.showMessage(f"{len(self._plugins)} plugin(s) found in {PLUGINS_DIR}", 4000)

    def _on_select(self, row: int):
        if row < 0 or row >= len(self._plugins):
            self._detail.clear()
            return
        plugin_dir = self._plugins[row]
        meta       = _load_json(plugin_dir / "plugin.json") or {}
        formulas   = _load_json(plugin_dir / "formulas.json") or []

        name_raw = meta.get("name", {})
        name     = name_raw.get("en", plugin_dir.name) if isinstance(name_raw, dict) else str(name_raw)
        langs    = list(name_raw.keys()) if isinstance(name_raw, dict) else ["en"]

        lines = [
            f"<b>Name:</b> {name}",
            f"<b>ID (folder):</b> {plugin_dir.name}",
            f"<b>Version:</b> {meta.get('version', '?')}",
            f"<b>Author:</b> {meta.get('author', '–')}",
            f"<b>Enabled:</b> {meta.get('enabled', True)}",
            f"<b>Formulas:</b> {len(formulas)}",
            f"<b>Languages:</b> {', '.join(langs)}",
        ]
        self._detail.setHtml("<br>".join(lines))

    def _selected_dir(self) -> Optional[Path]:
        row = self._plugin_list.currentRow()
        if 0 <= row < len(self._plugins):
            return self._plugins[row]
        return None

    # ── Actions ──────────────────────────────────────────────────────────────

    def _create_new(self):
        dlg = NewPluginWizard(self)
        if dlg.exec_() == QDialog.Accepted:
            self._load_plugins()

    def _add_formulas(self, _item=None):
        d = self._selected_dir()
        if not d:
            QMessageBox.information(self, "No Plugin", "Please select a plugin first.")
            return
        dlg = AddFormulasDialog(d, self)
        dlg.exec_()
        self._on_select(self._plugin_list.currentRow())

    def _edit_translations(self):
        d = self._selected_dir()
        if not d:
            QMessageBox.information(self, "No Plugin", "Please select a plugin first.")
            return
        dlg = FormulaTranslationDialog(d, self)
        dlg.exec_()

    def _open_folder(self):
        d = self._selected_dir()
        if not d:
            QMessageBox.information(self, "No Plugin", "Please select a plugin first.")
            return
        import subprocess
        if sys.platform == "win32":
            subprocess.Popen(["explorer", str(d)])
        elif sys.platform == "darwin":
            subprocess.Popen(["open", str(d)])
        else:
            subprocess.Popen(["xdg-open", str(d)])

    def _delete_plugin(self):
        d = self._selected_dir()
        if not d:
            QMessageBox.information(self, "No Plugin", "Please select a plugin first.")
            return
        ans = QMessageBox.question(
            self, "Delete Plugin",
            f"Delete plugin '{d.name}' and ALL its files?\nThis cannot be undone.",
            QMessageBox.Yes | QMessageBox.No,
        )
        if ans == QMessageBox.Yes:
            import shutil
            shutil.rmtree(d)
            self._load_plugins()
            self._status.showMessage(f"Plugin '{d.name}' deleted.", 4000)

    def _export_plugin(self):
        """Export selected plugin as a .zip file."""
        from PyQt5.QtWidgets import QFileDialog
        d = self._selected_dir()
        if not d:
            QMessageBox.information(self, "No Plugin", "Please select a plugin first.")
            return

        meta = _load_json(d / "plugin.json") or {}
        version = meta.get("version", "1.0")
        default_name = f"{d.name}_v{version}.zip"

        dest, _ = QFileDialog.getSaveFileName(
            self, "Export Plugin", default_name,
            "ZIP Archive (*.zip)"
        )
        if not dest:
            return

        try:
            with zipfile.ZipFile(dest, "w", zipfile.ZIP_DEFLATED) as zf:
                for file in d.iterdir():
                    if file.is_file():
                        # Store as plugin_id/filename inside the zip
                        zf.write(file, arcname=f"{d.name}/{file.name}")
            self._status.showMessage(f"✅  Exported '{d.name}' → {dest}", 5000)
        except Exception as e:
            QMessageBox.critical(self, "Export Error", f"Could not export plugin:\n{e}")

    def _import_plugin(self):
        """Import a plugin from a .zip file."""
        from PyQt5.QtWidgets import QFileDialog
        src, _ = QFileDialog.getOpenFileName(
            self, "Import Plugin", "",
            "ZIP Archive (*.zip)"
        )
        if not src:
            return

        try:
            with zipfile.ZipFile(src, "r") as zf:
                names = zf.namelist()

                # Expect at least plugin.json somewhere inside
                json_files = [n for n in names if n.endswith("plugin.json")]
                if not json_files:
                    QMessageBox.critical(
                        self, "Invalid Package",
                        "This ZIP does not contain a valid plugin.\n"
                        "(plugin.json not found)"
                    )
                    return

                # Determine plugin_id from the folder name inside zip
                plugin_id = json_files[0].split("/")[0] if "/" in json_files[0] else ""
                if not plugin_id:
                    QMessageBox.critical(self, "Invalid Package",
                                         "Cannot determine plugin ID from ZIP structure.")
                    return

                # Read and validate plugin.json
                with zf.open(json_files[0]) as jf:
                    try:
                        meta = json.loads(jf.read().decode("utf-8"))
                    except Exception:
                        QMessageBox.critical(self, "Invalid Package",
                                             "plugin.json could not be parsed.")
                        return

                if not isinstance(meta.get("name"), dict) or "en" not in meta.get("name", {}):
                    QMessageBox.critical(self, "Invalid Package",
                                         "plugin.json is missing required field 'name.en'.")
                    return

                dest_dir = _plugins_dir() / plugin_id

                # Warn if plugin already exists
                if dest_dir.exists():
                    ans = QMessageBox.question(
                        self, "Plugin Already Exists",
                        f"A plugin with ID '{plugin_id}' already exists.\nOverwrite it?",
                        QMessageBox.Yes | QMessageBox.No,
                    )
                    if ans != QMessageBox.Yes:
                        return
                    shutil.rmtree(dest_dir)

                dest_dir.mkdir(parents=True, exist_ok=True)

                # Extract only files belonging to this plugin_id folder
                for member in names:
                    if member.startswith(plugin_id + "/") and not member.endswith("/"):
                        filename = member[len(plugin_id) + 1:]
                        target = dest_dir / filename
                        with zf.open(member) as src_f, open(target, "wb") as dst_f:
                            dst_f.write(src_f.read())

            plugin_name = meta.get("name", {}).get("en", plugin_id)
            formulas_count = len(_load_json(dest_dir / "formulas.json") or [])
            self._load_plugins()
            self._status.showMessage(
                f"✅  Imported '{plugin_name}' ({formulas_count} formula(s))", 5000
            )
            QMessageBox.information(
                self, "Import Successful",
                f"Plugin '{plugin_name}' imported successfully!\n"
                f"Formulas: {formulas_count}\n"
                f"Location: {dest_dir}"
            )
        except zipfile.BadZipFile:
            QMessageBox.critical(self, "Import Error", "The selected file is not a valid ZIP archive.")
        except Exception as e:
            QMessageBox.critical(self, "Import Error", f"Could not import plugin:\n{e}")

    def _show_notice(self):
        """Show the Important Notice dialog."""
        dlg = ImportantNoticeDialog(self)
        dlg.exec_()

    def _scan_missing_translations(self):
        """Scans all plugins for missing translations and shows results."""
        dlg = MissingTranslationsDialog(self)
        dlg.exec_()


class ImportantNoticeDialog(QDialog):
    """Displays the important notice from the external .md file."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Important Notice — Formula Compatibility")
        self.setMinimumSize(560, 480)
        self.resize(620, 520)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 12, 16, 12)
        layout.setSpacing(10)

        text = QTextEdit()
        text.setReadOnly(True)

        # PFAD ZUR DATEI: Wir suchen die Datei im gleichen Ordner wie das Skript
        notice_path = HERE / "IMPORTANT_NOTICE.md"

        if notice_path.exists():
            try:
                # Datei öffnen und Inhalt lesen
                with open(notice_path, "r", encoding="utf-8") as f:
                    content = f.read()
                text.setPlainText(content) # Zeigt den Text deiner .md Datei an
            except Exception as e:
                text.setHtml(f"<b style='color:red;'>Fehler beim Laden:</b><br>{str(e)}")
        else:
            text.setHtml("<b style='color:red;'>Fehler:</b> Die Datei <code>IMPORTANT_NOTICE.md</code> wurde nicht gefunden.")

        layout.addWidget(text)

        btns = QDialogButtonBox(QDialogButtonBox.Ok)
        btns.accepted.connect(self.accept)
        layout.addWidget(btns)

# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    app = QApplication(sys.argv)
    app.setApplicationName(APP_NAME)
    app.setApplicationVersion(APP_VERSION)

    # Clean default style
    app.setStyle("Fusion")

    win = PluginManagerWindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()