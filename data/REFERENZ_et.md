# Funktsioonide viide – LibreOffice Calc Valemiabi

Kõik programmis saadaval olevad funktsioonid koos süntaksi, parameetrite ja näidetega.

---

## Sakk 1 – Põhifunktsioonid

### Aritmeetikaoperaatorid

| Operaator | Tähendus | Näide | Tulemus |
|-----------|----------|-------|---------|
| `+` | Liitmine | `=A1+B1` | Kahe lahtri summa |
| `-` | Lahutamine | `=A1-B1` | Vahe |
| `*` | Korrutamine | `=A1*B1` | Korrutis |
| `/` | Jagamine | `=A1/B1` | Jagatis |
| `^` | Astendamine | `=A1^2` | A1 ruudus |

---

### SUMMA
**Süntaks:** `=SUMMA(vahemik)`

Liidab kõik arvud lahtrivahemikus.

| Parameeter | Kirjeldus |
|------------|-----------|
| `vahemik` | nt `A1:A10` |

```
=SUMMA(A1:A10)
```

---

### KESKMINE
**Süntaks:** `=KESKMINE(vahemik)`

Arvutab vahemiku kõigi arvude keskmise.

```
=KESKMINE(A1:A10)
```

---

### MIN
**Süntaks:** `=MIN(vahemik)`

Tagastab vahemiku väikseima väärtuse.

```
=MIN(A1:A10)
```

---

### MAX
**Süntaks:** `=MAX(vahemik)`

Tagastab vahemiku suurima väärtuse.

```
=MAX(A1:A10)
```

---

### ARVU
**Süntaks:** `=ARVU(vahemik)`

Loeb kõik **arvväärtustega** lahtrid vahemikus.

```
=ARVU(A1:A10)
```

---

### ARVU2
**Süntaks:** `=ARVU2(vahemik)`

Loeb kõik **mittetühjad** lahtrid (arvud ja tekst).

```
=ARVU2(A1:A10)
```

---

### MEDIAAN
**Süntaks:** `=MEDIAAN(vahemik)`

Tagastab sorteeritud väärtuste loendi keskmise väärtuse.

```
=MEDIAAN(A1:A10)
```

---

### SUMMAKORRUTIS
**Süntaks:** `=SUMMAKORRUTIS(vahemik1; vahemik2)`

Korrutab kahe vahemiku elemendid omavahel ja liidab tulemused.

| Parameeter | Kirjeldus |
|------------|-----------|
| `vahemik1` | Esimene vahemik |
| `vahemik2` | Teine vahemik (sama suurus) |

```
=SUMMAKORRUTIS(A1:A10; B1:B10)
```

---

## Sakk 2 – Täiustatud funktsioonid

### KUI
**Süntaks:** `=KUI(tingimus; siis; muidu)`

Tagastab ühe kahest väärtusest sõltuvalt sellest, kas tingimus on tõene või väär.

| Parameeter | Kirjeldus |
|------------|-----------|
| `tingimus` | nt `A1>0` |
| `siis` | Väärtus, kui tõene |
| `muidu` | Väärtus, kui väär |

```
=KUI(A1>0; "OK"; "Viga")
```

---

### JA
**Süntaks:** `=JA(tingimus1; tingimus2)`

Tagastab TÕENE, kui **kõik** tingimused on täidetud.

```
=JA(A1>0; B1>0)
```

---

### VÕI
**Süntaks:** `=VÕI(tingimus1; tingimus2)`

Tagastab TÕENE, kui **vähemalt üks** tingimus on täidetud.

```
=VÕI(A1>0; B1>0)
```

---

### MITTE
**Süntaks:** `=MITTE(tingimus)`

Pöörab tõeväärtuse ümber: TÕENE → VÄÄR, VÄÄR → TÕENE.

```
=MITTE(A1>0)
```

---

### SUMMAKUI
**Süntaks:** `=SUMMAKUI(vahemik; kriteerium; summa_vahemik)`

Liidab väärtused, mis vastavad kriteeriumile.

