# LibreOffice Calc Assistente per Formule

Uno strumento Python per creare, testare e gestire rapidamente formule di LibreOffice Calc – con sistema dei preferiti, sincronizzazione del team, multilingua e gestore di plugin.

## 🚀 Funzionalità

- 📑 4 schede con oltre 60 funzioni

- 🌐 38 lingue (incluso l'hindi con installazione automatica del carattere)

- ⭐ Sistema dei preferiti (locale e sincronizzazione del team tramite unità di rete)

- 🛠 Pannello di amministrazione per i preferiti del team (protetto da password)

- 📋 Formule copiabili direttamente con evidenziazione della sintassi

- ✏️ Campo di output modificabile con Annulla/Ripristina

- 📖 Guida integrata e riferimento delle funzioni (per lingua)

- 💾 Salvataggio automatico (JSON, scrittura atomica)

- 🌙 Modalità scura

- 🔌 Gestore di plugin per creare plugin di formule personalizzati

- 🔤 Supporto RTL (da destra a sinistra) – rilevamento automatico della direzione di scrittura

- 🗄️ Backup e ripristino – salva tutte le impostazioni e i preferiti con nome e password

- ⌨️ Scorciatoia globale `Ctrl+F12` per ridurre a icona/ripristinare
- 🔍 Validatore JSON – controllo e correzione automatica di `languages.json` e `formula_explanations.json`

## 🖥️ Utilizzo

**1. Inserire i dati**

- Intervallo di celle (es. `A1:A10`)

- Cella 1 / Cella 2 (es. `A1`, `B1`)

- Parametro opzionale (es. testo o indice)

- Modalità riferimento assoluto selezionabile: `A1`, `$A1`, `A$1`, `$A$1`

**2. Selezionare una funzione** Scegli una scheda e clicca su una funzione – la formula viene generata immediatamente.

**3. Modificare la formula** La formula generata può essere modificata direttamente nel campo di output.

**4. Copiare** Con un clic negli appunti (inclusi i colori della sintassi).

**5. Usare i preferiti**

- ⭐ Salva → salva la formula corrente (Ctrl+S)

- 📂 Carica → riutilizza una formula

- ❌ Elimina → tasto Canc o pulsante

- 🕐 Cronologia → formule usate di recente

## 📊 Panoramica delle schede

**Scheda 1 – Funzioni di base** `+` `-` `\*` `/` `^` SUM, AVERAGE, MIN, MAX, MEDIAN, COUNT, COUNTA, SUMPRODUCT

**Scheda 2 – Funzioni avanzate** IF, AND, OR, NOT SUMIF, COUNTIF, AVERAGEIF, SUMIFS, STDEV, VAR, COUNTBLANK, LARGE

**Scheda 3 – Data e testo** TODAY, NOW, YEAR, MONTH, DAY, DATE, DATEDIF, WEEKDAY CONCATENATE, LEN, LEFT, RIGHT, MID, UPPER, LOWER, TRIM

**Scheda 4 – Ricerca e arrotondamento** VLOOKUP, HLOOKUP, INDEX, MATCH, INDEX+MATCH ROUND, ROUNDUP, ROUNDDOWN, INT, TRUNC, ABS, MOD, SQRT, RAND


## 📖 Spiegazioni delle formule dalla documentazione di LibreOffice

Il file `formula_explanations.json` viene popolato direttamente dalla **documentazione ufficiale di LibreOffice Calc** (https://help.libreoffice.org).

### Fonte dati e aggiornamento

- Descrizioni, informazioni sulla sintassi ed esempi vengono prelevati dal sito ufficiale di LibreOffice
- Le lingue supportate dipendono dalle traduzioni disponibili sul sito
- Il file contiene per ogni funzione: nome, sintassi, descrizione, esempio e categoria
- Aggiunte o correzioni possono essere effettuate manualmente (vedere Validatore JSON)

### Struttura di `formula_explanations.json`

```json
{
  "SUM": {
    "it": {
      "syntax": "SUM(Numero1; Numero2; ...)",
      "description": "Somma tutti i numeri in un intervallo di celle.",
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

| Campo | Obbligatorio | Descrizione |
|-------|-------------|-------------|
| `syntax` | ✅ | Sintassi della formula con parametri |
| `description` | ✅ | Breve descrizione della funzione |
| `example` | ✅ | Esempio d'uso come formula pronta |
| `note` | ❌ | Nota opzionale |

> 💡 **Nota:** Se non esiste una voce per una lingua, l'app torna automaticamente alla versione inglese.

---

## 🔍 Validatore JSON per i file di lingua

Il **Validatore JSON** integrato controlla e corregge `languages.json` e `formula_explanations.json` per coerenza, completezza e correttezza dei nomi dei paesi. Accessibile tramite **Impostazioni → 🔍 Validatore JSON**.

### Cosa viene controllato?

#### `languages.json`

- ✅ Tutte le 38 lingue presenti (per codice ISO 639-1)
- ✅ **Nomi di paese e lingua corretti** (es. `"it"` → `"Italiano"`)
- ✅ Nessun codice lingua duplicato
- ✅ Campi obbligatori presenti: `name`, `native_name`, `flag`, `rtl`
- ✅ Flag RTL impostato correttamente (Arabo, Ebraico, Persiano, Urdu → `"rtl": true`)

#### `formula_explanations.json`

- ✅ Tutte le funzioni delle 4 schede registrate
- ✅ Campi obbligatori presenti: `syntax`, `description`, `example`
- ✅ Nessun campo vuoto (`""` o `null`)
- ✅ I codici lingua corrispondono a `languages.json`

### Funzioni di correzione

| Tipo di errore | Correzione automatica |
|---------------|----------------------|
| Nome paese errato | Sostituito con il nome corretto secondo ISO |
| Voce lingua mancante | Integrata con versione inglese di riserva |
| Campo obbligatorio vuoto | Contrassegnato come `"[MISSING]"` per revisione manuale |
| Voce duplicata | Duplicati rimossi, voce più completa mantenuta |
| Flag RTL errato | Corretto automaticamente in base ai codici RTL noti |

### Come usarlo

1. Apri **Impostazioni → 🔍 Validatore JSON**
2. Seleziona il file: `languages.json` o `formula_explanations.json` (o entrambi)
3. **🔎 Controlla** – mostra tutti i problemi trovati
4. **🛠 Correggi automaticamente** – risolve tutti gli errori correggibili automaticamente
5. **💾 Salva** – riscrive il file corretto in modo atomico
6. **📋 Esporta report** (opzionale) – salva un file di testo con tutti i risultati

> ⚠️ **Nota:** Prima di ogni correzione automatica viene creata una copia di backup del file originale (`languages.json.bak` / `formula_explanations.json.bak`).

## ⭐ Sistema dei preferiti

- Salvare e riutilizzare le proprie formule

- Separazione tra preferiti personali e preferiti del team

- I preferiti del team sono in sola lettura (solo l'amministratore può modificarli)

- I duplicati vengono impediti

- Ordinamento libero dei preferiti personali

- Sincronizzazione tramite unità di rete (configurabile facoltativamente)

### Sincronizzazione del team

Tramite **Impostazioni → 🌐 Percorso di rete** è possibile inserire un'unità di rete (es. `\\\\Server\\Condivisione\\formule`).

- All'avvio: i preferiti di rete vengono salvati localmente (copia offline)

- Al salvataggio: le formule personali vengono scritte sulla rete, le formule del team rimangono intatte

## 🛠 Pannello di amministrazione

Accessibile tramite il pulsante 🛠. Al primo clic viene impostata una password (PBKDF2-SHA256, viene salvato solo l'hash).

- Aggiungere, modificare ed eliminare formule del team

- Cambiare la password

- Le modifiche vengono scritte direttamente sull'unità di rete

## 🔌 Gestore di plugin

Il gestore di plugin (`plugin_manager.py`) è uno strumento autonomo per creare e gestire plugin di formule personalizzati per Calc2. Si trova nella stessa cartella di `Calc2.py` e viene avviato con il pulsante 🔌 in Calc2.py:

### Funzioni

- **Creare un nuovo plugin** – procedura guidata passo dopo passo (nome, formule, traduzioni, riepilogo)

- **Aggiungere formule** – integrare un plugin esistente con nuove formule

- **Modificare le traduzioni** – tradurre i nomi delle formule in tutte le 38 lingue

- **Aprire la cartella dei plugin** – direttamente nel gestore file

- **Eliminare un plugin** – con conferma di sicurezza

### Struttura di un plugin

Ogni plugin si trova come sottocartella in `plugins/` ed è composto da due file:

```
plugins/
  mio_plugin/
    plugin.json      ← metadati (nome, versione, autore, descrizione)
    formulas.json    ← formule con traduzioni
```

**Esempio `plugin.json`:**

```
{
  "id": "mio_plugin",
  "enabled": true,
  "version": "1.0",
  "author": "Il Tuo Nome",
  "icon": "💰",
  "name": { "en": "Finance Formulas", "it": "Formule finanziarie" },
  "description": { "en": "Useful formulas for financial calculations." }
}
```

**Esempio `formulas.json`:**

```
[
  {
    "formula": "=SUM(A1:A10)",
    "name": { "en": "Sum of range", "it": "Somma dell'intervallo" },
    "description": { "en": "Adds all values in A1:A10." },
    "category": { "en": "Basic", "it": "Base" }
  }
]
```

### Avviso importante (⚠️ Important Notice)

Nel gestore di plugin è presente il pulsante **⚠️ Important Notice**. Cliccandolo si apre una finestra con tutte le regole per la corretta creazione di plugin in inglese. Le stesse informazioni sono disponibili anche in `IMPORTANT_NOTICE.md`.

## 🌐 Multilingua

38 lingue disponibili, selezionabili direttamente nell'applicazione.
È possibile aggiungere nuove lingue tramite il pulsante 🌍 con la procedura guidata per le lingue.

**Nota sull'hindi (हिंदी):** Al primo passaggio all'hindi, il carattere *Noto Sans Devanagari* viene installato una volta a livello di sistema. Windows richiederà i diritti di amministratore.

## 🔤 Supporto RTL (da destra a sinistra)

Le lingue con scrittura da destra a sinistra vengono rilevate automaticamente e l'intera interfaccia viene specchiata:

- **Arabo (عربي)** – rilevamento RTL automatico
- **Ebraico (עברית)** – rilevamento RTL automatico
- **Persiano / Farsi (فارسی)** – rilevamento RTL automatico
- **Urdu (اردو)** – rilevamento RTL automatico

**Cosa cambia in modalità RTL:** L'intero layout dell'interfaccia viene specchiato, i campi di input usano l'allineamento RTL, il carattere cambia automaticamente con uno compatibile RTL (es. *Noto Sans Arabic*, *Noto Sans Hebrew*).

> 💡 **Nota:** Le formule LibreOffice generate rimangono sempre in sintassi LTR – solo l'interfaccia utente cambia direzione.


## 🗄️ Backup e ripristino

### Creazione di un backup

Tramite **Impostazioni → 🗄️ Crea backup**:

1. **Nome** – etichetta libera (es. `Backup_Maggio_2025`)
2. **Password** – il backup è cifrato AES; senza di essa il ripristino non è possibile
3. **Posizione di salvataggio** – locale o su un'unità di rete
4. Clicca su **💾 Crea backup** – viene creato un file `.calc2backup`

**Contenuto:** Tutti i preferiti, le impostazioni, i preferiti del team (facoltativo), i plugin installati.

### Ripristino di un backup

Tramite **Impostazioni → 📂 Ripristina backup**:

1. Seleziona il file (`.calc2backup`)
2. Inserisci la password
3. Scegli l'ambito: solo preferiti / solo impostazioni / tutto
4. Clicca su **🔄 Ripristina**

> ⚠️ Durante il ripristino i dati esistenti vengono sovrascritti. Prima del ripristino viene proposto un backup automatico dei dati attuali.


## 💡 Suggerimenti

- `$A$1` → riferimento assoluto (menu a discesa accanto ai campi cella)

- **Ctrl+S** → salva la formula nei preferiti

- **Ctrl+C** → copia la formula (al di fuori dei campi di input)

- **Ctrl+Z / Ctrl+Y** → Annulla / Ripristina

- **Ctrl+F12** → riduci a icona/ripristina la finestra (funziona anche quando Calc2 è ridotto a icona)

- **Tasto Canc** nell'elenco dei preferiti → elimina una voce

- Le formule possono essere modificate direttamente nel campo di output dopo la generazione

## 📁 Struttura del progetto

```
Calc2.py                        ← programma principale
plugin_manager.py               ← gestore di plugin
IMPORTANT_NOTICE.md             ← istruzioni per la creazione di plugin
data/
  README_it.md / README_en.md / ...      ← guida per lingua
  RIFERIMENTO_it.md / RIFERIMENTO_en.md / ... ← riferimento funzioni per lingua
language/
  languages.json                ← traduzioni dell'interfaccia (38 lingue)
  formula_explanations.json
services/
  language_tool.py              ← procedura guidata: aggiungere una nuova lingua
  settings_service.py
  auth_service.py
  favorites_service.py
  network_sync.py
  install_service.py
  backup_service.py             ← backup e ripristino
  json_validator.py             ← controllo e correzione di languages.json / formula_explanations.json
plugins/                        ← cartella dei plugin (creata automaticamente)
  mio_plugin/
    plugin.json
    formulas.json
fonts/
  NotoSansDevanagari-Regular.ttf  ← carattere hindi
  NotoSansArabic-Regular.ttf      ← carattere arabo (RTL)
  NotoSansHebrew-Regular.ttf      ← carattere ebraico (RTL)
python/                         ← Python incorporato
  python.exe
  ...
settings.json                   ← creato automaticamente
preferiti.json                  ← preferiti locali (creato automaticamente)
```

## 🧠 Punti tecnici salienti

- **Scrittura atomica dei file** → impedisce il danneggiamento dei file durante il salvataggio

- **Architettura a servizi** → logica e interfaccia utente rigorosamente separate

- **Migrazione automatica** → i vecchi formati dei preferiti vengono rilevati e convertiti

- **Gestione degli errori robusta** → i file danneggiati non causano il blocco dell'applicazione

- **Evidenziazione della sintassi** → le formule vengono visualizzate a colori

- **Modalità scura** → completamente supportata

- **Sistema di plugin** → Calc2 è estendibile con plugin di formule personalizzati

- **Motore RTL** → rilevamento automatico delle lingue RTL, specchiatura completa dell'interfaccia con i caratteri adatti

- **Backup e ripristino** → backup cifrati AES con nome e password, ripristino selettivo

- **Validatore JSON** → controllo e correzione automatica di `languages.json` e `formula_explanations.json` incl. nomi dei paesi e campi obbligatori

- **Fonte LibreOffice** → `formula_explanations.json` viene popolato dalla documentazione ufficiale di LibreOffice Calc (https://help.libreoffice.org)

- **Scorciatoia globale** → `Ctrl+F12` funziona a livello di sistema tramite la libreria `keyboard` (thread in background)

## Licenza

Liberamente utilizzabile per scopi personali e commerciali.
