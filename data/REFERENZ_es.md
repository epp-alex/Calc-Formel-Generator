# Referencia de funciones – Asistente de fórmulas de LibreOffice Calc

Todas las funciones disponibles en el programa, con sintaxis, parámetros y ejemplos.

---

## Pestaña 1 – Funciones básicas

### Operadores aritméticos

| Operador | Significado | Ejemplo | Resultado |
|----------|-------------|---------|-----------|
| `+` | Suma | `=A1+B1` | Suma de dos celdas |
| `-` | Resta | `=A1-B1` | Diferencia |
| `*` | Multiplicación | `=A1*B1` | Producto |
| `/` | División | `=A1/B1` | Cociente |
| `^` | Potencia | `=A1^2` | A1 al cuadrado |

---

### SUMA
**Sintaxis:** `=SUMA(rango)`

Suma todos los números de un rango de celdas.

| Parámetro | Descripción |
|-----------|-------------|
| `rango` | p. ej. `A1:A10` |

```
=SUMA(A1:A10)
```

---

### PROMEDIO
**Sintaxis:** `=PROMEDIO(rango)`

Calcula la media de todos los números del rango.

```
=PROMEDIO(A1:A10)
```

---

### MIN
**Sintaxis:** `=MIN(rango)`

Devuelve el valor más pequeño del rango.

```
=MIN(A1:A10)
```

---

### MAX
**Sintaxis:** `=MAX(rango)`

Devuelve el valor más grande del rango.

```
=MAX(A1:A10)
```

---

### CONTAR
**Sintaxis:** `=CONTAR(rango)`

Cuenta todas las celdas con **valores numéricos** del rango.

```
=CONTAR(A1:A10)
```

---

### CONTARA
**Sintaxis:** `=CONTARA(rango)`

Cuenta todas las celdas **no vacías** (números y texto).

```
=CONTARA(A1:A10)
```

---

### MEDIANA
**Sintaxis:** `=MEDIANA(rango)`

Devuelve el valor central de la lista de valores ordenados.

```
=MEDIANA(A1:A10)
```

---

### SUMAPRODUCTO
**Sintaxis:** `=SUMAPRODUCTO(rango1; rango2)`

Multiplica los elementos de dos rangos entre sí y suma los resultados.

| Parámetro | Descripción |
|-----------|-------------|
| `rango1` | Primer rango |
| `rango2` | Segundo rango (mismo tamaño) |

```
=SUMAPRODUCTO(A1:A10; B1:B10)
```

---

## Pestaña 2 – Funciones avanzadas

### SI
**Sintaxis:** `=SI(condición; entonces; si_no)`

Devuelve uno de dos valores según si la condición es verdadera o falsa.

| Parámetro | Descripción |
|-----------|-------------|
| `condición` | p. ej. `A1>0` |
| `entonces` | Valor si es verdadero |
| `si_no` | Valor si es falso |

```
=SI(A1>0; "OK"; "Error")
```

---

### Y
**Sintaxis:** `=Y(condición1; condición2)`

Devuelve VERDADERO si **todas** las condiciones se cumplen.

```
=Y(A1>0; B1>0)
```

---

### O
**Sintaxis:** `=O(condición1; condición2)`

Devuelve VERDADERO si **al menos una** condición se cumple.

```
=O(A1>0; B1>0)
```

---

### NO
**Sintaxis:** `=NO(condición)`

Invierte un valor lógico: VERDADERO → FALSO, FALSO → VERDADERO.

```
=NO(A1>0)
```

---

### SUMAR.SI
**Sintaxis:** `=SUMAR.SI(rango; criterio; rango_suma)`

Suma los valores que cumplen un criterio.

| Parámetro | Descripción |
|-----------|-------------|
| `rango` | Rango que se evalúa |
| `criterio` | p. ej. `">10"` o `"Sí"` |
| `rango_suma` | Rango que se suma |

```
=SUMAR.SI(A1:A10; ">10"; B1:B10)
```

---

### CONTAR.SI
**Sintaxis:** `=CONTAR.SI(rango; criterio)`

Cuenta las celdas que cumplen un criterio.

```
=CONTAR.SI(A1:A10; "Sí")
```

---

### PROMEDIO.SI
**Sintaxis:** `=PROMEDIO.SI(rango; criterio; rango_promedio)`

Calcula la media de los valores que cumplen un criterio.

```
=PROMEDIO.SI(A1:A10; ">0"; B1:B10)
```

---

### SUMAR.SI.CONJUNTO
**Sintaxis:** `=SUMAR.SI.CONJUNTO(rango_suma; rango_criterios; criterio)`

Suma los valores que cumplen **varios** criterios.

| Parámetro | Descripción |
|-----------|-------------|
| `rango_suma` | Rango que se suma |
| `rango_criterios` | Rango que se evalúa |
| `criterio` | Condición, p. ej. `">10"` |

```
=SUMAR.SI.CONJUNTO(A1:A10; B1:B10; ">10")
```