| Parameeter | Kirjeldus |
|------------|-----------|
| `vahemik` | Kontrollitav vahemik |
| `kriteerium` | nt `">10"` või `"Jah"` |
| `summa_vahemik` | Liidetav vahemik |

```
=SUMMAKUI(A1:A10; ">10"; B1:B10)
```

---

### LOEKUI
**Süntaks:** `=LOEKUI(vahemik; kriteerium)`

Loeb lahtrid, mis vastavad kriteeriumile.

```
=LOEKUI(A1:A10; "Jah")
```

---

### KESKMINEkui
**Süntaks:** `=KESKMINEkui(vahemik; kriteerium; keskmine_vahemik)`

Arvutab kriteeriumile vastavate väärtuste keskmise.

```
=KESKMINEkui(A1:A10; ">0"; B1:B10)
```

---

### SUMMAKUIS
**Süntaks:** `=SUMMAKUIS(summa_vahemik; kriteerium_vahemik; kriteerium)`

Liidab väärtused, mis vastavad **mitmele** kriteeriumile.

| Parameeter | Kirjeldus |
|------------|-----------|
| `summa_vahemik` | Liidetav vahemik |
| `kriteerium_vahemik` | Kontrollitav vahemik |
| `kriteerium` | Tingimus, nt `">10"` |

```
=SUMMAKUIS(A1:A10; B1:B10; ">10")
```

---

### STDEV
**Süntaks:** `=STDEV(vahemik)`

Arvutab standardhälbe (väärtuste hajuvus).

```
=STDEV(A1:A10)
```

---

### DISPERSIOON
**Süntaks:** `=DISPERSIOON(vahemik)`

Arvutab dispersiooni (ruuthajuvus).

```
=DISPERSIOON(A1:A10)
```

---

### LOETÜHJAD
**Süntaks:** `=LOETÜHJAD(vahemik)`

Loeb kõik **tühjad** lahtrid vahemikus.

```
=LOETÜHJAD(A1:A10)
```

---

### SUUR
**Süntaks:** `=SUUR(vahemik; k)`

Tagastab vahemiku k-nda suurima väärtuse.

| Parameeter | Kirjeldus |
|------------|-----------|
| `vahemik` | Arvude vahemik |
| `k` | Järjestuskoht (1 = suurim, 2 = teiseks suurim, …) |

```
=SUUR(A1:A10; 2)
```

---

## Sakk 3 – Kuupäev ja tekst

### TÄNA
**Süntaks:** `=TÄNA()`

Tagastab tänase kuupäeva. Uueneb iga kord faili avamisel.

```
=TÄNA()
```

---

### PRAEGU
**Süntaks:** `=PRAEGU()`

Tagastab praeguse kuupäeva **koos kellaajaga**.

```
=PRAEGU()
```

---

### AASTA
**Süntaks:** `=AASTA(kuupäev)`

Eraldab kuupäevast aasta.

```
=AASTA(A1)
```

---

### KUU
**Süntaks:** `=KUU(kuupäev)`

Eraldab kuupäevast kuu (1–12).

```
=KUU(A1)
```

---

### PÄEV
**Süntaks:** `=PÄEV(kuupäev)`

Eraldab kuupäevast päeva (1–31).

```
=PÄEV(A1)
```

---

### KUUPÄEV
**Süntaks:** `=KUUPÄEV(aasta; kuu; päev)`

Loob kuupäeva üksikutest väärtustest.

```
=KUUPÄEV(2025; 1; 1)
```

---

### DATEDIF
**Süntaks:** `=DATEDIF(alguskuupäev; lõppkuupäev; ühik)`

Arvutab kahe kuupäeva vahe.

| Ühik | Tähendus |
|------|----------|
| `"D"` | Päevad |
| `"M"` | Kuud |
| `"Y"` | Aastad |

```
=DATEDIF(A1; B1; "D")
```

> **Märkus:** DATEDIF on dokumenteerimata funktsioon – see toimib LibreOffice'is ja Excelis, kuid ei ilmu automaatse täitmise soovitustes.

