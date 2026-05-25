# LibreOffice Calc Cúntóir Foirmlí

Uirlis Python chun foirmlí LibreOffice Calc a chruthú, a thástáil agus a bhainistiú go tapa – le córas ceanán, sioncrónú foirne, ilteangachas agus bainisteoir breiseán.

## 🚀 Gnéithe

- 📑 4 cluaisín le breis is 60 feidhm

- 🌐 38 teanga (Hindi san áireamh le suiteáil cló uathoibríoch)

- ⭐ Córas ceanán (áitiúil agus sioncrónú foirne trí thiomántán líonra)

- 🛠 Painéal riaracháin do cheanáin foirne (cosanta le focal faire)

- 📋 Foirmlí incóipeála díreach le aibhsiú comhréire

- ✏️ Réimse aschuir insherkaithe le Cealaigh/Athdhéan

- 📖 Cabhair ionsuite agus tagairt feidhmeanna (de réir teanga)

- 💾 Sábháil uathoibríoch (JSON, scríofa go adamhach)

- 🌙 Mód dorcha

- 🔌 Bainisteoir breiseán chun breiseáin foirmlí féin a chruthú

- 🔤 Tacaíocht RTL (deas go clé) – aithint uathoibríoch treo scríbhneoireachta

- 🗄️ Cúltaca & Athchóiriú – sábháil gach socrú agus ceanán le hainm agus focal faire

- ⌨️ Eochair ghearr dhomhanda `Ctrl+F12` chun íoslaghdú/athchóiriú
- 🔍 Bailíochtóir JSON – seiceáil agus ceartú uathoibríoch ar `languages.json` agus `formula_explanations.json`

## 🖥️ Úsáid

**1. Sonraí a iontráil**

- Raon cille (m.sh. `A1:A10`)

- Cill 1 / Cill 2 (m.sh. `A1`, `B1`)

- Paraiméadar roghnach (m.sh. téacs nó innéacs)

- Mód tagartha absalóidí inscoite: `A1`, `$A1`, `A$1`, `$A$1`

**2. Feidhm a roghnú** Roghnaigh cluaisín agus cliceáil ar fheidhm – gintear an fhoirmle láithreach bonn.

**3. An fhoirmle a choigeartú** Is féidir an fhoirmle ginte a chur in eagar go díreach sa réimse aschuir.

**4. Cóipeáil** Le haon chliceáil chuig an gearrthaisce (dathanna comhréire san áireamh).

**5. Ceanáin a úsáid**

- ⭐ Sábháil → an fhoirmle reatha a shábháil (Ctrl+S)

- 📂 Luchtaigh → foirmle a athúsáid

- ❌ Scrios → eochair Del nó cnaipe

- 🕐 Stair → foirmlí a úsáideadh le déanaí

## 📊 Forbhreathnú ar Chluaisíní

**Cluaisín 1 – Feidhmeanna Bunúsacha** `+` `-` `\*` `/` `^` SUM, AVERAGE, MIN, MAX, MEDIAN, COUNT, COUNTA, SUMPRODUCT

**Cluaisín 2 – Feidhmeanna Casta** IF, AND, OR, NOT SUMIF, COUNTIF, AVERAGEIF, SUMIFS, STDEV, VAR, COUNTBLANK, LARGE

**Cluaisín 3 – Dáta agus Téacs** TODAY, NOW, YEAR, MONTH, DAY, DATE, DATEDIF, WEEKDAY CONCATENATE, LEN, LEFT, RIGHT, MID, UPPER, LOWER, TRIM

**Cluaisín 4 – Cuardach agus Slánú** VLOOKUP, HLOOKUP, INDEX, MATCH, INDEX+MATCH ROUND, ROUNDUP, ROUNDDOWN, INT, TRUNC, ABS, MOD, SQRT, RAND


## 📖 Mínithe Foirmlí ó Dhoiciméadacht LibreOffice

