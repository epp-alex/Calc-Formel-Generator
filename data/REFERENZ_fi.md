# Funktioviite – LibreOffice Calc -kaavaohje

Kaikki ohjelmassa käytettävissä olevat funktiot syntakseineen, parametreineen ja esimerkkeineen.

---

## Välilehti 1 – Perustoiminnot

### Laskuoperaattorit

| Operaattori | Merkitys | Esimerkki | Tulos |
|-------------|----------|-----------|-------|
| `+` | Yhteenlasku | `=A1+B1` | Kahden solun summa |
| `-` | Vähennyslasku | `=A1-B1` | Erotus |
| `*` | Kertolasku | `=A1*B1` | Tulo |
| `/` | Jakolasku | `=A1/B1` | Osamäärä |
| `^` | Potenssi | `=A1^2` | A1 toiseen potenssiin |

---

### SUMMA
**Syntaksi:** `=SUMMA(alue)`

Laskee yhteen kaikki luvut solualueella.

| Parametri | Kuvaus |
|-----------|--------|
| `alue` | esim. `A1:A10` |

```
=SUMMA(A1:A10)
```

---

### KESKIARVO
**Syntaksi:** `=KESKIARVO(alue)`

Laskee kaikkien alueen lukujen keskiarvon.

```
=KESKIARVO(A1:A10)
```

---

### MIN
**Syntaksi:** `=MIN(alue)`

Palauttaa alueen pienimmän arvon.

```
=MIN(A1:A10)
```

---

### MAKS
**Syntaksi:** `=MAKS(alue)`

Palauttaa alueen suurimman arvon.

```
=MAKS(A1:A10)
```

---

### LASKE
**Syntaksi:** `=LASKE(alue)`

Laskee kaikki **lukuarvoja** sisältävät solut alueella.

```
=LASKE(A1:A10)
```

---

### LASKE2
**Syntaksi:** `=LASKE2(alue)`

Laskee kaikki **ei-tyhjät** solut (luvut ja teksti).

```
=LASKE2(A1:A10)
```

---

### MEDIAANI
**Syntaksi:** `=MEDIAANI(alue)`

Palauttaa järjestetyn arvolistan keskimmäisen arvon.

```
=MEDIAANI(A1:A10)
```

---

### TULOJEN.SUMMA
**Syntaksi:** `=TULOJEN.SUMMA(alue1; alue2)`

Kertoo kahden alueen alkiot keskenään ja laskee tulokset yhteen.

| Parametri | Kuvaus |
|-----------|--------|
| `alue1` | Ensimmäinen alue |
| `alue2` | Toinen alue (sama koko) |

```
=TULOJEN.SUMMA(A1:A10; B1:B10)
```

---

## Välilehti 2 – Lisätoiminnot

### JOS
**Syntaksi:** `=JOS(ehto; sitten; muuten)`

Palauttaa toisen kahdesta arvosta sen mukaan, onko ehto tosi vai epätosi.

| Parametri | Kuvaus |
|-----------|--------|
| `ehto` | esim. `A1>0` |
| `sitten` | Arvo, jos tosi |
| `muuten` | Arvo, jos epätosi |

```
=JOS(A1>0; "OK"; "Virhe")
```

---

### JA
**Syntaksi:** `=JA(ehto1; ehto2)`

Palauttaa TOSI, jos **kaikki** ehdot täyttyvät.

```
=JA(A1>0; B1>0)
```

---

### TAI
**Syntaksi:** `=TAI(ehto1; ehto2)`

Palauttaa TOSI, jos **vähintään yksi** ehto täyttyy.

```
=TAI(A1>0; B1>0)
```

---

### EI
**Syntaksi:** `=EI(ehto)`

Kääntää totuusarvon: TOSI → EPÄTOSI, EPÄTOSI → TOSI.

```
=EI(A1>0)
```

---

### SUMMA.JOS
**Syntaksi:** `=SUMMA.JOS(alue; ehto; summa_alue)`

Laskee yhteen arvot, jotka täyttävät ehdon.

| Parametri | Kuvaus |
|-----------|--------|
| `alue` | Tarkistettava alue |
| `ehto` | esim. `">10"` tai `"Kyllä"` |
| `summa_alue` | Yhteenlaskettava alue |

```
=SUMMA.JOS(A1:A10; ">10"; B1:B10)
```

