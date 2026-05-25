# LibreOffice Calc Pomocník vzorcov

Nástroj v Pythone na rýchle vytváranie, testovanie a správu vzorcov LibreOffice Calc – so systémom obľúbených položiek, synchronizáciou tímu, viacjazyčnosťou a správcom doplnkov.

## 🚀 Funkcie

- 📑 4 karty s viac ako 60 funkciami

- 🌐 38 jazykov (vrátane hindčiny s automatickou inštaláciou písma)

- ⭐ Systém obľúbených položiek (lokálne a synchronizácia tímu cez sieťovú jednotku)

- 🛠 Správcovský panel pre obľúbené tímu (chránený heslom)

- 📋 Vzorce pripravené na skopírovanie so zvýrazňovaním syntaxe

- ✏️ Upraviteľné výstupné pole s vrátením/opakovaním zmien

- 📖 Integrovaná pomocníka a referencia funkcií (pre každý jazyk)

- 💾 Automatické ukladanie (JSON, atomický zápis)

- 🌙 Tmavý režim

- 🔌 Správca doplnkov na vytváranie vlastných doplnkov vzorcov

- 🔤 Podpora RTL (sprava doľava) – automatické rozpoznanie smeru písania

- 🗄️ Zálohovanie a obnova – uložte všetky nastavenia a obľúbené položky s názvom a heslom

- ⌨️ Globálna klávesová skratka `Ctrl+F12` na minimalizovanie/obnovenie okna
- 🔍 Validátor JSON – automatická kontrola a oprava `languages.json` a `formula_explanations.json`

## 🖥️ Používanie

**1. Zadanie vstupov**

- Rozsah buniek (napr. `A1:A10`)

- Bunka 1 / Bunka 2 (napr. `A1`, `B1`)

- Voliteľný parameter (napr. text alebo index)

- Výber režimu absolútneho odkazu: `A1`, `$A1`, `A$1`, `$A$1`

**2. Výber funkcie** Vyberte kartu a kliknite na funkciu – vzorec sa okamžite vygeneruje.

**3. Úprava vzorca** Vygenerovaný vzorec možno upravovať priamo vo výstupnom poli.

**4. Kopírovanie** Preneste do schránky jedným kliknutím (vrátane farieb syntaxe).

**5. Používanie obľúbených položiek**

- ⭐ Uložiť → uložiť aktuálny vzorec (Ctrl+S)

- 📂 Načítať → znovu použiť vzorec

- ❌ Odstrániť → kláves Delete alebo tlačidlo

- 🕐 História → naposledy použité vzorce

## 📊 Prehľad kariet

**Karta 1 – Základné funkcie** `+` `-` `*` `/` `^` SUM, AVERAGE, MIN, MAX, MEDIAN, COUNT, COUNTA, SUMPRODUCT

**Karta 2 – Pokročilé funkcie** IF, AND, OR, NOT SUMIF, COUNTIF, AVERAGEIF, SUMIFS, STDEV, VAR, COUNTBLANK, LARGE

**Karta 3 – Dátum a text** TODAY, NOW, YEAR, MONTH, DAY, DATE, DATEDIF, WEEKDAY CONCATENATE, LEN, LEFT, RIGHT, MID, UPPER, LOWER, TRIM

**Karta 4 – Vyhľadávanie a zaokrúhľovanie** VLOOKUP, HLOOKUP, INDEX, MATCH, INDEX+MATCH ROUND, ROUNDUP, ROUNDDOWN, INT, TRUNC, ABS, MOD, SQRT, RAND


## 📖 Vysvetlenia vzorcov z dokumentácie LibreOffice