---

### NÄDALAPÄEV
**Süntaks:** `=NÄDALAPÄEV(kuupäev; tüüp)`

Tagastab nädalapäeva arvuna.

| Tüüp | Tähendus |
|------|----------|
| `2` | 1=E, 2=T, … 7=P (soovitatav) |
| `1` | 1=P, 2=E, … 7=L |

```
=NÄDALAPÄEV(A1; 2)
```

---

### ÜHENDA
**Süntaks:** `=ÜHENDA(tekst1; tekst2; …)`

Ühendab mitu teksti üheks.

```
=ÜHENDA(A1; " "; B1)
```

---

### PIKKUS
**Süntaks:** `=PIKKUS(tekst)`

Tagastab teksti tähemärkide arvu.

```
=PIKKUS(A1)
```

---

### VASAK
**Süntaks:** `=VASAK(tekst; arv)`

Tagastab teksti esimesed n tähemärki.

```
=VASAK(A1; 5)
```

---

### PAREM
**Süntaks:** `=PAREM(tekst; arv)`

Tagastab teksti viimased n tähemärki.

```
=PAREM(A1; 5)
```

---

### KESKOSA
**Süntaks:** `=KESKOSA(tekst; alguspositsioon; arv)`

Tagastab tekstist lõigu.

| Parameeter | Kirjeldus |
|------------|-----------|
| `tekst` | Lähtestekst |
| `alguspositsioon` | Millisest tähemärgist alates (1 = esimene) |
| `arv` | Mitu tähemärki |

```
=KESKOSA(A1; 1; 5)
```

---

### SUUR2
**Süntaks:** `=SUUR2(tekst)`

Teisendab kõik tähed suurtähtedeks.

```
=SUUR2(A1)
```

---

### VÄIKE
**Süntaks:** `=VÄIKE(tekst)`

Teisendab kõik tähed väiketähtedeks.

```
=VÄIKE(A1)
```

---

### TRIM
**Süntaks:** `=TRIM(tekst)`

Eemaldab üleliigsed tühikud (ees, taga ja topelt).

```
=TRIM(A1)
```

---

## Sakk 4 – Otsimine ja ümardamine

### VLOOKUPP
**Süntaks:** `=VLOOKUPP(otsikriteerium; maatriks; veeruindeks; vaste)`

Otsib väärtust tabeli **esimesest veerust** ja tagastab väärtuse teisest veerust.

| Parameeter | Kirjeldus |
|------------|-----------|
| `otsikriteerium` | Otsitav väärtus, nt `A1` |
| `maatriks` | Otsinguvahemik, nt `B1:D10` |
| `veeruindeks` | Tagastatava veeru number (1 = esimene veerg) |
| `vaste` | `0` = täpne, `1` = ligikaudne |

```
=VLOOKUPP(A1; B1:D10; 2; 0)
```

---

### HLOOKUPP
**Süntaks:** `=HLOOKUPP(otsikriteerium; maatriks; reaindeks; vaste)`

Nagu VLOOKUPP, kuid otsib **esimesest reast** (horisontaalselt).

```
=HLOOKUPP(A1; B1:D10; 2; 0)
```

---

### INDEKS
**Süntaks:** `=INDEKS(vahemik; rida; veerg)`

Tagastab väärtuse vahemiku kindlal positsioonil.

| Parameeter | Kirjeldus |
|------------|-----------|
| `vahemik` | Otsinguvahemik |
| `rida` | Rea number |
| `veerg` | Veeru number (vaikimisi: 1) |

```
=INDEKS(B1:B10; 3; 1)
```

---

### VASTE
**Süntaks:** `=VASTE(otsikriteerium; otsinguvahemik; vastetüüp)`

Tagastab väärtuse **positsiooni** vahemikus.

| Vastetüüp | Tähendus |
|-----------|----------|
| `0` | Täpne vaste |
| `1` | Väikseim, mis on suurem või võrdne |
| `-1` | Suurim, mis on väiksem või võrdne |

