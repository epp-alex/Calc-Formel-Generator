# Funktionsoversigt – LibreOffice Calc Formula Helper

Alle funktioner tilgængelige i programmet, med syntaks, parametre og eksempler.

---

## Fane 1 – Grundlæggende funktioner

### Aritmetiske operatorer

| Operator | Betydning | Eksempel | Resultat |
|----------|-----------|---------|---------|
| `+` | Addition | `=A1+B1` | Sum af to celler |
| `-` | Subtraktion | `=A1-B1` | Forskel |
| `*` | Multiplikation | `=A1*B1` | Produkt |
| `/` | Division | `=A1/B1` | Kvotient |
| `^` | Potens | `=A1^2` | A1 i anden |

---

### SUM
**Syntaks:** `=SUM(område)`

Lægger alle tal i et celleområde sammen.

| Parameter | Beskrivelse |
|-----------|-------------|
| `område` | f.eks. `A1:A10` |

```
=SUM(A1:A10)
```

---

### GENNEMSNIT
**Syntaks:** `=GENNEMSNIT(område)`

Beregner gennemsnittet af alle tal i området.

```
=GENNEMSNIT(A1:A10)
```

---

### MIN
**Syntaks:** `=MIN(område)`

Returnerer den mindste værdi i området.

```
=MIN(A1:A10)
```

---

### MAKS
**Syntaks:** `=MAKS(område)`

Returnerer den største værdi i området.

```
=MAKS(A1:A10)
```

---

### TÆL
**Syntaks:** `=TÆL(område)`

Tæller alle celler med **talværdier** i området.

```
=TÆL(A1:A10)
```

---

### TÆLV
**Syntaks:** `=TÆLV(område)`

Tæller alle **ikke-tomme** celler (tal og tekst).

```
=TÆLV(A1:A10)
```

---

### MEDIAN
**Syntaks:** `=MEDIAN(område)`

Returnerer medianen af den sorterede værdiliste (midterste værdi).

```
=MEDIAN(A1:A10)
```

---

### SUMPRODUKT
**Syntaks:** `=SUMPRODUKT(område1; område2)`

Multiplicerer elementerne i to områder med hinanden og lægger resultaterne sammen.

| Parameter | Beskrivelse |
|-----------|-------------|
| `område1` | Første område |
| `område2` | Andet område (samme størrelse) |

```
=SUMPRODUKT(A1:A10; B1:B10)
```

---

## Fane 2 – Avancerede funktioner

### HVIS
**Syntaks:** `=HVIS(betingelse; så; ellers)`

Returnerer én af to værdier afhængigt af om betingelsen er sand eller falsk.

| Parameter | Beskrivelse |
|-----------|-------------|
| `betingelse` | f.eks. `A1>0` |
| `så` | Værdi hvis sand |
| `ellers` | Værdi hvis falsk |

```
=HVIS(A1>0; "OK"; "Fejl")
```

---

### OG
**Syntaks:** `=OG(betingelse1; betingelse2)`

Returnerer SAND hvis **alle** betingelser er opfyldt.

```
=OG(A1>0; B1>0)
```

---

### ELLER
**Syntaks:** `=ELLER(betingelse1; betingelse2)`

Returnerer SAND hvis **mindst én** betingelse er opfyldt.

```
=ELLER(A1>0; B1>0)
```

---

### IKKE
**Syntaks:** `=IKKE(betingelse)`

Vender en logisk værdi om: SAND → FALSK, FALSK → SAND.

```
=IKKE(A1>0)
```

---

### SUM.HVIS
**Syntaks:** `=SUM.HVIS(område; kriterium; sum_område)`

Lægger værdier sammen der opfylder et kriterium.

| Parameter | Beskrivelse |
|-----------|-------------|
| `område` | Område der kontrolleres |
| `kriterium` | f.eks. `">10"` eller `"Ja"` |
| `sum_område` | Område der lægges sammen |

```
=SUM.HVIS(A1:A10; ">10"; B1:B10)
```

---

### TÆL.HVIS
**Syntaks:** `=TÆL.HVIS(område; kriterium)`

Tæller celler der opfylder et kriterium.

```
=TÆL.HVIS(A1:A10; "Ja")
```

---

### GENNEMSNIT.HVIS
**Syntaks:** `=GENNEMSNIT.HVIS(område; kriterium; gennemsnit_område)`

Beregner gennemsnittet af værdier der opfylder et kriterium.

```
=GENNEMSNIT.HVIS(A1:A10; ">0"; B1:B10)
```

---

### SUM.HVISER
**Syntaks:** `=SUM.HVISER(sum_område; kriterier_område; kriterium)`

Lægger værdier sammen der opfylder **flere** kriterier.

| Parameter | Beskrivelse |
|-----------|-------------|
| `sum_område` | Område der lægges sammen |
| `kriterier_område` | Område der kontrolleres |
| `kriterium` | Betingelse f.eks. `">10"` |

```
=SUM.HVISER(A1:A10; B1:B10; ">10")
```

