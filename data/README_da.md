# LibreOffice Calc Formelassistent

Et Python-værktøj til hurtig oprettelse, afprøvning og administration af formler i LibreOffice Calc – med et favoritssystem, teamsynkronisering, flersproget understøttelse og en plugin-manager.

## 🚀 Funktioner

- 📑 4 faner med over 60 funktioner

- 🌐 38 sprog (inkl. hindi med automatisk skrifttypeinstallation)

- ⭐ Favoritssystem (lokalt og teamsynkronisering via netværksdrev)

- 🛠 Adminpanel til teamfavoritter (adgangskodebeskyttet)

- 📋 Indsætningsklare formler med syntaksfremhævning

- ✏️ Redigerbart outputfelt med fortryd/gentag

- 📖 Integreret hjælp og funktionsreference (pr. sprog)

- 💾 Automatisk lagring (JSON, atomisk skrivning)

- 🌙 Mørkt tema

- 🔌 Plugin-manager til oprettelse af egne formel-plugins

- 🔤 RTL-understøttelse (højre mod venstre) – automatisk genkendelse af skriveretning

- 🗄️ Sikkerhedskopiering og gendannelse – gem alle indstillinger og favoritter med navn og adgangskode

- ⌨️ Global tastaturgenvej `Ctrl+F12` til at minimere/gendanne vinduet
- 🔍 JSON-validator – automatisk kontrol og rettelse af `languages.json` og `formula_explanations.json`

## 🖥️ Brug

**1. Indtast dine værdier**

- Celleområde (f.eks. `A1:A10`)

- Celle 1 / Celle 2 (f.eks. `A1`, `B1`)

- Valgfri parameter (f.eks. tekst eller indeks)

- Referencetilstand valgbar: `A1`, `$A1`, `A$1`, `$A$1`

**2. Vælg en funktion** Vælg en fane og klik på en funktion – formlen genereres med det samme.

**3. Tilpas formlen** Den genererede formel kan redigeres direkte i outputfeltet.

**4. Kopiér** Kopiér til udklipsholderen med ét klik (inkl. syntaksfarver).

**5. Brug favoritter**

- ⭐ Gem → gem den aktuelle formel (Ctrl+S)

- 📂 Indlæs → genbrug en gemt formel

- ❌ Slet → Delete-tasten eller knappen

- 🕐 Historik → senest anvendte formler

## 📊 Faneoversigt

**Fane 1 – Grundlæggende funktioner** `+` `-` `\*` `/` `^` SUM, AVERAGE, MIN, MAX, MEDIAN, COUNT, COUNTA, SUMPRODUCT

**Fane 2 – Avancerede funktioner** IF, AND, OR, NOT SUMIF, COUNTIF, AVERAGEIF, SUMIFS, STDEV, VAR, COUNTBLANK, LARGE

**Fane 3 – Dato og tekst** TODAY, NOW, YEAR, MONTH, DAY, DATE, DATEDIF, WEEKDAY CONCATENATE, LEN, LEFT, RIGHT, MID, UPPER, LOWER, TRIM

**Fane 4 – Opslag og afrunding** VLOOKUP, HLOOKUP, INDEX, MATCH, INDEX+MATCH ROUND, ROUNDUP, ROUNDDOWN, INT, TRUNC, ABS, MOD, SQRT, RAND


## 📖 Formelforklaringer fra LibreOffice-dokumentationen

