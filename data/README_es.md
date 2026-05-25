# LibreOffice Calc Asistente de Fórmulas

Una herramienta Python para crear, probar y gestionar fórmulas de LibreOffice Calc de forma rápida – con sistema de favoritos, sincronización de equipo, multilingüismo y gestor de plugins.

## 🚀 Funcionalidades

- 📑 4 pestañas con más de 60 funciones

- 🌐 38 idiomas (incluido hindi con instalación automática de fuentes)

- ⭐ Sistema de favoritos (local y sincronización de equipo mediante unidad de red)

- 🛠 Panel de administración para favoritos de equipo (protegido por contraseña)

- 📋 Fórmulas copiables directamente con resaltado de sintaxis

- ✏️ Campo de salida editable con Deshacer/Rehacer

- 📖 Ayuda integrada y referencia de funciones (por idioma)

- 💾 Guardado automático (JSON, escritura atómica)

- 🌙 Modo oscuro

- 🔌 Gestor de plugins para crear plugins de fórmulas propios

- 🔤 Compatibilidad RTL (de derecha a izquierda) – detección automática de la dirección de escritura

- 🗄️ Copia de seguridad y restauración – guarda todos los ajustes y favoritos con nombre y contraseña

- ⌨️ Atajo global `Ctrl+F12` para minimizar/restaurar
- 🔍 Validador JSON – comprobación y corrección automática de `languages.json` y `formula_explanations.json`

## 🖥️ Uso

**1. Introducir datos**

- Rango de celdas (p. ej. `A1:A10`)

- Celda 1 / Celda 2 (p. ej. `A1`, `B1`)

- Parámetro opcional (p. ej. texto o índice)

- Modo de referencia absoluta seleccionable: `A1`, `$A1`, `A$1`, `$A$1`

**2. Seleccionar función** Elige una pestaña y haz clic en una función – la fórmula se genera de inmediato.

**3. Ajustar la fórmula** La fórmula generada puede editarse directamente en el campo de salida.

**4. Copiar** Con un clic al portapapeles (incluidos los colores de sintaxis).

**5. Usar favoritos**

- ⭐ Guardar → guardar la fórmula actual (Ctrl+S)

- 📂 Cargar → reutilizar una fórmula

- ❌ Eliminar → tecla Supr o botón

- 🕐 Historial → fórmulas usadas recientemente

## 📊 Resumen de pestañas

**Pestaña 1 – Funciones básicas** `+` `-` `\*` `/` `^` SUM, AVERAGE, MIN, MAX, MEDIAN, COUNT, COUNTA, SUMPRODUCT

**Pestaña 2 – Funciones avanzadas** IF, AND, OR, NOT SUMIF, COUNTIF, AVERAGEIF, SUMIFS, STDEV, VAR, COUNTBLANK, LARGE

**Pestaña 3 – Fecha y texto** TODAY, NOW, YEAR, MONTH, DAY, DATE, DATEDIF, WEEKDAY CONCATENATE, LEN, LEFT, RIGHT, MID, UPPER, LOWER, TRIM

**Pestaña 4 – Búsqueda y redondeo** VLOOKUP, HLOOKUP, INDEX, MATCH, INDEX+MATCH ROUND, ROUNDUP, ROUNDDOWN, INT, TRUNC, ABS, MOD, SQRT, RAND


## 📖 Explicaciones de fórmulas desde la documentación de LibreOffice