---

### STDAFV
**Syntaks:** `=STDAFV(område)`

Beregner standardafvigelsen (spredningen af værdier).

```
=STDAFV(A1:A10)
```

---

### VARIANS
**Syntaks:** `=VARIANS(område)`

Beregner variansen (kvadratisk spredning).

```
=VARIANS(A1:A10)
```

---

### TÆL.TOMME
**Syntaks:** `=TÆL.TOMME(område)`

Tæller alle **tomme** celler i området.

```
=TÆL.TOMME(A1:A10)
```

---

### STOR
**Syntaks:** `=STOR(område; k)`

Returnerer den k-te største værdi i området.

| Parameter | Beskrivelse |
|-----------|-------------|
| `område` | Talområde |
| `k` | Rang (1 = størst, 2 = næststørst, …) |

```
=STOR(A1:A10; 2)
```

---

## Fane 3 – Dato og tekst

### IDAG
**Syntaks:** `=IDAG()`

Returnerer den aktuelle dato. Opdateres hver gang filen åbnes.

```
=IDAG()
```

---

### NU
**Syntaks:** `=NU()`

Returnerer den aktuelle dato **med klokkeslæt**.

```
=NU()
```

---

### ÅR
**Syntaks:** `=ÅR(dato)`

Udtrækker året fra en dato.

```
=ÅR(A1)
```

---

### MÅNED
**Syntaks:** `=MÅNED(dato)`

Udtrækker måneden (1–12) fra en dato.

```
=MÅNED(A1)
```

---

### DAG
**Syntaks:** `=DAG(dato)`

Udtrækker dagen (1–31) fra en dato.

```
=DAG(A1)
```

---

### DATO
**Syntaks:** `=DATO(år; måned; dag)`

Opretter en dato fra individuelle værdier.

```
=DATO(2025; 1; 1)
```

---

### DATEDIF
**Syntaks:** `=DATEDIF(startdato; slutdato; enhed)`

Beregner forskellen mellem to datoer.

| Enhed | Betydning |
|-------|-----------|
| `"D"` | Dage |
| `"M"` | Måneder |
| `"Y"` | År |

```
=DATEDIF(A1; B1; "D")
```

> **Bemærk:** DATEDIF er en udokumenteret funktion – den virker i LibreOffice og Excel, men vises ikke i autofuldførelse.

---

### UGEDAG
**Syntaks:** `=UGEDAG(dato; type)`

Returnerer ugedagen som et tal.

| Type | Betydning |
|------|-----------|
| `2` | 1=Man, 2=Tir, … 7=Søn (anbefalet) |
| `1` | 1=Søn, 2=Man, … 7=Lør |

```
=UGEDAG(A1; 2)
```

---

### SAMMENKÆD
**Syntaks:** `=SAMMENKÆD(tekst1; tekst2; …)`

Sammensætter flere tekster til én.

```
=SAMMENKÆD(A1; " "; B1)
```

---

### LÆNGDE
**Syntaks:** `=LÆNGDE(tekst)`

Returnerer antallet af tegn i en tekst.

```
=LÆNGDE(A1)
```

---

### VENSTRE
**Syntaks:** `=VENSTRE(tekst; antal)`

Returnerer de første n tegn i en tekst.

```
=VENSTRE(A1; 5)
```

---

### HØJRE
**Syntaks:** `=HØJRE(tekst; antal)`

Returnerer de sidste n tegn i en tekst.

```
=HØJRE(A1; 5)
```

---

### MIDT
**Syntaks:** `=MIDT(tekst; startposition; antal)`

Returnerer et uddrag fra en tekst.

| Parameter | Beskrivelse |
|-----------|-------------|
| `tekst` | Kildetekst |
| `startposition` | Fra hvilket tegn (1 = første) |
| `antal` | Hvor mange tegn |

```
=MIDT(A1; 1; 5)
```

---

### STORE.BOGSTAVER
**Syntaks:** `=STORE.BOGSTAVER(tekst)`

Konverterer alle bogstaver til store bogstaver.

```
=STORE.BOGSTAVER(A1)
```

---

### SMÅ.BOGSTAVER
**Syntaks:** `=SMÅ.BOGSTAVER(tekst)`

Konverterer alle bogstaver til små bogstaver.

```
=SMÅ.BOGSTAVER(A1)
```

---

### FJERN.OVERFLØDIGE.BLANKE
**Syntaks:** `=FJERN.OVERFLØDIGE.BLANKE(tekst)`

Fjerner overflødige mellemrum (foranstillede, efterstillede og dobbelte).

```
=FJERN.OVERFLØDIGE.BLANKE(A1)
```

---

## Fane 4 – Opslag og afrunding

### LOPSLAG
**Syntaks:** `=LOPSLAG(opslagsværdi; tabel; kolonneindeks; match)`

Søger efter en værdi i **første kolonne** i en tabel og returnerer værdien fra en anden kolonne.

