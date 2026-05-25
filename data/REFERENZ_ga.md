# Tagairt Feidhmeanna – Cúntóir Foirmlí LibreOffice Calc

Gach feidhm atá ar fáil sa chlár, le comhréir, paraiméadair agus samplaí.

---

## Cluaisín 1 – Feidhmeanna Bunúsacha

### Oibreoirí Uimhríochta

| Oibreoir | Brí | Sampla | Toradh |
|----------|-----|--------|--------|
| `+` | Suimiú | `=A1+B1` | Suim dhá chill |
| `-` | Dealú | `=A1-B1` | Difríocht |
| `*` | Iolrú | `=A1*B1` | Táirge |
| `/` | Roinnt | `=A1/B1` | Caiteach |
| `^` | Cumhacht | `=A1^2` | A1 faoi chearnóg |

---

### SUM
**Comhréir:** `=SUM(raon)`

Suimiíonn sé gach uimhir i raon cill.

| Paraiméadar | Cur síos |
|-------------|----------|
| `raon` | m.sh. `A1:A10` |

```
=SUM(A1:A10)
```

---

### AVERAGE
**Comhréir:** `=AVERAGE(raon)`

Ríomhann sé meán na n-uimhreacha go léir sa raon.

```
=AVERAGE(A1:A10)
```

---

### MIN
**Comhréir:** `=MIN(raon)`

Cuireann sé ar ais an luach is lú sa raon.

```
=MIN(A1:A10)
```

---

### MAX
**Comhréir:** `=MAX(raon)`

Cuireann sé ar ais an luach is mó sa raon.

```
=MAX(A1:A10)
```

---

### COUNT
**Comhréir:** `=COUNT(raon)`

Comhairíonn sé gach cill le **luachanna uimhriúla** sa raon.

```
=COUNT(A1:A10)
```

---

### COUNTA
**Comhréir:** `=COUNTA(raon)`

Comhairíonn sé gach cill **nach bhfuil folamh** (uimhreacha agus téacs).

```
=COUNTA(A1:A10)
```

---

### MEDIAN
**Comhréir:** `=MEDIAN(raon)`

Cuireann sé ar ais luach lár na liosta luachanna sórtáilte.

```
=MEDIAN(A1:A10)
```

---

### SUMPRODUCT
**Comhréir:** `=SUMPRODUCT(raon1; raon2)`

Iolraíonn sé eilimintí dhá raon le chéile agus suimiíonn na torthaí.

| Paraiméadar | Cur síos |
|-------------|----------|
| `raon1` | An chéad raon |
| `raon2` | An dara raon (an méid céanna) |

```
=SUMPRODUCT(A1:A10; B1:B10)
```

---

## Cluaisín 2 – Feidhmeanna Casta

### IF
**Comhréir:** `=IF(coinníoll; ansin; murach_sin)`

Cuireann sé ar ais ceann de dhá luach ag brath ar an gcoinníoll a bheith fíor nó bréagach.

| Paraiméadar | Cur síos |
|-------------|----------|
| `coinníoll` | m.sh. `A1>0` |
| `ansin` | Luach má tá sé fíor |
| `murach_sin` | Luach má tá sé bréagach |

```
=IF(A1>0; "OK"; "Earráid")
```

---

### AND
**Comhréir:** `=AND(coinníoll1; coinníoll2)`

Cuireann sé ar ais FÍOR má tá **gach** coinníoll comhlíonta.

```
=AND(A1>0; B1>0)
```

---

### OR
**Comhréir:** `=OR(coinníoll1; coinníoll2)`

Cuireann sé ar ais FÍOR má tá **coinníoll amháin ar a laghad** comhlíonta.

```
=OR(A1>0; B1>0)
```

---

### NOT
**Comhréir:** `=NOT(coinníoll)`

Aisiompaíonn luach loighciúil: FÍOR → BRÉAGACH, BRÉAGACH → FÍOR.

```
=NOT(A1>0)
```

---

### SUMIF
**Comhréir:** `=SUMIF(raon; critéar; raon_suime)`

Suimiíonn luachanna a chomhlíonann critéar.

