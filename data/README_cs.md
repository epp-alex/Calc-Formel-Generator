# LibreOffice Calc Pomocník pro vzorce

Pythonový nástroj pro rychlé vytváření, testování a správu vzorců v LibreOffice Calc – se systémem oblíbených, týmovou synchronizací, vícejazyčnou podporou a správcem zásuvných modulů.

## 🚀 Funkce

- 📑 4 záložky s více než 60 funkcemi

- 🌐 38 jazyků (vč. hindštiny s automatickou instalací písma)

- ⭐ Systém oblíbených (lokálně i týmová synchronizace přes síťové úložiště)

- 🛠 Administrátorský panel pro týmové oblíbené (chráněný heslem)

- 📋 Vzorce připravené ke vložení se zvýrazněním syntaxe

- ✏️ Upravitelné výstupní pole s funkcí undo/redo

- 📖 Integrovaná nápověda a přehled funkcí (pro každý jazyk)

- 💾 Automatické ukládání (JSON, atomický zápis)

- 🌙 Tmavý režim

- 🔌 Správce zásuvných modulů pro vytváření vlastních modulů se vzorci

- 🔤 Podpora RTL (zprava doleva) – automatické rozpoznání směru písma

- 🗄️ Zálohování a obnovení – uložení všech nastavení a oblíbených s názvem a heslem

- ⌨️ Globální klávesová zkratka `Ctrl+F12` pro minimalizaci/obnovení okna
- 🔍 Validátor JSON – automatická kontrola a oprava `languages.json` a `formula_explanations.json`

## 🖥️ Použití

**1. Zadejte hodnoty**

- Rozsah buněk (např. `A1:A10`)

- Buňka 1 / Buňka 2 (např. `A1`, `B1`)

- Volitelný parametr (např. text nebo index)

- Volitelný režim reference: `A1`, `$A1`, `A$1`, `$A$1`

**2. Vyberte funkci** Zvolte záložku a klikněte na funkci – vzorec se vygeneruje okamžitě.

**3. Upravte vzorec** Vygenerovaný vzorec lze přímo upravit ve výstupním poli.

**4. Zkopírujte** Zkopírujte do schránky jediným kliknutím (vč. barev syntaxe).

**5. Používejte oblíbené**

- ⭐ Uložit → uložení aktuálního vzorce (Ctrl+S)

- 📂 Načíst → opětovné použití uloženého vzorce

- ❌ Smazat → klávesa Delete nebo tlačítko

- 🕐 Historie → naposledy použité vzorce

## 📊 Přehled záložek

**Záložka 1 – Základní funkce** `+` `-` `\*` `/` `^` SUM, AVERAGE, MIN, MAX, MEDIAN, COUNT, COUNTA, SUMPRODUCT

**Záložka 2 – Pokročilé funkce** IF, AND, OR, NOT SUMIF, COUNTIF, AVERAGEIF, SUMIFS, STDEV, VAR, COUNTBLANK, LARGE

**Záložka 3 – Datum a text** TODAY, NOW, YEAR, MONTH, DAY, DATE, DATEDIF, WEEKDAY CONCATENATE, LEN, LEFT, RIGHT, MID, UPPER, LOWER, TRIM

**Záložka 4 – Vyhledávání a zaokrouhlování** VLOOKUP, HLOOKUP, INDEX, MATCH, INDEX+MATCH ROUND, ROUNDUP, ROUNDDOWN, INT, TRUNC, ABS, MOD, SQRT, RAND


## 📖 Vysvětlení vzorců z dokumentace LibreOffice

