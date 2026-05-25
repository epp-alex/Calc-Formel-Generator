# Pembantu Formula LibreOffice Calc (LibreOffice Calc Formula Helper)

Sebuah alat berbasis Python untuk membuat, menguji, dan mengelola formula LibreOffice Calc dengan cepat – dilengkapi dengan sistem favorit, sinkronisasi tim, kemampuan multibahasa, dukungan RTL, pencadangan & pemulihan (Backup & Restore), serta manajer plugin.

## 🚀 Fitur

- 📑 4 tab dengan lebih dari 60 fungsi

- 🌐 38 bahasa (termasuk bahasa Hindi dengan instalasi font otomatis)

- 🔤 Dukungan RTL (Arab, Ibrani, dan banyak lagi) – deteksi otomatis arah penulisan

- ⭐ Sistem favorit (lokal & sinkronisasi tim melalui drive jaringan)

- 🛠 Panel admin untuk favorit tim (dilindungi kata sandi)

- 📋 Formula yang dapat langsung disalin dengan penyorotan sintaksis (Syntax Highlighting)

- ✏️ Kolom output yang dapat diedit dengan fitur Undo/Redo

- 📖 Bantuan terintegrasi & referensi fungsi (sesuai bahasa yang dipilih)

- 💾 Penyimpanan otomatis (JSON, ditulis secara atomik)

- 🌙 Mode Gelap (Dark Mode)

- 🔌 Manajer plugin untuk membuat plugin formula sendiri

- ⌨️ Hotkey global `Ctrl+F12` untuk meminimalkan/memulihkan jendela

- 🗄️ Pencadangan & Pemulihan (Backup & Restore) – mengamankan semua pengaturan dan favorit dengan nama dan kata sandi

- 🔍 Validator JSON – pemeriksaan dan koreksi file `languages.json` dan `formula\\\_explanations.json`

## 🖥️ Penggunaan

**1. Memasukkan Input**

- Rentang sel (misalnya `A1:A10`)

- Sel 1 / Sel 2 (misalnya `A1`, `B1`)

- Parameter opsional (misalnya teks atau indeks)

- Mode referensi absolut yang dapat dipilih: `A1`, `$A1`, `A$1`, `$A$1`

**2. Memilih Fungsi** Pilih salah satu tab dan klik sebuah fungsi – formula akan segera dibuat.

**3. Menyesuaikan Formula** Formula yang dihasilkan dapat langsung diedit di dalam kolom output.

**4. Menyalin** Salin ke papan klip (Clipboard) dengan satu klik (termasuk warna sintaksis).

**5. Menggunakan Favorit**

- ⭐ Simpan → mengamankan formula saat ini (Ctrl+S)

- 📂 Muat → menggunakan kembali formula

- ❌ Hapus → tombol Delete atau tombol hapus pada layar

- 🕐 Riwayat → menampilkan formula yang terakhir digunakan

## 📊 Ikhtisar Tab

**Tab 1 – Fungsi Dasar** `+` `-` `\\\*` `/` `^` SUM, AVERAGE, MIN, MAX, MEDIAN, COUNT, COUNTA, SUMPRODUCT

**Tab 2 – Fungsi Lanjutan** IF, AND, OR, NOT SUMIF, COUNTIF, AVERAGEIF, SUMIFS, STDEV, VAR, COUNTBLANK, LARGE

**Tab 3 – Tanggal & Teks** TODAY, NOW, YEAR, MONTH, DAY, DATE, DATEDIF, WEEKDAY CONCATENATE, LEN, LEFT, RIGHT, MID, UPPER, LOWER, TRIM

**Tab 4 – Pencarian & Pembulatan** VLOOKUP, HLOOKUP, INDEX, MATCH, INDEX+MATCH ROUND, ROUNDUP, ROUNDDOWN, INT, TRUNC, ABS, MOD, SQRT, RAND

## 📖 Penjelasan Formula dari Dokumentasi LibreOffice