| Paraiméadar | Cur síos |
|-------------|----------|
| `raon` | An raon a ndéantar measúnú air |
| `critéar` | m.sh. `">10"` nó `"Sea"` |
| `raon_suime` | An raon le suimiú |

```
=SUMIF(A1:A10; ">10"; B1:B10)
```

---

### COUNTIF
**Comhréir:** `=COUNTIF(raon; critéar)`

Comhairíonn cealla a chomhlíonann critéar.

```
=COUNTIF(A1:A10; "Sea")
```

---

### AVERAGEIF
**Comhréir:** `=AVERAGEIF(raon; critéar; raon_meáin)`

Ríomhann meán na luachanna a chomhlíonann critéar.

```
=AVERAGEIF(A1:A10; ">0"; B1:B10)
```

---

### SUMIFS
**Comhréir:** `=SUMIFS(raon_suime; raon_critéar; critéar)`

Suimiíonn luachanna a chomhlíonann **critéir iolracha**.

| Paraiméadar | Cur síos |
|-------------|----------|
| `raon_suime` | An raon le suimiú |
| `raon_critéar` | An raon a ndéantar measúnú air |
| `critéar` | Coinníoll, m.sh. `">10"` |

```
=SUMIFS(A1:A10; B1:B10; ">10")
```

---

### STDEV
**Comhréir:** `=STDEV(raon)`

Ríomhann sé an diall caighdeánach (scaipeadh na luachanna).

```
=STDEV(A1:A10)
```

---

### VAR
**Comhréir:** `=VAR(raon)`

Ríomhann sé an t-athraitheacht (scaipeadh cearnógach).

```
=VAR(A1:A10)
```

---

### COUNTBLANK
**Comhréir:** `=COUNTBLANK(raon)`

Comhairíonn sé gach cill **fholamh** sa raon.

```
=COUNTBLANK(A1:A10)
```

---

### LARGE
**Comhréir:** `=LARGE(raon; k)`

Cuireann sé ar ais an k-ú luach is mó sa raon.

| Paraiméadar | Cur síos |
|-------------|----------|
| `raon` | Raon uimhreacha |
| `k` | Rang (1 = is mó, 2 = an dara ceann is mó, …) |

```
=LARGE(A1:A10; 2)
```

---

## Cluaisín 3 – Dáta agus Téacs

### TODAY
**Comhréir:** `=TODAY()`

Cuireann sé ar ais an dáta reatha. Nuashonraítear é gach uair a osclaítear an comhad.

```
=TODAY()
```

---

### NOW
**Comhréir:** `=NOW()`

Cuireann sé ar ais an dáta reatha **leis an am**.

```
=NOW()
```

---

### YEAR
**Comhréir:** `=YEAR(dáta)`

Baineann an bhliain as dáta.

```
=YEAR(A1)
```

---

### MONTH
**Comhréir:** `=MONTH(dáta)`

Baineann an mhí (1–12) as dáta.

```
=MONTH(A1)
```

---

### DAY
**Comhréir:** `=DAY(dáta)`

Baineann an lá (1–31) as dáta.

```
=DAY(A1)
```

---

### DATE
**Comhréir:** `=DATE(bliain; mí; lá)`

Cruthaíonn dáta ó luachanna aonair.

```
=DATE(2025; 1; 1)
```

---

### DATEDIF
**Comhréir:** `=DATEDIF(dáta_tosaigh; dáta_deiridh; aonad)`

Ríomhann sé an difríocht idir dhá dháta.

| Aonad | Brí |
|-------|-----|
| `"D"` | Laethanta |
| `"M"` | Míonna |
| `"Y"` | Blianta |

```
=DATEDIF(A1; B1; "D")
```

> **Nóta:** Is feidhm gan doiciméadú í DATEDIF – oibríonn sí in LibreOffice agus Excel, ach ní léirítear í san uathlíonadh.

---

### WEEKDAY
**Comhréir:** `=WEEKDAY(dáta; cineál)`

Cuireann sé ar ais lá na seachtaine mar uimhir.

