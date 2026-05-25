# Funktionsreferenz – LibreOffice Calc Formel Helper

Alle Funktionen die im Programm verfügbar sind, mit Syntax, Parametern und Beispielen.


## Tab 1 – Grundfunktionen

### Rechenoperatoren

| Operator | Bedeutung | Beispiel | Ergebnis |
| - | - | - | - |
| `+` | Addition | `=A1+B1` | Summe zweier Zellen |
| `-` | Subtraktion | `=A1-B1` | Differenz |
| `\*` | Multiplikation | `=A1\*B1` | Produkt |
| `/` | Division | `=A1/B1` | Quotient |
| `^` | Potenz | `=A1^2` | A1 zum Quadrat |



### SUMME

**Syntax:** `=SUMME(Bereich)`

Addiert alle Zahlen in einem Zellbereich.

| Parameter | Beschreibung |
| - | - |
| `Bereich` | z. B. `A1:A10` |


```
=SUMME(A1:A10)
```


### MITTELWERT

**Syntax:** `=MITTELWERT(Bereich)`

Berechnet den Durchschnitt aller Zahlen im Bereich.

```
=MITTELWERT(A1:A10)
```


### MIN

**Syntax:** `=MIN(Bereich)`

Gibt den kleinsten Wert im Bereich zurück.

```
=MIN(A1:A10)
```


### MAX

**Syntax:** `=MAX(Bereich)`

Gibt den größten Wert im Bereich zurück.

```
=MAX(A1:A10)
```


### ANZAHL

**Syntax:** `=ANZAHL(Bereich)`

Zählt alle Zellen mit **Zahlenwerten** im Bereich.

```
=ANZAHL(A1:A10)
```


### ANZAHL2

**Syntax:** `=ANZAHL2(Bereich)`

Zählt alle **nicht leeren** Zellen (Zahlen und Text).

```
=ANZAHL2(A1:A10)
```


### MEDIAN

**Syntax:** `=MEDIAN(Bereich)`

Gibt den Mittelwert der sortierten Werteliste zurück (mittlerer Wert).

```
=MEDIAN(A1:A10)
```


### SUMMENPRODUKT

**Syntax:** `=SUMMENPRODUKT(Bereich1; Bereich2)`

Multipliziert die Elemente zweier Bereiche miteinander und addiert die Ergebnisse.

| Parameter | Beschreibung |
| - | - |
| `Bereich1` | Erster Bereich |
| `Bereich2` | Zweiter Bereich (gleiche Größe) |


```
=SUMMENPRODUKT(A1:A10; B1:B10)
```


## Tab 2 – Erweiterte Funktionen

### WENN

**Syntax:** `=WENN(Bedingung; Dann; Sonst)`

Gibt einen von zwei Werten zurück, je nachdem ob die Bedingung wahr oder falsch ist.

| Parameter | Beschreibung |
| - | - |
| `Bedingung` | z. B. `A1\>0` |
| `Dann` | Wert wenn wahr |
| `Sonst` | Wert wenn falsch |


```
=WENN(A1\>0; "OK"; "Fehler")
```


### UND

**Syntax:** `=UND(Bedingung1; Bedingung2)`

Gibt WAHR zurück wenn **alle** Bedingungen erfüllt sind.

```
=UND(A1\>0; B1\>0)
```


### ODER

**Syntax:** `=ODER(Bedingung1; Bedingung2)`

Gibt WAHR zurück wenn **mindestens eine** Bedingung erfüllt ist.

```
=ODER(A1\>0; B1\>0)
```


### NICHT

**Syntax:** `=NICHT(Bedingung)`

Kehrt einen Wahrheitswert um: WAHR → FALSCH, FALSCH → WAHR.

```
=NICHT(A1\>0)
```


### SUMMEWENN

**Syntax:** `=SUMMEWENN(Bereich; Kriterium; Summe\_Bereich)`

Addiert Werte die einem Kriterium entsprechen.

