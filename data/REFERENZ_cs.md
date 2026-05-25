# Přehled funkcí – LibreOffice Calc Formula Helper

Všechny funkce dostupné v programu, včetně syntaxe, parametrů a příkladů.

---

## Záložka 1 – Základní funkce

### Aritmetické operátory

| Operátor | Význam | Příklad | Výsledek |
|----------|--------|---------|---------|
| `+` | Sčítání | `=A1+B1` | Součet dvou buněk |
| `-` | Odčítání | `=A1-B1` | Rozdíl |
| `*` | Násobení | `=A1*B1` | Součin |
| `/` | Dělení | `=A1/B1` | Podíl |
| `^` | Umocňování | `=A1^2` | A1 na druhou |

---

### SUMA
**Syntaxe:** `=SUMA(oblast)`

Sečte všechna čísla v oblasti buněk.

| Parametr | Popis |
|----------|-------|
| `oblast` | např. `A1:A10` |

```
=SUMA(A1:A10)
```

---

### PRŮMĚR
**Syntaxe:** `=PRŮMĚR(oblast)`

Vypočítá průměr všech čísel v oblasti.

```
=PRŮMĚR(A1:A10)
```

---

### MIN
**Syntaxe:** `=MIN(oblast)`

Vrátí nejmenší hodnotu v oblasti.

```
=MIN(A1:A10)
```

---

### MAX
**Syntaxe:** `=MAX(oblast)`

Vrátí největší hodnotu v oblasti.

```
=MAX(A1:A10)
```

---

### POČET
**Syntaxe:** `=POČET(oblast)`

Spočítá všechny buňky s **číselnými hodnotami** v oblasti.

```
=POČET(A1:A10)
```

---

### POČET2
**Syntaxe:** `=POČET2(oblast)`

Spočítá všechny **neprázdné** buňky (čísla i text).

```
=POČET2(A1:A10)
```

---

### MEDIAN
**Syntaxe:** `=MEDIAN(oblast)`

Vrátí střední hodnotu seřazeného seznamu hodnot.

```
=MEDIAN(A1:A10)
```

---

### SOUČIN.SKALÁRNÍ
**Syntaxe:** `=SOUČIN.SKALÁRNÍ(oblast1; oblast2)`

Vynásobí prvky dvou oblastí navzájem a sečte výsledky.

| Parametr | Popis |
|----------|-------|
| `oblast1` | První oblast |
| `oblast2` | Druhá oblast (stejná velikost) |

```
=SOUČIN.SKALÁRNÍ(A1:A10; B1:B10)
```

---

## Záložka 2 – Pokročilé funkce

### KDYŽ
**Syntaxe:** `=KDYŽ(podmínka; pak; jinak)`

Vrátí jednu ze dvou hodnot podle toho, zda je podmínka pravdivá nebo nepravdivá.

| Parametr | Popis |
|----------|-------|
| `podmínka` | např. `A1>0` |
| `pak` | Hodnota pokud je pravda |
| `jinak` | Hodnota pokud je nepravda |

```
=KDYŽ(A1>0; "OK"; "Chyba")
```

---

### A
**Syntaxe:** `=A(podmínka1; podmínka2)`

Vrátí PRAVDA pokud jsou **všechny** podmínky splněny.

```
=A(A1>0; B1>0)
```

---

### NEBO
**Syntaxe:** `=NEBO(podmínka1; podmínka2)`

Vrátí PRAVDA pokud je splněna **alespoň jedna** podmínka.

```
=NEBO(A1>0; B1>0)
```

---

### NE
**Syntaxe:** `=NE(podmínka)`

Obrátí logickou hodnotu: PRAVDA → NEPRAVDA, NEPRAVDA → PRAVDA.

```
=NE(A1>0)
```

---

### SUMIF
**Syntaxe:** `=SUMIF(oblast; kritérium; součet_oblast)`

Sečte hodnoty splňující zadané kritérium.