| Cineál | Brí |
|--------|-----|
| `2` | 1=Luan, 2=Máirt, … 7=Domh (molta) |
| `1` | 1=Domh, 2=Luan, … 7=Satharn |

```
=WEEKDAY(A1; 2)
```

---

### CONCATENATE
**Comhréir:** `=CONCATENATE(téacs1; téacs2; …)`

Ceanglaíonn sé téacsanna iolracha in aon téacs amháin.

```
=CONCATENATE(A1; " "; B1)
```

---

### LEN
**Comhréir:** `=LEN(téacs)`

Cuireann sé ar ais líon na gcarachtar i dtéacs.

```
=LEN(A1)
```

---

### LEFT
**Comhréir:** `=LEFT(téacs; líon)`

Cuireann sé ar ais na n carachtar tosaigh i dtéacs.

```
=LEFT(A1; 5)
```

---

### RIGHT
**Comhréir:** `=RIGHT(téacs; líon)`

Cuireann sé ar ais na n carachtar deiridh i dtéacs.

```
=RIGHT(A1; 5)
```

---

### MID
**Comhréir:** `=MID(téacs; suíomh_tosaigh; líon)`

Cuireann sé ar ais blúire as téacs.

| Paraiméadar | Cur síos |
|-------------|----------|
| `téacs` | Téacs foinse |
| `suíomh_tosaigh` | Ón gcarachtar cé (1 = an chéad cheann) |
| `líon` | Cé mhéad carachtar |

```
=MID(A1; 1; 5)
```

---

### UPPER
**Comhréir:** `=UPPER(téacs)`

Tiontaíonn gach litir go ceannlitreacha.

```
=UPPER(A1)
```

---

### LOWER
**Comhréir:** `=LOWER(téacs)`

Tiontaíonn gach litir go litreacha beaga.

```
=LOWER(A1)
```

---

### TRIM
**Comhréir:** `=TRIM(téacs)`

Baineann spásanna iomarcacha (tosaigh, deiridh agus dúbailt).

```
=TRIM(A1)
```

---

## Cluaisín 4 – Cuardach agus Slánú

### VLOOKUP
**Comhréir:** `=VLOOKUP(luach_cuardaigh; maitrís; innéacs_colúin; meaitseáil)`

Cuardaíonn luach i **gcéad cholún** tábla agus cuireann ar ais luach ó cholún eile.

| Paraiméadar | Cur síos |
|-------------|----------|
| `luach_cuardaigh` | Luach cuardaigh, m.sh. `A1` |
| `maitrís` | Raon cuardaigh, m.sh. `B1:D10` |
| `innéacs_colúin` | Uimhir an cholúin le cur ar ais (1 = céad cholún) |
| `meaitseáil` | `0` = beacht, `1` = gar-mheaitseáil |

```
=VLOOKUP(A1; B1:D10; 2; 0)
```

---

### HLOOKUP
**Comhréir:** `=HLOOKUP(luach_cuardaigh; maitrís; innéacs_ró; meaitseáil)`

Cosúil le VLOOKUP, ach cuardaíonn sé sa **chéad ró** (cothrománach).

```
=HLOOKUP(A1; B1:D10; 2; 0)
```

---

### INDEX
**Comhréir:** `=INDEX(raon; ró; colún)`

Cuireann sé ar ais an luach ag suíomh áirithe sa raon.

| Paraiméadar | Cur síos |
|-------------|----------|
| `raon` | Raon cuardaigh |
| `ró` | Uimhir an ró |
| `colún` | Uimhir an cholúin (réamhshocrú: 1) |

```
=INDEX(B1:B10; 3; 1)
```

---

### MATCH
**Comhréir:** `=MATCH(luach_cuardaigh; raon_cuardaigh; cineál_meaitseála)`

Cuireann sé ar ais **suíomh** luacha i raon.

| Cineál meaitseála | Brí |
|-------------------|-----|
| `0` | Meaitseáil bheacht |
| `1` | An ceann is lú atá níos mó ná nó cothrom le |
| `-1` | An ceann is mó atá níos lú ná nó cothrom le |

```
=MATCH(A1; A1:A10; 0)
```