| Parameter | Beskrivelse |
|-----------|-------------|
| `opslagsværdi` | Søgt værdi, f.eks. `A1` |
| `tabel` | Søgeområde, f.eks. `B1:D10` |
| `kolonneindeks` | Kolonnenummer der returneres (1 = første kolonne) |
| `match` | `0` = præcis, `1` = omtrentlig |

```
=LOPSLAG(A1; B1:D10; 2; 0)
```

---

### VOPSLAG
**Syntaks:** `=VOPSLAG(opslagsværdi; tabel; rækkeindeks; match)`

Som LOPSLAG, men søger i **første række** (vandret).

```
=VOPSLAG(A1; B1:D10; 2; 0)
```

---

### INDEKS
**Syntaks:** `=INDEKS(område; række; kolonne)`

Returnerer værdien på en bestemt position i området.

| Parameter | Beskrivelse |
|-----------|-------------|
| `område` | Søgeområde |
| `række` | Rækkenummer |
| `kolonne` | Kolonnenummer (standard: 1) |

```
=INDEKS(B1:B10; 3; 1)
```

---

### SAMMENLIGN
**Syntaks:** `=SAMMENLIGN(opslagsværdi; søgeområde; matchtype)`

Returnerer **positionen** af en værdi i et område.

| Matchtype | Betydning |
|-----------|-----------|
| `0` | Præcis match |
| `1` | Mindste der er større end eller lig med |
| `-1` | Største der er mindre end eller lig med |

```
=SAMMENLIGN(A1; A1:A10; 0)
```

---

### INDEKS + SAMMENLIGN
**Syntaks:** `=INDEKS(resultat_område; SAMMENLIGN(opslagsværdi; søge_område; 0))`

Et mere fleksibelt alternativ til LOPSLAG – kan søge i **alle retninger**.

| Parameter | Beskrivelse |
|-----------|-------------|
| `resultat_område` | Kolonne med returværdier |
| `opslagsværdi` | Søgt værdi |
| `søge_område` | Kolonne der søges i |

```
=INDEKS(B1:B10; SAMMENLIGN(A1; A1:A10; 0))
```

> **Fordel frem for LOPSLAG:** Søgekolonnen behøver ikke være den første kolonne. Stabil selv ved indsættelse/sletning af kolonner.

---

### AFRUND
**Syntaks:** `=AFRUND(tal; decimaler)`

Afrunder til det angivne antal decimaler.

| Decimaler | Eksempel |
|-----------|---------|
| `2` | 3,14159 → 3,14 |
| `0` | 3,7 → 4 |
| `-1` | 34 → 30 |

```
=AFRUND(A1; 2)
```

---

### AFRUND.OP
**Syntaks:** `=AFRUND.OP(tal; decimaler)`

Afrunder altid **op** (væk fra nul).

```
=AFRUND.OP(A1; 2)
```

---

### AFRUND.NED
**Syntaks:** `=AFRUND.NED(tal; decimaler)`

Afrunder altid **ned** (mod nul).

```
=AFRUND.NED(A1; 2)
```

---

### HELTAL
**Syntaks:** `=HELTAL(tal)`

Afrunder ned til nærmeste heltal (også for negative tal).

```
=HELTAL(A1)
```

---

### AFKORT
**Syntaks:** `=AFKORT(tal; decimaler)`

Afskærer decimaler **uden** afrunding.

```
=AFKORT(A1; 2)
```

---

### ABS
**Syntaks:** `=ABS(tal)`

Returnerer den **absolutte værdi** (altid positiv).

```
=ABS(A1)
```

---

### REST
**Syntaks:** `=REST(tal; divisor)`

Returnerer **resten** af en division.

```
=REST(A1; 3)
```
> Eksempel: `=REST(10; 3)` → `1`

---

### KVROD
**Syntaks:** `=KVROD(tal)`

Beregner kvadratroden.

```
=KVROD(A1)
```

---

### SLUMP
**Syntaks:** `=SLUMP()`

Returnerer et tilfældigt decimaltal mellem 0 og 1. Opdateres ved hver genberegning.

```
=SLUMP()
```

> For et tilfældigt tal mellem 1 og 100: `=HELTAL(SLUMP()*100)+1`

---

## Absolutte referencer

I programmet kan referencetilstanden vælges via en rullemenu:

| Tilstand | Eksempel | Betydning |
|----------|---------|-----------|
| Relativ | `A1` | Forskydes ved kopiering |
| Fast kolonne | `$A1` | Kolonnen forbliver, rækken forskydes |
| Fast række | `A$1` | Rækken forbliver, kolonnen forskydes |
| Absolut | `$A$1` | Forbliver altid den samme ved kopiering |

---

## Tastaturgenveje

| Genvej | Funktion |
|--------|---------|
| `Ctrl+S` | Gem formel i favoritter |
| `Ctrl+C` | Kopiér formel |
| `Ctrl+Z` | Fortryd |
| `Ctrl+Y` | Annullér fortryd |
| `Ctrl+F12` | Minimer / gendan vindue |
| `Del` | Slet favorit (på listen) |
