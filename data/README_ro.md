# LibreOffice Calc Asistent de Formule

Un instrument Python pentru crearea rapidă, testarea și gestionarea formulelor LibreOffice Calc – cu sistem de favorite, sincronizare de echipă, suport multilingv și manager de pluginuri.

## 🚀 Funcționalități

- 📑 4 file cu peste 60 de funcții

- 🌐 38 de limbi (inclusiv hindi cu instalare automată a fontului)

- ⭐ Sistem de favorite (local și sincronizare de echipă prin unitate de rețea)

- 🛠 Panou de administrare pentru favoritele echipei (protejat cu parolă)

- 📋 Formule gata de copiat cu evidențierea sintaxei

- ✏️ Câmp de ieșire editabil cu anulare/refacere

- 📖 Ajutor integrat și referință de funcții (per limbă)

- 💾 Salvare automată (JSON, scriere atomică)

- 🌙 Mod întunecat

- 🔌 Manager de pluginuri pentru crearea propriilor pluginuri de formule

- 🔤 Suport RTL (de la dreapta la stânga) – detectare automată a direcției de scriere

- 🗄️ Copie de rezervă și restaurare – salvați toate setările și favoritele cu nume și parolă

- ⌨️ Comandă rapidă globală `Ctrl+F12` pentru minimizarea/restaurarea ferestrei
- 🔍 Validator JSON – verificare și corecție automată a `languages.json` și `formula_explanations.json`

## 🖥️ Utilizare

**1. Introducerea datelor**

- Interval de celule (ex.: `A1:A10`)

- Celula 1 / Celula 2 (ex.: `A1`, `B1`)

- Parametru opțional (ex.: text sau index)

- Mod de referință absolută selectabil: `A1`, `$A1`, `A$1`, `$A$1`

**2. Selectarea unei funcții** Alegeți o filă și faceți clic pe o funcție – formula este generată imediat.

**3. Personalizarea formulei** Formula generată poate fi editată direct în câmpul de ieșire.

**4. Copiere** Transferați în clipboard cu un singur clic (inclusiv culorile sintaxei).

**5. Folosirea favoritelor**

- ⭐ Salvare → salvați formula curentă (Ctrl+S)

- 📂 Încărcare → reutilizați formula

- ❌ Ștergere → tasta Delete sau butonul

- 🕐 Istoric → formulele utilizate recent

## 📊 Prezentare generală a filelor

**Fila 1 – Funcții de bază** `+` `-` `*` `/` `^` SUM, AVERAGE, MIN, MAX, MEDIAN, COUNT, COUNTA, SUMPRODUCT

**Fila 2 – Funcții avansate** IF, AND, OR, NOT SUMIF, COUNTIF, AVERAGEIF, SUMIFS, STDEV, VAR, COUNTBLANK, LARGE

**Fila 3 – Dată și text** TODAY, NOW, YEAR, MONTH, DAY, DATE, DATEDIF, WEEKDAY CONCATENATE, LEN, LEFT, RIGHT, MID, UPPER, LOWER, TRIM

**Fila 4 – Căutare și rotunjire** VLOOKUP, HLOOKUP, INDEX, MATCH, INDEX+MATCH ROUND, ROUNDUP, ROUNDDOWN, INT, TRUNC, ABS, MOD, SQRT, RAND


## 📖 Explicații formule din documentația LibreOffice