| Parameter | Beschreibung |
| - | - |
| `Bereich` | Bereich der geprüft wird |
| `Kriterium` | z. B. `"\>10"` oder `"Ja"` |
| `Summe\_Bereich` | Bereich der addiert wird |


```
=SUMMEWENN(A1:A10; "\>10"; B1:B10)
```


### ZÄHLENWENN

**Syntax:** `=ZÄHLENWENN(Bereich; Kriterium)`

Zählt Zellen die einem Kriterium entsprechen.

```
=ZÄHLENWENN(A1:A10; "Ja")
```


### MITTELWERTWENN

**Syntax:** `=MITTELWERTWENN(Bereich; Kriterium; Mittelwert\_Bereich)`

Berechnet den Durchschnitt der Werte die einem Kriterium entsprechen.

```
=MITTELWERTWENN(A1:A10; "\>0"; B1:B10)
```


### SUMMEWENNS

**Syntax:** `=SUMMEWENNS(Summe\_Bereich; Kriterien\_Bereich; Kriterium)`

Addiert Werte die **mehreren** Kriterien entsprechen.

| Parameter | Beschreibung |
| - | - |
| `Summe\_Bereich` | Bereich der addiert wird |
| `Kriterien\_Bereich` | Bereich der geprüft wird |
| `Kriterium` | Bedingung z. B. `"\>10"` |


```
=SUMMEWENNS(A1:A10; B1:B10; "\>10")
```


### STABW

**Syntax:** `=STABW(Bereich)`

Berechnet die Standardabweichung (Streuung der Werte).

```
=STABW(A1:A10)
```


### VARIANZ

**Syntax:** `=VARIANZ(Bereich)`

Berechnet die Varianz (quadratische Streuung).

```
=VARIANZ(A1:A10)
```


### ANZAHLLEEREZELLEN

**Syntax:** `=ANZAHLLEEREZELLEN(Bereich)`

Zählt alle **leeren** Zellen im Bereich.

```
=ANZAHLLEEREZELLEN(A1:A10)
```


### KGRÖSSTE

**Syntax:** `=KGRÖSSTE(Bereich; k)`

Gibt den k-größten Wert im Bereich zurück.

| Parameter | Beschreibung |
| - | - |
| `Bereich` | Zahlenbereich |
| `k` | Rang (1 = größter, 2 = zweitgrößter, …) |


```
=KGRÖSSTE(A1:A10; 2)
```


## Tab 3 – Datum & Text

### HEUTE

**Syntax:** `=HEUTE()`

Gibt das aktuelle Datum zurück. Wird bei jedem Öffnen der Datei aktualisiert.

```
=HEUTE()
```


### JETZT

**Syntax:** `=JETZT()`

Gibt das aktuelle Datum **mit Uhrzeit** zurück.

```
=JETZT()
```


### JAHR

**Syntax:** `=JAHR(Datum)`

Extrahiert das Jahr aus einem Datum.

```
=JAHR(A1)
```


### MONAT

**Syntax:** `=MONAT(Datum)`

Extrahiert den Monat (1–12) aus einem Datum.

```
=MONAT(A1)
```


### TAG

**Syntax:** `=TAG(Datum)`

Extrahiert den Tag (1–31) aus einem Datum.

```
=TAG(A1)
```


### DATUM

**Syntax:** `=DATUM(Jahr; Monat; Tag)`

Erstellt ein Datum aus einzelnen Werten.

```
=DATUM(2025; 1; 1)
```


### DATEDIF

**Syntax:** `=DATEDIF(Startdatum; Enddatum; Einheit)`

Berechnet die Differenz zwischen zwei Datumsangaben.

| Einheit | Bedeutung |
| - | - |
| `"D"` | Tage |
| `"M"` | Monate |
| `"Y"` | Jahre |


```
=DATEDIF(A1; B1; "D")
```

> **Hinweis:** DATEDIF ist eine undokumentierte Funktion – sie funktioniert in LibreOffice und Excel, erscheint aber nicht in der Autovervollständigung.


### WOCHENTAG