---

### DESVEST
**Sintaxis:** `=DESVEST(rango)`

Calcula la desviación estándar (dispersión de los valores).

```
=DESVEST(A1:A10)
```

---

### VAR
**Sintaxis:** `=VAR(rango)`

Calcula la varianza (dispersión al cuadrado).

```
=VAR(A1:A10)
```

---

### CONTAR.BLANCO
**Sintaxis:** `=CONTAR.BLANCO(rango)`

Cuenta todas las celdas **vacías** del rango.

```
=CONTAR.BLANCO(A1:A10)
```

---

### K.ESIMO.MAYOR
**Sintaxis:** `=K.ESIMO.MAYOR(rango; k)`

Devuelve el k-ésimo valor más grande del rango.

| Parámetro | Descripción |
|-----------|-------------|
| `rango` | Rango de números |
| `k` | Posición (1 = mayor, 2 = segundo mayor, …) |

```
=K.ESIMO.MAYOR(A1:A10; 2)
```

---

## Pestaña 3 – Fecha y texto

### HOY
**Sintaxis:** `=HOY()`

Devuelve la fecha actual. Se actualiza cada vez que se abre el archivo.

```
=HOY()
```

---

### AHORA
**Sintaxis:** `=AHORA()`

Devuelve la fecha actual **con la hora**.

```
=AHORA()
```

---

### AÑO
**Sintaxis:** `=AÑO(fecha)`

Extrae el año de una fecha.

```
=AÑO(A1)
```

---

### MES
**Sintaxis:** `=MES(fecha)`

Extrae el mes (1–12) de una fecha.

```
=MES(A1)
```

---

### DIA
**Sintaxis:** `=DIA(fecha)`

Extrae el día (1–31) de una fecha.

```
=DIA(A1)
```

---

### FECHA
**Sintaxis:** `=FECHA(año; mes; día)`

Crea una fecha a partir de valores individuales.

```
=FECHA(2025; 1; 1)
```

---

### SIFECHA
**Sintaxis:** `=SIFECHA(fecha_inicio; fecha_fin; unidad)`

Calcula la diferencia entre dos fechas.

| Unidad | Significado |
|--------|-------------|
| `"D"` | Días |
| `"M"` | Meses |
| `"Y"` | Años |

```
=SIFECHA(A1; B1; "D")
```

> **Nota:** SIFECHA es una función no documentada – funciona en LibreOffice y Excel, pero no aparece en el autocompletado.

---

### DIASEM
**Sintaxis:** `=DIASEM(fecha; tipo)`

Devuelve el día de la semana como número.

| Tipo | Significado |
|------|-------------|
| `2` | 1=Lun, 2=Mar, … 7=Dom (recomendado) |
| `1` | 1=Dom, 2=Lun, … 7=Sáb |

```
=DIASEM(A1; 2)
```

---

### CONCATENAR
**Sintaxis:** `=CONCATENAR(texto1; texto2; …)`

Une varios textos en uno.

```
=CONCATENAR(A1; " "; B1)
```

---

### LARGO
**Sintaxis:** `=LARGO(texto)`

Devuelve el número de caracteres de un texto.

```
=LARGO(A1)
```

---

### IZQUIERDA
**Sintaxis:** `=IZQUIERDA(texto; número)`

Devuelve los primeros n caracteres de un texto.

```
=IZQUIERDA(A1; 5)
```

---

### DERECHA
**Sintaxis:** `=DERECHA(texto; número)`

Devuelve los últimos n caracteres de un texto.

```
=DERECHA(A1; 5)
```

---

### EXTRAE
**Sintaxis:** `=EXTRAE(texto; posición_inicial; número)`

Devuelve un fragmento de un texto.

| Parámetro | Descripción |
|-----------|-------------|
| `texto` | Texto de origen |
| `posición_inicial` | Desde qué carácter (1 = primero) |
| `número` | Cuántos caracteres |

```
=EXTRAE(A1; 1; 5)
```

---

### MAYUSC
**Sintaxis:** `=MAYUSC(texto)`

Convierte todas las letras en mayúsculas.

```
=MAYUSC(A1)
```

---

### MINUSC
**Sintaxis:** `=MINUSC(texto)`

Convierte todas las letras en minúsculas.

```
=MINUSC(A1)
```

---

### ESPACIOS
**Sintaxis:** `=ESPACIOS(texto)`

Elimina los espacios sobrantes (iniciales, finales y dobles).

```
=ESPACIOS(A1)
```

---

## Pestaña 4 – Búsqueda y redondeo

### BUSCARV
**Sintaxis:** `=BUSCARV(valor_buscado; matriz; índice_columna; coincidencia)`

Busca un valor en la **primera columna** de una tabla y devuelve el valor de otra columna.

| Parámetro | Descripción |
|-----------|-------------|
| `valor_buscado` | Valor buscado, p. ej. `A1` |
| `matriz` | Rango de búsqueda, p. ej. `B1:D10` |
| `índice_columna` | Número de columna del resultado (1 = primera columna) |
| `coincidencia` | `0` = exacta, `1` = aproximada |

