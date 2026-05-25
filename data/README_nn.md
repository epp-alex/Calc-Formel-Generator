# LibreOffice Calc Formel-hjelpar

Eit Python-verktøy for rask oppretting, testing og handtering av LibreOffice Calc-formlar – med favorittsystem, teamsynkronisering, fleirspråklegheit og plugin-handterar.

## 🚀 Funksjonar

- 📑 4 faner med over 60 funksjonar

- 🌐 38 språk (inkl. hindi med automatisk skriftinstallasjon)

- ⭐ Favorittsystem (lokalt og teamsynkronisering via nettverksstasjon)

- 🛠 Adminpanel for teamfavorittар (passordbeskytta)

- 📋 Direkte kopierbare formlar med syntaksfarging

- ✏️ Redigerbart utdatafelt med angre/gjer om

- 📖 Integrert hjelp og funksjonsreferanse (per språk)

- 💾 Automatisk lagring (JSON, atomisk skriven)

- 🌙 Mørk modus

- 🔌 Plugin-handterar for å laga eigne formel-plugin

- 🔤 RTL-støtte (høgre til venstre) – automatisk gjenkjenning av skriveretning

- 🗄️ Tryggleikskopiering og gjenoppretting – lagra alle innstillingar og favorittar med namn og passord

- ⌨️ Global snøggtast `Ctrl+F12` for å minimera/gjenoppretta vindauget
- 🔍 JSON-validator – automatisk kontroll og retting av `languages.json` og `formula_explanations.json`

## 🖥️ Bruk

**1. Gjera inndata**

- Celleområde (t.d. `A1:A10`)

- Celle 1 / Celle 2 (t.d. `A1`, `B1`)

- Valfri parameter (t.d. tekst eller indeks)

- Val av absolutt referansemodus: `A1`, `$A1`, `A$1`, `$A$1`

**2. Vel ein funksjon** Vel ei fane og klikk på ein funksjon – formelen vert generert med det same.

**3. Tilpass formelen** Den genererte formelen kan redigerast direkte i utdatafeltet.

**4. Kopiera** Overfør til utklippstavla med eitt klikk (inkl. syntaksfargar).

**5. Bruka favorittar**

- ⭐ Lagra → lagra gjeldande formel (Ctrl+S)

- 📂 Lasta → gjenbruka formel

- ❌ Sletta → Delete-tasten eller knapp

- 🕐 Historikk → sist nytta formlar

## 📊 Faneoversyn

**Fane 1 – Grunnfunksjonar** `+` `-` `*` `/` `^` SUM, AVERAGE, MIN, MAX, MEDIAN, COUNT, COUNTA, SUMPRODUCT

**Fane 2 – Avanserte funksjonar** IF, AND, OR, NOT SUMIF, COUNTIF, AVERAGEIF, SUMIFS, STDEV, VAR, COUNTBLANK, LARGE

**Fane 3 – Dato og tekst** TODAY, NOW, YEAR, MONTH, DAY, DATE, DATEDIF, WEEKDAY CONCATENATE, LEN, LEFT, RIGHT, MID, UPPER, LOWER, TRIM

**Fane 4 – Oppslag og avrunding** VLOOKUP, HLOOKUP, INDEX, MATCH, INDEX+MATCH ROUND, ROUNDUP, ROUNDDOWN, INT, TRUNC, ABS, MOD, SQRT, RAND


## 📖 Formelforklaringar frå LibreOffice-dokumentasjonen