Súbor `formula_explanations.json` sa vypĺňa priamo z **oficiálnej dokumentácie LibreOffice Calc** (https://help.libreoffice.org).

### Zdroj údajov a aktualizácia

- Popisy, informácie o syntaxi a príklady sa preberajú z oficiálnej webovej stránky pomoci LibreOffice
- Podporované jazyky závisia od prekladov dostupných na stránke
- Súbor obsahuje pre každú funkciu: názov, syntax, popis, príklad a kategóriu
- Doplnenia alebo opravy je možné vykonať ručne (pozri Validátor JSON)

### Štruktúra `formula_explanations.json`

```json
{
  "SUM": {
    "sk": {
      "syntax": "SUM(Číslo1; Číslo2; ...)",
      "description": "Sčíta všetky čísla v rozsahu buniek.",
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

| Pole | Povinné | Popis |
|------|---------|-------|
| `syntax` | ✅ | Syntax vzorca s parametrami |
| `description` | ✅ | Stručný popis funkcie |
| `example` | ✅ | Príklad použitia ako hotový vzorec |
| `note` | ❌ | Voliteľná poznámka |

> 💡 **Poznámka:** Ak pre jazyk neexistuje záznam, aplikácia sa automaticky vráti k anglickej verzii.

---

## 🔍 Validátor JSON pre jazykové súbory

Integrovaný **Validátor JSON** kontroluje a opravuje `languages.json` a `formula_explanations.json` z hľadiska konzistencie, úplnosti a správnych názvov krajín. Prístupný cez **Nastavenia → 🔍 Validátor JSON**.

### Čo sa kontroluje?

#### `languages.json`

- ✅ Všetkých 38 jazykov je prítomných (podľa kódu ISO 639-1)
- ✅ Správne **názvy krajín a jazykov** (napr. `"sk"` → `"Slovenčina"`)
- ✅ Žiadne duplicitné jazykové kódy
- ✅ Povinné polia sú prítomné: `name`, `native_name`, `flag`, `rtl`
- ✅ RTL príznak správne nastavený (Arabčina, Hebrejčina, Perzština, Urdčina → `"rtl": true`)

#### `formula_explanations.json`

- ✅ Všetky funkcie zo 4 kariet zaznamenané
- ✅ Povinné polia sú prítomné: `syntax`, `description`, `example`
- ✅ Žiadne prázdne polia (`""` alebo `null`)
- ✅ Jazykové kódy zodpovedajú `languages.json`

### Funkcie opravy

| Typ chyby | Automatická oprava |
|-----------|-------------------|
| Nesprávny názov krajiny | Nahradený správnym názvom podľa ISO |
| Chýbajúci jazykový záznam | Doplnený anglickou záložnou verziou |
| Prázdne povinné pole | Označené ako `"[MISSING]"` na ručnú kontrolu |
| Duplicitný záznam | Duplicity odstránené, úplnejší záznam zachovaný |
| Nesprávny RTL príznak | Automaticky opravený na základe známych RTL kódov |

### Postup používania

1. Otvorte **Nastavenia → 🔍 Validátor JSON**
2. Vyberte súbor: `languages.json` alebo `formula_explanations.json` (alebo oba)
3. **🔎 Kontrolovať** – zobrazí všetky nájdené problémy
4. **🛠 Automaticky opraviť** – opraví všetky automaticky riešiteľné chyby
5. **💾 Uložiť** – atomicky zapíše opravený súbor
6. **📋 Exportovať správu** (voliteľné) – uloží textový súbor so všetkými zisteniami

> ⚠️ **Poznámka:** Pred každou automatickou opravou sa vytvorí záložná kópia pôvodného súboru (`languages.json.bak` / `formula_explanations.json.bak`).

## ⭐ Systém obľúbených položiek

- Ukladanie a opätovné používanie vlastných vzorcov

- Rozlíšenie medzi vlastnými obľúbenými a obľúbenými tímu

- Obľúbené tímu sú chránené pred zápisom (upravovať ich môže iba správca)

- Zamedzenie duplicitných záznamov

- Voľné zoradenie vlastných obľúbených položiek

- Synchronizácia cez sieťovú jednotku (voliteľne konfigurovateľná)

### Synchronizácia tímu

V časti **Nastavenia → 🌐 Sieťová cesta** možno zadať sieťovú jednotku (napr. `\\\\Server\\Zdieľané\\vzorce`).

- Pri spustení: obľúbené zo siete sa uložia lokálne (záložná kópia pre prácu offline)

- Pri ukladaní: vlastné vzorce sa zapíšu do siete, vzorce tímu zostanú nezmenené

## 🛠 Správcovský panel

Prístupný cez tlačidlo 🛠. Pri prvom kliknutí sa nastaví heslo (PBKDF2-SHA256, ukladá sa iba hash).

- Pridávanie, upravovanie a odstraňovanie vzorcov tímu

- Zmena hesla

- Zápis zmien priamo na sieťovú jednotku

## 🔌 Správca doplnkov

Správca doplnkov (`plugin_manager.py`) je samostatný nástroj na vytváranie a správu vlastných doplnkov vzorcov pre Calc2. Nachádza sa v rovnakom priečinku ako `Calc2.py` a spúšťa sa tlačidlom 🔌 v Calc2.py:

### Funkcie

- **Vytvoriť nový doplnok** – sprievodca krok za krokom (názov, vzorce, preklady, zhrnutie)

- **Pridať vzorce** – pridanie vzorcov do existujúceho doplnku

- **Upraviť preklady** – preklad názvov vzorcov do všetkých 38 jazykov

- **Otvoriť priečinok doplnkov** – priamo v správcovi súborov

- **Odstrániť doplnok** – s potvrdením bezpečnostnou otázkou

### Štruktúra doplnku

Každý doplnok sa nachádza ako podpriečinok v `plugins/` a pozostáva z dvoch súborov:

```
plugins/
  moj_dodatok/
    plugin.json      ← metadáta (názov, verzia, autor, popis)
    formulas.json    ← vzorce s prekladmi
```

**Príklad `plugin.json`:**

```
{
  "id": "moj_dodatok",
  "enabled": true,
  "version": "1.0",
  "author": "Vaše meno",
  "icon": "💰",
  "name": { "en": "Finance Formulas", "sk": "Finančné vzorce" },
  "description": { "en": "Useful formulas for financial calculations." }
}
```

**Príklad `formulas.json`:**

```
[
  {
    "formula": "=SUM(A1:A10)",
    "name": { "en": "Sum of range", "sk": "Súčet rozsahu" },
    "description": { "en": "Adds all values in A1:A10." },
    "category": { "en": "Basic", "sk": "Základné" }
  }
]
```

### Dôležité upozornenie (⚠️ Important Notice)

V správcovi doplnkov sa nachádza tlačidlo **⚠️ Important Notice**. Kliknutím sa otvorí okno so všetkými pravidlami pre správne vytváranie doplnkov v angličtine. Rovnaké informácie sú dostupné aj v súbore `IMPORTANT_NOTICE.md`.

## 🌐 Viacjazyčnosť

K dispozícii je 38 jazykov, prepínateľných priamo v aplikácii.  
Nové jazyky možno pridať cez tlačidlo 🌍 pomocou Sprievodcu jazykmi.

**Poznámka k hindčine (हिंदी):** Pri prvom prepnutí na hindčinu sa písmo *Noto Sans Devanagari* jednorazovo nainštaluje na úrovni systému. Systém Windows pri tom požiada o práva správcu.

## 🔤 Podpora RTL (sprava doľava)

Jazyky s písmom sprava doľava sú automaticky rozpoznané a celé rozhranie sa zrkadlí:

- **Arabčina (عربي)** – automatické rozpoznanie RTL
- **Hebrejčina (עברית)** – automatické rozpoznanie RTL
- **Perzština / Farsí (فارسی)** – automatické rozpoznanie RTL
- **Urdčina (اردو)** – automatické rozpoznanie RTL

**Čo sa mení v režime RTL:** Celé rozloženie UI sa zrkadlí, vstupné polia používajú RTL zarovnanie, písmo sa automaticky prepne na RTL-kompatibilné (napr. *Noto Sans Arabic*, *Noto Sans Hebrew*).

> 💡 **Poznámka:** Vygenerované vzorce LibreOffice zostávajú vždy v LTR syntaxi – mení sa len smer rozhrania.


## 🗄️ Zálohovanie a obnova

### Vytvorenie zálohy

Cez **Nastavenia → 🗄️ Vytvoriť zálohu**:

1. **Názov** – ľubovoľný popis (napr. `Zaloha_Maj_2025`)
2. **Heslo** – záloha je šifrovaná AES; bez neho obnova nie je možná
3. **Miesto uloženia** – lokálne alebo sieťová jednotka
4. Kliknite na **💾 Vytvoriť zálohu** – vytvorí sa súbor `.calc2backup`

**Obsah:** Všetky obľúbené, nastavenia, obľúbené tímu (voliteľné), nainštalované doplnky.

### Obnovenie zálohy

Cez **Nastavenia → 📂 Obnoviť zálohu**:

1. Vyberte súbor (`.calc2backup`)
2. Zadajte heslo
3. Vyberte rozsah: len obľúbené / len nastavenia / všetko
4. Kliknite na **🔄 Obnoviť**

> ⚠️ Pri obnove sa existujúce údaje prepíšu. Pred obnovením sa ponúkne automatická záloha aktuálnych údajov.


## 💡 Tipy

- `$A$1` → absolútny odkaz (rozbaľovací zoznam vedľa polí buniek)

- **Ctrl+S** → uložiť vzorec do obľúbených

- **Ctrl+C** → kopírovať vzorec (mimo vstupných polí)

- **Ctrl+Z / Ctrl+Y** → vrátiť späť / zopakovať

- **Ctrl+F12** → minimalizovať / obnoviť okno (funguje aj keď je Calc2 minimalizovaný)

- **Kláves Delete** v zozname obľúbených → odstrániť záznam

- Vzorce možno upravovať priamo vo výstupnom poli po ich vygenerovaní

## 📁 Štruktúra projektu

```
Calc2.py                        ← hlavný program
plugin_manager.py               ← správca doplnkov
IMPORTANT_NOTICE.md             ← poznámky k vytváraniu doplnkov
data/
  README_de.md / README_en.md / ...      ← pomocník pre každý jazyk
  REFERENZ_de.md / REFERENZ_en.md / ...  ← referencia funkcií pre každý jazyk
language/
  languages.json                ← preklady rozhrania (38 jazykov)
  formula_explanations.json
services/
  language_tool.py              ← sprievodca: pridanie nového jazyka
  settings_service.py
  auth_service.py
  favorites_service.py
  network_sync.py
  install_service.py
  backup_service.py             ← zálohovanie a obnova
  json_validator.py             ← kontrola a oprava languages.json / formula_explanations.json
plugins/                        ← priečinok doplnkov (vytvorí sa automaticky)
  moj_dodatok/
    plugin.json
    formulas.json
fonts/
  NotoSansDevanagari-Regular.ttf  ← písmo hindčiny
  NotoSansArabic-Regular.ttf      ← arabské písmo (RTL)
  NotoSansHebrew-Regular.ttf      ← hebrejské písmo (RTL)
python/                         ← vstavaný Python
  python.exe
  ...
settings.json                   ← vytvorí sa automaticky
oblubene.json                   ← lokálne obľúbené (vytvorí sa automaticky)
```

## 🧠 Technické prednosti

- **Atomický zápis súborov** → zabraňuje poškodeniu súborov pri ukladaní

- **Servisná architektúra** → logika a používateľské rozhranie sú striktne oddelené

- **Automatická migrácia** → staré formáty obľúbených sú rozpoznané a konvertované

- **Spoľahlivé spracovanie chýb** → poškodené súbory nespôsobia pád aplikácie

- **Zvýrazňovanie syntaxe** → vzorce sú zobrazené farebne

- **Tmavý režim** → plná podpora

- **Systém doplnkov** → Calc2 možno rozšíriť vlastnými doplnkami vzorcov

- **Motor RTL** → automatické rozpoznanie RTL jazykov, úplné zrkadlenie UI s príslušnými písmami

- **Zálohovanie a obnova** → zálohy šifrované AES s názvom a heslom, selektívna obnova

- **Validátor JSON** → automatická kontrola a oprava `languages.json` a `formula_explanations.json` vrátane názvov krajín a povinných polí

- **Zdroj LibreOffice** → `formula_explanations.json` sa vypĺňa z oficiálnej dokumentácie LibreOffice Calc (https://help.libreoffice.org)

- **Globálna klávesová skratka** → `Ctrl+F12` funguje na úrovni systému prostredníctvom knižnice `keyboard` (vlákno na pozadí)

## Licencia

Voľne použiteľné na osobné aj komerčné účely.
