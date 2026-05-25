# Function Reference – LibreOffice Calc Formula Helper

All functions available in the program, with syntax, parameters, and examples.

---

## Tab 1 – Basic Functions

### Arithmetic Operators

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `+` | Addition | `=A1+B1` | Sum of two cells |
| `-` | Subtraction | `=A1-B1` | Difference |
| `*` | Multiplication | `=A1*B1` | Product |
| `/` | Division | `=A1/B1` | Quotient |
| `^` | Exponentiation | `=A1^2` | A1 squared |

---

### SUM
**Syntax:** `=SUM(range)`

Adds all numbers in a cell range.

| Parameter | Description |
|-----------|-------------|
| `range` | e.g. `A1:A10` |

```
=SUM(A1:A10)
```

---

### AVERAGE
**Syntax:** `=AVERAGE(range)`

Calculates the average of all numbers in the range.

```
=AVERAGE(A1:A10)
```

---

### MIN
**Syntax:** `=MIN(range)`

Returns the smallest value in the range.

```
=MIN(A1:A10)
```

---

### MAX
**Syntax:** `=MAX(range)`

Returns the largest value in the range.

```
=MAX(A1:A10)
```

---

### COUNT
**Syntax:** `=COUNT(range)`

Counts all cells with **numeric values** in the range.

```
=COUNT(A1:A10)
```

---

### COUNTA
**Syntax:** `=COUNTA(range)`

Counts all **non-empty** cells (numbers and text).

```
=COUNTA(A1:A10)
```

---

### MEDIAN
**Syntax:** `=MEDIAN(range)`

Returns the median of the sorted value list (middle value).

```
=MEDIAN(A1:A10)
```

---

### SUMPRODUCT
**Syntax:** `=SUMPRODUCT(range1; range2)`

Multiplies the elements of two ranges together and adds the results.

| Parameter | Description |
|-----------|-------------|
| `range1` | First range |
| `range2` | Second range (same size) |

```
=SUMPRODUCT(A1:A10; B1:B10)
```

---

## Tab 2 – Advanced Functions

### IF
**Syntax:** `=IF(condition; then; else)`

Returns one of two values depending on whether the condition is true or false.

| Parameter | Description |
|-----------|-------------|
| `condition` | e.g. `A1>0` |
| `then` | Value if true |
| `else` | Value if false |

```
=IF(A1>0; "OK"; "Error")
```

---

### AND
**Syntax:** `=AND(condition1; condition2)`

Returns TRUE if **all** conditions are met.

```
=AND(A1>0; B1>0)
```

---

### OR
**Syntax:** `=OR(condition1; condition2)`

Returns TRUE if **at least one** condition is met.

```
=OR(A1>0; B1>0)
```

---

### NOT
**Syntax:** `=NOT(condition)`

Reverses a logical value: TRUE → FALSE, FALSE → TRUE.

```
=NOT(A1>0)
```

---

### SUMIF
**Syntax:** `=SUMIF(range; criterion; sum_range)`

Adds values that match a criterion.

| Parameter | Description |
|-----------|-------------|
| `range` | Range to be checked |
| `criterion` | e.g. `">10"` or `"Yes"` |
| `sum_range` | Range to be added |

```
=SUMIF(A1:A10; ">10"; B1:B10)
```

---

### COUNTIF
**Syntax:** `=COUNTIF(range; criterion)`

Counts cells that match a criterion.

```
=COUNTIF(A1:A10; "Yes")
```

---

### AVERAGEIF
**Syntax:** `=AVERAGEIF(range; criterion; average_range)`

Calculates the average of values that match a criterion.

```
=AVERAGEIF(A1:A10; ">0"; B1:B10)
```

---

### SUMIFS
**Syntax:** `=SUMIFS(sum_range; criteria_range; criterion)`

Adds values that match **multiple** criteria.

| Parameter | Description |
|-----------|-------------|
| `sum_range` | Range to be added |
| `criteria_range` | Range to be checked |
| `criterion` | Condition e.g. `">10"` |

```
=SUMIFS(A1:A10; B1:B10; ">10")
```

---