**Syntax:** `=WOCHENTAG(Datum; Typ)`

Gibt den Wochentag als Zahl zurück.

| Typ | Bedeutung |
| - | - |
| `2` | 1=Mo, 2=Di, … 7=So (empfohlen) |
| `1` | 1=So, 2=Mo, … 7=Sa |


```
=WOCHENTAG(A1; 2)
```


### VERKETTEN

**Syntax:** `=VERKETTEN(Text1; Text2; …)`

Verbindet mehrere Texte zu einem.

```
=VERKETTEN(A1; " "; B1)
```


### LÄNGE

**Syntax:** `=LÄNGE(Text)`

Gibt die Anzahl der Zeichen in einem Text zurück.

```
=LÄNGE(A1)
```


### LINKS

**Syntax:** `=LINKS(Text; Anzahl)`

Gibt die ersten n Zeichen eines Textes zurück.

```
=LINKS(A1; 5)
```


### RECHTS

**Syntax:** `=RECHTS(Text; Anzahl)`

Gibt die letzten n Zeichen eines Textes zurück.

```
=RECHTS(A1; 5)
```


### TEIL

**Syntax:** `=TEIL(Text; Startposition; Anzahl)`

Gibt einen Ausschnitt aus einem Text zurück.

| Parameter | Beschreibung |
| - | - |
| `Text` | Quelltext |
| `Startposition` | Ab welchem Zeichen (1 = erstes) |
| `Anzahl` | Wie viele Zeichen |


```
=TEIL(A1; 1; 5)
```


### GROSS

**Syntax:** `=GROSS(Text)`

Wandelt alle Buchstaben in Großbuchstaben um.

```
=GROSS(A1)
```


### KLEIN

**Syntax:** `=KLEIN(Text)`

Wandelt alle Buchstaben in Kleinbuchstaben um.

```
=KLEIN(A1)
```


### GLÄTTEN

**Syntax:** `=GLÄTTEN(Text)`

Entfernt überflüssige Leerzeichen (führend, nachfolgend, doppelt).

```
=GLÄTTEN(A1)
```


## Tab 4 – Nachschlagen & Runden

### SVERWEIS

**Syntax:** `=SVERWEIS(Suchkriterium; Matrix; Spaltenindex; Übereinstimmung)`

Sucht einen Wert in der **ersten Spalte** einer Tabelle und gibt den Wert aus einer anderen Spalte zurück.

| Parameter | Beschreibung |
| - | - |
| `Suchkriterium` | Gesuchter Wert, z. B. `A1` |
| `Matrix` | Suchbereich, z. B. `B1:D10` |
| `Spaltenindex` | Spaltennummer der Rückgabe (1 = erste Spalte) |
| `Übereinstimmung` | `0` = genau, `1` = ungefähr |


```
=SVERWEIS(A1; B1:D10; 2; 0)
```


### WVERWEIS

**Syntax:** `=WVERWEIS(Suchkriterium; Matrix; Zeilenindex; Übereinstimmung)`

Wie SVERWEIS, sucht aber in der **ersten Zeile** (waagerecht).

```
=WVERWEIS(A1; B1:D10; 2; 0)
```


### INDEX

**Syntax:** `=INDEX(Bereich; Zeile; Spalte)`

Gibt den Wert an einer bestimmten Position im Bereich zurück.

| Parameter | Beschreibung |
| - | - |
| `Bereich` | Suchbereich |
| `Zeile` | Zeilennummer |
| `Spalte` | Spaltennummer (Standard: 1) |


```
=INDEX(B1:B10; 3; 1)
```


### VERGLEICH

**Syntax:** `=VERGLEICH(Suchkriterium; Suchbereich; Vergleichstyp)`

Gibt die **Position** eines Wertes in einem Bereich zurück.

| Vergleichstyp | Bedeutung |
| - | - |
| `0` | Genaue Übereinstimmung |
| `1` | Kleinstes das größer oder gleich ist |
| `-1` | Größtes das kleiner oder gleich ist |