```
=VASTE(A1; A1:A10; 0)
```

---

### INDEKS + VASTE
**Süntaks:** `=INDEKS(tulemus_vahemik; VASTE(otsikriteerium; otsing_vahemik; 0))`

Paindlikum alternatiiv VLOOKUPP-ile – saab otsida **igas suunas**.

| Parameeter | Kirjeldus |
|------------|-----------|
| `tulemus_vahemik` | Tagastavate väärtustega veerg |
| `otsikriteerium` | Otsitav väärtus |
| `otsing_vahemik` | Veerg, kust otsitakse |

```
=INDEKS(B1:B10; VASTE(A1; A1:A10; 0))
```

> **Eelis VLOOKUPP ees:** Otsinguveerg ei pea olema esimene veerg. Stabiilne ka veergude lisamisel/kustutamisel.

---

### ÜMARDA
**Süntaks:** `=ÜMARDA(arv; komakohad)`

Ümardab määratud komakohani.

| Komakohad | Näide |
|-----------|-------|
| `2` | 3,14159 → 3,14 |
| `0` | 3,7 → 4 |
| `-1` | 34 → 30 |

```
=ÜMARDA(A1; 2)
```

---

### ÜMARDAÜLES
**Süntaks:** `=ÜMARDAÜLES(arv; komakohad)`

Ümardab alati **üles** (nullist eemale).

```
=ÜMARDAÜLES(A1; 2)
```

---

### ÜMARDAALLA
**Süntaks:** `=ÜMARDAALLA(arv; komakohad)`

Ümardab alati **alla** (nulli poole).

```
=ÜMARDAALLA(A1; 2)
```

---

### TÄISARV
**Süntaks:** `=TÄISARV(arv)`

Ümardab lähima täisarvuni **alla** (ka negatiivsete arvude puhul).

```
=TÄISARV(A1)
```

---

### KÄRBI
**Süntaks:** `=KÄRBI(arv; komakohad)`

Kärpib komakohad **ilma ümardamata**.

```
=KÄRBI(A1; 2)
```

---

### ABS
**Süntaks:** `=ABS(arv)`

Tagastab **absoluutväärtuse** (alati positiivne).

```
=ABS(A1)
```

---

### JAK
**Süntaks:** `=JAK(arv; jagaja)`

Tagastab jagamise **jäägi**.

```
=JAK(A1; 3)
```
> Näide: `=JAK(10; 3)` → `1`

---

### RUUTJUUR
**Süntaks:** `=RUUTJUUR(arv)`

Arvutab ruutjuure.

```
=RUUTJUUR(A1)
```

---

### JUHUSARV
**Süntaks:** `=JUHUSARV()`

Tagastab juhusliku kümnendarvu vahemikus 0 kuni 1. Uueneb iga ümberarvutuse korral.

```
=JUHUSARV()
```

> Juhusliku arvu saamiseks vahemikus 1 kuni 100: `=TÄISARV(JUHUSARV()*100)+1`

---

## Absoluutsed viited

Programmis saab viidetüüpi rippmenüüst valida:

| Režiim | Näide | Tähendus |
|--------|-------|----------|
| Suhteline | `A1` | Liigub kopeerimisel kaasa |
| Veerg fikseeritud | `$A1` | Veerg jääb paigale, rida liigub |
| Rida fikseeritud | `A$1` | Rida jääb paigale, veerg liigub |
| Absoluutne | `$A$1` | Jääb kopeerimisel alati samaks |

---

## Kiirklahvid

| Kiirklahv | Funktsioon |
|-----------|-----------|
| `Ctrl+S` | Salvesta valem lemmikutesse |
| `Ctrl+C` | Kopeeri valem |
| `Ctrl+Z` | Võta tagasi |
| `Ctrl+Y` | Tee uuesti |
| `Ctrl+F12` | Minimeeri / taasta aken |
| `Kustuta` | Kustuta lemmik (loendist) |
