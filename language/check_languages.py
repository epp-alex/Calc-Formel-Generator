import json
import os
import re

# KORREKTE PFADE ANPASSEN:
# Trage hier den Pfad zu deiner JSON-Datei ein
JSON_FILE = 'C:/Users/Alex/Desktop/Calc/language/languages.json'
# Trage hier den Ordnernamen ein, in dem die .md-Dateien liegen (z.B. 'daten' oder '.')
TARGET_DIR = 'C:/Users/Alex/Desktop/Calc/data'  

def verify_languages():
    # 1. JSON-Datei einlesen
    if not os.path.exists(JSON_FILE):
        print(f"❌ Fehler: Die Datei '{JSON_FILE}' wurde nicht gefunden.")
        return

    with open(JSON_FILE, 'r', encoding='utf-8') as f:
        try:
            lang_data = json.load(f)
        except json.JSONDecodeError as e:
            print(f"❌ Fehler beim Lesen der JSON-Datei: {e}")
            return

    # Sprachcodes extrahieren (interne Keys wie '_ANLEITUNG' ignorieren)
    json_langs = [key for key in lang_data.keys() if not key.startswith('_')]
    print(f"📋 In '{JSON_FILE}' definierte Sprachen ({len(json_langs)}):")
    print(f"   {', '.join(json_langs)}\n")

    # 2. Dateien aus dem Verzeichnis einlesen
    if not os.path.exists(TARGET_DIR):
        print(f"❌ Fehler: Der Ordner '{TARGET_DIR}' wurde nicht gefunden.")
        return

    actual_files = os.listdir(TARGET_DIR)

    # 3. Prüfung 1: JSON -> Dateien (Fehlen Dokumente zu einer registrierten Sprache?)
    print("=== 1. PRÜFUNG: Fehlen Dateien für definierte Sprachen? ===")
    missing_count = 0
    for lang in json_langs:
        readme_file = f"README_{lang}.md"
        referenz_file = f"REFERENZ_{lang}.md"
        
        # README prüfen
        if readme_file not in actual_files:
            print(f"❌ Fehler [{lang}]: '{readme_file}' fehlt im Ordner!")
            missing_count += 1
        
        # REFERENZ prüfen
        if referenz_file not in actual_files:
            print(f"❌ Fehler [{lang}]: '{referenz_file}' fehlt im Ordner!")
            missing_count += 1
            
    if missing_count == 0:
        print("✅ Vollständig! Alle in der JSON definierten Sprachen besitzen beide Dateien.\n")
    else:
        print(f"⚠️ Achtung: Es fehlen insgesamt {missing_count} Datei(en)!\n")

    # 4. Prüfung 2: Dateien -> JSON (Gibt es 'verwaiste' Dateien ohne JSON-Eintrag?)
    print("=== 2. PRÜFUNG: Gibt es unregistrierte Dateien im Ordner? ===")
    orphan_count = 0
    for file in actual_files:
        # Regulärer Ausdruck fängt auch komplexere Codes wie pt-BR ab
        match = re.match(r'^(README|REFERENZ)_(.+)\.md$', file)
        if match:
            file_type = match.group(1)
            lang_code = match.group(2)
            
            if lang_code not in json_langs:
                print(f"⚠️ Warnung: '{file}' existiert, aber '{lang_code}' ist nicht in der JSON eingetragen!")
                orphan_count += 1
                
    if orphan_count == 0:
        print("✅ Sauber! Keine unregistrierten Dokumentationsdateien gefunden.\n")
    else:
        print(f"💡 Tipp: Füge die fehlenden Sprachcodes in die '{JSON_FILE}' ein, damit die App sie nutzt.\n")

    # Fazit ausgeben
    print("=== FAZIT ===")
    if missing_count == 0 and orphan_count == 0:
        print("🎉 Perfekt! Deine JSON-Konfiguration und die Markdown-Dateien stimmen zu 100% überein.")
    else:
        print("🛠️ Es gibt Abweichungen. Bitte korrigiere die oben aufgelisteten Fehler.")

if __name__ == '__main__':
    verify_languages()