---

### LASKE.JOS
**Syntaksi:** `=LASKE.JOS(alue; ehto)`

Laskee solut, jotka täyttävät ehdon.

```
=LASKE.JOS(A1:A10; "Kyllä")
```

---

### KESKIARVO.JOS
**Syntaksi:** `=KESKIARVO.JOS(alue; ehto; keskiarvo_alue)`

Laskee ehdon täyttävien arvojen keskiarvon.

```
=KESKIARVO.JOS(A1:A10; ">0"; B1:B10)
```

---

### SUMMA.JOS.JOUKKO
**Syntaksi:** `=SUMMA.JOS.JOUKKO(summa_alue; ehto_alue; ehto)`

Laskee yhteen arvot, jotka täyttävät **useita** ehtoja.

| Parametri | Kuvaus |
|-----------|--------|
| `summa_alue` | Yhteenlaskettava alue |
| `ehto_alue` | Tarkistettava alue |
| `ehto` | Ehto, esim. `">10"` |

```
=SUMMA.JOS.JOUKKO(A1:A10; B1:B10; ">10")
```

---

### KESKIHAJONTA
**Syntaksi:** `=KESKIHAJONTA(alue)`

Laskee keskihajonnan (arvojen hajonta).

```
=KESKIHAJONTA(A1:A10)
```

---

### VAR
**Syntaksi:** `=VAR(alue)`

Laskee varianssin (neliöllinen hajonta).

```
=VAR(A1:A10)
```

---

### LASKE.TYHJÄT
**Syntaksi:** `=LASKE.TYHJÄT(alue)`

Laskee kaikki **tyhjät** solut alueella.

```
=LASKE.TYHJÄT(A1:A10)
```

---

### SUURI
**Syntaksi:** `=SUURI(alue; k)`

Palauttaa alueen k:nneksi suurimman arvon.

| Parametri | Kuvaus |
|-----------|--------|
| `alue` | Lukualue |
| `k` | Sijaluku (1 = suurin, 2 = toiseksi suurin, …) |

```
=SUURI(A1:A10; 2)
```

---

## Välilehti 3 – Päivämäärä ja teksti

### TÄNÄÄN
**Syntaksi:** `=TÄNÄÄN()`

Palauttaa kuluvan päivämäärän. Päivittyy aina tiedostoa avattaessa.

```
=TÄNÄÄN()
```

---

### NYT
**Syntaksi:** `=NYT()`

Palauttaa kuluvan päivämäärän **kellonajan kera**.

```
=NYT()
```

---

### VUOSI
**Syntaksi:** `=VUOSI(päivämäärä)`

Poimii vuoden päivämäärästä.

```
=VUOSI(A1)
```

---

### KUUKAUSI
**Syntaksi:** `=KUUKAUSI(päivämäärä)`

Poimii kuukauden (1–12) päivämäärästä.

```
=KUUKAUSI(A1)
```

---

### PÄIVÄ
**Syntaksi:** `=PÄIVÄ(päivämäärä)`

Poimii päivän (1–31) päivämäärästä.

```
=PÄIVÄ(A1)
```

---

### PÄIVÄMÄÄRÄ
**Syntaksi:** `=PÄIVÄMÄÄRÄ(vuosi; kuukausi; päivä)`

Luo päivämäärän yksittäisistä arvoista.

```
=PÄIVÄMÄÄRÄ(2025; 1; 1)
```

---

### PÄIVÄMÄÄRÄERO
**Syntaksi:** `=PÄIVÄMÄÄRÄERO(alkupäivä; loppupäivä; yksikkö)`

Laskee kahden päivämäärän välisen eron.

| Yksikkö | Merkitys |
|---------|----------|
| `"D"` | Päivät |
| `"M"` | Kuukaudet |
| `"Y"` | Vuodet |

```
=PÄIVÄMÄÄRÄERO(A1; B1; "D")
```

> **Huom.:** PÄIVÄMÄÄRÄERO on dokumentoimaton funktio – se toimii LibreOfficessa ja Excelissä, mutta ei näy automaattisessa täydennyksessä.

---

### VIIKONPÄIVÄ
**Syntaksi:** `=VIIKONPÄIVÄ(päivämäärä; tyyppi)`

Palauttaa viikonpäivän numerona.

