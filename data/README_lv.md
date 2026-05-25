# LibreOffice Calc Formulu Palīgs

Python rīks LibreOffice Calc formulu ātrai izveidei, testēšanai un pārvaldībai – ar izlases sistēmu, komandas sinhronizāciju, daudzvalodību un spraudņu pārvaldnieku.

## 🚀 Funkcijas

- 📑 4 cilnes ar vairāk nekā 60 funkcijām

- 🌐 38 valodas (ieskaitot hindi ar automātisku fonta instalēšanu)

- ⭐ Izlases sistēma (lokāla un komandas sinhronizācija caur tīkla disku)

- 🛠 Administrēšanas panelis komandas izlasei (aizsargāts ar paroli)

- 📋 Tieši kopējamas formulas ar sintakses izcelšanu

- ✏️ Rediģējams izvades lauks ar Atsaukt/Atcelt atsaukšanu

- 📖 Iebūvēta palīdzība un funkciju uzziņa (katrai valodai)

- 💾 Automātiska saglabāšana (JSON, atomiska rakstīšana)

- 🌙 Tumšais režīms

- 🔌 Spraudņu pārvaldnieks pašu formulu spraudņu izveidei

- 🔤 RTL atbalsts (no labās uz kreiso) – rakstīšanas virziena automātiska noteikšana

- 🗄️ Dublējums un atjaunošana – saglabājiet visus iestatījumus un izlasi ar nosaukumu un paroli

- ⌨️ Globālais īsinājumtaustiņš `Ctrl+F12` minimizēšanai/atjaunošanai
- 🔍 JSON validētājs – automātiska `languages.json` un `formula_explanations.json` pārbaude un labošana

## 🖥️ Lietošana

**1. Datu ievade**

- Šūnu diapazons (piem. `A1:A10`)

- Šūna 1 / Šūna 2 (piem. `A1`, `B1`)

- Neobligāts parametrs (piem. teksts vai indekss)

- Izvēlams absolūtās atsauces režīms: `A1`, `$A1`, `A$1`, `$A$1`

**2. Funkcijas izvēle** Izvēlieties cilni un noklikšķiniet uz funkcijas – formula tiek ģenerēta uzreiz.

**3. Formulas pielāgošana** Ģenerēto formulu var tieši rediģēt izvades laukā.

**4. Kopēšana** Ar vienu klikšķi uz starpliktuvi (ieskaitot sintakses krāsas).

**5. Izlases izmantošana**

- ⭐ Saglabāt → saglabāt pašreizējo formulu (Ctrl+S)

- 📂 Ielādēt → atkārtoti izmantot formulu

- ❌ Dzēst → taustiņš Del vai poga

- 🕐 Vēsture → nesen izmantotās formulas

## 📊 Ciļņu pārskats

**1. cilne – Pamata funkcijas** `+` `-` `\*` `/` `^` SUM, AVERAGE, MIN, MAX, MEDIAN, COUNT, COUNTA, SUMPRODUCT

**2. cilne – Papildu funkcijas** IF, AND, OR, NOT SUMIF, COUNTIF, AVERAGEIF, SUMIFS, STDEV, VAR, COUNTBLANK, LARGE

**3. cilne – Datums un teksts** TODAY, NOW, YEAR, MONTH, DAY, DATE, DATEDIF, WEEKDAY CONCATENATE, LEN, LEFT, RIGHT, MID, UPPER, LOWER, TRIM

**4. cilne – Meklēšana un noapaļošana** VLOOKUP, HLOOKUP, INDEX, MATCH, INDEX+MATCH ROUND, ROUNDUP, ROUNDDOWN, INT, TRUNC, ABS, MOD, SQRT, RAND


## 📖 Formulu paskaidrojumi no LibreOffice dokumentācijas