---

### INDEX + MATCH
**Comhréir:** `=INDEX(raon_torthaí; MATCH(luach_cuardaigh; raon_cuardaigh; 0))`

Rogha níos solúbtha ná VLOOKUP – is féidir cuardach a dhéanamh in **aon treo**.

| Paraiméadar | Cur síos |
|-------------|----------|
| `raon_torthaí` | Colún leis na luachanna le cur ar ais |
| `luach_cuardaigh` | Luach cuardaigh |
| `raon_cuardaigh` | Colún ina ndéantar cuardach |

```
=INDEX(B1:B10; MATCH(A1; A1:A10; 0))
```

> **Buntáiste thar VLOOKUP:** Ní gá don cholún cuardaigh a bheith sa chéad cholún. Cobhsaí freisin agus colúin á gcur isteach nó á scriosadh.

---

### ROUND
**Comhréir:** `=ROUND(uimhir; deachúlacha)`

Slánaiíonn sé go dtí an líon deachúlacha sonraithe.

| Deachúlacha | Sampla |
|-------------|--------|
| `2` | 3.14159 → 3.14 |
| `0` | 3.7 → 4 |
| `-1` | 34 → 30 |

```
=ROUND(A1; 2)
```

---

### ROUNDUP
**Comhréir:** `=ROUNDUP(uimhir; deachúlacha)`

Slánaiíonn sé i gcónaí **suas** (ar shiúl ó nialas).

```
=ROUNDUP(A1; 2)
```

---

### ROUNDDOWN
**Comhréir:** `=ROUNDDOWN(uimhir; deachúlacha)`

Slánaiíonn sé i gcónaí **síos** (i dtreo nialais).

```
=ROUNDDOWN(A1; 2)
```

---

### INT
**Comhréir:** `=INT(uimhir)`

Slánaiíonn sé go dtí an slánuimhir is gaire **síos** (fiú d'uimhreacha diúltacha).

```
=INT(A1)
```

---

### TRUNC
**Comhréir:** `=TRUNC(uimhir; deachúlacha)`

Gearrann sé deachúlacha **gan slánú**.

```
=TRUNC(A1; 2)
```

---

### ABS
**Comhréir:** `=ABS(uimhir)`

Cuireann sé ar ais an **luach absalóideach** (dearfach i gcónaí).

```
=ABS(A1)
```

---

### MOD
**Comhréir:** `=MOD(uimhir; roinneoir)`

Cuireann sé ar ais **iarsma** roinnte.

```
=MOD(A1; 3)
```
> Sampla: `=MOD(10; 3)` → `1`

---

### SQRT
**Comhréir:** `=SQRT(uimhir)`

Ríomhann sé fréamh chearnach.

```
=SQRT(A1)
```

---

### RAND
**Comhréir:** `=RAND()`

Cuireann sé ar ais uimhir dheachúlach randamach idir 0 agus 1. Nuashonraítear é le gach ath-ríomh.

```
=RAND()
```

> Le haghaidh uimhir randamach idir 1 agus 100: `=INT(RAND()*100)+1`

---

## Tagairtí Absalóideacha

Sa chlár, is féidir an mód tagartha a roghnú ó roghchlár anuas:

| Mód | Sampla | Brí |
|-----|--------|-----|
| Coibhneasta | `A1` | Bogann le linn cóipeála |
| Colún seasta | `$A1` | Fanann an colún, bogann an ró |
| Ró seasta | `A$1` | Fanann an ró, bogann an colún |
| Absalóideach | `$A$1` | Fanann mar an gcéanna i gcónaí le linn cóipeála |

---

## Aicearraí Méarchlár

| Aicearra | Feidhm |
|----------|--------|
| `Ctrl+S` | Sábháil foirmle sna ceanáin |
| `Ctrl+C` | Cóipeáil foirmle |
| `Ctrl+Z` | Cealaigh |
| `Ctrl+Y` | Athdhéan |
| `Ctrl+F12` | Íoslaghdaigh / athchóirigh an fhuinneog |
| `Del` | Scrios ceanán (sa liosta) |