| Tyyppi | Merkitys |
|--------|----------|
| `2` | 1=Ma, 2=Ti, … 7=Su (suositeltu) |
| `1` | 1=Su, 2=Ma, … 7=La |

```
=VIIKONPÄIVÄ(A1; 2)
```

---

### KETJUTA
**Syntaksi:** `=KETJUTA(teksti1; teksti2; …)`

Yhdistää useita tekstejä yhdeksi.

```
=KETJUTA(A1; " "; B1)
```

---

### PITUUS
**Syntaksi:** `=PITUUS(teksti)`

Palauttaa tekstin merkkien lukumäärän.

```
=PITUUS(A1)
```

---

### VASEN
**Syntaksi:** `=VASEN(teksti; määrä)`

Palauttaa tekstin ensimmäiset n merkkiä.

```
=VASEN(A1; 5)
```

---

### OIKEA
**Syntaksi:** `=OIKEA(teksti; määrä)`

Palauttaa tekstin viimeiset n merkkiä.

```
=OIKEA(A1; 5)
```

---

### POIMI.TEKSTI
**Syntaksi:** `=POIMI.TEKSTI(teksti; aloituskohta; määrä)`

Palauttaa osan tekstistä.

| Parametri | Kuvaus |
|-----------|--------|
| `teksti` | Lähdeteksti |
| `aloituskohta` | Mistä merkistä alkaen (1 = ensimmäinen) |
| `määrä` | Kuinka monta merkkiä |

```
=POIMI.TEKSTI(A1; 1; 5)
```

---

### ISO.KIRJAIN
**Syntaksi:** `=ISO.KIRJAIN(teksti)`

Muuntaa kaikki kirjaimet isoiksi kirjaimiksi.

```
=ISO.KIRJAIN(A1)
```

---

### PIENI
**Syntaksi:** `=PIENI(teksti)`

Muuntaa kaikki kirjaimet pieniksi kirjaimiksi.

```
=PIENI(A1)
```

---

### SIISTI
**Syntaksi:** `=SIISTI(teksti)`

Poistaa ylimääräiset välilyönnit (alussa, lopussa ja kaksinkertaiset).

```
=SIISTI(A1)
```

---

## Välilehti 4 – Haku ja pyöristys

### PHAKU
**Syntaksi:** `=PHAKU(hakuarvo; matriisi; sarakeindeksi; vastaavuus)`

Etsii arvon taulukon **ensimmäisestä sarakkeesta** ja palauttaa arvon toisesta sarakkeesta.

| Parametri | Kuvaus |
|-----------|--------|
| `hakuarvo` | Haettava arvo, esim. `A1` |
| `matriisi` | Hakualue, esim. `B1:D10` |
| `sarakeindeksi` | Palautettavan sarakkeen numero (1 = ensimmäinen sarake) |
| `vastaavuus` | `0` = tarkka, `1` = likimääräinen |

```
=PHAKU(A1; B1:D10; 2; 0)
```

---

### VHAKU
**Syntaksi:** `=VHAKU(hakuarvo; matriisi; riviindeksi; vastaavuus)`

Kuten PHAKU, mutta etsii **ensimmäisestä rivistä** (vaakasuunnassa).

```
=VHAKU(A1; B1:D10; 2; 0)
```

---

### INDEKSI
**Syntaksi:** `=INDEKSI(alue; rivi; sarake)`

Palauttaa arvon tietyssä alueen kohdassa.

| Parametri | Kuvaus |
|-----------|--------|
| `alue` | Hakualue |
| `rivi` | Rivinumero |
| `sarake` | Sarakenumero (oletus: 1) |

```
=INDEKSI(B1:B10; 3; 1)
```

---

### VASTINE
**Syntaksi:** `=VASTINE(hakuarvo; hakualue; vastaavuustyyppi)`

Palauttaa arvon **sijainnin** alueella.

| Vastaavuustyyppi | Merkitys |
|------------------|----------|
| `0` | Tarkka vastaavuus |
| `1` | Pienin, joka on suurempi tai yhtä suuri |
| `-1` | Suurin, joka on pienempi tai yhtä suuri |

```
=VASTINE(A1; A1:A10; 0)
```

---

### INDEKSI + VASTINE
**Syntaksi:** `=INDEKSI(tulos_alue; VASTINE(hakuarvo; haku_alue; 0))`

