# LibreOffice Calc Formulių Pagalbininkas

Python įrankis, skirtas greitai kurti, testuoti ir valdyti LibreOffice Calc formules – su mėgstamiausių sistema, komandos sinchronizavimu, daugiakalbystės palaikymu ir papildinių tvarkykle.

## 🚀 Funkcijos

- 📑 4 skirtukai su daugiau nei 60 funkcijų

- 🌐 38 kalbos (įskaitant hindi su automatišku šriftų diegimu)

- ⭐ Mėgstamiausių sistema (vietinė ir komandos sinchronizavimas per tinklo diską)

- 🛠 Administravimo skydelis komandos mėgstamiausiiems (apsaugotas slaptažodžiu)

- 📋 Tiesiogiai kopijuojamos formulės su sintaksės paryškinimo

- ✏️ Redaguojamas išvesties laukas su Atšaukti/Perdaryti funkcijomis

- 📖 Integruota pagalba ir funkcijų nuoroda (kiekvienai kalbai)

- 💾 Automatinis išsaugojimas (JSON, atominis įrašymas)

- 🌙 Tamsus režimas

- 🔌 Papildinių tvarkyklė savo formulių papildinių kūrimui

- 🔤 RTL palaikymas (iš dešinės į kairę) – automatinis rašymo krypties atpažinimas

- 🗄️ Atsarginė kopija ir atkūrimas – išsaugokite visus nustatymus ir mėgstamiausius su pavadinimu ir slaptažodžiu

- ⌨️ Visuotinis spartusis klavišas `Ctrl+F12` sumažinimui/atkūrimui
- 🔍 JSON tikrintuvas – automatinis `languages.json` ir `formula_explanations.json` tikrinimas ir taisymas

## 🖥️ Naudojimas

**1. Duomenų įvedimas**

- Ląstelių diapazonas (pvz. `A1:A10`)

- Ląstelė 1 / Ląstelė 2 (pvz. `A1`, `B1`)

- Neprivalomas parametras (pvz. tekstas arba indeksas)

- Pasirenkamas absoliučios nuorodos režimas: `A1`, `$A1`, `A$1`, `$A$1`

**2. Funkcijos pasirinkimas** Pasirinkite skirtuką ir spustelėkite funkciją – formulė sugeneruojama akimirksniu.

**3. Formulės koregavimas** Sugeneruotą formulę galima tiesiogiai redaguoti išvesties lauke.

**4. Kopijavimas** Vienu paspaudimu į iškarpinę (įskaitant sintaksės spalvas).

**5. Mėgstamiausių naudojimas**

- ⭐ Išsaugoti → išsaugoti esamą formulę (Ctrl+S)

- 📂 Įkelti → pakartotinai naudoti formulę

- ❌ Ištrinti → Del klavišas arba mygtukas

- 🕐 Istorija → neseniai naudotos formulės

## 📊 Skirtukų apžvalga

**1 skirtukas – Pagrindinės funkcijos** `+` `-` `\*` `/` `^` SUM, AVERAGE, MIN, MAX, MEDIAN, COUNT, COUNTA, SUMPRODUCT

**2 skirtukas – Išplėstinės funkcijos** IF, AND, OR, NOT SUMIF, COUNTIF, AVERAGEIF, SUMIFS, STDEV, VAR, COUNTBLANK, LARGE

**3 skirtukas – Data ir tekstas** TODAY, NOW, YEAR, MONTH, DAY, DATE, DATEDIF, WEEKDAY CONCATENATE, LEN, LEFT, RIGHT, MID, UPPER, LOWER, TRIM

**4 skirtukas – Paieška ir apvalinimas** VLOOKUP, HLOOKUP, INDEX, MATCH, INDEX+MATCH ROUND, ROUNDUP, ROUNDDOWN, INT, TRUNC, ABS, MOD, SQRT, RAND


## 📖 Formulių paaiškinimai iš LibreOffice dokumentacijos

