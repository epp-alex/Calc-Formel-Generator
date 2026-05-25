# LibreOffice Calc Pomocnik Formuł

Narzędzie Python do szybkiego tworzenia, testowania i zarządzania formułami LibreOffice Calc – z systemem ulubionych, synchronizacją zespołową, wielojęzycznością i menedżerem wtyczek.

## 🚀 Funkcje

- 📑 4 zakładki z ponad 60 funkcjami

- 🌐 38 języków (w tym hindi z automatyczną instalacją czcionki)

- ⭐ System ulubionych (lokalnie i synchronizacja zespołowa przez dysk sieciowy)

- 🛠 Panel administratora dla ulubionych zespołu (chroniony hasłem)

- 📋 Gotowe do skopiowania formuły z podświetlaniem składni

- ✏️ Edytowalne pole wyjściowe z cofaniem/ponawianiem zmian

- 📖 Wbudowana pomoc i dokumentacja funkcji (dla każdego języka)

- 💾 Automatyczny zapis (JSON, zapis atomowy)

- 🌙 Tryb ciemny

- 🔌 Menedżer wtyczek do tworzenia własnych wtyczek formuł

- 🔤 Obsługa RTL (od prawej do lewej) – automatyczne wykrywanie kierunku pisania

- 🗄️ Kopia zapasowa i przywracanie – zapisz wszystkie ustawienia i ulubione z nazwą i hasłem

- ⌨️ Globalny skrót klawiszowy `Ctrl+F12` do minimalizowania/przywracania okna
- 🔍 Walidator JSON – automatyczna weryfikacja i korekta `languages.json` i `formula_explanations.json`

## 🖥️ Użytkowanie

**1. Wprowadź dane**

- Zakres komórek (np. `A1:A10`)

- Komórka 1 / Komórka 2 (np. `A1`, `B1`)

- Opcjonalny parametr (np. tekst lub indeks)

- Wybór trybu odwołania bezwzględnego: `A1`, `$A1`, `A$1`, `$A$1`

**2. Wybierz funkcję** Wybierz zakładkę i kliknij funkcję – formuła zostanie natychmiast wygenerowana.

**3. Dostosuj formułę** Wygenerowana formuła może być edytowana bezpośrednio w polu wyjściowym.

**4. Kopiuj** Przenieś do schowka jednym kliknięciem (wraz z kolorami składni).

**5. Korzystaj z ulubionych**

- ⭐ Zapisz → zapisz bieżącą formułę (Ctrl+S)

- 📂 Wczytaj → użyj ponownie formuły

- ❌ Usuń → klawisz Delete lub przycisk

- 🕐 Historia → ostatnio używane formuły

## 📊 Przegląd zakładek

**Zakładka 1 – Funkcje podstawowe** `+` `-` `*` `/` `^` SUM, AVERAGE, MIN, MAX, MEDIAN, COUNT, COUNTA, SUMPRODUCT

**Zakładka 2 – Funkcje zaawansowane** IF, AND, OR, NOT SUMIF, COUNTIF, AVERAGEIF, SUMIFS, STDEV, VAR, COUNTBLANK, LARGE

**Zakładka 3 – Data i tekst** TODAY, NOW, YEAR, MONTH, DAY, DATE, DATEDIF, WEEKDAY CONCATENATE, LEN, LEFT, RIGHT, MID, UPPER, LOWER, TRIM

**Zakładka 4 – Wyszukiwanie i zaokrąglanie** VLOOKUP, HLOOKUP, INDEX, MATCH, INDEX+MATCH ROUND, ROUNDUP, ROUNDDOWN, INT, TRUNC, ABS, MOD, SQRT, RAND


## 📖 Objaśnienia formuł z dokumentacji LibreOffice

