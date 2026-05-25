# LibreOffice Calc Formül Yardımcısı

LibreOffice Calc formüllerini hızlıca oluşturmak, test etmek ve yönetmek için bir Python aracı – favoriler sistemi, takım senkronizasyonu, çok dil desteği ve eklenti yöneticisi ile birlikte.

## 🚀 Özellikler

- 📑 60'tan fazla fonksiyonlu 4 sekme

- 🌐 38 dil (otomatik yazı tipi kurulumu ile Hintçe dahil)

- ⭐ Favoriler sistemi (yerel & ağ sürücüsü üzerinden takım senkronizasyonu)

- 🛠 Takım favorileri için yönetici paneli (şifre korumalı)

- 📋 Sözdizimi vurgulama ile doğrudan kopyalanabilir formüller

- ✏️ Geri al/Yinele destekli düzenlenebilir çıktı alanı

- 📖 Entegre yardım & fonksiyon referansı (her dil için)

- 💾 Otomatik kayıt (JSON, atomik yazım)

- 🌙 Karanlık mod

- 🔌 Kendi formül eklentilerini oluşturmak için Eklenti Yöneticisi

- 🔤 RTL desteği (sağdan sola) – yazı yönünün otomatik algılanması

- 🗄️ Yedekleme ve Geri Yükleme – tüm ayarları ve favorileri ad ve şifre ile kaydedin

- ⌨️ Küçültmek/Geri yüklemek için global kısayol `Ctrl+F12`
- 🔍 JSON Doğrulayıcı – `languages.json` ve `formula_explanations.json` otomatik denetim ve düzeltme

## 🖥️ Kullanım

**1. Giriş yapın**

- Hücre aralığı (ör. `A1:A10`)

- Hücre 1 / Hücre 2 (ör. `A1`, `B1`)

- İsteğe bağlı parametre (ör. metin veya indeks)

- Mutlak referans modu seçilebilir: `A1`, `$A1`, `A$1`, `$A$1`

**2. Fonksiyon seçin** Bir sekme seçin ve bir fonksiyona tıklayın – formül anında oluşturulur.

**3. Formülü özelleştirin** Oluşturulan formül, çıktı alanında doğrudan düzenlenebilir.

**4. Kopyalayın** Tek tıkla panoya alın (sözdizimi renkleri dahil).

**5. Favorileri kullanın**

- ⭐ Kaydet → mevcut formülü sakla (Ctrl+S)

- 📂 Yükle → formülü yeniden kullan

- ❌ Sil → Del tuşu veya buton

- 🕐 Geçmiş → son kullanılan formüller

## 📊 Sekme Özeti

**Sekme 1 – Temel Fonksiyonlar** `+` `-` `*` `/` `^` SUM, AVERAGE, MIN, MAX, MEDIAN, COUNT, COUNTA, SUMPRODUCT

**Sekme 2 – Gelişmiş Fonksiyonlar** IF, AND, OR, NOT SUMIF, COUNTIF, AVERAGEIF, SUMIFS, STDEV, VAR, COUNTBLANK, LARGE

**Sekme 3 – Tarih & Metin** TODAY, NOW, YEAR, MONTH, DAY, DATE, DATEDIF, WEEKDAY CONCATENATE, LEN, LEFT, RIGHT, MID, UPPER, LOWER, TRIM

**Sekme 4 – Arama & Yuvarlama** VLOOKUP, HLOOKUP, INDEX, MATCH, INDEX+MATCH ROUND, ROUNDUP, ROUNDDOWN, INT, TRUNC, ABS, MOD, SQRT, RAND


## 📖 LibreOffice Belgelerinden Formül Açıklamaları