Fila `formula_explanations.json` vert fylt direkte frå den offisielle **LibreOffice Calc-dokumentasjonen** (https://help.libreoffice.org).

### Datakjelde og oppdatering

- Skildringar, syntaksinformasjon og døme vert henta frå LibreOffice si offisielle hjelpeside
- Støtta språk er avhengig av omsetjingane som er tilgjengelege på sida
- Fila inneheld for kvar funksjon: namn, syntaks, skildring, døme og kategori
- Tillegg eller rettingar kan gjerast manuelt (sjå JSON-validator)

### Struktur for `formula_explanations.json`

```json
{
  "SUM": {
    "nn": {
      "syntax": "SUM(Tal1; Tal2; ...)",
      "description": "Legg saman alle tal i eit celleområde.",
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

| Felt | Obligatorisk | Skildring |
|------|-------------|----------|
| `syntax` | ✅ | Formelsyntaks med parametrar |
| `description` | ✅ | Kort skildring av funksjonen |
| `example` | ✅ | Bruksdøme som ferdig formel |
| `note` | ❌ | Valfri merknad |

> 💡 **Merknad:** Viss det ikkje finst ei oppføring for eit språk, fell appen automatisk tilbake til den engelske versjonen.

---

## 🔍 JSON-validator for språkfiler

Den integrerte **JSON-validatoren** kontrollerer og rettar `languages.json` og `formula_explanations.json` for konsistens, fullstende og korrekte landsnamn. Tilgjengeleg via **Innstillingar → 🔍 JSON-validator**.

### Kva vert kontrollert?

#### `languages.json`

- ✅ Alle 38 språk er til stades (etter ISO 639-1 språkkode)
- ✅ Korrekte **lands- og språknamn** (t.d. `"nn"` → `"Nynorsk"`)
- ✅ Ingen duplikate språkkoder
- ✅ Obligatoriske felt til stades: `name`, `native_name`, `flag`, `rtl`
- ✅ RTL-merking sett korrekt (Arabisk, Hebraisk, Persisk, Urdu → `"rtl": true`)

#### `formula_explanations.json`

- ✅ Alle funksjonar frå dei 4 fanene er registrerte
- ✅ Obligatoriske felt til stades: `syntax`, `description`, `example`
- ✅ Ingen tomme felt (`""` eller `null`)
- ✅ Språkkoder stemmer overeins med `languages.json`

### Rettefunksjonar

| Feiltype | Automatisk retting |
|----------|-------------------|
| Feil landsnamn | Erstatta med riktig namn i samsvar med ISO |
| Manglande språkoppføring | Fylt med engelsk reserveversjon |
| Tomt obligatorisk felt | Merka som `"[MISSING]"` for manuell gjennomgang |
| Duplikat oppføring | Duplikat fjerna, mest fullstendig oppføring behalde |
| Feil RTL-merking | Automatisk retta basert på kjende RTL-kodar |

### Bruk

1. Opna **Innstillingar → 🔍 JSON-validator**
2. Vel fil: `languages.json` eller `formula_explanations.json` (eller begge)
3. **🔎 Kontroller** – syner alle funne problem
4. **🛠 Rett automatisk** – løyser alle automatisk rettbare feil
5. **💾 Lagra** – skriv den retta fila atomisk tilbake
6. **📋 Eksporter rapport** (valfritt) – lagrar ei tekstfil med alle funn

> ⚠️ **Merknad:** Før kvar automatisk retting vert det oppretta ei tryggleikskopi av den originale fila (`languages.json.bak` / `formula_explanations.json.bak`).

## ⭐ Favorittsystem

- Lagra og gjenbruka eigne formlar

- Skilje mellom eigne og teamfavorittar

- Teamfavorittar er skriveverna (berre admin kan redigera)

- Duplikate oppføringer vert hindra

- Fri sortering av eigne favorittar

- Synkronisering via nettverksstasjon (valfritt konfigurerbart)

### Teamsynkronisering

Via **Innstillingar → 🌐 Nettverkssти** kan ein leggja inn ein nettverksstasjon (t.d. `\\\\Server\\Deling\\formlar`).

- Ved oppstart: nettverksfavorittar vert lagra lokalt (offline-reserve)

- Ved lagring: eigne formlar vert skrivne til nettverket, teamformlar vert uendra

## 🛠 Adminpanel

Tilgjengeleg via 🛠-knappen. Ved første klikk vert det sett eit passord (PBKDF2-SHA256, berre hash-verdi vert lagra).

- Leggja til, redigera og sletta teamformlar

- Endra passord

- Skriva endringar direkte til nettverksstasjonen

## 🔌 Plugin-handterar

Plugin-handteraren (`plugin_manager.py`) er eit sjølvstendig verktøy for å oppretta og handsama eigne formel-plugin for Calc2. Han ligg i same mappe som `Calc2.py` og vert starta via 🔌-knappen i Calc2.py:

### Funksjonar

- **Opprett nytt plugin** – steg-for-steg-veiviser (namn, formlar, omsetjingar, samanfatning)

- **Leggja til formlar** – leggja formlar til eit eksisterande plugin

- **Redigera omsetjingar** – omsetja formelnamn til alle 38 språk

- **Opna plugin-mappe** – direkte i filutforskaren

- **Sletta plugin** – inkl. stadfestingsspørsmål

### Plugin-struktur

Kvart plugin ligg som ein undermappe i `plugins/` og inneheld to filer:

```
plugins/
  mitt_plugin/
    plugin.json      ← metadata (namn, versjon, forfattar, skildring)
    formulas.json    ← formlar med omsetjingar
```

**Døme på `plugin.json`:**

```
{
  "id": "mitt_plugin",
  "enabled": true,
  "version": "1.0",
  "author": "Ditt namn",
  "icon": "💰",
  "name": { "en": "Finance Formulas", "nn": "ØkonomiFormlar" },
  "description": { "en": "Useful formulas for financial calculations." }
}
```

**Døme på `formulas.json`:**

```
[
  {
    "formula": "=SUM(A1:A10)",
    "name": { "en": "Sum of range", "nn": "Sum av område" },
    "description": { "en": "Adds all values in A1:A10." },
    "category": { "en": "Basic", "nn": "Grunnleggande" }
  }
]
```

### Viktig merknad (⚠️ Important Notice)

I plugin-handteraren finst knappen **⚠️ Important Notice**. Eit klikk opnar eit vindauge med alle reglar for korrekt plugin-oppretting på engelsk. Den same informasjonen finst òg i `IMPORTANT_NOTICE.md`.

## 🌐 Fleirspråklegheit

38 språk tilgjengelege, kan byttast direkte i appen.  
Nye språk kan leggjast til via 🌍-knappen med Språkveivisaren.

**Merknad om hindi (हिंदी):** Ved første bytte til hindi vert skrifttypen *Noto Sans Devanagari* installert systemomfattande éin gong. Windows ber då om administratorrettar.

## 🔤 RTL-støtte (høgre til venstre)

Språk med skrift frå høgre til venstre vert gjenkjende automatisk og heile grensesnittet vert spegla:

- **Arabisk (عربي)** – automatisk RTL-gjenkjenning
- **Hebraisk (עברית)** – automatisk RTL-gjenkjenning
- **Persisk / Farsi (فارسی)** – automatisk RTL-gjenkjenning
- **Urdu (اردو)** – automatisk RTL-gjenkjenning

**Kva endrar seg i RTL-modus:** Heile UI-layouten vert spegla, inndatafelt bruker RTL-justering, skrifttypen skiftar automatisk til ein RTL-kompatibel (t.d. *Noto Sans Arabic*, *Noto Sans Hebrew*).

> 💡 **Merknad:** Genererte LibreOffice-formlar er alltid i LTR-syntaks – berre brukargrensesnittet skiftar retning.


## 🗄️ Tryggleikskopiering og gjenoppretting

### Opprett tryggleikskopi

Via **Innstillingar → 🗄️ Opprett tryggleikskopi**:

1. **Namn** – valfri nemning (t.d. `Kopi_Mai_2025`)
2. **Passord** – kopien vert kryptert med AES; utan passord er gjenoppretting umogeleg
3. **Lagringsstad** – lokalt eller på ein nettverksstasjon
4. Klikk **💾 Opprett tryggleikskopi** – oppretter ei `.calc2backup`-fil

**Innhald:** Alle favorittar, innstillingar, teamfavorittar (valfritt), installerte plugin.

### Gjenopprett tryggleikskopi

Via **Innstillingar → 📂 Gjenopprett tryggleikskopi**:

1. Vel tryggleikskopifila (`.calc2backup`)
2. Oppgi passordet
3. Vel omfang: berre favorittar / berre innstillingar / alt
4. Klikk **🔄 Gjenopprett**

> ⚠️ Eksisterande data vert overskrivne ved gjenoppretting. Automatisk kopi av gjeldande data vert tilbode på førehand.


## 💡 Tips

- `$A$1` → absolutt referanse (rullegardin ved sida av cellefelta)

- **Ctrl+S** → lagra formel i favorittар

- **Ctrl+C** → kopiera formel (utanfor inndatafelt)

- **Ctrl+Z / Ctrl+Y** → angre / gjer om

- **Ctrl+F12** → minimera / gjenoppretta vindauget (fungerer òg når Calc2 er minimert)

- **Delete-tasten** i favorittlista → slett oppføring

- Formlar kan tilpassast direkte i utdatafeltet etter generering

## 📁 Prosjektstruktur

```
Calc2.py                        ← hovudprogram
plugin_manager.py               ← plugin-handterar
IMPORTANT_NOTICE.md             ← merknader om plugin-oppretting
data/
  README_de.md / README_en.md / ...      ← hjelp per språk
  REFERENZ_de.md / REFERENZ_en.md / ...  ← funksjonsreferanse per språk
language/
  languages.json                ← UI-omsetjingar (38 språk)
  formula_explanations.json
services/
  language_tool.py              ← veiviser: leggja til nytt språk
  settings_service.py
  auth_service.py
  favorites_service.py
  network_sync.py
  install_service.py
  backup_service.py             ← tryggleikskopiering og gjenoppretting
  json_validator.py             ← kontroll og retting av languages.json / formula_explanations.json
plugins/                        ← plugin-mappe (vert oppretta automatisk)
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
settings.json                   ← vert oppretta automatisk
favoritar.json                  ← lokale favorittar (vert oppretta automatisk)
```

## 🧠 Tekniske høgdepunkt

- **Atomisk filskriving** → hindrar øydelagde filer ved lagring

- **Teneste-arkitektur** → logikk og brukargrensesnitt er strengt skilde

- **Automatisk migrering** → gamle favoritformat vert gjenkjende og konverterte

- **Robust feilhandsaming** → feilaktige filer fører ikkje til krasj

- **Syntaksfarging** → formlar vert viste i fargar

- **Mørk modus** → fullt støtta

- **Plugin-system** → Calc2 kan utvidast med eigne formel-plugin

- **RTL-motor** → automatisk gjenkjenning av RTL-språk, full UI-spegling inkl. høvelege skrifttypar

- **Tryggleikskopiering og gjenoppretting** → AES-krypterte tryggleikskopiar med namn og passord, selektiv gjenoppretting

- **JSON-validator** → automatisk kontroll og retting av `languages.json` og `formula_explanations.json` inkl. landsnamn og obligatoriske felt

- **LibreOffice-kjelde** → `formula_explanations.json` vert fylt frå den offisielle LibreOffice Calc-dokumentasjonen (https://help.libreoffice.org)

- **Global snøggtast** → `Ctrl+F12` fungerer systemomfattande via `keyboard`-biblioteket (bakgrunnstråd)

## Lisens

Fritt brukbart til personlege og kommersielle føremål.