| Parametr | Popis |
|----------|-------|
| `oblast` | Oblast, která se kontroluje |
| `kritérium` | např. `">10"` nebo `"Ano"` |
| `součet_oblast` | Oblast, která se sčítá |

```
=SUMIF(A1:A10; ">10"; B1:B10)
```

---

### COUNTIF
**Syntaxe:** `=COUNTIF(oblast; kritérium)`

Spočítá buňky splňující zadané kritérium.

```
=COUNTIF(A1:A10; "Ano")
```

---

### AVERAGEIF
**Syntaxe:** `=AVERAGEIF(oblast; kritérium; průměr_oblast)`

Vypočítá průměr hodnot splňujících zadané kritérium.

```
=AVERAGEIF(A1:A10; ">0"; B1:B10)
```

---

### SUMIFS
**Syntaxe:** `=SUMIFS(součet_oblast; kritéria_oblast; kritérium)`

Sečte hodnoty splňující **více** kritérií.

| Parametr | Popis |
|----------|-------|
| `součet_oblast` | Oblast, která se sčítá |
| `kritéria_oblast` | Oblast, která se kontroluje |
| `kritérium` | Podmínka např. `">10"` |

```
=SUMIFS(A1:A10; B1:B10; ">10")
```

---

### SMODCH
**Syntaxe:** `=SMODCH(oblast)`

Vypočítá směrodatnou odchylku (rozptyl hodnot).

```
=SMODCH(A1:A10)
```

---

### VAR
**Syntaxe:** `=VAR(oblast)`

Vypočítá rozptyl (kvadratický rozptyl).

```
=VAR(A1:A10)
```

---

### COUNTBLANK
**Syntaxe:** `=COUNTBLANK(oblast)`

Spočítá všechny **prázdné** buňky v oblasti.

```
=COUNTBLANK(A1:A10)
```

---

### LARGE
**Syntaxe:** `=LARGE(oblast; k)`

Vrátí k-tou největší hodnotu v oblasti.

| Parametr | Popis |
|----------|-------|
| `oblast` | Číselná oblast |
| `k` | Pořadí (1 = největší, 2 = druhý největší, …) |

```
=LARGE(A1:A10; 2)
```

---

## Záložka 3 – Datum a text

### DNES
**Syntaxe:** `=DNES()`

Vrátí aktuální datum. Aktualizuje se při každém otevření souboru.

```
=DNES()
```

---

### NYNÍ
**Syntaxe:** `=NYNÍ()`

Vrátí aktuální datum **s časem**.

```
=NYNÍ()
```

---

### ROK
**Syntaxe:** `=ROK(datum)`

Extrahuje rok z data.

```
=ROK(A1)
```

---

### MĚSÍC
**Syntaxe:** `=MĚSÍC(datum)`

Extrahuje měsíc (1–12) z data.

```
=MĚSÍC(A1)
```

---

### DEN
**Syntaxe:** `=DEN(datum)`

Extrahuje den (1–31) z data.

```
=DEN(A1)
```

---

### DATUM
**Syntaxe:** `=DATUM(rok; měsíc; den)`

Vytvoří datum z jednotlivých hodnot.

```
=DATUM(2025; 1; 1)
```

---

### DATEDIF
**Syntaxe:** `=DATEDIF(počáteční_datum; koncové_datum; jednotka)`

Vypočítá rozdíl mezi dvěma daty.

| Jednotka | Význam |
|----------|--------|
| `"D"` | Dny |
| `"M"` | Měsíce |
| `"Y"` | Roky |

```
=DATEDIF(A1; B1; "D")
```

> **Poznámka:** DATEDIF je nezdokumentovaná funkce – funguje v LibreOffice i Excelu, ale nezobrazuje se v automatickém doplňování.

---

### DENTÝDNE
**Syntaxe:** `=DENTÝDNE(datum; typ)`

Vrátí den v týdnu jako číslo.

