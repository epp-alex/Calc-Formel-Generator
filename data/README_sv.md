# LibreOffice Calc Formelassistent

Ett Python-verktyg för att snabbt skapa, testa och hantera formler i LibreOffice Calc – med ett favoritersystem, teamsynkronisering, flerspråkighet och ett plugin-hanterare.

## 🚀 Funktioner

- 📑 4 flikar med över 60 funktioner

- 🌐 38 språk (inkl. hindi med automatisk teckensnittsinstallation)

- ⭐ Favoritersystem (lokalt och teamsynkronisering via nätverksenhet)

- 🛠 Administratörspanel för teamfavoriter (lösenordsskyddad)

- 📋 Direkt kopieringsbara formler med syntaxmarkering

- ✏️ Redigerbart utdatafält med ångra/gör om

- 📖 Inbyggd hjälp och funktionsreferens (per språk)

- 💾 Automatisk sparning (JSON, atomär skrivning)

- 🌙 Mörkt läge

- 🔌 Plugin-hanterare för att skapa egna formel-plugins

- 🔤 RTL-stöd (höger till vänster) – automatisk igenkänning av skrivriktning

- 🗄️ Säkerhetskopiering och återställning – spara alla inställningar och favoriter med namn och lösenord

- ⌨️ Global kortkommando `Ctrl+F12` för att minimera/återställa fönstret
- 🔍 JSON-validator – automatisk kontroll och rättelse av `languages.json` och `formula_explanations.json`

## 🖥️ Användning

**1. Ange indata**

- Cellområde (t.ex. `A1:A10`)

- Cell 1 / Cell 2 (t.ex. `A1`, `B1`)

- Valfri parameter (t.ex. text eller index)

- Valbart läge för absolut referens: `A1`, `$A1`, `A$1`, `$A$1`

**2. Välj en funktion** Välj en flik och klicka på en funktion – formeln genereras omedelbart.

**3. Anpassa formeln** Den genererade formeln kan redigeras direkt i utdatafältet.

**4. Kopiera** Överför till urklipp med ett klick (inkl. syntaxfärger).

**5. Använd favoriter**

- ⭐ Spara → spara aktuell formel (Ctrl+S)

- 📂 Ladda → återanvänd formel

- ❌ Ta bort → Delete-tangenten eller knappen

- 🕐 Historik → senast använda formler

## 📊 Fliköversikt

**Flik 1 – Grundfunktioner** `+` `-` `*` `/` `^` SUM, AVERAGE, MIN, MAX, MEDIAN, COUNT, COUNTA, SUMPRODUCT

**Flik 2 – Avancerade funktioner** IF, AND, OR, NOT SUMIF, COUNTIF, AVERAGEIF, SUMIFS, STDEV, VAR, COUNTBLANK, LARGE

**Flik 3 – Datum och text** TODAY, NOW, YEAR, MONTH, DAY, DATE, DATEDIF, WEEKDAY CONCATENATE, LEN, LEFT, RIGHT, MID, UPPER, LOWER, TRIM

**Flik 4 – Uppslagning och avrundning** VLOOKUP, HLOOKUP, INDEX, MATCH, INDEX+MATCH ROUND, ROUNDUP, ROUNDDOWN, INT, TRUNC, ABS, MOD, SQRT, RAND


## 📖 Formelförklaringar från LibreOffice-dokumentationen

