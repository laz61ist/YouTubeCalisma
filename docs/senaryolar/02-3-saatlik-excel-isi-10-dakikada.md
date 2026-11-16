# Senaryo 02 — 3 Saatlik Excel İşini 10 Dakikada Bitirmek

Kategori: G (görev çözümleri) · Hedef süre: 10,5–12 dk · Seslendirme: yaklaşık 1.330 kelime (yer tutucular hariç; dolunca tahmini 1.450) · Format: ekran kaydı + seslendirme, yüz yok · Kurgu: kronometre yarışı (elle yol ↔ yapay zekâlı yol)

> **Başlıktaki rakamlar ölçülmeden yayınlanmaz.** "3 saat" ve "10 dakika" çalışma başlığıdır. Elle süre ve yapay zekâlı süre çekimde gerçekten ölçülür (bkz. bölüm 2.3); başlık, kapak ve seslendirme ölçülen değere göre düzeltilir. Ölçüm "1 sa 40 dk → 22 dk" çıkarsa başlık da budur.

---

## 1. Paket

### Başlık seçenekleri

| # | Başlık | Ne zaman kullanılır |
|---|---|---|
| A | [ELLE SÜRE]'lik Excel İşini [YZ SÜRE]'de Bitirmek (çalışma hâli: "3 Saatlik Excel İşini 10 Dakikada Bitirmek") | Yalnızca süresiz kapakla ("DAĞINIK → ÖZET") birlikte; başlık/kapak testinin ikinci paketi. Rakamlar ölçümle birebir aynı olmalı; yuvarlama gerçeğe doğru yapılır (17 dk "10 dk" olmaz, "17 dk" ya da "20 dk'dan kısa" olur). Elle süre yapay zekâlı sürenin 3 katından azsa bu başlık hiç kullanılmaz (aşağıdaki eşik kuralı). |
| B | Dağınık Satış Dökümünden Yönetici Özetine: Kronometreyle Denedim | Varsayılan. Aşağıdaki kapak süre çiftini taşıdığı için başlık görevi söyler; süre iki yerde tekrar edilmez (`docs/01-icerik-uretim-sistemi.md`, 2.1 adım 6). |
| C | Excel'de Veri Temizleme ve Tablo Birleştirme: Dosyayı Yapay Zekâya Yüklemeden | Arama trafiği için ("excel veri temizleme", "düşeyara çalışmıyor", "iki tabloyu birleştirme"). Yayından birkaç hafta sonra trafik kaynağı aramaya kayıyorsa denenir. |

### Eşik kuralı: süre farkı küçük çıkarsa

Bu dosya 650 satır civarında; Excel'i iyi kullanan biri için elle sürenin 3 saate yaklaşması beklenmez (tahmini 30–60 dk; ölçülmeden bilinmez). Karar çekimden sonra, seslendirmeden önce verilir. Oran = `[ELLE SÜRE]` ÷ `[YZ SÜRE]`.

| Ölçülen oran | Kapak | Başlık | Hook ve sonuç bölümü |
|---|---|---|---|
| 3 kat ya da fazla | Süre çifti büyük | B; A test paketinde kullanılabilir | Hook süre farkıyla açılır (aşağıdaki metin) |
| 2 kat ile 3 kat arası | Süre çifti büyük | B; A kullanılmaz | Aynı |
| 2 katın altında | Süre çifti yok; "DAĞINIK → ÖZET" + etiket "DOSYAYI YÜKLEMEDEN" | B | Hook'ta iki süre yine söylenir ama cümle tuzağa geçer; sonuç bölümünde "süre farkı küçük; asıl kazanç şurada/yok" açıkça söylenir |
| Yapay zekâlı süre eşit ya da daha uzun | Aynı | B | Sonuç bölümünde "bu işte süre kazanmadım" denir; video yine yayınlanır |

Rakamlar her durumda videoda ve açıklamada yazar; küçük fark gizlenmez.

### Kapak tarifi