File `formula\\\_explanations.json` diisi langsung dari **Dokumentasi Resmi Formula LibreOffice Calc** ([https://help.libreoffice.org](https://help.libreoffice.org/)).

### Sumber Data & Pembaruan

- Deskripsi, spesifikasi sintaksis, dan contoh diambil dari situs web bantuan resmi LibreOffice

- Bahasa yang didukung disesuaikan dengan terjemahan yang tersedia di situs web resmi tersebut

- File ini berisi data per fungsi: Nama, Sintaksis, Deskripsi, Contoh, dan Kategori

- Penambahan atau koreksi dapat dilakukan secara manual di dalam file tersebut (lihat Validator JSON)

### Struktur `formula\\\_explanations.json`

```
\{    
  "SUM": \{    
    "de": \{    
      "syntax": "SUMME(Zahl1; Zahl2; ...)",    
      "description": "Addiert alle Zahlen in einem Zellbereich.",    
      "example": "=SUMME(A1:A10)"    
    \},    
    "en": \{    
      "syntax": "SUM(Number1; Number2; ...)",    
      "description": "Adds all numbers in a cell range.",    
      "example": "=SUM(A1:A10)"    
    \}    
  \}    
\}
```

### Kolom yang Tersedia per Entri

| **Kolom** | **Wajib** | **Deskripsi** |
| - | - | - |
| `syntax` | ✅ | Sintaksis formula beserta parameternya |
| `description` | ✅ | Deskripsi singkat mengenai fungsi |
| `example` | ✅ | Contoh penerapan sebagai formula siap pakai |
| `note` | ❌ | Catatan opsional (misalnya hal khusus atau batasan fungsi) |

> 💡 **Catatan:** Jika suatu entri tidak tersedia dalam bahasa tertentu, aplikasi akan secara otomatis beralih kembali ke versi bahasa Inggris (Fallback).

## 🔍 Validator JSON untuk File Bahasa

**Validator JSON** yang terintegrasi pemeriksaan dan mengoreksi file `languages.json` serta `formula\\\_explanations.json` untuk memastikan konsistensi, kelengkapan, dan penamaan negara yang benar.

Dapat diakses melalui **Pengaturan (Settings) → 🔍 Validator JSON**.

### Apa Saju yang Diperiksa?

#### `languages.json`

- ✅ Semua 38 bahasa tersedia (berdasarkan kode bahasa ISO 639-1)

- ✅ Penamaan **negara dan bahasa** yang benar (misalnya `"de"` → `"Deutsch"`, bukan `"German"` atau `"Allemand"`)

- ✅ Tidak ada kode bahasa yang ganda

- ✅ Kolom wajib tersedia: `name`, `native\\\_name`, `flag`, `rtl`

- ✅ Penandaan RTL diatur dengan benar (Arab, Ibrani, Persia, Urdu → `"rtl": true`)

- ✅ Emoji bendera sesuai dengan kode negara

#### `formula\\\_explanations.json`

- ✅ Semua fungsi dari ke-4 tab telah terdaftar

- ✅ Kolom wajib tersedia: `syntax`, `description`, `example`

- ✅ Tidak ada kolom yang kosong (`""` atau `null`)

- ✅ Kode bahasa dalam entri cocok dengan yang ada di `languages.json`

- ✅ Tidak ada nama fungsi yang ganda

### Fungsi Koreksi

Validator dapat memperbaiki kesalahan yang ditemukan secara otomatis:

| **Jenis Kesalahan** | **Koreksi Otomatis** |
| - | - |
| Penamaan negara salah | Diganti dengan penamaan yang benar sesuai standar ISO |
| Entri bahasa hilang | Mengisi bahasa yang hilang dengan cadangan (Fallback) versi bahasa Inggris |
| Kolom wajib kosong | Menandai entri sebagai `"\\\[MISSING\\\]"` untuk pemeriksaan manual |
| Entri ganda | Menghapus duplikasi dan mempertahankan entri yang lebih lengkap |
| Bendera RTL salah atur | Mengoreksi secara otomatis berdasarkan kode bahasa RTL yang diketahui |

### Cara Pengoperasian

1. Buka **Pengaturan (Settings) → 🔍 Validator JSON**

2. Pilih file: `languages.json` atau `formula\\\_explanations.json` (atau keduanya sekaligus)

3. 🔎 **Periksa (Check)** – menampilkan semua masalah yang ditemukan dalam daftar yang jelas

4. 🛠 **Perbaiki Otomatis** – menyelesaikan semua kesalahan yang dapat diperbaiki secara otomatis

5. 💾 **Simpan** – menulis kembali file yang telah dikoreksi secara atomik

6. Opsional: 📋 **Ekspor Laporan** – menyimpan file teks berisi semua hasil temuan

> ⚠️ **Catatan:** Sebelum setiap koreksi otomatis dilakukan, salinan cadangan dari file asli akan selalu dibuat (`languages.json.bak` / `formula\\\_explanations.json.bak`).

### Penamaan Negara Diketahui – Tabel Koreksi (Pilihan)

| **Kode Bahasa** | **Salah (Contoh)** | **Benar** |
| - | - | - |
| `de` | German, Allemand, Deutsch\_DE | Deutsch |
| `en` | Englisch, Anglais | English |
| `fr` | French, Französisch | Français |
| `ar` | Arabic, Arabisch | العربية |
| `zh` | Chinese, Chinesisch | 中文 |
| `hi` | Hindi\_IN, Hindisch | hindi |
| `he` | Hebrew, Hebräisch | עبرית |
| `fa` | Farsi, Persian | فارسی |
| `ur` | Urdu\_PK, Urdisch | اردو |
| `tr` | Turkish, Türkisch\_TR | Türkçe |
| `pl` | Polish, Polnisch | Polski |
| `pt` | Portuguese, Portugiesisch | Português |
| `ru` | Russian, Russisch | Русский |
| `uk` | Ukranian, Ukrainisch | Українська |
| `ko` | Korean, Koreanisch | 한국어 |
| `ja` | Japanese, Japanisch | 日本語 |

> 💡 Validator memeriksa seluruh 38 bahasa yang didukung untuk memastikan penamaan asli yang benar (`native\\\_name`) sesuai dengan standar ISO.

## ⭐ Sistem Favorit

- Menyimpan dan menggunakan kembali formula milik sendiri

- Pemisahan yang jelas antara favorit pribadi dan favorit tim

- Favorit tim bersifat proteksi-tulis / read-only (hanya admin yang dapat mengedit)

- Mencegah adanya entri ganda

- Kebebasan pengurutan posisi pada favorit pribadi

- Sinkronisasi melalui drive jaringan (konfigurasi opsional)

### Sinkronisasi Tim

Melalui **Pengaturan (Settings) → 🌐 Jalur Jaringan (Network Path)**, sebuah drive jaringan dapat dimasukkan (misalnya `\\\\Server\\Freigabe\\formeln`).

- Saat Memulai: Favorit jaringan akan disimpan secara lokal (Cadangan Offline)

- Saat Menyimpan: Formula pribadi akan ditulis ke jaringan, sementara formula tim tetap tidak berubah

## 🗄️ Pencadangan & Pemulihan (Backup & Restore)

Sistem pencadangan yang terintegrasi memungkinkan pengamanan dan pemulihan data secara penuh – termasuk data favorit, pengaturan, dan konfigurasi tim.

### Membuat Cadangan (Backup)

Dapat diakses melalui **Pengaturan (Settings) → 🗄️ Buat Cadangan**:

1. Masukkan **Nama** – deskripsi bebas untuk penamaan file cadangan (misalnya `Backup\\\_Mei\\\_2025` atau `Sebelum\\\_Pembaruan`)

2. Tentukan **Kata Sandi** – file cadangan akan disimpan dengan enkripsi AES; pemulihan data tidak akan dapat dilakukan tanpa kata sandi ini

3. Pilih **Lokasi Penyimpanan** – lokal atau pada drive jaringan

4. Klik pada 💾 **Buat Cadangan** – menghasilkan file dengan ekstensi `.calc2backup`

**Konten di dalam Cadangan:**

- Semua favorit pribadi (`favoriten.json`)

- Semua pengaturan aplikasi (`settings.json`)

- Favorit tim opsional (jika jalur jaringan dikonfigurasi)

- Plugin yang terpasang (Metadata dan formula)

### Memulihkan Cadangan (Restore)

Dapat diakses melalui **Pengaturan (Settings) → 📂 Pulihkan Cadangan**:

1. Pilih **File Cadangan** (`.calc2backup`)

2. Masukkan **Kata Sandi** – harus cocok dengan kata sandi yang digunakan saat pembuatan cadangan

3. Pilih **Cakupan Pemulihan**:

   - Hanya Favorit

   - Hanya Pengaturan

   - Pulihkan Semua Data

4. Klik pada 🔄 **Pulihkan** – data akan diimpor, tidak memerlukan mulai ulang (Restart) aplikasi

> ⚠️ **Catatan:** Proses pemulihan data akan menimpa data yang ada saat ini. Pembuatan cadangan otomatis untuk data saat ini akan ditawarkan sebelum proses pemulihan berjalan.

### Lupa Kata Sandi

Cadangan yang dibuat tanpa kata sandi yang benar **not akan bisa** dipulihkan (tidak ada pintu belakang / backdoor). Simpan kata sandi Anda dengan aman, misalnya menggunakan manajer kata sandi (Password Manager).

## 🛠 Panel Admin

Dapat diakses melalui tombol 🛠. Pada klik pertama, sebuah kata sandi baru harus ditentukan (PBKDF2-SHA256, hanya nilai hash yang disimpan).

- Menambahkan, mengedit, dan menghapus formula tim

- Mengubah kata sandi

- Menulis perubahan secara langsung ke drive jaringan

## 🌐 Multibahasa & Dukungan RTL

### 38 Bahasa

Tersedia 38 bahasa yang dapat dialihkan secara langsung di dalam aplikasi.

Bahasa baru dapat ditambahkan melalui tombol 🌍 menggunakan Wizard Bahasa (Language Wizard).

**Catatan untuk Bahasa Hindi (**हिंदी**):** Saat pertama kali beralih ke bahasa Hindi, font *Noto Sans Devanagari* akan dipasang sekali secara sistemis. Windows akan meminta hak akses administrator untuk proses ini.

### 🔤 Dukungan RTL (Right-to-Left)

Bahasa dengan arah penulisan dari kanan ke kiri akan dideteksi secara otomatis dan seluruh tampilan antarmuka (UI) akan disesuaikan secara terbalik (spionase/mirroring):

- **Bahasa Arab (**عربي**)** – deteksi RTL otomatis

- **Bahasa Ibrani (**עברית**)** – deteksi RTL otomatis

- **Bahasa Persia / Farsi (**فارسی**)** – deteksi RTL otomatis

- **Bahasa Urdu (**اردو**)** – deteksi RTL otomatis

- Bahasa RTL lainnya akan dideteksi secara otomatis saat ditambahkan melalui Wizard Bahasa

**Apa saja yang berubah pada mode RTL:**

- Seluruh tata letak UI akan dibalik (Tombol, Tab, Kolom input)

- Kolom input teks menggunakan perataan arah kanan-ke-kiri

- Daftar favorit dan riwayat menjadi rata kanan

- Kolom output untuk formula tetap dalam mode LTR (karena teks formula LibreOffice harus selalu LTR)

- Font otomatis beralih ke jenis font yang kompatibel dengan RTL (misalnya *Noto Sans Arabic*, *Noto Sans Hebrew*)

> 💡 **Catatan:** Formula LibreOffice yang dihasilkan selalu menggunakan sintaksis LTR – hanya antarmuka pengguna (UI) saja yang berubah arah.

## 🔌 Manajer Plugin

Manajer plugin (`plugin\\\_manager.py`) adalah alat mandiri untuk membuat dan mengelola plugin formula Anda sendiri untuk Calc2. Alat ini berada di folder yang sama dengan `Calc2.py` dan dijalankan melalui tombol 🔌 di dalam aplikasi Calc2.py:

### Fitur

- **Membuat Plugin Baru** – Wizard langkah-demi-langkah (Nama, Formula, Terjemahan, Ringkasan)

- **Menambahkan Formula** – Melengkapi formula ke dalam plugin yang sudah ada

- **Mengedit Terjemahan** – Menerjemahkan penamaan formula ke dalam seluruh 38 bahasa

- **Membuka Folder Plugin** – Membuka direktori secara langsung di File Explorer

- **Menghapus Plugin** – Disertai dengan pertanyaan konfirmasi keamanan

### Struktur Plugin

Setiap plugin berada sebagai subfolder di dalam direktori `plugins/` dan terdiri dari dua file:

```
`plugins/  `

`  mein\_plugin/  `

`    plugin.json      ← Metadata (Nama, Versi, Penulis, Deskripsi)  `

`    formulas.json    ← Formula beserta terjemahannya`
```

**Contoh `plugin.json`:**

JSON

```
`\{  `

`  "id": "mein\_plugin",  `

`  "enabled": true,  `

`  "version": "1.0",  `

`  "author": "Nama Anda",  `

`  "icon": "💰",  `

`  "name": \{ "en": "Finance Formulas", "de": "Finanz-Formeln" \},  `

`  "description": \{ "en": "Useful formulas for financial calculations." \}  `

`\}`
```

**Contoh `formulas.json`:**

JSON

```
`\[  `

`  \{  `

`    "formula": "=SUM(A1:A10)",  `

`    "name": \{ "en": "Sum of range", "de": "Summe des Bereichs" \},  `

`    "description": \{ "en": "Adds all values in A1:A10." \},  `

`    "category": \{ "en": "Basic", "de": "Grundlagen" \}  `

`  \}  `

`\]`
```

### Pemberitahuan Penting (⚠️ Important Notice)

Di dalam Manajer Plugin terdapat tombol ⚠️ **Important Notice**. Mengkliknya akan membuka jendela berisi semua aturan untuk pembuatan plugin yang benar dalam bahasa Englisch. Informasi yang sama juga tersedia di dalam file `IMPORTANT\\\_NOTICE.md`.

## 💡 Tips

- `$A$1` → Referenz absolut (Menu dropdown di samping kolom sel)

- **Strg+S** → Menyimpan formula saat ini ke dalam Favorit

- **Strg+C** → Menyalin formula (saat berada di luar kolom input)

- **Strg+Z / Strg+Y** → Undo / Redo

- **Strg+F12** → Meminimalkan / memulihkan jendela (tetap berfungsi meskipun Calc2 sedang diminimalkan ke latar belakang)

- **Tombol Delete** pada daftar favorit → Menghapus entri terpilih

- Formula dapat disesuaikan langsung di kolom output setelah dihasilkan

- Untuk bahasa RTL: Output formula akan selalu tetap LTR – hanya UI saja yang dicerminkan

## 📁 Struktur Proyek

```
`Calc2.py                        ← Program Utama  `

`plugin\\\_manager.py               ← Manajer Plugin  `

`IMPORTANT\\\_NOTICE.md             ← Petunjuk pembuatan plugin  `

`data/  `

`  README\\\_de.md / README\\\_en.md / ...      ← Bantuan per bahasa  `

`  REFERENZ\\\_de.md / REFERENZ\\\_en.md / ...  ← Referensi fungsi per bahasa  `

`language/  `

`  languages.json                ← Terjemahan UI (36 bahasa)  `

`  formula\\\_explanations.json     ← Penjelasan formula (dari situs web LibreOffice)  `

`services/  `

`  language\\\_tool.py              ← Wizard: menambahkan bahasa baru  `

`  settings\\\_service.py  `

`  auth\\\_service.py  `

`  favorites\\\_service.py  `

`  network\\\_sync.py  `

`  install\\\_service.py  `

`  backup\\\_service.py             ← Pencadangan & Pemulihan  `

`  json\\\_validator.py             ← Pemeriksaan & koreksi languages.json / formula\\\_explanations.json  `

`plugins/                        ← Folder Plugin (dibuat otomatis)  `

`  mein\\\_plugin/  `

`    plugin.json  `

`    formulas.json  `

`fonts/  `

`  NotoSansDevanagari-Regular.ttf  ← Font bahasa Hindi  `

`  NotoSansArabic-Regular.ttf      ← Font bahasa Arab (RTL)  `

`  NotoSansHebrew-Regular.ttf      ← Font bahasa Ibrani (RTL)  `

`python/                         ← Python bawaan (Embedded)  `

`  python.exe  `

`  ...  `

`settings.json                   ← Dibuat secara otomatis  `

`favoriten.json                  ← Favorit lokal (dibuat otomatis)`
```

## 🧠 Sorotan Teknis (Technical Highlights)

- **Atomic File Writes** → Mencegah file rusak atau korup saat proses penyimpanan data

- **Arsitektur Layanan (Service Architecture)** → Pemisahan ketat antara Logika Bisnis dan Antarmuka Pengguna (UI)

- **Migrasi Otomatis** → Format favorit versi lama akan dideteksi dan dikonversi secara otomatis

- **Penanganan Kesalahan yang Kuat** → File yang rusak tidak akan menyebabkan aplikasi mogok (Crash)

- **Penyorotan Sintaksis (Syntax Highlighting)** → Formula ditampilkan secara berwarna untuk kejelasan

- **Mode Gelap (Dark Mode)** → Didukung sepenuhnya di seluruh antarmuka

- **Sistem Plugin** → Calc2 dapat diperluas kemampuannya menggunakan plugin formula buatan sendiri

- **Hotkey Global** → Shortcut `Strg+F12` berfungsi di seluruh sistem menggunakan pustaka `keyboard` (Thread Latar Belakang)

- **Mesin RTL (RTL Engine)** → Deteksi otomatis bahasa RTL, pembalikan UI penuh termasuk penyesuaian font yang cocok

- **Pencadangan & Pemulihan** → File cadangan terenkripsi AES dengan nama dan kata sandi, opsi pemulihan selektif tersedia

- **Validator JSON** → Pemeriksaan dan koreksi otomatis untuk `languages.json` dan `formula\\\_explanations.json` termasuk penamaan negara dan kolom wajib

- **Sumber Data LibreOffice** → `formula\\\_explanations.json` diisi langsung dari dokumentasi resmi LibreOffice Calc ([https://help.libreoffice.org](https://help.libreoffice.org/))

## Lisensi

Bebas digunakan untuk keperluan pribadi maupun komersial.

