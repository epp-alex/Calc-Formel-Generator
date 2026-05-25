# LibreOffice Calc Formel-hjelper

Et Python-verktøy for rask oppretting, testing og administrasjon av LibreOffice Calc-formler – med favorattsystem, teamsynkronisering, flerspråklighet og plugin-behandler.

## 🚀 Funksjoner

- 📑 4 faner med over 60 funksjoner

- 🌐 38 språk (inkl. hindi med automatisk skriftinstallasjon)

- ⭐ Favorattsystem (lokalt og teamsynkronisering via nettverksstasjon)

- 🛠 Adminpanel for teamfavoratter (passordbeskyttet)

- 📋 Direkte kopierbare formler med syntaksfarging

- ✏️ Redigerbart utdatafelt med angre/gjør om

- 📖 Integrert hjelp og funksjonsreferanse (per språk)

- 💾 Automatisk lagring (JSON, atomisk skrevet)

- 🌙 Mørk modus

- 🔌 Plugin-behandler for å lage egne formel-plugin

- 🔤 RTL-støtte (høyre til venstre) – automatisk gjenkjenning av skriveretning

- 🗄️ Sikkerhetskopiering og gjenoppretting – lagre alle innstillinger og favoratter med navn og passord

- ⌨️ Global hurtigtast `Ctrl+F12` for å minimere/gjenopprette vinduet
- 🔍 JSON-validator – automatisk kontroll og retting av `languages.json` og `formula_explanations.json`

## 🖥️ Bruk

**1. Angi inndata**

- Celleområde (f.eks. `A1:A10`)

- Celle 1 / Celle 2 (f.eks. `A1`, `B1`)

- Valgfri parameter (f.eks. tekst eller indeks)

- Valg av absolutt referansemodus: `A1`, `$A1`, `A$1`, `$A$1`

**2. Velg en funksjon** Velg en fane og klikk på en funksjon – formelen genereres umiddelbart.

**3. Tilpass formelen** Den genererte formelen kan redigeres direkte i utdatafeltet.

**4. Kopier** Overfør til utklippstavlen med ett klikk (inkl. syntaksfarger).

**5. Bruk favoratter**

- ⭐ Lagre → lagre gjeldende formel (Ctrl+S)

- 📂 Laste → gjenbruke formel

- ❌ Slette → Delete-tasten eller knapp

- 🕐 Historikk → sist brukte formler

## 📊 Faneoversikt

**Fane 1 – Grunnfunksjoner** `+` `-` `*` `/` `^` SUM, AVERAGE, MIN, MAX, MEDIAN, COUNT, COUNTA, SUMPRODUCT

**Fane 2 – Avanserte funksjoner** IF, AND, OR, NOT SUMIF, COUNTIF, AVERAGEIF, SUMIFS, STDEV, VAR, COUNTBLANK, LARGE

**Fane 3 – Dato og tekst** TODAY, NOW, YEAR, MONTH, DAY, DATE, DATEDIF, WEEKDAY CONCATENATE, LEN, LEFT, RIGHT, MID, UPPER, LOWER, TRIM

**Fane 4 – Oppslag og avrunding** VLOOKUP, HLOOKUP, INDEX, MATCH, INDEX+MATCH ROUND, ROUNDUP, ROUNDDOWN, INT, TRUNC, ABS, MOD, SQRT, RAND


## 📖 Formelforklaringer fra LibreOffice-dokumentasjonen