- Zemin koyu lacivert, vurgu sarı, yüz yok.
- Sabit kalıp büyük puntoyla: `[ELLE SÜRE] → [YZ SÜRE]` (biçim örneği "3 sa → 12 dk"; rakamlar ölçülenle değiştirilir).
- Sol yarıda soluk, eğik bir Excel ekran parçası: karışık tarihler ve "1.014,00 TL" yazan hücreler sarı çerçeveli. Sağ yarıda temiz, küçük bir özet tablo.
- Etiket: "DOSYAYI YÜKLEMEDEN". Süre çifti dışında en fazla 2 kelimelik tek etiket; sağ alt köşe boş kalır (YouTube'un süre damgası oraya biner).
- Telefon boyutuna küçültüp bak: süre kalıbı okunuyor, Excel parçası "dağınık tablo" olarak anlaşılıyor mu.

### Tek cümlelik vaat

Dağınık bir satış dökümünü, dosyanın kendisini yapay zekâya yüklemeden temizleyip ürün tablosuyla birleştiriyor, ekim özetini ve yöneticiye gidecek 3 maddelik yorumu çıkarıyorum; elle süreyle arasındaki farkı kronometreyle, veriye bilerek koyduğum tuzağın yakalanıp yakalanmadığını da kontrol adımıyla gösteriyorum.

### Bu videonun (21) "Excel Formülünü Yapay Zekâya Yazdırmak" videosundan farkı

Bu video uçtan uca bir iş akışı: temizlik → birleştirme → özet → yorum → kontrol. Tek tek formül türlerine (iç içe EĞER, metin ayırma, tarih hesapları) girilmez; o konu 21'e bırakılır ve açıklamada oraya bağlantı verilir (yayınlandığında).

---

## 2. Çekim öncesi hazırlık (bunlar olmadan senaryo okunamaz)

### 2.1 Vaka

Kurgusal bir ofis malzemeleri toptancısı (Senaryo 01'deki firma; isim verilmez). Elindeki döküm 28 Eylül – 3 Kasım 2026 arasını kapsıyor (ay sonu dökümü komşu günleri de içeriyor). Görev: dökümü temizle, ürün tablosundan kategori bilgisini getir, **yalnızca Ekim 2026** için Kategori × Şehir özet tablosu çıkar, genel müdür için 3 maddelik yorum yaz.

### 2.2 Örnek veri seti

İki dosya hazırlanır: `cevap-anahtari.xlsx` (temiz veri + beklenen sonuçlar) ve ondan türetilen `satis-dokumu-ORNEK.xlsx` (kirli dosya; videoda görünen). Gerçek şirket, müşteri ya da kişi adı yok; fiyatlar kurgusaldır, gerçek piyasa fiyatı iddiası taşımaz.

#### Yapı

**Sayfa "Satis"** — kirli dosyada 1–2. satırlar birleştirilmiş hücreli başlık bloğu, 3. satır sütun başlıkları, veri 4. satırdan başlar. Başlık bloğu kayıtta silinir; ondan sonra başlıklar 1. satırda, veri 2. satırdadır. Senaryodaki bütün satır numaraları blok silindikten sonraki hâle göredir.

| Sütun | Başlık | İçerik | Örnek |
|---|---|---|---|
| A | Sipariş No | `S-` + 5 hane; web siparişlerinde `WEB-` + 5 hane | S-10482, WEB-20031 |
| B | Tarih | 28.09.2026 – 03.11.2026 | (kirli, aşağıya bak) |
| C | Müşteri Kodu | `M-` + 3 hane (60 kurgusal müşteri) | M-017 |
| D | Ürün Kodu | Urunler sayfasındaki kodlar | KG-104 |
| E | Adet | Tam sayı, temiz | 12 |
| F | Birim Fiyat | İki ondalıklı sayı, temiz | 84,50 |
| G | Tutar | Adet × Birim Fiyat (birebir) | (kirli) |
| H | Şehir | 5 şehir: İstanbul, Ankara, İzmir, Bursa, Antalya | (kirli) |
| I | Satış Temsilcisi | 6 kurgusal etiket: "Temsilci A" … "Temsilci F" | |

Satırlar tarihe göre sıralıdır (ara toplam satırlarının anlamlı olması için).

**Sayfa "Urunler"** — kirli dosyada 37 ürün (anahtarda 40), temiz.

| Sütun | Başlık | Örnek |
|---|---|---|
| A | Ürün Kodu | KG-104 |
| B | Ürün Adı | A4 Fotokopi Kâğıdı 500'lü |
| C | Kategori | Kâğıt Ürünleri |

Kod ön eklerinde i/ı harfi kullanma (Türkçe büyük-küçük harf dönüşümü ayrı bir sorun; bu videonun konusu değil).

#### Temiz verinin üretimi (`cevap-anahtari.xlsx`)

Hedef: **620 satır** = 10 satır 28–30 Eylül + **600 satır Ekim** + 10 satır 1–3 Kasım.

Parametreler (hepsi hedef değerdir; gerçekleşen paylar üretimden sonra anahtardan okunur):

| Kategori | Ön ek | Ürün sayısı | Birim fiyat aralığı (kurgusal TL) | Adet aralığı | Satır payı hedefi |
|---|---|---|---|---|---|
| Kâğıt Ürünleri | KG- | 8 | 60–450 | 5–40 | %30 |
| Yazı Gereçleri | YZ- | 8 | 15–180 | 5–40 | %20 |
| Dosyalama | DS- | 6 | 25–220 | 5–40 | %14 |
| Toner ve Kartuş | TN- | 6 | 350–2.400 | 1–8 | %14 |
| Temizlik | TM- | 6 | 30–380 | 1–30 | %12 |
| Masaüstü | MS- | 6 | 40–600 | 1–30 | %10 |

| Şehir | Müşteri sayısı (60 içinde) | Satır payı hedefi |
|---|---|---|
| İstanbul | 21 | %35 |
| Ankara | 15 | %25 |
| İzmir | 12 | %20 |
| Bursa | 7 | %12 |
| Antalya | 5 | %8 |

Üretim adımları (Türkçe Excel; `[ÇEKİMDE DOĞRULA]` yerine burada "hazırlıkta dene" geçerli, çünkü bu dosya kayıttan önce biter):

1. **Yardımcı sayfalar.** "Urunler": Kod · Ad · Kategori · Birim Fiyat (ürün başına sabit, iki ondalıklı) · En Az Adet · En Çok Adet. "Musteriler": Kod (M-001…M-060) · Şehir (yukarıdaki sayılarla) · Temsilci. "Agirlik": A sütununda 0'dan başlayan kümülatif alt sınır, B sütununda ürün kodu (her ürünün ağırlığı = kategorinin satır payı ÷ kategorideki ürün sayısı).
2. **"Uretim" sayfası, 2–621. satırlar.** Q sütunu "önceki satırla aynı sipariş mi": Q2'ye `YANLIŞ`, Q3'ten aşağıya `=S_SAYI_ÜRET()<0,3`.

```
B2 (Tarih):    =EĞER(Q2;B1;RASTGELEARADA(TARİH(2026;10;1);TARİH(2026;10;31)))
C2 (Müşteri):  =EĞER(Q2;C1;"M-"&METNEÇEVİR(RASTGELEARADA(1;60);"000"))
D2 (Ürün):     =DÜŞEYARA(S_SAYI_ÜRET();Agirlik!A:B;2;DOĞRU)
E2 (Adet):     =RASTGELEARADA(DÜŞEYARA(D2;Urunler!A:F;5;YANLIŞ);DÜŞEYARA(D2;Urunler!A:F;6;YANLIŞ))
F2 (Fiyat):    =DÜŞEYARA(D2;Urunler!A:F;4;YANLIŞ)
G2 (Tutar):    =YUVARLA(E2*F2;2)
H2 (Şehir):    =DÜŞEYARA(C2;Musteriler!A:C;2;YANLIŞ)
I2 (Temsilci): =DÜŞEYARA(C2;Musteriler!A:C;3;YANLIŞ)
```

3. Hepsini **değer olarak yapıştır** (rastgele formüller her hesaplamada değişir). Tarih, sonra müşteri koduna göre sırala.
4. **Sipariş No.** A2'ye `S-10001`; A3'ten aşağıya `=EĞER(VE(B3=B2;C3=C2);A2;"S-"&(SAĞDAN(A2;5)+1))`; sonra değer olarak yapıştır. Aynı gün aynı müşterinin satırları tek sipariş olur.
5. **Eylül ve Kasım satırları.** Tek satırlı siparişlerden 10'unun tarihini 28–30 Eylül, 10'unun tarihini 1–3 Kasım yap; yeniden sırala.
6. **WEB siparişleri.** Ekim içinden, tam siparişler hâlinde toplam **40 satır** seç; Sipariş No'yu `WEB-2xxxx` yap. 20 satırın günü 01–12 arasında (10 hariç), 20 satırın günü 13–31 arasında olmalı; tutmuyorsa seçimi değiştir. Gün 10 kullanılmaz: 10/10/2026 iki okunuşta da aynı tarihtir, tuzağa girmez.
7. **Listede olmayan 3 ürün.** Üç ayrı kategoriden birer ürün seç (ör. bir KG, bir DS, bir TM). Bu üç ürünün satır sayısı toplam **7** kalana kadar fazla satırların ürün kodunu aynı kategoriden başka bir ürünle değiştir (fiyat ve tutar güncellenir). 7 satırın hepsi ekimde olsun, WEB olmasın.
8. **Üç bulgu** (yorum maddeleri bunlara dayanacak). Ürün kodu değiştirerek ayarla; her değişiklikte fiyat ve tutar güncellenir:
   - (a) **Kâğıt Ürünleri** ekim cirosunun en büyük parçası; hedef yaklaşık %35–40. Tutmuyorsa satır payını değiştirip yeniden üret.
   - (b) **Toner ve Kartuş** genelde ikinci sırada, ama **Ankara**'da zayıf: Ankara'nın toner tutarının Ankara toplamındaki payı, diğer dört şehirdeki toner payının üçte birinin altında olsun. Ankara'daki toner satırlarının çoğunu başka kategorilerden ürünlerle değiştir.
   - (c) **Antalya** (en küçük şehir), **Temizlik** kategorisinde **Bursa**'yı geçsin; hedef en az %15 fark (tabloda gözle görülsün). Antalya satırlarının bir kısmını temizlik ürünleriyle değiştir.
9. **Doğal yinelenen kontrolü.** R sütununa `=A2&"|"&D2&"|"&E2`, S sütununa `=EĞERSAY(R:R;R2)>1`. `DOĞRU` çıkan satır varsa ürününü değiştir; hiç `DOĞRU` kalmamalı. (Aynı siparişte aynı ürün aynı adetle iki kez geçerse kayıtta "12 yinelenen" sayısı tutmaz.)
10. **Anahtar değerleri.** Ayrı bir "Anahtar" sayfasına yaz: 620 satırın toplamı · ekim toplamı (600 satır) · yedi dönemin ara toplamları (aşağıdaki tablo) · ekim için Kategori × Şehir tablosu, iki hâliyle: "tam" (40 ürünle) ve "beklenen çıktı" (7 satır `EŞLEŞMEDİ` satırında) · WEB satırlarının toplam tutarı · üç bulgunun sayıları. Senaryoda `[ANAHTAR]` yazan her yer buradan okunur.

#### Kirletme (`satis-dokumu-ORNEK.xlsx`) — sıra önemlidir

Temiz verinin kopyası üzerinde, **bu sırayla**:

| Sıra | Kirli veri türü | Miktar | Nasıl hazırlanır |
|---|---|---|---|
| 1 | Karışık tarih biçimi | yaklaşık 150 satır metin | WEB olmayan satırlardan yaklaşık 75'i metin `03.10.2026`, yaklaşık 75'i metin `2026-10-03`; kalanı gerçek tarih olarak kalır. Metni yardımcı sütunda `=METNEÇEVİR(B2;"gg.aa.yyyy")` ve `=METNEÇEVİR(B2;"yyyy-aa-gg")` ile üret, "Metin" biçimli hücreye **değer olarak** yapıştır |
| 2 | **Tuzak: ay/gün/yıl tarihler** | 40 satır (WEB siparişlerinin tamamı) | Metin olarak `10/03/2026` (= 3 Ekim) ve `10/17/2026` (= 17 Ekim); `=METNEÇEVİR(B2;"aa/gg/yyyy")`, "Metin" biçimli hücreye değer olarak yapıştır. Ay ve gün iki haneli, başta ve sonda boşluk yok |
| 3 | Ürün kodunda baş/son boşluk | yaklaşık 60 satır | `" KG-104"`, `"KG-104 "` |
| 4 | Metin olarak tutar | yaklaşık 200 satır | `=METNEÇEVİR(G2;"#.##0,00")&" TL"` → `1.014,00 TL`; "Metin" biçimli hücreye değer olarak yapıştır. Kalanı gerçek sayı |
| 5 | Tutarsız şehir yazımı | yaklaşık 180 satır | Aşağıdaki yazım listesi |
| 6 | Ürün tablosunda olmayan kod | 3 kod, 7 satır | Kirli dosyanın Urunler sayfasından üretimin 7. adımındaki 3 ürünü sil; Satis'te kalsınlar |
| 7 | Birebir yinelenen satırlar | 12 satır | **1–6 bittikten sonra**, kirletilmiş hâlinden 12 satırı kopyala; araya satır ekleyip biçimiyle birlikte yapıştır (kopya ile aslı hücre hücre aynı olmalı). WEB ve listede olmayan kodlu satırlardan seçme |
| 8 | Ara toplam satırları | 7 satır | Her dönemin son satırının altına: A sütununa etiket, G sütununa **sayı** olarak anahtardaki dönem toplamı (aşağıdaki tablo) |
| 9 | Araya girmiş boş satırlar | 10 satır | Rastgele yerlere; ilk 5 veri satırının arasına ve art arda koyma |
| 10 | Başlık bloğu | 2 satır | En üste iki satır ekle. 1. satır A:I birleştirilmiş: "SATIŞ DÖKÜMÜ". 2. satır A:I birleştirilmiş: "Dönem: 28.09.2026 – 03.11.2026" |

Ara toplam satırları (dökümü veren sistemin kendi hesabı gibi düşünülür):

| A sütunundaki etiket | Kapsadığı satırlar |
|---|---|
| `ARA TOPLAM 28.09-30.09` | Eylül satırları |
| `ARA TOPLAM 01.10-04.10` | Ekim, 1. dönem |
| `ARA TOPLAM 05.10-11.10` | Ekim, 2. dönem |
| `ARA TOPLAM 12.10-18.10` | Ekim, 3. dönem |
| `ARA TOPLAM 19.10-25.10` | Ekim, 4. dönem |
| `ARA TOPLAM 26.10-31.10` | Ekim, 5. dönem |
| `ARA TOPLAM 01.11-03.11` | Kasım satırları |

Her ara toplam, **temiz verideki** o döneme ait bütün satırların tutarıdır: WEB siparişleri ve listede olmayan kodlu 7 satır dahil, sonradan eklenen 12 yinelenen satır hariç. Yedisinin toplamı 620 satırın toplamına, ortadaki beşinin toplamı ekim toplamına eşittir. Videoda bu satırlar silinmeden önce kenara alınır ve tarihten bağımsız kontrol kaynağı olarak kullanılır.

Şehir yazımları (17 ham yazım):

| Doğrusu | Dosyadaki yazımlar |
|---|---|
| İstanbul | İstanbul · istanbul · Istanbul · İST. · "İstanbul " (sonda boşluk) |
| Ankara | Ankara · ANKARA · ankara · Ank. |
| İzmir | İzmir · izmir · Izmir |
| Bursa | Bursa · BURSA · "Bursa " (sonda boşluk) |
| Antalya | Antalya · antalya |

`BENZERSİZ` ve `ÇAPRAZARA` büyük-küçük harfi ayırmaz; bu yüzden ekrandaki benzersiz liste 17'den kısa çıkar ("Ankara / ANKARA / ankara" tek satır olur). Türkçe i/İ/ı/I çiftlerinin ("istanbul / İstanbul / Istanbul") kaç satıra indiğini bilmiyorum; hazırlıkta dene ve çıkan sayıyı not et `[ÇEKİMDE DOĞRULA: benzersiz listede kaç satır var; hangi yazımlar birleşti]`. Seslendirmedeki ilgili cümle bu sonuca göre yazılır.

İlk 5 veri satırı (yapay zekâya örnek olarak gidecek; 28 Eylül satırları) şunları **içermeli**: en az bir metin tarih, en az bir gerçek tarih, en az bir metin tutar, en az bir boşluklu ürün kodu, en az iki farklı şehir yazımı. Şunları **içermemeli**: WEB siparişi, boş satır, ara toplam satırı, yinelenen satır.

Satır hesabı: 620 + 12 yinelenen + 7 ara toplam + 10 boş = **649 veri satırı** (başlık bloğu silindikten sonra 2–650. satırlar) → 17 satır silinince 632 (2–633) → yinelenenler kalkınca **620** (2–621); bunların **600**'ü ekim.

Senaryo 01'in sonunda verilen söz ("boş satırlar, metin olarak girilmiş tutarlar, üç ayrı biçimde yazılmış tarihler") yukarıdaki 1, 4 ve 9 numaralı kirli veri türleriyle karşılanır; Senaryo 01'in kapanış görüntüsü bu dosyadan alınır.

### 2.3 Ölçümler

1. **Elle yöntem ölçümden önce yazılı olarak sabitlenir.** Tanım: "Yapay zekâ kullanmaya başlamadan önce bu işi gerçekten nasıl yapıyorsam öyle." Filtre biliyorsan filtre, PivotTable biliyorsan PivotTable kullanılır; süre uzasın diye yavaş yöntem seçilmez. Kayıttan önce yöntemi dört satırda yaz (silme · temizlik · birleştirme · özet ve yorum) `[ÇEKİMDEN ÖNCE YAZ]`; kayıtta bu listeden sapma olursa not edilir. Liste açıklamaya konur.
2. **Elle süre = `[ELLE SÜRE]`.** Aynı kirli dosya, baştan sona (yorum maddelerini yazmak dahil). Telefon kronometresiyle ölç, ekranı kaydet (hızlandırılmış B-roll). Elle yolda da aynı kontroller yapılır (silmeden önce sayma, tarih aralığı, toplamların karşılaştırılması) ve süreye dahildir; kontrolsüz elle süre ile kontrollü yapay zekâlı süre karşılaştırılmaz. Çıkan süre ne ise o kullanılır.
3. **Adım süreleri iki yolda da aynı dört adımla ölçülür** `[ÇEKİMDE ÖLÇ]`: Temizle (silme + yardımcı sütunlar + tarih kontrolü ve düzeltmesi) · Birleştir · Özetle (toplam kontrolleri dahil) · Yorumla. Yapay zekâlı yolda ilk prompt'u yazma ve cevabı bekleme süresi "Temizle" adımına yazılır. Bu süreler ekranda kronometrenin yanında adım bazında karşılaştırılır.
4. **Yapay zekâlı süre = `[YZ SÜRE]`.** Tek, kesintisiz kayıt. Başlık bloğunu silme, prompt yazma, cevabı bekleme, formülleri uygulama, kontroller ve hata düzeltme süreye dahil. Kayıttan önce akışın provası yapılmaz: prova yapılırsa süre gerçekte olduğundan kısa çıkar. Prova gerekiyorsa farklı bir kirli kopya üzerinde yapılır ve açıklamada belirtilir.
5. **Sıra.** Önce elle yolu çekiyorum; ikinci yolda dosyayı tanıyor olmam yapay zekâlı süreyi kısaltır. Ayrıca veriyi ve bütün sorunları ben hazırladım; sorunların yerini iki yolda da biliyordum. İkisi de açıklamada ve sonuç bölümünde söylenir.
6. **Tahmin.** Kayıttan önce bir yere yaz: "Yapay zekâlı sürenin yüzde kaçı kontrol ve düzeltmeye gidecek?" `[ÇEKİMDEN ÖNCE YAZ]`. Gerçekleşen oran tahminden en az 10 puan farklıysa hook'taki ve sonuç bölümündeki "tahminimden farklı çıktı" cümlesi kullanılır; değilse kullanılmaz.

**Kalite karşılaştırmasının ölçütleri** (sonuç bölümünde ekranda tablo olarak gösterilir; seslendirme bu tablodan okunur):

| # | Ölçüt | Nasıl bakılır | Elle yol | Yapay zekâlı yol |
|---|---|---|---|---|
| 1 | Ekim genel toplamı anahtarla aynı mı | Özet tablonun genel toplamı − `[ANAHTAR: ekim toplamı]` | evet / fark | evet / fark |
| 2 | Kategori × Şehir tablosunda kaç hücre anahtarla aynı | 30 hücre (6 kategori × 5 şehir), anahtarın "beklenen çıktı" hâliyle hücre hücre fark formülü | … / 30 | … / 30 |
| 3 | Kalan satır sayısı | 620 toplam, 600 ekim | sayı | sayı |
| 4 | Listede olmayan kodlu 7 satır görünür mü | Özet tabloda ayrı satır olarak ve tutarıyla duruyor mu; yoksa bir kategoriye mi karıştı ya da kayboldu mu | evet / hayır | evet / hayır |
| 5 | Yöntem gelecek ay yeniden kullanılabilir mi | Kasım dökümü geldiğinde hangi adımlar baştan yapılacak | bir cümle | bir cümle |

Ölçütler çekimden önce yazılmıştır; sonuç ne çıkarsa tabloya o yazılır. Elle yolun daha iyi çıktığı ölçüt varsa seslendirmede söylenir.

### 2.4 Karşılaştırma formülleri (yapay zekânın verdiğini doğrulamak için; ekranda gösterilen, yapay zekânın gerçek cevabıdır)

Yardımcı sütunlar: J Tarih_T · K UrunKodu_T · L Tutar_T · M Sehir_T · N Kategori · O Ay. Temizlikten sonra veri 2–621. satırlarda.

```
J2 (ilk hâl, tuzağa düşen):
=EĞER(ESAYIYSA(B2);B2;TARİHSAYISI(KIRP(B2)))

J2 (düzeltilmiş):
=EĞER(ESAYIYSA(B2);B2;EĞER(SOLDAN(A2;4)="WEB-";TARİH(SAĞDAN(KIRP(B2);4);SOLDAN(KIRP(B2);2);PARÇAAL(KIRP(B2);4;2));TARİHSAYISI(KIRP(B2))))

J2 (kaçınılacak yarım düzeltme; yalnızca hata verenleri yakalar, yanlış okunan 20 satırı bırakır):
=EĞERHATA(EĞER(ESAYIYSA(B2);B2;TARİHSAYISI(KIRP(B2)));TARİH(SAĞDAN(KIRP(B2);4);SOLDAN(KIRP(B2);2);PARÇAAL(KIRP(B2);4;2)))

K2:
=KIRP(D2)

L2:
=EĞER(ESAYIYSA(G2);G2;SAYIYAÇEVİR(YERİNEKOY(G2;"TL";"");",";"."))

Sehirler!A2 (benzersiz yazımlar):
=BENZERSİZ(KIRP(Satis!H2:H621))
→ çıkan listeyi kopyala, aynı yere Değer olarak yapıştır; sonra B sütununa doğru adı elle yaz.

M2:
=ÇAPRAZARA(KIRP(H2);Sehirler!A:A;Sehirler!B:B;"EŞLEŞMEDİ")

N2:
=ÇAPRAZARA(K2;Urunler!A:A;Urunler!C:C;"EŞLEŞMEDİ")

O2:
=AY(J2)
```

Eski Excel sürümleri için (`BENZERSİZ` ve `ÇAPRAZARA` yoksa):

```
Şehir listesi: H sütununu boş bir sayfaya ("Sehirler", A sütunu) kopyala → Veri > Yinelenenleri Kaldır → B sütununa doğru adı yaz.
               Listede sonda boşluklu bir yazım kaldıysa boşluğunu sil; aynı yazımın boşluksuz hâli zaten varsa satırı sil.
M2:  =EĞERHATA(DÜŞEYARA(KIRP(H2);Sehirler!A:B;2;YANLIŞ);"EŞLEŞMEDİ")
N2:  =EĞERHATA(DÜŞEYARA(K2;Urunler!A:C;3;YANLIŞ);"EŞLEŞMEDİ")
```

Kontrol formülleri:

```
SİLMEDEN ÖNCE (veri 2–650. satırlarda)
Boş satır:             =BOŞLUKSAY(A2:A650)                         beklenen 10
Ara toplam satırı:     =EĞERSAY(A2:A650;"ARA TOPLAM*")             beklenen 7
Ara toplamları ayır:   filtreyle "ARA TOPLAM" satırlarını göster → A ve G sütunlarını "Kontrol" sayfasına, A1:B7'ye kopyala
                       Kontrol!B8  =TOPLA(B1:B7)   (dökümün tamamı)
                       Kontrol!B9  =TOPLA(B2:B6)   (yalnızca ekim)

17 SATIR SİLİNDİKTEN SONRA, YİNELENENLERDEN ÖNCE (veri 2–633)
Geçici J2:             =A2&"|"&B2&"|"&C2&"|"&D2&"|"&E2&"|"&F2&"|"&G2&"|"&H2&"|"&I2
Geçici K2:             =EĞERSAY(J$2:J2;J2)>1
Birebir yinelenen:     =EĞERSAY(K2:K633;DOĞRU)                     beklenen 12
→ geçici J ve K sütunlarını SİL, sonra Veri > Yinelenenleri Kaldır (A–I, hepsi seçili). Excel'in bildirdiği sayı 12 olmalı; 620 satır kalır.

TARİH (veri 2–621)
Hata veren hücre:      =TOPLA.ÇARPIM(--EHATALIYSA(J2:J621))        ilk formülle beklenen 20 · düzeltmeden sonra 0
Dönem dışı tarih:      =EĞERSAY(J2:J621;"<"&TARİH(2026;9;28))+EĞERSAY(J2:J621;">"&TARİH(2026;11;3))
                                                                   ilk formülle beklenen 20 · düzeltmeden sonra 0
En küçük / en büyük:   =MİN(J2:J621)  ve  =MAK(J2:J621)            ilk formülle #DEĞER! · düzeltmeden sonra 28.09.2026 / 03.11.2026
WEB satırı:            =EĞERSAY(A2:A621;"WEB-*")                   beklenen 40
WEB satırlarının tutarı: =ETOPLA(A2:A621;"WEB-*";L2:L621)          beklenen [ANAHTAR]
Ekim satırı:           =EĞERSAY(O2:O621;10)                        beklenen 600

TOPLAM
Çevirme doğru mu:      =YUVARLA(TOPLA(L2:L621)-TOPLA.ÇARPIM(E2:E621;F2:F621);2)   beklenen 0
Satır kaybı var mı:    =YUVARLA(TOPLA(L2:L621)-Kontrol!B8;2)                      beklenen 0
Ekim toplamı:          =YUVARLA(ETOPLA(O2:O621;10;L2:L621)-Kontrol!B9;2)          beklenen 0
                       (PivotTable'ın genel toplamı da Kontrol!B9 ile aynı olmalı)

EŞLEŞME
Eşleşmeyen ürün:       =EĞERSAY(N2:N621;"EŞLEŞMEDİ")               beklenen 7
Eşleşmeyen şehir:      =EĞERSAY(M2:M621;"EŞLEŞMEDİ")               beklenen 0
```

Notlar (hepsi kayıttan önce, ayrı bir kopyada denenir `[ÇEKİMDE DOĞRULA]`):

- Formüller Türkçe arayüzlü Excel ve Türkçe bölge ayarı (ayırıcı `;`, ondalık `,`) içindir. Fonksiyon adı tanınmıyorsa Excel dilin Türkçe değildir; ayırıcı hatası alıyorsan Windows bölge ayarına bak. `METNEÇEVİR` içindeki biçim kodları (`gg.aa.yyyy`, `#.##0,00`) da bölge ayarına bağlıdır.
- **Tuzağın dayandığı davranış:** `TARİHSAYISI`, Türkçe bölge ayarında ay/gün/yıl yazılmış metni gün/ay/yıl diye okur. Gün 12 ya da küçükse hata vermeden yanlış tarihe çevirir (`10/03/2026` → 10 Mart 2026); gün 13 ya da büyükse `#DEĞER!` verir (`10/17/2026` → 17. ay yok). Beklenen: 20 hata + 20 yanlış tarih. Kendi makinende sayılar farklıysa kontrol ve düzeltme bölümleri gerçek davranışa göre yeniden yazılır.
- Sütunda hata değeri varken `MİN` ve `MAK` da hata döndürür; bu, senaryoda ilk işaret olarak kullanılır. `EĞERSAY` ve `ETOPLA` ölçüt aralığındaki hata hücrelerini saymadan geçer (hata döndürmez).
- **Filtre ve boş satırlar:** veride araya girmiş boş satırlar varken tek hücre seçiliyken filtre açılırsa Excel yalnızca ilk boş satıra kadar olan bölgeyi filtreler. Önce A–I sütunlarının tamamı seçilir, filtre öyle açılır. "(Boş Olanlar)" seçeneğinin listede göründüğünü dene.
- **Yinelenenleri Kaldır:** geçici anahtar sütunları silinmeden çalıştırılırsa onlar da karşılaştırmaya girer (K sütunu ilk kopyada `YANLIŞ`, ikincide `DOĞRU`) ve hiçbir satır yinelenen sayılmaz. Kaldırılan satır sayısının 12 olduğunu dene; farklıysa kopyalar asıllarıyla hücre hücre aynı değildir (biçim farkı dahil), kirli dosya düzeltilir.
- **Metin hücreler gerçekten metin mi:** kirli dosyada `=TOPLA.ÇARPIM(--EMETİNSE(G4:G652))` yaklaşık 200, `=TOPLA.ÇARPIM(--EMETİNSE(B4:B652))` yaklaşık 190 (150 + 40) vermeli. Excel `1.014,00 TL` ya da `10/03/2026` değerini yazarken sayıya/tarihe çevirdiyse hücre "Metin" biçimine alınıp değer yeniden yapıştırılır.
- **Tarih biçimi:** J sütununa formül yazıldığında sonuç varsayılan biçimde seri numarası (46 binli bir sayı) olarak görünür. J sütunu ve MİN/MAK hücreleri "Kısa Tarih" biçimine alınır; bu adım senaryoda vardır.
- **Şehir listesi neden değere çevrilir:** `BENZERSİZ` sonucu canlıdır; kaynak aralık değişince (yeni ay verisi, düzeltilen bir satır) listenin sırası ve uzunluğu değişir, B sütununa elle yazılan doğru adlar başka yazımın karşısına kayar ve `ÇAPRAZARA` hata vermeden yanlış şehir döndürür.
- `TARİH` fonksiyonuna metinden kesilen parçalar ("2026", "10", "03") veriliyor; Excel'in bunları sayıya çevirdiğini dene.
- `BENZERSİZ` ve `ÇAPRAZARA` eski Excel sürümlerinde yoktur. Hangi sürümde çektiğini açıklamaya yaz.

### 2.5 Kurallar

- **Çıktı uydurma yok.** `[UYARLA]` ile işaretli cümleler yapay zekânın ne cevap vereceğine ya da ekranda ne görüneceğine dair tahmindir. Çekimden sonra gerçek sonuca göre yeniden yazılır.
- **Hata uydurma yok.** Tarih tuzağı veriye bilerek kondu, prompt'a bilerek yazılmadı ve videoda ikisi de söylenir. Yapay zekâ tuzağa düşmezse (farklı tarih biçimi ihtimalini kendiliğinden sorar ya da ilk formülü zaten sağlam yazarsa) B metinleri okunur: hook, kontrol bölümü, "yapamadığı şey" madde 2, Shorts 1 ve bölüm listesi için B karşılıkları ilgili yerlerde verildi.
- **Bilmiyormuş gibi yapılmaz.** Yapay zekâ "başka tarih biçimi var mı?" diye sorarsa cevap: "Olabilir; ilk bakışta gördüklerim bunlar. Görmediğim bir biçim varsa formül sessizce yanlış sonuç vermesin, ona göre yaz." Ardından B metinleri kullanılır.
- Kullanılan araç, plan (ücretsiz/ücretli) ve çekim tarihi açıklamaya yazılır; seslendirmede araç ve sürüm adı geçmez.

Yer tutucular: `[ELLE SÜRE]`, `[YZ SÜRE]`, `[ÇEKİMDE ÖLÇ]`, `[ÇEKİMDE DOLDUR: …]`, `[ÇEKİMDE DOĞRULA]`, `[ÇEKİMDEN ÖNCE YAZ]`, `[ANAHTAR]`, `[UYARLA]`, `[YAYINDAN ÖNCE DOĞRULA]`.

### 2.6 Planlı tuzak dışındaki hatalar: nereye bakılacak

Tarih tuzağı, yapay zekânın değil, eksik bilgi veren kullanıcının hatasını gösterir; senaryo bunu açıkça söyler. Yapay zekânın kendi yaptığı bir hata çıkarsa o da gösterilir. Aşağıdaki yerler kayıt sırasında zaten kontrol edilir; hata çıkıp çıkmayacağı çekime kadar bilinmez, çıkmazsa "çıktı" denmez.

| Bakılacak yer | Kontrol | Çıkarsa nerede gösterilir |
|---|---|---|
| Fonksiyon adları ve ayırıcı | Formül yapıştırılınca Excel kabul ediyor mu; İngilizce ad, virgül ya da Türkçe Excel'de olmayan bir ad var mı | İlgili adımda, kesilmeden |
| Metin tutarı sayıya çeviren formül | `Çevirme doğru mu` farkı 0 mı | Özet adımında |
| Tarih düzeltmesi yarım mı | Düzeltmeden sonra `Dönem dışı tarih` 0 mı (2.4'teki "yarım düzeltme" gelirse 20 kalır) | Düzeltme bölümünde; ikinci tur düzeltme süreye dahil |
| Şehir eşlemesi | Yapay zekâ "İST." ya da "Ank." için kendi başına karar verdi mi; `Eşleşmeyen şehir` 0 mı | Yardımcı sütunlar adımında |
| Menü yolları | Tarif ettiği menü adı (PivotTable, Yinelenenleri Kaldır, Filtre) kullandığın Excel'de o adla var mı | İlgili adımda tek cümle |
| Yorum maddeleri | Her sayı özet tabloda var mı; yüzdeler Excel'de yeniden hesaplanınca tutuyor mu; "neden" ya da başka ayla karşılaştırma yazmış mı; `EŞLEŞMEDİ` satırını bir kategoriye katmış mı | Yorum adımında; bu videoda yapay zekânın kendi hatasının çıkabileceği başlıca yer burasıdır |

Kayıt sırasında her sapma bir satırla not edilir: zaman damgası · ne beklendi · ne geldi · nasıl fark edildi · düzeltmesi kaç saniye sürdü. Kurguda en öğretici olan tam gösterilir, diğerleri "yapamadığı şey" bölümünün ilgili maddesine bir cümleyle eklenir. Hiç sapma çıkmadıysa sonuç bölümünde "planlı tuzak dışında hata çıkmadı; bu, bir sonraki dosyada çıkmayacağı anlamına gelmez" denir.

---

## 3. Senaryo

Biçim: **SES** = kelimesi kelimesine okunacak metin. **EKRAN** = görüntü tarifi. Prompt'lar ekranda tam metin gösterilir, seslendirmede baştan sona okunmaz. Ekrandaki kronometre gerçek çalışma süresini gösterir; video hızlandırılan yerlerde ileri atlar, bu yüzden kronometre video süresinden hızlı ilerler. Kronometrenin altında küçük bir satır durur: "Elle bu adım: `[ÇEKİMDE ÖLÇ]`" (2.3 madde 3); adım değişince satır da değişir.

Zaman damgaları seslendirme sayımına göre tahminidir; kurgu sonrası gerçek değerlerle değiştirilir.

---

### 0:00–0:35 — Hook

**SES (A — tuzak beklendiği gibi çalıştıysa)** `[UYARLA]`

> Bu, bir toptancının satış dökümü. Altı yüz küsur satır. Tarihler üç ayrı biçimde yazılmış, tutarların bir kısmı sayı değil metin, aynı şehir üç dört farklı şekilde girilmiş. Bundan ekim özetini elle çıkarmam [ELLE SÜRE] sürdü. Aynı işi yapay zekâyla, kontroller dahil [YZ SÜRE] sürede bitirdim; dosyanın kendisini yüklemeden, yalnızca yapısını ve beş örnek satır vererek. Yolda bir formül yirmi hücrede açıkça hata verdi. Asıl sorun, hata vermeyen yirmi satırdı. Onu nasıl yakaladığımı ve bu sürenin ne kadarının kontrole gittiğini göstereceğim.

**SES (B — yapay zekâ tuzağa düşmediyse)**: son üç cümlenin yerine

> Veriye bilerek bir tuzak koydum; yapay zekânın onu görüp görmediğini kontrol etmeden bilemezdim. O kontrolü ve bu sürenin ne kadarının kontrole gittiğini göstereceğim.

Her iki metinde: "yirmi" sayıları ekranda görülen gerçek sayıyla değiştirilir `[ÇEKİMDE DOĞRULA]`. 2.3 madde 6'daki koşul sağlanıyorsa son cümleye "tahminimden farklı çıktı" eklenir; sağlanmıyorsa eklenmez. Oran 2 katın altındaysa (eşik kuralı) iki süre aynı cümlede düz söylenir, "aynı işi… bitirdim" vurgusu yapılmaz.

**EKRAN**

- 0:00 Kirli tablo tam ekran, yavaş aşağı kayar. Sırayla sarı çerçeve: karışık tarihler → "1.014,00 TL" hücresi → "istanbul / İST. / Istanbul".
- 0:11 Elle yol kaydı 30× hızlandırılmış; üstte sarı etiket "Elle: [ELLE SÜRE]".
- 0:17 Yan yana temiz özet tablo; etiket "Yapay zekâ + kontrol: [YZ SÜRE]".
- 0:21 Sohbet penceresi, ataş (dosya ekle) simgesinin üstünde sarı çarpı: "Dosya yüklenmedi · yapı + 5 örnek satır".
- 0:26 (A) Tarih sütunundan iki hücre yan yana: biri `#DEĞER!`, diğeri "10.03.2026". Kırmızı çerçeve hata veren hücrede değil, **düzgün görünen** hücrede bir saniyeden kısa yanıp söner. (B) Yapay zekâya giden 5 satır sarı, tablonun kalanı gri; üstünde soru işareti.
- 0:31 Kronometre 00:00; altında boş bir çubuk: "Kontrol + düzeltme: ?".

**Tutma notu:** İlk altı saniyede izleyicinin kendi dosyası ekranda (tanıma anı). İki süre başta verildiği için "kim kazandı" sorusu gerilim taşımaz; açık döngüler bunlardır: (1) hata vermeyen yirmi satır nasıl yakalandı, (2) sürenin ne kadarı kontrole gitti (boş çubuk sonuç bölümünde dolar), (3) "dosyayı yüklemeden nasıl?". Kırmızı çerçevenin neden düzgün görünen hücrede olduğu söylenmez. Selamlama ve jenerik yok.

---

### 0:35–1:20 — Görev, veri ve kurallar

**SES**

> Önce işi netleştirelim. İki sayfa var. Birincisi satış dökümü: sipariş numarası, tarih, ürün kodu, adet, fiyat, tutar, şehir. İkincisi ürün listesi: hangi kod hangi kategoride. Döküm eylülün son günlerinden kasımın ilk günlerine uzanıyor; müdürümün istediği ise yalnızca ekim: hangi kategori hangi şehirde ne kadar sattı, altında da üç maddelik yorum. Dört iş var: temizle, birleştir, özetle, yorumla. Bir not: bu dosya gerçek bir şirkete ait değil. Verinin tamamını ben ürettim, kirli kısımlarını da bilerek koydum; gerçek satış verisi videoda gösterilmez. Kendi dosyanda neyi paylaşıp neyi paylaşmayacağına iki yerde değineceğim. Kronometrenin kuralı: prompt yazmam, formülleri uygulamam, kontrol etmem ve hatayı düzeltmem süreye dahil.

**EKRAN**

- "Satis" sayfası; üstte birleştirilmiş başlık bloğu ("Dönem: 28.09.2026 – 03.11.2026" sarı alt çizgi), sütun başlıkları sırayla sarı çerçeve. Sonra "Urunler" sayfası.
- Lacivert zeminde dört kutu: "1 Temizle · 2 Birleştir · 3 Özetle · 4 Yorumla" (video boyunca üstte ince ilerleme çubuğu olarak kalır).
- Alt köşede kalıcı küçük not: "Örnek veri — gerçek şirket değil".
- Kronometre gri, yanında: "Süreye dahil: prompt · uygulama · kontrol · düzeltme".

**Tutma notu:** Dört kutu videonun haritası; izleyici nerede olduğunu her an görür. Gizlilik burada tek cümleyle açılır ve iki yerde somut olarak cevaplanır (örnek satırlar, özet tablo); hedef izleyicinin ilk itirazı "şirket dosyamı oraya yükleyemem" olduğu için söz erken verilir.

---

### 1:20–1:50 — Elle yol: süre nereye gitti

**SES**

> Elle yaparken süre tek bir zor işe gitmedi; küçük işlerin toplamına gitti. [ÇEKİMDE DOLDUR: elle yolda gerçekten kullanılan yöntemler, tek cümle — 2.3 madde 1'deki listeden]. En uzun süren adım [ÇEKİMDE DOLDUR: adım ve süresi] oldu. Toplam [ELLE SÜRE]. Bu işlerin hiçbiri zor değil; hepsini tarif edebiliyorum. Tarif edebildiğim işi yapay zekâya da tarif edebilirim.

**EKRAN**

- Elle yol kaydı 30–40× hızlandırılmış, arka planda.
- Önde yatay çubuk grafik: dört adımın elle süresi `[ÇEKİMDE ÖLÇ]`; en uzun çubuk sarı.
- Sonda büyük: "Elle: [ELLE SÜRE]". Küçük satır: "Yöntem ve ölçüm açıklamada".

**Tutma notu:** Otuz saniyeyi geçmez; izleyici çözüm için geldi ve elle yolu zaten biliyor. Çubuk grafik iki iş görür: elle sürenin ölçüldüğünü gösterir ve adım bazındaki yarışın hedeflerini koyar (aynı dört süre kronometrenin altında geri gelecek). Yöntem cümlesi ölçümden önce yazılmaz; elle yolda ne yapıldıysa o söylenir.

---

### 1:50–3:15 — Adım 1: Dosyayı değil, yapısını ver

**SES**

> Kronometreyi başlatıyorum. Önce üstteki birleştirilmiş başlığı siliyorum; başlık satırı birinci satıra geliyor. İçindeki dönemi not aldım: yirmi sekiz Eylül, üç Kasım. İlk karar: dosyayı yüklemiyorum. Yapay zekâya üç şey veriyorum: sütun başlıkları, beş örnek satır ve gördüğüm sorunların listesi. O adımları ve formülleri yazacak, ben Excel'de uygulayacağım. Beş örnek satırdaki müşteri kodunu ve temsilci adını değiştirdim; biçimi aynı kalsın yeter. Prompt ekranda; dört yerine dikkat et. Bir: Excel'imin Türkçe olduğunu, fonksiyon adlarını Türkçe istediğimi ve ayırıcının noktalı virgül olduğunu yazdım. Yazmazsan formül İngilizce adla ve virgülle gelebilir; Türkçe Excel onu kabul etmez. İki: özgün sütunlara dokunmasın, temiz veriyi yan sütunlara yazsın; hata olursa geri dönebileyim. Üç: eşleşmeyen ürün kodunu gizlemesin, hücreye "eşleşmedi" yazsın. Dört, en önemlisi: her adımın sonuna benim bakacağım bir kontrol eklesin. Gönderiyorum. [UYARLA] Cevap geldi: numaralı adımlar, her adımda hangi hücreye ne yazacağım ve altında bir kontrol satırı.

**EKRAN**

- Kronometre sarıya döner ve çalışır; altında "Elle bu adım (Temizle): [ÇEKİMDE ÖLÇ]". İlerleme çubuğu: "1 Temizle".
- 1. ve 2. satırlar seçilir → sağ tık → Sil. Başlık satırı 1. satıra gelir. Köşede küçük not kutusu: "Dönem: 28.09 – 03.11".
- Başlık satırı + 5 veri satırı kopyalanır, boş "Ornek" sayfasına yapıştırılır. C sütunundaki beş müşteri kodu "M-901 … M-905", I sütunundaki adlar "Temsilci X / Y" yapılır (değişen hücreler sarı). Buradan kopyalanıp sohbete yapıştırılır. Ataş simgesine dokunulmaz.
- Alt bant (3 sn): "Kişiyi ya da müşteriyi tanıtan değerleri değiştir; biçim aynı kalsın".
- Prompt tam ekran, en az 6 saniye sabit; seslendirmedeki dört nokta sırayla sarıyla işaretlenir:

```
Excel'de bir temizlik ve özet işi yapacağım. Dosyayı sana yüklemiyorum; yapısını ve örnek satırları veriyorum. Bana uygulayacağım adımları ve formülleri yaz.

ORTAM
- Excel Türkçe (Microsoft 365). Fonksiyon adlarını Türkçe yaz (ör. DÜŞEYARA, ÇAPRAZARA, EĞER, KIRP).
- Formüllerde ayırıcı noktalı virgül (;). Ondalık ayırıcı virgül, binlik ayırıcı nokta.
- Makro/VBA ve Power Query istemiyorum; yalnızca menü adımları ve hücre formülleri.

DOSYA
- "Satis" sayfası: başlıklar 1. satırda, veri 2. satırdan başlıyor, yaklaşık 650 satır.
  A: Sipariş No | B: Tarih | C: Müşteri Kodu | D: Ürün Kodu | E: Adet | F: Birim Fiyat | G: Tutar | H: Şehir | I: Satış Temsilcisi
- "Urunler" sayfası: A: Ürün Kodu | B: Ürün Adı | C: Kategori (temiz, yaklaşık 40 satır)
- Bir siparişte birden fazla ürün satırı olabilir; aynı Sipariş No'nun tekrar etmesi tek başına hata değildir.
- Dökümün dönemi 28.09.2026 – 03.11.2026. Rapor yalnızca Ekim 2026 için istenecek.

ÖRNEK SATIRLAR (Satis sayfasından; müşteri kodu ve temsilci adı değiştirildi, biçim aynı)
[başlık satırı + ilk 5 veri satırı yapıştırılır]

GÖRDÜĞÜM SORUNLAR
1. Araya boş satırlar ve A sütunu "ARA TOPLAM" ile başlayan satırlar girmiş.
2. Bazı satırlar birebir iki kez yazılmış.
3. Tarihler karışık: bazıları gerçek tarih, bazıları metin (03.10.2026 ya da 2026-10-03 gibi).
4. Ürün kodlarının başında ya da sonunda boşluk var.
5. Tutar bazı satırlarda sayı, bazılarında "1.014,00 TL" biçiminde metin.
6. Şehir adları farklı yazılmış (İstanbul, istanbul, İST., Istanbul gibi).

İSTEDİĞİM
- Özgün sütunlara dokunma. Temiz veriyi J sütunundan başlayan yardımcı sütunlara yazdır: Tarih_T, UrunKodu_T, Tutar_T, Sehir_T, Kategori, Ay.
- Kategori, Urunler sayfasından ürün koduyla gelsin. Eşleşmeyen kodu boş bırakma ve gizleme; hücreye "EŞLEŞMEDİ" yazdır.
- Sonunda yalnızca Ekim 2026 satırlarını içeren, Kategori × Şehir kırılımında toplam tutarı gösteren bir PivotTable.

NASIL CEVAP VER
- Adımları uygulama sırasıyla numarala. Her formülü 2. satır için yaz ve hangi hücreye yazılacağını belirt.
- Her adımın sonuna, o adımın doğru çalıştığını anlamam için bakacağım tek bir kontrol ekle (bir sayım, bir toplam, en küçük/en büyük değer gibi).
- Emin olmadığın ya da veriyi görmeden bilemeyeceğin bir şey varsa tahmin etme; bana sor.
```

- Çekimde gerçek cevap gösterilir; yavaşça kaydırılır, kontrol satırları sarı alt çizgi.
- Alt yazı (küçük): "Bu prompt'un boş şablonu açıklamada".

**Tutma notu:** Hook'taki "yüklemeden nasıl?" sorusu ilk yirmi saniyede cevaplanıyor; bu, izleyiciye diğer sözlerin de tutulacağını gösterir. Uzun prompt okunmaz; dört işaretli nokta anlatılır, tamamı için ekran altı saniye sabit durur. "Dört, en önemlisi" vurgusu kontrol bölümüne tohum eker. Müşteri kodunun değiştirilmesi ekranda gerçekten yapılır; yalnızca söylenirse gizlilik sözü havada kalır.

---

### 3:15–4:10 — Adım 2: Silinecek satırlar

**SES**

> Önce silinecek satırlar. Silmeden önce iki şey yapıyorum. Sayıyorum: on boş satır, yedi ara toplam satırı. Ara toplamları da ayrı bir sayfaya kopyalıyorum; bunlar sistemin kendi hesabı, sonda işime yarayacak. Arada boş satır olduğu için önce A'dan I'ya bütün sütunları seçiyorum, filtreyi öyle açıyorum; yoksa filtre ilk boş satırda durur. Boşları ve ara toplamları seçip satır olarak siliyorum. Sonra yinelenenler. Önce kaç satırın birebir aynı olduğunu sayıyorum: on iki. Veri sekmesi, Yinelenenleri Kaldır, bütün sütunlar seçili. Burası önemli: yalnızca sipariş numarasına göre kaldırsaydım aynı siparişteki farklı ürünleri de silerdi. Prompt'a "bir siparişte birden fazla satır olabilir" diye yazmamın sebebi bu. Excel de on iki satır kaldırdığını söylüyor. Altı yüz yirmi satır kaldı.

Sayılar (on, yedi, on iki, altı yüz yirmi) ekranda görülenle aynı olmalı `[ÇEKİMDE DOĞRULA]`. Yapay zekânın bu adım için önerdiği yöntem farklıysa (ör. yardımcı sütunla işaretleme) onun önerisi uygulanır ve cümleler ona göre yazılır `[UYARLA]`; silmeden önce sayma ve ara toplamları kenara alma her durumda yapılır.

**EKRAN**

- İki sayım hücresi büyütülür:

```
=BOŞLUKSAY(A2:A650)                  → 10
=EĞERSAY(A2:A650;"ARA TOPLAM*")      → 7
```

- A–I sütun harfleri seçilir → Veri > Filtre. Yan not kutusu (2 sn): "Önce sütunları seç — filtre ilk boş satırda durmasın".
- A sütunu filtresi: yalnızca "ARA TOPLAM…" satırları → A ve G sütunları kopyalanır → yeni "Kontrol" sayfası. Altına iki toplam: "Dökümün tamamı" ve "Yalnızca ekim (ortadaki beş)". Sayfa sekmesi sarı yanar, kapanır.
- Filtre: (Boş Olanlar) + "ARA TOPLAM…" → satırlar silinir → filtre temizlenir. Hızlandırılmış.
- Geçici anahtar sütunu ve sayımı hızlandırılmış (formüller 2.4'te); sonuç hücresi büyütülür: 12. Geçici sütunlar silinir.
- Veri > Yinelenenleri Kaldır penceresi; "Tümünü Seç" işaretli hâli büyütülür. Excel'in sonuç mesajı (kaldırılan / kalan) büyütülür; önceki "12" ile yan yana, sarı onay.
- Yan not kutusu (2 sn): "Yalnızca Sipariş No'ya göre kaldırma — aynı siparişin diğer satırları da gider".

**Tutma notu:** Üç küçük iş, her biri 15–20 saniye; bekleme anları kesilir. "Sonda işime yarayacak" cümlesi ara toplamlar için açık döngü bırakır (özet adımında kapanır). "Yalnızca sipariş numarasına göre kaldırsaydım" ve "önce sütunları seç" izleyicinin kendi dosyasında yapacağı iki gerçek hatayı gösterir (kaydetmeye değer anlar).

---

### 4:10–5:00 — Adım 2 (devam): Yardımcı sütunlar

**SES**

> Şimdi yardımcı sütunlar. Ürün kodundaki boşluklar için KIRP. Metin olan tutarlar için: "TL" yazısını at, kalanı sayıya çevir. Şehirler için formül yerine küçük bir eşleme tablosu önerdi: [UYARLA] farklı yazımları tek listede topladı. Listeyi kopyalayıp değer olarak yapıştırıyorum; formül olarak kalırsa veri değiştiğinde sırası kayar, karşısına yazdığım adlar yanlış satıra denk gelir. Doğru adları ben yazıyorum. "İST." kısaltmasının İstanbul olduğuna ben karar veriyorum, o değil. Tarihler için de bir formül verdi; yazıp aşağı çektim, sütunu tarih biçimine aldım. [UYARLA] Üç sütun temiz. Tarih sütununda ise bazı hücreler hata veriyor.

B metni (tarih sütununda hata görünmüyorsa) son iki cümlenin yerine: "Dört sütun dolu, görünürde hata yok."

**EKRAN**

- K2, L2 formülleri formül çubuğunda büyütülür (yapay zekânın gerçek cevabı; bölüm 2.4 ile karşılaştır):

```
K2:  =KIRP(D2)
L2:  =EĞER(ESAYIYSA(G2);G2;SAYIYAÇEVİR(YERİNEKOY(G2;"TL";"");",";"."))
```

- "Sehirler" sayfası: A sütununda benzersiz yazım listesi `[ÇEKİMDE DOĞRULA: kaç satır]` → Kopyala → Özel Yapıştır > Değerler (menü büyütülür) → B sütununa doğru adlar yazılır; "İST. → İstanbul" satırı sarı. Büyük-küçük harf farkı olan yazımlar tek satıra indiyse küçük not: "Excel büyük-küçük harfi aynı sayar".
- M2 formülü yazılır, aşağı çekilir.
- J2 tarih formülü yazılır, aşağı çekilir; J sütunu seçilir → Giriş > Sayı Biçimi > Kısa Tarih:

```
J2:  =EĞER(ESAYIYSA(B2);B2;TARİHSAYISI(KIRP(B2)))
```

- Tablo aşağı kayar; J sütununda `#DEĞER!` hücreleri görünür (çerçeve yok, vurgu yok). Kronometre ara değeri: `[ÇEKİMDE ÖLÇ]`.

**Tutma notu:** Bölüm, görünen bir sorunla biter ve çözümü bir sonraki bölüme bırakır; izleyicinin beklediği şey "hata veren hücreler düzelecek"tir, asıl sürpriz hata vermeyenlerdir. "Değer olarak yapıştır" cümlesi videonun ana fikrinin (hata vermeden yanlış sonuç) ikinci, küçük bir örneğidir; uzatılmaz.

---

### 5:00–5:50 — Kontrol: hata veren ve vermeyen satırlar

**SES (A)** `[UYARLA]`

> Kontrol zamanı. En küçük ve en büyük tarihi soruyorum; ikisi de hata, çünkü sütunda hata var. Sayıyorum: yirmi hücre. Hepsinin sipariş numarası "WEB" ile başlıyor ve tarihleri şöyle yazılmış: on, eğik çizgi, on yedi. Ay önce, gün sonra. On yedinci ay olmadığı için formül hata vermiş. Buraya kadar iyi; hata veren hücreyi görürüm. Ama web siparişlerini sayınca kırk çıkıyor. Yirmisi hata verdi; kalan yirmisi? Birine bakıyorum: on, eğik çizgi, sıfır üç. Üç Ekim olması gerekirken on Mart yazıyor. Hata yok; hücre düzgün bir tarih gibi duruyor. Dönemin dışında kalan tarihleri sayıyorum: yirmi. Bu kırk satırın tutarı [ÇEKİMDE DOLDUR: WEB satırlarının tutarı]; ekim özetine hiç girmeyecekti.

**EKRAN (A)**

- İlerleme çubuğunda "1 Temizle"nin yanında küçük büyüteç simgesi: "Kontrol".
- Boş hücrelere sırayla (MİN/MAK hücreleri Kısa Tarih biçiminde):

```
=MİN(J2:J621)                          → #DEĞER!
=MAK(J2:J621)                          → #DEĞER!
=TOPLA.ÇARPIM(--EHATALIYSA(J2:J621))   → [ÇEKİMDE DOĞRULA: 20]
```

- J sütununda filtre: yalnızca `#DEĞER!`. A sütunundaki "WEB-" ön ekleri ve B sütunundaki `10/17/2026` yan yana sarı çerçeve. Üstte tek satır: "10/17/2026 → 17. ay yok → #DEĞER!".
- Filtre temizlenir. Sayım:

```
=EĞERSAY(A2:A621;"WEB-*")              → [ÇEKİMDE DOĞRULA: 40]
```

- "40 − 20 = 20 ?" yazısı. A sütunu filtresi "WEB-", J sütununda hata vermeyen bir satır büyütülür: B `10/03/2026`, J `10.03.2026`. **Kırmızı çerçeve** (hook'taki görüntünün aynısı). Yarım saniye müzik kesilir. Üstte: "10/03/2026 → doğrusu 3 Ekim → formül 10 Mart okudu".
- Sayım:

```
=EĞERSAY(J2:J621;"<"&TARİH(2026;9;28))+EĞERSAY(J2:J621;">"&TARİH(2026;11;3))   → [ÇEKİMDE DOĞRULA: 20]
=ETOPLA(A2:A621;"WEB-*";L2:L621)                                               → [ÇEKİMDE DOLDUR]
```

- Tutar hücresi büyütülür; altında: "Ekim özetine girmeyecek tutar".

**SES (B — tarih sütununda hata yoksa)**

> Görünürde hata yok dedim; yine de kontrol ediyorum, çünkü altı yüz satıra gözle bakamam. Hata veren hücre: sıfır. Dönemin dışında kalan tarih: sıfır. En küçük yirmi sekiz Eylül, en büyük üç Kasım. Tutuyor. Burada bir şey göstermem gerek. Veriye bilerek bir tuzak koymuştum: web siparişlerinde tarih ay, gün, yıl sırasıyla yazılı ve bu satırlar yapay zekâya verdiğim beş örnekte yoktu. Prompt'a da yazmadım. [ÇEKİMDE DOLDUR: yapay zekâ bunu nasıl ele aldı — soru mu sordu, formüle koşul mu ekledi]. Bu sefer yakaladı. Ama dikkat et: kontrolü, yakaladığını bilmeden yaptım. Daha basit bir formül aynı satırlarda ne yapardı, ayrı bir kopyada göstereyim: yirmisinde hata verir, yirmisinde hata vermeden on Mart yazar.

**EKRAN (B):** aynı üç kontrol, sonuçlar 0 / 0 / 28.09.2026–03.11.2026, sarı onay. Sonra kronometre durur (ekranda "süre dışı" etiketi), dosyanın ayrı bir kopyasında 2.4'teki ilk hâl formül uygulanır; `#DEĞER!` ve "10.03.2026" hücreleri yan yana gösterilir; kronometre yeniden başlar. B'de bir sonraki bölümün yalnızca son paragrafı ("bu satırları bilerek koydum…") okunur.

**Tutma notu:** Videonun dönüm noktası. Gerilim iki basamaklıdır: önce görünen hata (izleyici "tamam, bulundu" der), sonra "kırk eksi yirmi" sorusu. Kırmızı çerçeve hook'taki görüntüyle aynı olmalı ki izleyici bağlantıyı kursun. Hatanın bedeli TL olarak söylenir; "rapordan çıkacaktı" soyut kalmaz. Tuzağın bilerek konduğu bu bölümde söylenmez; düzeltmeden sonraya bırakılır ki gerilim düzeltmeye kadar taşınsın. Shorts 1 buradan kesilir.

---

### 5:50–6:45 — Düzeltme ve tuzağın açıklanması

**SES (A)**

> Düzeltme için ne gördüğümü yazıyorum: hata verenleri de, vermeyenleri de. Yalnızca hata veren hücreleri sorsaydım, kalan yirmi satır yanlış tarihle kalabilirdi. [UYARLA] Yeni formül geldi: web siparişlerinde ayı ve günü ayrı ayrı alıp doğru sıraya koyuyor. Yazıp aşağı çekiyorum. Hata veren hücre: sıfır. Dönem dışı tarih: sıfır. En küçük yirmi sekiz Eylül, en büyük üç Kasım. Şimdi açık söyleyeyim: bu satırları veriye bilerek koydum, prompt'a da bilerek yazmadım. Çünkü gerçek dosyada ilk bakışta gözden kaçan bir şey kalabilir. Yapay zekâ yalnızca ona gösterdiğim beş satırı gördü; o beş satırda web siparişi yoktu. Formül yanlış değildi, eksik bilgiyle yazılmıştı. Geriye bir soru kaldı: özet tablonun toplamı, baştan ayırdığım ara toplamlarla tutacak mı?

Düzeltmeden sonra dönem dışı tarih sayısı sıfır çıkmazsa (ör. 2.4'teki yarım düzeltme geldiyse) ikinci tur düzeltme kesilmeden gösterilir, süreye dahildir ve "Yeni formül geldi…" cümlesi gerçekte olana göre yazılır `[UYARLA]`.

**EKRAN**

- Sohbete yazılan düzeltme prompt'u; en az 4 saniye sabit, iki örnek satırı sarı:

```
Kontrolde sorun çıktı. J sütununda [ÇEKİMDE GÖRÜLEN SAYI] hücre #DEĞER! veriyor; [ÇEKİMDE GÖRÜLEN SAYI] hücre de hata vermiyor ama dökümün dönemi (28.09.2026 – 03.11.2026) dışında bir tarih gösteriyor.
Baktım: hepsi Sipariş No'su "WEB-" ile başlayan satırlar. Bu satırlarda tarih metin olarak ve ay/gün/yıl sırasıyla yazılmış. Ay ve gün her zaman iki haneli.
- 10/17/2026 = 17 Ekim 2026 → formül #DEĞER! verdi.
- 10/03/2026 = 3 Ekim 2026 → formül hata vermedi, 10 Mart 2026 yaptı.
Bu satırlar sana verdiğim 5 örnek satırın içinde yoktu.
J2 formülünü şöyle düzelt:
- Hücre zaten gerçek tarihse olduğu gibi kalsın.
- Sipariş No "WEB-" ile başlıyorsa metni ay/gün/yıl olarak çöz.
- Diğer metinleri önceki gibi çevir.
- Yalnızca hata veren hücreleri yakalayan bir çözüm istemiyorum; hata vermeyen WEB satırları da düzelmeli.
Fonksiyon adları Türkçe, ayırıcı noktalı virgül. Sonuna, düzeltmenin çalıştığını göstereceğim kontrolü de yaz.
```

- Yeni formül formül çubuğunda (gerçek cevap; karşılaştırma için beklenen biçim):

```
=EĞER(ESAYIYSA(B2);B2;EĞER(SOLDAN(A2;4)="WEB-";TARİH(SAĞDAN(KIRP(B2);4);SOLDAN(KIRP(B2);2);PARÇAAL(KIRP(B2);4;2));TARİHSAYISI(KIRP(B2))))
```

- Dört kontrol hücresi alt alta yeniden hesaplanır: 0 · 0 · 28.09.2026 · 03.11.2026; yeşil değil sarı onay işareti (kanal paleti). Kronometre ara değeri: `[ÇEKİMDE ÖLÇ]` — yanında "kontrol + düzeltme: [ÇEKİMDE ÖLÇ]".
- "Açık söyleyeyim" cümlesinde grafik: sol kutu "Yapay zekânın gördüğü: 5 satır", sağ kutu "Dosya: 620 satır"; aradaki fark gri. Altında küçük: "Tuzak bilerek kondu · prompt'a bilerek yazılmadı".
- Son cümlede "Kontrol" sayfasının sekmesi bir saniye sarı yanar.

**Tutma notu:** Düzeltme prompt'u seslendirmede tek cümleyle özetlenir, tam metni ekranda durur. Tuzağın bilerek konduğu açıkça söylenir: kanalın tonu sahte "aa hata çıktı" tepkisini kaldırmaz, ayrıca dürüstlük yorumlarda "kurgu" itirazını önler. "Beş satır gördü" grafiği videodan akılda kalacak tek fikirdir. Hata döngüsü burada kapanır; son cümle hemen ikinci döngüyü açar (ara toplamlar), yoksa kalan beş dakikayı yalnızca "yedi satır" taşır.

---

### 6:45–7:35 — Adım 3: İki tabloyu birleştir

**SES**

> İkinci iş: kategoriyi ürün listesinden getirmek. Formül ÇAPRAZARA; Excel'in eskiyse aynı işi DÜŞEYARA yapar, ikisi de ekranda. Dikkat edeceğin yer: arama, temizlediğim ürün kodu sütununda yapılıyor; özgün sütunda değil. Özgün sütunda yapsaydım, başında ya da sonunda boşluk olan kodlar bulunamazdı. [ÇEKİMDE DOLDUR: elle yolda bu adım ne kadar sürdü ve neden — tek cümle; ölçümde öne çıkan bir şey yoksa cümle yazılmaz]. Aşağı çekiyorum ve hemen sayıyorum: kaç satır eşleşmedi? Yedi. Bakıyorum: üç ürün kodu, ürün listesinde hiç yok. Bu, formülün hatası değil; listenin eksiği. Prompt'ta "eşleşmeyeni gizleme" dememin sebebi buydu. Gizleseydi bu yedi satırın tutarı özet tabloda hiçbir kategoriye girmeden kaybolacaktı. Bunları ne yapacağıma sonda döneceğim; şimdilik "eşleşmedi" olarak kalıyorlar.

**EKRAN**

- İlerleme çubuğu: "2 Birleştir". Kronometrenin altı: "Elle bu adım (Birleştir): [ÇEKİMDE ÖLÇ]".
- N2 formülü büyütülür; altında gri kutuda eski sürüm karşılığı:

```
N2:  =ÇAPRAZARA(K2;Urunler!A:A;Urunler!C:C;"EŞLEŞMEDİ")

ÇAPRAZARA yoksa:
N2:  =EĞERHATA(DÜŞEYARA(K2;Urunler!A:C;3;YANLIŞ);"EŞLEŞMEDİ")
```

- K2 başvurusu sarı çerçeve; yanında üstü çizili D2: "özgün sütun değil".
- Kontrol hücresi:

```
=EĞERSAY(N2:N621;"EŞLEŞMEDİ")
```

- Sonuç `[ÇEKİMDE DOĞRULA: 7]`. Filtreyle 7 satır; üç kod sarı. Yanlarına küçük not: "Urunler sayfasında yok".
- Kronometre ara değeri `[ÇEKİMDE ÖLÇ]`.

**Tutma notu:** Hata bölümünün gerilimi düştükten sonra tempo yükseltilir; bölüm bir dakikanın altında. "Sonda döneceğim" cümlesi "yapamadığı şey" bölümüne açık döngü bırakır. DÜŞEYARA karşılığı ekranda durur ama anlatılmaz. Şehir eşlemesinin eski sürüm karşılığı ekranda gösterilmez; açıklamada verilir ve videoda kullanılan sürüm açıklamaya yazılır.

---

### 7:35–8:25 — Adım 4: Özet tablo ve toplamın iki sınaması

**SES**

> Üçüncü iş: özet. Tarihin yanına ay numarasını veren bir sütun ekledim. Verinin içine tıklıyorum, Ekle, PivotTable. Satırlara kategori, sütunlara temiz şehir, değerlere temiz tutar, filtreye ay: on. Tablo hazır. Göndermeden önce toplamı iki ayrı yoldan sınıyorum. Bir: temiz tutar sütununun toplamı ile adet çarpı birim fiyatın toplamı; yani tutar sütununa hiç bakmadan. [UYARLA] Fark sıfır; metinden sayıya çevirme doğru çalışmış. İki: baştan ayırdığım ara toplamlar. Ekime ait beş ara toplamın toplamı ile özet tablonun genel toplamı. [UYARLA] Fark sıfır: [ÇEKİMDE DOLDUR: ekim toplamı]. Yani silerken fazla satır gitmemiş, yinelenen kalmamış, ekim satışlarının hepsi ekimde. Tarihleri düzeltmeseydim bu fark sıfır çıkmazdı.

Farklardan biri sıfır çıkmazsa neden aranır, bulunur ve gösterilir; süreye dahildir. Sıfır çıkmayan farkın üstü örtülmez.

**EKRAN**

- İlerleme çubuğu: "3 Özetle". Kronometrenin altı: "Elle bu adım (Özetle): [ÇEKİMDE ÖLÇ]".
- O2: `=AY(J2)`, aşağı çekilir.
- Ekle > PivotTable; alan listesi: Filtreler = Ay (10 seçili), Satırlar = Kategori, Sütunlar = Sehir_T, Değerler = Toplam Tutar_T. Sayı biçimi binlik ayırıcılı.
- Üç kontrol hücresi alt alta; her biri yazılırken büyütülür:

```
=YUVARLA(TOPLA(L2:L621)-TOPLA.ÇARPIM(E2:E621;F2:F621);2)      → 0    "Çevirme doğru mu"
=YUVARLA(TOPLA(L2:L621)-Kontrol!B8;2)                         → 0    "Satır kaybı var mı"
=YUVARLA(ETOPLA(O2:O621;10;L2:L621)-Kontrol!B9;2)             → 0    "Ekim toplamı"
```

- "Kontrol" sayfasındaki ekim toplamı ile PivotTable'ın genel toplamı çizgiyle birbirine bağlanır, sarı onay.
- Son cümlede küçük kutu (2 sn): "Tarihler düzeltilmeseydi fark: [ÇEKİMDE DOLDUR: 5:00 bölümündeki WEB tutarı]".
- Kronometre ara değeri `[ÇEKİMDE ÖLÇ]`.

**Tutma notu:** PivotTable adımı on saniyede geçilir (çoğu izleyici görmüştür); bölümün değeri iki sınamadadır. Birincisi cevap anahtarı ve ara toplam olmayan her dosyada uygulanabilir; ikincisi 3:15'te ve 5:50'de açılan döngüyü kapatır ve tarih hatasının teslim edilen sayıyı gerçekten değiştireceğini gösterir. Farkın `YUVARLA` ile alınmasının nedeni anlatılmaz; açıklamada bir satırla yazılır. Shorts 3 buradan kesilir.

---

### 8:25–9:15 — Adım 5: Üç maddelik yorum

**SES**

> Son iş: yorum. Burada yapay zekâya ilk kez sayı veriyorum; altı yüz satırı değil, yalnızca özet tabloyu. Müşteri yok, sipariş yok. Ama özet tablo da şirket verisidir; kendi işinde bunu yapıştırmadan önce şirketinin kuralına bak ya da tutarları yüzdeye çevirip öyle ver. Prompt'ta üç kural var. Her madde tablodaki bir sayıya dayansın. Yüzde hesapladıysa hangi iki sayıyı böldüğünü göstersin. Ve neden yazmasın; çünkü tabloda neden yok. [UYARLA] Üç madde geldi: [ÇEKİMDE DOLDUR: maddelerin bir cümlelik özeti]. Göndermeden önce maddelerdeki her sayıyı özet tabloda buluyorum, yüzdeleri Excel'de yeniden hesaplıyorum. [ÇEKİMDE DOLDUR: sayılar tuttu mu; tutmayan varsa hangisi, nasıl fark edildi ve nasıl düzeltildi]. Kronometreyi durduruyorum.

**EKRAN**

- İlerleme çubuğu: "4 Yorumla". Kronometrenin altı: "Elle bu adım (Yorumla): [ÇEKİMDE ÖLÇ]".
- PivotTable kopyalanır, sohbete yapıştırılır. Alt bant (3 sn): "Özet tablo da şirket verisi — kuralına bak ya da yüzdeye çevir".
- Prompt tam ekran, en az 4 saniye sabit:

```
Aşağıda Ekim 2026 satışlarının Kategori × Şehir özet tablosu var (TL). Bu tabloya bakarak genel müdür için 3 maddelik yorum yaz.

Kurallar:
- Her madde en fazla iki cümle olsun ve tablodaki en az bir sayıya dayansın; sayıyı maddede yaz.
- Yüzde hesapladıysan hangi iki sayıyı böldüğünü madde sonunda parantez içinde göster.
- Neden yazma. Tabloda neden yok; "kampanya", "sezon", "talep" gibi açıklamalar ekleme.
- Önceki ayla karşılaştırma yapma; elimde yalnızca ekim var.
- "EŞLEŞMEDİ" satırı, kategorisi henüz belli olmayan ürünlerdir. Bunu maddelere karıştırma; en alta tek cümlelik ayrı bir not olarak yaz.
- Sade ve kurumsal bir Türkçe kullan; sıfat ve abartı yok.

[özet tablo yapıştırılır]
```

- Çekimde gerçek üç madde gösterilir. Bölünmüş ekran: solda maddeler, sağda PivotTable. Maddedeki her sayı için tablodaki hücre sarı çerçeve; yüzdeler için Excel'de bölme formülü görünür. Tutmayan sayı varsa kırmızı çerçeve ve düzeltilmiş hâli.
- Kronometre durur: `[YZ SÜRE]`.

**Tutma notu:** Gizlilik çizgisi burada tamamlanır: satırlar verilmedi, özet verildi ve özetin de masum olmadığı söylendi. Sayı doğrulama ekranda gerçekten yapılır; yapay zekânın kendi hatasının çıkabileceği başlıca yer burasıdır (2.6) ve çıkıp çıkmayacağı çekime kadar belli değildir. Kronometrenin durması bir sonraki bölüme doğrudan bağlanır; arada nefes verilmez.

---

### 9:15–10:00 — Süre ve kalite karşılaştırması

**SES**

> Sonuç: elle [ELLE SÜRE], yapay zekâyla [YZ SÜRE]. Bunun [ÇEKİMDE ÖLÇ] kadarı kontrol ve düzeltmeydi. [UYARLA: 2.3 madde 6'daki koşul sağlandıysa "Kayıttan önceki tahminim … idi."; sağlanmadıysa cümle yok]. O süreyi atlamanı önermem. Kaliteye beş ölçütle baktım; tablo ekranda. [ÇEKİMDE DOLDUR: tablodan okunur — ekim toplamı iki yolda da anahtarla aynı mı; otuz hücreden kaçı aynı; yedi satır iki yolda da görünür mü]. Yapay zekâlı yolun farkı: [ÇEKİMDE DOLDUR: tablodaki bir ölçüt]. Elle yolun daha iyi olduğu nokta: [ÇEKİMDE DOLDUR: tablodaki bir ölçüt; yoksa yapay zekâlı yolda eksik kalan şey]. İki not. Veriyi ben hazırladım; sorunların yerini iki yolda da biliyordum. Ve bu, ilk seferin süresi. Kasım dökümü geldiğinde prompt ve formüller hazır olacak; şehir listesine ve kontrollere yeniden bakmam gerekecek. Ne kadar kısalacağını ölçmeden söylemeyeceğim.

Planlı tuzak dışında hata çıkmadıysa "İki not"tan önce eklenir: "Planlı tuzak dışında hata çıkmadı; bu, bir sonraki dosyada çıkmayacağı anlamına gelmez."

**EKRAN**

- Kronometre tam ekran. Sabit kalıp, kapaktaki tipografiyle: `[ELLE SÜRE] → [YZ SÜRE]`.
- Hook'taki boş çubuk dolar: "Kontrol + düzeltme: [ÇEKİMDE ÖLÇ]" (toplam sürenin içindeki payı sarı).
- Altında dört adımın iki yoldaki süresi yan yana (çift çubuk): Temizle · Birleştir · Özetle · Yorumla `[ÇEKİMDE ÖLÇ]`.
- Kalite tablosu (2.3'teki beş ölçüt, iki sütun); seslendirmede geçen satır sarı.
- Küçük not: "İki süre aynı kişi tarafından, aynı dosyada ölçüldü; önce elle yol çekildi. Veriyi hazırlayan da aynı kişi. Yöntem açıklamada."

**Tutma notu:** İki süre baştan belliydi; bu bölümün taşıdığı şey sürenin dağılımıdır (hook'taki boş çubuk) ve kalite tablosu. İzleyicinin çıkma riski en yüksek an burasıdır; bölüm kısa tutulur ve son cümleden hemen sonra "yapamadığı şey" başlar, yedi satırlık açık döngü hâlâ duruyor. Elle yolun daha iyi olduğu noktanın söylenmesi zorunludur; yoksa karşılaştırma reklam gibi durur.

---

### 10:00–11:05 — Yapamadığı şey

**SES**

> Şimdi yapamadığı şey. Üç tane var. Bir: şu yedi satır. Üç ürün kodu listede yok ve hangi kategoriye ait olduklarını yapay zekâ bilemez. Sorarsan kodun ön ekine bakıp tahmin eder; tahmin belki tutar da. Ama müdüre giden tabloya tahmin yazılmaz. Bunu ürün listesini tutan kişiye soracağım; o zamana kadar tabloda "eşleşmedi" diye, tutarıyla birlikte duracak. İki: görmediği veriyi bilmiyor. [UYARLA] Bugünkü hata buradan çıktı. Beş satır verdiysen formül beş satır için yazılmıştır; kalanı için kontrol senin işin. Dosyanın tamamını yükleyebildiğin bir araç kullansan bile aynı üç kontrolü yap: silmeden önce say, en küçük ve en büyük değere bak, toplamı iki yoldan hesapla. Üç: nedeni bilmiyor. Bir kategori bir şehirde az sattıysa tablo bunu gösterir; sebebini göstermez. Sebebi sen biliyorsun ya da soracağın kişi biliyor. Sana bir sorum var: Excel'de en çok vaktini alan iş hangisi? Yoruma yaz; tek tek formüllere girdiğim videonun örneklerini o yorumlardan seçeceğim.

Madde 2, B metni ("Bugünkü hata buradan çıktı." yerine): "Bugün tuzağı gördü; yarın başka bir dosyada göreceğini bilemem."

Yorum adımında ya da başka bir yerde yapay zekânın kendi hatası çıktıysa (2.6) ilgili maddeye bir cümle eklenir `[ÇEKİMDE DOLDUR]`.

**EKRAN**

- Başlık kartı: "Yapamadığı şey" (kanalın sabit bölüm kartı).
- Madde 1 — "Karar": 7 satırlık filtre görüntüsü; PivotTable'da "EŞLEŞMEDİ" satırı ve tutarı sarı `[ÇEKİMDE DOLDUR: tutar]`.
- Madde 2 — "Görmediği veri": "5 satır / 620 satır" grafiği tekrar. Altında üç kontrol tek satırda: "Silmeden önce say · MİN/MAK · İki yoldan toplam".
- Madde 3 — "Neden": PivotTable'da Ankara × Toner ve Kartuş hücresi sarı; yanında soru işareti.
- Yorum sorusu alt bantta yazılı olarak da görünür.

**Tutma notu:** Kanalın imza bölümü ve 6:45'te açılan "yedi satır" döngüsünün kapanışı. Madde 2 videonun ana fikrini bir cümleyle tekrar eder; izleyicinin yanında götüreceği üç kontrol tek karede toplanır (ekran görüntüsü alınacak kare).

---

### 11:05–11:35 — Kopyalanabilir prompt ve sonraki video

**SES**

> Bugün kullandığım üç prompt'un boş şablonu açıklamada; ilki şu an ekranda. Köşeli parantezleri kendi dosyana göre doldur: sütunların, beş örnek satır, gördüğün sorunlar. "Fonksiyon adları Türkçe, ayırıcı noktalı virgül" satırını ve "her adıma kontrol ekle" satırını silme. Bugün tek bir yapay zekâ aracı kullandım ve hangisi olduğunu söylemedim; açıklamada yazıyor. Gelecek hafta sıra onda: aynı Türkçe işleri üç ayrı araca veriyorum ve cevapları yan yana koyuyorum.

Son cümle `[YAYINDAN ÖNCE DOĞRULA: bir sonraki yayınlanacak video hâlâ Yayın 3 mü — (3) ChatGPT / Gemini / Claude: Türkçede Hangisi Daha İyi; sıra `docs/01-icerik-uretim-sistemi.md` Bölüm 9'da]`. Sıra değiştiyse cümle ve bitiş ekranı kartı yeni videoya göre yazılır; Senaryo 03 stok videodur ve bu videonun ertesi haftasına konmaz.

**EKRAN**

- Şablon prompt tam ekran (bölüm 4, Prompt 1); doldurulacak yerler sarı. Köşede küçük: "Prompt 2 ve 3 açıklamada".
- "Gelecek hafta" cümlesinde: üç boş sohbet penceresi yan yana, üstlerinde aynı Türkçe prompt, 3 saniye.
- Bitiş ekranı (son 15–20 sn): solda sonraki video kartı (yayınlanana kadar Senaryo 01), sağda abone düğmesi. Sesli "abone ol" çağrısı ve vedalaşma cümlesi yok; son sesli cümle sonraki videodur.

**Tutma notu:** Kapanış bir teslimatla yapılır; prompt, "ekranda" denildiği anda görünür. Sonraki videonun köprüsü bu videoda bilerek açık bırakılan sorudur ("hangi araç?"). Yorum sorusu bir önceki bölümün sonunda sorulmuştur ve gerçek bir kullanıma bağlıdır: (21) numaralı formül videosunun örnekleri.

**Süre aşılırsa kesme sırası** (kurgu 12 dakikayı geçerse): (1) 1:20–1:50 bölümünde yöntem cümlesi çıkar, çubuk grafik 12 saniye kalır; (2) 4:10–5:00'da K ve L formüllerinin anlatımı tek cümleye iner; (3) 6:45–7:35'te elle yol cümlesi çıkar. Kontrol, düzeltme, toplam sınaması ve "yapamadığı şey" bölümlerinden kesilmez.

---

## 4. Kopyalanabilir prompt'lar ve kontroller (açıklamaya konacak; Prompt 1 ayrıca sabit yoruma)

**Prompt 1 — Dosyayı yüklemeden adım ve formül istemek**

```
Excel'de bir temizlik ve özet işi yapacağım. Dosyayı sana yüklemiyorum; yapısını ve örnek satırları veriyorum. Bana uygulayacağım adımları ve formülleri yaz.

ORTAM
- Excel Türkçe ([sürümün, ör. Microsoft 365 / Excel 2019]). Fonksiyon adlarını Türkçe yaz (ör. DÜŞEYARA, ÇAPRAZARA, EĞER, KIRP).
- Formüllerde ayırıcı noktalı virgül (;). Ondalık ayırıcı virgül, binlik ayırıcı nokta.
- Makro/VBA ve Power Query istemiyorum; yalnızca menü adımları ve hücre formülleri.

DOSYA
- "[sayfa adı]" sayfası: başlıklar [kaçıncı] satırda, yaklaşık [kaç] satır.
  [A: … | B: … | C: … — sütun harfi ve başlığı]
- "[ikinci sayfa adı]" sayfası: [sütun harfi ve başlığı]
- [Bilmesi gereken kural, ör. "aynı sipariş numarası birden fazla satırda olabilir"]
- [Verinin kapsadığı dönem ve raporun istendiği dönem, ör. "döküm 28.09–03.11; rapor yalnızca ekim"]

ÖRNEK SATIRLAR
[başlık satırı + 5 veri satırı; kişiyi ya da müşteriyi tanıtan değerleri önce değiştir, biçimi aynı bırak]

GÖRDÜĞÜM SORUNLAR
1. […]
2. […]
3. […]

İSTEDİĞİM
- Özgün sütunlara dokunma. Temiz veriyi [harf] sütunundan başlayan yardımcı sütunlara yazdır: [istediğin temiz sütunlar].
- [Getirilecek bilgi], "[ikinci sayfa]" sayfasından [eşleşecek sütun] ile gelsin. Eşleşmeyeni boş bırakma ve gizleme; hücreye "EŞLEŞMEDİ" yazdır.
- Sonunda [dönem/filtre] için [satır alanı] × [sütun alanı] kırılımında [toplanacak değer] gösteren bir PivotTable.

NASIL CEVAP VER
- Adımları uygulama sırasıyla numarala. Her formülü 2. satır için yaz ve hangi hücreye yazılacağını belirt.
- Her adımın sonuna, o adımın doğru çalıştığını anlamam için bakacağım tek bir kontrol ekle (bir sayım, bir toplam, en küçük/en büyük değer gibi).
- Emin olmadığın ya da veriyi görmeden bilemeyeceğin bir şey varsa tahmin etme; bana sor.
```

**Prompt 2 — Kontrolde sorun çıkınca**

```
Kontrolde sorun çıktı.
- Yaptığım kontrol: [formül ya da sayım]. Beklediğim: [beklenen sonuç]. Gördüğüm: [görülen sonuç].
- Sorunlu satırların ortak yanı: [ör. sipariş numarası "WEB-" ile başlıyor].
- Hata veren örnek: [özgün değer] = [olması gereken] → formül [verdiği sonuç] verdi.
- Hata vermeyen ama yanlış olan örnek (varsa): [özgün değer] = [olması gereken] → formül [verdiği sonuç] yaptı.
- Bu satırlar sana verdiğim örnek satırların içinde yoktu.

[Hücre] formülünü şöyle düzelt:
- [Doğru çalışan durumlar olduğu gibi kalsın.]
- [Sorunlu satırlar nasıl ayırt edilecek ve nasıl çözülecek.]
- Yalnızca hata veren hücreleri yakalayan bir çözüm istemiyorum; hata vermeyip yanlış sonuç veren satırlar da düzelmeli.
Fonksiyon adları Türkçe, ayırıcı noktalı virgül. Sonuna, düzeltmenin çalıştığını göstereceğim kontrolü de yaz.
```

**Prompt 3 — Özet tablodan yorum**

```
Aşağıda [dönem] [konu] için [satır alanı] × [sütun alanı] özet tablosu var ([birim]). Bu tabloya bakarak [kim] için [kaç] maddelik yorum yaz.

Kurallar:
- Her madde en fazla iki cümle olsun ve tablodaki en az bir sayıya dayansın; sayıyı maddede yaz.
- Yüzde hesapladıysan hangi iki sayıyı böldüğünü madde sonunda parantez içinde göster.
- Neden yazma. Tabloda neden yok; tabloda olmayan açıklama ekleme.
- [Elinde olmayan karşılaştırmayı yasakla, ör. "önceki ayla karşılaştırma yapma; elimde yalnızca bu ay var".]
- [Tabloda özel bir satır varsa ne yapacağını söyle, ör. "EŞLEŞMEDİ satırını maddelere karıştırma; en alta ayrı not yaz".]
- Sade ve kurumsal bir Türkçe kullan; sıfat ve abartı yok.

[özet tablo; şirketinin kuralı izin vermiyorsa tutarlar yerine yüzdeler]
```

**Üç kontrol** (yapay zekâ ne derse desin yapılır):

```
1. Silmeden önce say:  kaç boş satır, kaç toplam satırı, kaç birebir yinelenen var? Sildikten sonra Excel'in bildirdiği sayı bununla aynı mı?
                       Dosyada sistemin kendi ara toplamları varsa silmeden önce bir kenara kopyala.
2. Uç değerler:        tarih sütununda hata veren hücre var mı (=TOPLA.ÇARPIM(--EHATALIYSA(aralık))), =MİN ve =MAK beklenen dönemin içinde mi?
3. İki yoldan toplam:  =YUVARLA(TOPLA(temiz tutar)-TOPLA.ÇARPIM(adet;birim fiyat);2) sıfır mı?
                       Kenara aldığın ara toplamlar varsa: temiz verinin toplamıyla farkı sıfır mı?
```

"Kalan satır = ham − silinen" hesabı kontrol sayılmaz: Excel ne sildiyse o çıkar, yanlış satır silinmiş olsa da tutar. Bu yüzden sayım silmeden **önce** yapılır ve toplam, silme işleminden bağımsız bir kaynakla (ara toplamlar, adet × fiyat) karşılaştırılır.

---

## 5. Shorts'a kesilecek 3 an

| # | Kaynak | Süre (tahmini) | Açılış cümlesi | İçerik | Uzun videoya köprü |
|---|---|---|---|---|---|
| 1 | 5:00–5:50 (kontrol) + 5:50–6:45'ten "beş satır gördü" cümlesi | 40–50 sn | **A:** "Bu hücrede hata mesajı yok. Ama tarih yanlış." **B:** "Yapay zekâya beş satır gösterdim. Dosyada altı yüz yirmi satır vardı." | **A:** 10/17/2026 hata veriyor, 10/03/2026 sessizce 10 Mart oluyor; "kırk eksi yirmi" sayımıyla yakalama; "yapay zekâ yalnızca gösterdiğin beş satırı gördü". **B:** tuzağın ne olduğu, yapay zekânın onu nasıl ele aldığı `[ÇEKİMDE DOLDUR]`, basit formülün ayrı kopyada ürettiği iki sonuç; "kontrolü yakaladığını bilmeden yaptım". | "Düzeltilmiş formül ve işin tamamı uzun videoda." |
| 2 | 1:50–3:15 (prompt'taki tek satır) | 25–35 sn | "Yapay zekânın yazdığı Excel formülü sende hata veriyorsa, prompt'a bu satırı ekle." | "Excel Türkçe, fonksiyon adları Türkçe, ayırıcı noktalı virgül" satırı. Satır olmadan ve satırla alınan formül yan yana — ayrı çekilir, gerçek çıktı kullanılır `[ÇEKİMDE DOĞRULA: satır olmadan gerçekten İngilizce/virgüllü geliyor mu; gelmiyorsa bu Shorts yapılmaz, yerine "filtreyi açmadan önce sütunları seç" ya da "yalnızca sipariş numarasına göre yinelenen kaldırma" anı (3:15–4:10) kesilir]`. | "Bu satırın içinde olduğu prompt'un tamamı uzun videonun açıklamasında." |
| 3 | 7:35–8:25 (toplamın sınanması) | 25–35 sn | "Excel tablonu göndermeden önce toplamı iki ayrı yoldan hesapla." | TOPLA ile TOPLA.ÇARPIM farkı; neden iki yol. Ara toplam kısmı alınmaz (bağlam ister). Yapay zekâ kelimesi hiç geçmeyebilir: salt Excel ipucu olarak daha geniş kitleye ulaşabilir (varsayım; Shorts verisiyle bakılır). | "Bu kontrolü neden yaptığımı uzun videoda görürsün." |

Dikey kadraj için: formül çubuğu ve ilgili hücreler yakınlaştırılır; tablo tam genişlikte gösterilmez. Her Shorts'ta kanalın lacivert-sarı çerçevesi ve ilgili video bağlantısı. Yayın sırası önerisi: 1 → 3 → 2.

---

## 6. Açıklama metni taslağı

```
Dağınık bir satış dökümünü temizleyip ürün tablosuyla birleştirmek, ekim özetini ve 3 maddelik yorumu çıkarmak: elle [ELLE SÜRE], yapay zekâyla kontroller dahil [YZ SÜRE]. Dosyanın kendisini yüklemeden; yalnızca yapısını ve 5 örnek satırı vererek.

KOPYALANABİLİR PROMPT'LAR
1) Dosyayı yüklemeden adım ve formül istemek
[bölüm 4, Prompt 1]
2) Kontrolde sorun çıkınca
[bölüm 4, Prompt 2]
3) Özet tablodan yorum
[bölüm 4, Prompt 3]

HER SEFERİNDE YAPILACAK 3 KONTROL
1. Silmeden önce say: kaç boş, kaç toplam satırı, kaç birebir yinelenen? Excel'in sildiği sayı aynı mı?
2. Tarih sütununda hata veren hücre var mı; =MİN ve =MAK beklenen dönemin içinde mi?
3. =YUVARLA(TOPLA(tutar)-TOPLA.ÇARPIM(adet;fiyat);2) sıfır mı? (YUVARLA: ondalıklı sayılarda görünmeyen küsurat farkı yanlış alarm vermesin diye.)

VİDEODAKİ FORMÜLLER (Türkçe Excel, ayırıcı noktalı virgül)
Ürün kodu:        =KIRP(D2)
Tutar:            =EĞER(ESAYIYSA(G2);G2;SAYIYAÇEVİR(YERİNEKOY(G2;"TL";"");",";"."))
Tarih (ilk hâl):  [ÇEKİMDE DOLDUR: videoda görünen ilk formül]
Tarih (düzeltilmiş): [ÇEKİMDE DOLDUR: videoda kullanılan son formül]
Şehir listesi:    =BENZERSİZ(KIRP(Satis!H2:H621)) → kopyala, Değer olarak yapıştır, karşısına doğru adı yaz
Şehir:            =ÇAPRAZARA(KIRP(H2);Sehirler!A:A;Sehirler!B:B;"EŞLEŞMEDİ")
Kategori:         =ÇAPRAZARA(K2;Urunler!A:A;Urunler!C:C;"EŞLEŞMEDİ")
Ay:               =AY(J2)

ESKİ EXCEL SÜRÜMLERİ (BENZERSİZ ve ÇAPRAZARA yoksa)
Şehir listesi:    H sütununu boş bir sayfaya kopyala → Veri > Yinelenenleri Kaldır → karşısına doğru adı yaz
Şehir:            =EĞERHATA(DÜŞEYARA(KIRP(H2);Sehirler!A:B;2;YANLIŞ);"EŞLEŞMEDİ")
Kategori:         =EĞERHATA(DÜŞEYARA(K2;Urunler!A:C;3;YANLIŞ);"EŞLEŞMEDİ")
Excel'in İngilizceyse fonksiyon adları ve ayırıcı farklıdır; Prompt 1'deki ORTAM bölümünü kendine göre değiştir.

BÖLÜMLER
[bölüm 7'deki liste]

NASIL ÖLÇTÜM
- Elle süre: aynı dosyayı yapay zekâ kullanmadan, bu işi daha önce nasıl yapıyorsam öyle bitirdim; kontroller dahil. Yöntem: [ÇEKİMDE DOLDUR: 2.3 madde 1'deki liste]. Süre: [ELLE SÜRE].
- Yapay zekâlı süre: tek kesintisiz kayıt; prompt yazma, uygulama, kontrol ve hata düzeltme dahil. Süre: [YZ SÜRE].
- Önce elle yolu yaptım; ikinci yolda dosyayı tanıyor olmam yapay zekâlı süreyi kısaltır.
- Veriyi ben hazırladım; sorunların yerini iki yolda da biliyordum.
- [ÇEKİMDE DOLDUR: prova yapıldıysa hangi kopyada yapıldığı; yapılmadıysa "akışın provası yapılmadı, yalnızca formüller ayrı kopyada denendi"]
- Senin süren Excel bilgine ve dosyana göre farklı çıkar.

VERİ VE GİZLİLİK
Videodaki dosya gerçek bir şirkete ait değil; tamamını ben ürettim. Tarih tuzağını veriye bilerek koydum ve prompt'a bilerek yazmadım. Yapay zekâya dosyanın kendisi gitmedi; sütun başlıkları, müşteri kodu ve temsilci adı değiştirilmiş 5 örnek satır ve en sonda özet tablo gitti. Özet tablo da şirket verisidir: kendi işinde müşteri adı, kişisel veri, ciro ya da şirketinin gizli saydığı bir bilgiyi herhangi bir yapay zekâ aracına yapıştırmadan önce şirketinin kuralına bak.

KULLANILAN ARAÇLAR
Yapay zekâ: [ÇEKİMDE DOLDUR: araç, plan (ücretsiz/ücretli)] · Excel: [ÇEKİMDE DOLDUR: sürüm, dil] · Çekim tarihi: [ÇEKİMDE DOLDUR]

ÖNCEKİ VİDEO
ChatGPT'yi Yanlış Kullanıyorsun: Sonucu Değiştiren 7 Alışkanlık → [bağlantı]

Kısa Mesai: aynı işi yarı sürede bitir. Haftada bir video.
```

Sabit yorum: Prompt 1 + "Excel'de en çok vaktini alan iş hangisi?" sorusu.

---

## 7. Bölüm (chapter) listesi

Süreler kurgu bitince gerçek zaman damgalarıyla değiştirilir. Bölüm adları aranan ifadeleri içerir ve hem A hem B senaryosunda doğrudur.

```
0:00 Elle [ELLE SÜRE], yapay zekâyla [YZ SÜRE]
0:35 Görev: dağınık satış dökümü ve örnek veri
1:20 Elle yapınca süre nereye gidiyor
1:50 Dosyayı yüklemeden prompt yazmak
3:15 Excel'de boş satır, ara toplam ve yinelenen satırları silmek
4:10 Metin tutarı sayıya çevirmek, şehir adlarını düzeltmek
5:00 Kontrol: ay/gün/yıl yazılmış tarihleri yakalamak
5:50 Tarih formülünü düzeltmek
6:45 İki tabloyu birleştirme: ÇAPRAZARA ve DÜŞEYARA
7:35 PivotTable ve toplamı iki yoldan sınamak
8:25 Yöneticiye 3 maddelik yorum
9:15 Süre ve kalite karşılaştırması
10:00 Yapay zekânın yapamadığı şey
11:05 Kopyalanabilir prompt'lar
```

---

## 8. Çekim öncesi hazırlık listesi

**Veri**
- [ ] 620 satırlık temiz veri üretildi (10 eylül + 600 ekim + 10 kasım); `cevap-anahtari.xlsx` olarak saklandı.
- [ ] "Anahtar" sayfası dolu: toplam, ekim toplamı, yedi dönem toplamı, Kategori × Şehir tablosunun iki hâli (tam ve beklenen çıktı), WEB satırlarının tutarı.
- [ ] Üç bulgu anahtarda görünüyor: (a) Kâğıt Ürünleri en büyük pay, (b) Ankara'da Toner ve Kartuş zayıf, (c) Antalya Temizlik'te Bursa'nın önünde.
- [ ] Temiz veride doğal yinelenen yok (Sipariş No + Ürün Kodu + Adet anahtarında EĞERSAY > 1 çıkan satır yok).
- [ ] Tutar = Adet × Birim Fiyat her satırda birebir.
- [ ] Kirletme 2.2'deki sırayla yapıldı; yinelenen 12 satır kirletilmiş hâlinden, biçimiyle kopyalandı.
- [ ] Kirli dosyada 649 veri satırı var: 10 boş, 7 ara toplam, 12 yinelenen; üstte 2 satırlık birleştirilmiş başlık bloğu.
- [ ] Yedi ara toplam satırının G değeri sayı ve anahtardaki dönem toplamlarıyla aynı.
- [ ] 40 WEB satırının hepsi ekimde; tarihleri "Metin" biçiminde ve ay/gün/yıl; 20'sinde gün 01–12 (10 yok), 20'sinde 13–31.
- [ ] Metin hücreler gerçekten metin: `EMETİNSE` sayımları 2.4'teki gibi (tutar yaklaşık 200, tarih yaklaşık 190).
- [ ] İlk 5 veri satırı kurala uygun: metin tarih, gerçek tarih, metin tutar, boşluklu kod ve iki şehir yazımı var; WEB, boş, ara toplam ve yinelenen satır yok.
- [ ] Kirli dosyanın Urunler sayfasında 37 ürün var; eksik 3 kod Satis'te 7 ekim satırında geçiyor.
- [ ] Dosyada gerçek şirket, müşteri ya da kişi adı yok.
- [ ] Kirli dosyanın üç kopyası var: elle yol, yapay zekâlı yol, formül denemeleri.

**Doğrulama (kayıttan önce, deneme kopyasında)**
- [ ] Bölüm 2.4'teki bütün formüller kendi Excel'inde çalışıyor (Türkçe adlar, noktalı virgül).
- [ ] Tuzak beklendiği gibi: ilk tarih formülüyle 20 hücre `#DEĞER!`, 20 hücre dönem dışı tarih; `MİN`/`MAK` hata döndürüyor. Sayılar farklıysa kontrol ve düzeltme bölümleri yeniden yazıldı.
- [ ] Düzeltilmiş formülle hata 0, dönem dışı 0, MİN = 28.09.2026, MAK = 03.11.2026.
- [ ] Sütunlar seçilip açılan filtrede "(Boş Olanlar)" görünüyor ve 649 satırın tamamı filtreleniyor.
- [ ] Geçici anahtar sütunuyla sayım 12; sütunlar silindikten sonra Yinelenenleri Kaldır 12 satır siliyor, 620 kalıyor.
- [ ] Benzersiz şehir listesinin kaç satır çıktığı ve hangi yazımların birleştiği not edildi; 4:10 bölümündeki cümle ve ekran notu buna göre yazıldı.
- [ ] Eşleşmeyen ürün 7; eşleşmeyen şehir 0; ekim satırı 600.
- [ ] Üç toplam farkı 0; PivotTable genel toplamı anahtardaki ekim toplamıyla aynı.
- [ ] Bu doğrulama prova sayılmasın diye yalnızca formüller denendi; akış baştan sona oynanmadı.

**Ölçüm ve kayıt**
- [ ] Elle yöntem dört satırda yazıldı ve kayıttan önce sabitlendi (2.3 madde 1).
- [ ] Kontrol + düzeltme payı tahmini kayıttan önce yazıldı (2.3 madde 6).
- [ ] Elle yol kaydedildi, süre ölçüldü, dört adımın süresi not edildi → `[ELLE SÜRE]`.
- [ ] Elle yolun özet tablosu kalite karşılaştırması için saklandı.
- [ ] Ekran kaydı çözünürlüğü ve Excel yakınlaştırması telefonda okunacak düzeyde (formül çubuğu büyütülmüş).
- [ ] Bildirimler kapalı; sohbet geçmişinde ve dosya yolunda kişisel bilgi görünmüyor.
- [ ] Yapay zekâ aracında yeni, boş bir sohbet açık; kalıcı talimat ya da bellek özelliği varsa kapalı ya da açıklamada belirtilecek.
- [ ] Kronometre yerleşimi hazır; kayıt tek parça alınacak. Sapma notları için boş bir tablo açık (2.6).

**Kayıttan sonra**
- [ ] `[YZ SÜRE]`, dört adım süresi ve kontrol + düzeltme süresi kayıttan okundu.
- [ ] Oran hesaplandı; eşik kuralına göre kapak, başlık ve hook seçildi.
- [ ] A ya da B senaryosu seçildi ve beş yerde aynı senaryo kullanıldı: hook, 4:10 bölümünün son cümlesi, kontrol bölümü, "yapamadığı şey" madde 2, Shorts 1.
- [ ] Bütün `[UYARLA]` cümleleri gerçek çıktıya göre yeniden yazıldı.
- [ ] Kalite tablosunun beş satırı iki yol için dolduruldu; seslendirme tablodan yazıldı.
- [ ] Sapma notlarındaki her satır ya gösterildi ya da "yapamadığı şey" bölümüne eklendi; hiç yoksa sonuç bölümündeki cümle eklendi.
- [ ] Başlık, kapak, hook, sonuç bölümü ve açıklamadaki süreler aynı ve ölçülenle birebir.
- [ ] Son cümle ve bitiş ekranı kartı bir sonraki yayınlanacak videoyla eşleşiyor.
- [ ] Senaryoda `[` ile başlayan doldurulmamış yer tutucu kalmadı (metinde ara).
- [ ] Seslendirme, yer tutucular dolduktan sonra yeniden sayıldı; kurgu 10,5–12 dk aralığında, aşıyorsa kesme sırası uygulandı.
