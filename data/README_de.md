# LibreOffice Calc Formel Helper

Ein Python-Tool zum schnellen Erstellen, Testen und Verwalten von LibreOffice Calc Formeln – mit Favoriten-System, Team-Synchronisation, Mehrsprachigkeit, RTL-Unterstützung, Backup & Restore und Plugin-Manager.

## 🚀 Features

- 📑 4 Tabs mit über 60 Funktionen

- 🌐 38 Sprachen (inkl. Hindi mit automatischer Schriftart-Installation)

- 🔤 RTL-Unterstützung (Arabisch, Hebräisch u. v. m.) – automatische Erkennung der Schreibrichtung

- ⭐ Favoriten-System (lokal & Team-Synchronisation über Netzlaufwerk)

- 🛠 Admin-Panel für Team-Favoriten (passwortgeschützt)

- 📋 Direkt kopierbare Formeln mit Syntax-Highlighting

- ✏️ Editierbares Ausgabefeld mit Undo/Redo

- 📖 Integrierte Hilfe & Funktionsreferenz (je Sprache)

- 💾 Automatische Speicherung (JSON, atomar geschrieben)

- 🌙 Dark Mode

- 🔌 Plugin-Manager zum Erstellen eigener Formel-Plugins

- ⌨️ Globaler Hotkey `Strg+F12` zum Minimieren/Wiederherstellen

- 🗄️ Backup & Restore – Sicherung aller Einstellungen und Favoriten mit Name und Passwort

- 🔍 JSON-Validator – Prüfung und Korrektur von `languages.json` und `formula\\\_explanations.json`

## 🖥️ Benutzung

**1. Eingaben machen**

- Zellbereich (z. B. `A1:A10`)

- Zelle 1 / Zelle 2 (z. B. `A1`, `B1`)

- Optionaler Parameter (z. B. Text oder Index)

- Absolut-Referenz-Modus wählbar: `A1`, `$A1`, `A$1`, `$A$1`

**2. Funktion auswählen** Wähle einen Tab und klicke eine Funktion – die Formel wird sofort generiert.

**3. Formel anpassen** Die generierte Formel kann direkt im Ausgabefeld bearbeitet werden.

**4. Kopieren** Mit einem Klick in die Zwischenablage übernehmen (inkl. Syntax-Farben).

**5. Favoriten nutzen**

- ⭐ Speichern → aktuelle Formel sichern (Strg+S)

- 📂 Laden → Formel wiederverwenden

- ❌ Löschen → Entf-Taste oder Button

- 🕐 Verlauf → zuletzt verwendete Formeln

## 📊 Tabs Übersicht

**Tab 1 – Grundfunktionen** `+` `-` `\\\\\\\*` `/` `^` SUM, AVERAGE, MIN, MAX, MEDIAN, COUNT, COUNTA, SUMPRODUCT

**Tab 2 – Erweiterte Funktionen** IF, AND, OR, NOT SUMIF, COUNTIF, AVERAGEIF, SUMIFS, STDEV, VAR, COUNTBLANK, LARGE

**Tab 3 – Datum & Text** TODAY, NOW, YEAR, MONTH, DAY, DATE, DATEDIF, WEEKDAY CONCATENATE, LEN, LEFT, RIGHT, MID, UPPER, LOWER, TRIM

**Tab 4 – Nachschlagen & Runden** VLOOKUP, HLOOKUP, INDEX, MATCH, INDEX+MATCH ROUND, ROUNDUP, ROUNDDOWN, INT, TRUNC, ABS, MOD, SQRT, RAND

## 📖 Formel-Erklärungen aus der LibreOffice-Dokumentation