Joustavampi vaihtoehto PHAKU:lle – voi hakea **mihin suuntaan tahansa**.

| Parametri | Kuvaus |
|-----------|--------|
| `tulos_alue` | Palautettavat arvot sisältävä sarake |
| `hakuarvo` | Haettava arvo |
| `haku_alue` | Sarake, josta haetaan |

```
=INDEKSI(B1:B10; VASTINE(A1; A1:A10; 0))
```

> **Etu PHAKU:hun nähden:** Hakusarakkeen ei tarvitse olla ensimmäinen sarake. Toimii vakaasti myös sarakkeita lisättäessä tai poistettaessa.

---

### PYÖRISTÄ
**Syntaksi:** `=PYÖRISTÄ(luku; desimaalit)`

Pyöristää määritettyyn desimaalien määrään.

| Desimaalit | Esimerkki |
|------------|-----------|
| `2` | 3,14159 → 3,14 |
| `0` | 3,7 → 4 |
| `-1` | 34 → 30 |

```
=PYÖRISTÄ(A1; 2)
```

---

### PYÖRISTÄ.YLÖS
**Syntaksi:** `=PYÖRISTÄ.YLÖS(luku; desimaalit)`

Pyöristää aina **ylöspäin** (poispäin nollasta).

```
=PYÖRISTÄ.YLÖS(A1; 2)
```

---

### PYÖRISTÄ.ALAS
**Syntaksi:** `=PYÖRISTÄ.ALAS(luku; desimaalit)`

Pyöristää aina **alaspäin** (kohti nollaa).

```
=PYÖRISTÄ.ALAS(A1; 2)
```

---

### KOKONAISLUKU
**Syntaksi:** `=KOKONAISLUKU(luku)`

Pyöristää lähimpään kokonaislukuun **alaspäin** (myös negatiivisilla luvuilla).

```
=KOKONAISLUKU(A1)
```

---

### KATKAISE
**Syntaksi:** `=KATKAISE(luku; desimaalit)`

Katkaisee desimaalit **pyöristämättä**.

```
=KATKAISE(A1; 2)
```

---

### ITSEISARVO
**Syntaksi:** `=ITSEISARVO(luku)`

Palauttaa **itseisarvon** (aina positiivinen).

```
=ITSEISARVO(A1)
```

---

### JAKOJÄÄNNÖS
**Syntaksi:** `=JAKOJÄÄNNÖS(luku; jakaja)`

Palauttaa jakolaskun **jakojäännöksen**.

```
=JAKOJÄÄNNÖS(A1; 3)
```
> Esimerkki: `=JAKOJÄÄNNÖS(10; 3)` → `1`

---

### NELIÖJUURI
**Syntaksi:** `=NELIÖJUURI(luku)`

Laskee neliöjuuren.

```
=NELIÖJUURI(A1)
```

---

### SATUNNAISLUKU
**Syntaksi:** `=SATUNNAISLUKU()`

Palauttaa satunnaisen desimaaliluvun väliltä 0–1. Päivittyy jokaisen uudelleenlaskennan yhteydessä.

```
=SATUNNAISLUKU()
```

> Satunnaisluku väliltä 1–100: `=KOKONAISLUKU(SATUNNAISLUKU()*100)+1`

---

## Absoluuttiset viittaukset

Ohjelmassa viittaustapa voidaan valita pudotusvalikosta:

| Tila | Esimerkki | Merkitys |
|------|-----------|----------|
| Suhteellinen | `A1` | Siirtyy kopioitaessa |
| Sarake kiinnitetty | `$A1` | Sarake pysyy, rivi siirtyy |
| Rivi kiinnitetty | `A$1` | Rivi pysyy, sarake siirtyy |
| Absoluuttinen | `$A$1` | Pysyy aina samana kopioitaessa |

---

## Pikanäppäimet

| Pikanäppäin | Toiminto |
|-------------|----------|
| `Ctrl+S` | Tallenna kaava suosikkeihin |
| `Ctrl+C` | Kopioi kaava |
| `Ctrl+Z` | Kumoa |
| `Ctrl+Y` | Tee uudelleen |
| `Ctrl+F12` | Pienennä / palauta ikkuna |
| `Del` | Poista suosikki (luettelosta) |