Fișierul `formula_explanations.json` este populat direct din **documentația oficială LibreOffice Calc** (https://help.libreoffice.org).

### Sursă de date și actualizare

- Descrierile, informațiile de sintaxă și exemplele sunt preluate de pe site-ul oficial de ajutor LibreOffice
- Limbile acceptate depind de traducerile disponibile pe site
- Fișierul conține pentru fiecare funcție: nume, sintaxă, descriere, exemplu și categorie
- Completările sau corecțiile pot fi făcute manual (consultați Validator JSON)

### Structura `formula_explanations.json`

```json
{
  "SUM": {
    "ro": {
      "syntax": "SUM(Număr1; Număr2; ...)",
      "description": "Adună toate numerele dintr-un interval de celule.",
      "example": "=SUM(A1:A10)"
    },
    "en": {
      "syntax": "SUM(Number1; Number2; ...)",
      "description": "Adds all numbers in a cell range.",
      "example": "=SUM(A1:A10)"
    }
  }
}
```

| Câmp | Obligatoriu | Descriere |
|------|------------|-----------|
| `syntax` | ✅ | Sintaxa formulei cu parametri |
| `description` | ✅ | Descriere scurtă a funcției |
| `example` | ✅ | Exemplu de utilizare ca formulă gata pregătită |
| `note` | ❌ | Notă opțională |

> 💡 **Notă:** Dacă nu există o intrare pentru o limbă, aplicația revine automat la versiunea în engleză.

---

## 🔍 Validator JSON pentru fișierele de limbă

**Validatorul JSON** integrat verifică și corectează `languages.json` și `formula_explanations.json` pentru consistență, completitudine și denumiri corecte ale țărilor. Accesibil prin **Setări → 🔍 Validator JSON**.

### Ce se verifică?

#### `languages.json`

- ✅ Toate cele 38 de limbi sunt prezente (după codul ISO 639-1)
- ✅ **Denumiri corecte ale țărilor și limbilor** (ex.: `"ro"` → `"Română"`)
- ✅ Fără coduri de limbă duplicate
- ✅ Câmpuri obligatorii prezente: `name`, `native_name`, `flag`, `rtl`
- ✅ Fanion RTL setat corect (Arabă, Ebraică, Persană, Urdu → `"rtl": true`)

#### `formula_explanations.json`

- ✅ Toate funcțiile din cele 4 file înregistrate
- ✅ Câmpuri obligatorii prezente: `syntax`, `description`, `example`
- ✅ Fără câmpuri goale (`""` sau `null`)
- ✅ Codurile de limbă corespund cu `languages.json`

### Funcții de corecție

| Tip de eroare | Corecție automată |
|-------------|------------------|
| Denumire incorectă a țării | Înlocuită cu denumirea corectă conform ISO |
| Intrare limbă lipsă | Completată cu versiunea de rezervă în engleză |
| Câmp obligatoriu gol | Marcat ca `"[MISSING]"` pentru revizuire manuală |
| Intrare duplicată | Duplicatele eliminate, intrarea mai completă păstrată |
| Fanion RTL incorect | Corectat automat pe baza codurilor RTL cunoscute |

### Cum se utilizează

1. Deschide **Setări → 🔍 Validator JSON**
2. Selectează fișierul: `languages.json` sau `formula_explanations.json` (sau ambele)
3. **🔎 Verificare** – afișează toate problemele găsite
4. **🛠 Corecție automată** – rezolvă toate erorile corectabile automat
5. **💾 Salvare** – scrie atomic fișierul corectat
6. **📋 Export raport** (opțional) – salvează un fișier text cu toate constatările

> ⚠️ **Notă:** Înainte de fiecare corecție automată se creează o copie de siguranță a fișierului original (`languages.json.bak` / `formula_explanations.json.bak`).

## ⭐ Sistemul de favorite

- Salvarea și reutilizarea propriilor formule

- Separarea între favoritele personale și cele ale echipei

- Favoritele echipei sunt protejate la scriere (doar administratorul le poate edita)

- Intrările duplicate sunt prevenite

- Sortare liberă a favoritelor personale

- Sincronizare prin unitate de rețea (configurabil opțional)

### Sincronizarea de echipă

În **Setări → 🌐 Cale de rețea** se poate introduce o unitate de rețea (ex.: `\\\\Server\\Partajat\\formule`).

- La pornire: favoritele de rețea sunt salvate local (copie de rezervă offline)

- La salvare: formulele proprii sunt scrise în rețea, formulele echipei rămân nemodificate

## 🛠 Panoul de administrare

Accesibil prin butonul 🛠. La primul clic se setează o parolă (PBKDF2-SHA256, se salvează doar hash-ul).

- Adăugarea, editarea și ștergerea formulelor de echipă

- Schimbarea parolei

- Scrierea modificărilor direct pe unitatea de rețea

## 🔌 Managerul de pluginuri

Managerul de pluginuri (`plugin_manager.py`) este un instrument independent pentru crearea și gestionarea propriilor pluginuri de formule pentru Calc2. Se află în același folder ca `Calc2.py` și este pornit prin butonul 🔌 din Calc2.py:

### Funcții

- **Crearea unui plugin nou** – expert pas cu pas (nume, formule, traduceri, rezumat)

- **Adăugarea de formule** – adăugarea formulelor la un plugin existent

- **Editarea traducerilor** – traducerea numelor de formule în toate cele 38 de limbi

- **Deschiderea folderului de pluginuri** – direct în exploratorul de fișiere

- **Ștergerea unui plugin** – cu confirmare de siguranță

### Structura pluginului

Fiecare plugin se află ca subdosar în `plugins/` și este alcătuit din două fișiere:

```
plugins/
  pluginul_meu/
    plugin.json      ← metadate (nume, versiune, autor, descriere)
    formulas.json    ← formule cu traduceri
```

**Exemplu `plugin.json`:**

```
{
  "id": "pluginul_meu",
  "enabled": true,
  "version": "1.0",
  "author": "Numele dvs.",
  "icon": "💰",
  "name": { "en": "Finance Formulas", "ro": "Formule financiare" },
  "description": { "en": "Useful formulas for financial calculations." }
}
```

**Exemplu `formulas.json`:**

```
[
  {
    "formula": "=SUM(A1:A10)",
    "name": { "en": "Sum of range", "ro": "Suma intervalului" },
    "description": { "en": "Adds all values in A1:A10." },
    "category": { "en": "Basic", "ro": "De bază" }
  }
]
```

### Notă importantă (⚠️ Important Notice)

În managerul de pluginuri există butonul **⚠️ Important Notice**. Un clic deschide o fereastră cu toate regulile pentru crearea corectă a pluginurilor în limba engleză. Aceleași informații se găsesc și în `IMPORTANT_NOTICE.md`.

## 🌐 Suport multilingv

38 de limbi disponibile, comutabile direct în aplicație.  
Limbile noi pot fi adăugate prin butonul 🌍 cu Expertul de limbi.

**Notă privind hindi (हिंदी):** La prima comutare la hindi, fontul *Noto Sans Devanagari* este instalat o singură dată la nivel de sistem. Windows va solicita drepturi de administrator în acel moment.

## 🔤 Suport RTL (de la dreapta la stânga)

Limbile cu scriere de la dreapta la stânga sunt detectate automat și întreaga interfață este oglindită:

- **Arabă (عربي)** – detectare RTL automată
- **Ebraică (עברית)** – detectare RTL automată
- **Persană / Farsi (فارسی)** – detectare RTL automată
- **Urdu (اردو)** – detectare RTL automată

**Ce se schimbă în modul RTL:** Întregul aspect al interfeței este oglindit, câmpurile de introducere folosesc alinierea RTL, fontul se schimbă automat cu unul compatibil RTL (ex.: *Noto Sans Arabic*, *Noto Sans Hebrew*).

> 💡 **Notă:** Formulele LibreOffice generate rămân întotdeauna în sintaxă LTR – doar interfața utilizatorului își schimbă direcția.


## 🗄️ Copie de rezervă și restaurare

### Crearea unei copii de rezervă

Prin **Setări → 🗄️ Creare copie de rezervă**:

1. **Nume** – etichetă liberă (ex.: `Backup_Mai_2025`)
2. **Parolă** – copia este criptată AES; fără ea restaurarea este imposibilă
3. **Locație salvare** – local sau pe o unitate de rețea
4. Faceți clic pe **💾 Creare copie de rezervă** – se creează un fișier `.calc2backup`

**Conținut:** Toate favoritele, setările, favoritele echipei (opțional), pluginurile instalate.

### Restaurarea copiei de rezervă

Prin **Setări → 📂 Restaurare copie de rezervă**:

1. Selectați fișierul (`.calc2backup`)
2. Introduceți parola
3. Alegeți domeniul: doar favorite / doar setări / totul
4. Faceți clic pe **🔄 Restaurare**

> ⚠️ La restaurare datele existente sunt suprascrise. Înainte de restaurare se oferă o copie automată a datelor curente.


## 💡 Sfaturi

- `$A$1` → referință absolută (listă derulantă lângă câmpurile de celule)

- **Ctrl+S** → salvați formula în favorite

- **Ctrl+C** → copiați formula (în afara câmpurilor de introducere)

- **Ctrl+Z / Ctrl+Y** → anulare / refacere

- **Ctrl+F12** → minimizați / restaurați fereastra (funcționează și când Calc2 este minimizat)

- **Tasta Delete** în lista de favorite → ștergeți intrarea

- Formulele pot fi ajustate direct în câmpul de ieșire după generare

## 📁 Structura proiectului

```
Calc2.py                        ← programul principal
plugin_manager.py               ← managerul de pluginuri
IMPORTANT_NOTICE.md             ← note privind crearea pluginurilor
data/
  README_de.md / README_en.md / ...      ← ajutor per limbă
  REFERENZ_de.md / REFERENZ_en.md / ...  ← referință de funcții per limbă
language/
  languages.json                ← traduceri interfață (38 de limbi)
  formula_explanations.json
services/
  language_tool.py              ← expert: adăugarea unei noi limbi
  settings_service.py
  auth_service.py
  favorites_service.py
  network_sync.py
  install_service.py
  backup_service.py             ← copie de rezervă și restaurare
  json_validator.py             ← verificare și corecție languages.json / formula_explanations.json
plugins/                        ← folderul de pluginuri (creat automat)
  pluginul_meu/
    plugin.json
    formulas.json
fonts/
  NotoSansDevanagari-Regular.ttf  ← fontul hindi
  NotoSansArabic-Regular.ttf      ← font arab (RTL)
  NotoSansHebrew-Regular.ttf      ← font ebraic (RTL)
python/                         ← Python încorporat
  python.exe
  ...
settings.json                   ← creat automat
favorite.json                   ← favorite locale (creat automat)
```

## 🧠 Aspecte tehnice remarcabile

- **Scriere atomică a fișierelor** → previne fișierele corupte la salvare

- **Arhitectură de servicii** → logica și interfața utilizatorului sunt strict separate

- **Migrare automată** → formatele vechi de favorite sunt detectate și convertite

- **Gestionare robustă a erorilor** → fișierele defecte nu provoacă blocarea aplicației

- **Evidențierea sintaxei** → formulele sunt afișate în culori

- **Mod întunecat** → complet suportat

- **Sistem de pluginuri** → Calc2 poate fi extins cu pluginuri de formule proprii

- **Motor RTL** → detectare automată a limbilor RTL, oglindire completă a interfeței cu fonturi adecvate

- **Copie de rezervă și restaurare** → copii de rezervă criptate AES cu nume și parolă, restaurare selectivă

- **Validator JSON** → verificare și corecție automată a `languages.json` și `formula_explanations.json` incl. denumiri ale țărilor și câmpuri obligatorii

- **Sursă LibreOffice** → `formula_explanations.json` este populat din documentația oficială LibreOffice Calc (https://help.libreoffice.org)

- **Comandă rapidă globală** → `Ctrl+F12` funcționează la nivel de sistem prin biblioteca `keyboard` (fir de execuție în fundal)

## Licență

Liber de utilizat în scopuri personale și comerciale.
