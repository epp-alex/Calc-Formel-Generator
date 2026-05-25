# LibreOffice Calc Formule-assistent

Een Python-tool voor het snel aanmaken, testen en beheren van LibreOffice Calc-formules – met favorieten­systeem, teamsynchronisatie, meertaligheid en plug-inbeheer.

## 🚀 Functies

- 📑 4 tabbladen met meer dan 60 functies

- 🌐 38 talen (inclusief Hindi met automatische lettertype-installatie)

- ⭐ Favorieten­systeem (lokaal en teamsynchronisatie via netwerkschijf)

- 🛠 Beheerpaneel voor teamfavorieten (beveiligd met wachtwoord)

- 📋 Direct kopieerbare formules met syntaxismarkering

- ✏️ Bewerkbaar uitvoerveld met Ongedaan maken/Opnieuw

- 📖 Ingebouwde help en functieverwijzing (per taal)

- 💾 Automatisch opslaan (JSON, atomisch geschreven)

- 🌙 Donkere modus

- 🔌 Plug-inbeheer voor het aanmaken van eigen formule-plug-ins

- 🔤 RTL-ondersteuning (rechts naar links) – automatische herkenning van schrijfrichting

- 🗄️ Back-up en herstel – sla alle instellingen en favorieten op met naam en wachtwoord

- ⌨️ Globale sneltoets `Ctrl+F12` voor minimaliseren/herstellen
- 🔍 JSON-validator – automatische controle en correctie van `languages.json` en `formula_explanations.json`

## 🖥️ Gebruik

**1. Gegevens invoeren**

- Celbereik (bijv. `A1:A10`)

- Cel 1 / Cel 2 (bijv. `A1`, `B1`)

- Optionele parameter (bijv. tekst of index)

- Absolute-verwijzingsmodus instelbaar: `A1`, `$A1`, `A$1`, `$A$1`

**2. Functie selecteren** Kies een tabblad en klik op een functie – de formule wordt direct gegenereerd.

**3. Formule aanpassen** De gegenereerde formule kan direct in het uitvoerveld worden bewerkt.

**4. Kopiëren** Met één klik naar het klembord (inclusief syntaxiskleuren).

**5. Favorieten gebruiken**

- ⭐ Opslaan → huidige formule opslaan (Ctrl+S)

- 📂 Laden → formule hergebruiken

- ❌ Verwijderen → Del-toets of knop

- 🕐 Geschiedenis → recent gebruikte formules

## 📊 Overzicht tabbladen

**Tabblad 1 – Basisfuncties** `+` `-` `\\\*` `/` `^` SUM, AVERAGE, MIN, MAX, MEDIAN, COUNT, COUNTA, SUMPRODUCT

**Tabblad 2 – Geavanceerde functies** IF, AND, OR, NOT SUMIF, COUNTIF, AVERAGEIF, SUMIFS, STDEV, VAR, COUNTBLANK, LARGE

**Tabblad 3 – Datum en tekst** TODAY, NOW, YEAR, MONTH, DAY, DATE, DATEDIF, WEEKDAY CONCATENATE, LEN, LEFT, RIGHT, MID, UPPER, LOWER, TRIM

**Tabblad 4 – Zoeken en afronden** VLOOKUP, HLOOKUP, INDEX, MATCH, INDEX+MATCH ROUND, ROUNDUP, ROUNDDOWN, INT, TRUNC, ABS, MOD, SQRT, RAND


## 📖 Formeluitleg uit de LibreOffice-documentatie

