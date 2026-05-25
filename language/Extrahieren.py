#!/usr/bin/env python3
# coding: utf-8
"""
Kleinere Tkinter-App, die eine languages.json lädt,
die Top-Level-Sprachblöcke auflistet und jeden Block
als eigene Datei (JSON oder TXT) in einen Zielordner schreibt.
"""

import json
import os
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

class LangExporter(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Language Block Exporter")
        self.geometry("720x480")
        self.json_path = None
        self.data = {}
        self.out_dir = os.getcwd()

        # --- UI ---
        frm_top = tk.Frame(self)
        frm_top.pack(fill="x", padx=10, pady=8)

        tk.Button(frm_top, text="languages.json öffnen", command=self.open_json).pack(side="left")
        tk.Button(frm_top, text="Zielordner wählen", command=self.choose_outdir).pack(side="left", padx=6)
        tk.Button(frm_top, text="Alle exportieren (.json)", command=lambda: self.export_all(ext="json")).pack(side="left", padx=6)
        tk.Button(frm_top, text="Alle exportieren (.txt)", command=lambda: self.export_all(ext="txt")).pack(side="left", padx=6)

        frm_mid = tk.Frame(self)
        frm_mid.pack(fill="both", expand=True, padx=10, pady=8)

        left = tk.Frame(frm_mid)
        left.pack(side="left", fill="y")

        tk.Label(left, text="Gefundene Sprach-Keys:").pack(anchor="w")
        self.lb = tk.Listbox(left, selectmode="extended", width=24, height=20)
        self.lb.pack(side="left", fill="y")
        scrollbar = tk.Scrollbar(left, orient="vertical", command=self.lb.yview)
        scrollbar.pack(side="left", fill="y")
        self.lb.config(yscrollcommand=scrollbar.set)

        right = tk.Frame(frm_mid)
        right.pack(side="left", fill="both", expand=True, padx=10)

        tk.Label(right, text="Vorschau / Log:").pack(anchor="w")
        self.log = scrolledtext.ScrolledText(right, wrap="word", font=("Consolas", 10))
        self.log.pack(fill="both", expand=True)

        frm_bot = tk.Frame(self)
        frm_bot.pack(fill="x", padx=10, pady=8)
        tk.Button(frm_bot, text="Ausgewählte exportieren (.json)", command=lambda: self.export_selected(ext="json")).pack(side="left")
        tk.Button(frm_bot, text="Ausgewählte exportieren (.txt)", command=lambda: self.export_selected(ext="txt")).pack(side="left", padx=6)
        tk.Button(frm_bot, text="In Vorschau anzeigen", command=self.show_preview).pack(side="right")

        self.status_var = tk.StringVar(value=f"Zielordner: {self.out_dir}")
        tk.Label(self, textvariable=self.status_var, anchor="w").pack(fill="x", padx=10, pady=(0,8))

    # --- Aktionen ---
    def open_json(self):
        path = filedialog.askopenfilename(title="languages.json auswählen", filetypes=[("JSON files", "*.json"), ("All files", "*.*")])
        if not path:
            return
        try:
            with open(path, "r", encoding="utf-8") as f:
                raw = f.read()
            # robustes Laden: falls Kommentare vorhanden sind, versuchen wir json.load direkt und fallback auf simple strip
            try:
                data = json.loads(raw)
            except json.JSONDecodeError:
                # einfacher Kommentar-Strip (// oder #) - nicht perfekt, aber oft hilfreich
                clean_lines = []
                for line in raw.splitlines():
                    s = line.strip()
                    if s.startswith("//") or s.startswith("#"):
                        continue
                    if "//" in line:
                        line = line.split("//", 1)[0]
                    clean_lines.append(line)
                data = json.loads("\n".join(clean_lines))
            if not isinstance(data, dict):
                raise ValueError("Top-level ist kein JSON-Objekt (dict).")
            self.json_path = path
            self.data = data
            self.populate_listbox()
            self.log_insert(f"✅ '{os.path.basename(path)}' geladen. Gefundene Keys: {len(self.data.keys())}")
        except Exception as e:
            messagebox.showerror("Fehler", f"Fehler beim Laden der JSON-Datei:\n{e}")

    def choose_outdir(self):
        d = filedialog.askdirectory(title="Zielordner wählen", initialdir=self.out_dir)
        if d:
            self.out_dir = d
            self.status_var.set(f"Zielordner: {self.out_dir}")
            self.log_insert(f"Zielordner gesetzt: {self.out_dir}")

    def populate_listbox(self):
        self.lb.delete(0, tk.END)
        keys = list(self.data.keys())
        # optional: entferne meta/Anleitung-Keys aus der Auswahl, aber zeige sie an (markiert)
        for k in keys:
            self.lb.insert(tk.END, k)

    def export_all(self, ext="json"):
        if not self.data:
            messagebox.showwarning("Keine Daten", "Bitte zuerst eine languages.json laden.")
            return
        count = 0
        for key, block in self.data.items():
            # optional: skip internal keys like "_ANLEITUNG"
            if key.startswith("_"):
                continue
            try:
                self._write_block_file(key, block, ext)
                count += 1
            except Exception as e:
                self.log_insert(f"Fehler beim Schreiben {key}: {e}")
        self.log_insert(f"✅ Export abgeschlossen: {count} Dateien geschrieben (.{ext})")

    def export_selected(self, ext="json"):
        sel = [self.lb.get(i) for i in self.lb.curselection()]
        if not sel:
            messagebox.showinfo("Auswahl fehlt", "Bitte mindestens einen Sprach-Key auswählen.")
            return
        count = 0
        for key in sel:
            block = self.data.get(key)
            if block is None:
                self.log_insert(f"Key nicht gefunden: {key}")
                continue
            try:
                self._write_block_file(key, block, ext)
                count += 1
            except Exception as e:
                self.log_insert(f"Fehler beim Schreiben {key}: {e}")
        self.log_insert(f"✅ Export abgeschlossen: {count} Dateien geschrieben (.{ext})")

    def _write_block_file(self, lang_key, block, ext="json"):
        safe_key = lang_key.replace("/", "_").replace("\\", "_")
        if ext == "json":
            out_path = os.path.join(self.out_dir, f"{safe_key}.json")
            with open(out_path, "w", encoding="utf-8") as f:
                json.dump({lang_key: block}, f, ensure_ascii=False, indent=2)
            self.log_insert(f"geschrieben: {out_path}")
        else:
            # txt: menschenlesbar, key: value pro Zeile
            out_path = os.path.join(self.out_dir, f"{safe_key}.txt")
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(f"# Sprachblock: {lang_key}\n\n")
                if isinstance(block, dict):
                    for k, v in block.items():
                        # falls v komplex ist, als JSON-String schreiben
                        if isinstance(v, (dict, list)):
                            v_str = json.dumps(v, ensure_ascii=False)
                        else:
                            v_str = str(v)
                        f.write(f"{k} = {v_str}\n")
                else:
                    f.write(str(block))
            self.log_insert(f"geschrieben: {out_path}")

    def show_preview(self):
        sel = self.lb.curselection()
        if not sel:
            messagebox.showinfo("Vorschau", "Bitte einen Sprach-Key auswählen.")
            return
        key = self.lb.get(sel[0])
        block = self.data.get(key)
        if block is None:
            messagebox.showerror("Fehler", "Block nicht gefunden.")
            return
        pretty = json.dumps(block, ensure_ascii=False, indent=2)
        # zeige in einem separaten Fenster
        win = tk.Toplevel(self)
        win.title(f"Vorschau: {key}")
        txt = scrolledtext.ScrolledText(win, width=100, height=40, font=("Consolas", 10))
        txt.pack(fill="both", expand=True)
        txt.insert("1.0", pretty)
        txt.configure(state="disabled")

    def log_insert(self, text):
        self.log.insert(tk.END, text + "\n")
        self.log.see(tk.END)

if __name__ == "__main__":
    app = LangExporter()
    app.mainloop()
