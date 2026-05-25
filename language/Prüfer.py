import json
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import re

def validate_json_structure():
    file_path = filedialog.askopenfilename(
        title="languages.json auswählen",
        filetypes=[("JSON files", "*.json")]
    )
    
    if not file_path:
        return

    ignore_list = ["_ANLEITUNG", "config_meta", "version", "_comment", "_meta"]

    try:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
        except UnicodeDecodeError:
            with open(file_path, 'r', encoding='cp1252') as f:
                lines = f.readlines()

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except UnicodeDecodeError:
            with open(file_path, 'r', encoding='cp1252') as f:
                data = json.load(f)

        report = "🔍 VALIDIERUNG DER SPRACHDATEI\n"
        report += f"📄 Datei: {file_path.split('/')[-1].split(chr(92))[-1]}\n"
        report += "=" * 60 + "\n\n"

        lang_pattern = re.compile(r'^\s*"([a-z]{2}(?:\-[A-Z]{2})?)":\s*\{')
        key_pattern  = re.compile(r'^\s*"([^"]+)"\s*:')

        # --- TEIL A: Doppelte Keys ---
        report += "1️⃣ PRÜFUNG AUF DOPPELTE KEYS PRO SPRACHE\n"
        current_lang = None
        lang_keys = {}

        for line_num, line in enumerate(lines, 1):
            lang_match = lang_pattern.search(line)
            if lang_match:
                current_lang = lang_match.group(1)
                if current_lang not in ignore_list:
                    lang_keys[current_lang] = {}
                continue
            if current_lang and current_lang not in ignore_list:
                key_match = key_pattern.search(line)
                if key_match:
                    k = key_match.group(1)
                    if k not in lang_keys[current_lang]:
                        lang_keys[current_lang][k] = []
                    lang_keys[current_lang][k].append(line_num)

        duplicate_found = False
        for lang, keys in lang_keys.items():
            for k, line_nums in keys.items():
                if len(line_nums) > 1:
                    report += (f"❌ Fehler in '{lang}': Key '{k}' kommt mehrfach vor "
                               f"(Zeilen: {', '.join(map(str, line_nums))})\n")
                    duplicate_found = True
        if not duplicate_found:
            report += "✅ Keine doppelten Keys innerhalb der einzelnen Sprachen gefunden.\n"

        report += "\n" + "=" * 60 + "\n\n"

        # --- TEIL B: Vergleich mit 'de' ---
        report += "2️⃣ VERGLEICH MIT DER REFERENZ 'de'\n"
        if "de" not in data:
            alle_keys = [k for k in data.keys() if k not in ignore_list]
            report += "❌ Fehler: Key 'de' als Referenz nicht in der Datei gefunden!\n"
            report += f"   Gefundene Top-Level-Keys: {alle_keys}\n"
        else:
            de_keys = set(data["de"].keys())
            for lang in data.keys():
                if lang in ignore_list or lang == "de" or not isinstance(data[lang], dict):
                    continue
                current_keys = set(data[lang].keys())
                missing = de_keys - current_keys
                if missing:
                    report += (f"❌ Sprache '{lang}' unvollständig! "
                               f"Es fehlen {len(missing)} Keys aus 'de':\n")
                    for m in sorted(missing):
                        report += f"   - {m}\n"
                else:
                    report += f"✅ Sprache '{lang}' ist vollständig (alle 'de' Keys vorhanden).\n"
                report += "-" * 30 + "\n"

        report += "\n" + "=" * 60 + "\n\n"

        # --- TEIL C: Einträge zählen ---
        report += "3️⃣ ANZAHL DER EINTRÄGE PRO SPRACHE\n"
        sprachen_count = {}
        for lang in data.keys():
            if lang in ignore_list or not isinstance(data[lang], dict):
                continue
            sprachen_count[lang] = len(data[lang])

        if sprachen_count:
            ref_count = sprachen_count.get("de", None)
            max_name_len = max(len(k) for k in sprachen_count)
            for lang, count in sorted(sprachen_count.items()):
                if ref_count is not None and lang != "de":
                    diff = count - ref_count
                    if diff == 0:
                        diff_str = ""
                    elif diff > 0:
                        diff_str = f"  ⚠️  (+{diff} extra)"
                    else:
                        diff_str = f"  ⚠️  ({diff} fehlend)"
                else:
                    diff_str = "  📌 Referenz"
                report += f"  {lang.ljust(max_name_len)} → {count:>5} Einträge{diff_str}\n"

            report += "\n"
            total_langs = len(sprachen_count)
            total_entries = sum(sprachen_count.values())
            report += f"📊 Zusammenfassung:\n"
            report += f"   Sprachen gesamt:  {total_langs}\n"
            report += f"   Einträge gesamt:  {total_entries}\n"
            if ref_count:
                report += f"   Referenz ('de'):  {ref_count} Einträge\n"
        else:
            report += "⚠️ Keine Sprachblöcke gefunden.\n"

        report += "\n" + "=" * 60 + "\n\n"

        # ----------------------------------------------------------------
        # TEIL D: Komma-Prüfung am Zeilenende
        # Jede Key-Value-Zeile AUSSER der letzten im Block braucht ein Komma.
        # Format:  "schluessel": "wert",
        # ----------------------------------------------------------------
        report += "4️⃣ PRÜFUNG AUF FEHLENDES KOMMA AM ZEILENENDE\n"
        report += '   Regel: Jede Zeile "key": "wert" muss mit , enden\n'
        report += "   (Ausnahme: letzte Zeile vor der schließenden })\n\n"

        # Passt auf:  "irgendwas": "irgendwas"   mit oder ohne Komma am Ende
        kv_line_pattern = re.compile(r'^\s*"([^"]+)"\s*:\s*"(.*?)"(\s*)(,?)\s*$')
        closing_brace   = re.compile(r'^\s*\}')

        current_lang   = None
        in_lang_block  = False
        lang_kv_lines  = {}   # { 'de': [(line_num, key, has_comma, raw_line), ...] }

        for line_num, line in enumerate(lines, 1):
            lang_match = lang_pattern.search(line)
            if lang_match:
                current_lang = lang_match.group(1)
                if current_lang not in ignore_list:
                    in_lang_block = True
                    lang_kv_lines[current_lang] = []
                else:
                    in_lang_block = False
                    current_lang  = None
                continue

            if in_lang_block and current_lang:
                if closing_brace.match(line):
                    in_lang_block = False
                    current_lang  = None
                    continue
                kv_match = kv_line_pattern.match(line)
                if kv_match:
                    key       = kv_match.group(1)
                    has_comma = kv_match.group(4) == ","
                    lang_kv_lines[current_lang].append(
                        (line_num, key, has_comma, line.rstrip())
                    )

        comma_errors_total = 0

        for lang, entries in lang_kv_lines.items():
            errors = []
            for i, (line_num, key, has_comma, raw) in enumerate(entries):
                is_last = (i == len(entries) - 1)
                # Letzte Zeile eines Blocks → kein Komma nötig (JSON-Standard)
                if is_last:
                    continue
                if not has_comma:
                    errors.append((line_num, key, raw))

            if errors:
                comma_errors_total += len(errors)
                report += f"❌ Sprache '{lang}': {len(errors)} Zeile(n) ohne Komma:\n"
                for line_num, key, raw in errors:
                    preview = raw.strip()
                    if len(preview) > 65:
                        preview = preview[:62] + "..."
                    report += f"   → Zeile {line_num:>6}: {preview}\n"
                report += "-" * 30 + "\n"
            else:
                report += f"✅ Sprache '{lang}': Alle Zeilen korrekt mit Komma.\n"

        report += "\n"
        if comma_errors_total == 0:
            report += "✅ Gesamt: Kein einziges fehlendes Komma gefunden!\n"
        else:
            report += f"⚠️  Gesamt: {comma_errors_total} Zeile(n) mit fehlendem Komma!\n"

        show_result_window(report)

    except Exception as e:
        messagebox.showerror("Fehler", f"Kritischer Fehler:\n{e}")


def show_result_window(report):
    result_win = tk.Toplevel()
    result_win.title("Detaillierter Sprach-Check")
    result_win.geometry("900x750")

    text_area = scrolledtext.ScrolledText(result_win, wrap=tk.WORD, font=("Consolas", 10))
    text_area.insert(tk.INSERT, report)
    text_area.config(state=tk.DISABLED)
    text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)


root = tk.Tk()
root.title("Sprach-Manager Validator")
root.geometry("400x200")

tk.Label(root, text="JSON Multi-Check", font=("Arial", 12, "bold")).pack(pady=20)
tk.Button(root, text="languages.json tiefenprüfen", command=validate_json_structure,
          bg="#28A745", fg="white", font=("Arial", 10, "bold"), padx=20, pady=10).pack()

root.mainloop()
