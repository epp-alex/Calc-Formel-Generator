# LibreOffice Calc Assistent tal-Formuli

Għodda Python biex toħloq, ttestja u timmaniġġja formuli tal-LibreOffice Calc malajr – b'sistema ta' favoriti, sinkronizzazzjoni tat-tim, multilingwiżmu u maniġer tal-plugins.

## 🚀 Karatteristiċi

- 📑 4 tabs b'aktar minn 60 funzjoni

- 🌐 38 lingwa (inkluż il-Hindi b'installazzjoni awtomatika tal-font)

- ⭐ Sistema ta' favoriti (lokali u sinkronizzazzjoni tat-tim permezz ta' drive tan-netwerk)

- 🛠 Panel tal-amministrazzjoni għall-favoriti tat-tim (protett b'password)

- 📋 Formuli li jistgħu jiġu kkupjati direttament b'evidenzjar tas-sintassi

- ✏️ Qasam tal-output li jista' jiġi editjat b'Agħmel Lura/Erġa' Agħmel

- 📖 Għajnuna integrata u referenza tal-funzjonijiet (skont il-lingwa)

- 💾 Salvataggio awtomatiku (JSON, miktub atomikament)

- 🌙 Modalità skura

- 🔌 Maniġer tal-plugins biex toħloq plugins tal-formuli tiegħek stess

- 🔤 Appoġġ RTL (mil-lemin għax-xellug) – detezzjoni awtomatika tad-direzzjoni tal-kitba

- 🗄️ Backup u Rkupru – salva s-settings u l-favoriti kollha b'isem u password

- ⌨️ Shortcut globali `Ctrl+F12` biex timminimizza/tirkupra
- 🔍 Validatur JSON – verifika u korrezzjoni awtomatika ta' `languages.json` u `formula_explanations.json`

## 🖥️ Użu

**1. Daħħal id-dejta**

- Firxa taċ-ċelloli (eż. `A1:A10`)

- Ċellola 1 / Ċellola 2 (eż. `A1`, `B1`)

- Parametru fakultattiv (eż. test jew indiċi)

- Modalità ta' referenza assoluta li tista' tagħżel: `A1`, `$A1`, `A$1`, `$A$1`

**2. Agħżel funzjoni** Agħżel tab u kklikkja fuq funzjoni – il-formula tinġenerja immedjatament.

**3. Aġġusta l-formula** Il-formula ġġenerata tista' tiġi editjata direttament fil-qasam tal-output.

**4. Ikkuppja** B'klikk wieħed fil-clipboard (inkluż il-kuluri tas-sintassi).

**5. Uża l-favoriti**

- ⭐ Salva → salva l-formula attwali (Ctrl+S)

- 📂 Illowdja → uża mill-ġdid formula

- ❌ Ħassar → buttuna Del jew buttuna

- 🕐 Storja → formuli użati reċentement

## 📊 Ħarsa ġenerali tat-tabs

**Tab 1 – Funzjonijiet Bażiċi** `+` `-` `\*` `/` `^` SUM, AVERAGE, MIN, MAX, MEDIAN, COUNT, COUNTA, SUMPRODUCT

**Tab 2 – Funzjonijiet Avanzati** IF, AND, OR, NOT SUMIF, COUNTIF, AVERAGEIF, SUMIFS, STDEV, VAR, COUNTBLANK, LARGE

**Tab 3 – Data u Test** TODAY, NOW, YEAR, MONTH, DAY, DATE, DATEDIF, WEEKDAY CONCATENATE, LEN, LEFT, RIGHT, MID, UPPER, LOWER, TRIM

**Tab 4 – Tfittxija u Tqarrib** VLOOKUP, HLOOKUP, INDEX, MATCH, INDEX+MATCH ROUND, ROUNDUP, ROUNDDOWN, INT, TRUNC, ABS, MOD, SQRT, RAND


## 📖 Spjegazzjonijiet tal-Formuli mid-Dokumentazzjoni ta' LibreOffice

Il-fajl `formula_explanations.json` jiġi mimlija direttament mid-**dokumentazzjoni uffiċjali ta' LibreOffice Calc** (https://help.libreoffice.org).

### Sors tad-Dejta u Aġġornament

- Id-deskrizzjonijiet, l-informazzjoni dwar is-sintassi u l-eżempji jittieħdu mis-sit tal-għajnuna uffiċjali ta' LibreOffice
- Il-lingwi appoġġjati jiddependu mit-traduzzjonijiet disponibbli fuq is-sit
- Il-fajl fih għal kull funzjoni: isem, sintassi, deskrizzjoni, eżempju u kategorija
- Żidiet jew korrezzjonijiet jistgħu jsiru manwalment (ara Validatur JSON)

### Struttura ta' `formula_explanations.json`

```json
{
  "SUM": {
    "mt": {
      "syntax": "SUM(Numru1; Numru2; ...)",
      "description": "Tiżdied in-numri kollha f'firxa ta' ċelloli.",
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

| Qasam | Meħtieġ | Deskrizzjoni |
|-------|---------|-------------|
| `syntax` | ✅ | Sintassi tal-formula bil-parametri |
| `description` | ✅ | Deskrizzjoni qasira tal-funzjoni |
| `example` | ✅ | Eżempju ta' użu bħala formula lesta |
| `note` | ❌ | Nota fakultattiva |

> 💡 **Nota:** Jekk m'hemmx dħul għal lingwa, l-app tirritorna awtomatikament għall-verżjoni bl-Ingliż.

---

## 🔍 Validatur JSON għall-Fajls tal-Lingwa

Il-**Validatur JSON** integrat jivverifika u jikkorriġi `languages.json` u `formula_explanations.json` għal konsistenza, kompletezza u ismijiet korretti tal-pajjiżi. Aċċessibbli permezz ta' **Settings → 🔍 Validatur JSON**.

### X'jiġi vverifikat?

#### `languages.json`

- ✅ Il-38 lingwa kollha preżenti (skont il-kodiċi ISO 639-1)
- ✅ **Ismijiet korretti tal-pajjiżi u tal-lingwi** (eż. `"mt"` → `"Malti"`)
- ✅ L-ebda kodiċi lingwa dupplikat
- ✅ Oqsma meħtieġa preżenti: `name`, `native_name`, `flag`, `rtl`
- ✅ Bandiera RTL issettjata b'mod korrett (Għarbi, Ebrajk, Persjan, Urdu → `"rtl": true`)

#### `formula_explanations.json`

- ✅ Il-funzjonijiet kollha mit-4 tabs irreġistrati
- ✅ Oqsma meħtieġa preżenti: `syntax`, `description`, `example`
- ✅ L-ebda oqsma vojta (`""` jew `null`)
- ✅ Il-kodiċi tal-lingwa jaqblu ma' `languages.json`

### Funzjonijiet ta' Korrezzjoni

| Tip ta' żball | Korrezzjoni awtomatika |
|-------------|----------------------|
| Isem tal-pajjiż żbaljat | Sostitwit bl-isem korrett skont ISO |
| Dħul tal-lingwa nieqes | Mimlija bil-verżjoni Ingliża bħala riserva |
| Qasam meħtieġ vojt | Immarkat bħala `"[MISSING]"` għar-reviżjoni manwali |
| Dħul dupplikat | Id-duplikati jitneħħew, jinżamm dak aktar komplet |
| Bandiera RTL żbaljata | Ikkorriġuta awtomatikament abbażi tal-kodiċi RTL magħrufa |

### Kif Tuża

1. Iftaħ **Settings → 🔍 Validatur JSON**
2. Agħżel il-fajl: `languages.json` jew `formula_explanations.json` (jew it-tnejn)
3. **🔎 Ivverifika** – juri l-problemi kollha misjuba
4. **🛠 Ikkorriġi awtomatikament** – jsolvi l-iżbalji kollha li jistgħu jiġu korretti awtomatikament
5. **💾 Salva** – jikteb il-fajl ikkorriġut b'mod atomiku
6. **📋 Esporta rapport** (fakultattiv) – jissalva fajl tat-test bir-riżultati kollha

> ⚠️ **Nota:** Qabel kull korrezzjoni awtomatika tinħoloq kopja tal-fajl oriġinali (`languages.json.bak` / `formula_explanations.json.bak`).

## ⭐ Sistema ta' Favoriti

- Salva u uża mill-ġdid il-formuli tiegħek stess

- Separazzjoni bejn il-favoriti personali u tal-tim

- Il-favoriti tat-tim huma read-only (l-amministratur biss jista' jeditjahom)

- Duplikati huma evitati

- Ordnar liberu tal-favoriti personali

- Sinkronizzazzjoni permezz ta' drive tan-netwerk (ikkonfigurabbli b'mod fakultattiv)

### Sinkronizzazzjoni tat-Tim

Permezz ta' **Settings → 🌐 Mogħdija tan-Netwerk** tista' ddaħħal drive tan-netwerk (eż. `\\\\Server\\Kondiviżjoni\\formuli`).

- Fl-ibdija: il-favoriti tan-netwerk jiġu salvati lokalment (backup offline)

- Meta ssalva: il-formuli personali jiġu miktuba fuq in-netwerk, il-formuli tat-tim jibqgħu intatti

## 🛠 Panel tal-Amministrazzjoni

Aċċessibbli permezz tal-buttuna 🛠. Fl-ewwel klikk tiġi stabbilita password (PBKDF2-SHA256, tinħażen il-hash biss).

- Żid, editja u ħassar formuli tat-tim

- Ibdel il-password

- Il-bidliet jiġu miktuba direttament fuq id-drive tan-netwerk

## 🔌 Maniġer tal-Plugins

Il-maniġer tal-plugins (`plugin_manager.py`) huwa għodda awtonomu biex toħloq u timmaniġġja plugins tal-formuli tiegħek stess għal Calc2. Jinsab fl-istess folder bħal `Calc2.py` u jinbeda bil-buttuna 🔌 f'Calc2.py:

### Funzjonijiet

- **Oħloq plugin ġdid** – wizard pass pass (isem, formuli, traduzzjonijiet, sommarju)

- **Żid formuli** – komplemeta plugin eżistenti bil-formuli

- **Editja t-traduzzjonijiet** – traduzzjoni tal-ismijiet tal-formuli fil-38 lingwa kollha

- **Iftaħ il-folder tal-plugins** – direttament fil-file manager

- **Ħassar plugin** – b'konferma ta' sigurtà

### Struttura tal-Plugin

Kull plugin jinsab bħala subfolder f'`plugins/` u jikkonsisti f'żewġ fajls:

```
plugins/
  il-plugin-tieghi/
    plugin.json      ← metadejta (isem, verżjoni, awtur, deskrizzjoni)
    formulas.json    ← formuli bit-traduzzjonijiet
```

**Eżempju `plugin.json`:**

```
{
  "id": "il-plugin-tieghi",
  "enabled": true,
  "version": "1.0",
  "author": "Ismek",
  "icon": "💰",
  "name": { "en": "Finance Formulas", "mt": "Formuli Finanzjarji" },
  "description": { "en": "Useful formulas for financial calculations." }
}
```

**Eżempju `formulas.json`:**

```
[
  {
    "formula": "=SUM(A1:A10)",
    "name": { "en": "Sum of range", "mt": "Somma tal-firxa" },
    "description": { "en": "Adds all values in A1:A10." },
    "category": { "en": "Basic", "mt": "Bażiku" }
  }
]
```

### Avviż Importanti (⚠️ Important Notice)

Fil-maniġer tal-plugins hemm il-buttuna **⚠️ Important Notice**. Klikk jiftaħ tieqa bir-regoli kollha għall-ħolqien korrett tal-plugins bl-Ingliż. L-istess informazzjoni tinsab ukoll f'`IMPORTANT_NOTICE.md`.

## 🌐 Multilingwiżmu

38 lingwa disponibbli, li jistgħu jinbidlu direttament fl-applikazzjoni.
Lingwi ġodda jistgħu jiżdiedu permezz tal-buttuna 🌍 bil-wizard tal-lingwa.

**Nota dwar il-Hindi (हिंदी):** Fl-ewwel darba li tibdel għall-Hindi, il-font *Noto Sans Devanagari* jiġi installat darba waħda fil-livell tas-sistema. Windows jitlob drittijiet tal-amministratur.

## 🔤 Appoġġ RTL (Mil-Lemin għax-Xellug)

Il-lingwi bil-kitba mil-lemin għax-xellug jiġu ddetettati awtomatikament u l-interface kollha tiġi riflessa:

- **Għarbi (عربي)** – detezzjoni RTL awtomatika
- **Ebrajk (עברית)** – detezzjoni RTL awtomatika
- **Persjan / Farsi (فارسی)** – detezzjoni RTL awtomatika
- **Urdu (اردو)** – detezzjoni RTL awtomatika

**X'jinbidel fil-modalità RTL:** Il-layout kollu tal-UI jiġi rifless, il-oqsma tal-input jużaw allinjament RTL, il-font jinbidel awtomatikament għal wieħed kompatibbli ma' RTL (eż. *Noto Sans Arabic*, *Noto Sans Hebrew*).

> 💡 **Nota:** Il-formuli tal-LibreOffice ġġenerati jibqgħu dejjem fis-sintassi LTR – tibdel biss id-direzzjoni tal-interface.


## 🗄️ Backup u Rkupru

### Oħloq Backup

Permezz ta' **Settings → 🗄️ Oħloq Backup**:

1. **Isem** – tikketta libera (eż. `Backup_Mejju_2025`)
2. **Password** – il-backup jiġi encrypted b'AES; mingħajrha l-irkupru mhuwiex possibbli
3. **Post tas-salvataggio** – lokali jew fuq drive tan-netwerk
4. Klikk fuq **💾 Oħloq Backup** – jinħoloq fajl `.calc2backup`

**Kontenut:** Il-favoriti kollha, settings, favoriti tat-tim (fakultattiv), plugins installati.

### Rkupru tal-Backup

Permezz ta' **Settings → 📂 Irkupra Backup**:

1. Agħżel il-fajl (`.calc2backup`)
2. Daħħal il-password
3. Agħżel l-ambitu: favoriti biss / settings biss / kollox
4. Klikk fuq **🔄 Irkupra**

> ⚠️ Waqt l-irkupru d-dejta eżistenti tiġi miktuba fuqha. Qabel l-irkupru joffri backup awtomatiku tad-dejta attwali.


## 💡 Tips

- `$A$1` → referenza assoluta (menu dropdown ħdejn il-qasam taċ-ċelloli)

- **Ctrl+S** → salva l-formula fil-favoriti

- **Ctrl+C** → ikkuppja l-formula (barra mill-oqsma tal-input)

- **Ctrl+Z / Ctrl+Y** → Agħmel Lura / Erġa' Agħmel

- **Ctrl+F12** → imminimizza/irkupra l-tieqa (taħdem anke meta Calc2 tkun imminimizzata)

- **Buttuna Del** fil-lista tal-favoriti → ħassar dħul

- Il-formuli jistgħu jiġu aġġustati direttament fil-qasam tal-output wara l-ġenerazzjoni

## 📁 Struttura tal-Proġett

```
Calc2.py                        ← programm prinċipali
plugin_manager.py               ← maniġer tal-plugins
IMPORTANT_NOTICE.md             ← istruzzjonijiet għall-ħolqien tal-plugins
data/
  README_mt.md / README_en.md / ...      ← għajnuna skont il-lingwa
  REFERENZA_mt.md / REFERENZA_en.md / ... ← referenza tal-funzjonijiet skont il-lingwa
language/
  languages.json                ← traduzzjonijiet tal-interface (38 lingwa)
  formula_explanations.json
services/
  language_tool.py              ← wizard: żid lingwa ġdida
  settings_service.py
  auth_service.py
  favorites_service.py
  network_sync.py
  install_service.py
  backup_service.py             ← backup u rkupru
  json_validator.py             ← verifika u korrezzjoni ta' languages.json / formula_explanations.json
plugins/                        ← folder tal-plugins (maħluq awtomatikament)
  il-plugin-tieghi/
    plugin.json
    formulas.json
fonts/
  NotoSansDevanagari-Regular.ttf  ← font tal-Hindi
  NotoSansArabic-Regular.ttf      ← font Għarbi (RTL)
  NotoSansHebrew-Regular.ttf      ← font Ebrajk (RTL)
python/                         ← Python inkorporat
  python.exe
  ...
settings.json                   ← maħluq awtomatikament
favoriti.json                   ← favoriti lokali (maħluq awtomatikament)
```

## 🧠 Punti Tekniċi Ewlenin

- **Kitba atomika tal-fajls** → tipprevjeni l-korruzzjoni tal-fajls waqt is-salvataggio

- **Arkitettura tas-servizzi** → il-loġika u l-interface tal-utent huma separati b'mod strett

- **Migrazzjoni awtomatika** → il-formati antiki tal-favoriti jiġu rikonoxxuti u kkonvertiti

- **Ġestjoni robusta tal-iżbalji** → fajls korrotti ma jikkawżawx il-waqfien tal-applikazzjoni

- **Evidenzjar tas-sintassi** → il-formuli jintwera bil-kulur

- **Modalità skura** → appoġġjata kompletament

- **Sistema tal-plugins** → Calc2 tista' tiġi estiża b'plugins tal-formuli tiegħek stess

- **Magna RTL** → detezzjoni awtomatika tal-lingwi RTL, riflessjoni sħiħa tal-UI b'fonts adattati

- **Backup u Rkupru** → backups AES-encrypted b'isem u password, rkupru selettiv

- **Validatur JSON** → verifika u korrezzjoni awtomatika ta' `languages.json` u `formula_explanations.json` inkl. ismijiet tal-pajjiżi u oqsma meħtieġa

- **Sors LibreOffice** → `formula_explanations.json` jiġi mimlija mid-dokumentazzjoni uffiċjali ta' LibreOffice Calc (https://help.libreoffice.org)

- **Shortcut globali** → `Ctrl+F12` taħdem fil-livell tas-sistema permezz tal-librerija `keyboard` (thread tal-isfond)

## Liċenzja

Użu liberu għal skopijiet personali u kummerċjali.