### STDEV
**Syntax:** `=STDEV(range)`

Calculates the standard deviation (spread of values).

```
=STDEV(A1:A10)
```

---

### VAR
**Syntax:** `=VAR(range)`

Calculates the variance (squared spread).

```
=VAR(A1:A10)
```

---

### COUNTBLANK
**Syntax:** `=COUNTBLANK(range)`

Counts all **empty** cells in the range.

```
=COUNTBLANK(A1:A10)
```

---

### LARGE
**Syntax:** `=LARGE(range; k)`

Returns the k-th largest value in the range.

| Parameter | Description |
|-----------|-------------|
| `range` | Number range |
| `k` | Rank (1 = largest, 2 = second largest, …) |

```
=LARGE(A1:A10; 2)
```

---

## Tab 3 – Date & Text

### TODAY
**Syntax:** `=TODAY()`

Returns the current date. Updated every time the file is opened.

```
=TODAY()
```

---

### NOW
**Syntax:** `=NOW()`

Returns the current date **with time**.

```
=NOW()
```

---

### YEAR
**Syntax:** `=YEAR(date)`

Extracts the year from a date.

```
=YEAR(A1)
```

---

### MONTH
**Syntax:** `=MONTH(date)`

Extracts the month (1–12) from a date.

```
=MONTH(A1)
```

---

### DAY
**Syntax:** `=DAY(date)`

Extracts the day (1–31) from a date.

```
=DAY(A1)
```

---

### DATE
**Syntax:** `=DATE(year; month; day)`

Creates a date from individual values.

```
=DATE(2025; 1; 1)
```

---

### DATEDIF
**Syntax:** `=DATEDIF(start_date; end_date; unit)`

Calculates the difference between two dates.

| Unit | Meaning |
|------|---------|
| `"D"` | Days |
| `"M"` | Months |
| `"Y"` | Years |

```
=DATEDIF(A1; B1; "D")
```

> **Note:** DATEDIF is an undocumented function – it works in LibreOffice and Excel but does not appear in autocomplete.

---

### WEEKDAY
**Syntax:** `=WEEKDAY(date; type)`

Returns the day of the week as a number.

| Type | Meaning |
|------|---------|
| `2` | 1=Mon, 2=Tue, … 7=Sun (recommended) |
| `1` | 1=Sun, 2=Mon, … 7=Sat |

```
=WEEKDAY(A1; 2)
```

---

### CONCATENATE
**Syntax:** `=CONCATENATE(text1; text2; …)`

Joins multiple texts into one.

```
=CONCATENATE(A1; " "; B1)
```

---

### LEN
**Syntax:** `=LEN(text)`

Returns the number of characters in a text.

```
=LEN(A1)
```

---

### LEFT
**Syntax:** `=LEFT(text; count)`

Returns the first n characters of a text.

```
=LEFT(A1; 5)
```

---

### RIGHT
**Syntax:** `=RIGHT(text; count)`

Returns the last n characters of a text.

```
=RIGHT(A1; 5)
```

---

### MID
**Syntax:** `=MID(text; start_position; count)`

Returns a substring from a text.

| Parameter | Description |
|-----------|-------------|
| `text` | Source text |
| `start_position` | Starting character (1 = first) |
| `count` | How many characters |

```
=MID(A1; 1; 5)
```

---

### UPPER
**Syntax:** `=UPPER(text)`

Converts all letters to uppercase.

```
=UPPER(A1)
```

---

### LOWER
**Syntax:** `=LOWER(text)`

Converts all letters to lowercase.

```
=LOWER(A1)
```

---

### TRIM
**Syntax:** `=TRIM(text)`

Removes excess spaces (leading, trailing, and double spaces).

```
=TRIM(A1)
```

---

## Tab 4 – Lookup & Rounding

### VLOOKUP
**Syntax:** `=VLOOKUP(lookup_value; table; column_index; match)`

Searches for a value in the **first column** of a table and returns the value from another column.

| Parameter | Description |
|-----------|-------------|
| `lookup_value` | Value to search for, e.g. `A1` |
| `table` | Search range, e.g. `B1:D10` |
| `column_index` | Column number to return (1 = first column) |
| `match` | `0` = exact, `1` = approximate |