`formula_explanations.json` dosyası doğrudan **LibreOffice Calc resmi belgeleri** (https://help.libreoffice.org) üzerinden doldurulmaktadır.

### Veri Kaynağı ve Güncelleme

- Açıklamalar, sözdizimi bilgileri ve örnekler LibreOffice'in resmi yardım sitesinden alınmaktadır
- Desteklenen diller sitedeki mevcut çevirilere bağlıdır
- Dosya her fonksiyon için içerir: ad, sözdizimi, açıklama, örnek ve kategori
- Eklemeler veya düzeltmeler manuel olarak yapılabilir (JSON Doğrulayıcı'ya bakın)

### `formula_explanations.json` Yapısı

```json
{
  "SUM": {
    "tr": {
      "syntax": "SUM(Sayı1; Sayı2; ...)",
      "description": "Bir hücre aralığındaki tüm sayıları toplar.",
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

| Alan | Zorunlu | Açıklama |
|------|---------|---------|
| `syntax` | ✅ | Parametreli formül sözdizimi |
| `description` | ✅ | Fonksiyonun kısa açıklaması |
| `example` | ✅ | Hazır formül olarak kullanım örneği |
| `note` | ❌ | İsteğe bağlı not |

> 💡 **Not:** Bir dil için giriş yoksa uygulama otomatik olarak İngilizce sürüme geri döner.

---

## 🔍 Dil Dosyaları için JSON Doğrulayıcı

Entegre **JSON Doğrulayıcı**, `languages.json` ve `formula_explanations.json` dosyalarını tutarlılık, tamlık ve doğru ülke isimleri açısından denetler ve düzeltir. **Ayarlar → 🔍 JSON Doğrulayıcı** üzerinden erişilebilir.

### Ne Denetlenir?

#### `languages.json`

- ✅ Tüm 38 dil mevcut (ISO 639-1 dil koduna göre)
- ✅ Doğru **ülke ve dil isimleri** (ör. `"tr"` → `"Türkçe"`)
- ✅ Yinelenen dil kodu yok
- ✅ Zorunlu alanlar mevcut: `name`, `native_name`, `flag`, `rtl`
- ✅ RTL bayrağı doğru ayarlı (Arapça, İbranice, Farsça, Urduca → `"rtl": true`)

#### `formula_explanations.json`

- ✅ 4 sekmedeki tüm fonksiyonlar kayıtlı
- ✅ Zorunlu alanlar mevcut: `syntax`, `description`, `example`
- ✅ Boş alan yok (`""` veya `null`)
- ✅ Dil kodları `languages.json` ile eşleşiyor

### Düzeltme İşlevleri

| Hata Türü | Otomatik Düzeltme |
|----------|------------------|
| Yanlış ülke adı | ISO standardına göre doğru isimle değiştirildi |
| Eksik dil girişi | İngilizce yedek sürümle dolduruldu |
| Boş zorunlu alan | Manuel inceleme için `"[MISSING]"` olarak işaretlendi |
| Yinelenen giriş | Kopyalar kaldırıldı, daha eksiksiz giriş tutuldu |
| Yanlış RTL bayrağı | Bilinen RTL kodlarına göre otomatik düzeltildi |

### Nasıl Kullanılır

1. **Ayarlar → 🔍 JSON Doğrulayıcı**'yı açın
2. Dosya seçin: `languages.json` veya `formula_explanations.json` (veya her ikisi)
3. **🔎 Denetle** – bulunan tüm sorunları gösterir
4. **🛠 Otomatik Düzelt** – otomatik çözülebilen tüm hataları düzeltir
5. **💾 Kaydet** – düzeltilmiş dosyayı atomik olarak yazar
6. **📋 Rapor Dışa Aktar** (isteğe bağlı) – tüm bulguları içeren bir metin dosyası kaydeder

> ⚠️ **Not:** Her otomatik düzeltme öncesinde orijinal dosyanın yedek kopyası oluşturulur (`languages.json.bak` / `formula_explanations.json.bak`).

## ⭐ Favoriler Sistemi

- Kendi formüllerinizi kaydedin ve yeniden kullanın

- Kişisel ve takım favorileri arasında ayrım

- Takım favorileri salt okunur (yalnızca yönetici düzenleyebilir)

- Yinelenen girişler engellenir

- Kişisel favorilerin sıralaması serbestçe değiştirilebilir

- Ağ sürücüsü üzerinden senkronizasyon (isteğe bağlı yapılandırılabilir)

### Takım Senkronizasyonu

**Ayarlar → 🌐 Ağ Yolu** üzerinden bir ağ sürücüsü girilebilir (ör. `\\\\Server\\Paylasim\\formuller`).

- Başlangıçta: Ağ favorileri yerel olarak kaydedilir (çevrimdışı yedek)

- Kaydederken: kişisel formüller ağa yazılır, takım formülleri değişmez

## 🛠 Yönetici Paneli

🛠 butonu ile erişilir. İlk tıklamada bir şifre belirlenir (PBKDF2-SHA256, yalnızca hash kaydedilir).

- Takım formülleri ekle, düzenle, sil

- Şifre değiştir

- Değişiklikleri doğrudan ağ sürücüsüne yaz

## 🔌 Eklenti Yöneticisi

Eklenti Yöneticisi (`plugin_manager.py`), Calc2 için kendi formül eklentilerinizi oluşturmak ve yönetmek için bağımsız bir araçtır. `Calc2.py` ile aynı klasörde bulunur ve Calc2.py içindeki 🔌 butonu ile başlatılır.

### Özellikler

- **Yeni eklenti oluştur** – Adım adım sihirbaz (ad, formüller, çeviriler, özet)

- **Formül ekle** – Mevcut bir eklentiye formül ekle

- **Çevirileri düzenle** – Formül adlarını 38 dile çevir

- **Eklenti klasörünü aç** – Doğrudan Dosya Gezgini'nde

- **Eklenti sil** – Onay sorusu dahil

### Eklenti Yapısı

Her eklenti `plugins/` altında bir alt klasör olarak bulunur ve iki dosyadan oluşur:

```
plugins/
  benim_eklentim/
    plugin.json      ← Meta veriler (ad, sürüm, yazar, açıklama)
    formulas.json    ← Çevirili formüller
```

**Örnek `plugin.json`:**

```json
{
  "id": "benim_eklentim",
  "enabled": true,
  "version": "1.0",
  "author": "Adınız",
  "icon": "💰",
  "name": { "en": "Finance Formulas", "tr": "Finans Formülleri" },
  "description": { "en": "Useful formulas for financial calculations." }
}
```

**Örnek `formulas.json`:**

```json
[
  {
    "formula": "=SUM(A1:A10)",
    "name": { "en": "Sum of range", "tr": "Aralık toplamı" },
    "description": { "en": "Adds all values in A1:A10." },
    "category": { "en": "Basic", "tr": "Temel" }
  }
]
```

### Önemli Uyarı (⚠️ Important Notice)

Eklenti Yöneticisi'nde **⚠️ Important Notice** butonu bulunur. Tıklandığında, doğru eklenti oluşturma kurallarını İngilizce olarak gösteren bir pencere açılır. Aynı bilgiler `IMPORTANT_NOTICE.md` dosyasında da yer alır.

## 🌐 Çok Dil Desteği

38 dil mevcut, uygulama içinde doğrudan değiştirilebilir.  
Yeni diller, 🌍 butonu ile Dil Sihirbazı aracılığıyla eklenebilir.

**Hintçe (हिंदी) notu:** Hintçe'ye ilk geçişte, *Noto Sans Devanagari* yazı tipi bir kez sistem genelinde kurulur. Windows bu işlem için yönetici hakları isteyebilir.

## 🔤 RTL Desteği (Sağdan Sola)

Sağdan sola yazılan diller otomatik olarak algılanır ve tüm arayüz yansıtılır:

- **Arapça (عربي)** – otomatik RTL algılama
- **İbranice (עברית)** – otomatik RTL algılama
- **Farsça / Farsi (فارسی)** – otomatik RTL algılama
- **Urduca (اردو)** – otomatik RTL algılama

**RTL modunda neler değişir:** Tüm UI düzeni yansıtılır, giriş alanları RTL hizalaması kullanır, yazı tipi otomatik olarak RTL uyumlu bir yazı tipine geçer (örn. *Noto Sans Arabic*, *Noto Sans Hebrew*).

> 💡 **Not:** Oluşturulan LibreOffice formülleri her zaman LTR sözdiziminde kalır – yalnızca kullanıcı arayüzü yön değiştirir.


## 🗄️ Yedekleme ve Geri Yükleme

### Yedek Oluşturma

**Ayarlar → 🗄️ Yedek Oluştur** üzerinden:

1. **Ad** – serbest etiket (örn. `Yedek_Mayis_2025`)
2. **Şifre** – yedek AES ile şifrelenir; şifre olmadan geri yükleme mümkün değildir
3. **Kayıt konumu** – yerel veya ağ sürücüsü
4. **💾 Yedek Oluştur** butonuna tıklayın – `.calc2backup` dosyası oluşturulur

**İçerik:** Tüm favoriler, ayarlar, takım favorileri (isteğe bağlı), yüklü eklentiler.

### Yedeği Geri Yükleme

**Ayarlar → 📂 Yedeği Geri Yükle** üzerinden:

1. Yedek dosyasını seçin (`.calc2backup`)
2. Şifreyi girin
3. Kapsam seçin: yalnızca favoriler / yalnızca ayarlar / her şey
4. **🔄 Geri Yükle** butonuna tıklayın

> ⚠️ Geri yükleme sırasında mevcut veriler üzerine yazılır. Geri yüklemeden önce mevcut verilerin otomatik yedeği önerilir.


## 💡 İpuçları

- `$A$1` → mutlak referans (hücre alanlarının yanındaki açılır menü)

- **Ctrl+S** → formülü favorilere kaydet

- **Ctrl+C** → formülü kopyala (giriş alanlarının dışında)

- **Ctrl+Z / Ctrl+Y** → Geri al / Yinele

- **Ctrl+F12** → pencereyi küçült / geri yükle (Calc2 küçültülmüşken de çalışır)

- **Del tuşu** favori listesinde → girişi sil

- Formüller oluşturulduktan sonra çıktı alanında doğrudan düzenlenebilir

## 📁 Proje Yapısı

```
Calc2.py                        ← Ana program
plugin_manager.py               ← Eklenti Yöneticisi
IMPORTANT_NOTICE.md             ← Eklenti oluşturma notları
data/
  README_tr.md / README_en.md / ...      ← Dile göre yardım
  REFERENZ_tr.md / REFERENZ_en.md / ...  ← Dile göre fonksiyon referansı
language/
  languages.json                ← UI çevirileri (38 dil)
  formula_explanations.json
services/
  language_tool.py              ← Sihirbaz: yeni dil ekle
  settings_service.py
  auth_service.py
  favorites_service.py
  network_sync.py
  install_service.py
  backup_service.py             ← yedekleme ve geri yükleme
  json_validator.py             ← languages.json / formula_explanations.json denetim ve düzeltme
plugins/                        ← Eklenti klasörü (otomatik oluşturulur)
  benim_eklentim/
    plugin.json
    formulas.json
fonts/
  NotoSansDevanagari-Regular.ttf  ← Hintçe yazı tipi
  NotoSansArabic-Regular.ttf      ← Arapça yazı tipi (RTL)
  NotoSansHebrew-Regular.ttf      ← İbranice yazı tipi (RTL)
python/                         ← gömülü Python
  python.exe
  ...
settings.json                   ← otomatik oluşturulur
favoriten.json                  ← yerel favoriler (otomatik oluşturulur)
```

## 🧠 Teknik Öne Çıkanlar

- **Atomik Dosya Yazımı** → kayıt sırasında bozuk dosyaları önler

- **Servis Mimarisi** → mantık ve arayüz tamamen ayrılmış

- **Otomatik Geçiş** → eski favori formatları tanınır ve dönüştürülür

- **Sağlam Hata Yönetimi** → hatalı dosyalar çökmeye neden olmaz

- **Sözdizimi Vurgulama** → formüller renkli gösterilir

- **Karanlık Mod** → tamamen destekleniyor

- **Eklenti Sistemi** → Calc2, kendi formül eklentileriyle genişletilebilir

- **RTL Motoru** → RTL dillerinin otomatik algılanması, uygun yazı tipleriyle tam UI yansıması

- **Yedekleme ve Geri Yükleme** → ad ve şifre ile AES şifreli yedekler, seçici geri yükleme

- **JSON Doğrulayıcı** → `languages.json` ve `formula_explanations.json` otomatik denetim ve düzeltme, ülke isimleri ve zorunlu alanlar dahil

- **LibreOffice Kaynağı** → `formula_explanations.json`, LibreOffice Calc resmi belgelerinden doldurulmaktadır (https://help.libreoffice.org)

- **Global Kısayol** → `Ctrl+F12`, `keyboard` kütüphanesi aracılığıyla sistem genelinde çalışır (arka plan iş parçacığı)

## Lisans

Kişisel ve ticari kullanım için serbestçe kullanılabilir.
