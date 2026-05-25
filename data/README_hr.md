# LibreOffice Calc Pomoćnik za Formule

Python alat za brzo stvaranje, testiranje i upravljanje formulama LibreOffice Calc – s sustavom favorita, sinkronizacijom tima, višejezičnošću i upraviteljem dodataka.

## 🚀 Značajke

- 📑 4 kartice s više od 60 funkcija

- 🌐 38 jezika (uključujući hindi s automatskom instalacijom fonta)

- ⭐ Sustav favorita (lokalni i sinkronizacija tima putem mrežnog pogona)

- 🛠 Administratorska ploča za favourite tima (zaštićena lozinkom)

- 📋 Izravno kopirabilne formule s isticanjem sintakse

- ✏️ Polje za izlaz koje se može uređivati s Poništi/Ponovi

- 📖 Ugrađena pomoć i referenca funkcija (po jeziku)

- 💾 Automatsko spremanje (JSON, atomski zapisano)

- 🌙 Tamni način rada

- 🔌 Upravitelj dodataka za stvaranje vlastitih dodataka za formule

- 🔤 RTL podrška (zdesna nalijevo) – automatsko prepoznavanje smjera pisanja

- 🗄️ Sigurnosna kopija i obnova – spremi sve postavke i favourite s imenom i lozinkom

- ⌨️ Globalna tipkovnička prečica `Ctrl+F12` za minimiziranje/vraćanje
- 🔍 JSON validator – automatska provjera i ispravak `languages.json` i `formula_explanations.json`

## 🖥️ Korištenje

**1. Unos podataka**

- Raspon ćelija (npr. `A1:A10`)

- Ćelija 1 / Ćelija 2 (npr. `A1`, `B1`)

- Neobavezni parametar (npr. tekst ili indeks)

- Odabir načina apsolutne reference: `A1`, `$A1`, `A$1`, `$A$1`

**2. Odabir funkcije** Odaberite karticu i kliknite na funkciju – formula se odmah generira.

**3. Prilagodba formule** Generiranu formulu moguće je izravno urediti u polju za izlaz.

**4. Kopiranje** Jednim klikom u međuspremnik (uključujući boje sintakse).

**5. Korištenje favorita**

- ⭐ Spremi → spremi trenutnu formulu (Ctrl+S)

- 📂 Učitaj → ponovna upotreba formule

- ❌ Izbriši → tipka Del ili gumb

- 🕐 Povijest → nedavno korištene formule

## 📊 Pregled kartica

**Kartica 1 – Osnovne funkcije** `+` `-` `\*` `/` `^` SUM, AVERAGE, MIN, MAX, MEDIAN, COUNT, COUNTA, SUMPRODUCT

**Kartica 2 – Napredne funkcije** IF, AND, OR, NOT SUMIF, COUNTIF, AVERAGEIF, SUMIFS, STDEV, VAR, COUNTBLANK, LARGE

**Kartica 3 – Datum i tekst** TODAY, NOW, YEAR, MONTH, DAY, DATE, DATEDIF, WEEKDAY CONCATENATE, LEN, LEFT, RIGHT, MID, UPPER, LOWER, TRIM

**Kartica 4 – Pretraživanje i zaokruživanje** VLOOKUP, HLOOKUP, INDEX, MATCH, INDEX+MATCH ROUND, ROUNDUP, ROUNDDOWN, INT, TRUNC, ABS, MOD, SQRT, RAND


## 📖 Objašnjenja formula iz dokumentacije LibreOffice