El archivo `formula_explanations.json` se rellena directamente desde la **documentación oficial de LibreOffice Calc** (https://help.libreoffice.org).

### Fuente de datos y actualización

- Las descripciones, información de sintaxis y ejemplos se obtienen del sitio web de ayuda oficial de LibreOffice
- Los idiomas admitidos dependen de las traducciones disponibles en el sitio web
- El archivo contiene para cada función: nombre, sintaxis, descripción, ejemplo y categoría
- Se pueden añadir o corregir entradas manualmente (véase Validador JSON)

### Estructura de `formula_explanations.json`

```json
{
  "SUM": {
    "es": {
      "syntax": "SUM(Número1; Número2; ...)",
      "description": "Suma todos los números en un rango de celdas.",
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

| Campo | Obligatorio | Descripción |
|-------|------------|-------------|
| `syntax` | ✅ | Sintaxis de la fórmula con parámetros |
| `description` | ✅ | Descripción breve de la función |
| `example` | ✅ | Ejemplo de uso como fórmula lista para usar |
| `note` | ❌ | Nota opcional |

> 💡 **Nota:** Si no existe una entrada para un idioma, la app vuelve automáticamente a la versión en inglés.

---

## 🔍 Validador JSON para archivos de idioma

El **Validador JSON** integrado comprueba y corrige `languages.json` y `formula_explanations.json` para garantizar coherencia, completitud y designaciones de país correctas.

Accesible desde **Configuración → 🔍 Validador JSON**.

### ¿Qué se comprueba?

#### `languages.json`

- ✅ Los 38 idiomas presentes (por código ISO 639-1)
- ✅ **Nombres de país e idioma correctos** (p. ej. `"es"` → `"Español"`)
- ✅ Sin códigos de idioma duplicados
- ✅ Campos obligatorios presentes: `name`, `native_name`, `flag`, `rtl`
- ✅ Marca RTL correctamente configurada (Árabe, Hebreo, Persa, Urdu → `"rtl": true`)

#### `formula_explanations.json`

- ✅ Todas las funciones de las 4 pestañas registradas
- ✅ Campos obligatorios presentes: `syntax`, `description`, `example`
- ✅ Sin campos vacíos (`""` o `null`)
- ✅ Códigos de idioma coinciden con `languages.json`

### Funciones de corrección

| Tipo de error | Corrección automática |
|--------------|----------------------|
| Nombre de país incorrecto | Sustituido por el nombre correcto según ISO |
| Entrada de idioma faltante | Completado con versión de reserva en inglés |
| Campo obligatorio vacío | Marcado como `"[MISSING]"` para revisión manual |
| Entrada duplicada | Duplicados eliminados, se conserva la más completa |
| Marca RTL incorrecta | Corregida automáticamente según códigos RTL conocidos |

### Cómo usarlo

1. Abre **Configuración → 🔍 Validador JSON**
2. Selecciona el archivo: `languages.json` o `formula_explanations.json` (o ambos)
3. **🔎 Comprobar** – muestra todos los problemas encontrados
4. **🛠 Corregir automáticamente** – corrige todos los errores solucionables automáticamente
5. **💾 Guardar** – escribe atómicamente el archivo corregido
6. **📋 Exportar informe** (opcional) – guarda un archivo de texto con todos los hallazgos

> ⚠️ **Nota:** Antes de cada corrección automática se crea una copia de seguridad del archivo original (`languages.json.bak` / `formula_explanations.json.bak`).

## ⭐ Sistema de favoritos

- Guardar y reutilizar fórmulas propias

- Separación entre favoritos personales y de equipo

- Los favoritos de equipo son de solo lectura (solo el administrador puede editarlos)

- Se evitan entradas duplicadas

- Ordenación libre de los favoritos personales

- Sincronización mediante unidad de red (configurable opcionalmente)

### Sincronización de equipo

Mediante **Configuración → 🌐 Ruta de red** se puede introducir una unidad de red (p. ej. `\\\\Servidor\\Recurso\\formulas`).

- Al iniciar: los favoritos de red se guardan localmente (copia sin conexión)

- Al guardar: las fórmulas propias se escriben en la red, los favoritos de equipo no se modifican

## 🛠 Panel de administración

Accesible mediante el botón 🛠. Al hacer clic por primera vez se establece una contraseña (PBKDF2-SHA256, solo se guarda el hash).

- Añadir, editar y eliminar fórmulas de equipo

- Cambiar contraseña

- Los cambios se escriben directamente en la unidad de red

## 🔌 Gestor de plugins

El gestor de plugins (`plugin_manager.py`) es una herramienta independiente para crear y gestionar plugins de fórmulas propios para Calc2. Se encuentra en la misma carpeta que `Calc2.py` y se inicia con el botón 🔌 en Calc2.py:

### Funciones

- **Crear nuevo plugin** – asistente paso a paso (nombre, fórmulas, traducciones, resumen)

- **Añadir fórmulas** – agregar fórmulas a un plugin existente

- **Editar traducciones** – traducir nombres de fórmulas a los 38 idiomas

- **Abrir carpeta de plugins** – directamente en el explorador de archivos

- **Eliminar plugin** – con confirmación de seguridad

### Estructura del plugin

Cada plugin se encuentra como subcarpeta en `plugins/` y consta de dos archivos:

```
plugins/
  mi_plugin/
    plugin.json      ← metadatos (nombre, versión, autor, descripción)
    formulas.json    ← fórmulas con traducciones
```

**Ejemplo `plugin.json`:**

```
{
  "id": "mi_plugin",
  "enabled": true,
  "version": "1.0",
  "author": "Tu Nombre",
  "icon": "💰",
  "name": { "en": "Finance Formulas", "es": "Fórmulas Financieras" },
  "description": { "en": "Useful formulas for financial calculations." }
}
```

**Ejemplo `formulas.json`:**

```
[
  {
    "formula": "=SUM(A1:A10)",
    "name": { "en": "Sum of range", "es": "Suma del rango" },
    "description": { "en": "Adds all values in A1:A10." },
    "category": { "en": "Basic", "es": "Básico" }
  }
]
```

### Aviso importante (⚠️ Important Notice)

En el gestor de plugins hay un botón **⚠️ Important Notice**. Al hacer clic se abre una ventana con todas las reglas para la creación correcta de plugins en inglés. La misma información está disponible en `IMPORTANT_NOTICE.md`.

## 🌐 Multilingüismo

38 idiomas disponibles, cambiables directamente en la aplicación.
Se pueden añadir nuevos idiomas mediante el botón 🌍 con el asistente de idiomas.

**Nota sobre hindi (हिंदी):** Al cambiar a hindi por primera vez, se instala una vez la fuente *Noto Sans Devanagari* a nivel del sistema. Windows solicitará permisos de administrador.

## 🔤 Compatibilidad RTL (de derecha a izquierda)

Los idiomas con escritura de derecha a izquierda se detectan automáticamente y toda la interfaz se invierte:

- **Árabe (عربي)** – detección RTL automática
- **Hebreo (עברית)** – detección RTL automática
- **Persa / Farsi (فارسی)** – detección RTL automática
- **Urdu (اردو)** – detección RTL automática

**Qué cambia en modo RTL:** El diseño completo de la interfaz se invierte, los campos de entrada usan alineación RTL, la fuente cambia automáticamente a una compatible con RTL (p. ej. *Noto Sans Arabic*, *Noto Sans Hebrew*).

> 💡 **Nota:** Las fórmulas de LibreOffice generadas siempre permanecen en sintaxis LTR – solo la interfaz cambia de dirección.


## 🗄️ Copia de seguridad y restauración

### Crear una copia de seguridad

Mediante **Configuración → 🗄️ Crear copia de seguridad**:

1. **Nombre** – etiqueta libre (p. ej. `Backup_Mayo_2025`)
2. **Contraseña** – la copia se cifra con AES; sin ella no se puede restaurar
3. **Ubicación** – local o en una unidad de red
4. Haz clic en **💾 Crear copia de seguridad** – se genera un archivo `.calc2backup`

**Contenido:** Todos los favoritos, ajustes, favoritos de equipo (opcional), plugins instalados.

### Restaurar una copia de seguridad

Mediante **Configuración → 📂 Restaurar copia de seguridad**:

1. Selecciona el archivo (`.calc2backup`)
2. Introduce la contraseña
3. Elige el alcance: solo favoritos / solo ajustes / todo
4. Haz clic en **🔄 Restaurar**

> ⚠️ Los datos existentes se sobrescriben al restaurar. Antes se ofrece una copia automática de los datos actuales.


## 💡 Consejos

- `$A$1` → referencia absoluta (menú desplegable junto a los campos de celda)

- **Ctrl+S** → guardar fórmula en favoritos

- **Ctrl+C** → copiar fórmula (fuera de los campos de entrada)

- **Ctrl+Z / Ctrl+Y** → Deshacer / Rehacer

- **Ctrl+F12** → minimizar/restaurar ventana (funciona incluso cuando Calc2 está minimizado)

- **Tecla Supr** en la lista de favoritos → eliminar entrada

- Las fórmulas pueden ajustarse directamente en el campo de salida tras generarlas

## 📁 Estructura del proyecto

```
Calc2.py                        ← programa principal
plugin_manager.py               ← gestor de plugins
IMPORTANT_NOTICE.md             ← instrucciones para la creación de plugins
data/
  README_es.md / README_en.md / ...      ← ayuda por idioma
  REFERENCIA_es.md / REFERENCIA_en.md / ... ← referencia de funciones por idioma
language/
  languages.json                ← traducciones de la interfaz (38 idiomas)
  formula_explanations.json
services/
  language_tool.py              ← asistente: añadir nuevo idioma
  settings_service.py
  auth_service.py
  favorites_service.py
  network_sync.py
  install_service.py
  backup_service.py             ← copia de seguridad y restauración
  json_validator.py             ← comprobación y corrección de languages.json / formula_explanations.json
plugins/                        ← carpeta de plugins (creada automáticamente)
  mi_plugin/
    plugin.json
    formulas.json
fonts/
  NotoSansDevanagari-Regular.ttf  ← fuente hindi
  NotoSansArabic-Regular.ttf      ← fuente árabe (RTL)
  NotoSansHebrew-Regular.ttf      ← fuente hebrea (RTL)
python/                         ← Python integrado
  python.exe
  ...
settings.json                   ← se crea automáticamente
favoritos.json                  ← favoritos locales (se crea automáticamente)
```

## 🧠 Aspectos técnicos destacados

- **Escritura atómica de archivos** → evita archivos corruptos al guardar

- **Arquitectura de servicios** → lógica e interfaz de usuario estrictamente separadas

- **Migración automática** → los formatos de favoritos antiguos se detectan y convierten

- **Manejo robusto de errores** → los archivos dañados no causan fallos en la aplicación

- **Resaltado de sintaxis** → las fórmulas se muestran en color

- **Modo oscuro** → completamente compatible

- **Sistema de plugins** → Calc2 es ampliable mediante plugins de fórmulas propios

- **Motor RTL** → detección automática de idiomas RTL, espejo completo de la interfaz con fuentes adecuadas

- **Copia de seguridad y restauración** → copias cifradas AES con nombre y contraseña, restauración selectiva

- **Validador JSON** → comprobación y corrección automática de `languages.json` y `formula_explanations.json` incl. nombres de país y campos obligatorios

- **Fuente LibreOffice** → `formula_explanations.json` se rellena desde la documentación oficial de LibreOffice Calc (https://help.libreoffice.org)

- **Atajo global** → `Ctrl+F12` funciona a nivel del sistema mediante la biblioteca `keyboard` (hilo en segundo plano)

## Licencia

De uso libre para fines personales y comerciales.