Het bestand `formula_explanations.json` wordt direct gevuld vanuit de **officiële LibreOffice Calc-documentatie** (https://help.libreoffice.org).

### Gegevensbron en updates

- Beschrijvingen, syntaxisinformatie en voorbeelden worden overgenomen van de officiële LibreOffice-helpsite
- Ondersteunde talen zijn afhankelijk van de beschikbare vertalingen op de site
- Het bestand bevat per functie: naam, syntaxis, beschrijving, voorbeeld en categorie
- Toevoegingen of correcties kunnen handmatig worden aangebracht (zie JSON-validator)

### Structuur van `formula_explanations.json`

```json
{
  "SUM": {
    "nl": {
      "syntax": "SUM(Getal1; Getal2; ...)",
      "description": "Telt alle getallen in een celbereik op.",
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

| Veld | Verplicht | Beschrijving |
|------|----------|-------------|
| `syntax` | ✅ | Formelsyntaxis met parameters |
| `description` | ✅ | Korte beschrijving van de functie |
| `example` | ✅ | Gebruiksvoorbeeld als kant-en-klare formule |
| `note` | ❌ | Optionele noot |

> 💡 **Opmerking:** Als er geen vermelding voor een taal bestaat, valt de app automatisch terug op de Engelstalige versie.

---

## 🔍 JSON-validator voor taalbestanden

De ingebouwde **JSON-validator** controleert en corrigeert `languages.json` en `formula_explanations.json` op consistentie, volledigheid en correcte landsnamen. Toegankelijk via **Instellingen → 🔍 JSON-validator**.

### Wat wordt gecontroleerd?

#### `languages.json`

- ✅ Alle 38 talen aanwezig (op ISO 639-1 taalcode)
- ✅ Correcte **land- en taalnamen** (bijv. `"nl"` → `"Nederlands"`)
- ✅ Geen dubbele taalcodes
- ✅ Verplichte velden aanwezig: `name`, `native_name`, `flag`, `rtl`
- ✅ RTL-vlag correct ingesteld (Arabisch, Hebreeuws, Perzisch, Urdu → `"rtl": true`)

#### `formula_explanations.json`

- ✅ Alle functies van de 4 tabbladen geregistreerd
- ✅ Verplichte velden aanwezig: `syntax`, `description`, `example`
- ✅ Geen lege velden (`""` of `null`)
- ✅ Taalcodes komen overeen met `languages.json`

### Correctiefuncties

| Fouttype | Automatische correctie |
|---------|----------------------|
| Onjuiste landsnaam | Vervangen door de juiste naam volgens ISO |
| Ontbrekende taalvermelding | Aangevuld met Engelstalige reserve |
| Leeg verplicht veld | Gemarkeerd als `"[MISSING]"` voor handmatige controle |
| Dubbele vermelding | Duplicaten verwijderd, meest complete vermelding behouden |
| Onjuiste RTL-vlag | Automatisch gecorrigeerd op basis van bekende RTL-codes |

### Gebruik

1. Open **Instellingen → 🔍 JSON-validator**
2. Selecteer bestand: `languages.json` of `formula_explanations.json` (of beide)
3. **🔎 Controleren** – toont alle gevonden problemen
4. **🛠 Automatisch corrigeren** – lost alle automatisch oplosbare fouten op
5. **💾 Opslaan** – schrijft het gecorrigeerde bestand atomisch terug
6. **📋 Rapport exporteren** (optioneel) – slaat een tekstbestand op met alle bevindingen

> ⚠️ **Opmerking:** Voor elke automatische correctie wordt een back-up van het oorspronkelijke bestand aangemaakt (`languages.json.bak` / `formula_explanations.json.bak`).

## ⭐ Favorieten­systeem

- Eigen formules opslaan en hergebruiken

- Scheiding tussen persoonlijke en teamfavorieten

- Teamfavorieten zijn alleen-lezen (alleen de beheerder kan ze bewerken)

- Dubbele vermeldingen worden voorkomen

- Vrije sortering van persoonlijke favorieten

- Synchronisatie via netwerkschijf (optioneel instelbaar)

### Teamsynchronisatie

Via **Instellingen → 🌐 Netwerkpad** kan een netwerkschijf worden ingevoerd (bijv. `\\\\\\\\Server\\\\Gedeeld\\\\formules`).

- Bij opstarten: netwerkfavorieten worden lokaal opgeslagen (offline reservekopie)

- Bij opslaan: eigen formules worden naar het netwerk geschreven, teamformules blijven onaangeroerd

## 🛠 Beheerpaneel

Toegankelijk via de 🛠-knop. Bij de eerste klik wordt een wachtwoord ingesteld (PBKDF2-SHA256, alleen de hash wordt opgeslagen).

- Teamformules toevoegen, bewerken en verwijderen

- Wachtwoord wijzigen

- Wijzigingen worden direct naar de netwerkschijf geschreven

## 🔌 Plug-inbeheer

De plug-inbeheer (`plugin\_manager.py`) is een zelfstandige tool voor het aanmaken en beheren van eigen formule-plug-ins voor Calc2. Deze bevindt zich in dezelfde map als `Calc2.py` en wordt gestart via de 🔌-knop in Calc2.py:

### Functies

- **Nieuwe plug-in aanmaken** – stapsgewijze wizard (naam, formules, vertalingen, samenvatting)

- **Formules toevoegen** – een bestaande plug-in aanvullen met formules

- **Vertalingen bewerken** – formulenamen vertalen naar alle 38 talen

- **Plug-inmap openen** – direct in de bestandsbeheer

- **Plug-in verwijderen** – met beveiligingsbevestiging

### Plug-instructuur

Elke plug-in bevindt zich als submap in `plugins/` en bestaat uit twee bestanden:

```
`plugins/`

`  mijn\_plugin/`

`    plugin.json      ← metadata (naam, versie, auteur, beschrijving)`

`    formulas.json    ← formules met vertalingen`
```

**Voorbeeld `plugin.json`:**

```
`\{`

`  "id": "mijn\_plugin",`

`  "enabled": true,`

`  "version": "1.0",`

`  "author": "Uw Naam",`

`  "icon": "💰",`

`  "name": \{ "en": "Finance Formulas", "nl": "Financiële formules" \},`

`  "description": \{ "en": "Useful formulas for financial calculations." \}`

`\}`
```

**Voorbeeld `formulas.json`:**

```
`\[`

`  \{`

`    "formula": "=SUM(A1:A10)",`

`    "name": \{ "en": "Sum of range", "nl": "Som van bereik" \},`

`    "description": \{ "en": "Adds all values in A1:A10." \},`

`    "category": \{ "en": "Basic", "nl": "Basis" \}`

`  \}`

`\]`
```

### Belangrijke mededeling (⚠️ Important Notice)

In de plug-inbeheer bevindt zich de knop **⚠️ Important Notice**. Een klik opent een venster met alle regels voor het correct aanmaken van plug-ins in het Engels. Dezelfde informatie is ook te vinden in `IMPORTANT\_NOTICE.md`.

## 🌐 Meertaligheid

38 talen beschikbaar, direct in de app te wisselen. Nieuwe talen kunnen worden toegevoegd via de 🌍-knop met de taalwizard.

**Opmerking over Hindi (हिंदी):** Bij het eerste overschakelen naar Hindi wordt het lettertype *Noto Sans Devanagari* eenmalig op systeemniveau geïnstalleerd. Windows vraagt om beheerdersrechten.

## 🔤 RTL-ondersteuning (rechts naar links)

Talen met schrift van rechts naar links worden automatisch herkend en de volledige interface wordt gespiegeld:

- **Arabisch (عربي)** – automatische RTL-herkenning
- **Hebreeuws (עברית)** – automatische RTL-herkenning
- **Perzisch / Farsi (فارسی)** – automatische RTL-herkenning
- **Urdu (اردو)** – automatische RTL-herkenning

**Wat verandert in RTL-modus:** De volledige UI-indeling wordt gespiegeld, invoervelden gebruiken RTL-uitlijning, het lettertype wisselt automatisch naar een RTL-compatibel lettertype (bijv. *Noto Sans Arabic*, *Noto Sans Hebrew*).

> 💡 **Opmerking:** Gegenereerde LibreOffice-formules blijven altijd in LTR-syntaxis – alleen de gebruikersinterface verandert van richting.


## 🗄️ Back-up en herstel

### Back-up maken

Via **Instellingen → 🗄️ Back-up maken**:

1. **Naam** – vrij te kiezen label (bijv. `Backup_Mei_2025`)
2. **Wachtwoord** – de back-up wordt AES-versleuteld; zonder wachtwoord is herstel niet mogelijk
3. **Opslaglocatie** – lokaal of op een netwerkschijf
4. Klik op **💾 Back-up maken** – er wordt een `.calc2backup`-bestand aangemaakt

**Inhoud:** Alle favorieten, instellingen, teamfavorieten (optioneel), geïnstalleerde plug-ins.

### Back-up herstellen

Via **Instellingen → 📂 Back-up herstellen**:

1. Selecteer het back-upbestand (`.calc2backup`)
2. Voer het wachtwoord in
3. Kies het herstelbereik: alleen favorieten / alleen instellingen / alles
4. Klik op **🔄 Herstellen**

> ⚠️ Bij herstel worden de bestaande gegevens overschreven. Vooraf wordt een automatische back-up van de huidige gegevens aangeboden.


## 💡 Tips

- `$A$1` → absolute verwijzing (vervolgkeuzelijst naast de celvelden)

- **Ctrl+S** → formule opslaan in favorieten

- **Ctrl+C** → formule kopiëren (buiten invoervelden)

- **Ctrl+Z / Ctrl+Y** → Ongedaan maken / Opnieuw

- **Ctrl+F12** → venster minimaliseren/herstellen (werkt ook wanneer Calc2 geminimaliseerd is)

- **Del-toets** in de favorietenlijst → vermelding verwijderen

- Formules kunnen na het genereren direct in het uitvoerveld worden aangepast

## 📁 Projectstructuur

```
`Calc2.py                        ← hoofdprogramma`

`plugin\_manager.py               ← plug-inbeheer`

`IMPORTANT\_NOTICE.md             ← instructies voor het aanmaken van plug-ins`

`data/`

`  README\_nl.md / README\_en.md / ...      ← help per taal`

`  VERWIJZING\_nl.md / VERWIJZING\_en.md / ... ← functieverwijzing per taal`

`language/`

`  languages.json                ← vertalingen van de interface (38 talen)`

`  formula\_explanations.json`

`services/`

`  language\_tool.py              ← wizard: nieuwe taal toevoegen`

`  settings\_service.py`

`  auth\_service.py`

`  favorites\_service.py`

`  network\_sync.py`

`  install\_service.py`

`  json_validator.py             ← controle en correctie van languages.json / formula_explanations.json`

`plugins/                        ← plug-inmap (automatisch aangemaakt)`

`  mijn\_plugin/`

`    plugin.json`

`    formulas.json`

`fonts/`

`  NotoSansDevanagari-Regular.ttf  ← Hindi-lettertype
  NotoSansArabic-Regular.ttf      ← Arabisch lettertype (RTL)
  NotoSansHebrew-Regular.ttf      ← Hebreeuws lettertype (RTL)`

`python/                         ← ingebedde Python`

`  python.exe`

`  ...`

`settings.json                   ← wordt automatisch aangemaakt`

`favorieten.json                 ← lokale favorieten (wordt automatisch aangemaakt)`
```

## 🧠 Technische hoogtepunten

- **Atomisch bestanden schrijven** → voorkomt beschadiging van bestanden bij opslaan

- **Service-architectuur** → logica en gebruikersinterface strikt gescheiden

- **Automatische migratie** → oude favorietenformaten worden herkend en geconverteerd

- **Robuuste foutafhandeling** → beschadigde bestanden veroorzaken geen programmacrash

- **Syntaxismarkering** → formules worden in kleur weergegeven

- **Donkere modus** → volledig ondersteund

- **Plug-insysteem** → Calc2 is uitbreidbaar met eigen formule-plug-ins

- **RTL-motor** → automatische herkenning van RTL-talen, volledige UI-spiegeling incl. bijpassende lettertypes

- **Back-up en herstel** → AES-versleutelde back-ups met naam en wachtwoord, selectief herstel

- **JSON-validator** → automatische controle en correctie van `languages.json` en `formula_explanations.json` incl. landsnamen en verplichte velden

- **LibreOffice-bron** → `formula_explanations.json` wordt gevuld vanuit de officiële LibreOffice Calc-documentatie (https://help.libreoffice.org)

- **Globale sneltoets** → `Ctrl+F12` werkt systeembreed via de `keyboard`-bibliotheek (achtergrondthread)

## Licentie

Vrij te gebruiken voor persoonlijke en commerciële doeleinden.

