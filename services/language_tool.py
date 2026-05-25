#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Language Tool  –  Neue Sprache zu languages.json / formula_explanations.json hinzufügen.
Wird aus Calc2.py gestartet: LanguageTool(base_dir=_here).run()
Nutzt PyQt5 – kein tkinter nötig.
"""

import json
from pathlib import Path

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QApplication, QDialog, QHBoxLayout, QLabel,
    QMessageBox, QPlainTextEdit, QPushButton,
    QSizePolicy, QStackedWidget, QVBoxLayout, QWidget,
)


# ──────────────────────────────────────────────────────────────────────────────
# RTL-Sprachen  –  werden aus rtl_languages.json geladen.
# Neue RTL-Sprache hinzufügen: einfach den Code in rtl_languages.json ergänzen.
# ──────────────────────────────────────────────────────────────────────────────
def _load_rtl_codes(base_dir: Path) -> set:
    """Lädt RTL-Sprachcodes aus language/rtl_languages.json.
    Fällt auf eingebaute Mindeststliste zurück wenn Datei fehlt."""
    rtl_file = base_dir / "language" / "rtl_languages.json"
    try:
        data = json.loads(rtl_file.read_text(encoding="utf-8"))
        codes = set(data.get("codes", []))
        if codes:
            return codes
    except Exception:
        pass
    # Fallback – Mindestliste
    return {"ar", "he", "fa", "ur", "ps", "sd", "ug", "yi",
            "dv", "ku", "syr", "arc", "nqo", "rhg", "lad", "ckb"}

# ──────────────────────────────────────────────────────────────────────────────
# Hilfsfunktionen
# ──────────────────────────────────────────────────────────────────────────────

def _load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        QMessageBox.critical(None, "Error", f"Could not read file:\n{path}\n\n{e}")
        return {}


def _get_en_block(data: dict) -> str:
    en = data.get("en")
    if not en:
        for key, val in data.items():
            if not key.startswith("_") and isinstance(val, dict):
                en = val
                break
    if not en:
        return "{}"
    return json.dumps({"en": en}, ensure_ascii=False, indent=2)


def _validate(en_block: dict, user_block: dict) -> list:
    return sorted(set(en_block.keys()) - set(user_block.keys()))


def _make_btn(text, primary=False, green=False, width=None):
    b = QPushButton(text)
    if width:
        b.setFixedWidth(width)
    if primary:
        b.setStyleSheet("QPushButton{background:#0078D4;color:white;font-weight:bold;"
                        "border-radius:4px;padding:6px 14px;}"
                        "QPushButton:hover{background:#005fa3;}")
    elif green:
        b.setStyleSheet("QPushButton{background:#107C10;color:white;font-weight:bold;"
                        "border-radius:4px;padding:6px 14px;}"
                        "QPushButton:hover{background:#0a5a0a;}")
    else:
        b.setStyleSheet("QPushButton{border:1px solid #aaa;border-radius:4px;padding:6px 14px;}"
                        "QPushButton:hover{background:#e8e8e8;}")
    return b


# ──────────────────────────────────────────────────────────────────────────────
# Haupt-Dialog  –  nutzt QStackedWidget (kein deleteLater-Absturz)
# ──────────────────────────────────────────────────────────────────────────────

class LanguageTool(QDialog):
    def __init__(self, base_dir: Path, parent=None):
        super().__init__(parent)
        self.base_dir  = base_dir
        self._rtl_codes: set = _load_rtl_codes(base_dir)
        self.lang_file = base_dir / "language" / "languages.json"
        self.expl_file = base_dir / "language" / "formula_explanations.json"
        self.lang_data = _load_json(self.lang_file)
        self.expl_data = _load_json(self.expl_file)
        self.new_lang_code = ""

        # Sprachen aus libreoffice_calc_translations.json einlesen
        calc_tr_file = base_dir / "language" / "libreoffice_calc_translations.json"
        calc_tr = _load_json(calc_tr_file)
        first_entry = next(iter(calc_tr.values()), {}) if calc_tr else {}
        self._calc_tr_langs: set = set(first_entry.keys())

        self.setWindowTitle("Calc2 – Language Tool")
        self.setMinimumSize(720, 560)
        self.resize(740, 600)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)

        # QStackedWidget – alle Seiten leben gleichzeitig, wir schalten nur um
        self._stack = QStackedWidget(self)
        root = QVBoxLayout(self)
        root.setContentsMargins(0, 0, 0, 0)
        root.addWidget(self._stack)

        # Seiten aufbauen und zum Stack hinzufügen
        self._p1  = self._build_step1()
        self._p2  = self._build_step2()
        self._p3  = self._build_step3()
        self._p4  = self._build_step4()
        self._p5  = self._build_done()

        for p in [self._p1, self._p2, self._p3, self._p4, self._p5]:
            self._stack.addWidget(p)

        self._stack.setCurrentWidget(self._p1)

    def _go(self, page):
        """Sicher zur nächsten Seite wechseln – via QTimer damit der aktuelle Event abgeschlossen ist."""
        QTimer.singleShot(0, lambda: self._stack.setCurrentWidget(page))

    # ── Seite bauen: Header + Trennlinie ─────────────────────────────────────

    def _make_page(self, step: str, title: str):
        w = QWidget()
        layout = QVBoxLayout(w)
        layout.setContentsMargins(20, 16, 20, 12)
        layout.setSpacing(8)

        step_lbl = QLabel(step)
        step_lbl.setStyleSheet("color:#888; font-size:11px;")
        layout.addWidget(step_lbl)

        title_lbl = QLabel(title)
        title_lbl.setFont(QFont("Arial", 13, QFont.Bold))
        layout.addWidget(title_lbl)

        line = QWidget()
        line.setFixedHeight(1)
        line.setStyleSheet("background:#cccccc;")
        layout.addWidget(line)

        return w, layout

    # ── Schritt 1: Vorlage anzeigen ───────────────────────────────────────────

    def _build_step1(self):
        w, lay = self._make_page("Step 1 of 4", "English template – languages.json")

        info = QLabel(
            'Below you see the English ("en") block from languages.json – your template.\n\n'
            '1.  Click "Copy template" to copy it.\n'
            '2.  Paste it into a text editor or translation tool.\n'
            '3.  Translate all values (right side of each key).\n'
            '4.  Change the language code "en" to your new code  (e.g. "fr", "es", "ar", "he" …).\n'
            '5.  Click "Next ▶" when ready.\n\n'
            '💡  RTL-Sprachen (Arabisch, Hebräisch, Persisch, Urdu …) werden automatisch erkannt.\n'
            '    Das Tool fügt "rtl": true in den _meta-Block ein – kein manueller Schritt nötig.'
        )
        info.setWordWrap(True)
        info.setStyleSheet("font-size:11px; color:#333;")
        lay.addWidget(info)

        self._ed1 = QPlainTextEdit()
        self._ed1.setFont(QFont("Consolas", 10))
        self._ed1.setReadOnly(True)
        self._ed1.setPlainText(_get_en_block(self.lang_data))
        lay.addWidget(self._ed1)

        row = QHBoxLayout()
        copy_btn = _make_btn("📋  Copy template", width=160)
        next_btn = _make_btn("Next  ▶", primary=True, width=120)

        def _copy():
            QApplication.clipboard().setText(self._ed1.toPlainText())
            copy_btn.setText("✓  Copied!")
            QTimer.singleShot(1800, lambda: copy_btn.setText("📋  Copy template"))

        copy_btn.clicked.connect(_copy)
        next_btn.clicked.connect(lambda: self._go(self._p2))

        row.addWidget(copy_btn)
        row.addStretch()
        row.addWidget(next_btn)
        lay.addLayout(row)
        return w

    # ── Schritt 2: Einfügen + prüfen ─────────────────────────────────────────

    def _build_step2(self):
        w, lay = self._make_page("Step 2 of 4", "Paste your translation – languages.json")

        info = QLabel(
            'Paste your translated block below.\n'
            'Make sure the language code matches your target language  (e.g.  "fr": { ... }).\n'
            'Click "Check & Save" – the tool will validate and add it to languages.json.'
        )
        info.setWordWrap(True)
        info.setStyleSheet("font-size:11px; color:#333;")
        lay.addWidget(info)

        self._ed2 = QPlainTextEdit()
        self._ed2.setFont(QFont("Consolas", 10))
        lay.addWidget(self._ed2)

        self._status2 = QLabel("")
        self._status2.setWordWrap(True)
        self._status2.setStyleSheet("color:red; font-size:10px;")
        lay.addWidget(self._status2)

        row = QHBoxLayout()
        back_btn = _make_btn("◀  Back", width=100)
        save_btn = _make_btn("✔  Check & Save", green=True)
        back_btn.clicked.connect(lambda: self._go(self._p1))
        save_btn.clicked.connect(self._save_lang)
        row.addWidget(back_btn)
        row.addStretch()
        row.addWidget(save_btn)
        lay.addLayout(row)
        return w

    def _save_lang(self):
        raw = self._ed2.toPlainText().strip()
        self._status2.setText("")
        # KI liefert manchmal den Block ohne äußere { } → automatisch ergänzen
        if raw and not raw.startswith("{"):
            raw = "{" + raw + "}"
        try:
            user_data = json.loads(raw)
        except json.JSONDecodeError as e:
            self._status2.setText(f"❌  Invalid JSON: {e}")
            return

        keys = [k for k in user_data if not k.startswith("_")]
        if len(keys) != 1:
            self._status2.setText('❌  Please provide exactly one language block,  e.g.  { "fr": { … } }')
            return

        lang_code  = keys[0]
        lang_block = user_data[lang_code]
        if not isinstance(lang_block, dict):
            self._status2.setText("❌  The language block must be a JSON object { }.")
            return

        # ── Abgleich mit libreoffice_calc_translations.json ──────────────
        if self._calc_tr_langs:
            if lang_code not in self._calc_tr_langs:
                # Ähnliche Codes vorschlagen (z.B. "pt" → "pt-BR")
                similar = [c for c in sorted(self._calc_tr_langs)
                           if c.startswith(lang_code) or lang_code.startswith(c.split("-")[0])]
                hint = ""
                if similar:
                    hint = "\n\nÄhnliche Codes in LO: " + ", ".join(similar[:8])
                ans = QMessageBox.warning(
                    self, "⚠️  Sprachcode nicht in LibreOffice",
                    f'Sprachcode "{lang_code}" wurde nicht in \n'
                    f'libreoffice_calc_translations.json gefunden.\n\n'
                    f'Das bedeutet: Formelnamen können für diese Sprache \n'
                    f'NICHT übersetzt werden – sie bleiben auf Englisch.{hint}\n\n'
                    f'Trotzdem fortfahren?',
                    QMessageBox.Yes | QMessageBox.No
                )
                if ans != QMessageBox.Yes:
                    return

        if lang_code in self.lang_data:
            if QMessageBox.question(self, "Language exists",
                f'Language code "{lang_code}" already exists.\nOverwrite?',
                QMessageBox.Yes | QMessageBox.No) != QMessageBox.Yes:
                return

        en_block = self.lang_data.get("en", {})
        missing  = _validate(en_block, lang_block)
        if missing:
            preview = "\n".join(f"  • {k}" for k in missing[:20])
            if len(missing) > 20:
                preview += "\n  …"
            if QMessageBox.question(self, "Incomplete translation",
                f'{len(missing)} key(s) missing:\n\n{preview}\n\nSave anyway?',
                QMessageBox.Yes | QMessageBox.No) != QMessageBox.Yes:
                return

        # RTL-Sprache automatisch erkennen und _meta-Flag setzen
        rtl_note = ""
        if lang_code in self._rtl_codes:
            if "_meta" not in lang_block or not isinstance(lang_block["_meta"], dict):
                lang_block["_meta"] = {}
            lang_block["_meta"]["rtl"] = True
            rtl_note = '\n\n🔁  RTL erkannt: "rtl": true wurde automatisch in _meta eingefügt.'

        self.lang_data[lang_code] = lang_block
        self.new_lang_code = lang_code
        try:
            self.lang_file.write_text(
                json.dumps(self.lang_data, ensure_ascii=False, indent=2), encoding="utf-8")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Could not write languages.json:\n{e}")
            return

        QMessageBox.information(self, "Saved ✓",
            f'Language "{lang_code}" added to languages.json!{rtl_note}\n\nProceeding to formula_explanations.json …')
        self._go(self._p3)

    # ── Schritt 3: Vorlage formula_explanations ───────────────────────────────

    def _build_step3(self):
        w, lay = self._make_page("Step 3 of 4", "English template – formula_explanations.json")

        info = QLabel(
            'Below you see the English ("en") block from formula_explanations.json.\n'
            'These are the formula explanation texts shown in the app.\n\n'
            '⏭  This step is OPTIONAL – you can skip it.\n'
            '    If skipped, the app will fall back to the default explanations.'
        )
        info.setWordWrap(True)
        info.setStyleSheet("font-size:11px; color:#333;")
        lay.addWidget(info)

        self._ed3 = QPlainTextEdit()
        self._ed3.setFont(QFont("Consolas", 10))
        self._ed3.setReadOnly(True)
        lay.addWidget(self._ed3)

        row = QHBoxLayout()
        copy_btn = _make_btn("📋  Copy template", width=160)
        skip_btn = _make_btn("⏭  Skip", width=100)
        next_btn = _make_btn("Next  ▶", primary=True, width=120)

        def _copy():
            QApplication.clipboard().setText(self._ed3.toPlainText())
            copy_btn.setText("✓  Copied!")
            QTimer.singleShot(1800, lambda: copy_btn.setText("📋  Copy template"))

        copy_btn.clicked.connect(_copy)
        skip_btn.clicked.connect(lambda: self._go(self._p5))
        next_btn.clicked.connect(lambda: self._go(self._p4))
        row.addWidget(copy_btn)
        row.addStretch()
        row.addWidget(skip_btn)
        row.addWidget(next_btn)
        lay.addLayout(row)
        return w

    # ── Schritt 4: Einfügen formula_explanations ──────────────────────────────

    def _build_step4(self):
        w, lay = self._make_page("Step 4 of 4", "Paste your translation – formula_explanations.json")

        self._info4 = QLabel("")
        self._info4.setWordWrap(True)
        self._info4.setStyleSheet("font-size:11px; color:#333;")
        lay.addWidget(self._info4)

        self._ed4 = QPlainTextEdit()
        self._ed4.setFont(QFont("Consolas", 10))
        lay.addWidget(self._ed4)

        self._status4 = QLabel("")
        self._status4.setWordWrap(True)
        self._status4.setStyleSheet("color:red; font-size:10px;")
        lay.addWidget(self._status4)

        row = QHBoxLayout()
        back_btn = _make_btn("◀  Back", width=100)
        save_btn = _make_btn("✔  Check & Save", green=True)
        back_btn.clicked.connect(lambda: self._go(self._p3))
        save_btn.clicked.connect(self._save_expl)
        row.addWidget(back_btn)
        row.addStretch()
        row.addWidget(save_btn)
        lay.addLayout(row)
        return w

    def _save_expl(self):
        raw = self._ed4.toPlainText().strip()
        self._status4.setText("")
        # KI liefert manchmal den Block ohne äußere { } → automatisch ergänzen
        if raw and not raw.startswith("{"):
            raw = "{" + raw + "}"
        try:
            user_data = json.loads(raw)
        except json.JSONDecodeError as e:
            self._status4.setText(f"❌  Invalid JSON: {e}")
            return

        keys = [k for k in user_data if not k.startswith("_")]
        if len(keys) != 1:
            self._status4.setText("❌  Please provide exactly one language block.")
            return

        lang_code  = keys[0]
        lang_block = user_data[lang_code]
        en_block   = self.expl_data.get("en", {})
        missing    = _validate(en_block, lang_block)
        if missing:
            preview = "\n".join(f"  • {k}" for k in missing[:20])
            if len(missing) > 20:
                preview += "\n  …"
            if QMessageBox.question(self, "Incomplete translation",
                f'{len(missing)} key(s) missing:\n\n{preview}\n\nSave anyway?',
                QMessageBox.Yes | QMessageBox.No) != QMessageBox.Yes:
                return

        self.expl_data[lang_code] = lang_block
        try:
            self.expl_file.write_text(
                json.dumps(self.expl_data, ensure_ascii=False, indent=2), encoding="utf-8")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Could not write formula_explanations.json:\n{e}")
            return

        self._go(self._p5)

    # ── Fertig ────────────────────────────────────────────────────────────────

    def _build_done(self):
        w, lay = self._make_page("Done ✓", "Language successfully added!")

        self._done_lbl = QLabel("")
        self._done_lbl.setFont(QFont("Consolas", 11))
        self._done_lbl.setStyleSheet("color:#222; padding:16px 0;")
        lay.addWidget(self._done_lbl)
        lay.addStretch()

        row = QHBoxLayout()
        close_btn = _make_btn("Close", primary=True, width=120)
        close_btn.clicked.connect(self.accept)
        row.addStretch()
        row.addWidget(close_btn)
        lay.addLayout(row)
        return w

    # Wenn zur Done-Seite gewechselt wird, Text aktualisieren
    def _go(self, page):
        if page is self._p3:
            # formula_explanations Vorlage frisch laden
            self._ed3.setPlainText(_get_en_block(self.expl_data) if self.expl_data else '{\n  "en": {}\n}')
        if page is self._p4:
            self._info4.setText(
                'Paste your translated formula_explanations block below.\n'
                f'Use the same language code as before:  "{self.new_lang_code or "your_code"}"\n\n'
                'Click "Check & Save" to validate and update formula_explanations.json.'
            )
            self._ed4.clear()
        if page is self._p5:
            expl_ok = self.new_lang_code and self.new_lang_code in self.expl_data
            lines = []
            if self.new_lang_code:
                lines.append(f'✅  "{self.new_lang_code}" added to languages.json')
                lines.append(f'✅  "{self.new_lang_code}" added to formula_explanations.json'
                             if expl_ok else '⏭  formula_explanations.json – skipped')
            else:
                lines.append("No changes were made.")
            lines += ["", "Next steps:",
                      "  • Restart Calc2 to load the new language.",
                      "  • Select it from the language dropdown in the header."]
            self._done_lbl.setText("\n".join(lines))

        QTimer.singleShot(0, lambda: self._stack.setCurrentWidget(page))

    def run(self):
        self.exec_()


# ──────────────────────────────────────────────────────────────────────────────
# Direktstart zum Testen
# ──────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    # Beim Direktstart: language_tool.py liegt in services/
    # → parent = services/, parent.parent = Calc/
    _script_dir = Path(__file__).resolve().parent
    base = _script_dir.parent if _script_dir.name == "services" else _script_dir
    # Sicherheitscheck: languages.json muss erreichbar sein
    if not (base / "language" / "languages.json").exists():
        print(f"WARNUNG: languages.json nicht gefunden unter {base / 'language'}")
        print("Bitte language_tool.py aus dem Calc/-Ordner heraus starten.")
    LanguageTool(base_dir=base).run()
    sys.exit(0)
