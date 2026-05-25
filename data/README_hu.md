# LibreOffice Calc Képletsegéd

Egy Python-eszköz LibreOffice Calc képletek gyors létrehozásához, teszteléséhez és kezeléséhez – kedvencek rendszerével, csapatsszinkronizálással, többnyelvűséggel és bővítménykezelővel.

## 🚀 Funkciók

- 📑 4 fül több mint 60 funkcióval

- 🌐 38 nyelv (köztük hindi automatikus betűtípus-telepítéssel)

- ⭐ Kedvencek rendszer (helyi és csapatsszinkronizálás hálózati meghajtón keresztül)

- 🛠 Adminisztrációs panel a csapat kedvenceihez (jelszóval védett)

- 📋 Közvetlenül másolható képletek szintaxiskiemelással

- ✏️ Szerkeszthető kimeneti mező Visszavonás/Újra funkcióval

- 📖 Beépített súgó és funkcióhivatkozás (nyelvenként)

- 💾 Automatikus mentés (JSON, atomi írással)

- 🌙 Sötét mód

- 🔌 Bővítménykezelő saját képletbővítmények létrehozásához

- 🔤 RTL támogatás (jobbról balra) – az írásirány automatikus felismerése

- 🗄️ Biztonsági mentés és visszaállítás – mentse az összes beállítást és kedvencet névvel és jelszóval

- ⌨️ Globális gyorsbillentyű `Ctrl+F12` kis méretbe helyezéshez/visszaállításhoz
- 🔍 JSON-érvényesítő – `languages.json` és `formula_explanations.json` automatikus ellenőrzése és javítása

## 🖥️ Használat

**1. Adatok megadása**

- Cellatartomány (pl. `A1:A10`)

- Cella 1 / Cella 2 (pl. `A1`, `B1`)

- Opcionális paraméter (pl. szöveg vagy index)

- Abszolút hivatkozási mód választható: `A1`, `$A1`, `A$1`, `$A$1`

**2. Funkció kiválasztása** Válasszon egy fület, és kattintson egy funkcióra – a képlet azonnal létrejön.

**3. Képlet módosítása** A generált képlet közvetlenül szerkeszthető a kimeneti mezőben.

**4. Másolás** Egy kattintással a vágólapra (szintaxisszínekkel együtt).

**5. Kedvencek használata**

- ⭐ Mentés → aktuális képlet mentése (Ctrl+S)

- 📂 Betöltés → képlet újrafelhasználása

- ❌ Törlés → Del billentyű vagy gomb

- 🕐 Előzmények → legutóbb használt képletek

## 📊 Fülek áttekintése

**1. fül – Alapfunkciók** `+` `-` `\*` `/` `^` SUM, AVERAGE, MIN, MAX, MEDIAN, COUNT, COUNTA, SUMPRODUCT

**2. fül – Speciális funkciók** IF, AND, OR, NOT SUMIF, COUNTIF, AVERAGEIF, SUMIFS, STDEV, VAR, COUNTBLANK, LARGE

**3. fül – Dátum és szöveg** TODAY, NOW, YEAR, MONTH, DAY, DATE, DATEDIF, WEEKDAY CONCATENATE, LEN, LEFT, RIGHT, MID, UPPER, LOWER, TRIM

**4. fül – Keresés és kerekítés** VLOOKUP, HLOOKUP, INDEX, MATCH, INDEX+MATCH ROUND, ROUNDUP, ROUNDDOWN, INT, TRUNC, ABS, MOD, SQRT, RAND


## 📖 Képletmagyarázatok a LibreOffice dokumentációból