Filen `formula_explanations.json` fylles direkte fra den offisielle **LibreOffice Calc-dokumentasjonen** (https://help.libreoffice.org).

### Datakilde og oppdatering

- Beskrivelser, syntaksinformasjon og eksempler hentes fra LibreOffices offisielle hjelpeside
- Støttede språk avhenger av oversettelsene tilgjengelig på siden
- Filen inneholder for hver funksjon: navn, syntaks, beskrivelse, eksempel og kategori
- Tillegg eller rettinger kan gjøres manuelt (se JSON-validator)

### Struktur for `formula_explanations.json`

```json
{
  "SUM": {
    "nb": {
      "syntax": "SUM(Tall1; Tall2; ...)",
      "description": "Legger sammen alle tall i et celleområde.",
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

| Felt | Obligatorisk | Beskrivelse |
|------|-------------|-------------|
| `syntax` | ✅ | Formelsyntaks med parametere |
| `description` | ✅ | Kort beskrivelse av funksjonen |
| `example` | ✅ | Brukseksempel som ferdig formel |
| `note` | ❌ | Valgfri merknad |

> 💡 **Merknad:** Hvis det ikke finnes en oppføring for et språk, faller appen automatisk tilbake til den engelske versjonen.

---

## 🔍 JSON-validator for språkfiler

Den integrerte **JSON-validatoren** kontrollerer og retter `languages.json` og `formula_explanations.json` for konsistens, fullstendighet og korrekte landsnavn. Tilgjengelig via **Innstillinger → 🔍 JSON-validator**.

### Hva kontrolleres?

#### `languages.json`

- ✅ Alle 38 språk er til stede (etter ISO 639-1 språkkode)
- ✅ Korrekte **lands- og språknavn** (f.eks. `"nb"` → `"Norsk bokmål"`)
- ✅ Ingen duplikate språkkoder
- ✅ Obligatoriske felt til stede: `name`, `native_name`, `flag`, `rtl`
- ✅ RTL-merking satt korrekt (Arabisk, Hebraisk, Persisk, Urdu → `"rtl": true`)

#### `formula_explanations.json`

- ✅ Alle funksjoner fra de 4 fanene er registrert
- ✅ Obligatoriske felt til stede: `syntax`, `description`, `example`
- ✅ Ingen tomme felt (`""` eller `null`)
- ✅ Språkkoder stemmer overens med `languages.json`

### Rettefunksjoner

| Feiltype | Automatisk retting |
|----------|-------------------|
| Feil landsnavn | Erstattet med riktig navn i henhold til ISO |
| Manglende språkoppføring | Fylt med engelsk reserveversjon |
| Tomt obligatorisk felt | Merket som `"[MISSING]"` for manuell gjennomgang |
| Duplikat oppføring | Duplikater fjernet, mest fullstendig oppføring beholdt |
| Feil RTL-merking | Automatisk rettet basert på kjente RTL-koder |

### Bruk

1. Åpne **Innstillinger → 🔍 JSON-validator**
2. Velg fil: `languages.json` eller `formula_explanations.json` (eller begge)
3. **🔎 Kontroller** – viser alle fundne problemer
4. **🛠 Rett automatisk** – løser alle automatisk rettbare feil
5. **💾 Lagre** – skriver den rettede filen atomisk tilbake
6. **📋 Eksporter rapport** (valgfritt) – lagrer en tekstfil med alle funn

> ⚠️ **Merknad:** Før hver automatisk retting opprettes en sikkerhetskopi av den originale filen (`languages.json.bak` / `formula_explanations.json.bak`).

## ⭐ Favorattsystem

- Lagre og gjenbruke egne formler

- Skille mellom egne og teamfavoratter

- Teamfavoratter er skrivebeskyttet (bare admin kan redigere)

- Duplikate oppføringer forhindres

- Fri sortering av egne favoratter

- Synkronisering via nettverksstasjon (valgfritt konfigurerbart)

### Teamsynkronisering

Via **Innstillinger → 🌐 Nettverksbane** kan man angi en nettverksstasjon (f.eks. `\\\\Server\\Deling\\formler`).

- Ved oppstart: nettverksfavoratter lagres lokalt (offline-reserve)

- Ved lagring: egne formler skrives til nettverket, teamformler forblir uendret

## 🛠 Adminpanel

Tilgjengelig via 🛠-knappen. Ved første klikk angis et passord (PBKDF2-SHA256, bare hash-verdi lagres).

- Legge til, redigere og slette teamformler

- Endre passord

- Skrive endringer direkte til nettverksstasjonen

## 🔌 Plugin-behandler

Plugin-behandleren (`plugin_manager.py`) er et selvstendig verktøy for å opprette og administrere egne formel-plugin for Calc2. Den ligger i samme mappe som `Calc2.py` og startes via 🔌-knappen i Calc2.py:

### Funksjoner

- **Opprett nytt plugin** – steg-for-steg-veiviser (navn, formler, oversettelser, sammendrag)

- **Legge til formler** – legge til formler i et eksisterende plugin

- **Rediger oversettelser** – oversette formelnavn til alle 38 språk

- **Åpne plugin-mappe** – direkte i filutforskeren

- **Slette plugin** – inkl. bekreftelsesdialog

### Plugin-struktur

Hvert plugin ligger som en undermappe i `plugins/` og består av to filer:

```
plugins/
  mitt_plugin/
    plugin.json      ← metadata (navn, versjon, forfatter, beskrivelse)
    formulas.json    ← formler med oversettelser
```

**Eksempel på `plugin.json`:**

```
{
  "id": "mitt_plugin",
  "enabled": true,
  "version": "1.0",
  "author": "Ditt navn",
  "icon": "💰",
  "name": { "en": "Finance Formulas", "nb": "ØkonomiFormler" },
  "description": { "en": "Useful formulas for financial calculations." }
}
```

**Eksempel på `formulas.json`:**

```
[
  {
    "formula": "=SUM(A1:A10)",
    "name": { "en": "Sum of range", "nb": "Sum av område" },
    "description": { "en": "Adds all values in A1:A10." },
    "category": { "en": "Basic", "nb": "Grunnleggende" }
  }
]
```

### Viktig merknad (⚠️ Important Notice)

I plugin-behandleren finnes knappen **⚠️ Important Notice**. Et klikk åpner et vindu med alle regler for korrekt plugin-oppretting på engelsk. Den samme informasjonen finnes også i `IMPORTANT_NOTICE.md`.

## 🌐 Flerspråklighet

38 språk tilgjengelige, kan byttes direkte i appen.  
Nye språk kan legges til via 🌍-knappen med Språkveiviseren.

**Merknad om hindi (हिंदी):** Ved første bytte til hindi installeres skrifttypen *Noto Sans Devanagari* systemomfattende én gang. Windows ber da om administratorrettigheter.

## 🔤 RTL-støtte (høyre til venstre)

Språk med skrift fra høyre til venstre gjenkjennes automatisk og hele grensesnittet speiles:

- **Arabisk (عربي)** – automatisk RTL-gjenkjenning
- **Hebraisk (עברית)** – automatisk RTL-gjenkjenning
- **Persisk / Farsi (فارسی)** – automatisk RTL-gjenkjenning
- **Urdu (اردو)** – automatisk RTL-gjenkjenning

**Hva endres i RTL-modus:** Hele UI-layouten speiles, inndatafelter bruker RTL-justering, skrifttypen byttes automatisk til en RTL-kompatibel (f.eks. *Noto Sans Arabic*, *Noto Sans Hebrew*).

> 💡 **Merknad:** Genererte LibreOffice-formler forblir alltid i LTR-syntaks – bare brukergrensesnittet endrer retning.


## 🗄️ Sikkerhetskopiering og gjenoppretting

### Opprett sikkerhetskopi

Via **Innstillinger → 🗄️ Opprett sikkerhetskopi**:

1. **Navn** – valgfri betegnelse (f.eks. `Kopi_Mai_2025`)
2. **Passord** – kopien krypteres med AES; uten passord er gjenoppretting ikke mulig
3. **Lagringssted** – lokalt eller på en nettverksstasjon
4. Klikk **💾 Opprett sikkerhetskopi** – oppretter en `.calc2backup`-fil

**Innhold:** Alle favoratter, innstillinger, teamfavoratter (valgfritt), installerte plugin.

### Gjenopprett sikkerhetskopi

Via **Innstillinger → 📂 Gjenopprett sikkerhetskopi**:

1. Velg sikkerhetskopifil (`.calc2backup`)
2. Oppgi passordet
3. Velg omfang: bare favoratter / bare innstillinger / alt
4. Klikk **🔄 Gjenopprett**

> ⚠️ Eksisterende data overskrives ved gjenoppretting. Et automatisk backup av gjeldende data tilbys på forhånd.


## 💡 Tips

- `$A$1` → absolutt referanse (rullegardin ved siden av cellefeltene)

- **Ctrl+S** → lagre formel i favoratter

- **Ctrl+C** → kopiere formel (utenfor inndatafelt)

- **Ctrl+Z / Ctrl+Y** → angre / gjør om

- **Ctrl+F12** → minimere / gjenopprette vinduet (fungerer også når Calc2 er minimert)

- **Delete-tasten** i favorattlisten → slett oppføring

- Formler kan tilpasses direkte i utdatafeltet etter generering

## 📁 Prosjektstruktur

```
Calc2.py                        ← hovedprogram
plugin_manager.py               ← plugin-behandler
IMPORTANT_NOTICE.md             ← merknader om plugin-oppretting
data/
  README_de.md / README_en.md / ...      ← hjelp per språk
  REFERENZ_de.md / REFERENZ_en.md / ...  ← funksjonsreferanse per språk
language/
  languages.json                ← UI-oversettelser (38 språk)
  formula_explanations.json
services/
  language_tool.py              ← veiviser: legge til nytt språk
  settings_service.py
  auth_service.py
  favorites_service.py
  network_sync.py
  install_service.py
  backup_service.py             ← sikkerhetskopiering og gjenoppretting
  json_validator.py             ← kontroll og retting av languages.json / formula_explanations.json
plugins/                        ← plugin-mappe (opprettes automatisk)
  mitt_plugin/
    plugin.json
    formulas.json
fonts/
  NotoSansDevanagari-Regular.ttf  ← hindi-skrifttype
  NotoSansArabic-Regular.ttf      ← arabisk skrifttype (RTL)
  NotoSansHebrew-Regular.ttf      ← hebraisk skrifttype (RTL)
python/                         ← innebygd Python
  python.exe
  ...
settings.json                   ← opprettes automatisk
favoratter.json                 ← lokale favoratter (opprettes automatisk)
```

## 🧠 Tekniske høydepunkter

- **Atomisk filskriving** → forhindrer ødelagte filer ved lagring

- **Tjenestearkitektur** → logikk og brukergrensesnitt er strengt atskilt

- **Automatisk migrering** → gamle favoritformater gjenkjennes og konverteres

- **Robust feilhåndtering** → feilaktige filer fører ikke til krasj

- **Syntaksfarging** → formler vises i farger

- **Mørk modus** → fullt støttet

- **Plugin-system** → Calc2 kan utvides med egne formel-plugin

- **RTL-motor** → automatisk gjenkjenning av RTL-språk, full UI-speiling inkl. passende skrifttyper

- **Sikkerhetskopiering og gjenoppretting** → AES-krypterte sikkerhetskopier med navn og passord, selektiv gjenoppretting

- **JSON-validator** → automatisk kontroll og retting av `languages.json` og `formula_explanations.json` inkl. landsnavn og obligatoriske felt

- **LibreOffice-kilde** → `formula_explanations.json` fylles fra den offisielle LibreOffice Calc-dokumentasjonen (https://help.libreoffice.org)

- **Global hurtigtast** → `Ctrl+F12` fungerer systemomfattende via `keyboard`-biblioteket (bakgrunnstråd)

## Lisens

Fritt brukbart til personlige og kommersielle formål.
