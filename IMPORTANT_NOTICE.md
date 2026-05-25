# Calc2 Plugin Manager — Guide

## Quick Overview

1. Launch `plugin\_manager.py`.

2. Click **🆕 Create New Plugin**.

3. Enter name and description in **English**.

4. Add at least one formula — enter it in **English only** (e.g. `=SUM(A1:A10)`).

5. Optionally add name/description translations.

6. Click **✅ Create Plugin** — done.

> **New in this version:** Formula translations are handled **automatically** at runtime via `language/libreoffice\_calc\_translations.json`. You no longer need to enter the formula separately for each language — only the **English formula** is required.


## Main Window

### 🔍 Scan for Missing Translations

At the top of the Plugin Manager you will find the button:

> **🔍 Search all plugins for missing translations**

Click it to scan **all installed plugins** across **all supported languages** for missing **name/description** translations. The results window shows:

- 🟠 **Orange** — language/plugin combinations with missing entries, including a list of the affected formulas.

- 🟢 **Green** — language/plugin combinations that are fully translated.

- A **summary line** at the bottom with the total count of missing entries.

You can filter the results by a specific language using the dropdown at the top of the results window.


## Creating a New Plugin

Click **🆕 Create New Plugin**. The wizard guides you through four steps.

### Step 1 — Basic Info

Enter the basic details of your plugin.

| Field | Required | Description |
| - | - | - |
| **Name (English)** | ✅ Yes | The displayed plugin name. The folder ID is automatically generated (e.g. `Finance Formulas` → `finance\_formulas`). |
| **Description (English)** | No | A short description of the plugin. |
| **Version** | No | Defaults to `1.0`. |
| **Author** | No | Your name or team. |
| **Icon (Emoji)** | No | An optional emoji, e.g. `💰`. |


> Name and description must be in **English** — English is the fallback language for all users without a matching translation.

### Step 2 — Add Formulas

Add at least one formula. Click **➕ Add Formula**.

This dialog has two tabs:

**Tab 🇬🇧 English (Required)**

| Field | Required | Description |
| - | - | - |
| **Formula** | ✅ Yes | The formula in English LibreOffice notation, e.g. `=SUM(A1:A10)`. **Only English is needed** — the formula is translated automatically for all other languages at runtime. |
| **Name (EN)** | ✅ Yes | Display name of the formula, e.g. `Sum of range`. |
| **Description (EN)** | No | A brief explanation of what the formula does. |
| **Category (EN)** | No | Group/category, e.g. `Basic` or `Finance`. |


> ⚙️ **Automatic formula translation:** When a user opens the app in another language (e.g. German), the formula `=SUM(A1:A10)` is automatically converted to `=SUMME(A1:A10)` using `language/libreoffice\_calc\_translations.json`. No manual input required.

**Tab 🌐 Translations (optional)**

Here you can translate the **name, description and category** for each supported language. The formula field itself is **not shown here** — it is handled automatically.

Fields left empty fall back to English automatically.

**AI Translation (Quick Method):**

1. Click **📋 Copy English block for AI translation** — name, description and category are copied to the clipboard.

2. Paste into an AI tool (e.g. ChatGPT, Claude, Gemini) and request translation.

3. Copy the output and click **📥 Paste AI translations** — all fields are filled in automatically.

Formulas can be added at any time after plugin creation via **➕ Add Formulas to Plugin**.

### Step 3 — Translations (optional)

Translate the **plugin name and description** (not the formulas) into other languages. Click **➕ Add Language** and select a language.

Translations can also be added afterwards via **🌍 Edit Formula Translations**.

### Step 4 — Summary & Finish

A summary displays all entered data. Click **✅ Create Plugin** — the plugin is saved.


## Editing Existing Plugins

| Action | Description |
| - | - |
| **➕ Add Formulas to Plugin** | Add new formulas to an existing plugin. |
| **🌍 Edit Formula Translations** | Edit name/description/category translations for individual formulas. The formula itself does not need to be translated. Select a language, fill in the fields, click 💾 Save Translations. |
| **📂 Open Plugin Folder** | Opens the plugin folder in File Explorer. |
| **🗑 Delete Plugin** | Deletes the plugin and all its files (cannot be undone). |


### Translating Missing Entries Only

Inside **🌍 Edit Formula Translations**, use the button:

> **🤖 Only translate missing**

This builds an AI prompt containing **only the name/description entries that have no translation yet** for the selected language — saving time when you add new formulas to an already partially translated plugin.


## Formula Auto-Translation

Calc2 automatically translates formula function names at runtime using the file:

```
language/libreoffice\_calc\_translations.json
```

**Structure:**

```
\{  
  "SUM":  \{ "en": "SUM",   "de": "SUMME",  "fr": "SOMME",  "es": "SUMA", ... \},  
  "IF":   \{ "en": "IF",    "de": "WENN",   "fr": "SI",     "es": "SI",   ... \},  
  ...  
\}
```

**What this means for plugin authors:**

- Enter the formula **once, in English** (e.g. `=SUM(A1:A10)`).

- The app converts it to the user's language automatically (e.g. `=SUMME(A1:A10)` for German).

- If a function is not found in the translation file, the English name is used as fallback.

- Custom or non-standard function names that are not in the translation file are passed through unchanged.


## Plugin File Structure

Each plugin is stored in its own subfolder within the `plugins/` directory:

```
plugins/  
  finance\_formulas/  
    plugin.json      ← Metadata  
    formulas.json    ← Formula list
```

**plugin.json**

```
\{  
  "id": "finance\_formulas",  
  "enabled": true,  
  "version": "1.0",  
  "author": "Your Name",  
  "icon": "💰",  
  "min\_app\_version": "1.0.0",  
  "name":        \{ "en": "Finance Formulas", "de": "Finanz-Formeln" \},  
  "description": \{ "en": "Useful formulas for financial calculations." \}  
\}
```

**formulas.json**

```
\[  
  \{  
    "formula": "=@SUM(A1:A10)",  
    "name":        \{ "en": "Sum of range",             "de": "Summe eines Bereichs" \},  
    "description": \{ "en": "Adds all values in A1:A10." \},  
    "category":    \{ "en": "Basic" \}  
  \}  
\]
```

All text fields (`name`, `description`, `category`) are objects with language codes as keys. English (`"en"`) is always required; all other languages are optional.


## Import / Export

| Action | Description |
| - | - |
| **📦 Export Plugin (.zip)** | Saves the selected plugin as a `.zip` file for sharing or backup. |
| **📥 Import Plugin (.zip)** | Imports a plugin from a `.zip` file. If a plugin with the same ID already exists, you will be asked whether to overwrite it. |



## Supported Languages

`ar` · `bg` · `br` · `cs` · `da` · `de` · `el` · `en` · `es` · `et` · `fa` · `fi` · `fr` · `ga` · `he` · `hi` · `hr` · `hu` · `id` · `it` · `ja` · `ko` · `lt` · `lv` · `mt` · `nl` · `nn` · `no` · `pl` · `pt` · `ro` · `ru` · `sk` · `sl` · `sv` · `tr` · `uk` · `zh`

38 languages total.

