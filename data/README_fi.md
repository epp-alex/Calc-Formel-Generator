# LibreOffice Calc Kaavatyökalu

Python-työkalu LibreOffice Calc -kaavojen nopeaan luomiseen, testaamiseen ja hallintaan – suosikkijärjestelmällä, tiimin synkronoinnilla, monikielisyydellä ja laajennushallinnalla.

## 🚀 Ominaisuudet

- 📑 4 välilehteä yli 60 funktiolla

- 🌐 38 kieltä (ml. hindi automaattisella fontin asennuksella)

- ⭐ Suosikkijärjestelmä (paikallinen ja tiimin synkronointi verkkoaseman kautta)

- 🛠 Hallintapaneeli tiimin suosikeille (salasanasuojattu)

- 📋 Suoraan kopioitavat kaavat syntaksin korostuksella

- ✏️ Muokattava tulostuskenttä Kumoa/Tee uudelleen -tuella

- 📖 Sisäänrakennettu ohje ja funktioviite (kielikohtainen)

- 💾 Automaattinen tallennus (JSON, atomisesti kirjoitettu)

- 🌙 Tumma tila

- 🔌 Laajennushallinta omien kaavalaajennusten luomiseen

- 🔤 RTL-tuki (oikealta vasemmalle) – kirjoitussuunnan automaattinen tunnistus

- 🗄️ Varmuuskopio ja palautus – tallenna kaikki asetukset ja suosikit nimellä ja salasanalla

- ⌨️ Yleinen pikanäppäin `Ctrl+F12` pienentämiseen/palauttamiseen
- 🔍 JSON-validaattori – `languages.json` ja `formula_explanations.json` automaattinen tarkistus ja korjaus

## 🖥️ Käyttö

**1. Syötä tiedot**

- Solualue (esim. `A1:A10`)

- Solu 1 / Solu 2 (esim. `A1`, `B1`)

- Valinnainen parametri (esim. teksti tai indeksi)

- Absoluuttinen viittaustila valittavissa: `A1`, `$A1`, `A$1`, `$A$1`

**2. Valitse funktio** Valitse välilehti ja napsauta funktiota – kaava luodaan välittömästi.

**3. Muokkaa kaavaa** Luotua kaavaa voi muokata suoraan tulostuskentässä.

**4. Kopioi** Yhdellä napsautuksella leikepöydälle (syntaksin värit mukaan lukien).

**5. Käytä suosikkeja**

- ⭐ Tallenna → tallenna nykyinen kaava (Ctrl+S)

- 📂 Lataa → käytä kaavaa uudelleen

- ❌ Poista → Delete-näppäin tai painike

- 🕐 Historia → viimeksi käytetyt kaavat

## 📊 Välilehtien yleiskatsaus

**Välilehti 1 – Perustoiminnot** `+` `-` `\*` `/` `^` SUM, AVERAGE, MIN, MAX, MEDIAN, COUNT, COUNTA, SUMPRODUCT

**Välilehti 2 – Edistyneet funktiot** IF, AND, OR, NOT SUMIF, COUNTIF, AVERAGEIF, SUMIFS, STDEV, VAR, COUNTBLANK, LARGE

**Välilehti 3 – Päivämäärä ja teksti** TODAY, NOW, YEAR, MONTH, DAY, DATE, DATEDIF, WEEKDAY CONCATENATE, LEN, LEFT, RIGHT, MID, UPPER, LOWER, TRIM

**Välilehti 4 – Haku ja pyöristys** VLOOKUP, HLOOKUP, INDEX, MATCH, INDEX+MATCH ROUND, ROUNDUP, ROUNDDOWN, INT, TRUNC, ABS, MOD, SQRT, RAND


## 📖 Kaavojen selitykset LibreOffice-dokumentaatiosta