Failas `formula_explanations.json` pildomas tiesiogiai iš **oficialios LibreOffice Calc dokumentacijos** (https://help.libreoffice.org).

### Duomenų šaltinis ir atnaujinimas

- Aprašymai, sintaksės informacija ir pavyzdžiai imami iš oficialios LibreOffice pagalbos svetainės
- Palaikomos kalbos priklauso nuo svetainėje esamų vertimų
- Failas kiekvienai funkcijai apima: pavadinimą, sintaksę, aprašymą, pavyzdį ir kategoriją
- Papildymai ar pataisymai gali būti atlikti rankiniu būdu (žr. JSON tikrintuvas)

### `formula_explanations.json` struktūra

```json
{
  "SUM": {
    "lt": {
      "syntax": "SUM(Skaičius1; Skaičius2; ...)",
      "description": "Sudeda visus skaičius ląstelių diapazone.",
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

| Laukas | Privalomas | Aprašymas |
|--------|-----------|-----------|
| `syntax` | ✅ | Formulės sintaksė su parametrais |
| `description` | ✅ | Trumpas funkcijos aprašymas |
| `example` | ✅ | Naudojimo pavyzdys kaip paruošta formulė |
| `note` | ❌ | Neprivaloma pastaba |

> 💡 **Pastaba:** Jei kalbai nėra įrašo, programa automatiškai grįžta prie anglų kalbos versijos.

---

## 🔍 JSON tikrintuvas kalbų failams

Integruotas **JSON tikrintuvas** tikrina ir taiso `languages.json` ir `formula_explanations.json` nuoseklumą, išsamumą ir teisingus šalių pavadinimus. Pasiekiamas per **Nustatymai → 🔍 JSON tikrintuvas**.

### Kas tikrinama?

#### `languages.json`

- ✅ Visos 38 kalbos yra (pagal ISO 639-1 kalbos kodą)
- ✅ Teisingi **šalių ir kalbų pavadinimai** (pvz. `"lt"` → `"Lietuvių"`)
- ✅ Nėra pasikartojančių kalbų kodų
- ✅ Privalomi laukai yra: `name`, `native_name`, `flag`, `rtl`
- ✅ RTL žymė teisingai nustatyta (Arabų, Hebrajų, Persų, Urdu → `"rtl": true`)

#### `formula_explanations.json`

- ✅ Visos 4 skirtukų funkcijos užregistruotos
- ✅ Privalomi laukai yra: `syntax`, `description`, `example`
- ✅ Nėra tuščių laukų (`""` arba `null`)
- ✅ Kalbų kodai atitinka `languages.json`

### Taisymo funkcijos

| Klaidos tipas | Automatinis taisymas |
|-------------|---------------------|
| Neteisingas šalies pavadinimas | Pakeičiamas teisingu pagal ISO standartą |
| Trūkstamas kalbos įrašas | Užpildomas anglų kalbos atsarginiu variantu |
| Tuščias privalomas laukas | Pažymimas kaip `"[MISSING]"` rankiniam patikrinimui |
| Pasikartojantis įrašas | Dublikatai pašalinami, išsaugomas išsamesnis |
| Neteisinga RTL žymė | Automatiškai pataisoma remiantis žinomais RTL kodais |

### Naudojimas

1. Atidarykite **Nustatymai → 🔍 JSON tikrintuvas**
2. Pasirinkite failą: `languages.json` arba `formula_explanations.json` (arba abu)
3. **🔎 Tikrinti** – rodo visas rastas problemas
4. **🛠 Taisyti automatiškai** – taiso visas automatiškai sprendžiamas klaidas
5. **💾 Išsaugoti** – atomiškai įrašo pataisytą failą
6. **📋 Eksportuoti ataskaitą** (neprivaloma) – išsaugo tekstinį failą su visais rezultatais

> ⚠️ **Pastaba:** Prieš kiekvieną automatinį taisymą sukuriama pradinio failo atsarginė kopija (`languages.json.bak` / `formula_explanations.json.bak`).

## ⭐ Mėgstamiausių sistema

- Savo formulių išsaugojimas ir pakartotinis naudojimas

- Asmeninių ir komandos mėgstamiausių atskyrimas

- Komandos mėgstamiausi yra tik skaitymui (tik administratorius gali redaguoti)

- Dublikatai neleidžiami

- Laisvas asmeninių mėgstamiausių rūšiavimas

- Sinchronizavimas per tinklo diską (pasirinktinai konfigūruojama)

### Komandos sinchronizavimas

Per **Nustatymai → 🌐 Tinklo kelias** galima įvesti tinklo diską (pvz. `\\\\Serveris\\Bendrinama\\formules`).

- Paleidžiant: tinklo mėgstamiausi išsaugomi vietiškai (atsarginė kopija be interneto)

- Išsaugant: savos formulės įrašomos į tinklą, komandos formulės lieka nepakeistos

## 🛠 Administravimo skydelis

Pasiekiamas per 🛠 mygtuką. Pirmą kartą paspaudus nustatomas slaptažodis (PBKDF2-SHA256, išsaugomas tik maišos kodas).

- Komandos formulių pridėjimas, redagavimas ir trynimas

- Slaptažodžio keitimas

- Pakeitimai tiesiogiai įrašomi į tinklo diską

## 🔌 Papildinių tvarkyklė

Papildinių tvarkyklė (`plugin_manager.py`) yra atskiras įrankis skirtas kurti ir valdyti savus formulių papildinius Calc2. Ji yra tame pačiame aplanke kaip ir `Calc2.py` ir paleidžiama 🔌 mygtuku Calc2.py:

### Funkcijos

- **Naujo papildinio kūrimas** – žingsnis po žingsnio vedlys (pavadinimas, formulės, vertimai, santrauka)

- **Formulių pridėjimas** – formulių papildymas esamame papildinyje

- **Vertimų redagavimas** – formulių pavadinimų vertimas į visas 38 kalbas

- **Papildinių aplanko atidarymas** – tiesiogiai failų tvarkyklėje

- **Papildinio trynimas** – su saugos patvirtinimu

### Papildinio struktūra

Kiekvienas papildinys yra kaip poaplankis `plugins/` kataloge ir susideda iš dviejų failų:

```
plugins/
  mano_papildinys/
    plugin.json      ← metaduomenys (pavadinimas, versija, autorius, aprašymas)
    formulas.json    ← formulės su vertimais
```

**Pavyzdys `plugin.json`:**

```
{
  "id": "mano_papildinys",
  "enabled": true,
  "version": "1.0",
  "author": "Jūsų Vardas",
  "icon": "💰",
  "name": { "en": "Finance Formulas", "lt": "Finansų formulės" },
  "description": { "en": "Useful formulas for financial calculations." }
}
```

**Pavyzdys `formulas.json`:**

```
[
  {
    "formula": "=SUM(A1:A10)",
    "name": { "en": "Sum of range", "lt": "Diapazono suma" },
    "description": { "en": "Adds all values in A1:A10." },
    "category": { "en": "Basic", "lt": "Pagrindinė" }
  }
]
```

### Svarbus pranešimas (⚠️ Important Notice)

Papildinių tvarkyklėje yra mygtukas **⚠️ Important Notice**. Paspaudus atsidaro langas su visomis taisyklėmis, kaip teisingai kurti papildinius anglų kalba. Ta pati informacija taip pat pateikiama `IMPORTANT_NOTICE.md` faile.

## 🌐 Daugiakalbystė

Galimos 38 kalbos, keičiamos tiesiogiai programoje.
Naujas kalbas galima pridėti per 🌍 mygtuką su kalbų vedliu.

**Pastaba dėl hindi (हिंदी):** Pirmą kartą persijungus į hindi, *Noto Sans Devanagari* šriftas įdiegiamas vieną kartą sistemos lygmeniu. Windows paprašys administratoriaus teisių.

## 🔤 RTL palaikymas (iš dešinės į kairę)

Kalbos su rašymu iš dešinės į kairę atpažįstamos automatiškai ir visas sąsaja atspindima:

- **Arabų (عربي)** – automatinis RTL atpažinimas
- **Hebrajų (עברית)** – automatinis RTL atpažinimas
- **Persų / Farsi (فارسی)** – automatinis RTL atpažinimas
- **Urdu (اردو)** – automatinis RTL atpažinimas

**Kas keičiasi RTL režime:** Visas UI išdėstymas atspindimas, įvesties laukai naudoja RTL lygiavimą, šriftas automatiškai keičiasi į RTL suderinamą (pvz. *Noto Sans Arabic*, *Noto Sans Hebrew*).

> 💡 **Pastaba:** Generuotos LibreOffice formulės visada išlieka LTR sintaksėje – keičiasi tik vartotojo sąsajos kryptis.


## 🗄️ Atsarginė kopija ir atkūrimas

### Atsarginės kopijos kūrimas

Per **Nustatymai → 🗄️ Sukurti atsarginę kopiją**:

1. **Pavadinimas** – laisvas aprašas (pvz. `Kopija_Geguze_2025`)
2. **Slaptažodis** – kopija šifruojama AES; be jo atkūrimas neįmanomas
3. **Išsaugojimo vieta** – vietinis arba tinklo diskas
4. Spustelėkite **💾 Sukurti atsarginę kopiją** – sukuriamas `.calc2backup` failas

**Turinys:** Visi mėgstamiausi, nustatymai, komandos mėgstamiausi (pasirinktinai), įdiegti papildiniai.

### Atkūrimas

Per **Nustatymai → 📂 Atkurti atsarginę kopiją**:

1. Pasirinkite failą (`.calc2backup`)
2. Įveskite slaptažodį
3. Pasirinkite apimtį: tik mėgstamiausi / tik nustatymai / viskas
4. Spustelėkite **🔄 Atkurti**

> ⚠️ Atkuriant esami duomenys perrašomi. Prieš atkūrimą siūloma automatinė esamų duomenų atsarginė kopija.


## 💡 Patarimai

- `$A$1` → absoliuti nuoroda (išskleidžiamasis sąrašas šalia ląstelių laukų)

- **Ctrl+S** → išsaugoti formulę mėgstamiausiosiose

- **Ctrl+C** → kopijuoti formulę (už įvesties laukų ribų)

- **Ctrl+Z / Ctrl+Y** → Atšaukti / Perdaryti

- **Ctrl+F12** → sumažinti/atkurti langą (veikia net kai Calc2 yra sumažintas)

- **Del klavišas** mėgstamiausių sąraše → įrašo trynimas

- Formulės gali būti koreguojamos tiesiogiai išvesties lauke po sugeneravimo

## 📁 Projekto struktūra

```
Calc2.py                        ← pagrindinė programa
plugin_manager.py               ← papildinių tvarkyklė
IMPORTANT_NOTICE.md             ← papildinių kūrimo instrukcijos
data/
  README_lt.md / README_en.md / ...      ← pagalba kiekvienai kalbai
  NUORODA_lt.md / NUORODA_en.md / ...    ← funkcijų nuoroda kiekvienai kalbai
language/
  languages.json                ← sąsajos vertimai (38 kalbos)
  formula_explanations.json
services/
  language_tool.py              ← vedlys: naujos kalbos pridėjimas
  settings_service.py
  auth_service.py
  favorites_service.py
  network_sync.py
  install_service.py
  backup_service.py             ← atsarginė kopija ir atkūrimas
  json_validator.py             ← languages.json / formula_explanations.json tikrinimas ir taisymas
plugins/                        ← papildinių aplankas (sukuriamas automatiškai)
  mano_papildinys/
    plugin.json
    formulas.json
fonts/
  NotoSansDevanagari-Regular.ttf  ← hindi šriftas
  NotoSansArabic-Regular.ttf      ← arabų šriftas (RTL)
  NotoSansHebrew-Regular.ttf      ← hebrajų šriftas (RTL)
python/                         ← įdiegtas Python
  python.exe
  ...
settings.json                   ← sukuriamas automatiškai
megstamiausi.json               ← vietiniai mėgstamiausi (sukuriamas automatiškai)
```

## 🧠 Techniniai akcentai

- **Atominis failų įrašymas** → apsaugo failus nuo sugadinimo išsaugant

- **Paslaugų architektūra** → logika ir vartotojo sąsaja griežtai atskirtos

- **Automatinė migracija** → seni mėgstamiausių formatai atpažįstami ir konvertuojami

- **Patikimas klaidų valdymas** → sugadinti failai nesukelia programos gedimo

- **Sintaksės paryškinimas** → formulės rodomos spalvotai

- **Tamsus režimas** → pilnai palaikomas

- **Papildinių sistema** → Calc2 galima išplėsti savo formulių papildiniais

- **RTL variklis** → automatinis RTL kalbų atpažinimas, visiškas UI atspindėjimas su tinkamais šriftais

- **Atsarginė kopija ir atkūrimas** → AES šifruotos atsarginės kopijos su pavadinimu ir slaptažodžiu, pasirinktas atkūrimas

- **JSON tikrintuvas** → automatinis `languages.json` ir `formula_explanations.json` tikrinimas ir taisymas, įskaitant šalių pavadinimus ir privalomus laukus

- **LibreOffice šaltinis** → `formula_explanations.json` pildomas iš oficialios LibreOffice Calc dokumentacijos (https://help.libreoffice.org)

- **Visuotinis spartusis klavišas** → `Ctrl+F12` veikia sistemos lygmeniu per `keyboard` biblioteką (fono gija)

## Licencija

Laisvai naudojama asmeniniais ir komerciniais tikslais.
