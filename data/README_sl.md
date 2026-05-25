# LibreOffice Calc Pomočnik za formule

Orodje v Pythonu za hitro ustvarjanje, testiranje in upravljanje formul LibreOffice Calc – s sistemom priljubljenih, sinhronizacijo ekipe, večjezičnostjo in upraviteljem vtičnikov.

## 🚀 Funkcije

- 📑 4 zavihki z več kot 60 funkcijami

- 🌐 38 jezikov (vključno s hindijščino z avtomatsko namestitvijo pisave)

- ⭐ Sistem priljubljenih (lokalno in sinhronizacija ekipe prek omrežnega pogona)

- 🛠 Skrbniška plošča za priljubljene ekipe (zaščitena z geslom)

- 📋 Formule, pripravljene za kopiranje, z označevanjem sintakse

- ✏️ Urejalno izhodno polje z razveljavitvijo/ponovitvijo

- 📖 Vgrajena pomoč in referenca funkcij (za vsak jezik)

- 💾 Samodejno shranjevanje (JSON, atomsko pisanje)

- 🌙 Temni način

- 🔌 Upravitelj vtičnikov za ustvarjanje lastnih vtičnikov formul

- 🔤 Podpora RTL (od desne proti levi) – samodejno zaznavanje smeri pisanja

- 🗄️ Varnostna kopija in obnovitev – shranite vse nastavitve in priljubljene z imenom in geslom

- ⌨️ Globalna bližnjica `Ctrl+F12` za minimiziranje/obnovitev okna
- 🔍 Validator JSON – samodejno preverjanje in popravljanje `languages.json` in `formula_explanations.json`

## 🖥️ Uporaba

**1. Vnos podatkov**

- Obseg celic (npr. `A1:A10`)

- Celica 1 / Celica 2 (npr. `A1`, `B1`)

- Neobvezni parameter (npr. besedilo ali indeks)

- Izbira načina absolutne sklicevanja: `A1`, `$A1`, `A$1`, `$A$1`

**2. Izbira funkcije** Izberite zavihek in kliknite funkcijo – formula se takoj ustvari.

**3. Prilagoditev formule** Ustvarjeno formulo lahko urejate neposredno v izhodnem polju.

**4. Kopiranje** Prenesite v odložišče z enim klikom (vključno z barvami sintakse).

**5. Uporaba priljubljenih**

- ⭐ Shrani → shrani trenutno formulo (Ctrl+S)

- 📂 Naloži → ponovno uporabi formulo

- ❌ Izbriši → tipka Delete ali gumb

- 🕐 Zgodovina → nedavno uporabljene formule

## 📊 Pregled zavihkov

**Zavihek 1 – Osnovne funkcije** `+` `-` `*` `/` `^` SUM, AVERAGE, MIN, MAX, MEDIAN, COUNT, COUNTA, SUMPRODUCT

**Zavihek 2 – Napredne funkcije** IF, AND, OR, NOT SUMIF, COUNTIF, AVERAGEIF, SUMIFS, STDEV, VAR, COUNTBLANK, LARGE

**Zavihek 3 – Datum in besedilo** TODAY, NOW, YEAR, MONTH, DAY, DATE, DATEDIF, WEEKDAY CONCATENATE, LEN, LEFT, RIGHT, MID, UPPER, LOWER, TRIM

**Zavihek 4 – Iskanje in zaokroževanje** VLOOKUP, HLOOKUP, INDEX, MATCH, INDEX+MATCH ROUND, ROUNDUP, ROUNDDOWN, INT, TRUNC, ABS, MOD, SQRT, RAND


## 📖 Razlage formul iz dokumentacije LibreOffice

