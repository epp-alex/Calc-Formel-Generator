# LibreOffice Calc Valemite Abivahend

Python-tööriist LibreOffice Calc valemite kiireks loomiseks, testimiseks ja haldamiseks – lemmikute süsteemi, meeskonna sünkroniseerimise, mitmekeelsuse ja pluginate halduriga.

## 🚀 Funktsioonid

- 📑 4 vahekaarti üle 60 funktsiooniga

- 🌐 38 keelt (sh hindi koos automaatse fontide installimisega)

- ⭐ Lemmikute süsteem (kohalik ja meeskonna sünkroniseerimine võrgudraivi kaudu)

- 🛠 Adminipaneel meeskonna lemmikute jaoks (parooliga kaitstud)

- 📋 Otse kopeeritavad valemid koos süntaksi esiletõstmisega

- ✏️ Muudetav väljundväli Undo/Redo toega

- 📖 Sisseehitatud abi ja funktsioonide viide (keele kaupa)

- 💾 Automaatne salvestamine (JSON, aatomiliselt kirjutatud)

- 🌙 Tume režiim

- 🔌 Pluginate haldur omaenda valemipluginite loomiseks

- 🔤 RTL-tugi (paremalt vasakule) – kirjutamissuuna automaatne tuvastamine

- 🗄️ Varundamine ja taastamine – kõigi seadete ja lemmikute salvestamine nime ja parooliga

- ⌨️ Globaalne kiirklahv `Ctrl+F12` minimeerimiseks/taastamiseks
- 🔍 JSON validaator – `languages.json` ja `formula_explanations.json` automaatne kontrollimine ja parandamine

## 🖥️ Kasutamine

**1. Sisesta andmed**

- Lahtrivahemik (nt `A1:A10`)

- Lahter 1 / Lahter 2 (nt `A1`, `B1`)

- Valikuline parameeter (nt tekst või indeks)

- Absoluutviite režiim on valitav: `A1`, `$A1`, `A$1`, `$A$1`

**2. Vali funktsioon** Vali vahekaart ja klõpsa funktsioonil – valem genereeritakse kohe.

**3. Kohanda valemit** Genereeritud valemit saab otse väljundväljas muuta.

**4. Kopeeri** Ühe klõpsuga lõikelauale (koos süntaksi värvidega).

**5. Kasuta lemmikuid**

- ⭐ Salvesta → salvesta praegune valem (Ctrl+S)

- 📂 Laadi → kasuta valemit uuesti

- ❌ Kustuta → Delete-klahv või nupp

- 🕐 Ajalugu → hiljuti kasutatud valemid

## 📊 Vahelehtede ülevaade

**Vahekaart 1 – Põhifunktsioonid** `+` `-` `\*` `/` `^` SUM, AVERAGE, MIN, MAX, MEDIAN, COUNT, COUNTA, SUMPRODUCT

**Vahekaart 2 – Täiustatud funktsioonid** IF, AND, OR, NOT SUMIF, COUNTIF, AVERAGEIF, SUMIFS, STDEV, VAR, COUNTBLANK, LARGE

**Vahekaart 3 – Kuupäev ja tekst** TODAY, NOW, YEAR, MONTH, DAY, DATE, DATEDIF, WEEKDAY CONCATENATE, LEN, LEFT, RIGHT, MID, UPPER, LOWER, TRIM

**Vahekaart 4 – Otsimine ja ümardamine** VLOOKUP, HLOOKUP, INDEX, MATCH, INDEX+MATCH ROUND, ROUNDUP, ROUNDDOWN, INT, TRUNC, ABS, MOD, SQRT, RAND


## 📖 Valemite selgitused LibreOffice dokumentatsioonist