| Typ | Význam |
|-----|--------|
| `2` | 1=Po, 2=Út, … 7=Ne (doporučeno) |
| `1` | 1=Ne, 2=Po, … 7=So |

```
=DENTÝDNE(A1; 2)
```

---

### CONCATENATE
**Syntaxe:** `=CONCATENATE(text1; text2; …)`

Spojí více textů do jednoho.

```
=CONCATENATE(A1; " "; B1)
```

---

### DÉLKA
**Syntaxe:** `=DÉLKA(text)`

Vrátí počet znaků v textu.

```
=DÉLKA(A1)
```

---

### ZLEVA
**Syntaxe:** `=ZLEVA(text; počet)`

Vrátí prvních n znaků textu.

```
=ZLEVA(A1; 5)
```

---

### ZPRAVA
**Syntaxe:** `=ZPRAVA(text; počet)`

Vrátí posledních n znaků textu.

```
=ZPRAVA(A1; 5)
```

---

### ČÁST
**Syntaxe:** `=ČÁST(text; počáteční_pozice; počet)`

Vrátí část textu.

| Parametr | Popis |
|----------|-------|
| `text` | Zdrojový text |
| `počáteční_pozice` | Od kterého znaku (1 = první) |
| `počet` | Kolik znaků |

```
=ČÁST(A1; 1; 5)
```

---

### VELKÁ
**Syntaxe:** `=VELKÁ(text)`

Převede všechna písmena na velká.

```
=VELKÁ(A1)
```

---

### MALÁ
**Syntaxe:** `=MALÁ(text)`

Převede všechna písmena na malá.

```
=MALÁ(A1)
```

---

### PROČISTIT
**Syntaxe:** `=PROČISTIT(text)`

Odstraní nadbytečné mezery (úvodní, koncové a dvojité).

```
=PROČISTIT(A1)
```

---

## Záložka 4 – Vyhledávání a zaokrouhlování

### SVYHLEDAT
**Syntaxe:** `=SVYHLEDAT(hledaná_hodnota; tabulka; index_sloupce; shoda)`

Hledá hodnotu v **prvním sloupci** tabulky a vrátí hodnotu z jiného sloupce.

| Parametr | Popis |
|----------|-------|
| `hledaná_hodnota` | Hledaná hodnota, např. `A1` |
| `tabulka` | Oblast hledání, např. `B1:D10` |
| `index_sloupce` | Číslo sloupce pro vrácení (1 = první sloupec) |
| `shoda` | `0` = přesná, `1` = přibližná |

```
=SVYHLEDAT(A1; B1:D10; 2; 0)
```

---

### VVYHLEDAT
**Syntaxe:** `=VVYHLEDAT(hledaná_hodnota; tabulka; index_řádku; shoda)`

Jako SVYHLEDAT, ale hledá v **prvním řádku** (vodorovně).

```
=VVYHLEDAT(A1; B1:D10; 2; 0)
```

---

### INDEX
**Syntaxe:** `=INDEX(oblast; řádek; sloupec)`

Vrátí hodnotu na určité pozici v oblasti.

| Parametr | Popis |
|----------|-------|
| `oblast` | Oblast hledání |
| `řádek` | Číslo řádku |
| `sloupec` | Číslo sloupce (výchozí: 1) |

```
=INDEX(B1:B10; 3; 1)
```

---

### POZVYHLEDAT
**Syntaxe:** `=POZVYHLEDAT(hledaná_hodnota; oblast_hledání; typ_shody)`

Vrátí **pozici** hodnoty v oblasti.

| Typ shody | Význam |
|-----------|--------|
| `0` | Přesná shoda |
| `1` | Nejmenší větší nebo rovno |
| `-1` | Největší menší nebo rovno |

```
=POZVYHLEDAT(A1; A1:A10; 0)
```

---

### INDEX + POZVYHLEDAT
**Syntaxe:** `=INDEX(výsledná_oblast; POZVYHLEDAT(hledaná_hodnota; oblast_hledání; 0))`