A `formula_explanations.json` fájl közvetlenül a **LibreOffice Calc hivatalos dokumentációjából** töltődik fel (https://help.libreoffice.org).

### Adatforrás és frissítés

- A leírások, szintaxisadatok és példák a LibreOffice hivatalos súgóoldaláról kerülnek be
- A támogatott nyelvek az oldalon elérhető fordításoktól függenek
- A fájl minden függvényhez tartalmaz: nevet, szintaxist, leírást, példát és kategóriát
- Kiegészítések vagy javítások manuálisan elvégezhetők (lásd JSON-érvényesítő)

### A `formula_explanations.json` szerkezete

```json
{
  "SUM": {
    "hu": {
      "syntax": "SUM(Szám1; Szám2; ...)",
      "description": "Összeadja a cellatartomány összes számát.",
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

| Mező | Kötelező | Leírás |
|------|---------|--------|
| `syntax` | ✅ | Képletszintaxis paraméterekkel |
| `description` | ✅ | A függvény rövid leírása |
| `example` | ✅ | Felhasználási példa kész képletként |
| `note` | ❌ | Opcionális megjegyzés |

> 💡 **Megjegyzés:** Ha egy nyelvhez nincs bejegyzés, az alkalmazás automatikusan az angol verzióra vált vissza.

---

## 🔍 JSON-érvényesítő nyelvfájlokhoz

Az integrált **JSON-érvényesítő** ellenőrzi és javítja a `languages.json` és `formula_explanations.json` fájlokat a konzisztencia, teljesség és helyes országmegnevezések szempontjából.

Elérhető: **Beállítások → 🔍 JSON-érvényesítő**.

### Mit ellenőriz?

#### `languages.json`

- ✅ Mind a 38 nyelv szerepel (ISO 639-1 nyelvi kód szerint)
- ✅ Helyes **ország- és nyelvmegnevezések** (pl. `"hu"` → `"Magyar"`)
- ✅ Nincs duplikált nyelvkód
- ✅ Kötelező mezők megvannak: `name`, `native_name`, `flag`, `rtl`
- ✅ RTL jelző megfelelően van beállítva (Arab, Héber, Perzsa, Urdu → `"rtl": true`)

#### `formula_explanations.json`

- ✅ Mind a 4 fül összes függvénye rögzítve
- ✅ Kötelező mezők megvannak: `syntax`, `description`, `example`
- ✅ Nincs üres mező (`""` vagy `null`)
- ✅ Nyelvkódok megfelelnek a `languages.json` fájlnak

### Javítási funkciók

| Hibatípus | Automatikus javítás |
|-----------|---------------------|
| Hibás országnév | ISO-szabvány szerinti helyes névvel helyettesítve |
| Hiányzó nyelvbejegyzés | Angol tartalékkal kitöltve |
| Üres kötelező mező | `"[MISSING]"`-ként jelölve manuális ellenőrzéshez |
| Duplikált bejegyzés | Duplikátumok eltávolítva, teljesebb bejegyzés megtartva |
| Hibás RTL jelző | Automatikusan javítva ismert RTL kódok alapján |

### Használat

1. Nyissa meg a **Beállítások → 🔍 JSON-érvényesítő** menüpontot
2. Válasszon fájlt: `languages.json` vagy `formula_explanations.json` (vagy mindkettő)
3. **🔎 Ellenőrzés** – megjeleníti az összes talált problémát
4. **🛠 Automatikus javítás** – megoldja az összes automatikusan javítható hibát
5. **💾 Mentés** – atomikusan visszaírja a javított fájlt
6. **📋 Jelentés exportálása** (opcionális) – szövegfájlba menti az összes találatot

> ⚠️ **Megjegyzés:** Minden automatikus javítás előtt biztonsági másolat készül az eredeti fájlról (`languages.json.bak` / `formula_explanations.json.bak`).

## ⭐ Kedvencek rendszer

- Saját képletek mentése és újrafelhasználása

- Személyes és csapat kedvencek elkülönítve

- A csapat kedvencei csak olvashatók (csak az adminisztrátor szerkesztheti)

- Ismétlődő bejegyzések megakadályozva

- Személyes kedvencek szabad rendezése

- Szinkronizálás hálózati meghajtón keresztül (opcionálisan konfigurálható)

### Csapatsszinkronizálás

A **Beállítások → 🌐 Hálózati elérési út** menüponton keresztül megadható egy hálózati meghajtó (pl. `\\\\Szerver\\Megosztás\\keplet`).

- Indításkor: a hálózati kedvencek helyben kerülnek mentésre (offline tartalék)

- Mentéskor: a saját képletek a hálózatra kerülnek, a csapatképletek érintetlenek maradnak

## 🛠 Adminisztrációs panel

A 🛠 gombon keresztül érhető el. Az első kattintáskor jelszó kerül beállításra (PBKDF2-SHA256, csak a hash kerül mentésre).

- Csapatképletek hozzáadása, szerkesztése és törlése

- Jelszó módosítása

- A módosítások közvetlenül a hálózati meghajtóra kerülnek

## 🔌 Bővítménykezelő

A bővítménykezelő (`plugin_manager.py`) egy önálló eszköz saját képletbővítmények létrehozásához és kezeléséhez a Calc2 számára. Ugyanabban a mappában található, mint a `Calc2.py`, és a 🔌 gombbal indítható a Calc2.py-ból:

### Funkciók

- **Új bővítmény létrehozása** – lépésenkénti varázsló (név, képletek, fordítások, összefoglaló)

- **Képletek hozzáadása** – képletek kiegészítése egy meglévő bővítményhez

- **Fordítások szerkesztése** – képletnevek lefordítása mind a 38 nyelvre

- **Bővítménymappa megnyitása** – közvetlenül a fájlkezelőben

- **Bővítmény törlése** – biztonsági megerősítéssel

### Bővítmény szerkezete

Minden bővítmény almappaként található a `plugins/` könyvtárban, és két fájlból áll:

```
plugins/
  sajat_bovitmeny/
    plugin.json      ← metaadatok (név, verzió, szerző, leírás)
    formulas.json    ← képletek fordításokkal
```

**Példa `plugin.json`:**

```
{
  "id": "sajat_bovitmeny",
  "enabled": true,
  "version": "1.0",
  "author": "Az Ön Neve",
  "icon": "💰",
  "name": { "en": "Finance Formulas", "hu": "Pénzügyi képletek" },
  "description": { "en": "Useful formulas for financial calculations." }
}
```

**Példa `formulas.json`:**

```
[
  {
    "formula": "=SUM(A1:A10)",
    "name": { "en": "Sum of range", "hu": "Tartomány összege" },
    "description": { "en": "Adds all values in A1:A10." },
    "category": { "en": "Basic", "hu": "Alap" }
  }
]
```

### Fontos figyelmeztetés (⚠️ Important Notice)

A bővítménykezelőben található egy **⚠️ Important Notice** gomb. Kattintásra megnyílik egy ablak, amely angolul tartalmazza a bővítmények helyes létrehozásának összes szabályát. Ugyanezek az információk az `IMPORTANT_NOTICE.md` fájlban is megtalálhatók.

## 🌐 Többnyelvűség

38 nyelv érhető el, közvetlenül az alkalmazásban váltható.
Új nyelvek adhatók hozzá a 🌍 gombon keresztül a Nyelvavarázslóval.

**Megjegyzés a hindiről (हिंदी):** A hindire való első váltáskor a *Noto Sans Devanagari* betűtípus egyszeri alkalommal, rendszerszinten kerül telepítésre. A Windows rendszergazdai jogosultságot kér.

## 🔤 RTL támogatás (jobbról balra)

A jobbról balra írott nyelvek automatikusan felismerésre kerülnek, és a teljes felület tükrözésre kerül:

- **Arab (عربي)** – automatikus RTL felismerés
- **Héber (עברית)** – automatikus RTL felismerés
- **Perzsa / Fárszi (فارسی)** – automatikus RTL felismerés
- **Urdu (اردو)** – automatikus RTL felismerés

**Mi változik RTL módban:** A teljes UI-elrendezés tükröződik, a beviteli mezők RTL igazítást használnak, a betűtípus automatikusan RTL-kompatibilisre vált (pl. *Noto Sans Arabic*, *Noto Sans Hebrew*).

> 💡 **Megjegyzés:** A generált LibreOffice-képletek mindig LTR szintaxisban maradnak – csak a felhasználói felület változtatja irányát.


## 🗄️ Biztonsági mentés és visszaállítás

### Biztonsági mentés létrehozása

A **Beállítások → 🗄️ Biztonsági mentés létrehozása** menüponton keresztül:

1. **Név** – szabadon választott elnevezés (pl. `Mentes_Majus_2025`)
2. **Jelszó** – a mentés AES-titkosítással készül; nélküle nem állítható vissza
3. **Mentési hely** – helyi vagy hálózati meghajtó
4. Kattintson a **💾 Biztonsági mentés létrehozása** gombra – `.calc2backup` fájl jön létre

**Tartalom:** Összes kedvenc, beállítások, csapat kedvencek (opcionális), telepített bővítmények.

### Biztonsági mentés visszaállítása

A **Beállítások → 📂 Biztonsági mentés visszaállítása** menüponton keresztül:

1. Válassza ki a fájlt (`.calc2backup`)
2. Adja meg a jelszót
3. Válassza ki a visszaállítási hatókört: csak kedvencek / csak beállítások / minden
4. Kattintson a **🔄 Visszaállítás** gombra

> ⚠️ Visszaállításkor a meglévő adatok felülírásra kerülnek. A visszaállítás előtt a program automatikus mentést ajánl fel az aktuális adatokról.


## 💡 Tippek

- `$A$1` → abszolút hivatkozás (legördülő menü a cellmezők mellett)

- **Ctrl+S** → képlet mentése a kedvencek közé

- **Ctrl+C** → képlet másolása (beviteli mezőkön kívül)

- **Ctrl+Z / Ctrl+Y** → Visszavonás / Újra

- **Ctrl+F12** → ablak kis méretbe helyezése/visszaállítása (akkor is működik, ha a Calc2 kis méretben van)

- **Del billentyű** a kedvencek listájában → bejegyzés törlése

- A képletek generálás után közvetlenül szerkeszthetők a kimeneti mezőben

## 📁 Projektstruktúra

```
Calc2.py                        ← főprogram
plugin_manager.py               ← bővítménykezelő
IMPORTANT_NOTICE.md             ← útmutató a bővítmények létrehozásához
data/
  README_hu.md / README_en.md / ...      ← súgó nyelvenként
  HIVATKOZAS_hu.md / HIVATKOZAS_en.md / ... ← funkcióhivatkozás nyelvenként
language/
  languages.json                ← felhasználói felület fordításai (38 nyelv)
  formula_explanations.json
services/
  language_tool.py              ← varázsló: új nyelv hozzáadása
  settings_service.py
  auth_service.py
  favorites_service.py
  network_sync.py
  install_service.py
  backup_service.py             ← biztonsági mentés és visszaállítás
  json_validator.py             ← languages.json / formula_explanations.json ellenőrzése és javítása
plugins/                        ← bővítménymappa (automatikusan létrehozva)
  sajat_bovitmeny/
    plugin.json
    formulas.json
fonts/
  NotoSansDevanagari-Regular.ttf  ← hindi betűtípus
  NotoSansArabic-Regular.ttf      ← arab betűtípus (RTL)
  NotoSansHebrew-Regular.ttf      ← héber betűtípus (RTL)
python/                         ← beágyazott Python
  python.exe
  ...
settings.json                   ← automatikusan létrehozva
kedvencek.json                  ← helyi kedvencek (automatikusan létrehozva)
```

## 🧠 Technikai kiemelések

- **Atomi fájlírás** → megakadályozza a fájlok sérülését mentés közben

- **Szolgáltatás-architektúra** → a logika és a felhasználói felület szigorúan elkülönítve

- **Automatikus migráció** → a régi kedvencformátumok felismerésre és konvertálásra kerülnek

- **Robusztus hibakezelés** → a hibás fájlok nem okozzák az alkalmazás összeomlását

- **Szintaxiskiemelés** → a képletek színesen jelennek meg

- **Sötét mód** → teljes mértékben támogatott

- **Bővítményrendszer** → a Calc2 saját képletbővítményekkel bővíthető

- **RTL motor** → RTL nyelvek automatikus felismerése, teljes UI-tükrözés megfelelő betűtípusokkal

- **Biztonsági mentés és visszaállítás** → AES-titkosított mentések névvel és jelszóval, szelektív visszaállítás

- **JSON-érvényesítő** → `languages.json` és `formula_explanations.json` automatikus ellenőrzése és javítása, beleértve az országneveket és a kötelező mezőket

- **LibreOffice-forrás** → a `formula_explanations.json` a LibreOffice Calc hivatalos dokumentációjából töltődik fel (https://help.libreoffice.org)

- **Globális gyorsbillentyű** → a `Ctrl+F12` rendszerszinten működik a `keyboard` könyvtáron keresztül (háttérszál)

## Licenc

Személyes és kereskedelmi célokra szabadon felhasználható.