Líontar an comhad `formula_explanations.json` go díreach ó **dhoiciméadacht oifigiúil LibreOffice Calc** (https://help.libreoffice.org).

### Foinse Sonraí agus Nuashonrú

- Glactar cur síos, faisnéis comhréire agus samplaí ó shuíomh cabhrach oifigiúil LibreOffice
- Braitheann na teangacha tacaithe ar na haistriúcháin atá ar fáil ar an suíomh
- Tá sa chomhad do gach feidhm: ainm, comhréir, cur síos, sampla agus catagóir
- Is féidir breiseanna nó ceartúcháin a dhéanamh de láimh (féach Bailíochtóir JSON)

### Struchtúr `formula_explanations.json`

```json
{
  "SUM": {
    "ga": {
      "syntax": "SUM(Uimhir1; Uimhir2; ...)",
      "description": "Suimíonn sé gach uimhir i raon cille.",
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

| Réimse | Riachtanach | Cur Síos |
|--------|------------|---------|
| `syntax` | ✅ | Comhréir foirmle le paraiméadair |
| `description` | ✅ | Cur síos gearr ar an bhfeidhm |
| `example` | ✅ | Sampla úsáide mar fhoirmle réidh |
| `note` | ❌ | Nóta roghnach |

> 💡 **Nóta:** Mura bhfuil iontráil ann do theanga, filleann an aip go huathoibríoch ar an leagan Béarla.

---

## 🔍 Bailíochtóir JSON do Chomhaid Teanga

Seiceálann agus ceartaíonn an **Bailíochtóir JSON** ionsuite `languages.json` agus `formula_explanations.json` le haghaidh comhsheasmhachta, iomláine agus ainmneacha tíortha cearta.

Inrochtana trí **Socruithe → 🔍 Bailíochtóir JSON**.

### Cad a Sheiceáiltear?

#### `languages.json`

- ✅ Na 38 teanga ar fad i láthair (de réir cód teanga ISO 639-1)
- ✅ **Ainmneacha tíre agus teanga ceart** (m.sh. `"ga"` → `"Gaeilge"`)
- ✅ Gan chóid teanga dúbailte
- ✅ Réimsí riachtanacha i láthair: `name`, `native_name`, `flag`, `rtl`
- ✅ Bratach RTL socraithe i gceart (Araibis, Eabhrais, Peirsis, Urdúis → `"rtl": true`)

#### `formula_explanations.json`

- ✅ Gach feidhm ó na 4 cluaisín cláraithe
- ✅ Réimsí riachtanacha i láthair: `syntax`, `description`, `example`
- ✅ Gan réimsí folmha (`""` nó `null`)
- ✅ Cóid teanga ag teacht le `languages.json`

### Feidhmeanna Ceartúcháin

| Cineál Earráide | Ceartú Uathoibríoch |
|----------------|---------------------|
| Ainm tíre mícheart | Athsholáthraithe leis an ainm ceart de réir ISO |
| Iontráil teanga ar iarraidh | Líonta le leagan cúltaca Béarla |
| Réimse riachtanach folamh | Marcáilte mar `"[MISSING]"` le haghaidh athbhreithniú de láimh |
| Iontráil dúbailte | Dúbláin bainte, iontráil níos iomláine coinnithe |
| Bratach RTL mícheart | Ceartaithe go huathoibríoch bunaithe ar chóid RTL aitheanta |

### Conas é a Úsáid

1. Oscail **Socruithe → 🔍 Bailíochtóir JSON**
2. Roghnaigh comhad: `languages.json` nó `formula_explanations.json` (nó an dá cheann)
3. **🔎 Seiceáil** – taispeánann gach fadhb a aimsíodh
4. **🛠 Ceartú Uathoibríoch** – réitíonn gach earráid is féidir a cheartú go huathoibríoch
5. **💾 Sábháil** – scríobhann an comhad ceartaithe ar ais go hadamhach
6. **📋 Tuarascáil a Easpórtáil** (roghnach) – sábhálann comhad téacs le gach torthaí

> ⚠️ **Nóta:** Roimh gach ceartú uathoibríoch cruthaítear cóip chúltaca den chomhad bunaidh (`languages.json.bak` / `formula_explanations.json.bak`).

## ⭐ Córas Ceanán

- Foirmlí féin a shábháil agus a athúsáid

- Scaradh idir ceanáin phearsanta agus ceanáin foirne

- Tá ceanáin foirne inléite amháin (ní féidir ach leis an riarthóir iad a chur in eagar)

- Cuirtear cosc ar dhúbláin

- Sórtáil saor ar cheanáin phearsanta

- Sioncrónú trí thiomántán líonra (insocraithe go roghnach)

### Sioncrónú Foirne

Trí **Socruithe → 🌐 Cosán Líonra** is féidir tiomántán líonra a iontráil (m.sh. `\\\\Freastalaí\\Roinnt\\foirmlí`).

- Ag tosú: sábháiltear ceanáin líonra go háitiúil (cúltaca as líne)

- Ag sábháil: scríobhtar foirmlí pearsanta chuig an líonra, fágtar foirmlí foirne gan athrú

## 🛠 Painéal Riaracháin

Inrochtana trí chnaipe 🛠. Ar an gcéad chliceáil socraítear focal faire (PBKDF2-SHA256, ní shábháiltear ach an hais).

- Foirmlí foirne a chur leis, a chur in eagar agus a scriosadh

- Focal faire a athrú

- Scríobhtar athruithe go díreach chuig an tiomántán líonra

## 🔌 Bainisteoir Breiseán

Is uirlis neamhspleách é an bainisteoir breiseán (`plugin_manager.py`) chun breiseáin foirmlí féin a chruthú agus a bhainistiú do Calc2. Tá sé sa chomhad céanna le `Calc2.py` agus tosaítear é le cnaipe 🔌 i gCalc2.py:

### Feidhmeanna

- **Breiseán nua a chruthú** – treoraí céim ar chéim (ainm, foirmlí, aistriúcháin, achoimre)

- **Foirmlí a chur leis** – foirmlí a chur le breiseán atá ann cheana

- **Aistriúcháin a chur in eagar** – ainmneacha foirmlí a aistriú go dtí na 38 teanga

- **Fillteán breiseán a oscailt** – go díreach i mbainisteoir comhad

- **Breiseán a scriosadh** – le deimhniú slándála

### Struchtúr Breiseáin

Tá gach breiseán mar fhofhillteán in `plugins/` agus tá sé comhdhéanta de dhá chomhad:

```
plugins/
  mo_bhreiseán/
    plugin.json      ← meiteashonraí (ainm, leagan, údar, cur síos)
    formulas.json    ← foirmlí le haistriúcháin
```

**Sampla `plugin.json`:**

```
{
  "id": "mo_bhreiseán",
  "enabled": true,
  "version": "1.0",
  "author": "D'Ainm",
  "icon": "💰",
  "name": { "en": "Finance Formulas", "ga": "Foirmlí Airgeadais" },
  "description": { "en": "Useful formulas for financial calculations." }
}
```

**Sampla `formulas.json`:**

```
[
  {
    "formula": "=SUM(A1:A10)",
    "name": { "en": "Sum of range", "ga": "Suim an raoin" },
    "description": { "en": "Adds all values in A1:A10." },
    "category": { "en": "Basic", "ga": "Bunúsach" }
  }
]
```

### Fógra Tábhachtach (⚠️ Important Notice)

Sa bhainisteoir breiseán tá cnaipe **⚠️ Important Notice**. Osclaíonn cliceáil fuinneog le gach riail maidir le cruthú ceart breiseán as Béarla. Tá an fhaisnéis chéanna ar fáil freisin in `IMPORTANT_NOTICE.md`.

## 🌐 Ilteangachas

38 teanga ar fáil, inathraithe go díreach san aip.
Is féidir teangacha nua a chur leis trí chnaipe 🌍 leis an treoraí teanga.

**Nóta faoi Hiondúis (हिंदी):** Ar an gcéad aistriú go Hiondúis suiteáiltear an cló *Noto Sans Devanagari* uair amháin ar leibhéal an chórais. Iarrfaidh Windows cearta riarthóra.

## 🔤 Tacaíocht RTL (Deas go Clé)

Aithníonn an clár teangacha le scríbhneoireacht ó dheas go clé go huathoibríoch agus scáthánáiltear an comhéadan iomlán:

- **Araibis (عربي)** – aithint RTL uathoibríoch
- **Eabhrais (עברית)** – aithint RTL uathoibríoch
- **Peirsis / Farsi (فارسی)** – aithint RTL uathoibríoch
- **Urdúis (اردو)** – aithint RTL uathoibríoch

**Athruithe i mód RTL:** Scáthánáiltear leagan amach iomlán an UI, úsáideann réimsí ionchuir ailíniú RTL, athraíonn an cló go huathoibríoch go cló comhoiriúnach le RTL (m.sh. *Noto Sans Arabic*, *Noto Sans Hebrew*).

> 💡 **Nóta:** Fanann foirmlí LibreOffice ginte i gcónaí i gcomhréir LTR – ní athraíonn ach an comhéadan úsáideora treo.


## 🗄️ Cúltaca & Athchóiriú

### Cúltaca a Chruthú

Trí **Socruithe → 🗄️ Cúltaca a Chruthú**:

1. **Ainm** – lipéad saorcheaptha (m.sh. `Cúltaca_Bealtaine_2025`)
2. **Focal faire** – cripthítear an cúltaca le AES; ní féidir athchóiriú gan é
3. **Suíomh sábhála** – áitiúil nó ar thiomántán líonra
4. Cliceáil **💾 Cúltaca a Chruthú** – cruthaítear comhad `.calc2backup`

**Inneachar:** Gach ceanán, socruithe, ceanáin foirne (roghnach), breiseáin suiteáilte.

### Athchóiriú

Trí **Socruithe → 📂 Cúltaca a Athchóiriú**:

1. Roghnaigh comhad (`.calc2backup`)
2. Iontráil an focal faire
3. Roghnaigh raon: ceanáin amháin / socruithe amháin / gach rud
4. Cliceáil **🔄 Athchóiriú**

> ⚠️ Scriosaítear sonraí reatha le linn athchóirithe. Tairgtear cúltaca uathoibríoch de na sonraí reatha roimhe sin.


## 💡 Leideanna

- `$A$1` → tagairt absalóideach (liosta anuas in aice le réimsí cille)

- **Ctrl+S** → foirmle a shábháil i gceanáin

- **Ctrl+C** → foirmle a chóipeáil (lasmuigh de réimsí ionchuir)

- **Ctrl+Z / Ctrl+Y** → Cealaigh / Athdhéan

- **Ctrl+F12** → fuinneog a íoslaghdú/athchóiriú (oibríonn fiú nuair atá Calc2 íoslaghdaithe)

- **Eochair Del** sa liosta ceanán → iontráil a scriosadh

- Is féidir foirmlí a choigeartú go díreach sa réimse aschuir tar éis a nginiúna

## 📁 Struchtúr an Tionscadail

```
Calc2.py                        ← príomhchlár
plugin_manager.py               ← bainisteoir breiseán
IMPORTANT_NOTICE.md             ← treoracha maidir le cruthú breiseán
data/
  README_ga.md / README_en.md / ...      ← cabhair de réir teanga
  TAGAIRT_ga.md / TAGAIRT_en.md / ...    ← tagairt feidhmeanna de réir teanga
language/
  languages.json                ← aistriúcháin comhéadain (38 teanga)
  formula_explanations.json
services/
  language_tool.py              ← treoraí: teanga nua a chur leis
  settings_service.py
  auth_service.py
  favorites_service.py
  network_sync.py
  install_service.py
  backup_service.py             ← cúltaca & athchóiriú
  json_validator.py             ← seiceáil agus ceartú languages.json / formula_explanations.json
plugins/                        ← fillteán breiseán (cruthaithe go huathoibríoch)
  mo_bhreiseán/
    plugin.json
    formulas.json
fonts/
  NotoSansDevanagari-Regular.ttf  ← cló Hiondúise
  NotoSansArabic-Regular.ttf      ← cló Araibise (RTL)
  NotoSansHebrew-Regular.ttf      ← cló Eabhraise (RTL)
python/                         ← Python leabaithe
  python.exe
  ...
settings.json                   ← cruthaithe go huathoibríoch
ceanáin.json                    ← ceanáin áitiúla (cruthaithe go huathoibríoch)
```

## 🧠 Buaicphointí Teicniúla

- **Scríobh Comhad Adamhach** → cuireann cosc ar chomhaid lofa le linn sábhála

- **Ailtireacht Seirbhíse** → loighic agus comhéadan úsáideora scartha go docht

- **Imirce Uathoibríoch** → aithníonn agus tiontaíonn formáidí ceanán sean

- **Láimhseáil Earráidí Láidir** → ní chuireann comhaid lofa an feidhmchlár ar fionraí

- **Aibhsiú Comhréire** → taispeántar foirmlí i ndath

- **Mód Dorcha** → tacaíocht iomlán

- **Córas Breiseán** → is féidir Calc2 a leathnú le breiseáin foirmlí féin

- **Inneall RTL** → aithint uathoibríoch teangacha RTL, scáthánú iomlán UI le clónna oiriúnacha

- **Cúltaca & Athchóiriú** → cúltacaí AES-chriptithe le hainm agus focal faire, athchóiriú roghnach

- **Bailíochtóir JSON** → seiceáil agus ceartú uathoibríoch `languages.json` agus `formula_explanations.json` lena n-áirítear ainmneacha tíortha agus réimsí riachtanacha

- **Foinse LibreOffice** → líontar `formula_explanations.json` ó dhoiciméadacht oifigiúil LibreOffice Calc (https://help.libreoffice.org)

- **Eochair Ghearr Dhomhanda** → oibríonn `Ctrl+F12` ar leibhéal an chórais trí leabharlann `keyboard` (snáithe cúlra)

## Ceadúnas

Saor le húsáid chun críocha pearsanta agus tráchtála.