Plik `formula_explanations.json` jest wypełniany bezpośrednio z **oficjalnej dokumentacji LibreOffice Calc** (https://help.libreoffice.org).

### Źródło danych i aktualizacje

- Opisy, informacje o składni i przykłady są pobierane z oficjalnej strony pomocy LibreOffice
- Obsługiwane języki zależą od dostępnych tłumaczeń na stronie
- Plik zawiera dla każdej funkcji: nazwę, składnię, opis, przykład i kategorię
- Uzupełnienia lub korekty można wykonać ręcznie (patrz Walidator JSON)

### Struktura `formula_explanations.json`

```json
{
  "SUM": {
    "pl": {
      "syntax": "SUM(Liczba1; Liczba2; ...)",
      "description": "Sumuje wszystkie liczby w zakresie komórek.",
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

| Pole | Wymagane | Opis |
|------|---------|------|
| `syntax` | ✅ | Składnia formuły z parametrami |
| `description` | ✅ | Krótki opis funkcji |
| `example` | ✅ | Przykład użycia jako gotowa formuła |
| `note` | ❌ | Opcjonalna notatka |

> 💡 **Uwaga:** Jeśli nie istnieje wpis dla danego języka, aplikacja automatycznie wraca do wersji angielskiej.

---

## 🔍 Walidator JSON dla plików językowych

Zintegrowany **Walidator JSON** weryfikuje i koryguje `languages.json` i `formula_explanations.json` pod kątem spójności, kompletności i poprawnych nazw krajów. Dostępny przez **Ustawienia → 🔍 Walidator JSON**.

### Co jest weryfikowane?

#### `languages.json`

- ✅ Wszystkie 38 języków jest obecnych (wg kodu ISO 639-1)
- ✅ Poprawne **nazwy krajów i języków** (np. `"pl"` → `"Polski"`)
- ✅ Brak zduplikowanych kodów języków
- ✅ Wymagane pola są obecne: `name`, `native_name`, `flag`, `rtl`
- ✅ Flaga RTL ustawiona poprawnie (Arabski, Hebrajski, Perski, Urdu → `"rtl": true`)

#### `formula_explanations.json`

- ✅ Wszystkie funkcje z 4 zakładek są wpisane
- ✅ Wymagane pola są obecne: `syntax`, `description`, `example`
- ✅ Brak pustych pól (`""` lub `null`)
- ✅ Kody języków odpowiadają `languages.json`

### Funkcje korekty

| Typ błędu | Automatyczna korekta |
|----------|---------------------|
| Błędna nazwa kraju | Zastąpiona poprawną nazwą zgodnie z ISO |
| Brakujący wpis języka | Uzupełniony angielską wersją zapasową |
| Puste wymagane pole | Oznaczone jako `"[MISSING]"` do ręcznego przeglądu |
| Zduplikowany wpis | Duplikaty usunięte, zachowany bardziej kompletny |
| Błędna flaga RTL | Automatycznie skorygowana na podstawie znanych kodów RTL |

### Jak używać

1. Otwórz **Ustawienia → 🔍 Walidator JSON**
2. Wybierz plik: `languages.json` lub `formula_explanations.json` (lub oba)
3. **🔎 Weryfikuj** – wyświetla wszystkie znalezione problemy
4. **🛠 Automatyczna korekta** – rozwiązuje wszystkie automatycznie naprawialne błędy
5. **💾 Zapisz** – atomowo zapisuje skorygowany plik
6. **📋 Eksportuj raport** (opcjonalnie) – zapisuje plik tekstowy ze wszystkimi wynikami

> ⚠️ **Uwaga:** Przed każdą automatyczną korektą tworzona jest kopia zapasowa oryginalnego pliku (`languages.json.bak` / `formula_explanations.json.bak`).

## ⭐ System ulubionych

- Zapisywanie i ponowne używanie własnych formuł

- Rozróżnienie między własnymi ulubionymi a ulubionymi zespołu

- Ulubione zespołu są chronione przed zapisem (edycja tylko przez administratora)

- Zapobieganie duplikatom wpisów

- Dowolne sortowanie własnych ulubionych

- Synchronizacja przez dysk sieciowy (opcjonalnie konfigurowalna)

### Synchronizacja zespołowa

W **Ustawienia → 🌐 Ścieżka sieciowa** można podać dysk sieciowy (np. `\\\\Serwer\\Udostępnione\\formuly`).

- Przy uruchomieniu: ulubione sieciowe są zapisywane lokalnie (zapasowa kopia offline)

- Przy zapisie: własne formuły są zapisywane do sieci, formuły zespołu pozostają niezmienione

## 🛠 Panel administratora

Dostępny przez przycisk 🛠. Przy pierwszym kliknięciu ustawiane jest hasło (PBKDF2-SHA256, przechowywany jest tylko hash).

- Dodawanie, edytowanie i usuwanie formuł zespołu

- Zmiana hasła

- Zapisywanie zmian bezpośrednio na dysk sieciowy

## 🔌 Menedżer wtyczek

Menedżer wtyczek (`plugin_manager.py`) to samodzielne narzędzie do tworzenia i zarządzania własnymi wtyczkami formuł dla Calc2. Znajduje się w tym samym folderze co `Calc2.py` i jest uruchamiany przyciskiem 🔌 w Calc2.py:

### Funkcje

- **Utwórz nową wtyczkę** – kreator krok po kroku (nazwa, formuły, tłumaczenia, podsumowanie)

- **Dodaj formuły** – dodawanie formuł do istniejącej wtyczki

- **Edytuj tłumaczenia** – tłumaczenie nazw formuł na wszystkie 38 języków

- **Otwórz folder wtyczek** – bezpośrednio w eksploratorze plików

- **Usuń wtyczkę** – z potwierdzeniem bezpieczeństwa

### Struktura wtyczki

Każda wtyczka znajduje się jako podfolder w `plugins/` i składa się z dwóch plików:

```
plugins/
  moja_wtyczka/
    plugin.json      ← metadane (nazwa, wersja, autor, opis)
    formulas.json    ← formuły z tłumaczeniami
```

**Przykład `plugin.json`:**

```
{
  "id": "moja_wtyczka",
  "enabled": true,
  "version": "1.0",
  "author": "Twoje imię",
  "icon": "💰",
  "name": { "en": "Finance Formulas", "pl": "Formuły finansowe" },
  "description": { "en": "Useful formulas for financial calculations." }
}
```

**Przykład `formulas.json`:**

```
[
  {
    "formula": "=SUM(A1:A10)",
    "name": { "en": "Sum of range", "pl": "Suma zakresu" },
    "description": { "en": "Adds all values in A1:A10." },
    "category": { "en": "Basic", "pl": "Podstawowe" }
  }
]
```

### Ważna uwaga (⚠️ Important Notice)

W menedżerze wtyczek znajduje się przycisk **⚠️ Important Notice**. Kliknięcie otwiera okno ze wszystkimi zasadami prawidłowego tworzenia wtyczek w języku angielskim. Te same informacje znajdują się również w pliku `IMPORTANT_NOTICE.md`.

## 🌐 Wielojęzyczność

Dostępnych 38 języków, przełączanych bezpośrednio w aplikacji.  
Nowe języki można dodać przez przycisk 🌍 za pomocą Kreatora języków.

**Uwaga dotycząca hindi (हिंदी):** Przy pierwszym przełączeniu na hindi czcionka *Noto Sans Devanagari* zostanie jednorazowo zainstalowana w całym systemie. System Windows poprosi wtedy o uprawnienia administratora.

## 🔤 Obsługa RTL (od prawej do lewej)

Języki pisane od prawej do lewej są automatycznie wykrywane, a cały interfejs jest lustrzanie odbijany:

- **Arabski (عربي)** – automatyczne wykrywanie RTL
- **Hebrajski (עברית)** – automatyczne wykrywanie RTL
- **Perski / Farsi (فارسی)** – automatyczne wykrywanie RTL
- **Urdu (اردو)** – automatyczne wykrywanie RTL

**Co się zmienia w trybie RTL:** Cały układ UI jest lustrzanie odbijany, pola wprowadzania używają wyrównania RTL, czcionka automatycznie zmienia się na kompatybilną z RTL (np. *Noto Sans Arabic*, *Noto Sans Hebrew*).

> 💡 **Uwaga:** Wygenerowane formuły LibreOffice pozostają zawsze w składni LTR – zmienia się tylko kierunek interfejsu użytkownika.


## 🗄️ Kopia zapasowa i przywracanie

### Tworzenie kopii zapasowej

Przez **Ustawienia → 🗄️ Utwórz kopię zapasową**:

1. **Nazwa** – dowolna etykieta (np. `Kopia_Maj_2025`)
2. **Hasło** – kopia jest szyfrowana AES; bez hasła przywrócenie jest niemożliwe
3. **Miejsce zapisu** – lokalnie lub na dysku sieciowym
4. Kliknij **💾 Utwórz kopię zapasową** – zostaje utworzony plik `.calc2backup`

**Zawartość:** Wszystkie ulubione, ustawienia, ulubione zespołu (opcjonalnie), zainstalowane wtyczki.

### Przywracanie kopii zapasowej

Przez **Ustawienia → 📂 Przywróć kopię zapasową**:

1. Wybierz plik kopii zapasowej (`.calc2backup`)
2. Wprowadź hasło
3. Wybierz zakres: tylko ulubione / tylko ustawienia / wszystko
4. Kliknij **🔄 Przywróć**

> ⚠️ Podczas przywracania istniejące dane są nadpisywane. Przed przywróceniem oferowana jest automatyczna kopia bieżących danych.


## 💡 Wskazówki

- `$A$1` → odwołanie bezwzględne (lista rozwijana obok pól komórek)

- **Ctrl+S** → zapisz formułę do ulubionych

- **Ctrl+C** → kopiuj formułę (poza polami wprowadzania)

- **Ctrl+Z / Ctrl+Y** → cofnij / ponów

- **Ctrl+F12** → minimalizuj / przywróć okno (działa również gdy Calc2 jest zminimalizowany)

- **Klawisz Delete** na liście ulubionych → usuń wpis

- Formuły można dostosowywać bezpośrednio w polu wyjściowym po wygenerowaniu

## 📁 Struktura projektu

```
Calc2.py                        ← program główny
plugin_manager.py               ← menedżer wtyczek
IMPORTANT_NOTICE.md             ← uwagi dotyczące tworzenia wtyczek
data/
  README_de.md / README_en.md / ...      ← pomoc dla każdego języka
  REFERENZ_de.md / REFERENZ_en.md / ...  ← dokumentacja funkcji dla każdego języka
language/
  languages.json                ← tłumaczenia UI (38 języków)
  formula_explanations.json
services/
  language_tool.py              ← kreator: dodawanie nowego języka
  settings_service.py
  auth_service.py
  favorites_service.py
  network_sync.py
  install_service.py
  backup_service.py             ← kopia zapasowa i przywracanie
  json_validator.py             ← weryfikacja i korekta languages.json / formula_explanations.json
plugins/                        ← folder wtyczek (tworzony automatycznie)
  moja_wtyczka/
    plugin.json
    formulas.json
fonts/
  NotoSansDevanagari-Regular.ttf  ← czcionka hindi
  NotoSansArabic-Regular.ttf      ← czcionka arabska (RTL)
  NotoSansHebrew-Regular.ttf      ← czcionka hebrajska (RTL)
python/                         ← wbudowany Python
  python.exe
  ...
settings.json                   ← tworzony automatycznie
ulubione.json                   ← lokalne ulubione (tworzone automatycznie)
```

## 🧠 Najważniejsze cechy techniczne

- **Atomowy zapis plików** → zapobiega uszkodzeniu plików podczas zapisywania

- **Architektura usługowa** → logika i interfejs użytkownika są ściśle rozdzielone

- **Automatyczna migracja** → stare formaty ulubionych są rozpoznawane i konwertowane

- **Solidna obsługa błędów** → błędne pliki nie powodują awarii

- **Podświetlanie składni** → formuły są wyświetlane w kolorach

- **Tryb ciemny** → w pełni obsługiwany

- **System wtyczek** → Calc2 można rozszerzyć o własne wtyczki formuł

- **Silnik RTL** → automatyczne wykrywanie języków RTL, pełne lustrzane odbicie UI z odpowiednimi czcionkami

- **Kopia zapasowa i przywracanie** → kopie zapasowe szyfrowane AES z nazwą i hasłem, selektywne przywracanie

- **Walidator JSON** → automatyczna weryfikacja i korekta `languages.json` i `formula_explanations.json` włącznie z nazwami krajów i wymaganymi polami

- **Źródło LibreOffice** → `formula_explanations.json` jest wypełniany z oficjalnej dokumentacji LibreOffice Calc (https://help.libreoffice.org)

- **Globalny skrót klawiszowy** → `Ctrl+F12` działa w całym systemie przez bibliotekę `keyboard` (wątek w tle)

## Licencja

Wolne do użytku osobistego i komercyjnego.