```
=VLOOKUP(A1; B1:D10; 2; 0)
```

---

### HLOOKUP
**Syntax:** `=HLOOKUP(lookup_value; table; row_index; match)`

Like VLOOKUP, but searches in the **first row** (horizontally).

```
=HLOOKUP(A1; B1:D10; 2; 0)
```

---

### INDEX
**Syntax:** `=INDEX(range; row; column)`

Returns the value at a specific position in the range.

| Parameter | Description |
|-----------|-------------|
| `range` | Search range |
| `row` | Row number |
| `column` | Column number (default: 1) |

```
=INDEX(B1:B10; 3; 1)
```

---

### MATCH
**Syntax:** `=MATCH(lookup_value; lookup_range; match_type)`

Returns the **position** of a value in a range.

| Match type | Meaning |
|------------|---------|
| `0` | Exact match |
| `1` | Smallest value greater than or equal |
| `-1` | Largest value less than or equal |

```
=MATCH(A1; A1:A10; 0)
```

---

### INDEX + MATCH
**Syntax:** `=INDEX(result_range; MATCH(lookup_value; lookup_range; 0))`

A more flexible alternative to VLOOKUP – can search in **any direction**.

| Parameter | Description |
|-----------|-------------|
| `result_range` | Column with return values |
| `lookup_value` | Value to search for |
| `lookup_range` | Column to search in |

```
=INDEX(B1:B10; MATCH(A1; A1:A10; 0))
```

> **Advantage over VLOOKUP:** The search column does not need to be the first column. Also stable when inserting/deleting columns.

---

### ROUND
**Syntax:** `=ROUND(number; decimal_places)`

Rounds to the specified number of decimal places.

| Decimal places | Example |
|----------------|---------|
| `2` | 3.14159 → 3.14 |
| `0` | 3.7 → 4 |
| `-1` | 34 → 30 |

```
=ROUND(A1; 2)
```

---

### ROUNDUP
**Syntax:** `=ROUNDUP(number; decimal_places)`

Always rounds **up** (away from zero).

```
=ROUNDUP(A1; 2)
```

---

### ROUNDDOWN
**Syntax:** `=ROUNDDOWN(number; decimal_places)`

Always rounds **down** (toward zero).

```
=ROUNDDOWN(A1; 2)
```

---

### INT
**Syntax:** `=INT(number)`

Rounds down to the nearest whole number (also for negative numbers).

```
=INT(A1)
```

---

### TRUNC
**Syntax:** `=TRUNC(number; decimal_places)`

Truncates decimal places **without** rounding.

```
=TRUNC(A1; 2)
```

---

### ABS
**Syntax:** `=ABS(number)`

Returns the **absolute value** (always positive).

```
=ABS(A1)
```

---

### MOD
**Syntax:** `=MOD(number; divisor)`

Returns the **remainder** of a division.

```
=MOD(A1; 3)
```
> Example: `=MOD(10; 3)` → `1`

---

### SQRT
**Syntax:** `=SQRT(number)`

Calculates the square root.

```
=SQRT(A1)
```

---

### RAND
**Syntax:** `=RAND()`

Returns a random decimal number between 0 and 1. Updated with every recalculation.

```
=RAND()
```

> For a random number between 1 and 100: `=INT(RAND()*100)+1`

---

## Absolute References

In the program, the reference mode can be selected via a dropdown:

| Mode | Example | Meaning |
|------|---------|---------|
| Relative | `A1` | Shifts when copied |
| Column fixed | `$A1` | Column stays, row shifts |
| Row fixed | `A$1` | Row stays, column shifts |
| Absolute | `$A$1` | Always stays the same when copied |

---

## Keyboard Shortcuts

| Shortcut | Function |
|----------|---------|
| `Ctrl+S` | Save formula to favorites |
| `Ctrl+C` | Copy formula |
| `Ctrl+Z` | Undo |
| `Ctrl+Y` | Redo |
| `Ctrl+F12` | Minimize / restore window |
| `Del` | Delete favorite (in the list) |