```
=BUSCARV(A1; B1:D10; 2; 0)
```

---

### BUSCARH
**Sintaxis:** `=BUSCARH(valor_buscado; matriz; índice_fila; coincidencia)`

Como BUSCARV, pero busca en la **primera fila** (horizontal).

```
=BUSCARH(A1; B1:D10; 2; 0)
```

---

### INDICE
**Sintaxis:** `=INDICE(rango; fila; columna)`

Devuelve el valor en una posición determinada del rango.

| Parámetro | Descripción |
|-----------|-------------|
| `rango` | Rango de búsqueda |
| `fila` | Número de fila |
| `columna` | Número de columna (predeterminado: 1) |

```
=INDICE(B1:B10; 3; 1)
```

---

### COINCIDIR
**Sintaxis:** `=COINCIDIR(valor_buscado; rango_búsqueda; tipo_coincidencia)`

Devuelve la **posición** de un valor en un rango.

| Tipo de coincidencia | Significado |
|----------------------|-------------|
| `0` | Coincidencia exacta |
| `1` | El más pequeño mayor o igual |
| `-1` | El más grande menor o igual |

```
=COINCIDIR(A1; A1:A10; 0)
```

---

### INDICE + COINCIDIR
**Sintaxis:** `=INDICE(rango_resultado; COINCIDIR(valor_buscado; rango_búsqueda; 0))`

Alternativa más flexible a BUSCARV – puede buscar en **cualquier dirección**.

| Parámetro | Descripción |
|-----------|-------------|
| `rango_resultado` | Columna con los valores de retorno |
| `valor_buscado` | Valor buscado |
| `rango_búsqueda` | Columna donde se busca |

```
=INDICE(B1:B10; COINCIDIR(A1; A1:A10; 0))
```

> **Ventaja sobre BUSCARV:** La columna de búsqueda no tiene que ser la primera. También es estable al insertar o eliminar columnas.

---

### REDONDEAR
**Sintaxis:** `=REDONDEAR(número; decimales)`

Redondea al número de decimales indicado.

| Decimales | Ejemplo |
|-----------|---------|
| `2` | 3,14159 → 3,14 |
| `0` | 3,7 → 4 |
| `-1` | 34 → 30 |

```
=REDONDEAR(A1; 2)
```

---

### REDONDEAR.MAS
**Sintaxis:** `=REDONDEAR.MAS(número; decimales)`

Redondea siempre **hacia arriba** (alejándose del cero).

```
=REDONDEAR.MAS(A1; 2)
```

---

### REDONDEAR.MENOS
**Sintaxis:** `=REDONDEAR.MENOS(número; decimales)`

Redondea siempre **hacia abajo** (hacia el cero).

```
=REDONDEAR.MENOS(A1; 2)
```

---

### ENTERO
**Sintaxis:** `=ENTERO(número)`

Redondea al entero más próximo **hacia abajo** (también para números negativos).

```
=ENTERO(A1)
```

---

### TRUNCAR
**Sintaxis:** `=TRUNCAR(número; decimales)`

Elimina los decimales **sin redondear**.

```
=TRUNCAR(A1; 2)
```

---

### ABS
**Sintaxis:** `=ABS(número)`

Devuelve el **valor absoluto** (siempre positivo).

```
=ABS(A1)
```

---

### RESIDUO
**Sintaxis:** `=RESIDUO(número; divisor)`

Devuelve el **resto** de una división.

```
=RESIDUO(A1; 3)
```
> Ejemplo: `=RESIDUO(10; 3)` → `1`

---

### RAIZ
**Sintaxis:** `=RAIZ(número)`

Calcula la raíz cuadrada.

```
=RAIZ(A1)
```

---

### ALEATORIO
**Sintaxis:** `=ALEATORIO()`

Devuelve un número decimal aleatorio entre 0 y 1. Se actualiza con cada recálculo.

```
=ALEATORIO()
```

> Para un número aleatorio entre 1 y 100: `=ENTERO(ALEATORIO()*100)+1`

---

## Referencias absolutas

En el programa se puede elegir el modo de referencia desde un menú desplegable:

| Modo | Ejemplo | Significado |
|------|---------|-------------|
| Relativa | `A1` | Se desplaza al copiar |
| Columna fija | `$A1` | La columna se fija, la fila se desplaza |
| Fila fija | `A$1` | La fila se fija, la columna se desplaza |
| Absoluta | `$A$1` | Siempre igual al copiar |

---

## Atajos de teclado

| Atajo | Función |
|-------|---------|
| `Ctrl+S` | Guardar fórmula en favoritos |
| `Ctrl+C` | Copiar fórmula |
| `Ctrl+Z` | Deshacer |
| `Ctrl+Y` | Rehacer |
| `Ctrl+F12` | Minimizar / restaurar ventana |
| `Supr` | Eliminar favorito (en la lista) |