Datoteka `formula_explanations.json` se polni neposredno iz **uradne dokumentacije LibreOffice Calc** (https://help.libreoffice.org).

### Vir podatkov in posodabljanje

- Opisi, informacije o sintaksi in primeri se prevzamejo z uradne strani za pomoč LibreOffice
- Podprti jeziki so odvisni od prevodov, ki so na voljo na spletišču
- Datoteka vsebuje za vsako funkcijo: ime, sintakso, opis, primer in kategorijo
- Dopolnitve ali popravke je mogoče vnesti ročno (glejte Validator JSON)

### Struktura `formula_explanations.json`

```json
{
  "SUM": {
    "sl": {
      "syntax": "SUM(Število1; Število2; ...)",
      "description": "Sešteje vsa števila v obsegu celic.",
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

| Polje | Obvezno | Opis |
|-------|---------|------|
| `syntax` | ✅ | Sintaksa formule s parametri |
| `description` | ✅ | Kratek opis funkcije |
| `example` | ✅ | Primer uporabe kot končna formula |
| `note` | ❌ | Neobvezna opomba |

> 💡 **Opomba:** Če za jezik ni vnosa, se aplikacija samodejno vrne na angleško različico.

---

## 🔍 Validator JSON za jezikovne datoteke

Vgrajeni **Validator JSON** preverja in popravlja `languages.json` in `formula_explanations.json` glede doslednosti, popolnosti in pravilnih imen držav. Dostopen prek **Nastavitve → 🔍 Validator JSON**.

### Kaj se preverja?

#### `languages.json`

- ✅ Vseh 38 jezikov je prisotnih (po kodi ISO 639-1)
- ✅ Pravilna **imena držav in jezikov** (npr. `"sl"` → `"Slovenščina"`)
- ✅ Brez podvojenih jezikovnih kod
- ✅ Obvezna polja so prisotna: `name`, `native_name`, `flag`, `rtl`
- ✅ Zastavica RTL je pravilno nastavljena (Arabščina, Hebrejščina, Perzijščina, Urdujščina → `"rtl": true`)

#### `formula_explanations.json`

- ✅ Vse funkcije iz 4 zavihkov so zabeležene
- ✅ Obvezna polja so prisotna: `syntax`, `description`, `example`
- ✅ Brez praznih polj (`""` ali `null`)
- ✅ Jezikovne kode ustrezajo `languages.json`

### Funkcije popravljanja

| Vrsta napake | Samodejni popravek |
|-------------|-------------------|
| Napačno ime države | Zamenjano s pravilnim po standardu ISO |
| Manjkajoči jezikovni vnos | Dopolnjeno z angleško rezervno različico |
| Prazno obvezno polje | Označeno kot `"[MISSING]"` za ročni pregled |
| Podvojen vnos | Dvojniki so odstranjeni, ohranjen je bolj popoln vnos |
| Napačna zastavica RTL | Samodejno popravljeno na podlagi znanih kod RTL |

### Kako uporabljati

1. Odprite **Nastavitve → 🔍 Validator JSON**
2. Izberite datoteko: `languages.json` ali `formula_explanations.json` (ali obe)
3. **🔎 Preveri** – prikaže vse najdene težave
4. **🛠 Samodejno popravi** – odpravi vse samodejno rešljive napake
5. **💾 Shrani** – atomsko zapiše popravljeno datoteko
6. **📋 Izvozi poročilo** (neobvezno) – shrani besedilno datoteko z vsemi ugotovitvami

> ⚠️ **Opomba:** Pred vsakim samodejnim popravkom se ustvari varnostna kopija izvirne datoteke (`languages.json.bak` / `formula_explanations.json.bak`).

## ⭐ Sistem priljubljenih

- Shranjevanje in ponovna uporaba lastnih formul

- Ločevanje med osebnimi priljubljenimi in priljubljenimi ekipe

- Priljubljene ekipe so zaščitene pred pisanjem (urejanje je dovoljeno samo skrbniku)

- Preprečevanje podvojenih vnosov

- Prosto razvrščanje osebnih priljubljenih

- Sinhronizacija prek omrežnega pogona (po želji nastavljiva)

### Sinhronizacija ekipe

V razdelku **Nastavitve → 🌐 Omrežna pot** lahko vnesete omrežni pogon (npr. `\\\\Strežnik\\Deljeno\\formule`).

- Ob zagonu: priljubljene iz omrežja se shranijo lokalno (varnostna kopija za delo brez povezave)

- Ob shranjevanju: lastne formule se zapišejo v omrežje, formule ekipe ostanejo nespremenjene

## 🛠 Skrbniška plošča

Dostopna prek gumba 🛠. Ob prvem kliku se nastavi geslo (PBKDF2-SHA256, shrani se samo zgoščena vrednost).

- Dodajanje, urejanje in brisanje formul ekipe

- Sprememba gesla

- Zapisovanje sprememb neposredno na omrežni pogon

## 🔌 Upravitelj vtičnikov

Upravitelj vtičnikov (`plugin_manager.py`) je samostojno orodje za ustvarjanje in upravljanje lastnih vtičnikov formul za Calc2. Nahaja se v isti mapi kot `Calc2.py` in se zažene z gumbom 🔌 v Calc2.py:

### Funkcije

- **Ustvari nov vtičnik** – čarovnik po korakih (ime, formule, prevodi, povzetek)

- **Dodaj formule** – dodajanje formul obstoječemu vtičniku

- **Uredi prevode** – prevajanje imen formul v vseh 38 jezikov

- **Odpri mapo vtičnikov** – neposredno v Raziskovalcu datotek

- **Izbriši vtičnik** – z varnostnim potrditvenim pogovorom

### Struktura vtičnika

Vsak vtičnik se nahaja kot podmapa v `plugins/` in je sestavljen iz dveh datotek:

```
plugins/
  moj_vticnik/
    plugin.json      ← metapodatki (ime, različica, avtor, opis)
    formulas.json    ← formule s prevodi
```

**Primer `plugin.json`:**

```
{
  "id": "moj_vticnik",
  "enabled": true,
  "version": "1.0",
  "author": "Vaše ime",
  "icon": "💰",
  "name": { "en": "Finance Formulas", "sl": "Finančne formule" },
  "description": { "en": "Useful formulas for financial calculations." }
}
```

**Primer `formulas.json`:**

```
[
  {
    "formula": "=SUM(A1:A10)",
    "name": { "en": "Sum of range", "sl": "Vsota obsega" },
    "description": { "en": "Adds all values in A1:A10." },
    "category": { "en": "Basic", "sl": "Osnovno" }
  }
]
```

### Pomembno obvestilo (⚠️ Important Notice)

V upravitelju vtičnikov se nahaja gumb **⚠️ Important Notice**. S klikom se odpre okno z vsemi pravili za pravilno ustvarjanje vtičnikov v angleščini. Iste informacije so na voljo tudi v datoteki `IMPORTANT_NOTICE.md`.

## 🌐 Večjezičnost

Na voljo je 38 jezikov, ki jih lahko preklapljate neposredno v aplikaciji.  
Nove jezike lahko dodate prek gumba 🌍 s Čarovnikom za jezike.

**Opomba za hindijščino (हिंदी):** Ob prvem preklopu na hindijščino se pisava *Noto Sans Devanagari* enkrat namesti na ravni sistema. Windows bo pri tem zahteval skrbniške pravice.

## 🔤 Podpora RTL (od desne proti levi)

Jeziki s pisanjem od desne proti levi se samodejno zaznajo in celoten vmesnik se zrcali:

- **Arabščina (عربي)** – samodejno zaznavanje RTL
- **Hebrejščina (עברית)** – samodejno zaznavanje RTL
- **Perzijščina / Farsi (فارسی)** – samodejno zaznavanje RTL
- **Urdujščina (اردو)** – samodejno zaznavanje RTL

**Kaj se spremeni v načinu RTL:** Celotna postavitev vmesnika se zrcali, vnosna polja uporabljajo poravnavo RTL, pisava se samodejno preklopi na združljivo z RTL (npr. *Noto Sans Arabic*, *Noto Sans Hebrew*).

> 💡 **Opomba:** Generirane formule LibreOffice ostanejo vedno v sintaksi LTR – le vmesnik spremeni smer.


## 🗄️ Varnostna kopija in obnovitev

### Ustvarjanje varnostne kopije

Prek **Nastavitve → 🗄️ Ustvari varnostno kopijo**:

1. **Ime** – prosto izbrana oznaka (npr. `Kopija_Maj_2025`)
2. **Geslo** – kopija je šifrirana z AES; brez gesla obnovitev ni mogoča
3. **Mesto shranjevanja** – lokalno ali na omrežnem pogonu
4. Kliknite **💾 Ustvari varnostno kopijo** – ustvari se datoteka `.calc2backup`

**Vsebina:** Vse priljubljene, nastavitve, priljubljene ekipe (neobvezno), nameščeni vtičniki.

### Obnovitev varnostne kopije

Prek **Nastavitve → 📂 Obnovi varnostno kopijo**:

1. Izberite datoteko (`.calc2backup`)
2. Vnesite geslo
3. Izberite obseg: samo priljubljene / samo nastavitve / vse
4. Kliknite **🔄 Obnovi**

> ⚠️ Pri obnovitvi se obstoječi podatki prepišejo. Pred obnovitvijo se ponudi samodejno varnostno kopiranje trenutnih podatkov.


## 💡 Nasveti

- `$A$1` → absolutno sklicevanje (spustni seznam poleg polj za celice)

- **Ctrl+S** → shrani formulo med priljubljene

- **Ctrl+C** → kopiraj formulo (zunaj vnosnih polj)

- **Ctrl+Z / Ctrl+Y** → razveljavi / ponovi

- **Ctrl+F12** → minimiziraj / obnovi okno (deluje tudi, ko je Calc2 minimiziran)

- **Tipka Delete** na seznamu priljubljenih → izbriši vnos

- Formule lahko prilagodite neposredno v izhodnem polju po ustvarjanju

## 📁 Struktura projekta

```
Calc2.py                        ← glavni program
plugin_manager.py               ← upravitelj vtičnikov
IMPORTANT_NOTICE.md             ← opombe o ustvarjanju vtičnikov
data/
  README_de.md / README_en.md / ...      ← pomoč za vsak jezik
  REFERENZ_de.md / REFERENZ_en.md / ...  ← referenca funkcij za vsak jezik
language/
  languages.json                ← prevodi vmesnika (38 jezikov)
  formula_explanations.json
services/
  language_tool.py              ← čarovnik: dodajanje novega jezika
  settings_service.py
  auth_service.py
  favorites_service.py
  network_sync.py
  install_service.py
  backup_service.py             ← varnostna kopija in obnovitev
  json_validator.py             ← preverjanje in popravljanje languages.json / formula_explanations.json
plugins/                        ← mapa vtičnikov (ustvari se samodejno)
  moj_vticnik/
    plugin.json
    formulas.json
fonts/
  NotoSansDevanagari-Regular.ttf  ← pisava za hindijščino
  NotoSansArabic-Regular.ttf      ← arabska pisava (RTL)
  NotoSansHebrew-Regular.ttf      ← hebrejska pisava (RTL)
python/                         ← vgrajeni Python
  python.exe
  ...
settings.json                   ← ustvari se samodejno
priljubljene.json               ← lokalne priljubljene (ustvari se samodejno)
```

## 🧠 Tehnične posebnosti

- **Atomsko pisanje datotek** → preprečuje poškodbe datotek med shranjevanjem

- **Storitvena arhitektura** → logika in uporabniški vmesnik sta strogo ločena

- **Samodejno selitev** → stare oblike priljubljenih se prepoznajo in pretvorijo

- **Zanesljivo obravnavanje napak** → poškodovane datoteke ne povzročijo sesutja programa

- **Označevanje sintakse** → formule so prikazane barvno

- **Temni način** → v celoti podprt

- **Sistem vtičnikov** → Calc2 je mogoče razširiti z lastnimi vtičniki formul

- **Motor RTL** → samodejno zaznavanje RTL-jezikov, popolno zrcaljenje vmesnika z ustreznimi pisavami

- **Varnostna kopija in obnovitev** → varnostne kopije, šifrirane z AES, z imenom in geslom, selektivna obnovitev

- **Validator JSON** → samodejno preverjanje in popravljanje `languages.json` in `formula_explanations.json` vključno z imeni držav in obveznimi polji

- **Vir LibreOffice** → `formula_explanations.json` se polni iz uradne dokumentacije LibreOffice Calc (https://help.libreoffice.org)

- **Globalna bližnjica** → `Ctrl+F12` deluje na ravni sistema prek knjižnice `keyboard` (nit v ozadju)

## Licenca

Prosto za osebno in komercialno uporabo.