```
=VERGLEICH(A1; A1:A10; 0)
```


### INDEX + VERGLEICH

**Syntax:** `=INDEX(Ergebnis\_Bereich; VERGLEICH(Suchkriterium; Such\_Bereich; 0))`

Flexiblere Alternative zu SVERWEIS – kann in **jeder Richtung** suchen.

| Parameter | Beschreibung |
| - | - |
| `Ergebnis\_Bereich` | Spalte mit den Rückgabewerten |
| `Suchkriterium` | Gesuchter Wert |
| `Such\_Bereich` | Spalte in der gesucht wird |


```
=INDEX(B1:B10; VERGLEICH(A1; A1:A10; 0))
```

> **Vorteil gegenüber SVERWEIS:** Suchspalte muss nicht die erste Spalte sein. Auch bei Einfügen/Löschen von Spalten stabil.


### RUNDEN

**Syntax:** `=RUNDEN(Zahl; Dezimalstellen)`

Rundet auf die angegebene Anzahl Dezimalstellen.

| Dezimalstellen | Beispiel |
| - | - |
| `2` | 3,14159 → 3,14 |
| `0` | 3,7 → 4 |
| `-1` | 34 → 30 |


```
=RUNDEN(A1; 2)
```


### AUFRUNDEN

**Syntax:** `=AUFRUNDEN(Zahl; Dezimalstellen)`

Rundet immer **auf** (weg von 0).

```
=AUFRUNDEN(A1; 2)
```


### ABRUNDEN

**Syntax:** `=ABRUNDEN(Zahl; Dezimalstellen)`

Rundet immer **ab** (zur 0 hin).

```
=ABRUNDEN(A1; 2)
```


### GANZZAHL

**Syntax:** `=GANZZAHL(Zahl)`

Rundet auf die nächste ganze Zahl **ab** (auch bei negativen Zahlen).

```
=GANZZAHL(A1)
```


### KÜRZEN

**Syntax:** `=KÜRZEN(Zahl; Dezimalstellen)`

Schneidet Dezimalstellen ab **ohne** zu runden.

```
=KÜRZEN(A1; 2)
```


### ABS

**Syntax:** `=ABS(Zahl)`

Gibt den **absoluten Betrag** (immer positiv) zurück.

```
=ABS(A1)
```


### REST

**Syntax:** `=REST(Zahl; Divisor)`

Gibt den **Rest** einer Division zurück.

```
=REST(A1; 3)
```

> Beispiel: `=REST(10; 3)` → `1`


### WURZEL

**Syntax:** `=WURZEL(Zahl)`

Berechnet die Quadratwurzel.

```
=WURZEL(A1)
```


### ZUFALLSZAHL

**Syntax:** `=ZUFALLSZAHL()`

Gibt eine zufällige Dezimalzahl zwischen 0 und 1 zurück. Wird bei jeder Neuberechnung aktualisiert.

```
=ZUFALLSZAHL()
```

> Für eine Zufallszahl zwischen 1 und 100: `=GANZZAHL(ZUFALLSZAHL()\*100)+1`


## Absolute Referenzen

Im Programm kann der Referenz-Modus per Dropdown gewählt werden:

| Modus | Beispiel | Bedeutung |
| - | - | - |
| Relativ | `A1` | Verschiebt sich beim Kopieren |
| Spalte fixiert | `$A1` | Spalte bleibt, Zeile verschiebt sich |
| Zeile fixiert | `A$1` | Zeile bleibt, Spalte verschiebt sich |
| Absolut | `$A$1` | Bleibt beim Kopieren immer gleich |



## Tastaturkürzel

| Kürzel | Funktion |
| - | - |
| `Strg+S` | Formel in Favoriten speichern |
| `Strg+C` | Formel kopieren |
| `Strg+Z` | Rückgängig |
| `Strg+Y` | Wiederholen |
| `Strg+F12` | Fenster minimieren / wiederherstellen |
| `Entf` | Favorit löschen (in der Liste) |