Flexibilnější alternativa k SVYHLEDAT – umí hledat **v libovolném směru**.

| Parametr | Popis |
|----------|-------|
| `výsledná_oblast` | Sloupec s vracenými hodnotami |
| `hledaná_hodnota` | Hledaná hodnota |
| `oblast_hledání` | Sloupec, ve kterém se hledá |

```
=INDEX(B1:B10; POZVYHLEDAT(A1; A1:A10; 0))
```

> **Výhoda oproti SVYHLEDAT:** Vyhledávací sloupec nemusí být první. Stabilní i při vkládání/mazání sloupců.

---

### ZAOKROUHLIT
**Syntaxe:** `=ZAOKROUHLIT(číslo; desetinná_místa)`

Zaokrouhlí na zadaný počet desetinných míst.

| Desetinná místa | Příklad |
|----------------|---------|
| `2` | 3,14159 → 3,14 |
| `0` | 3,7 → 4 |
| `-1` | 34 → 30 |

```
=ZAOKROUHLIT(A1; 2)
```

---

### ZAOKROUHLIT.NAHORU
**Syntaxe:** `=ZAOKROUHLIT.NAHORU(číslo; desetinná_místa)`

Vždy zaokrouhlí **nahoru** (od nuly).

```
=ZAOKROUHLIT.NAHORU(A1; 2)
```

---

### ZAOKROUHLIT.DOLŮ
**Syntaxe:** `=ZAOKROUHLIT.DOLŮ(číslo; desetinná_místa)`

Vždy zaokrouhlí **dolů** (k nule).

```
=ZAOKROUHLIT.DOLŮ(A1; 2)
```

---

### CELÁ.ČÁST
**Syntaxe:** `=CELÁ.ČÁST(číslo)`

Zaokrouhlí dolů na nejbližší celé číslo (i pro záporná čísla).

```
=CELÁ.ČÁST(A1)
```

---

### USEKNOUT
**Syntaxe:** `=USEKNOUT(číslo; desetinná_místa)`

Ořízne desetinná místa **bez** zaokrouhlení.

```
=USEKNOUT(A1; 2)
```

---

### ABS
**Syntaxe:** `=ABS(číslo)`

Vrátí **absolutní hodnotu** (vždy kladnou).

```
=ABS(A1)
```

---

### MOD
**Syntaxe:** `=MOD(číslo; dělitel)`

Vrátí **zbytek** po dělení.

```
=MOD(A1; 3)
```
> Příklad: `=MOD(10; 3)` → `1`

---

### ODMOCNINA
**Syntaxe:** `=ODMOCNINA(číslo)`

Vypočítá druhou odmocninu.

```
=ODMOCNINA(A1)
```

---

### NÁHČÍSLO
**Syntaxe:** `=NÁHČÍSLO()`

Vrátí náhodné desetinné číslo mezi 0 a 1. Aktualizuje se při každém přepočtu.

```
=NÁHČÍSLO()
```

> Pro náhodné číslo mezi 1 a 100: `=CELÁ.ČÁST(NÁHČÍSLO()*100)+1`

---

## Absolutní odkazy

V programu lze režim odkazu vybrat pomocí rozevíracího seznamu:

| Režim | Příklad | Význam |
|-------|---------|--------|
| Relativní | `A1` | Posune se při kopírování |
| Pevný sloupec | `$A1` | Sloupec zůstane, řádek se posune |
| Pevný řádek | `A$1` | Řádek zůstane, sloupec se posune |
| Absolutní | `$A$1` | Při kopírování zůstane vždy stejný |

---

## Klávesové zkratky

| Zkratka | Funkce |
|---------|--------|
| `Ctrl+S` | Uložit vzorec do oblíbených |
| `Ctrl+C` | Kopírovat vzorec |
| `Ctrl+Z` | Zpět |
| `Ctrl+Y` | Znovu |
| `Ctrl+F12` | Minimalizovat / obnovit okno |
| `Del` | Smazat oblíbený (v seznamu) |