Filen `formula_explanations.json` fylls direkt från den officiella **LibreOffice Calc-dokumentationen** (https://help.libreoffice.org).

### Datakälla och uppdatering

- Beskrivningar, syntaxinformation och exempel hämtas från LibreOffices officiella hjälpsida
- Stödda språk beror på tillgängliga översättningar på sidan
- Filen innehåller för varje funktion: namn, syntax, beskrivning, exempel och kategori
- Tillägg eller rättelser kan göras manuellt (se JSON-validator)

### Struktur för `formula_explanations.json`

```json
{
  "SUM": {
    "sv": {
      "syntax": "SUM(Tal1; Tal2; ...)",
      "description": "Lägger ihop alla tal i ett cellområde.",
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

| Fält | Obligatoriskt | Beskrivning |
|------|--------------|-------------|
| `syntax` | ✅ | Formelsyntax med parametrar |
| `description` | ✅ | Kort beskrivning av funktionen |
| `example` | ✅ | Användningsexempel som färdig formel |
| `note` | ❌ | Valfri anmärkning |

> 💡 **Obs:** Om det inte finns en post för ett språk återgår appen automatiskt till den engelska versionen.

---

## 🔍 JSON-validator för språkfiler

Den inbyggda **JSON-validatorn** kontrollerar och rättar `languages.json` och `formula_explanations.json` för konsistens, fullständighet och korrekta landsnamn. Nås via **Inställningar → 🔍 JSON-validator**.

### Vad kontrolleras?

#### `languages.json`

- ✅ Alla 38 språk är på plats (efter ISO 639-1 språkkod)
- ✅ Korrekta **lands- och språknamn** (t.ex. `"sv"` → `"Svenska"`)
- ✅ Inga duplicerade språkkoder
- ✅ Obligatoriska fält finns: `name`, `native_name`, `flag`, `rtl`
- ✅ RTL-flagga korrekt inställd (Arabiska, Hebreiska, Persiska, Urdu → `"rtl": true`)

#### `formula_explanations.json`

- ✅ Alla funktioner från de 4 flikarna är registrerade
- ✅ Obligatoriska fält finns: `syntax`, `description`, `example`
- ✅ Inga tomma fält (`""` eller `null`)
- ✅ Språkkoder stämmer med `languages.json`

### Rättelsefunktioner

| Feltyp | Automatisk rättelse |
|--------|---------------------|
| Fel landsnamn | Ersätts med rätt namn enligt ISO |
| Saknad språkpost | Fylls med engelsk reservversion |
| Tomt obligatoriskt fält | Märks som `"[MISSING]"` för manuell granskning |
| Duplicerad post | Dubletter borttagna, mer fullständig post behållen |
| Fel RTL-flagga | Rättas automatiskt utifrån kända RTL-koder |

### Användning

1. Öppna **Inställningar → 🔍 JSON-validator**
2. Välj fil: `languages.json` eller `formula_explanations.json` (eller båda)
3. **🔎 Kontrollera** – visar alla funna problem
4. **🛠 Rätta automatiskt** – löser alla automatiskt rättbara fel
5. **💾 Spara** – skriver tillbaka den rättade filen atomärt
6. **📋 Exportera rapport** (valfritt) – sparar en textfil med alla fynd

> ⚠️ **Obs:** Innan varje automatisk rättelse skapas en säkerhetskopia av originalfilen (`languages.json.bak` / `formula_explanations.json.bak`).

## ⭐ Favoritersystem

- Spara och återanvänd egna formler

- Åtskillnad mellan egna favoriter och teamfavoriter

- Teamfavoriter är skrivskyddade (endast administratören kan redigera)

- Dubblettinlägg förhindras

- Fri sortering av egna favoriter

- Synkronisering via nätverksenhet (valfritt konfigurerbart)

### Teamsynkronisering

Under **Inställningar → 🌐 Nätverkssökväg** kan en nätverksenhet anges (t.ex. `\\\\Server\\Delad\\formler`).

- Vid start: nätverksfavoriter sparas lokalt (reservkopia för offlineläge)

- Vid sparning: egna formler skrivs till nätverket, teamformler förblir oförändrade

## 🛠 Administratörspanel

Nås via knappen 🛠. Vid första klicket ställs ett lösenord in (PBKDF2-SHA256, endast hashen lagras).

- Lägga till, redigera och ta bort teamformler

- Ändra lösenord

- Skriva ändringar direkt till nätverksenheten

## 🔌 Plugin-hanterare

Plugin-hanteraren (`plugin_manager.py`) är ett fristående verktyg för att skapa och hantera egna formel-plugins för Calc2. Den finns i samma mapp som `Calc2.py` och startas via knappen 🔌 i Calc2.py:

### Funktioner

- **Skapa nytt plugin** – steg-för-steg-guide (namn, formler, översättningar, sammanfattning)

- **Lägg till formler** – lägga till formler i ett befintligt plugin

- **Redigera översättningar** – översätt formelnamn till alla 38 språk

- **Öppna plugin-mapp** – direkt i filutforskaren

- **Ta bort plugin** – med säkerhetsbekräftelse

### Plugin-struktur

Varje plugin finns som en undermapp i `plugins/` och består av två filer:

```
plugins/
  mitt_plugin/
    plugin.json      ← metadata (namn, version, författare, beskrivning)
    formulas.json    ← formler med översättningar
```

**Exempel på `plugin.json`:**

```
{
  "id": "mitt_plugin",
  "enabled": true,
  "version": "1.0",
  "author": "Ditt namn",
  "icon": "💰",
  "name": { "en": "Finance Formulas", "sv": "Ekonomiformler" },
  "description": { "en": "Useful formulas for financial calculations." }
}
```

**Exempel på `formulas.json`:**

```
[
  {
    "formula": "=SUM(A1:A10)",
    "name": { "en": "Sum of range", "sv": "Summa av område" },
    "description": { "en": "Adds all values in A1:A10." },
    "category": { "en": "Basic", "sv": "Grundläggande" }
  }
]
```

### Viktig information (⚠️ Important Notice)

I plugin-hanteraren finns knappen **⚠️ Important Notice**. Ett klick öppnar ett fönster med alla regler för korrekt plugin-skapande på engelska. Samma information finns också i `IMPORTANT_NOTICE.md`.

## 🌐 Flerspråkighet

38 språk tillgängliga, valbara direkt i appen.  
Nya språk kan läggas till via knappen 🌍 med Språkguiden.

**Obs om hindi (हिंदी):** Vid det första bytet till hindi installeras teckensnittet *Noto Sans Devanagari* en gång på systemnivå. Windows frågar då efter administratörsbehörighet.

## 🔤 RTL-stöd (höger till vänster)

Språk med skrift från höger till vänster känns igen automatiskt och hela gränssnittet speglas:

- **Arabiska (عربي)** – automatisk RTL-igenkänning
- **Hebreiska (עברית)** – automatisk RTL-igenkänning
- **Persiska / Farsi (فارسی)** – automatisk RTL-igenkänning
- **Urdu (اردو)** – automatisk RTL-igenkänning

**Vad ändras i RTL-läge:** Hela UI-layouten speglas, inmatningsfält använder RTL-justering, teckensnittet byter automatiskt till ett RTL-kompatibelt (t.ex. *Noto Sans Arabic*, *Noto Sans Hebrew*).

> 💡 **Obs:** Genererade LibreOffice-formler förblir alltid i LTR-syntax – bara gränssnittet ändrar riktning.


## 🗄️ Säkerhetskopiering och återställning

### Skapa säkerhetskopia

Via **Inställningar → 🗄️ Skapa säkerhetskopia**:

1. **Namn** – valfri beteckning (t.ex. `Kopia_Maj_2025`)
2. **Lösenord** – kopian krypteras med AES; utan lösenord är återställning omöjlig
3. **Sparplats** – lokalt eller på en nätverksenhet
4. Klicka på **💾 Skapa säkerhetskopia** – en `.calc2backup`-fil skapas

**Innehåll:** Alla favoriter, inställningar, teamfavoriter (valfritt), installerade plugins.

### Återställ säkerhetskopia

Via **Inställningar → 📂 Återställ säkerhetskopia**:

1. Välj säkerhetskopian (`.calc2backup`)
2. Ange lösenordet
3. Välj omfång: bara favoriter / bara inställningar / allt
4. Klicka på **🔄 Återställ**

> ⚠️ Vid återställning skrivs befintliga data över. Automatisk säkerhetskopiering av aktuella data erbjuds innan återställning.


## 💡 Tips

- `$A$1` → absolut referens (rullgardinsmeny bredvid cellfälten)

- **Ctrl+S** → spara formel i favoriter

- **Ctrl+C** → kopiera formel (utanför inmatningsfält)

- **Ctrl+Z / Ctrl+Y** → ångra / gör om

- **Ctrl+F12** → minimera / återställ fönstret (fungerar även när Calc2 är minimerat)

- **Delete-tangenten** i favoritlistan → ta bort post

- Formler kan justeras direkt i utdatafältet efter generering

## 📁 Projektstruktur

```
Calc2.py                        ← huvudprogram
plugin_manager.py               ← plugin-hanterare
IMPORTANT_NOTICE.md             ← anmärkningar om plugin-skapande
data/
  README_de.md / README_en.md / ...      ← hjälp per språk
  REFERENZ_de.md / REFERENZ_en.md / ...  ← funktionsreferens per språk
language/
  languages.json                ← gränssnittsöversättningar (38 språk)
  formula_explanations.json
services/
  language_tool.py              ← guide: lägga till nytt språk
  settings_service.py
  auth_service.py
  favorites_service.py
  network_sync.py
  install_service.py
  backup_service.py             ← säkerhetskopiering och återställning
  json_validator.py             ← kontroll och rättelse av languages.json / formula_explanations.json
plugins/                        ← plugin-mapp (skapas automatiskt)
  mitt_plugin/
    plugin.json
    formulas.json
fonts/
  NotoSansDevanagari-Regular.ttf  ← hindi-teckensnitt
  NotoSansArabic-Regular.ttf      ← arabiskt teckensnitt (RTL)
  NotoSansHebrew-Regular.ttf      ← hebreiskt teckensnitt (RTL)
python/                         ← inbäddad Python
  python.exe
  ...
settings.json                   ← skapas automatiskt
favoriter.json                  ← lokala favoriter (skapas automatiskt)
```

## 🧠 Tekniska höjdpunkter

- **Atomär filskrivning** → förhindrar skadade filer vid sparning

- **Tjänstearkitektur** → logik och gränssnitt är strikt åtskilda

- **Automatisk migrering** → gamla favoritformat känns igen och konverteras

- **Robust felhantering** → felaktiga filer leder inte till programkrasch

- **Syntaxmarkering** → formler visas i färg

- **Mörkt läge** → fullt stöd

- **Plugin-system** → Calc2 kan utökas med egna formel-plugins

- **RTL-motor** → automatisk igenkänning av RTL-språk, fullständig UI-spegling inkl. lämpliga teckensnitt

- **Säkerhetskopiering och återställning** → AES-krypterade säkerhetskopior med namn och lösenord, selektiv återställning

- **JSON-validator** → automatisk kontroll och rättelse av `languages.json` och `formula_explanations.json` inkl. landsnamn och obligatoriska fält

- **LibreOffice-källa** → `formula_explanations.json` fylls från den officiella LibreOffice Calc-dokumentationen (https://help.libreoffice.org)

- **Globalt kortkommando** → `Ctrl+F12` fungerar på systemnivå via biblioteket `keyboard` (bakgrundstråd)

## Licens

Fritt att använda för personliga och kommersiella ändamål.