Datoteka `formula_explanations.json` popunjava se izravno iz **službene dokumentacije LibreOffice Calc** (https://help.libreoffice.org).

### Izvor podataka i ažuriranje

- Opisi, sintaksni podaci i primjeri preuzimaju se sa službene stranice za pomoć LibreOffice-a
- Podržani jezici ovise o prijevodima dostupnim na stranici
- Datoteka sadrži za svaku funkciju: naziv, sintaksu, opis, primjer i kategoriju
- Dodaci ili ispravci mogu se ručno unijeti (pogledajte JSON validator)

### Struktura `formula_explanations.json`

```json
{
  "SUM": {
    "hr": {
      "syntax": "SUM(Broj1; Broj2; ...)",
      "description": "Zbraja sve brojeve u rasponu ćelija.",
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

| Polje | Obavezno | Opis |
|-------|---------|------|
| `syntax` | ✅ | Sintaksa formule s parametrima |
| `description` | ✅ | Kratki opis funkcije |
| `example` | ✅ | Primjer korištenja kao gotova formula |
| `note` | ❌ | Opcionalna napomena |

> 💡 **Napomena:** Ako za neki jezik nema unosa, aplikacija se automatski vraća na englesku verziju.

---

## 🔍 JSON validator za jezične datoteke

Ugrađeni **JSON validator** provjerava i ispravlja `languages.json` i `formula_explanations.json` za konzistentnost, potpunost i ispravne nazive zemalja.

Dostupan putem **Postavke → 🔍 JSON validator**.

### Što se provjerava?

#### `languages.json`

- ✅ Svih 38 jezika prisutno (prema ISO 639-1 kodu)
- ✅ Ispravni **nazivi zemalja i jezika** (npr. `"hr"` → `"Hrvatski"`)
- ✅ Bez duplikata jezičnih kodova
- ✅ Obavezna polja prisutna: `name`, `native_name`, `flag`, `rtl`
- ✅ RTL oznaka ispravno postavljena (Arapski, Hebrejski, Perzijski, Urdu → `"rtl": true`)

#### `formula_explanations.json`

- ✅ Sve funkcije iz 4 kartice unesene
- ✅ Obavezna polja prisutna: `syntax`, `description`, `example`
- ✅ Bez praznih polja (`""` ili `null`)
- ✅ Jezični kodovi odgovaraju `languages.json`

### Funkcije ispravka

| Vrsta greške | Automatski ispravak |
|-------------|---------------------|
| Pogrešan naziv države | Zamijenjen ispravnim nazivom prema ISO standardu |
| Nedostajući jezični unos | Popunjen engleskim zamjenskim unosom |
| Prazno obavezno polje | Označeno kao `"[MISSING]"` za ručnu provjeru |
| Duplicirani unos | Duplikati uklonjeni, zadržan potpuniji unos |
| Pogrešna RTL oznaka | Automatski ispravljena prema poznatim RTL kodovima |

### Kako koristiti

1. Otvorite **Postavke → 🔍 JSON validator**
2. Odaberite datoteku: `languages.json` ili `formula_explanations.json` (ili obje)
3. **🔎 Provjeri** – prikazuje sve pronađene probleme
4. **🛠 Automatski ispravi** – rješava sve automatski rješive greške
5. **💾 Spremi** – atomski zapisuje ispravku datoteke
6. **📋 Izvezi izvješće** (opcionalno) – sprema tekstualnu datoteku sa svim nalazima

> ⚠️ **Napomena:** Prije svakog automatskog ispravka stvara se sigurnosna kopija izvorne datoteke (`languages.json.bak` / `formula_explanations.json.bak`).

## ⭐ Sustav favorita

- Spremanje i ponovna upotreba vlastitih formula

- Odvojenost osobnih favorita i favorita tima

- Favoriti tima su samo za čitanje (samo administrator može uređivati)

- Duplikati su spriječeni

- Slobodno sortiranje osobnih favorita

- Sinkronizacija putem mrežnog pogona (opcijski konfigurirano)

### Sinkronizacija tima

Putem **Postavke → 🌐 Mrežna putanja** može se unijeti mrežni pogon (npr. `\\\\Poslužitelj\\Dijeljenje\\formule`).

- Pri pokretanju: mrežni favoriti se spremaju lokalno (pričuvna kopija bez mreže)

- Pri spremanju: vlastite formule se zapisuju na mrežu, timske formule ostaju netaknute

## 🛠 Administratorska ploča

Dostupna putem gumba 🛠. Pri prvom kliku postavlja se lozinka (PBKDF2-SHA256, sprema se samo hash).

- Dodavanje, uređivanje i brisanje timskih formula

- Promjena lozinke

- Promjene se izravno zapisuju na mrežni pogon

## 🔌 Upravitelj dodataka

Upravitelj dodataka (`plugin_manager.py`) samostalan je alat za stvaranje i upravljanje vlastitim dodacima za formule za Calc2. Nalazi se u istoj mapi kao i `Calc2.py` i pokreće se gumbom 🔌 u Calc2.py:

### Funkcije

- **Stvaranje novog dodatka** – čarobnjak korak po korak (ime, formule, prijevodi, sažetak)

- **Dodavanje formula** – nadopuna postojećeg dodatka formulama

- **Uređivanje prijevoda** – prevođenje naziva formula na sva 38 jezika

- **Otvaranje mape dodataka** – izravno u upravitelju datoteka

- **Brisanje dodatka** – s potvrdnim upitom

### Struktura dodatka

Svaki dodatak nalazi se kao podmapa u `plugins/` i sastoji se od dvije datoteke:

```
plugins/
  moj_dodatak/
    plugin.json      ← metapodaci (ime, verzija, autor, opis)
    formulas.json    ← formule s prijevodima
```

**Primjer `plugin.json`:**

```
{
  "id": "moj_dodatak",
  "enabled": true,
  "version": "1.0",
  "author": "Vaše Ime",
  "icon": "💰",
  "name": { "en": "Finance Formulas", "hr": "Financijske formule" },
  "description": { "en": "Useful formulas for financial calculations." }
}
```

**Primjer `formulas.json`:**

```
[
  {
    "formula": "=SUM(A1:A10)",
    "name": { "en": "Sum of range", "hr": "Zbroj raspona" },
    "description": { "en": "Adds all values in A1:A10." },
    "category": { "en": "Basic", "hr": "Osnovno" }
  }
]
```

### Važna napomena (⚠️ Important Notice)

U upravitelju dodataka nalazi se gumb **⚠️ Important Notice**. Klikom se otvara prozor sa svim pravilima za ispravno stvaranje dodataka na engleskom jeziku. Iste informacije dostupne su i u `IMPORTANT_NOTICE.md`.

## 🌐 Višejezičnost

38 jezika dostupna, izmjenjiva izravno u aplikaciji.
Novi jezici mogu se dodati putem gumba 🌍 pomoću čarobnjaka za jezike.

**Napomena o hindiju (हिंदी):** Prilikom prvog prebacivanja na hindi, font *Noto Sans Devanagari* instalira se jednom na razini sustava. Windows će zatražiti administratorska prava.

## 🔤 RTL podrška (zdesna nalijevo)

Jezici s pismom zdesna nalijevo automatski se prepoznaju i cijelo sučelje se zrcali:

- **Arapski (عربي)** – automatsko RTL prepoznavanje
- **Hebrejski (עברית)** – automatsko RTL prepoznavanje
- **Perzijski / Farsi (فارسی)** – automatsko RTL prepoznavanje
- **Urdu (اردو)** – automatsko RTL prepoznavanje

**Što se mijenja u RTL načinu:** Cijeli raspored UI-ja se zrcali, polja za unos koriste RTL poravnanje, font se automatski mijenja na RTL-kompatibilan (npr. *Noto Sans Arabic*, *Noto Sans Hebrew*).

> 💡 **Napomena:** Generirane LibreOffice formule uvijek ostaju u LTR sintaksi – samo se korisničko sučelje mijenja.


## 🗄️ Sigurnosna kopija i obnova

### Stvaranje sigurnosne kopije

Putem **Postavke → 🗄️ Stvori sigurnosnu kopiju**:

1. **Naziv** – slobodan opis (npr. `Kopija_Svibanj_2025`)
2. **Lozinka** – kopija se šifrira AES-om; bez lozinke obnova nije moguća
3. **Mjesto pohrane** – lokalno ili mrežni pogon
4. Kliknite **💾 Stvori sigurnosnu kopiju** – stvara se `.calc2backup` datoteka

**Sadržaj:** Svi favoriti, postavke, timski favoriti (opcionalno), instalirani dodaci.

### Obnova sigurnosne kopije

Putem **Postavke → 📂 Obnovi sigurnosnu kopiju**:

1. Odaberite datoteku (`.calc2backup`)
2. Unesite lozinku
3. Odaberite opseg: samo favoriti / samo postavke / sve
4. Kliknite **🔄 Obnovi**

> ⚠️ Pri obnovi postojeći podaci se prepisuju. Prije obnove nudi se automatska sigurnosna kopija trenutnih podataka.


## 💡 Savjeti

- `$A$1` → apsolutna referenca (padajući izbornik pored polja za ćelije)

- **Ctrl+S** → spremi formulu u favorite

- **Ctrl+C** → kopiraj formulu (izvan polja za unos)

- **Ctrl+Z / Ctrl+Y** → Poništi / Ponovi

- **Ctrl+F12** → minimiziraj/vrati prozor (radi čak i kada je Calc2 minimiziran)

- **Tipka Del** na popisu favorita → brisanje unosa

- Formule se mogu prilagoditi izravno u polju za izlaz nakon generiranja

## 📁 Struktura projekta

```
Calc2.py                        ← glavni program
plugin_manager.py               ← upravitelj dodataka
IMPORTANT_NOTICE.md             ← upute za stvaranje dodataka
data/
  README_hr.md / README_en.md / ...      ← pomoć po jeziku
  REFERENCA_hr.md / REFERENCA_en.md / ... ← referenca funkcija po jeziku
language/
  languages.json                ← prijevodi sučelja (38 jezika)
  formula_explanations.json
services/
  language_tool.py              ← čarobnjak: dodavanje novog jezika
  settings_service.py
  auth_service.py
  favorites_service.py
  network_sync.py
  install_service.py
  backup_service.py             ← sigurnosna kopija i obnova
  json_validator.py             ← provjera i ispravak languages.json / formula_explanations.json
plugins/                        ← mapa dodataka (automatski stvorena)
  moj_dodatak/
    plugin.json
    formulas.json
fonts/
  NotoSansDevanagari-Regular.ttf  ← hindi font
  NotoSansArabic-Regular.ttf      ← arapski font (RTL)
  NotoSansHebrew-Regular.ttf      ← hebrejski font (RTL)
python/                         ← ugrađeni Python
  python.exe
  ...
settings.json                   ← automatski se stvara
favoriti.json                   ← lokalni favoriti (automatski se stvara)
```

## 🧠 Tehnički highlights

- **Atomsko zapisivanje datoteka** → sprječava oštećenje datoteka pri spremanju

- **Servisna arhitektura** → logika i korisničko sučelje strogo su odvojeni

- **Automatska migracija** → stari formati favorita se prepoznaju i pretvaraju

- **Robusno upravljanje greškama** → oštećene datoteke ne uzrokuju pad aplikacije

- **Isticanje sintakse** → formule se prikazuju u boji

- **Tamni način rada** → potpuno podržan

- **Sustav dodataka** → Calc2 se može proširiti vlastitim dodacima za formule

- **RTL motor** → automatsko prepoznavanje RTL jezika, potpuno zrcaljenje UI-ja s odgovarajućim fontovima

- **Sigurnosna kopija i obnova** → AES-šifrirane sigurnosne kopije s imenom i lozinkom, selektivna obnova

- **JSON validator** → automatska provjera i ispravak `languages.json` i `formula_explanations.json` uključujući nazive zemalja i obavezna polja

- **Izvor LibreOffice** → `formula_explanations.json` popunjava se iz službene dokumentacije LibreOffice Calc (https://help.libreoffice.org)

- **Globalna tipkovnička prečica** → `Ctrl+F12` radi na razini sustava putem biblioteke `keyboard` (pozadinska nit)

## Licenca

Slobodno za korištenje u osobne i komercijalne svrhe.
