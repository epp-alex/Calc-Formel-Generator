# LibreOffice Calc Formula Helper

A Python tool for quickly creating, testing and managing LibreOffice Calc formulas – with a favourites system, team synchronisation, multilingual support and a plugin manager.

## 🚀 Features

- 📑 4 tabs with over 60 functions

- 🌐 38 languages (incl. Hindi with automatic font installation)

- ⭐ Favourites system (local & team synchronisation via network drive)

- 🛠 Admin panel for team favourites (password-protected)

- 📋 Ready-to-paste formulas with syntax highlighting

- ✏️ Editable output field with undo/redo

- 📖 Integrated help & function reference (per language)

- 💾 Automatic saving (JSON, written atomically)

- 🌙 Dark mode

- 🔌 Plugin manager for creating your own formula plugins

- 🔤 RTL support (right-to-left) – automatic detection of writing direction

- 🗄️ Backup & Restore – save all settings and favourites with name and password

- ⌨️ Global hotkey `Ctrl+F12` to minimise/restore the window
- 🔍 JSON Validator – automatic checking and correction of `languages.json` and `formula_explanations.json`

## 🖥️ Usage

**1. Enter your values**

- Cell range (e.g. `A1:A10`)

- Cell 1 / Cell 2 (e.g. `A1`, `B1`)

- Optional parameter (e.g. text or index)

- Reference mode selectable: `A1`, `$A1`, `A$1`, `$A$1`

**2. Select a function** Choose a tab and click a function – the formula is generated instantly.

**3. Adjust the formula** The generated formula can be edited directly in the output field.

**4. Copy** Copy to clipboard with a single click (incl. syntax colours).

**5. Use favourites**

- ⭐ Save → store the current formula (Ctrl+S)

- 📂 Load → reuse a saved formula

- ❌ Delete → Delete key or button

- 🕐 History → recently used formulas

## 📊 Tab Overview

**Tab 1 – Basic Functions** `+` `-` `\*` `/` `^` SUM, AVERAGE, MIN, MAX, MEDIAN, COUNT, COUNTA, SUMPRODUCT

**Tab 2 – Advanced Functions** IF, AND, OR, NOT SUMIF, COUNTIF, AVERAGEIF, SUMIFS, STDEV, VAR, COUNTBLANK, LARGE

**Tab 3 – Date & Text** TODAY, NOW, YEAR, MONTH, DAY, DATE, DATEDIF, WEEKDAY CONCATENATE, LEN, LEFT, RIGHT, MID, UPPER, LOWER, TRIM

**Tab 4 – Lookup & Rounding** VLOOKUP, HLOOKUP, INDEX, MATCH, INDEX+MATCH ROUND, ROUNDUP, ROUNDDOWN, INT, TRUNC, ABS, MOD, SQRT, RAND


## 📖 Formula Explanations from the LibreOffice Documentation