Fails `formula_explanations.json` tiek aizpildīts tieši no **LibreOffice Calc oficiālās dokumentācijas** (https://help.libreoffice.org).

### Datu avots un atjaunināšana

- Apraksti, sintakses informācija un piemēri tiek ņemti no LibreOffice oficiālās palīdzības vietnes
- Atbalstītās valodas ir atkarīgas no vietnē pieejamajiem tulkojumiem
- Fails katrai funkcijai satur: nosaukumu, sintaksi, aprakstu, piemēru un kategoriju
- Papildinājumus vai labojumus var veikt manuāli (skatīt JSON validētājs)

### `formula_explanations.json` struktūra

```json
{
  "SUM": {
    "lv": {
      "syntax": "SUM(Skaitlis1; Skaitlis2; ...)",
      "description": "Saskaita visus skaitļus šūnu diapazonā.",
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

| Lauks | Obligāts | Apraksts |
|-------|---------|---------|
| `syntax` | ✅ | Formulas sintakse ar parametriem |
| `description` | ✅ | Īss funkcijas apraksts |
| `example` | ✅ | Lietošanas piemērs kā gatava formula |
| `note` | ❌ | Neobligāta piezīme |

> 💡 **Piezīme:** Ja valodai nav ieraksta, lietotne automātiski atgriežas pie angļu valodas versijas.

---

## 🔍 JSON validētājs valodu failiem

Integrētais **JSON validētājs** pārbauda un labo `languages.json` un `formula_explanations.json` konsekvenci, pilnīgumu un pareizos valstu nosaukumus. Pieejams caur **Iestatījumi → 🔍 JSON validētājs**.

### Kas tiek pārbaudīts?

#### `languages.json`

- ✅ Visas 38 valodas ir klāt (pēc ISO 639-1 valodas koda)
- ✅ Pareizi **valstu un valodu nosaukumi** (piem. `"lv"` → `"Latviešu"`)
- ✅ Nav dublētu valodu kodu
- ✅ Obligātie lauki ir klāt: `name`, `native_name`, `flag`, `rtl`
- ✅ RTL karodziņš pareizi iestatīts (Arābu, Ivritu, Persiešu, Urdu → `"rtl": true`)

#### `formula_explanations.json`

- ✅ Visas 4 ciļņu funkcijas reģistrētas
- ✅ Obligātie lauki ir klāt: `syntax`, `description`, `example`
- ✅ Nav tukšu lauku (`""` vai `null`)
- ✅ Valodu kodi atbilst `languages.json`

### Labošanas funkcijas

| Kļūdas veids | Automātiskā labošana |
|-------------|---------------------|
| Nepareizs valsts nosaukums | Aizstāts ar pareizo nosaukumu pēc ISO standarta |
| Trūkstošs valodas ieraksts | Aizpildīts ar angļu valodas rezerves versiju |
| Tukšs obligātais lauks | Atzīmēts kā `"[MISSING]"` manuālai pārbaudei |
| Dublēts ieraksts | Dublāti noņemti, pilnīgāks ieraksts saglabāts |
| Nepareizs RTL karodziņš | Automātiski labots, pamatojoties uz zināmiem RTL kodiem |

### Lietošana

1. Atveriet **Iestatījumi → 🔍 JSON validētājs**
2. Izvēlieties failu: `languages.json` vai `formula_explanations.json` (vai abus)
3. **🔎 Pārbaudīt** – rāda visas atrastās problēmas
4. **🛠 Automātiski labot** – labo visas automātiski labojamās kļūdas
5. **💾 Saglabāt** – atomiski ieraksta laboto failu
6. **📋 Eksportēt pārskatu** (neobligāti) – saglabā teksta failu ar visiem atradumiem

> ⚠️ **Piezīme:** Pirms katras automātiskās labošanas tiek izveidota sākotnējā faila dublējumkopija (`languages.json.bak` / `formula_explanations.json.bak`).

## ⭐ Izlases sistēma

- Pašu formulu saglabāšana un atkārtota izmantošana

- Personīgās izlases un komandas izlases atdalīšana

- Komandas izlase ir tikai lasāma (tikai administrators var rediģēt)

- Dublikāti tiek novērsti

- Brīva personīgās izlases kārtošana

- Sinhronizācija caur tīkla disku (pēc izvēles konfigurējama)

### Komandas sinhronizācija

Caur **Iestatījumi → 🌐 Tīkla ceļš** var ievadīt tīkla disku (piem. `\\\\Serveris\\Koplietošana\\formulas`).

- Startējot: tīkla izlase tiek saglabāta lokāli (bezsaistes rezerves kopija)

- Saglabājot: pašu formulas tiek rakstītas tīklā, komandas formulas paliek neskartas

## 🛠 Administrēšanas panelis

Pieejams caur 🛠 pogu. Pirmajā klikšķī tiek iestatīta parole (PBKDF2-SHA256, tiek saglabāts tikai jaukteņkods).

- Komandas formulu pievienošana, rediģēšana un dzēšana

- Paroles maiņa

- Izmaiņas tiek tieši rakstītas uz tīkla disku

## 🔌 Spraudņu pārvaldnieks

Spraudņu pārvaldnieks (`plugin_manager.py`) ir patstāvīgs rīks pašu formulu spraudņu izveidei un pārvaldībai Calc2. Tas atrodas tajā pašā mapē kā `Calc2.py` un tiek palaists ar 🔌 pogu Calc2.py:

### Funkcijas

- **Jauna spraudņa izveide** – soli pa solim vednis (nosaukums, formulas, tulkojumi, kopsavilkums)

- **Formulu pievienošana** – formulu papildināšana esošam spraudnim

- **Tulkojumu rediģēšana** – formulu nosaukumu tulkošana visās 38 valodās

- **Spraudņu mapes atvēršana** – tieši failu pārvaldniekā

- **Spraudņa dzēšana** – ar drošības apstiprinājumu

### Spraudņa struktūra

Katrs spraudnis atrodas kā apakšmape `plugins/` direktorijā un sastāv no diviem failiem:

```
plugins/
  mans_sprudnis/
    plugin.json      ← metadati (nosaukums, versija, autors, apraksts)
    formulas.json    ← formulas ar tulkojumiem
```

**Piemērs `plugin.json`:**

```
{
  "id": "mans_sprudnis",
  "enabled": true,
  "version": "1.0",
  "author": "Jūsu Vārds",
  "icon": "💰",
  "name": { "en": "Finance Formulas", "lv": "Finanšu formulas" },
  "description": { "en": "Useful formulas for financial calculations." }
}
```

**Piemērs `formulas.json`:**

```
[
  {
    "formula": "=SUM(A1:A10)",
    "name": { "en": "Sum of range", "lv": "Diapazona summa" },
    "description": { "en": "Adds all values in A1:A10." },
    "category": { "en": "Basic", "lv": "Pamata" }
  }
]
```

### Svarīgs paziņojums (⚠️ Important Notice)

Spraudņu pārvaldniekā ir poga **⚠️ Important Notice**. Noklikšķinot tiek atvērts logs ar visiem noteikumiem pareizai spraudņu izveidei angļu valodā. Tā pati informācija ir pieejama arī failā `IMPORTANT_NOTICE.md`.

## 🌐 Daudzvalodība

Pieejamas 38 valodas, maināmas tieši lietotnē.
Jaunas valodas var pievienot caur 🌍 pogu ar valodas vedni.

**Piezīme par hindi (हिंदी):** Pirmo reizi pārslēdzoties uz hindi, fonts *Noto Sans Devanagari* tiek instalēts vienu reizi sistēmas līmenī. Windows pieprasīs administratora tiesības.

## 🔤 RTL atbalsts (no labās uz kreiso)

Valodas ar rakstīšanu no labās uz kreiso tiek automātiski noteiktas un visa saskarne tiek spoguļota:

- **Arābu (عربي)** – automātiska RTL noteikšana
- **Ivrits (עברית)** – automātiska RTL noteikšana
- **Persiešu / Farsi (فارسی)** – automātiska RTL noteikšana
- **Urdu (اردو)** – automātiska RTL noteikšana

**Kas mainās RTL režīmā:** Visa UI izkārtojums tiek spoguļots, ievades lauki izmanto RTL izlīdzinājumu, fonts automātiski mainās uz RTL saderīgu (piem. *Noto Sans Arabic*, *Noto Sans Hebrew*).

> 💡 **Piezīme:** Ģenerētās LibreOffice formulas vienmēr paliek LTR sintaksē – mainās tikai lietotāja saskarnes virziens.


## 🗄️ Dublējums un atjaunošana

### Dublējuma izveide

Caur **Iestatījumi → 🗄️ Izveidot dublējumu**:

1. **Nosaukums** – brīvs apraksts (piem. `Dublejs_Maijs_2025`)
2. **Parole** – dublējums tiek šifrēts ar AES; bez tās atjaunošana nav iespējama
3. **Saglabāšanas vieta** – lokāla vai tīkla disks
4. Noklikšķiniet uz **💾 Izveidot dublējumu** – tiek izveidots `.calc2backup` fails

**Saturs:** Visa izlase, iestatījumi, komandas izlase (pēc izvēles), instalētie spraudņi.

### Dublējuma atjaunošana

Caur **Iestatījumi → 📂 Atjaunot dublējumu**:

1. Izvēlieties failu (`.calc2backup`)
2. Ievadiet paroli
3. Izvēlieties apjomu: tikai izlase / tikai iestatījumi / viss
4. Noklikšķiniet uz **🔄 Atjaunot**

> ⚠️ Atjaunošanas laikā esošie dati tiek pārrakstīti. Pirms atjaunošanas tiek piedāvāts automātisks pašreizējo datu dublējums.


## 💡 Padomi

- `$A$1` → absolūtā atsauce (nolaižamā izvēlne blakus šūnu laukiem)

- **Ctrl+S** → saglabāt formulu izlasē

- **Ctrl+C** → kopēt formulu (ārpus ievades laukiem)

- **Ctrl+Z / Ctrl+Y** → Atsaukt / Atcelt atsaukšanu

- **Ctrl+F12** → minimizēt/atjaunot logu (darbojas arī tad, ja Calc2 ir minimizēts)

- **Taustiņš Del** izlases sarakstā → ieraksta dzēšana

- Formulas var pielāgot tieši izvades laukā pēc ģenerēšanas

## 📁 Projekta struktūra

```
Calc2.py                        ← galvenā programma
plugin_manager.py               ← spraudņu pārvaldnieks
IMPORTANT_NOTICE.md             ← norādījumi spraudņu izveidei
data/
  README_lv.md / README_en.md / ...      ← palīdzība katrai valodai
  UZZIŅA_lv.md / UZZIŅA_en.md / ...     ← funkciju uzziņa katrai valodai
language/
  languages.json                ← saskarnes tulkojumi (38 valodas)
  formula_explanations.json
services/
  language_tool.py              ← vednis: jaunas valodas pievienošana
  settings_service.py
  auth_service.py
  favorites_service.py
  network_sync.py
  install_service.py
  backup_service.py             ← dublējums un atjaunošana
  json_validator.py             ← languages.json / formula_explanations.json pārbaude un labošana
plugins/                        ← spraudņu mape (izveidota automātiski)
  mans_sprudnis/
    plugin.json
    formulas.json
fonts/
  NotoSansDevanagari-Regular.ttf  ← hindi fonts
  NotoSansArabic-Regular.ttf      ← arābu fonts (RTL)
  NotoSansHebrew-Regular.ttf      ← ivritu fonts (RTL)
python/                         ← iegultais Python
  python.exe
  ...
settings.json                   ← izveidots automātiski
izlase.json                     ← lokālā izlase (izveidots automātiski)
```

## 🧠 Tehniskie akcenti

- **Atomiska failu rakstīšana** → novērš failu bojājumus saglabāšanas laikā

- **Servisu arhitektūra** → loģika un lietotāja saskarne strikti atdalītas

- **Automātiska migrācija** → vecie izlases formāti tiek atpazīti un konvertēti

- **Robusta kļūdu apstrāde** → bojāti faili neizraisa lietotnes avāriju

- **Sintakses izcelšana** → formulas tiek attēlotas krāsaini

- **Tumšais režīms** → pilnībā atbalstīts

- **Spraudņu sistēma** → Calc2 var paplašināt ar pašu formulu spraudņiem

- **RTL dzinējs** → RTL valodu automātiska noteikšana, pilnīga UI spoguļošana ar atbilstošiem fontiem

- **Dublējums un atjaunošana** → AES šifrēti dublējumi ar nosaukumu un paroli, selektīva atjaunošana

- **JSON validētājs** → automātiska `languages.json` un `formula_explanations.json` pārbaude un labošana, ieskaitot valstu nosaukumus un obligātos laukus

- **LibreOffice avots** → `formula_explanations.json` tiek aizpildīts no LibreOffice Calc oficiālās dokumentācijas (https://help.libreoffice.org)

- **Globālais īsinājumtaustiņš** → `Ctrl+F12` darbojas sistēmas līmenī caur `keyboard` bibliotēku (fona pavediens)

## Licence

Brīvi izmantojams personīgiem un komerciāliem mērķiem.