Filen `formula_explanations.json` udfyldes direkte fra den officielle **LibreOffice Calc-dokumentation** (https://help.libreoffice.org).

### Datakilde og opdatering

- Beskrivelser, syntaksoplysninger og eksempler hentes fra LibreOffices officielle hjælpeside
- De understøttede sprog afhænger af de oversættelser, der er tilgængelige på hjemmesiden
- Filen indeholder for hver funktion: navn, syntaks, beskrivelse, eksempel og kategori
- Tilføjelser eller rettelser kan foretages manuelt (se JSON-validator)

### Struktur for `formula_explanations.json`

```json
{
  "SUM": {
    "da": {
      "syntax": "SUM(Tal1; Tal2; ...)",
      "description": "Lægger alle tal i et celleområde sammen.",
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
| `syntax` | ✅ | Formelsyntaks med parametre |
| `description` | ✅ | Kort beskrivelse af funktionen |
| `example` | ✅ | Anvendelseseksempel som færdig formel |
| `note` | ❌ | Valgfri bemærkning |

> 💡 **Bemærkning:** Hvis der ikke findes en post for et sprog, falder appen automatisk tilbage til den engelske version.

---

## 🔍 JSON-validator til sprogfiler

Den integrerede **JSON-validator** kontrollerer og retter `languages.json` og `formula_explanations.json` for konsistens, fuldstændighed og korrekte landenavne. Tilgængelig via **Indstillinger → 🔍 JSON-validator**.

### Hvad kontrolleres?

#### `languages.json`

- ✅ Alle 38 sprog er til stede (efter ISO 639-1 sprogkode)
- ✅ Korrekte **lande- og sprognavne** (f.eks. `"da"` → `"Dansk"`)
- ✅ Ingen duplikerede sprogkoder
- ✅ Obligatoriske felter til stede: `name`, `native_name`, `flag`, `rtl`
- ✅ RTL-markering sat korrekt (Arabisk, Hebraisk, Persisk, Urdu → `"rtl": true`)

#### `formula_explanations.json`

- ✅ Alle funktioner fra de 4 faner er registreret
- ✅ Obligatoriske felter til stede: `syntax`, `description`, `example`
- ✅ Ingen tomme felter (`""` eller `null`)
- ✅ Sprogkoder stemmer overens med `languages.json`

### Rettelseslunktioner

| Fejltype | Automatisk rettelse |
|----------|---------------------|
| Forkert landenavn | Erstattes med det korrekte navn ifl. ISO-standard |
| Manglende sprogpost | Udfyldes med engelsk reserve |
| Tomt obligatorisk felt | Markeres som `"[MISSING]"` til manuel kontrol |
| Duplikeret post | Dubletter fjernes, den mere fuldstændige beholdes |
| Forkert RTL-flag | Rettes automatisk ud fra kendte RTL-sprogkoder |

### Brug af validatoren

1. Åbn **Indstillinger → 🔍 JSON-validator**
2. Vælg fil: `languages.json` eller `formula_explanations.json` (eller begge)
3. **🔎 Kontrollér** – viser alle fundne problemer
4. **🛠 Ret automatisk** – løser alle automatisk rettelige fejl
5. **💾 Gem** – skriver den rettede fil atomisk
6. **📋 Eksportér rapport** (valgfrit) – gemmer en tekstfil med alle fund

> ⚠️ **Bemærkning:** Inden automatisk rettelse oprettes en sikkerhedskopi af den originale fil (`languages.json.bak` / `formula_explanations.json.bak`).

## ⭐ Favoritssystem

- Gem og genbrug dine egne formler

- Klar adskillelse mellem personlige og teamfavoritter

- Teamfavoritter er skrivebeskyttede (kun administratorer kan redigere dem)

- Dubletter forhindres automatisk

- Fri sortering af personlige favoritter

- Synkronisering via netværksdrev (valgfrit konfigurerbart)

### Teamsynkronisering

Gå til **Indstillinger → 🌐 Netværkssti** for at angive stien til et netværksdrev (f.eks. `\\\\Server\\Share\\formulas`).

- Ved opstart: netværksfavoritter gemmes lokalt i en cache (offline-reserveløsning)

- Ved lagring: egne formler skrives til netværket; teamformler forbliver uændrede

## 🛠 Adminpanel

Tilgængeligt via 🛠-knappen. Ved første klik oprettes en adgangskode (PBKDF2-SHA256, kun hashen gemmes).

- Tilføj, rediger og slet teamformler

- Skift adgangskode

- Skriv ændringer direkte til netværksdrevet

## 🔌 Plugin-manager

Plugin-manageren (`plugin_manager.py`) er et selvstændigt værktøj til at oprette og administrere egne formel-plugins til Calc2. Den ligger i samme mappe som `Calc2.py` og startes fra 🔌-knappen i Calc2.py.

### Funktioner

- **Opret nyt plugin** – trin-for-trin-guide (navn, formler, oversættelser, opsummering)

- **Tilføj formler** – tilføj formler til et eksisterende plugin

- **Rediger oversættelser** – oversæt formelnavne til alle 38 sprog

- **Åbn plugin-mappe** – direkte i filstifinderen

- **Slet plugin** – med bekræftelsesdialog

### Plugin-struktur

Hvert plugin ligger som en undermappe i `plugins/` og består af to filer:

```
plugins/
  my_plugin/
    plugin.json      ← metadata (navn, version, forfatter, beskrivelse)
    formulas.json    ← formler med oversættelser
```

**Eksempel på `plugin.json`:**

```json
{
  "id": "my_plugin",
  "enabled": true,
  "version": "1.0",
  "author": "Dit navn",
  "icon": "💰",
  "name": { "en": "Finance Formulas", "da": "Økonomiformler" },
  "description": { "en": "Useful formulas for financial calculations." }
}
```

**Eksempel på `formulas.json`:**

```json
[
  {
    "formula": "=SUM(A1:A10)",
    "name": { "en": "Sum of range", "da": "Sum af område" },
    "description": { "en": "Adds all values in A1:A10." },
    "category": { "en": "Basic", "da": "Grundlæggende" }
  }
]
```

### Vigtig bemærkning (⚠️)

Plugin-manageren indeholder en **⚠️ Important Notice**-knap. Et klik åbner et vindue med alle regler for korrekt oprettelse af plugins (på engelsk). De samme oplysninger findes også i `IMPORTANT_NOTICE.md`.

## 🌐 Flersproget understøttelse

38 sprog er tilgængelige og kan skiftes direkte i appen.  
Nye sprog kan tilføjes via 🌍-knappen med sprogguiden.

**Bemærkning om hindi (हिंदी):** Første gang der skiftes til hindi, installeres skrifttypen *Noto Sans Devanagari* systembredt én gang. Windows vil bede om administratorrettigheder.

## 🔤 RTL-understøttelse (højre mod venstre)

Sprog med skrift fra højre mod venstre genkendes automatisk, og hele grænsefladen spejles:

- **Arabisk (عربي)** – automatisk RTL-genkendelse
- **Hebraisk (עברית)** – automatisk RTL-genkendelse
- **Persisk / Farsi (فارسی)** – automatisk RTL-genkendelse
- **Urdu (اردو)** – automatisk RTL-genkendelse

**Hvad ændres ved RTL:** Hele UI-layoutet spejles, inputfelter bruger RTL-justering, skrifttypen skifter automatisk til en RTL-kompatibel skrifttype (f.eks. *Noto Sans Arabic*, *Noto Sans Hebrew*).

> 💡 **Bemærkning:** De genererede LibreOffice-formler forbliver altid i LTR-syntaks.


## 🗄️ Sikkerhedskopiering og gendannelse

### Opret sikkerhedskopi

Via **Indstillinger → 🗄️ Opret sikkerhedskopi**:

1. **Navn** – valgfri betegnelse (f.eks. `Backup_Mai_2025`)
2. **Adgangskode** – sikkerhedskopien krypteres med AES; uden adgangskoden er gendannelse ikke mulig
3. **Lagringssted** – lokalt eller på et netværksdrev
4. Klik på **💾 Opret sikkerhedskopi** – opretter en `.calc2backup`-fil

**Indhold:** Alle favoritter, indstillinger, teamfavoritter (valgfrit), installerede plugins.

### Gendannelse

Via **Indstillinger → 📂 Gendan sikkerhedskopi**:

1. Vælg sikkerhedskopifil (`.calc2backup`)
2. Indtast adgangskoden
3. Vælg omfang: kun favoritter / kun indstillinger / alt
4. Klik på **🔄 Gendan**

> ⚠️ Ved gendannelse overskrives de eksisterende data. En automatisk sikkerhedskopi af de aktuelle data tilbydes inden gendannelsen.


## 💡 Tips

- `$A$1` → absolut reference (rullemenu ved siden af cellefelterne)

- **Ctrl+S** → gem formel i favoritter

- **Ctrl+C** → kopiér formel (når fokus ikke er i et inputfelt)

- **Ctrl+Z / Ctrl+Y** → fortryd / gentag

- **Ctrl+F12** → minimer / gendan vinduet (virker selv når Calc2 er minimeret)

- **Delete-tasten** i favoritlisten → fjern post

- Formler kan justeres direkte i outputfeltet efter generering

## 📁 Projektstruktur

```
Calc2.py                        ← hovedapplikation
plugin_manager.py               ← plugin-manager
IMPORTANT_NOTICE.md             ← noter om plugin-oprettelse
data/
  README_de.md / README_en.md / ...      ← hjælp pr. sprog
  REFERENZ_de.md / REFERENZ_en.md / ...  ← funktionsreference pr. sprog
language/
  languages.json                ← UI-oversættelser (38 sprog)
  formula_explanations.json
services/
  language_tool.py              ← guide: tilføj nyt sprog
  settings_service.py
  auth_service.py
  favorites_service.py
  network_sync.py
  install_service.py
  backup_service.py             ← sikkerhedskopiering og gendannelse
  json_validator.py             ← kontrol og rettelse af languages.json / formula_explanations.json
plugins/                        ← plugin-mappe (oprettes automatisk)
  my_plugin/
    plugin.json
    formulas.json
fonts/
  NotoSansDevanagari-Regular.ttf  ← hindi-skrifttype
  NotoSansArabic-Regular.ttf      ← arabisk skrifttype (RTL)
  NotoSansHebrew-Regular.ttf      ← hebraisk skrifttype (RTL)
python/                         ← indlejret Python
  python.exe
  ...
settings.json                   ← oprettes automatisk
favoriten.json                  ← lokale favoritter (oprettes automatisk)
```

## 🧠 Tekniske højdepunkter

- **Atomisk filskrivning** → forhindrer beskadigede filer ved lagring

- **Servicearkitektur** → logik og UI er strengt adskilt

- **Automatisk migrering** → gamle favoritformater genkendes og konverteres

- **Robust fejlhåndtering** → beskadigede filer medfører ikke nedbrud

- **Syntaksfremhævning** → formler vises i farver

- **Mørkt tema** → fuldt understøttet

- **Plugin-system** → Calc2 kan udvides med egne formel-plugins

- **RTL-motor** → automatisk genkendelse af RTL-sprog, fuld spejling af UI inkl. passende skrifttyper

- **Sikkerhedskopiering og gendannelse** → AES-krypterede sikkerhedskopier med navn og adgangskode, selektiv gendannelse

- **JSON-validator** → automatisk kontrol og rettelse af `languages.json` og `formula_explanations.json` inkl. landenavne og obligatoriske felter

- **LibreOffice-kilde** → `formula_explanations.json` udfyldes fra den officielle LibreOffice Calc-dokumentation (https://help.libreoffice.org)

- **Global tastaturgenvej** → `Ctrl+F12` virker systembredt via `keyboard`-biblioteket (baggrundstråd)

## Licens

Fri til personlig og kommerciel brug.