The file `formula_explanations.json` is populated directly from the official **LibreOffice Calc documentation** (https://help.libreoffice.org).

### Data Source & Updates

- Descriptions, syntax information and examples are taken from the official LibreOffice help website
- Supported languages depend on the translations available on the website
- The file contains for each function: name, syntax, description, example and category
- Additions or corrections can be made manually (see JSON Validator)

### Structure of `formula_explanations.json`

```json
{
  "SUM": {
    "en": {
      "syntax": "SUM(Number1; Number2; ...)",
      "description": "Adds all numbers in a cell range.",
      "example": "=SUM(A1:A10)"
    },
    "de": {
      "syntax": "SUMME(Zahl1; Zahl2; ...)",
      "description": "Addiert alle Zahlen in einem Zellbereich.",
      "example": "=SUMME(A1:A10)"
    }
  }
}
```

### Available Fields per Entry

| Field | Required | Description |
|-------|----------|-------------|
| `syntax` | ✅ | Formula syntax with parameters |
| `description` | ✅ | Short description of the function |
| `example` | ✅ | Usage example as a ready-to-use formula |
| `note` | ❌ | Optional note (e.g. special behaviour or limits) |

> 💡 **Note:** If no entry exists for a language, the app automatically falls back to the English version.

---

## 🔍 JSON Validator for Language Files

The integrated **JSON Validator** checks and corrects both `languages.json` and `formula_explanations.json` for consistency, completeness and correct country designations.

Accessible via **Settings → 🔍 JSON Validator**.

### What is checked?

#### `languages.json`

- ✅ All 38 languages present (by ISO 639-1 language code)
- ✅ Correct **country and language names** (e.g. `"en"` → `"English"`, `"de"` → `"Deutsch"`)
- ✅ No duplicate language codes
- ✅ Required fields present: `name`, `native_name`, `flag`, `rtl`
- ✅ RTL flag correctly set (Arabic, Hebrew, Persian, Urdu → `"rtl": true`)
- ✅ Flag emoji matches the country code

#### `formula_explanations.json`

- ✅ All functions from the 4 tabs are recorded
- ✅ Required fields present: `syntax`, `description`, `example`
- ✅ No empty fields (`""` or `null`)
- ✅ Language codes match `languages.json`
- ✅ No duplicate function names

### Correction Functions

| Error type | Automatic correction |
|------------|---------------------|
| Wrong country name | Replaced with the correct name per ISO standard |
| Missing language entry | Filled with English fallback |
| Empty required field | Marked as `"[MISSING]"` for manual review |
| Duplicate entry | Duplicates removed, more complete entry kept |
| Incorrect RTL flag | Corrected automatically based on known RTL codes |

### How to Use

1. Open **Settings → 🔍 JSON Validator**
2. Select file: `languages.json` or `formula_explanations.json` (or both at once)
3. **🔎 Check** – shows all found issues in a clear list
4. **🛠 Auto-correct** – fixes all automatically solvable errors
5. **💾 Save** – writes the corrected file back atomically
6. **📋 Export report** (optional) – saves a text file with all findings

> ⚠️ **Note:** Before every automatic correction, a backup copy of the original file is created (`languages.json.bak` / `formula_explanations.json.bak`).

### Known Country Names – Correction Table (Selection)

| Language code | Wrong (examples) | Correct |
|---------------|-----------------|---------|
| `de` | German, Allemand | Deutsch |
| `en` | Englisch, Anglais | English |
| `fr` | French, Französisch | Français |
| `ar` | Arabic, Arabisch | العربية |
| `zh` | Chinese, Chinesisch | 中文 |
| `hi` | Hindi_IN, Hindisch | हिंदी |
| `he` | Hebrew, Hebräisch | עברית |
| `fa` | Farsi, Persian | فارسی |
| `ur` | Urdu_PK, Urdisch | اردو |
| `tr` | Turkish, Türkisch_TR | Türkçe |
| `ru` | Russian, Russisch | Русский |
| `ja` | Japanese, Japanisch | 日本語 |
| `ko` | Korean, Koreanisch | 한국어 |

> 💡 The validator checks all 38 supported languages for the correct native name (`native_name`) per ISO standard.

## ⭐ Favourites System

- Save and reuse your own formulas

- Clear separation between personal and team favourites

- Team favourites are read-only (only admins can edit them)

- Duplicate entries are prevented

- Free sorting of personal favourites

- Synchronisation via network drive (optionally configurable)

### Team Synchronisation

Go to **Settings → 🌐 Network path** to enter a network drive path (e.g. `\\\\Server\\Share\\formulas`).

- On startup: network favourites are cached locally (offline fallback)

- On save: your own formulas are written to the network; team formulas remain untouched

## 🛠 Admin Panel

Accessible via the 🛠 button. On first click, a password is set (PBKDF2-SHA256, only the hash is stored).

- Add, edit and delete team formulas

- Change the password

- Write changes directly to the network drive

## 🔌 Plugin Manager

The plugin manager (`plugin_manager.py`) is a standalone tool for creating and managing your own formula plugins for Calc2. It is located in the same folder as `Calc2.py` and is launched from the 🔌 button inside Calc2.py.

### Features

- **Create new plugin** – step-by-step wizard (name, formulas, translations, summary)

- **Add formulas** – add formulas to an existing plugin

- **Edit translations** – translate formula labels into all 38 languages

- **Open plugin folder** – directly in the file explorer

- **Delete plugin** – with confirmation prompt

### Plugin Structure

Each plugin lives as a subfolder inside `plugins/` and consists of two files:

```
plugins/
  my_plugin/
    plugin.json      ← metadata (name, version, author, description)
    formulas.json    ← formulas with translations
```

**Example `plugin.json`:**

```json
{
  "id": "my_plugin",
  "enabled": true,
  "version": "1.0",
  "author": "Your Name",
  "icon": "💰",
  "name": { "en": "Finance Formulas", "de": "Finanz-Formeln" },
  "description": { "en": "Useful formulas for financial calculations." }
}
```

**Example `formulas.json`:**

```json
[
  {
    "formula": "=SUM(A1:A10)",
    "name": { "en": "Sum of range", "de": "Summe des Bereichs" },
    "description": { "en": "Adds all values in A1:A10." },
    "category": { "en": "Basic", "de": "Grundlagen" }
  }
]
```

### Important Notice (⚠️)

The plugin manager has an **⚠️ Important Notice** button. Clicking it opens a window with all the rules for correct plugin creation (in English). The same information is also available in `IMPORTANT_NOTICE.md`.

## 🌐 Multilingual Support

38 languages available, switchable directly inside the app.  
New languages can be added via the 🌍 button using the Language Wizard.

**Note for Hindi (हिंदी):** When switching to Hindi for the first time, the font *Noto Sans Devanagari* is installed system-wide once. Windows will prompt for administrator rights.

## 🔤 RTL Support (Right-to-Left)

Languages with right-to-left script are detected automatically and the entire interface is mirrored:

- **Arabic (عربي)** – automatic RTL detection
- **Hebrew (עברית)** – automatic RTL detection
- **Persian / Farsi (فارسی)** – automatic RTL detection
- **Urdu (اردو)** – automatic RTL detection

**What changes in RTL mode:** The entire UI layout is mirrored, input fields use RTL alignment, the font automatically switches to an RTL-compatible font (e.g. *Noto Sans Arabic*, *Noto Sans Hebrew*).

> 💡 **Note:** Generated LibreOffice formulas always remain in LTR syntax – only the user interface changes direction.


## 🗄️ Backup & Restore

### Creating a Backup

Via **Settings → 🗄️ Create Backup**:

1. **Name** – a freely chosen label (e.g. `Backup_May_2025`)
2. **Password** – the backup is AES-encrypted; restoration is impossible without it
3. **Save location** – local or on a network drive
4. Click **💾 Create Backup** – a `.calc2backup` file is created

**Backup contents:** All favourites, settings, team favourites (optional), installed plugins.

### Restoring a Backup

Via **Settings → 📂 Restore Backup**:

1. Select the backup file (`.calc2backup`)
2. Enter the password
3. Choose restore scope: favourites only / settings only / everything
4. Click **🔄 Restore**

> ⚠️ Existing data is overwritten during restore. An automatic backup of current data is offered beforehand.

> 🔑 **Forgotten password:** Backups cannot be restored without the correct password – keep it safe.


## 💡 Tips

- `$A$1` → absolute reference (dropdown next to cell fields)

- **Ctrl+S** → save formula to favourites

- **Ctrl+C** → copy formula (when not focused on an input field)

- **Ctrl+Z / Ctrl+Y** → undo / redo

- **Ctrl+F12** → minimise / restore the window (works even when Calc2 is minimised)

- **Delete key** in the favourites list → remove entry

- Formulas can be adjusted directly in the output field after generation

## 📁 Project Structure

```
Calc2.py                        ← main application
plugin_manager.py               ← plugin manager
IMPORTANT_NOTICE.md             ← notes on plugin creation
data/
  README_de.md / README_en.md / ...      ← help per language
  REFERENZ_de.md / REFERENZ_en.md / ...  ← function reference per language
language/
  languages.json                ← UI translations (38 languages)
  formula_explanations.json
services/
  language_tool.py              ← wizard: add a new language
  settings_service.py
  auth_service.py
  favorites_service.py
  network_sync.py
  install_service.py
  backup_service.py             ← backup & restore
  json_validator.py             ← checking & correction of languages.json / formula_explanations.json
plugins/                        ← plugin folder (created automatically)
  my_plugin/
    plugin.json
    formulas.json
fonts/
  NotoSansDevanagari-Regular.ttf  ← Hindi font
  NotoSansArabic-Regular.ttf      ← Arabic font (RTL)
  NotoSansHebrew-Regular.ttf      ← Hebrew font (RTL)
python/                         ← embedded Python
  python.exe
  ...
settings.json                   ← created automatically
favoriten.json                  ← local favourites (created automatically)
```

## 🧠 Technical Highlights

- **Atomic file writes** → prevents corrupted files when saving

- **Service architecture** → logic and UI are strictly separated

- **Automatic migration** → old favourites formats are detected and converted

- **Robust error handling** → corrupt files do not cause crashes

- **Syntax highlighting** → formulas are displayed in colour

- **Dark mode** → fully supported

- **Plugin system** → Calc2 is extensible with custom formula plugins

- **RTL engine** → automatic detection of RTL languages, full UI mirroring incl. matching fonts

- **Backup & Restore** → AES-encrypted backups with name and password, selective restore

- **JSON Validator** → automatic checking and correction of `languages.json` and `formula_explanations.json` incl. country names and required fields

- **LibreOffice source** → `formula_explanations.json` is populated from the official LibreOffice Calc documentation (https://help.libreoffice.org)

- **Global hotkey** → `Ctrl+F12` works system-wide via the `keyboard` library (background thread)

## Licence

Free to use for personal and commercial purposes.