Die Datei `formula\\\_explanations.json` wird direkt aus der offiziellen **LibreOffice Calc Formel-Dokumentation** befüllt ([https://help.libreoffice.org](https://help.libreoffice.org/)).

### Datenquelle & Aktualisierung

- Die Beschreibungen, Syntax-Angaben und Beispiele werden von der offiziellen LibreOffice-Hilfe-Webseite bezogen

- Unterstützte Sprachen richten sich nach den auf der Webseite verfügbaren Übersetzungen

- Die Datei enthält pro Funktion: Name, Syntax, Beschreibung, Beispiel und Kategorie

- Ergänzungen oder Korrekturen können manuell in der Datei vorgenommen werden (siehe JSON-Validator)

### Struktur `formula\\\_explanations.json`

```
\`\\\{\`  
  
\`  "SUM": \\\{\`  
  
\`    "de": \\\{\`  
  
\`      "syntax": "SUMME(Zahl1; Zahl2; ...)",\`  
  
\`      "description": "Addiert alle Zahlen in einem Zellbereich.",\`  
  
\`      "example": "=SUMME(A1:A10)"\`  
  
\`    \\\},\`  
  
\`    "en": \\\{\`  
  
\`      "syntax": "SUM(Number1; Number2; ...)",\`  
  
\`      "description": "Adds all numbers in a cell range.",\`  
  
\`      "example": "=SUM(A1:A10)"\`  
  
\`    \\\}\`  
  
\`  \\\}\`  
  
\`\\\}\`
```

### Verfügbare Felder pro Eintrag

| **Feld** | **Pflicht** | **Beschreibung** |
| :-: | :-: | :-: |
| `syntax` | ✅ | Formelsyntax mit Parametern |
| `description` | ✅ | Kurzbeschreibung der Funktion |
| `example` | ✅ | Anwendungsbeispiel als fertige Formel |
| `note` | ❌ | Optionaler Hinweis (z. B. Besonderheiten oder Grenzen) |


> 💡 **Hinweis:** Ist für eine Sprache kein Eintrag vorhanden, fällt die App automatisch auf die englische Version zurück.

## 🔍 JSON-Validator für Sprachdateien

Der integrierte **JSON-Validator** prüft und korrigiert sowohl `languages.json` als auch `formula\\\_explanations.json` auf Konsistenz, Vollständigkeit und korrekte Länderbezeichnungen.

Erreichbar über **Einstellungen → 🔍 JSON-Validator**.

### Was wird geprüft?

#### `languages.json`

- ✅ Alle 38 Sprachen vorhanden (nach ISO 639-1 Sprachcode)

- ✅ Korrekte **Länder- und Sprachbezeichnungen** (z. B. `"de"` → `"Deutsch"`, nicht `"German"` oder `"Allemand"`)

- ✅ Keine doppelten Sprachcodes

- ✅ Pflichtfelder vorhanden: `name`, `native\\\_name`, `flag`, `rtl`

- ✅ RTL-Kennzeichnung korrekt gesetzt (Arabisch, Hebräisch, Persisch, Urdu → `"rtl": true`)

- ✅ Flaggen-Emoji passend zum Ländercode

#### `formula\\\_explanations.json`

- ✅ Alle Funktionen aus den 4 Tabs sind eingetragen

- ✅ Pflichtfelder vorhanden: `syntax`, `description`, `example`

- ✅ Keine leeren Felder (`""` oder `null`)

- ✅ Sprachcodes in den Einträgen stimmen mit `languages.json` überein

- ✅ Keine doppelten Funktionsnamen

### Korrektur-Funktionen

Der Validator kann gefundene Fehler automatisch beheben:

| **Fehlertyp** | **Automatische Korrektur** |
| :-: | :-: |
| Falsche Länderbezeichnung | Ersetzt durch die korrekte Bezeichnung gemäß ISO-Standard |
| Fehlender Spracheintrag | Füllt fehlende Sprache mit englischem Fallback auf |
| Leeres Pflichtfeld | Markiert den Eintrag als `"\\\[MISSING\\\]"` zur manuellen Prüfung |
| Doppelter Eintrag | Entfernt Duplikate und behält den vollständigeren Eintrag |
| Falsch gesetztes RTL-Flag | Korrigiert automatisch anhand bekannter RTL-Sprachcodes |


### Bedienung

1. **Einstellungen → 🔍 JSON-Validator** öffnen

2. Datei auswählen: `languages.json` oder `formula\\\_explanations.json` (oder beide gleichzeitig)

3. **🔎 Prüfen** – zeigt alle gefundenen Probleme in einer übersichtlichen Liste

4. **🛠 Automatisch korrigieren** – behebt alle automatisch lösbaren Fehler

5. **💾 Speichern** – schreibt die korrigierte Datei atomar zurück

6. Optional: **📋 Bericht exportieren** – speichert eine Textdatei mit allen Befunden

> ⚠️ **Hinweis:** Vor jeder automatischen Korrektur wird eine Sicherungskopie der Originaldatei angelegt (`languages.json.bak` / `formula\\\_explanations.json.bak`).

### Bekannte Länderbezeichnungen – Korrekturtabelle (Auswahl)

| **Sprachcode** | **Falsch (Beispiele)** | **Korrekt** |
| :-: | :-: | :-: |
| `de` | German, Allemand, Deutsch\_DE | Deutsch |
| `en` | Englisch, Anglais | English |
| `fr` | French, Französisch | Français |
| `ar` | Arabic, Arabisch | العربية |
| `zh` | Chinese, Chinesisch | 中文 |
| `hi` | Hindi\_IN, Hindisch | हिंदी |
| `he` | Hebrew, Hebräisch | עברית |
| `fa` | Farsi, Persian | فارسی |
| `ur` | Urdu\_PK, Urdisch | اردو |
| `tr` | Turkish, Türkisch\_TR | Türkçe |
| `pl` | Polish, Polnisch | Polski |
| `pt` | Portuguese, Portugiesisch | Português |
| `ru` | Russian, Russisch | Русский |
| `uk` | Ukranian, Ukrainisch | Українська |
| `ko` | Korean, Koreanisch | 한국어 |
| `ja` | Japanese, Japanisch | 日本語 |


> 💡 Der Validator prüft alle 38 unterstützten Sprachen auf korrekte Eigenbezeichnung (`native\\\_name`) gemäß ISO-Standard.

## ⭐ Favoriten-System

- Eigene Formeln speichern und wiederverwenden

- Trennung zwischen eigenen und Team-Favoriten

- Team-Favoriten sind schreibgeschützt (nur Admin kann bearbeiten)

- Doppelte Einträge werden verhindert

- Freie Sortierung der eigenen Favoriten

- Synchronisation über Netzlaufwerk (optional konfigurierbar)

### Team-Synchronisation

Über **Einstellungen → 🌐 Netzpfad** lässt sich ein Netzlaufwerk eintragen (z. B. `\\\\\\\\\\\\\\\\Server\\\\\\\\Freigabe\\\\\\\\formeln`).

- Beim Start: Netz-Favoriten werden lokal gespeichert (Offline-Fallback)

- Beim Speichern: eigene Formeln werden ins Netz geschrieben, Team-Formeln bleiben unberührt

## 🗄️ Backup & Restore

Das integrierte Backup-System ermöglicht die vollständige Sicherung und Wiederherstellung aller Daten – inklusive Favoriten, Einstellungen und Team-Konfiguration.

### Backup erstellen

Erreichbar über **Einstellungen → 🗄️ Backup erstellen**:

1. **Name** eingeben – frei wählbare Bezeichnung für das Backup (z. B. `Backup\\\_Mai\\\_2025` oder `Vor\\\_Update`)

2. **Passwort** vergeben – das Backup wird AES-verschlüsselt gespeichert; ohne das Passwort ist keine Wiederherstellung möglich

3. **Speicherort** wählen – lokal oder auf einem Netzlaufwerk

4. Klick auf **💾 Backup erstellen** – erzeugt eine `.calc2backup`-Datei

**Inhalt des Backups:**

- Alle eigenen Favoriten (`favoriten.json`)

- Alle Einstellungen (`settings.json`)

- Optionale Team-Favoriten (sofern Netzpfad konfiguriert)

- Installierte Plugins (Metadaten und Formeln)

### Backup wiederherstellen (Restore)

Erreichbar über **Einstellungen → 📂 Backup wiederherstellen**:

1. **Backup-Datei** auswählen (`.calc2backup`)

2. **Passwort** eingeben – muss mit dem beim Erstellen verwendeten Passwort übereinstimmen

3. **Wiederherstellungsumfang** wählen:

   - Nur Favoriten

   - Nur Einstellungen

   - Alles wiederherstellen

4. Klick auf **🔄 Wiederherstellen** – Daten werden importiert, ein Neustart ist nicht erforderlich

> ⚠️ **Hinweis:** Beim Wiederherstellen werden die vorhandenen Daten überschrieben. Eine automatische Sicherung der aktuellen Daten wird vor dem Restore angeboten.

### Passwort vergessen

Backups ohne das korrekte Passwort können **nicht** wiederhergestellt werden (keine Hintertür). Passwörter sicher aufbewahren, z. B. in einem Passwort-Manager.

## 🛠 Admin-Panel

Erreichbar über den 🛠-Button. Beim ersten Klick wird ein Passwort festgelegt (PBKDF2-SHA256, nur Hash gespeichert).

- Team-Formeln hinzufügen, bearbeiten, löschen

- Passwort ändern

- Änderungen direkt ins Netzlaufwerk schreiben

## 🌐 Mehrsprachigkeit & RTL-Unterstützung

### 38 Sprachen

38 Sprachen sind verfügbar, direkt in der App umschaltbar.  
Neue Sprachen können über den 🌍-Button mit dem Language Wizard hinzugefügt werden.

**Hinweis Hindi (हिंदी):** Beim ersten Wechsel auf Hindi wird einmalig die Schriftart *Noto Sans Devanagari* systemweit installiert. Windows fragt dabei nach Administrator-Rechten.

### 🔤 RTL-Unterstützung (Right-to-Left)

Sprachen mit Rechts-nach-links-Schreibrichtung werden automatisch erkannt und die gesamte Oberfläche entsprechend gespiegelt:

- **Arabisch (عربي)** – automatische RTL-Erkennung

- **Hebräisch (עברית)** – automatische RTL-Erkennung

- **Persisch / Farsi (فارسی)** – automatische RTL-Erkennung

- **Urdu (اردو)** – automatische RTL-Erkennung

- Weitere RTL-Sprachen werden beim Hinzufügen über den Language Wizard automatisch erkannt

**Was wird bei RTL umgestellt:**

- Gesamtes UI-Layout wird gespiegelt (Buttons, Tabs, Felder)

- Texteingabefelder verwenden RTL-Ausrichtung

- Favoriten- und Verlaufsliste rechtsbündig

- Ausgabefeld für Formeln in RTL-Modus (Formeltext bleibt jedoch in LTR)

- Schriftart wird automatisch auf eine RTL-kompatible Schrift umgestellt (z. B. *Noto Sans Arabic*, *Noto Sans Hebrew*)

> 💡 **Hinweis:** Die generierten LibreOffice-Formeln selbst sind immer in LTR-Syntax – nur die Benutzeroberfläche wechselt die Richtung.

## 🔌 Plugin-Manager

Der Plugin-Manager (`plugin\\\_manager.py`) ist ein eigenständiges Tool zum Erstellen und Verwalten eigener Formel-Plugins für Calc2. Er liegt im selben Ordner wie `Calc2.py` und wird von Button 🔌 in Calc2.py gestartet:

### Funktionen

- **Neues Plugin erstellen** – Schritt-für-Schritt-Wizard (Name, Formeln, Übersetzungen, Zusammenfassung)

- **Formeln hinzufügen** – Formeln zu einem bestehenden Plugin ergänzen

- **Übersetzungen bearbeiten** – Formelbezeichnungen in alle 38 Sprachen übersetzen

- **Plugin-Ordner öffnen** – Direkt im Datei-Explorer

- **Plugin löschen** – inkl. Sicherheitsabfrage

### Plugin-Struktur

Jedes Plugin liegt als Unterordner in `plugins/` und besteht aus zwei Dateien:

```
\`plugins/\`  
  
\`  mein\\\_plugin/\`  
  
\`    plugin.json      ← Metadaten (Name, Version, Autor, Beschreibung)\`  
  
\`    formulas.json    ← Formeln mit Übersetzungen\`
```

**Beispiel `plugin.json`:**

```
\`\\\{\`  
  
\`  "id": "mein\\\_plugin",\`  
  
\`  "enabled": true,\`  
  
\`  "version": "1.0",\`  
  
\`  "author": "Dein Name",\`  
  
\`  "icon": "💰",\`  
  
\`  "name": \\\{ "en": "Finance Formulas", "de": "Finanz-Formeln" \\\},\`  
  
\`  "description": \\\{ "en": "Useful formulas for financial calculations." \\\}\`  
  
\`\\\}\`
```

**Beispiel `formulas.json`:**

```
\`\\\[\`  
  
\`  \\\{\`  
  
\`    "formula": "=SUM(A1:A10)",\`  
  
\`    "name": \\\{ "en": "Sum of range", "de": "Summe des Bereichs" \\\},\`  
  
\`    "description": \\\{ "en": "Adds all values in A1:A10." \\\},\`  
  
\`    "category": \\\{ "en": "Basic", "de": "Grundlagen" \\\}\`  
  
\`  \\\}\`  
  
\`\\\]\`
```

### Wichtiger Hinweis (⚠️ Important Notice)

Im Plugin-Manager gibt es den Button **⚠️ Important Notice**. Ein Klick öffnet ein Fenster mit allen Regeln zur korrekten Plugin-Erstellung auf Englisch. Dieselben Informationen stehen auch in `IMPORTANT\\\_NOTICE.md`.

## 💡 Tipps

- `$A$1` → absolute Referenz (Dropdown neben Zellfeldern)

- **Strg+S** → Formel in Favoriten speichern

- **Strg+C** → Formel kopieren (außerhalb von Eingabefeldern)

- **Strg+Z / Strg+Y** → Undo / Redo

- **Strg+F12** → Fenster minimieren / wiederherstellen (funktioniert auch wenn Calc2 minimiert ist)

- **Entf-Taste** in der Favoritenliste → Eintrag löschen

- Formeln können nach der Generierung direkt im Ausgabefeld angepasst werden

- Bei RTL-Sprachen: Die Formelausgabe bleibt immer LTR – nur das UI spiegelt sich

## 📁 Projektstruktur

```
\`Calc2.py                        ← Hauptprogramm\`  
  
\`plugin\\\_manager.py               ← Plugin-Manager\`  
  
\`IMPORTANT\\\_NOTICE.md             ← Hinweise zur Plugin-Erstellung\`  
  
\`data/\`  
  
\`  README\\\_de.md / README\\\_en.md / ...      ← Hilfe je Sprache\`  
  
\`  REFERENZ\\\_de.md / REFERENZ\\\_en.md / ...  ← Funktionsreferenz je Sprache\`  
  
\`language/\`  
  
\`  languages.json                ← UI-Übersetzungen (36 Sprachen)\`  
  
\`  formula\\\_explanations.json     ← Formel-Erklärungen (aus LibreOffice-Webseite)\`  
  
\`services/\`  
  
\`  language\\\_tool.py              ← Wizard: neue Sprache hinzufügen\`  
  
\`  settings\\\_service.py\`  
  
\`  auth\\\_service.py\`  
  
\`  favorites\\\_service.py\`  
  
\`  network\\\_sync.py\`  
  
\`  install\\\_service.py\`  
  
\`  backup\\\_service.py             ← Backup & Restore\`  
  
\`  json\\\_validator.py             ← Prüfung & Korrektur von languages.json / formula\\\_explanations.json\`  
  
\`plugins/                        ← Plugin-Ordner (automatisch erstellt)\`  
  
\`  mein\\\_plugin/\`  
  
\`    plugin.json\`  
  
\`    formulas.json\`  
  
\`fonts/\`  
  
\`  NotoSansDevanagari-Regular.ttf  ← Hindi-Schriftart\`  
  
\`  NotoSansArabic-Regular.ttf      ← Arabisch-Schriftart (RTL)\`  
  
\`  NotoSansHebrew-Regular.ttf      ← Hebräisch-Schriftart (RTL)\`  
  
\`python/                         ← eingebettetes Python\`  
  
\`  python.exe\`  
  
\`  ...\`  
  
\`settings.json                   ← wird automatisch erstellt\`  
  
\`favoriten.json                  ← lokale Favoriten (automatisch erstellt)\`
```

## 🧠 Technische Highlights

- **Atomic File Writes** → verhindert beschädigte Dateien beim Speichern

- **Service-Architektur** → Logik und UI strikt getrennt

- **Automatische Migration** → alte Favoriten-Formate werden erkannt und konvertiert

- **Robuste Fehlerbehandlung** → fehlerhafte Dateien führen nicht zum Absturz

- **Syntax-Highlighting** → Formeln werden farbig dargestellt

- **Dark Mode** → vollständig unterstützt

- **Plugin-System** → Calc2 ist erweiterbar durch eigene Formel-Plugins

- **Globaler Hotkey** → `Strg+F12` funktioniert systemweit über `keyboard`-Bibliothek (Hintergrund-Thread)

- **RTL-Engine** → automatische Erkennung von RTL-Sprachen, vollständiges UI-Spiegeln inkl. passender Schriftarten

- **Backup & Restore** → AES-verschlüsselte Backups mit Name und Passwort, selektive Wiederherstellung möglich

- **JSON-Validator** → automatische Prüfung und Korrektur von `languages.json` und `formula\\\_explanations.json` inkl. Länderbezeichnungen und Pflichtfeldern

- **LibreOffice-Datenquelle** → `formula\\\_explanations.json` wird aus der offiziellen LibreOffice Calc Dokumentation befüllt ([https://help.libreoffice.org](https://help.libreoffice.org/))

## Lizenz

Frei verwendbar für persönliche und kommerzielle Zwecke.