Tiedosto `formula_explanations.json` täytetään suoraan virallisesta **LibreOffice Calc -dokumentaatiosta** (https://help.libreoffice.org).

### Tietolähde ja päivitys

- Kuvaukset, syntaksitiedot ja esimerkit haetaan LibreOffice:n viralliselta ohjesivustolta
- Tuetut kielet riippuvat sivustolla saatavilla olevista käännöksistä
- Tiedosto sisältää jokaiselle funktiolle: nimen, syntaksin, kuvauksen, esimerkin ja kategorian
- Lisäyksiä tai korjauksia voi tehdä manuaalisesti (ks. JSON-validaattori)

### `formula_explanations.json`-rakenne

```json
{
  "SUM": {
    "fi": {
      "syntax": "SUM(Luku1; Luku2; ...)",
      "description": "Laskee yhteen kaikki luvut solualueella.",
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

| Kenttä | Pakollinen | Kuvaus |
|--------|-----------|--------|
| `syntax` | ✅ | Kaavan syntaksi parametreineen |
| `description` | ✅ | Funktion lyhyt kuvaus |
| `example` | ✅ | Käyttöesimerkki valmiina kaavana |
| `note` | ❌ | Valinnainen huomio |

> 💡 **Huomio:** Jos kielelle ei löydy merkintää, sovellus palautuu automaattisesti englanninkieliseen versioon.

---

## 🔍 JSON-validaattori kielitiedostoille

Integroitu **JSON-validaattori** tarkistaa ja korjaa `languages.json`- ja `formula_explanations.json`-tiedostot johdonmukaisuuden, täydellisyyden ja oikeiden maaninitysten osalta.

Saavutettavissa: **Asetukset → 🔍 JSON-validaattori**.

### Mitä tarkistetaan?

#### `languages.json`

- ✅ Kaikki 38 kieltä löytyvät (ISO 639-1 -kielikoodin mukaan)
- ✅ Oikeat **maa- ja kielinimet** (esim. `"fi"` → `"Suomi"`)
- ✅ Ei päällekkäisiä kielikoodeja
- ✅ Pakolliset kentät läsnä: `name`, `native_name`, `flag`, `rtl`
- ✅ RTL-lippu asetettu oikein (Arabia, Heprea, Persia, Urdu → `"rtl": true`)

#### `formula_explanations.json`

- ✅ Kaikki 4 välilehden funktiot kirjattu
- ✅ Pakolliset kentät läsnä: `syntax`, `description`, `example`
- ✅ Ei tyhjiä kenttiä (`""` tai `null`)
- ✅ Kielikoodit vastaavat `languages.json`-tiedostoa

### Korjaustoiminnot

| Virhetyyppi | Automaattinen korjaus |
|-------------|----------------------|
| Väärä maanimi | Korvataan ISO-standardin mukaisella oikealla nimellä |
| Puuttuva kielimerkintä | Täytetään englanninkielisellä varamerkinnällä |
| Tyhjä pakollinen kenttä | Merkitään `"[MISSING]"` manuaalista tarkistusta varten |
| Päällekkäinen merkintä | Kaksoiskappaleet poistetaan, täydellisempi säilytetään |
| Väärä RTL-lippu | Korjataan automaattisesti tunnettujen RTL-koodien perusteella |

### Käyttö

1. Avaa **Asetukset → 🔍 JSON-validaattori**
2. Valitse tiedosto: `languages.json` tai `formula_explanations.json` (tai molemmat)
3. **🔎 Tarkista** – näyttää kaikki löydetyt ongelmat
4. **🛠 Korjaa automaattisesti** – korjaa kaikki automaattisesti ratkaistavissa olevat virheet
5. **💾 Tallenna** – kirjoittaa korjatun tiedoston atomisesti
6. **📋 Vie raportti** (valinnainen) – tallentaa tekstitiedoston kaikilla löydöksillä

> ⚠️ **Huomio:** Ennen jokaista automaattista korjausta luodaan varmuuskopio alkuperäisestä tiedostosta (`languages.json.bak` / `formula_explanations.json.bak`).

## ⭐ Suosikkijärjestelmä

- Tallenna ja käytä uudelleen omia kaavoja

- Omat suosikit ja tiimin suosikit erillään

- Tiimin suosikit ovat vain luku -tilassa (vain järjestelmänvalvoja voi muokata)

- Kaksoiskappaleet estetään

- Omien suosikkien vapaa järjestely

- Synkronointi verkkoaseman kautta (valinnainen asetus)

### Tiimin synkronointi

**Asetukset → 🌐 Verkkoasema** -kohdasta voi syöttää verkkoaseman osoitteen (esim. `\\\\Palvelin\\Jako\\kaavat`).

- Käynnistyksen yhteydessä: verkkosuosikit tallennetaan paikallisesti (offline-varakopio)

- Tallennuksen yhteydessä: omat kaavat kirjoitetaan verkkoon, tiimin kaavat jäävät koskemattomiksi

## 🛠 Hallintapaneeli

Saavutettavissa 🛠-painikkeella. Ensimmäisellä napsautuksella asetetaan salasana (PBKDF2-SHA256, vain tiiviste tallennetaan).

- Tiimin kaavojen lisääminen, muokkaaminen ja poistaminen

- Salasanan vaihtaminen

- Muutokset kirjoitetaan suoraan verkkoasemalle

## 🔌 Laajennushallinta

Laajennushallinta (`plugin_manager.py`) on itsenäinen työkalu omien kaavalaajennusten luomiseen ja hallintaan Calc2-ohjelmalle. Se sijaitsee samassa kansiossa kuin `Calc2.py` ja käynnistetään 🔌-painikkeella Calc2.py:ssä:

### Toiminnot

- **Luo uusi laajennus** – vaiheittainen ohjattu toiminto (nimi, kaavat, käännökset, yhteenveto)

- **Lisää kaavoja** – täydennä olemassa olevaa laajennusta kaavoilla

- **Muokkaa käännöksiä** – käännä kaavanimet kaikkiin 38 kieleen

- **Avaa laajennuskansio** – suoraan tiedostohallinnassa

- **Poista laajennus** – turvallisuusvahvistuksella

### Laajennuksen rakenne

Jokainen laajennus sijaitsee alikansiona `plugins/`-hakemistossa ja koostuu kahdesta tiedostosta:

```
plugins/
  oma_laajennus/
    plugin.json      ← metatiedot (nimi, versio, tekijä, kuvaus)
    formulas.json    ← kaavat käännöksineen
```

**Esimerkki `plugin.json`:**

```
{
  "id": "oma_laajennus",
  "enabled": true,
  "version": "1.0",
  "author": "Sinun Nimesi",
  "icon": "💰",
  "name": { "en": "Finance Formulas", "fi": "Talouskaavat" },
  "description": { "en": "Useful formulas for financial calculations." }
}
```

**Esimerkki `formulas.json`:**

```
[
  {
    "formula": "=SUM(A1:A10)",
    "name": { "en": "Sum of range", "fi": "Alueen summa" },
    "description": { "en": "Adds all values in A1:A10." },
    "category": { "en": "Basic", "fi": "Perustoiminnot" }
  }
]
```

### Tärkeä huomio (⚠️ Important Notice)

Laajennushallinnassa on painike **⚠️ Important Notice**. Napsauttamalla avautuu ikkuna, jossa on kaikki laajennusten oikean luomisen säännöt englanniksi. Samat tiedot löytyvät myös tiedostosta `IMPORTANT_NOTICE.md`.

## 🌐 Monikielisyys

38 kieltä saatavilla, vaihdettavissa suoraan sovelluksessa.
Uusia kieliä voi lisätä 🌍-painikkeella ohjatun kielitoiminnon avulla.

**Huomio hindistä (हिंदी):** Ensimmäisellä kertaa hindiin vaihdettaessa asennetaan kerran *Noto Sans Devanagari* -fontti järjestelmätasolla. Windows pyytää järjestelmänvalvojan oikeuksia.

## 🔤 RTL-tuki (oikealta vasemmalle)

Oikealta vasemmalle kirjoitettavat kielet tunnistetaan automaattisesti ja koko käyttöliittymä peilataan:

- **Arabia (عربي)** – automaattinen RTL-tunnistus
- **Heprea (עברית)** – automaattinen RTL-tunnistus
- **Persia / Farsi (فارسی)** – automaattinen RTL-tunnistus
- **Urdu (اردو)** – automaattinen RTL-tunnistus

**Mitä muuttuu RTL-tilassa:** Koko UI-asettelu peilataan, syöttökentät käyttävät RTL-tasausta, fontti vaihtuu automaattisesti RTL-yhteensopivaan (esim. *Noto Sans Arabic*, *Noto Sans Hebrew*).

> 💡 **Huomio:** Luodut LibreOffice-kaavat pysyvät aina LTR-syntaksissa – vain käyttöliittymä vaihtaa suuntaa.


## 🗄️ Varmuuskopio ja palautus

### Varmuuskopion luominen

**Asetukset → 🗄️ Luo varmuuskopio** -kohdasta:

1. **Nimi** – vapaavalintainen nimitys (esim. `Varmuuskopio_toukokuu_2025`)
2. **Salasana** – varmuuskopio salataan AES:llä; ilman salasanaa palautus ei onnistu
3. **Tallennuspaikka** – paikallinen tai verkkoasema
4. Napsauta **💾 Luo varmuuskopio** – luodaan `.calc2backup`-tiedosto

**Sisältö:** Kaikki suosikit, asetukset, tiimin suosikit (valinnainen), asennetut laajennukset.

### Varmuuskopion palauttaminen

**Asetukset → 📂 Palauta varmuuskopio** -kohdasta:

1. Valitse varmuuskopiotiedosto (`.calc2backup`)
2. Anna salasana
3. Valitse palautuslaajuus: vain suosikit / vain asetukset / kaikki
4. Napsauta **🔄 Palauta**

> ⚠️ Palautuksen yhteydessä olemassa olevat tiedot ylikirjoitetaan. Ennen palautusta tarjotaan automaattinen varmuuskopio nykyisistä tiedoista.


## 💡 Vinkit

- `$A$1` → absoluuttinen viittaus (pudotusvalikko solukenttien vieressä)

- **Ctrl+S** → tallenna kaava suosikkeihin

- **Ctrl+C** → kopioi kaava (syöttökenttien ulkopuolella)

- **Ctrl+Z / Ctrl+Y** → Kumoa / Tee uudelleen

- **Ctrl+F12** → pienennä/palauta ikkuna (toimii myös silloin kun Calc2 on pienennetty)

- **Delete-näppäin** suosikkiluettelossa → poista merkintä

- Kaavoja voi muokata suoraan tulostuskentässä luomisen jälkeen

## 📁 Projektin rakenne

```
Calc2.py                        ← pääohjelma
plugin_manager.py               ← laajennushallinta
IMPORTANT_NOTICE.md             ← ohjeet laajennusten luomiseen
data/
  README_fi.md / README_en.md / ...      ← ohje kielikohtaisesti
  VIITE_fi.md / VIITE_en.md / ...        ← funktioviite kielikohtaisesti
language/
  languages.json                ← käyttöliittymän käännökset (38 kieltä)
  formula_explanations.json
services/
  language_tool.py              ← ohjattu toiminto: lisää uusi kieli
  settings_service.py
  auth_service.py
  favorites_service.py
  network_sync.py
  install_service.py
  backup_service.py             ← varmuuskopio ja palautus
  json_validator.py             ← languages.json / formula_explanations.json tarkistus ja korjaus
plugins/                        ← laajennuskansio (luodaan automaattisesti)
  oma_laajennus/
    plugin.json
    formulas.json
fonts/
  NotoSansDevanagari-Regular.ttf  ← hindi-fontti
  NotoSansArabic-Regular.ttf      ← arabia-fontti (RTL)
  NotoSansHebrew-Regular.ttf      ← heprea-fontti (RTL)
python/                         ← upotettu Python
  python.exe
  ...
settings.json                   ← luodaan automaattisesti
suosikit.json                   ← paikalliset suosikit (luodaan automaattisesti)
```

## 🧠 Tekniset erityispiirteet

- **Atominen tiedostokirjoitus** → estää tiedostojen vahingoittumisen tallennuksen aikana

- **Palveluarkkitehtuuri** → logiikka ja käyttöliittymä tiukasti erotettu toisistaan

- **Automaattinen siirto** → vanhat suosikkiformaatit tunnistetaan ja muunnetaan

- **Vankka virheenkäsittely** → vialliset tiedostot eivät kaada sovellusta

- **Syntaksin korostus** → kaavat näytetään värillisinä

- **Tumma tila** → täysin tuettu

- **Laajennusjärjestelmä** → Calc2 on laajennettavissa omilla kaavalaajennuksilla

- **RTL-moottori** → RTL-kielten automaattinen tunnistus, täydellinen UI:n peilaus sopivine fontteineen

- **Varmuuskopio ja palautus** → AES-salatut varmuuskopiot nimellä ja salasanalla, valikoiva palautus

- **JSON-validaattori** → `languages.json` ja `formula_explanations.json` automaattinen tarkistus ja korjaus ml. maanimet ja pakolliset kentät

- **LibreOffice-lähde** → `formula_explanations.json` täytetään virallisesta LibreOffice Calc -dokumentaatiosta (https://help.libreoffice.org)

- **Yleinen pikanäppäin** → `Ctrl+F12` toimii järjestelmätasolla `keyboard`-kirjaston kautta (taustasäie)

## Lisenssi

Vapaasti käytettävissä henkilökohtaisiin ja kaupallisiin tarkoituksiin.