Soubor `formula_explanations.json` je plněn přímo z oficiální **dokumentace LibreOffice Calc** (https://help.libreoffice.org).

### Zdroj dat a aktualizace

- Popisy, syntaktické informace a příklady jsou přebírány z oficiálního webu nápovědy LibreOffice
- Podporované jazyky závisí na překladech dostupných na webu
- Soubor obsahuje pro každou funkci: název, syntaxi, popis, příklad a kategorii
- Doplnění nebo opravy lze provést ručně (viz Validátor JSON)

### Struktura `formula_explanations.json`

```json
{
  "SUM": {
    "cs": {
      "syntax": "SUM(Číslo1; Číslo2; ...)",
      "description": "Sečte všechna čísla v rozsahu buněk.",
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
| `syntax` | ✅ | Syntaxe vzorce s parametry |
| `description` | ✅ | Stručný popis funkce |
| `example` | ✅ | Příklad použití jako hotový vzorec |
| `note` | ❌ | Volitelná poznámka |

> 💡 **Poznámka:** Pokud pro daný jazyk není žádný záznam, aplikace automaticky přejde na anglickou verzi.

---

## 🔍 Validátor JSON pro jazykové soubory

Integrovaný **validátor JSON** kontroluje a opravuje `languages.json` i `formula_explanations.json` z hlediska konzistence, úplnosti a správnosti názvů zemí. Přístupný přes **Nastavení → 🔍 Validátor JSON**.

### Co se kontroluje?

#### `languages.json`

- ✅ Všech 38 jazyků je přítomno (podle kódu ISO 639-1)
- ✅ Správné **názvy zemí a jazyků** (např. `"cs"` → `"Čeština"`)
- ✅ Žádné duplicitní jazykové kódy
- ✅ Povinná pole jsou přítomna: `name`, `native_name`, `flag`, `rtl`
- ✅ RTL označení je správně nastaveno (Arabština, Hebrejština, Perština, Urdština → `"rtl": true`)

#### `formula_explanations.json`

- ✅ Všechny funkce ze 4 záložek jsou zapsány
- ✅ Povinná pole jsou přítomna: `syntax`, `description`, `example`
- ✅ Žádná prázdná pole (`""` nebo `null`)
- ✅ Jazykové kódy odpovídají `languages.json`

### Funkce oprav

| Typ chyby | Automatická oprava |
|-----------|-------------------|
| Nesprávný název země | Nahrazen správným názvem podle ISO standardu |
| Chybějící jazykový záznam | Doplněn anglickou záložní verzí |
| Prázdné povinné pole | Označeno jako `"[MISSING]"` k ruční kontrole |
| Duplicitní záznam | Duplicity odstraněny, ponechán úplnější záznam |
| Nesprávný RTL příznak | Automaticky opraven podle známých RTL kódů |

### Postup práce

1. Otevřete **Nastavení → 🔍 Validátor JSON**
2. Vyberte soubor: `languages.json` nebo `formula_explanations.json` (nebo oba)
3. **🔎 Zkontrolovat** – zobrazí všechny nalezené problémy
4. **🛠 Automaticky opravit** – opraví všechny automaticky řešitelné chyby
5. **💾 Uložit** – atomicky zapíše opravený soubor
6. **📋 Exportovat zprávu** (volitelně) – uloží textový soubor se všemi nálezy

> ⚠️ **Poznámka:** Před každou automatickou opravou je vytvořena záloha původního souboru (`languages.json.bak` / `formula_explanations.json.bak`).

## ⭐ Systém oblíbených

- Ukládejte a opakovaně používejte vlastní vzorce

- Jasné oddělení osobních a týmových oblíbených

- Týmové oblíbené jsou pouze pro čtení (upravovat je může jen administrátor)

- Duplicitní záznamy jsou automaticky zamezeny

- Volné řazení osobních oblíbených

- Synchronizace přes síťové úložiště (volitelně konfigurovatelné)

### Týmová synchronizace

V **Nastavení → 🌐 Síťová cesta** lze zadat cestu k síťovému úložišti (např. `\\\\Server\\Share\\formulas`).

- Při spuštění: síťové oblíbené se uloží lokálně do mezipaměti (záložní offline režim)

- Při ukládání: vlastní vzorce se zapíší do sítě; týmové vzorce zůstanou nedotčeny

## 🛠 Administrátorský panel

Přístupný přes tlačítko 🛠. Při prvním kliknutí se nastaví heslo (PBKDF2-SHA256, ukládá se pouze hash).

- Přidávání, úprava a mazání týmových vzorců

- Změna hesla

- Přímý zápis změn na síťové úložiště

## 🔌 Správce zásuvných modulů

Správce zásuvných modulů (`plugin_manager.py`) je samostatný nástroj pro vytváření a správu vlastních modulů se vzorci pro Calc2. Nachází se ve stejné složce jako `Calc2.py` a spouští se tlačítkem 🔌 v Calc2.py.

### Funkce

- **Vytvoření nového modulu** – průvodce krok za krokem (název, vzorce, překlady, souhrn)

- **Přidání vzorců** – přidání vzorců do existujícího modulu

- **Úprava překladů** – překlad názvů vzorců do všech 38 jazyků

- **Otevření složky modulu** – přímo v průzkumníku souborů

- **Smazání modulu** – s potvrzovacím dialogem

### Struktura modulu

Každý modul je uložen jako podsložka v `plugins/` a skládá se ze dvou souborů:

```
plugins/
  my_plugin/
    plugin.json      ← metadata (název, verze, autor, popis)
    formulas.json    ← vzorce s překlady
```

**Příklad `plugin.json`:**

```json
{
  "id": "my_plugin",
  "enabled": true,
  "version": "1.0",
  "author": "Vaše jméno",
  "icon": "💰",
  "name": { "en": "Finance Formulas", "cs": "Finanční vzorce" },
  "description": { "en": "Useful formulas for financial calculations." }
}
```

**Příklad `formulas.json`:**

```json
[
  {
    "formula": "=SUM(A1:A10)",
    "name": { "en": "Sum of range", "cs": "Součet rozsahu" },
    "description": { "en": "Adds all values in A1:A10." },
    "category": { "en": "Basic", "cs": "Základní" }
  }
]
```

### Důležitá poznámka (⚠️)

Správce zásuvných modulů obsahuje tlačítko **⚠️ Important Notice**. Po kliknutí se otevře okno se všemi pravidly pro správné vytváření modulů (v angličtině). Stejné informace jsou k dispozici také v souboru `IMPORTANT_NOTICE.md`.

## 🌐 Vícejazyčná podpora

K dispozici je 38 jazyků, přepínatelných přímo v aplikaci.  
Nové jazyky lze přidat tlačítkem 🌍 pomocí průvodce jazyky.

**Poznámka k hindštině (हिंदी):** Při prvním přepnutí na hindštinu se jednorázově nainstaluje systémové písmo *Noto Sans Devanagari*. Systém Windows vyžádá oprávnění správce.

## 🔤 Podpora RTL (zprava doleva)

Jazyky s písmem zprava doleva jsou automaticky rozpoznány a celé rozhraní se zrcadlí:

- **Arabština (عربي)** – automatické rozpoznání RTL
- **Hebrejština (עברית)** – automatické rozpoznání RTL
- **Perština / Fársí (فارسی)** – automatické rozpoznání RTL
- **Urdština (اردو)** – automatické rozpoznání RTL

**Co se při RTL změní:** Celé rozložení UI se zrcadlí, vstupní pole používají RTL zarovnání, písmo se automaticky přepne na RTL kompatibilní (např. *Noto Sans Arabic*, *Noto Sans Hebrew*).

> 💡 **Poznámka:** Generované vzorce LibreOffice zůstávají vždy v syntaxi LTR.


## 🗄️ Zálohování a obnovení

### Vytvoření zálohy

Přes **Nastavení → 🗄️ Vytvořit zálohu**:

1. **Název** – libovolný popis zálohy (např. `Backup_Mai_2025`)
2. **Heslo** – záloha je šifrována AES; bez hesla nelze obnovit
3. **Umístění** – lokální nebo síťové úložiště
4. Klikněte na **💾 Vytvořit zálohu** – vytvoří se soubor `.calc2backup`

**Obsah zálohy:** Všechny oblíbené, nastavení, týmové oblíbené (volitelně), nainstalované moduly.

### Obnovení zálohy

Přes **Nastavení → 📂 Obnovit zálohu**:

1. Vyberte soubor zálohy (`.calc2backup`)
2. Zadejte heslo
3. Zvolte rozsah obnovení: jen oblíbené / jen nastavení / vše
4. Klikněte na **🔄 Obnovit**

> ⚠️ Při obnovení jsou stávající data přepsána. Před obnovením je nabídnuto automatické zálohy aktuálních dat.


## 💡 Tipy

- `$A$1` → absolutní reference (rozbalovací nabídka vedle polí buněk)

- **Ctrl+S** → uložení vzorce do oblíbených

- **Ctrl+C** → kopírování vzorce (pokud není fokus v textovém poli)

- **Ctrl+Z / Ctrl+Y** → zpět / znovu

- **Ctrl+F12** → minimalizace / obnovení okna (funguje i když je Calc2 minimalizován)

- **Klávesa Delete** v seznamu oblíbených → smazání záznamu

- Vzorce lze po vygenerování upravit přímo ve výstupním poli

## 📁 Struktura projektu

```
Calc2.py                        ← hlavní aplikace
plugin_manager.py               ← správce zásuvných modulů
IMPORTANT_NOTICE.md             ← poznámky k vytváření modulů
data/
  README_de.md / README_en.md / ...      ← nápověda pro každý jazyk
  REFERENZ_de.md / REFERENZ_en.md / ...  ← přehled funkcí pro každý jazyk
language/
  languages.json                ← překlady UI (38 jazyků)
  formula_explanations.json
services/
  language_tool.py              ← průvodce: přidání nového jazyka
  settings_service.py
  auth_service.py
  favorites_service.py
  network_sync.py
  install_service.py
  backup_service.py             ← zálohování a obnovení
  json_validator.py             ← kontrola a oprava languages.json / formula_explanations.json
plugins/                        ← složka modulů (vytváří se automaticky)
  my_plugin/
    plugin.json
    formulas.json
fonts/
  NotoSansDevanagari-Regular.ttf  ← písmo pro hindštinu
  NotoSansArabic-Regular.ttf      ← arabské písmo (RTL)
  NotoSansHebrew-Regular.ttf      ← hebrejské písmo (RTL)
python/                         ← vestavěný Python
  python.exe
  ...
settings.json                   ← vytváří se automaticky
favoriten.json                  ← lokální oblíbené (vytváří se automaticky)
```

## 🧠 Technické zajímavosti

- **Atomický zápis souborů** → zabraňuje poškození souborů při ukládání

- **Servisní architektura** → logika a UI jsou striktně odděleny

- **Automatická migrace** → staré formáty oblíbených jsou rozpoznány a převedeny

- **Robustní zpracování chyb** → poškozené soubory nezpůsobí pád aplikace

- **Zvýraznění syntaxe** → vzorce jsou zobrazeny barevně

- **Tmavý režim** → plně podporován

- **Systém zásuvných modulů** → Calc2 lze rozšířit vlastními moduly se vzorci

- **RTL modul** → automatické rozpoznání RTL jazyků, úplné zrcadlení UI včetně odpovídajících písem

- **Zálohování a obnovení** → zálohy šifrované AES s názvem a heslem, selektivní obnovení

- **Validátor JSON** → automatická kontrola a oprava `languages.json` a `formula_explanations.json` vč. názvů zemí a povinných polí

- **Zdroj LibreOffice** → `formula_explanations.json` je plněn z oficiální dokumentace LibreOffice Calc (https://help.libreoffice.org)

- **Globální klávesová zkratka** → `Ctrl+F12` funguje systémově přes knihovnu `keyboard` (vlákno na pozadí)

## Licence

Volně použitelné pro osobní i komerční účely.