Fail `formula_explanations.json` täidetakse otse **LibreOffice Calc ametlikust dokumentatsioonist** (https://help.libreoffice.org).

### Andmeallikas ja uuendamine

- Kirjeldused, süntaksiteave ja näited pärinevad LibreOffice ametlikult abisaidilt
- Toetatud keeled sõltuvad saidil saadaolevatest tõlgetest
- Fail sisaldab iga funktsiooni kohta: nime, süntaksit, kirjeldust, näidet ja kategooriat
- Täiendusi või parandusi saab teha käsitsi (vt JSON validaator)

### `formula_explanations.json` struktuur

```json
{
  "SUM": {
    "et": {
      "syntax": "SUM(Arv1; Arv2; ...)",
      "description": "Liidab kõik arvud lahtrivahemikus.",
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

| Väli | Kohustuslik | Kirjeldus |
|------|------------|-----------|
| `syntax` | ✅ | Valemi süntaks koos parameetritega |
| `description` | ✅ | Funktsiooni lühikirjeldus |
| `example` | ✅ | Kasutusnäide valmis valemina |
| `note` | ❌ | Valikuline märkus |

> 💡 **Märkus:** Kui keele jaoks kirjet ei leidu, kasutab rakendus automaatselt ingliskeelset versiooni.

---

## 🔍 JSON validaator keelefailide jaoks

Integreeritud **JSON validaator** kontrollib ja parandab `languages.json` ja `formula_explanations.json` faile järjepidevuse, täielikkuse ja riikide nimede õigsuse osas.

Ligipääsetav: **Seaded → 🔍 JSON validaator**.

### Mida kontrollitakse?

#### `languages.json`

- ✅ Kõik 38 keelt on olemas (ISO 639-1 keelekoodi järgi)
- ✅ Õiged **riikide ja keelte nimed** (nt `"et"` → `"Eesti"`)
- ✅ Keelekoodide duplikaate pole
- ✅ Kohustuslikud väljad on olemas: `name`, `native_name`, `flag`, `rtl`
- ✅ RTL-lipp on õigesti seatud (Araabia, Heebrea, Pärsia, Urdu → `"rtl": true`)

#### `formula_explanations.json`

- ✅ Kõik funktsioonid 4 vahekaardilt on kirjas
- ✅ Kohustuslikud väljad on olemas: `syntax`, `description`, `example`
- ✅ Tühjasid välju pole (`""` ega `null`)
- ✅ Keelekoodid vastavad `languages.json` omadele

### Parandamise funktsioonid

| Veatüüp | Automaatne parandus |
|---------|---------------------|
| Vale riigi nimi | Asendatakse ISO standardi kohase õige nimega |
| Puuduv keelekirje | Täidetakse ingliskeelse varuga |
| Tühi kohustuslik väli | Märgitakse `"[MISSING]"` käsitsi ülevaatamiseks |
| Duplikaatkirje | Duplikaadid eemaldatakse, täielikum kirje säilitatakse |
| Vale RTL-lipp | Parandatakse automaatselt teadaolevate RTL-koodide alusel |

### Kasutamine

1. Ava **Seaded → 🔍 JSON validaator**
2. Vali fail: `languages.json` või `formula_explanations.json` (või mõlemad)
3. **🔎 Kontrolli** – kuvab kõik leitud probleemid
4. **🛠 Paranda automaatselt** – lahendab kõik automaatselt lahendatavad vead
5. **💾 Salvesta** – kirjutab parandatud faili aatomilistelt
6. **📋 Ekspordi aruanne** (valikuline) – salvestab tekstifaili kõigi leidudega

> ⚠️ **Märkus:** Enne iga automaatset parandust luuakse algse faili varukoopia (`languages.json.bak` / `formula_explanations.json.bak`).

## ⭐ Lemmikute süsteem

- Salvesta ja kasuta uuesti omaenda valemeid

- Eraldi isiklikud ja meeskonna lemmikud

- Meeskonna lemmikud on kirjutuskaitstud (ainult admin saab muuta)

- Topeltkirjeid ei lubata

- Isiklike lemmikute vaba sortimine

- Sünkroniseerimine võrgudraivi kaudu (valikuliselt seadistatav)

### Meeskonna sünkroniseerimine

**Seaded → 🌐 Võrgutee** kaudu saab sisestada võrgudraivi (nt `\\\\Server\\Jagamine\\valemid`).

- Käivitamisel: võrgulemmikud salvestatakse kohalikult (võrguühenduseta varukoopia)

- Salvestamisel: isiklikud valemid kirjutatakse võrku, meeskonna valemeid ei puututa

## 🛠 Adminipaneel

Ligipääsetav 🛠-nupu kaudu. Esimesel klõpsul määratakse parool (PBKDF2-SHA256, salvestatakse ainult räsi).

- Meeskonna valemite lisamine, muutmine, kustutamine

- Parooli vahetamine

- Muudatused kirjutatakse otse võrgudraivi

## 🔌 Pluginate haldur

Pluginate haldur (`plugin_manager.py`) on eraldiseisev tööriist omaenda valemipluginite loomiseks ja haldamiseks Calc2 jaoks. See asub samas kaustas kui `Calc2.py` ja käivitatakse 🔌-nupuga rakenduses Calc2.py:

### Funktsioonid

- **Loo uus plugin** – samm-sammulise nõustajaga (nimi, valemid, tõlked, kokkuvõte)

- **Lisa valemeid** – täienda olemasolevat pluginat uute valemitega

- **Muuda tõlkeid** – tõlgi valemite nimetused kõikidesse 38 keelde

- **Ava pluginate kaust** – otse failihalduris

- **Kustuta plugin** – koos kinnitusküsimusega

### Plugina struktuur

Iga plugin asub alamkaustas `plugins/` ja koosneb kahest failist:

```
plugins/
  minu_plugin/
    plugin.json      ← metaandmed (nimi, versioon, autor, kirjeldus)
    formulas.json    ← valemid koos tõlgetega
```

**Näide `plugin.json`:**

```
{
  "id": "minu_plugin",
  "enabled": true,
  "version": "1.0",
  "author": "Sinu Nimi",
  "icon": "💰",
  "name": { "en": "Finance Formulas", "et": "Finantsvalemid" },
  "description": { "en": "Useful formulas for financial calculations." }
}
```

**Näide `formulas.json`:**

```
[
  {
    "formula": "=SUM(A1:A10)",
    "name": { "en": "Sum of range", "et": "Vahemiku summa" },
    "description": { "en": "Adds all values in A1:A10." },
    "category": { "en": "Basic", "et": "Põhiline" }
  }
]
```

### Oluline märkus (⚠️ Important Notice)

Pluginate halduris on nupp **⚠️ Important Notice**. Klõps avab akna kõigi pluginite loomise reeglitega inglise keeles. Samad andmed on saadaval ka failis `IMPORTANT_NOTICE.md`.

## 🌐 Mitmekeelsus

38 keelt saadaval, vahetatavad otse rakenduses.
Uusi keeli saab lisada 🌍-nupu kaudu koos keele nõustajaga.

**Märkus hindi keele kohta (हिंदी):** Esimesel hindi keelele lülitumisel installitakse ühekordse toiminguna font *Noto Sans Devanagari* süsteemitasandil. Windows küsib administraatoriõigusi.

## 🔤 RTL-tugi (paremalt vasakule)

Paremalt vasakule kirjutamise suunaga keeled tuvastatakse automaatselt ja kogu liides peegeldatakse:

- **Araabia (عربي)** – automaatne RTL-tuvastus
- **Heebrea (עברית)** – automaatne RTL-tuvastus
- **Pärsia / Farsi (فارسی)** – automaatne RTL-tuvastus
- **Urdu (اردو)** – automaatne RTL-tuvastus

**Mis muutub RTL-režiimis:** Kogu kasutajaliidese paigutus peegeldatakse, sisestusväljad kasutavad RTL-joondust, font vahetub automaatselt RTL-ühilduvale (nt *Noto Sans Arabic*, *Noto Sans Hebrew*).

> 💡 **Märkus:** Genereeritud LibreOffice'i valemid jäävad alati LTR-süntaksiga – ainult kasutajaliides muudab suunda.


## 🗄️ Varundamine ja taastamine

### Varukoopia loomine

**Seaded → 🗄️ Loo varukoopia** kaudu:

1. **Nimi** – vabalt valitud nimetus (nt `Backup_Mai_2025`)
2. **Parool** – varukoopia krüptitakse AES-iga; ilma paroolita ei saa taastada
3. **Salvestuskoht** – kohalik või võrgudraiv
4. Klõpsa **💾 Loo varukoopia** – luuakse `.calc2backup`-fail

**Sisu:** Kõik lemmikud, seaded, meeskonna lemmikud (valikuline), installitud pluginad.

### Varukoopia taastamine

**Seaded → 📂 Taasta varukoopia** kaudu:

1. Vali varukoopia fail (`.calc2backup`)
2. Sisesta parool
3. Vali taastamise ulatus: ainult lemmikud / ainult seaded / kõik
4. Klõpsa **🔄 Taasta**

> ⚠️ Taastamisel kirjutatakse olemasolevad andmed üle. Enne taastamist pakutakse praeguste andmete automaatset varundamist.


## 💡 Näpunäited

- `$A$1` → absoluutviide (ripploend lahtriväljade kõrval)

- **Ctrl+S** → salvesta valem lemmikutesse

- **Ctrl+C** → kopeeri valem (väljaspool sisestusväljasid)

- **Ctrl+Z / Ctrl+Y** → Undo / Redo

- **Ctrl+F12** → minimeeri/taasta aken (töötab ka siis, kui Calc2 on minimeeritud)

- **Delete-klahv** lemmikute loendis → kustuta kirje

- Valemeid saab pärast genereerimist otse väljundväljas muuta

## 📁 Projekti struktuur

```
Calc2.py                        ← põhiprogramm
plugin_manager.py               ← pluginate haldur
IMPORTANT_NOTICE.md             ← pluginate loomise juhised
data/
  README_et.md / README_en.md / ...      ← abi keele kaupa
  REFERENTS_et.md / REFERENTS_en.md / ... ← funktsioonide viide keele kaupa
language/
  languages.json                ← kasutajaliidese tõlked (38 keelt)
  formula_explanations.json
services/
  language_tool.py              ← nõustaja: lisa uus keel
  settings_service.py
  auth_service.py
  favorites_service.py
  network_sync.py
  install_service.py
  backup_service.py             ← varundamine ja taastamine
  json_validator.py             ← languages.json / formula_explanations.json kontrollimine ja parandamine
plugins/                        ← pluginate kaust (luuakse automaatselt)
  minu_plugin/
    plugin.json
    formulas.json
fonts/
  NotoSansDevanagari-Regular.ttf  ← hindi font
  NotoSansArabic-Regular.ttf      ← araabia font (RTL)
  NotoSansHebrew-Regular.ttf      ← heebrea font (RTL)
python/                         ← manustatud Python
  python.exe
  ...
settings.json                   ← luuakse automaatselt
lemmikud.json                   ← kohalikud lemmikud (luuakse automaatselt)
```

## 🧠 Tehnilised eripärad

- **Aatomiline failisalvestus** → väldib failide rikkumist salvestamisel

- **Teenusepõhine arhitektuur** → loogika ja kasutajaliides on rangelt lahutatud

- **Automaatne migratsioon** → vanad lemmikute formaadid tuvastatakse ja teisendatakse

- **Robustne veakäsitlus** → vigased failid ei põhjusta rakenduse krahhi

- **Süntaksi esiletõstmine** → valemid kuvatakse värviliselt

- **Tume režiim** → täielikult toetatud

- **Pluginate süsteem** → Calc2 on laiendatav omaenda valemipluginatega

- **RTL-mootor** → RTL-keelte automaatne tuvastamine, täielik kasutajaliidese peegeldamine koos sobivate fontidega

- **Varundamine ja taastamine** → AES-krüptitud varukoopiad nime ja parooliga, valikuline taastamine

- **JSON validaator** → `languages.json` ja `formula_explanations.json` automaatne kontrollimine ja parandamine sh riikide nimed ja kohustuslikud väljad

- **LibreOffice allikas** → `formula_explanations.json` täidetakse LibreOffice Calc ametlikust dokumentatsioonist (https://help.libreoffice.org)

- **Globaalne kiirklahv** → `Ctrl+F12` töötab süsteemitasandil `keyboard`-teegi kaudu (taustaprotsess)

## Litsents

Vabalt kasutatav isiklikel ja ärilistel eesmärkidel.
