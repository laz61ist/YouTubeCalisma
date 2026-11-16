# 05 — Performans Analiz Sistemi

Kanal: **Kısa Mesai** · Belge tarihi: 2026-11-16 · Şablonlar: `sablonlar/analiz-tablosu.csv`, `sablonlar/aylik-degerlendirme.md`

Bu belge yeni bir ölçüm tanımı getirmez; var olan üç parçanın **üstüne kurulan analiz katmanıdır:**

| Zaten yazılmış olan | Yeri | Bu belgede |
|---|---|---|
| Metrik tanımları, Studio'daki yerleri, iyi/kötü işaretler | `02-buyume-stratejisi.md` Bölüm A (A1–A11) | Tekrar edilmez; atıf verilir |
| Kıyas merdiveni, "düşük/yüksek" tanımı, asgari veri eşikleri V1–V4, belirti → müdahale tablosu | 02 belgesi B5 | Teşhis yöntemi ve kanıt toplama adımları eklenir (Bölüm 6) |
| Test kuralları (tek değişken, FT1–FT7, hipotez kartı, kaç videoda karar) | 02 belgesi B4 | Analiz bulgusu teste buradan devredilir |
| Haftalık 30 dakikalık rutin, asgari doldurma kuralı | 02 belgesi B8 | Aynı 30 dakika; ekran ve soru düzeyinde açılır (Bölüm 4) |
| Video kartı, işaret noktaları, çıkarım alanları | `sablonlar/performans-kaydi.md` | Değişmez; özet tabloları elektronik tabloya taşınır (Bölüm 2) |
| Yayın sonrası tutma grafiği adımları | `01-icerik-uretim-sistemi.md` 7.5 | Blok ölçümü ve kural yazımı eklenir (Bölüm 7) |
| Tek videonun yapay zekâyla yorumu | `sablonlar/prompt-kutuphanesi.md` P10, P9 | Çok videolu üç yeni prompt (Bölüm 9) |

**Etiketler:** **[Resmî]** YouTube'un kendi sayfası (bağlantıyla) · **[Yaygın gözlem]** resmî olmayan, üreticiler arasında kabul gören çıkarım · **[Tahmini]** bu belgenin çalışma kuralı; gerekçesi yanında · **[DOĞRULA]** karardan önce senin kontrol etmen gereken şey.

**Doğrulama durumu:** YouTube Yardım sayfaları (support.google.com) bu belge yazılırken de açılamadı; resmî sayfaların varlığı ve başlıkları yalnızca arama sonuçlarından görüldü. Bu yüzden **[Resmî]** etiketli her Studio özelliği ayrıca **[DOĞRULA]** taşır (02 belgesindeki "[Resmî — sayfada teyit et]" ile aynı anlam). Studio'daki sekme ve düğme adları Türkçe arayüzde beklenen karşılıklardır; birebir bulamazsan aynı kavramı ara (02 belgesi Ek, madde 12). Kanal ve video düzeyindeki sekme adları ile tarih seçicinin hazır aralıkları da bu kapsamdadır. Bu belgedeki bütün sayısal eşikler **[Tahmini]**dir; YouTube'un açıkladığı sınırlar değildir.

---

## 1. Sistem haritası

Analizin dört katmanı vardır; her biri bir öncekinin çıktısını okur.

```
Studio (ham veri) → analiz-tablosu (video başına 1 satır) → değerlendirme (haftalık / aylık / çeyreklik) → karar (tek cümle, test kartı, içerik planı)
                    performans-kaydi (video kartı: tutma, yorum, çıkarım)
```

| Veri | Nereden | Ne sıklıkla | Nereye yazılır | Hangi kararı besler |
|---|---|---|---|---|
| Etiketler (kategori, kurgu, başlık formülü, kapak, hook, rol) | `video-brief.md`, `yayin-metaverisi.md` | Yayın günü, **veriyi görmeden önce** | Analiz tablosu A–O | Aylık kalıp analizi |
| Gösterim, 30. sn (48 saat) | Video → Analytics → Erişim; Etkileşim | Cumartesi, 5 dk (02 B5) | Video kartı, 48 saat sütunu | Karar yok; yalnızca açık hata |
| 7. gün değerleri (ön değer) | Video → Analytics; sabit aralık (aşağıda "7g ve 28g tanımı") | Perşembe (yayın + 7); sayım hücreleri bir sonraki perşembe kesinleşir | Analiz tablosu P–X, BR–BS | Haftanın tek kararı |
| 28. gün değerleri, trafik payları | Video → Analytics → Erişim → trafik kaynağı türleri | Perşembe (yayın + 28): karar hücreleri; kalanlar aylık veri hazırlığında | Analiz tablosu Y–AU, BT–BU; arama terimleri karta | Kart kapanışı; aylık analiz |
| Tutma grafiği: işaret noktaları, olaylar | Video → Analytics → Etkileşim | V2 varsa 7. gün, yoksa 28. gün (karta); 28. gün değerleri aylık veri hazırlığında tabloya | Video kartı "Tutma grafiği"; analiz tablosu BV–CB | Bir sonraki senaryo (Bölüm 7); blok kaybı |
| Arama terimleri, yorumlar | Video düzeyi: Erişim → arama terimleri kartı. Kanal düzeyi: Gelişmiş mod → Trafik kaynağı → YouTube araması; Yorumlar | Haftalık | `fikir-havuzu.md` (en fazla 3 satır) | Konu seçimi |
| Kanal tabanı, izleyici türleri, kitle kartları | Analytics → Genel Bakış; Kitle | Aylık | `aylik-degerlendirme.md`; performans kaydı §5.3 | Sürdür / durdur / dene |
| Shorts: görüntüleme, kaydırmadan kalma, uzun videoya geçiş | Shorts'un kendi Analytics sayfası; uzun videonun kaynak tablosunda "Shorts feed'i" satırı | Aylık veri hazırlığı | Performans kaydı §3; analiz tablosu AJ | FT5, FT6; üçüncü Shorts (Bölüm 5, adım 4) |
| Toplu sağlama | Gelişmiş mod → dışa aktarma | Aylık | Ayrı sayfa ("ham"); elle girilenle karşılaştırılır | Veri temizliği |
| Prompt tıklaması | Kısa bağlantı aracının paneli (performans kaydı Bölüm 0) | 7. gün; 28. gün değeri aylık veri hazırlığında | Analiz tablosu X, AU | Prompt'un değeri; bülten eşiği |
| Gelir, RPM; açılmadan önce eşiklere ilerleme | Analytics → Gelir (para kazanma açıksa); öncesinde Studio → Kazanç **[DOĞRULA]** | Aylık | Analiz tablosu AV–AW; aylık form Bölüm 6 | Bölüm 5, adım 6; Bölüm 6, D8 |

**Studio'nun dört aracı ve ne için kullanılacağı:**

- **Gelişmiş mod.** Herhangi bir rapor kartının altındaki "Daha fazla göster" ya da sağ üstteki "Gelişmiş mod" ile açılır; boyut (video, trafik kaynağı, coğrafya, abonelik durumu, tarih…) ve metrik seçilir. **[Resmî][DOĞRULA]** [Learn how to use Advanced mode for analytics reports](https://support.google.com/youtube/answer/9717005). Kullanım: bir videonun kaynak bazında gösterim/CTR/AVD tablosu; kaynağa tıklayarak arama terimleri ve öneren videolar.
- **Karşılaştırma.** Gelişmiş modda "Karşılaştır": iki video, iki grup ya da iki dönem yan yana gelir **[Resmî][DOĞRULA]** (aynı sayfa). Karşılaştırma menüsünde videoları yayından sonraki aynı süreye göre (ilk 24 saat / 7 gün / 28 gün) hizalayan seçenekler olup olmadığı doğrulanamadı **[DOĞRULA]**; varsa "aynı yaşta kıyas" kuralını tek tıkla sağlar, yoksa tarih aralığını elle yayın tarihine göre kur.
- **Gruplar.** Gelişmiş modda videolardan grup oluşturulabiliyor **[Resmî][DOĞRULA]** (aynı sayfa). Her kategori (B, G, K, M, İ, P) ve her seri için bir grup aç; aylık değerlendirmede kategori toplamı tek seçimle gelir.
- **Dışa aktarma.** Gelişmiş modda üstteki indirme düğmesi → "Geçerli görünümü dışa aktar" → Google E-Tablolar ya da .csv **[Resmî][DOĞRULA]** (aynı sayfa; biçim seçenekleri ikincil kaynaklardan). Satır sınırı olduğu ikincil kaynaklarda yazıyor; bu kanalın video sayısında sorun olmaz.

**Kanal düzeyi ile video düzeyi aynı sekmeleri taşımaz [DOĞRULA].** "Erişim" ve "Etkileşim" sekmeleri video düzeyindedir (Video → Analytics). Kanal genelinde trafik kaynakları ve arama terimleri için yol: Analytics → Gelişmiş mod → boyut: Trafik kaynağı (terimler için "YouTube araması"na tıkla); kısa yol, İçerik sekmesindeki "İzleyiciler videolarınızı nasıl buluyor" kartıdır. Bu belgede "Erişim → …" diye başlayan her yol video düzeyindedir.

**7g ve 28g tanımı (tek tanım).** `7g` = yayın günü dâhil ilk 7 takvim günü (yayın günü → yayın + 6); `28g` = ilk 28 takvim günü (→ yayın + 27). Her zaman **sabit aralıkla** okunur: Video → Analytics → tarih seçici → varsa "İlk 7 gün / İlk 28 gün" hazır aralığı **[DOĞRULA]**, yoksa özel aralık. "Yayınlandığından beri" kullanılmaz; okuma gününe göre değişen bir pencere verir. Studio verisi son bir iki gün için eksik gelebilir **[Yaygın gözlem]**; bu yüzden perşembe (yayın + 7) okunan değer **ön değerdir:** haftanın kararı ona dayanır, ama sayım hücreleri (`P`, `Q`, `R`, `BR`, `BS`) bir sonraki perşembe aynı aralıkla yeniden okunup üstüne yazılır (tahmini 1 dk). 28g hücreleri aylık oturumun veri hazırlığında aynı yolla kesinleşir. Perşembeyi kaçırırsan değer doğrudan kesin okunur; `Not` sütununa okuma tarihini yaz. İlk üç videoda ön ve kesin değeri yan yana not et: fark her hücrede yüzde 2'nin altındaysa **[Tahmini]** kesinleştirme adımını bırak.

**Dışa aktarmanın yapamadığı şey:** Dışa aktarılan tablo, seçili **takvim aralığının** toplamıdır; "her videonun kendi ilk 7 günü" tek tabloda gelmez. Bu yüzden değerler elle okunur: her perşembe iki video, 7. günü dolan için 11, 28. günü dolan için 13 hücre (Bölüm 4).

---

## 2. Veri modeli: `analiz-tablosu.csv`

### 2.1 Performans kaydıyla ilişkisi

`performans-kaydi.md` kendi kullanım notunda tabloların büyüyünce "aynı sütunlarla bir elektronik tabloya" taşınmasını ister. `analiz-tablosu.csv` o tablodur; ikinci bir takip şablonu değildir. **Her sayının tek yeri vardır:**

| Ne | Nerede tutulur |
|---|---|
| Sayılar ve etiketler (video başına bir satır) | `03_KAYITLAR/analiz-tablosu` (elektronik tablo). Performans kaydı §1 ve §2'deki sayıların ve karttaki "Metrikler" tablosunun 7 gün / 28 gün sütunlarının yeri burasıdır; iki yere birden yazılmaz |
| Kartta doldurulmaya devam edenler | "Metrikler" tablosunda yalnızca 48 saat sütunu (gösterim, 0:30) ve izlenme süresi (saat); öbür satırlara "bkz. analiz tablosu". Tutma grafiği notları, en çok getiren 3 arama terimi ve en çok öneren 2 video (§2'nin son iki sütunu), yorumlar, değişiklik günlüğü, çıkarım, üretim süresi |
| Shorts ve diğer platformlar | Performans kaydı §3 (değişmez); aylık oturumda okunur (Bölüm 5, adım 4) |
| Bulgular, açık sorular, aylık bakış | Performans kaydı §5.1–§5.3; aylık çalışma kâğıdı `aylik-degerlendirme.md`. §5.3'teki kategori dağılımı tablosunu "Özet" sayfası karşılar; ikisi birden doldurulmaz |

Metrikler performans kaydındakilerle aynıdır; sütun sırası farklıdır (önce etiketler). Adı ya da birimi değişenler:

| Performans kaydında | Analiz tablosunda | Fark |
|---|---|---|
| Tıklanma oranı (§1) · Gösterim tıklama oranı (kart) | `Toplam CTR % 7g / 28g` | README terim tablosundaki ad; yüzde işareti yok (4,6). Bilgi içindir |
| Planlanan birincil kaynakta gösterim / CTR (kart) | `Plan. kaynak gösterim`, `Plan. kaynak CTR %` (`BR–BU`) | Karttan tabloya taşındı; kararın dayandığı sayılar bunlardır (02 B5) |
| Süre · Ort. gör. süresi (d:ss) | `Süre (sn)` · `Ort. gör. süresi (sn)` | Saniye (9 dk 45 sn = 585) |
| Prompt tıkl. (kısa bağlantı) | `Prompt tıkl. 7g / 28g` | Yalnızca dönem eki |
| Kronometre / karşılaştırma / "yapamadığı şey" anı (kart) | `BV–CB` | Tabloya 28. gün değeri girer; 7. gün okuması kartta kalır |

Özel değerler aynıdır: `test` (yerleşik test süren videonun CTR'si; 02 B4), `[ölçüm yok]` (yöntem kurulmamış; 0 yazılmaz), `[yok]` (özellik kanalda yok, ör. gelir). Formüller metin hücrelerini kendiliğinden dışarıda bırakır.

**Kurulum (bir kez, tahmini 45–60 dk):**

1. **Aç.** CSV noktalı virgülle ayrılmış, ondalık ayırıcısı virgül, UTF-8'dir. Türkçe bölge ayarlı Excel doğrudan açar. Google E-Tablolar'da önce Dosya → Ayarlar → Yerel ayar: Türkiye, sonra Dosya → İçe aktar **[DOĞRULA]**. İki kez içe aktar: `Veri` ve `Sınama` sayfaları.
2. **Formülleri sına, sonra örnekleri sil.** Yedi ÖRNEK satırını silmeden 2.3-c'deki formülleri `Veri` sayfasında 2. satıra yapıştır, 8. satıra kadar doldur. Her `T:` sütunu `Sınama` sayfasındaki sabit değerle aynı çıkmalı (ör. ÖRNEK-6: `AZ` 1,53 · `BB` 1,58 · `BF` 1,83 · `BE` yüksek; ÖRNEK-7: `BA` yüksek · `CD` düşük · `CM` 14,7). Tutmayan sütunda formül yanlış yere yapışmıştır ya da bir işlev adı tanınmamıştır. Sonra `Veri`deki örnek satırların girdi hücrelerini temizle (formüller kalır), `Sınama` sayfasını sil.
3. **Açılır listeler.** `Listeler` adlı sayfada izinli değerleri tut; `D, E, F, G, H, I, K, L, M, N, O, AN` sütunlarına veri doğrulama koy (Excel: Veri → Veri Doğrulama → Liste; E-Tablolar: Veri → Veri doğrulama → Açılır liste (aralıktan) **[DOĞRULA]**). Gruplama ve `BN` birebir yazım karşılaştırır; "KG1" ile "KG 1" iki ayrı gruptur. Yeni konu ailesi önce listeye eklenir. `M` ve `AN` aynı listeyi kullanır (Studio'daki kaynak adları). Köprü rolünde `M`'ye paketin asıl hedeflediği kaynak (çoğunlukla YouTube araması), merkez rolünde Göz atma özellikleri yazılır **[Tahmini]**.
4. **"Özet" sayfası** (2.3-d) ve Studio'da gruplar: her kategori, her seri ve "Taban" (Bölüm 3, kural 7).

**Kullanım kuralı:** `Veri` sayfası her zaman **yayın tarihine göre artan sıradadır.** Sıralanmaz, satır silinmez, araya ya da sona boş satır bırakılarak satır eklenmez, yayın sırası dışında satır girilmez: `÷ medyan` ve üçte bir formülleri "üstteki satırlar = önceki videolar" varsayımıyla çalışır; sıra bozulunca uyarı vermeden yanlış sonuç üretir. `CC` sütunu sıra bozulduğunda "SIRA BOZUK" ya da "BOŞ SATIR" yazar. Sıralama ve filtreleme her zaman kopyada yapılır: sayfayı çoğalt → tümünü seç → kopyala → "yalnızca değerleri yapıştır" → kopyayı sırala. Süreler saniye, yüzdeler yüzde işaretsiz girilir.

### 2.2 Sütunlar

**Grup 1 — Girdi özellikleri (A–O).** Yayın günü, sonuç görülmeden yazılır. Sonradan etiketleme ("bu video aslında öneri videosuydu") kalıp analizini geçersiz kılar.

| Sütun | Ad | Değerler · kaynağı |
|---|---|---|
| A–C | No · Başlık (kısa) · Yayın | KM-00N · tarih (YYYY-AA-GG) |
| D | Kat. | B / G / K / M / İ / P (01 belgesi "Terimler ve kodlar") |
| E | Kurgu | KG1–KG7 (01 belgesi Bölüm 6) |
| F | Başlık formülü | F1–F16 (01 belgesi 2.2) |
| G | Kapak çifti | süre / çıktı / soru (01 belgesi 3.1) |
| H | Kapak yerleşimi | A / B / C (01 belgesi 3.3) |
| I | Hook | H1–H10 (01 belgesi Bölüm 4) |
| J | Süre (sn) | Video süresi, saniye |
| K | Konu ailesi | 2–3 kelime, **görev** adıyla ("Excel raporu", "sunum", "e-posta"); araç adı değil. Aynı aileye aynı yazım |
| L | Rol | arama / öneri / köprü / merkez (02 belgesi B3) |
| M | Planlanan birincil kaynak | Studio'daki kaynak adıyla ("YouTube araması", "Göz atma özellikleri"…) |
| N | Fikir kaynağı | plan / arama terimi / izleyici |
| O | Test (E/H) | Yerleşik başlık/kapak testi sürüyor mu |

**Grup 2 — Performans metrikleri (P–AW, BR–CB).** Tanımlar 02 belgesi Bölüm A'da; burada yalnızca hangi kontrolde doldurulduğu yazılı. Asgari doldurma kuralı (02 B8) geçerlidir: boş hücre "bakılmadı" demektir, sıfır değil.

| Sütun | Ad | Ne zaman |
|---|---|---|
| P–X | Gösterim · Toplam CTR % · Görüntüleme · Ort. gör. süresi (sn) · Ort. gör. % · 30. sn'de kalan % · Abone (+) · Yorum · Prompt tıkl. — hepsi `7g` | 7. gün (ön değer; P, Q, R bir hafta sonra kesinleşir) |
| Y–AC | Gösterim · Toplam CTR % · Görüntüleme · Ort. gör. süresi (sn) · Ort. gör. % — `28g` | 28. gün |
| AD | Karşılaştırmaya ulaşan % 28g | 28. gün; tutma grafiğinde karşılaştırmanın başladığı andaki değer (02 A3: kanalın ana metriği) |
| AE–AF | Abone (+) · Abone (−) 28g | AE 28. gün; AF aylık veri hazırlığı |
| AG–AM | Trafik payları: Göz atma · Önerilen · YouTube araması · Shorts feed'i · Harici · Kanal sayfası · Diğer (% 28g) | 28. gün; yalnızca en büyük üç kaynak, kalanı boş (02 B8) |
| AN | Gerçekleşen birincil kaynak | 28. gün |
| AO–AP | Yeni izleyici · Geri dönen izleyici 28g | **Koşullu;** aylık veri hazırlığı. Studio video düzeyinde bu adla satır göstermiyorsa `[ölçüm yok]` kalır; "ara sıra + düzenli" toplamı yerine yazılmaz (02 A5; Ek, madde 3 **[DOĞRULA]**) |
| AQ–AU | Beğeni · Paylaşım · Yorum · Bitiş ekranı tıkl. % · Prompt tıkl. — `28g` | Aylık veri hazırlığı |
| AV–AW | Tahmini gelir · RPM 28g | Para kazanma açılana kadar `[yok]` |
| BR–BU | Plan. kaynak gösterim · Plan. kaynak CTR % — `7g`; aynı ikili `28g` | 7. ve 28. gün; kaynak tablosunda `M` sütunundaki kaynağın satırı. V1 ve CTR kararları bunlara dayanır (02 B5) |
| BV–CB | 30. sn'de kalan % · kronometre başı (sn) ve o andaki % · karşılaştırma başı (sn) · "yapamadığı şey" başı (sn) ve o andaki % · sondan 30 sn önce kalan % — `28g` | Aylık veri hazırlığı; blok kaybının girdisi (Bölüm 7). Karşılaştırma başındaki yüzde `AD`dir |

**Grup 3 — Türetilmiş göstergeler (AX–BQ, CC–CP).** Başlıkları `T:` ile başlar; formülle hesaplanır, elle yazılmaz. `CQ` serbest `Not` sütunudur. `BR–CB` girdi sütunları türetilmişlerin sağında durur; haftalık girişte Bölüm 4'teki hücre listesini izle.

### 2.3 Formüller

Tablodaki formül ilgili sütunun 2. satırına yapıştırılır ve aşağı doldurulur; hiçbirinde harf değiştirmek gerekmez. İşlev adları Türkçe Excel'e göredir. Google E-Tablolar Türkçe arayüzde aynı adları kullanır **[DOĞRULA]**; bir ad tanınmazsa Dosya → Ayarlar'dan İngilizce işlev adlarını aç ve parantez içindeki adı kullan: ORTANCA (MEDIAN), EĞER (IF), EĞERHATA (IFERROR), YADA (OR), VE (AND), DEĞİL (NOT), ESAYIYSA (ISNUMBER), BAĞ_DEĞ_SAY (COUNT), KAYDIR (OFFSET), SATIR (ROW), MİN (MIN), MAK (MAX), TAMSAYI (INT), KAREKÖK (SQRT), TOPLA.ÇARPIM (SUMPRODUCT), ÇOKEĞERSAY (COUNTIFS), FİLTRE (FILTER), HİPERGEOM.DAĞ (HYPGEOM.DIST). Formüller İngilizce adlarla LibreOffice'te çalıştırıldı; CSV'deki yedi ÖRNEK satırının `T:` değerleri o çalıştırmanın çıktısıdır. Türkçe adlarla Excel'de ve E-Tablolar'da sınanmadı **[DOĞRULA]**; kurulumun 2. adımı bu sınamadır.

**a) Üçte bir etiketi — hüküm sütunu** (`BE`, `CD`, `CE`, `CF`, `CH`; kaynak içi: `BA`, `CG`). 02 B5'teki işlemsel tanımın formülü: video ve kendinden önceki 9 video içinde en düşük ⌊n/3⌋ değerden biriyse "düşük", en yüksek ⌊n/3⌋ değerden biriyse "yüksek", arası "normal". Kümede 6'dan az değer varsa boş kalır. `BA` ve `CG` kümeyi **aynı planlanan kaynağa** (`M`) sahip videolarla sınırlar (video ve önceki 19 satırdaki aynı kaynaklı videolar; 6 değer birikmeden boş **[Tahmini]**), çünkü arama CTR'si Göz atma CTR'siyle kıyaslanmaz. Bu belgede "düşük / yüksek" her yerde bu etiketler demektir.

**b) Kanal medyanına oran — yardımcı gösterge** (`AZ`, `BB`, `BC`, `BD`, `BF`, `BH`). Videonun değeri ÷ **kendinden önceki** en fazla 10 videonun aynı yaştaki medyanı (1,00 = medyan). Önceki videoların 5'ten azında değer varsa boş kalır (02 B5, 1. basamak: "yalnızca kaydet"). Video kendi kıyas kümesine girmez. "Ne kadar" sorusunu cevaplar; **eşik bağlanmaz:** gösterim ve görüntüleme geniş, tutma ve süre dar aralıkta oynadığı için tek bir oran bandı metrikler arasında aynı anlama gelmez. Etiketle çelişirse etiket geçerlidir. `BF` tanım gereği KM-001–005'te boştur; ilk 10 video kendi aralarında `CL` ile sıralanır (ilk 10 videonun sabit 28g medyanına oran; 10 değer dolunca hesaplanır, yalnızca bu 10 video arasında kıyas içindir).

**c) Formül tablosu (2. satır)**

| Sütun | Gösterge | Formül |
|---|---|---|
| AX | Süre bandı | `=EĞER(J2="";"";EĞER(J2<600;"<10 dk";EĞER(J2<720;"10–12 dk";"12+ dk")))` |
| AY | Plan. kaynak CTR ± puan 7g | `=EĞER(VE(ESAYIYSA(BR2);ESAYIYSA(BS2);BR2>0);1,96*KAREKÖK(BS2/100*(1-BS2/100)/BR2)*100;"")` |
| AZ | Gösterim ÷ medyan 7g | `=EĞERHATA(EĞER(YADA(DEĞİL(ESAYIYSA(P2));BAĞ_DEĞ_SAY(KAYDIR(P2;-MİN(10;SATIR()-2);0;MİN(10;SATIR()-2);1))<5);"";P2/ORTANCA(KAYDIR(P2;-MİN(10;SATIR()-2);0;MİN(10;SATIR()-2);1)));"")` |
| BA | Üçte bir (plan. kaynak CTR 7g) | `=EĞERHATA(EĞER(YADA(DEĞİL(ESAYIYSA(BS2));TOPLA.ÇARPIM((KAYDIR(M2;-MİN(19;SATIR()-2);0;MİN(19;SATIR()-2)+1;1)=M2)*ESAYIYSA(KAYDIR(BS2;-MİN(19;SATIR()-2);0;MİN(19;SATIR()-2)+1;1))*1)<6);"";EĞER(TOPLA.ÇARPIM((KAYDIR(M2;-MİN(19;SATIR()-2);0;MİN(19;SATIR()-2)+1;1)=M2)*ESAYIYSA(KAYDIR(BS2;-MİN(19;SATIR()-2);0;MİN(19;SATIR()-2)+1;1))*(KAYDIR(BS2;-MİN(19;SATIR()-2);0;MİN(19;SATIR()-2)+1;1)<BS2))+1<=TAMSAYI(TOPLA.ÇARPIM((KAYDIR(M2;-MİN(19;SATIR()-2);0;MİN(19;SATIR()-2)+1;1)=M2)*ESAYIYSA(KAYDIR(BS2;-MİN(19;SATIR()-2);0;MİN(19;SATIR()-2)+1;1))*1)/3);"düşük";EĞER(TOPLA.ÇARPIM((KAYDIR(M2;-MİN(19;SATIR()-2);0;MİN(19;SATIR()-2)+1;1)=M2)*ESAYIYSA(KAYDIR(BS2;-MİN(19;SATIR()-2);0;MİN(19;SATIR()-2)+1;1))*(KAYDIR(BS2;-MİN(19;SATIR()-2);0;MİN(19;SATIR()-2)+1;1)>BS2))+1<=TAMSAYI(TOPLA.ÇARPIM((KAYDIR(M2;-MİN(19;SATIR()-2);0;MİN(19;SATIR()-2)+1;1)=M2)*ESAYIYSA(KAYDIR(BS2;-MİN(19;SATIR()-2);0;MİN(19;SATIR()-2)+1;1))*1)/3);"yüksek";"normal")));"")` |
| BB | Görüntüleme ÷ medyan 7g | `=EĞERHATA(EĞER(YADA(DEĞİL(ESAYIYSA(R2));BAĞ_DEĞ_SAY(KAYDIR(R2;-MİN(10;SATIR()-2);0;MİN(10;SATIR()-2);1))<5);"";R2/ORTANCA(KAYDIR(R2;-MİN(10;SATIR()-2);0;MİN(10;SATIR()-2);1)));"")` |
| BC | Ort. gör. süresi ÷ medyan 7g | `=EĞERHATA(EĞER(YADA(DEĞİL(ESAYIYSA(S2));BAĞ_DEĞ_SAY(KAYDIR(S2;-MİN(10;SATIR()-2);0;MİN(10;SATIR()-2);1))<5);"";S2/ORTANCA(KAYDIR(S2;-MİN(10;SATIR()-2);0;MİN(10;SATIR()-2);1)));"")` |
| BD | 30. sn ÷ medyan 7g | `=EĞERHATA(EĞER(YADA(DEĞİL(ESAYIYSA(U2));BAĞ_DEĞ_SAY(KAYDIR(U2;-MİN(10;SATIR()-2);0;MİN(10;SATIR()-2);1))<5);"";U2/ORTANCA(KAYDIR(U2;-MİN(10;SATIR()-2);0;MİN(10;SATIR()-2);1)));"")` |
| BE | Üçte bir (görüntüleme 7g) | `=EĞERHATA(EĞER(YADA(DEĞİL(ESAYIYSA(R2));TOPLA.ÇARPIM(ESAYIYSA(KAYDIR(R2;-MİN(9;SATIR()-2);0;MİN(9;SATIR()-2)+1;1))*1)<6);"";EĞER(TOPLA.ÇARPIM(ESAYIYSA(KAYDIR(R2;-MİN(9;SATIR()-2);0;MİN(9;SATIR()-2)+1;1))*(KAYDIR(R2;-MİN(9;SATIR()-2);0;MİN(9;SATIR()-2)+1;1)<R2))+1<=TAMSAYI(TOPLA.ÇARPIM(ESAYIYSA(KAYDIR(R2;-MİN(9;SATIR()-2);0;MİN(9;SATIR()-2)+1;1))*1)/3);"düşük";EĞER(TOPLA.ÇARPIM(ESAYIYSA(KAYDIR(R2;-MİN(9;SATIR()-2);0;MİN(9;SATIR()-2)+1;1))*(KAYDIR(R2;-MİN(9;SATIR()-2);0;MİN(9;SATIR()-2)+1;1)>R2))+1<=TAMSAYI(TOPLA.ÇARPIM(ESAYIYSA(KAYDIR(R2;-MİN(9;SATIR()-2);0;MİN(9;SATIR()-2)+1;1))*1)/3);"yüksek";"normal")));"")` |
| BF | Görüntüleme ÷ medyan 28g | `=EĞERHATA(EĞER(YADA(DEĞİL(ESAYIYSA(AA2));BAĞ_DEĞ_SAY(KAYDIR(AA2;-MİN(10;SATIR()-2);0;MİN(10;SATIR()-2);1))<5);"";AA2/ORTANCA(KAYDIR(AA2;-MİN(10;SATIR()-2);0;MİN(10;SATIR()-2);1)));"")` |
| BG | 1000 gör. başına abone 28g | `=EĞER(VE(ESAYIYSA(AE2);ESAYIYSA(AA2);AA2>0);AE2/AA2*1000;"")` |
| BH | Abone/1000 ÷ medyan 28g | `=EĞERHATA(EĞER(YADA(DEĞİL(ESAYIYSA(BG2));BAĞ_DEĞ_SAY(KAYDIR(BG2;-MİN(10;SATIR()-2);0;MİN(10;SATIR()-2);1))<5);"";BG2/ORTANCA(KAYDIR(BG2;-MİN(10;SATIR()-2);0;MİN(10;SATIR()-2);1)));"")` |
| BI | Paylaşım / 1000 gör. 28g | `=EĞER(VE(ESAYIYSA(AR2);ESAYIYSA(AA2);AA2>0);AR2/AA2*1000;"")` |
| BJ | Prompt tıkl. / 1000 gör. 28g | `=EĞER(VE(ESAYIYSA(AU2);ESAYIYSA(AA2);AA2>0);AU2/AA2*1000;"")` |
| BK | Geri dönen izleyici payı % 28g (koşullu) | `=EĞER(VE(ESAYIYSA(AO2);ESAYIYSA(AP2);AO2+AP2>0);AP2/(AO2+AP2)*100;"")` |
| BL | 28g ÷ 7g görüntüleme | `=EĞER(VE(ESAYIYSA(R2);ESAYIYSA(AA2);R2>0);AA2/R2;"")` |
| BM | Kuyruk payı % (8–28. gün) | `=EĞER(VE(ESAYIYSA(R2);ESAYIYSA(AA2);AA2>0);(AA2-R2)/AA2*100;"")` |
| BN | Plan tuttu mu | `=EĞER(YADA(M2="";AN2="");"";EĞER(M2=AN2;"E";"H"))` |
| BO | V1 (plan. kaynak gösterim 7g ≥ 1000) | `=EĞER(ESAYIYSA(BR2);EĞER(BR2>=1000;"E";"H");"")` |
| BP | V2 (görüntüleme ≥ 100) | `=EĞER(ESAYIYSA(R2);EĞER(R2>=100;"E";"H");"")` |
| BQ | V3 (görüntüleme 28g ≥ 300) | `=EĞER(ESAYIYSA(AA2);EĞER(AA2>=300;"E";"H");"")` |
| CC | Sıra denetimi | `=EĞER(YADA(SATIR()=2;C2="");"";EĞER(C1="";"BOŞ SATIR";EĞER(C2>=C1;"";"SIRA BOZUK")))` |
| CD | Üçte bir (gösterim 7g) | `=EĞERHATA(EĞER(YADA(DEĞİL(ESAYIYSA(P2));TOPLA.ÇARPIM(ESAYIYSA(KAYDIR(P2;-MİN(9;SATIR()-2);0;MİN(9;SATIR()-2)+1;1))*1)<6);"";EĞER(TOPLA.ÇARPIM(ESAYIYSA(KAYDIR(P2;-MİN(9;SATIR()-2);0;MİN(9;SATIR()-2)+1;1))*(KAYDIR(P2;-MİN(9;SATIR()-2);0;MİN(9;SATIR()-2)+1;1)<P2))+1<=TAMSAYI(TOPLA.ÇARPIM(ESAYIYSA(KAYDIR(P2;-MİN(9;SATIR()-2);0;MİN(9;SATIR()-2)+1;1))*1)/3);"düşük";EĞER(TOPLA.ÇARPIM(ESAYIYSA(KAYDIR(P2;-MİN(9;SATIR()-2);0;MİN(9;SATIR()-2)+1;1))*(KAYDIR(P2;-MİN(9;SATIR()-2);0;MİN(9;SATIR()-2)+1;1)>P2))+1<=TAMSAYI(TOPLA.ÇARPIM(ESAYIYSA(KAYDIR(P2;-MİN(9;SATIR()-2);0;MİN(9;SATIR()-2)+1;1))*1)/3);"yüksek";"normal")));"")` |
| CE | Üçte bir (30. sn 7g) | `=EĞERHATA(EĞER(YADA(DEĞİL(ESAYIYSA(U2));TOPLA.ÇARPIM(ESAYIYSA(KAYDIR(U2;-MİN(9;SATIR()-2);0;MİN(9;SATIR()-2)+1;1))*1)<6);"";EĞER(TOPLA.ÇARPIM(ESAYIYSA(KAYDIR(U2;-MİN(9;SATIR()-2);0;MİN(9;SATIR()-2)+1;1))*(KAYDIR(U2;-MİN(9;SATIR()-2);0;MİN(9;SATIR()-2)+1;1)<U2))+1<=TAMSAYI(TOPLA.ÇARPIM(ESAYIYSA(KAYDIR(U2;-MİN(9;SATIR()-2);0;MİN(9;SATIR()-2)+1;1))*1)/3);"düşük";EĞER(TOPLA.ÇARPIM(ESAYIYSA(KAYDIR(U2;-MİN(9;SATIR()-2);0;MİN(9;SATIR()-2)+1;1))*(KAYDIR(U2;-MİN(9;SATIR()-2);0;MİN(9;SATIR()-2)+1;1)>U2))+1<=TAMSAYI(TOPLA.ÇARPIM(ESAYIYSA(KAYDIR(U2;-MİN(9;SATIR()-2);0;MİN(9;SATIR()-2)+1;1))*1)/3);"yüksek";"normal")));"")` |
| CF | Üçte bir (ort. gör. süresi 7g) | `=EĞERHATA(EĞER(YADA(DEĞİL(ESAYIYSA(S2));TOPLA.ÇARPIM(ESAYIYSA(KAYDIR(S2;-MİN(9;SATIR()-2);0;MİN(9;SATIR()-2)+1;1))*1)<6);"";EĞER(TOPLA.ÇARPIM(ESAYIYSA(KAYDIR(S2;-MİN(9;SATIR()-2);0;MİN(9;SATIR()-2)+1;1))*(KAYDIR(S2;-MİN(9;SATIR()-2);0;MİN(9;SATIR()-2)+1;1)<S2))+1<=TAMSAYI(TOPLA.ÇARPIM(ESAYIYSA(KAYDIR(S2;-MİN(9;SATIR()-2);0;MİN(9;SATIR()-2)+1;1))*1)/3);"düşük";EĞER(TOPLA.ÇARPIM(ESAYIYSA(KAYDIR(S2;-MİN(9;SATIR()-2);0;MİN(9;SATIR()-2)+1;1))*(KAYDIR(S2;-MİN(9;SATIR()-2);0;MİN(9;SATIR()-2)+1;1)>S2))+1<=TAMSAYI(TOPLA.ÇARPIM(ESAYIYSA(KAYDIR(S2;-MİN(9;SATIR()-2);0;MİN(9;SATIR()-2)+1;1))*1)/3);"yüksek";"normal")));"")` |
| CG | Üçte bir (plan. kaynak CTR 28g) | `=EĞERHATA(EĞER(YADA(DEĞİL(ESAYIYSA(BU2));TOPLA.ÇARPIM((KAYDIR(M2;-MİN(19;SATIR()-2);0;MİN(19;SATIR()-2)+1;1)=M2)*ESAYIYSA(KAYDIR(BU2;-MİN(19;SATIR()-2);0;MİN(19;SATIR()-2)+1;1))*1)<6);"";EĞER(TOPLA.ÇARPIM((KAYDIR(M2;-MİN(19;SATIR()-2);0;MİN(19;SATIR()-2)+1;1)=M2)*ESAYIYSA(KAYDIR(BU2;-MİN(19;SATIR()-2);0;MİN(19;SATIR()-2)+1;1))*(KAYDIR(BU2;-MİN(19;SATIR()-2);0;MİN(19;SATIR()-2)+1;1)<BU2))+1<=TAMSAYI(TOPLA.ÇARPIM((KAYDIR(M2;-MİN(19;SATIR()-2);0;MİN(19;SATIR()-2)+1;1)=M2)*ESAYIYSA(KAYDIR(BU2;-MİN(19;SATIR()-2);0;MİN(19;SATIR()-2)+1;1))*1)/3);"düşük";EĞER(TOPLA.ÇARPIM((KAYDIR(M2;-MİN(19;SATIR()-2);0;MİN(19;SATIR()-2)+1;1)=M2)*ESAYIYSA(KAYDIR(BU2;-MİN(19;SATIR()-2);0;MİN(19;SATIR()-2)+1;1))*(KAYDIR(BU2;-MİN(19;SATIR()-2);0;MİN(19;SATIR()-2)+1;1)>BU2))+1<=TAMSAYI(TOPLA.ÇARPIM((KAYDIR(M2;-MİN(19;SATIR()-2);0;MİN(19;SATIR()-2)+1;1)=M2)*ESAYIYSA(KAYDIR(BU2;-MİN(19;SATIR()-2);0;MİN(19;SATIR()-2)+1;1))*1)/3);"yüksek";"normal")));"")` |
| CH | Üçte bir (karşılaştırmaya ulaşan % 28g) | `=EĞERHATA(EĞER(YADA(DEĞİL(ESAYIYSA(AD2));TOPLA.ÇARPIM(ESAYIYSA(KAYDIR(AD2;-MİN(9;SATIR()-2);0;MİN(9;SATIR()-2)+1;1))*1)<6);"";EĞER(TOPLA.ÇARPIM(ESAYIYSA(KAYDIR(AD2;-MİN(9;SATIR()-2);0;MİN(9;SATIR()-2)+1;1))*(KAYDIR(AD2;-MİN(9;SATIR()-2);0;MİN(9;SATIR()-2)+1;1)<AD2))+1<=TAMSAYI(TOPLA.ÇARPIM(ESAYIYSA(KAYDIR(AD2;-MİN(9;SATIR()-2);0;MİN(9;SATIR()-2)+1;1))*1)/3);"düşük";EĞER(TOPLA.ÇARPIM(ESAYIYSA(KAYDIR(AD2;-MİN(9;SATIR()-2);0;MİN(9;SATIR()-2)+1;1))*(KAYDIR(AD2;-MİN(9;SATIR()-2);0;MİN(9;SATIR()-2)+1;1)>AD2))+1<=TAMSAYI(TOPLA.ÇARPIM(ESAYIYSA(KAYDIR(AD2;-MİN(9;SATIR()-2);0;MİN(9;SATIR()-2)+1;1))*1)/3);"yüksek";"normal")));"")` |
| CI | Plan. kaynak CTR ± puan 28g | `=EĞER(VE(ESAYIYSA(BT2);ESAYIYSA(BU2);BT2>0);1,96*KAREKÖK(BU2/100*(1-BU2/100)/BT2)*100;"")` |
| CJ | V1 28g (plan. kaynak gösterim ≥ 1000) | `=EĞER(ESAYIYSA(BT2);EĞER(BT2>=1000;"E";"H");"")` |
| CK | Yorum / 1000 gör. 28g | `=EĞER(VE(ESAYIYSA(AS2);ESAYIYSA(AA2);AA2>0);AS2/AA2*1000;"")` |
| CL | Görüntüleme ÷ ilk 10 medyanı 28g | `=EĞER(VE(SATIR()<=11;BAĞ_DEĞ_SAY(AA$2:AA$11)=10;ESAYIYSA(AA2));AA2/ORTANCA(AA$2:AA$11);"")` |
| CM | Kurulum kaybı (% / dk) | `=EĞERHATA(EĞER(VE(ESAYIYSA(BV2);ESAYIYSA(BX2);BV2>0;BW2-30>0);(BV2-BX2)/BV2*100/((BW2-30)/60);"");"")` |
| CN | Görev kaybı (% / dk) | `=EĞERHATA(EĞER(VE(ESAYIYSA(BX2);ESAYIYSA(AD2);BX2>0;BY2-BW2>0);(BX2-AD2)/BX2*100/((BY2-BW2)/60);"");"")` |
| CO | Karşılaştırma kaybı (% / dk) | `=EĞERHATA(EĞER(VE(ESAYIYSA(AD2);ESAYIYSA(CA2);AD2>0;BZ2-BY2>0);(AD2-CA2)/AD2*100/((BZ2-BY2)/60);"");"")` |
| CP | Son bölüm kaybı (% / dk) | `=EĞERHATA(EĞER(VE(ESAYIYSA(CA2);ESAYIYSA(CB2);CA2>0;J2-30-BZ2>0);(CA2-CB2)/CA2*100/((J2-30-BZ2)/60);"");"")` |

Okuma notları: `AY` ve `CI` Bölüm 3, kural 2'de; `BO` ve `CJ` gerçek V1'dir (planlanan kaynaktaki gösterim). `BL` için "iyi" bir değer yoktur; arama rolündeki videoda yüksek, öneri rolündeki videoda düşük çıkması beklenir **[Yaygın gözlem]**, yalnızca aynı roldeki videolar arasında kıyaslanır. `BM` aynı bilginin yüzde hâlidir. `BI` ve `CK` Bölüm 5 adım 5'te, `CM–CP` Bölüm 7 adım 5'te okunur. `BK` yalnızca `AO–AP` ölçülebiliyorsa dolar.

**d) "Özet" sayfası (bir kez kurulur, aylık oturumda yalnızca okunur).** Satırlarda etiket değerleri, sütunlarda video sayısı, medyan, en düşük ve en yüksek değer. Örnek: G kategorisinin 28 günlük görüntüleme medyanı ve dayandığı video sayısı:

```text
=ORTANCA(FİLTRE(Veri!AA2:AA200;(Veri!D2:D200="G")*ESAYIYSA(Veri!AA2:AA200)))
=ÇOKEĞERSAY(Veri!D2:D200;"G";Veri!AA2:AA200;">0")
```

En düşük ve en yüksek için `ORTANCA` yerine `MİN` ve `MAK` yazılır; "etiketi taşımayanlar" satırı için koşul `<>"G"` olur. Çapraz tablo hücresi: `=ÇOKEĞERSAY(Veri!D2:D200;"G";Veri!E2:E200;"KG1")`. `FİLTRE` eski Excel sürümlerinde yoktur; orada `=ORTANCA(EĞER((Veri!D2:D200="G")*ESAYIYSA(Veri!AA2:AA200);Veri!AA2:AA200))` formülünü Ctrl+Shift+Enter ile gir. Medyanın yanında **her zaman** video sayısı durur; sayısız medyan okunmaz.

---

## 3. Okuma kuralları

02 belgesi A2 (CTR'nin dört okuma kuralı), B5 (kıyas merdiveni, V1–V4) ve performans kaydının altı okuma kuralı geçerlidir. Aşağıdakiler onlara eklenir.

**1. Örneklem eşiği önce, yorum sonra.** Bir sayıya bakmadan önce `BO–BQ` (28. gün için `CJ`) sütunlarına bak. V1–V4 video başına okuma eşiğidir (02 B5); gruplar için ek eşikler **[Tahmini]**:

| Karar | Asgari | Mantığı |
|---|---|---|
| Bir etiketin grup medyanını **yazmak** | Grupta 3 video | 02 B8: 3'ten az videolu kategori yorumlanmaz |
| İki grubu **karşılaştırmak** | Her grupta 3 video, değerlerde tam ayrışma ve yönü **önceden yazılmış** karşılaştırma | 3'e 3 videoda *belirli* bir grubun bütün değerlerinin diğerininkilerden yüksek çıkması tesadüfen 20 dizilişten 1'inde olur (6 değerden 3'ünü seçmenin 20 yolu vardır). Yön önceden yazılmadıysa "gruplardan biri ayrık" sonucu 10'da 1'dir. Tek bir çakışma ölçütü düşürür. Bakılan çift sayısı arttıkça tesadüfen ayrık çıkan çift de artar (kural 11) |
| Grup medyanını **karar tablosunda** kullanmak | Grupta 5 video | 02 B4 ile aynı |
| Bir **oranı** (abone/1.000 gör., bitiş ekranı tıklaması) yorumlamak | Paydaki olay sayısı en az 10 | Seyrek olaylarda sayım hatası kabaca olay sayısının karekökü kadardır; 10 olayda bu yaklaşık üçte bir, 4 olayda yarı yarıya oynama demektir. 10'un altında oranı değil, sayının kendisini yaz |

**2. CTR'yi payıyla birlikte oku.** `AY` (7g) ve `CI` (28g), **planlanan kaynaktaki** CTR'nin yalnızca örneklem büyüklüğünden kaynaklanan oynama payını verir (yüzde 95 aralığının yarı genişliği, puan olarak). İki videonun aynı kaynaktaki CTR farkı bu payların toplamından küçükse **fark gösterilemedi** demektir ("fark yok" değil); karar verilmez. Başka bir kaynağın ya da toplamın payını elle hesapla: `=1,96*KAREKÖK(p*(1-p)/n)*100` (p = CTR ÷ 100, n = o satırın gösterimi); toplam CTR'nin payı kaynak kıyasında kullanılmaz. Pay bir alt sınırdır: aynı kişiye birden çok gösterim yapıldığı için gerçek belirsizlik daha büyüktür **[Tahmini]**. Evrensel bir "iyi CTR" eşiği yoktur (02 A2, B9).

**3. Ortalama değil medyan; toplam değil oran.** Görüntüleme dağılımı çarpıktır (02 B9); tek bir video ortalamayı çeker. Tabloda ortalama sütunu yoktur. Kanal büyürken ham sayılar yeni videoların lehine kayar; dönemler arası kıyasta ham görüntüleme yerine `÷ medyan` sütunlarını kullan.

**4. Benzeri benzerle.** Üç eşleşme aranır: **aynı yaş** (7g ile 7g), **aynı trafik kaynağı** (arama CTR'si ile Göz atma CTR'si kıyaslanmaz; `BA` ve `CG` bu yüzden yalnızca aynı planlanan kaynaklı videoları kıyaslar), **aynı rol** (`L` sütunu). Yüzdeler için dördüncüsü: **aynı süre bandı** (`AX`); farklı uzunlukta APV kıyaslanmaz, AVD saniye olarak yan yana yazılır (02 A3).

**5. Karışım etkisi.** Toplam CTR, hiçbir kaynakta CTR değişmeden de düşebilir: gösterimin daha büyük kısmı CTR'si doğal olarak düşük bir kaynağa (çoğunlukla Göz atma) kaymıştır. Toplam CTR'deki her değişimde önce kaynak paylarına bak; kaynak içi CTR değişmemişse yorum "paket bozuldu" değil, "karışım değişti"dir. "Gösterim arttıkça CTR düşer" kuralı (02 A2, kural 1) bunun en sık görülen hâlidir.

**6. Ortalamaya dönüş.** Olağandışı iyi bir videodan sonraki video, hiçbir şey değişmese de daha zayıf görünür; tersi de doğrudur. Bu yüzden kıyas kümesi tek video değil son 10 videodur ve "geçen haftaya göre düştü" cümlesi karar gerekçesi olmaz.

**7. Mevsimsellik.** Hedef kitle çalışan kesim olduğu için resmî tatil haftaları, bayram tatilleri, yaz izin dönemi ve yılbaşı haftasında izleme davranışının değişmesi beklenir **[Tahmini — kendi verinle sına]**. Sınama: Gelişmiş mod → Gruplar → "Taban" grubu; her perşembe 28. günü dolan video gruba eklenir (S3'ün son işi). Grup seçiliyken son 90 günün haftalık görüntülemesi "taban trafiği"dir. Tabanın haftalık görüntülemesi 200'ün altındaysa **[Tahmini]** sınama yapılmaz; hafta yalnızca `Not` sütununa "tatil haftası" diye yazılır. Üstündeyse: yeni videonun zayıf haftasında taban da benzer oranda düştüyse mevsim **olasıdır**; videoya müdahale ertelenir. Taban düzken yeni video düşükse neden videoda aranır.

**8. Tek değişken.** Bir bulguyu sınamak için aynı anda tek şey değişir; sınırlar 02 B4'tedir (aynı anda en fazla 1 format testi + 1 elle paket testi). Analiz açısından sonucu: iki etiketi aynı anda değişen iki video arasındaki fark **hiçbir** etikete yazılamaz.

**9. Etiketler birbirine yapışıktır.** İlk 10 videoda kategori, kurgu ve başlık formülü büyük ölçüde birlikte değişir (G videoları çoğunlukla KG1). Bir etiketi "nedeni" saymadan önce çapraz tabloya bak (Bölüm 5, adım 3-c); iki etiket hep birlikte geliyorsa ayrıştırılamaz, ayrıştıran bir video planlanır.

**10. İpucu → bulgu → kural.** Tek video ipucudur; aynı yönde, asgari verisi tam üç video bulgudur (performans kaydı, okuma kuralı 4); bulgu ancak 02 B4'teki test koşuluyla kanal kuralı olur ve ilgili belgeye işlenir.

**11. Önce yaz, sonra bak.** Bir oturumda onlarca etiket çifti karşılaştırılırsa birkaçının yalnızca tesadüfen ayrık çıkması beklenen sonuçtur. Bu yüzden karşılaştırma tabloyu açmadan önce yönüyle yazılır (oturum başına en fazla üç); yalnızca bunlar "ipucu" üretir. Önceden yazılmamış her ayrık çift **tarama bulgusu**dur: gelecek ayın yazılı sorusu olur ve ancak o tarihten sonra yayınlanan videolarda aynı yönde tekrar ederse ipucuna yükselir.

---

## 4. Haftalık değerlendirme (30 dakika)

02 B8'deki rutinin **kendisidir**; süre, sıra ve asgari doldurma kuralı aynıdır. Burada her adımın ekranı, okunacak hücreler ve cevaplanacak soru yazılı. Kronometreyle yapılır.

| Dk | Soru | Ekran | Ne yazılır |
|---|---|---|---|
| 0–3 | **S1. Kanal tabanı olağan mı?** | Analytics → Genel Bakış, son 7 gün ↔ önceki 7 gün | Yalnızca olağandışı sıçrama/düşüş ve hangi videodan geldiği. Olağandışı yoksa hiçbir şey |
| 3–13 | **S2. 7 günlük video zincirin hangi halkasında "düşük"?** | Video → Analytics, sabit aralık "ilk 7 gün": Erişim (gösterim, CTR, kaynak tablosu); Etkileşim (tutma grafiği) | Analiz tablosu P–X, BR–BS (11 hücre) · kartta tutma notları · geçen haftanın videosunda P, Q, R, BR, BS kesinleşir |
| 13–21 | **S3. 28 günlük video planlanan kaynaktan trafik aldı mı, dersi ne?** | Aynı ekranlar, sabit aralık "ilk 28 gün"; Erişim → trafik kaynağı türleri → kaynağa tıkla | Analiz tablosu Y–AE, en büyük üç kaynağın payı, AN, BT–BU (13 hücre) · karta 3 arama terimi ve tek cümle ders · kart kapanır · video "Taban" grubuna eklenir. `AF`, `AO–AU`, `BV–CB` aylık veri hazırlığına kalır |
| 21–26 | **S4. İzleyici bu hafta ne istedi?** | Kanal düzeyi: Gelişmiş mod → Trafik kaynağı → YouTube araması (terimler); Yorumlar | `fikir-havuzu.md`, en fazla 3 satır |
| 26–28 | **S5. Süren deneme ne durumda?** | Video ayrıntıları → test sonucu; test kartı | Test kartı (02 B4) |
| 28–30 | **Karar** | — | Tek cümle (aşağıda) |

**S2 nasıl cevaplanır (10 dakikanın dökümü):**

1. Sayıları gir (4 dk). `BO` (V1) ve `BP` (V2) "H" ise ilgili metrik bugün okunmaz; hücreyi doldur, yorumu 28. güne bırak.
2. Zinciri soldan sağa **üçte bir etiketleriyle** oku (02 A0): `CD` gösterim → `BA` planlanan kaynakta CTR → `CE` 30. sn → `CF` ort. gör. süresi; sonuç `BE` görüntüleme. İlk "düşük" halkayı bul. Tanım tektir (02 B5: ya alt üçte birdedir ya değildir); `÷ medyan` sütunları yalnızca farkın büyüklüğünü söyler. `BA` boşsa CTR için kanal içi kıyas henüz yoktur; yalnızca kaydet. Sayım sütunlarında (`CD`, `BE`) etiket ön değerle hesaplanır; kesinleşince değişebilir.
3. "Düşük" halka için kaynak tablosunda **planlanan birincil kaynağın** satırı (`BR`, `BS`) toplamla aynı yönde mi (2 dk)?
4. Tutma grafiğinde 0:30 değerini ve üç işaret noktasını oku (02 B8; 3 dk; V2 yoksa atla). Olay okuması Bölüm 7'deki alt sınıra bağlıdır.
5. Alt üçte bir tanım gereği her üç videodan birini işaretler; tek bir "düşük" **kayıttır.** Bölüm 6'nın giriş koşulu sağlanıyorsa ve video KM-006 ya da sonrasıysa 02 B5 karar tablosundaki satırı bul; satır müdahale gerektiriyorsa **tek** müdahale. Ayrıntılı teşhis bu 10 dakikaya sığmaz; teşhis oturumuna (Bölüm 6 sonu) bırakılır ve karar cümlesine "teşhis bekliyor" yazılır.

Dakikalar tahminidir: ilk üç hafta S2 ve S3'ü kronometreyle ölç, tablodaki süreleri kendi sürenle değiştir. Toplam 30 dakikayı aşıyorsa süre uzatılmaz; 28. gün hücrelerinden biri daha aylık veri hazırlığına aktarılır.

**Karar cümlesi (çıktı):** Video kartındaki "Çıkarım" tablosuna ve bir sonraki perşembe ilk okunacak yere yazılır.

```text
KM-[sıradaki no]'da [tek değişken]i [nasıl] yapacağım; [metrik]in [kıyas noktası]na göre [yön] olmasını bekliyorum; [tarih]te (yayın + [7/28]) bakacağım. Dayanak: [KM-no, metrik, değer] — [ipucu / bulgu].
```

Geçerli karar örnekleri: bir senaryo kuralı, bir test başlatma, "bu hafta değişiklik yok; KM-0NN'nin 28. gününü bekliyorum". Geçersiz: iki değişken içeren cümle; metrik ve tarih içermeyen cümle; "daha iyi kapak yapacağım".

**Haftalık rutinde yapılmayanlar:** grup medyanı hesaplamak, kategori kıyaslamak, eski videoların paketini gözden geçirmek, Shorts satırlarını doldurmak, gelire bakmak. Hepsi aylık oturumun işidir.

---

## 5. Aylık değerlendirme (90 dakika)

Her 4 haftada bir, **cuma** günü yapılır (02 B2 takviminin en hafif günü; perşembe yayın ve haftalık rutin günüdür, oraya eklenmez): 5. ve 9. hafta; üçüncü oturum KM-010'un 28. günü dolsun diye 13. değil 14. haftada yapılır ve ilk çeyreklikle birleşir; sonra 18, 22… Çalışma kâğıdı `sablonlar/aylik-degerlendirme.md`. 02 B8'deki "ayda bir, 20 dakika" bakışı bu oturumun **ikinci adımıdır**; ayrıca yapılmaz.

**Süre bütçesi [Tahmini]:** B8'deki 20 dakikanın yerine 90 dakika, yani ayda +70 dk; o hafta isteğe bağlı üçüncü Shorts ve topluluk gönderisi yapılmaz. Çeyreklik oturum ek olarak tahmini 3 saat ister; stokta en az 2 video olan haftaya konur ve o hafta yeni çekim yapılmaz. Teşhis oturumu (Bölüm 6) 20 dakikadır, ayda en fazla iki kez. Bu ekler 02 B2 ve 03 2.1'deki haftalık süre bütçesinde yer almaz (belge sonundaki liste).

**Kısa sürüm:** 28 günlük verisi olan video sayısı 6'nın altındayken (5. ve 9. hafta) yalnızca adım 1, 2 ve 7–8 yapılır (form Bölüm 0, 1, 7); tutma grafiği olan en az 3 video varsa blok kaybı tablosu da doldurulur (form Bölüm 3). Oturum 40–50 dakikada biter.

| Dk | Adım | Çıktı |
|---|---|---|
| 0–20 | **1. Veri hazırlığı.** Bu dönem 28. günü dolan videolarda: sayım hücrelerini sabit aralıkla kesinleştir; `AF`, `AO–AU` ve işaret noktalarını (`BV–CB`) gir. Shorts satırlarını (performans kaydı §3) doldur. Gelişmiş moddan video tablosunu dışa aktar, rastgele üç videoyu karşılaştır. `CC` sütununda uyarı var mı | Temiz tablo |
| 20–35 | **2. Aylık bakış.** Performans kaydı §5.3 satırı (izleyici türleri, vekil göstergeler, stok); taban trafiği; **paket yenileme adayları** (02 B8): `CH` = "yüksek" ve `CG` = "düşük" olan videolar | §5.3 satırı; aday listesi |
| 35–55 | **3. Kalıp bulma ve blok kaybı** (aşağıda) | Grup tablosu, uç grup tablosu, blok tablosu |
| 55–65 | **4. Trafik karışımı ve Shorts** | Kaynak payları, plan–gerçek uyumu, Shorts satırı |
| 65–75 | **5. Kitle, abone dönüşümü, etkileşim** | Dört satırlık not |
| 75–80 | **6. Gelir ve gelir öncülleri** | Eşik ilerlemesi ya da RPM satırı |
| 80–90 | **7–8. Sürdür / durdur / dene + gelecek ayın içerik kararları** | Liste ve plan |

### Adım 3 — Başarılı içerik kalıplarını bulma

**Ön kayıt (kural 11).** Tabloyu açmadan önce forma en fazla **üç** karşılaştırmayı yönüyle yaz (ör. "süre kapaklı videolarda `AD`, çıktı kapaklılardan yüksek"). Oturumun sonunda kaç etiket çiftine baktığını da yaz: yönü yazılmamış çiftlerde tesadüfen ayrık çıkması beklenen sayı ≈ bakılan çift ÷ 10 (3'e 3 videoda).

**a) Etikete göre gruplama.** Grup medyanları "Özet" sayfasından **okunur**; oturumda hesaplanmaz. Her oturumda üç etikete bakılır: `D` kategori ve `L` rol sabit, üçüncüsü dönüşümlü (`E`, `F`, `G`, `I`, `AX`, `K`) ya da ön kayıtlı sorunun etiketi. Dört sonuç sütunu: `BF` görüntüleme ÷ medyan 28g, `AD` karşılaştırmaya ulaşan %, `BG` 1.000 görüntüleme başına abone, `BJ` prompt tıklaması. KM-001–005'in `BF` değeri yoktur; bu videolar analize ham oran sütunlarıyla (`AD`, `BG`, `BJ`) ve ilk 10 video içi kıyasta `CL` ile girer. 3'ten az videolu gruba medyan yazılmaz; "n yetersiz" yazılır.

**b) Medyan karşılaştırma.** İki grup arasında fark aranırken medyanların yanına her grubun **en düşük ve en yüksek** değerini yaz. Aralıklar iç içeyse fark iddia edilmez (Bölüm 3, kural 1). Aralıklar ayrıksa: ön kayıtlı karşılaştırmaysa "ipucu", değilse "tarama bulgusu" yazılır ve çapraz kontrole geçilir.

**c) Çapraz kontrol.** Fark görünen etiket başka bir etiketle birlikte mi geliyor? "Özet" sayfasındaki çapraz tablo hücrelerine bak (2.3-d). G videolarının tamamı KG1 ise "G iyi" ile "KG1 iyi" ayrıştırılamaz; "dene" listesine ayrıştıran video yazılır (KG3 kurgulu bir G videosu gibi).

**d) Uç gruplar.** Sıralama sütunu `BF` (ham görüntüleme değil; ham sıralama kanal büyüdükçe yeni videoları öne alır). `BF` dolu video 9'un altındayken ve ilk 10 videonun 28. günü dolmuşsa `CL` kullanılır. Sıralama kopyada yapılır (2.1, kullanım kuralı). Sıralanabilir video **9'un altındaysa** adım atlanır. **9–19 video:** uç gruplar üst ve alt üçte birdir (02 B5 ile aynı tanım; en az 3'er video). **20 ve üstü:** uç gruplar beşte birdir (en az 4'er video). Aynı işlem ikinci kez `BG` için yapılır; iki sıralamada da uçta olan videolar işaretlenir.

**e) Ortak özellik tablosu.** Her etiket değeri için üç sayı yan yana yazılır:

| Özellik | En iyi grupta | En kötü grupta | Bütün videolarda (taban) | Sonuç |
|---|---|---|---|---|
| ör. Kapak çifti = süre | [x] / [uç grup] | [y] / [uç grup] | [z] / [toplam] | izle / ayrıştırıyor / — |

Taban sütunu olmadan tablo yanıltır: videoların çoğu KG1 ise en iyilerin çoğunun KG1 olması hiçbir şey söylemez. **20 videodan önce** sonuç sütununa en fazla "izle" yazılır: küçük uç grupta her özellik ayrıştırıyor görünür (10 videonun 6'sı bir özelliği taşıyorsa en iyi 2 videonun ikisinin de taşıması 45 dizilişin 15'inde, yani 3'te 1 olasılıkla tesadüfen olur). **20 videodan sonra** "ayrıştırıyor" ölçütü **[Tahmini]**: özellik en iyi grubun en az dörtte üçünde **ve** en kötü grubun en çok dörtte birinde (ya da tersi). Yanılma payını her satır için hesapla: 20 videonun 8'i özelliği taşıyorsa en iyi 4'ün en az 3'ünün taşıması `=1-HİPERGEOM.DAĞ(2;4;8;20;DOĞRU)` ≈ 0,15 olasılıkla tesadüfen olur; alt uç koşuluyla birlikte olasılık düşer, ama tabloda onlarca özellik sınandığı için tek satır yine kanıt değildir. Çıktı her durumda yalnızca **"dene"** listesine gider; bu tablodan "sürdür" ya da "durdur"a doğrudan geçilmez. Tablodan sonra en iyi ve en kötü videoların kartlarındaki "Çıkarım" satırlarını alt alta oku; etiketlerin yakalamadığı ortak nokta (aynı örnek şirket, aynı tür "yapamadığı şey", aynı haftada tatil) çoğu zaman oradadır.

**f) Blok kaybı tablosu.** `CM–CP` sütunları her bloğun dakika başına kaybını verir (Bölüm 7, adım 5). Kıyas yalnızca **aynı blok türü, farklı videolar** arasındadır: forma her blok türünün medyanı ve o medyandan en çok sapan video yazılır. Blok türleri birbiriyle kıyaslanmaz; izleyici kaybı videonun başında her zaman daha hızlıdır, kurulum bloğu hemen her videoda en çok kaybettiren görünür ve bu format hakkında bir şey söylemez **[Yaygın gözlem]**. 02 B1 Aşama 1'in sorusu ("format çalışıyor mu") bu tablodan okunur: bir blok türünde videoların çoğu aynı tür olayla (Bölüm 7) kaybediyor mu?

### Adım 4 — Trafik kaynağı karışımı

1. Kanal düzeyi: Analytics → Gelişmiş mod → boyut: Trafik kaynağı, son 28 gün ↔ önceki 28 gün (kısa yol: İçerik sekmesindeki kart **[DOĞRULA]**). Her kaynağın payını yaz; değişimi puan olarak not et.
2. Plan–gerçek: `BN` sütununda "E" oranı. Rol bazında ayrı say: arama rolündeki videoların kaçında birincil kaynak arama çıktı? Oran düşükse sorun videolarda değil, rol tahminindedir (02 B3).
3. Bağımlılık: tek bir kaynak görüntülemenin büyük çoğunluğunu veriyorsa ve o kaynak "Harici" ise YouTube içi keşif başlamamıştır (02 A6). Sayısal eşik yok; aydan aya yönüne bak.
4. Önerilen → kaynağa tıkla → kendi videolarının payı (02 A5 vekil göstergesi; §5.3'e yazılır).
5. **Shorts** (performans kaydı §3 satırlarından): (a) V4'ü sağlayan Shorts'larda kaydırmadan kalma oranı, tür bazında (FT5); (b) uzun videoların `AJ` sütunu ve §3'teki "uzun videoya geçiş", yayın sırası bazında (FT6; performans kaydı §5.2, soru 1); (c) o ayın kesim + dağıtım süresi. Karar kuralı **[Tahmini]**: dört hafta üst üste hiçbir uzun videonun kaynak tablosunda Shorts kaynaklı görüntüleme görünmüyorsa isteğe bağlı üçüncü Shorts bırakılır, iki Shorts sürer (02 B2). Türler arası hüküm, tür başına en az 3 Shorts V4'ü sağlamadan verilmez; belirti–müdahale satırları 02 B5'in son iki Shorts satırıdır.

### Adım 5 — Kitle ve abone dönüşümü

- **Kim izliyor:** Analytics → Kitle → yaş, cinsiyet, coğrafya; cihaz için Gelişmiş mod → boyut: Cihaz türü **[DOĞRULA]**. Hedef (26–42, Türkiye, çalışan) ile örtüşme. Kartlar yeterli veri yokken boş gelir; boşsa "veri yok" yaz.
- **Başka ne izliyor:** Kitle → "Kitlenizin izlediği kanallar / videolar" kartları **[DOĞRULA: küçük kanalda görünmeyebilir]**. Görünüyorsa listeyi fikir havuzuna değil aylık forma yaz; konumlandırma sorusu çeyreklikte ele alınır.
- **Abone dönüşümü:** Gelişmiş mod → boyut "Abonelik durumu": görüntülemenin abone / abone olmayan payı. Boyut "Abonelik kaynağı" **[DOĞRULA]**: aboneler video sayfasından mı, kanal sayfasından mı geldi. Video bazında `BG` sıralaması: en çok abone getiren üç video ile en az getiren üç videonun rolü ve kurgusu ne?
- **Geri gelme:** Esas olan üç vekil göstergedir (02 A5). `BK` yalnızca `AO–AP` ölçülebiliyorsa okunur; ölçüm yoksa yerine abone olmayanların görüntüleme payı yazılır. Düzenli izleyici sayısı ilk altı ayda sıfırdır; yorumlanmaz.
- **Etkileşim:** `BI` (1.000 görüntüleme başına paylaşım) üst üçte birde olan videoların konu ailesi ve rolü: başkasına gönderilecek kadar işe yarayan konu hangisi; aynı aile iki ay üst üste çıkıyorsa "dene" listesine devam videosu yazılır. `CK` (yorum) videodaki soru davetine bağlı olduğu için videolar arası kıyaslanmaz; onun yerine hangi "yapamadığı şey" sorusunun GÖREV yorumu getirdiği sayılır (02 B6 döngüsünün girdisi). Olay sayısı ≥ 10 kuralı geçerlidir; altında oran değil sayı yazılır. Beğeni kayıttır, karar beslemez.

### Adım 6 — Gelir ve gelir öncülleri

Gelir yöntemleri, İş Ortağı Programı eşikleri ve aşamalı yol haritası `04-gelir-stratejisi.md` belgesindedir (Bölüm 2 ve 4); burada yalnızca ayda bir okunan sayılar var. **Para kazanma açılmadan önce** üç satır: (1) eşiklere ilerleme: abone sayısı ve son 365 günün herkese açık izlenme saati, Studio → Kazanç sekmesinden **[DOĞRULA]** (eşik değerleri 04 belgesi 2.1'dedir); (2) son 5 videonun `BJ` medyanı: prompt'a gidenlerin oranı, dijital ürün ve bülten talebinin vekili (04 belgesi Kart 5 ve 8); (3) bülten eşiği sayımı (performans kaydı §3). Bu üçü burada karar üretmez; 04 belgesindeki aşama kapılarının girdisidir. **Açıldıktan sonra:** Analytics → Gelir → aylık tahmini gelir, RPM ve video bazında dağılım. RPM, 1.000 görüntüleme başına sana kalan toplam gelirdir; oynatma başına BGBM (CPM) ise reklamverenin ödediği tutardır ve ikisi kıyaslanmaz **[Resmî][DOĞRULA]** [Understand ad revenue analytics](https://support.google.com/youtube/answer/9314357). Tabloya yalnızca RPM ve tahmini gelir yazılır; teşhis için Bölüm 6, D8. Vergi ve beyan konuları için mali müşavire danış; bu belge hukuki ya da mali tavsiye içermez.

### Adım 7–8 — Çıktı

**Sürdür / durdur / dene** (her listede en fazla üç madde; her maddenin yanında dayandığı videolar ve güven düzeyi):

| Liste | Giriş koşulu |
|---|---|
| **Sürdür** | Bulgu düzeyinde (3+ video, aynı yön, asgari veri tam) olumlu kalıp. İpucu düzeyindekiler buraya değil "dene"ye girer |
| **Durdur** | Kategori için 02 B4'teki durdurma koşulu. Format öğesi için: 3 videoda alt üçte birde ve çapraz kontrolden geçmiş. Tek kötü video hiçbir şeyi durdurmaz |
| **Dene** | İpuçları ve ayrıştırılamayan etiketler. 02 B4 sınırı geçerli: aynı anda 1 format testi + 1 elle paket testi. Fazlası sıraya yazılır |

**Gelecek ayın içerik kararları** (4–5 yayın yuvası): her yuva için kategori, rol, kurgu ve hangi amaca hizmet ettiği (omurga / eksik kategoriyi tamamlama / deneme / ayrıştırma). Aşama dağılımı 02 B1'e uyar; aylık oturum dağılımı değiştirmez, yuvaları doldurur. Performans kaydı §5.3'teki "bu ayın tek kararı" hücresi buradan çıkar.

---

## 6. Düşük performans teşhisi

02 B5'teki karar tablosu "belirti → müdahale" verir. Bu bölüm araya girer: müdahaleden önce **hangi kanıt toplanır ve iki olası neden nasıl ayrılır.** Ön koşullar aynıdır: KM-006 ve sonrası, asgari veri sağlanmış, yerleşik test sürmüyor. **Giriş koşulu [Tahmini]:** belirtinin etiketi "düşük" **ve** şu ikisinden biri: aynı halka art arda iki videoda "düşük", ya da halkanın `÷ medyan` değeri son 10 videonun en düşüğü. Koşulu sağlamayan "düşük" kaydedilir, teşhis açılmaz. Her dalın sonucu **hipotezdir**, kesinleşmiş neden değildir; sonunda iyileştirme ve tek satırlık karar kuralıyla sınama yazılı. Müdahale metni B5'te varsa yalnızca atıf verilir.

```
Görüntüleme düşük (BE = "düşük")
├─ Gösterim de düşük (CD) ──────────────────────── D1  paket mi, konu mu?
├─ Gösterim olağan, kaynak içi CTR düşük (BA) ──── D2
└─ Gösterim ve CTR olağan → sorun izlemede
     ├─ 30. sn düşük (CE) ──────────────────────── D3
     └─ 30. sn olağan, gövdede kayıp (CF, CM–CP) ─ D4
Görüntüleme olağan ya da yüksek, ama…
├─ abone gelmiyor ──────────────────────────────── D5
├─ arama rolündeki videoda arama trafiği yok ───── D6
├─ Önerilen trafiği yok ────────────────────────── D7
└─ gelir düşük (para kazanma açıksa) ───────────── D8
```

**D1 — Gösterim yok: paket mi, konu mu?**
- *Kanıt:* (1) Gelişmiş modda videonun gösterimini kaynak kırılımıyla aç. (2) Planlanan kaynakta gösterim (`BR`), CTR (`BS`), pay (`AY`) ve V1 (`BO`). (3) Arama terimleri listesi. (4) Hedef sorguyu YouTube arama kutusuna yaz; otomatik tamamlamada çıkıyor mu. (5) Aynı konu ailesinden (`K`) başka video varsa onun `CD` etiketi.
- *Ayırıcı bulgu:* Aynı kaynakta, aynı yaşta, son 10 videoya göre okunur. Kaynak içi CTR "düşük" (`BA`) **ve** V1 sağlanıyor → **paket hipotezi.** Kaynak içi CTR olağan, o kaynaktaki gösterim düşük, terim listesi boş ve aynı konu ailesindeki öbür video da düşük → **konu/talep hipotezi** (talep az ya da çerçeve izleyicinin dilinde değil). V1 yoksa paket henüz sınanmamıştır, "paket kötü" denemez → B5'in ilk satırı: bekle, pakete dokunma. Günlük gösterimin ilk günlerden sonra azalması hemen her videoda görülür ve iki hipotezi ayırmaz **[Yaygın gözlem]**; yalnızca Gelişmiş mod → Karşılaştır ile aynı roldeki iki videonun günlük eğrisiyle üst üste konduğunda belirgin biçimde erken düşüyorsa not edilir.
- *İyileştirme:* Paket → B5 "CTR düşük" satırları. Konu → aynı görevin izleyici diliyle yazılmış çerçevesini fikir havuzuna al; mevcut videoya dokunma.
- *Test:* Paket hipotezi aynı videoda sınanır (02 B4 elle sıralı test). Karar kuralı: değişiklikten sonraki 7 günde aynı kaynakta V1 sağlanıyor ve CTR farkı iki dönemin paylarının toplamından büyükse "zayıf kanıt, kabul"; değilse "fark gösterilemedi", ikinci değişiklik yapılmaz. Konu hipotezi yeni videoda sınanır (paket kalıbı sabit, çerçeve değişir). Karar kuralı: aynı konu ailesinden yeni çerçeveli 2 videonun 2'sinde `CD` "düşük" değilse çerçeve kabul; biri düşükse "sonuçsuz".

**D2 — CTR düşük**
- *Kanıt:* (1) Kaynak bazında CTR ve V1. (2) Kıyas videosuyla fark `AY` paylarının toplamından büyük mü. (3) Kapağı telefonda, koyu modda, küçük boyutta aç (01 belgesi 3.4). (4) Arama kaynağıysa sorgunun sonuç sayfasının ekran görüntüsü. (5) "Özet" sayfasında kapak çifti türü (`G`) × CTR etiketi (`BA`) çapraz tablosu: "düşük"ler tek bir çift türünde mi toplanıyor.
- *Ayırıcı bulgu:* Yalnızca Göz atma'da düşükse paket soğuk kitleye konuşmuyor; yalnızca aramada düşükse sonuç sayfasında ayrışmıyor; toplamda düşük ama her kaynakta olağansa karışım etkisi (Bölüm 3, kural 5) → müdahale yok. "Düşük" etiketli videoların en az 3'ü aynı kapak çifti türündeyse ve o türde "yüksek" yoksa hipotez tek kapak değil **kalıptır.**
- *İyileştirme ve test:* B5'in ilgili satırı; test B4 (koşul varsa yerleşik, yoksa elle sıralı; önce kapak, sonra başlık), karar kuralı D1'deki paket kuralıdır. Kalıp hipotezi tek videoda sınanmaz: sonraki 3 videoda öbür çift türü kullanılır, en az 2'sinde `BA` "düşük" değilse kalıp değişir (02 B4, 2/3 kuralı).

**D3 — İlk 30 saniyede kayıp**
- *Kanıt:* (1) Grafikte düşüşün en dik olduğu aralığı bul: ilk adım (grafiğin ilk veri noktasına kadar; adım aralığı Bölüm 7'de), ilk adımdan 15. saniyeye, 15–30. saniye. (2) Altyazı dosyasından o aralıktaki cümleleri oku (Bölüm 7). (3) Kaynak bazında AVD: kayıp bir kaynağa mı özgü. (4) Kaynak içi CTR etiketi (`BA`). (5) Tutma raporunda izleyici kesimi seçilebiliyorsa abone / abone olmayan ayrımı **[DOĞRULA]**.
- *Ayırıcı bulgu:* İlk adımda kayıp + CTR "yüksek" → paket–açılış uyumsuzluğu; kontrolü B5'tekidir: başlıktaki vaat ilk 15 saniyede söyleniyor ya da gösteriliyor mu. İlk adımdan 15. saniyeye → ilk cümle görevi söylemiyor. 15–30. saniye → kurulum uzun; sonuç görüntüsü geç geliyor. Kayıp yalnızca Harici kaynaktaysa sorun videoda değil, gönderi metnindedir (02 A6).
- *İyileştirme:* 01 belgesi Bölüm 4 ve 5 (hook ve açılış sahnesi kuralları); B5'in iki "ilk 30 sn" satırı.
- *Test:* FT1 (02 B4): 3 video, 2/3 kuralı, metrik `U`, etiket `CE`.

**D4 — Ortada uçurum ya da sürekli eğim**
- *Kanıt:* Bölüm 7'deki eşleştirme; düşüşün türü (basamak mı, eğim mi, çukur + toparlanma mı); aynı blok türünün önceki videolardaki kaybı (blok kaybı tablosu).
- *Ayırıcı bulgu:* Yalnız bu videoda varsa o ana özgü (bekleme, erken CTA, konu dışı açıklama). Aynı blok türünde 3 videoda tekrar ediyorsa format sorunu.
- *İyileştirme:* Ana özgü → B5 "ortada basamak düşüş" satırı (bölüm başlığı ekle). Format → 01 belgesi 7.5 kontrolüne madde; FT2 / FT3 / FT4.
- *Test:* İlgili FT kartı; metrik o blok türünün dakika başına kaybı (`CM–CP`; toplam APV değil), kendi blok medyanına göre.

**D5 — İzlenme iyi ama abone yok**
- *Kanıt:* (1) V3 ve "olay sayısı ≥ 10" kuralı; sağlanmıyorsa teşhis yapılmaz. (2) Abonelik durumu kırılımı: görüntülemenin ne kadarı zaten abone? Çoğu aboneyse düşük yeni abone doğaldır. (3) Trafik kaynağı: arama kaynaklı izleyici tek seferlik çözüm alır **[Yaygın gözlem]**; `BG` yalnızca aynı roldeki videolarla kıyaslanır. (4) Bitiş ekranı tıklama oranı. (5) Videoda bir sonraki görevin vaadi var mı (01 belgesi 8.2).
- *Ayırıcı bulgu:* Bitiş ekranı tıklaması da düşükse izleyici kanalda kalmıyor → seri bağlantısı eksik. Bitiş ekranı olağan, abone düşükse → abone olma gerekçesi söylenmiyor (02 B7).
- *İyileştirme:* 02 B7 ve B3; mevcut videoda bitiş ekranı hedefi ve sabitlenmiş yorumun "sıradaki adım" bloğu değiştirilebilir.
- *Test:* Asgari veri (V3 ve 10 olay) tek videoda sağlanmıyorsa test açılmaz; soru FT7 sırasına yazılır (performans kaydı §5.2). Sağlanıyorsa FT7; karar kuralı: 3 videonun en az 2'sinde `AT`, aynı roldeki önceki videoların medyanının üstünde (02 B4).

**D6 — Arama trafiği yok**
- *Kanıt:* (1) Video arama rolünde miydi (`L`)? Değilse belirti değil. (2) 28. gün terim listesi. (3) Hedef sorgunun otomatik tamamlamadaki yazımı ile başlıktaki yazım. (4) Gizli pencerede sorguyu ara, sonuç sayfasını kaydet; sıralama kişiye ve konuma göre değişir, tek aramayla hüküm verilmez. (5) Arama trafiği yavaş birikir **[Yaygın gözlem]**; 28. günde yoksa 90. günde bir kez daha bak.
- *Ayırıcı bulgu:* Sorgu otomatik tamamlamada yoksa talep yok (konu). Var ama terim listesinde başka sorgular çıkıyorsa video başka bir niyetle eşleşmiş → başlık/açıklama dili. Aramada gösterim var, CTR düşükse → D2.
- *İyileştirme:* B5 "arama videosu, terim listesi boş" satırı.
- *Test:* Tek değişiklik (başlık yazımı). Karar kuralı: 28 gün sonra terim listesinde hedef sorgu görünüyor **ve** arama kaynaklı gösterim değişiklikten önceki 28 günün üstünde → "zayıf kanıt, kabul"; biri eksikse "sonuçsuz", ikinci değişiklik yapılmaz.

**D7 — Öneri trafiği yok**
- *Kanıt:* (1) Önerilen → kaynağa tıkla: hangi videolar öneriyor, kendi videoların var mı. (2) Videonun aynı sorunu sürdüren bir "kardeşi" yayında mı (02 A7). (3) Bitiş ekranı tıklama oranı. (4) Kanalda 28 günlük verisi olan kaç video var.
- *Ayırıcı bulgu:* İlk 10 videoda Önerilen payının küçük olması beklenen sıradır (02 A6) → teşhis değil, bekleme. Kardeş video varken bile liste boşsa → bağlantı (bitiş ekranı, sözlü geçiş, oynatma listesi) kurulmamış. Liste alakasız videolardan oluşuyorsa hipotez "konu sinyali dağınık"tır **[Yaygın gözlem]** (02 A11); öneri sisteminin neden öyle davrandığı bu veriden çıkarılamaz.
- *İyileştirme:* 02 B3 (seri mimarisi, oturum uzatma); devam videosu.
- *Test:* Devam videosu. Karar kuralı: yayından 28 gün sonra iki video birbirinin Önerilen listesinde görünüyor **ve** "kendi videolarından gelen pay" bir önceki aylık değerin üstünde → bağlantı kuruldu; biri eksikse ikinci devam videosuna kadar hüküm yok.

**D8 — Gelir düşük** (yalnızca para kazanma açıkken)
- *Kanıt:* Yöntem kartı 04 belgesi Kart 1. Gelir = (görüntüleme ÷ 1.000) × RPM. Önce hangisinin düşük olduğunu ayır. RPM düşükse: (1) video bazında RPM sıralaması; (2) görüntülemenin Shorts / uzun video payı (ikisinin RPM'i aynı terazide tartılmaz **[Yaygın gözlem]**); (3) videonun para kazanma simgesi (sınırlı reklam var mı); (4) aynı ayın geçen yılı yoksa önceki üç ay: reklam harcaması dönemseldir **[Yaygın gözlem]**; (5) coğrafya dağılımı; (6) video içi reklam aralarının yerleşimi (uzunluk koşulu ve ayarlar için **[Resmî][DOĞRULA]** [Manage mid-roll ad breaks](https://support.google.com/youtube/answer/6175006)).
- *Ayırıcı bulgu:* RPM bütün videolarda birlikte düştüyse neden dönem ya da kitledir; müdahale yok. Tek videoda düşükse o videonun reklam uygunluğu ya da reklam arası yerleşimi.
- *İyileştirme:* Konuyu RPM'e göre seçme; kanalın vaadi görevdir. Reklam arası otomatik yerleştirildiyse doğal bölüm geçişlerine elle taşı.
- *Test:* Tek videoda, tek değişiklik, önce/sonra 28 gün. Karar kuralı: videonun RPM değişimi aynı dönemde kanal RPM'indeki değişimden büyük **ve** o videonun blok kaybı (`CM–CP`) kötüleşmedi → yerleşim kalır; aksi hâlde geri alınır (reklam arası tutmayı düşürdüyse kazanç yanıltıcıdır). Kanıt zayıftır.

**Teşhis oturumu (20 dk) ve kayıt.** Haftalık rutinin dışında, cumartesi 48 saat bakışının ardından yapılır. (1) 5 dk: dalın "Kanıt" maddelerini Studio'dan topla. (2) 5 dk: ayırıcı bulguyu oku, tek cümle hipotez yaz. (3) 5 dk: isteğe bağlı A3 prompt'u (Bölüm 9). (4) 5 dk: müdahaleyi ve karar kuralını yaz. Kayıt yeri: video kartının "Çıkarım" tablosuna tek satır (`Dal: D[no] · Kanıt: … · Hipotez: … · Hüküm: müdahale / bekle / veri yetersiz`); müdahale yapıldıysa tarihiyle kartın değişiklik günlüğüne; test açıldıysa hipotez kartına (performans kaydı §5.2).

**İşlenmiş örnek (ÖRNEK: sayılar uydurmadır, yalnızca yolu gösterir).** KM-012, arama rolü, planlanan kaynak YouTube araması, 7. gün. Etiketler: `BE` düşük · `CD` düşük · `BA` normal · `CE` normal; KM-011'de de `CD` düşüktü → giriş koşulu sağlandı, dal D1. Kanıt: `BR` 310 (V1 yok) · terim listesinde iki sorgu var, ikisi de başlıktaki yazımdan farklı · hedef sorgu otomatik tamamlamada başka kelime sırasıyla çıkıyor · aynı konu ailesinde başka video yok. Ayırıcı bulgu: V1 yok → paket sınanmamış; terimler başka yazımda → hipotez "başlık izleyicinin yazdığı biçimde değil" (D6'ya geçiş). Hüküm: 7. günde müdahale yok. Karar cümlesi: "KM-012'nin 28. gününde terim listesine bakacağım; hedef sorgu yine yoksa başlığı otomatik tamamlamadaki yazıma çekeceğim; 28 gün sonra arama kaynaklı gösterimin önceki 28 günün üstünde olmasını bekliyorum. Dayanak: KM-012, `BR` 310, terim listesi (ipucu)."

---

## 7. Tutma grafiği analiz yöntemi

Şekil sözlüğü 02 A4'te, yayın sonrası adımlar ve "belirgin düşüş" tanımı 01 belgesi 7.5'tedir. Burada grafiğin senaryoyla nasıl eşleştirileceği ve bulgunun nasıl kurala dönüşeceği yazılı. Ön koşul V2; grafik yoksa hücreye "veri yok" yazılır. **Okuma zamanı:** V2 7. günde sağlanıyorsa 7. gün, sağlanmıyorsa 28. gün (01 belgesi 7.5'teki okumayla aynı oturum). Tabloya giren işaret noktası değerleri (`BV–CB`) her videoda 28. gün değeridir.

**Çözünürlük.** Tutma verisi videonun yaklaşık yüzde birlik dilimleriyle gelir (YouTube Analytics API'de 100 nokta; Studio grafiği için **[DOĞRULA]**): 8–14 dakikalık videoda bir adım yaklaşık 5–8 saniyedir. İlk videoda imleci gezdirerek adım aralığını ölç ve performans kaydı Bölüm 0'a yaz. Eşleştirme cümle düzeyinde değil, **±1 adımlık pencere** düzeyindedir: o penceredeki 2–3 cümlenin hepsi aday yazılır.

1. **Zaman damgalı metni hazırla.** Videonun düzeltilmiş altyazı dosyası (`06_cikti/` içindeki .srt; 03 belgesi Aşama 6) her cümlenin başlangıç saniyesini verir. Dosyayı metin olarak aç; grafikle yan yana koy. Ek hazırlık gerekmez.
2. **Grafiği aç ve imleci gezdir.** Video → Analytics → Etkileşim → tutma grafiği. İmleç her noktada zamanı ve yüzdeyi gösterir. Studio arayüzü eğriyi saniye saniye dışa aktarmaz **[DOĞRULA]**; değerler elle okunur.
3. **Önce dört sabit işaret noktası** (02 A4), sonra **en fazla üç olay** (01 belgesi 7.5 sınırı). Olay sayılmanın alt sınırı **[Tahmini]**: düşüş en az 5 izleyiciye karşılık gelmeli (puan × görüntüleme ÷ 100 ≥ 5; 100 görüntülemede 5 puan, 500 görüntülemede 1 puan). Altındaki düşüş gürültüden ayrılamaz; o videoda yalnızca işaret noktaları yazılır. Her olay için dört şey yaz: başlangıç saniyesi, bitiş saniyesi, baştaki ve sondaki yüzde.
4. **Olayın türünü ölçerek adlandır** **[Tahmini tanımlar]**:

| Tür | Ölçüsü | İlk bakılacak yer |
|---|---|---|
| **Basamak** | En çok 3 adımlık aralıkta, videonun kendi ortalama eğiminin en az üç katı diklikte düşüş | .srt'de o penceredeki cümleler: geçiş cümlesi, CTA, "şimdi…" ile başlayan duyuru |
| **Sürekli eğim** | 1 dakikadan uzun, ortalamadan dik ama basamaksız iniş | Blok bütün olarak: tempo, bekleme, kanıtsız geçen süre (01 belgesi 7.4) |
| **Çukur + toparlanma** | Düşüşten sonra eğri yeniden yükselir | İzleyici ileri sarmış; çukurdaki bölüm atlanabilir bulunmuş |
| **Tümsek** | Eğri yukarı döner | Geri sarma: ekrandaki prompt, tablo ya da hızlı geçilen adım |
| **Düzlük** | Eğim sıfıra yakın, 30 saniyeden uzun (en az 4 adım) | O blokta ne yapıldıysa tekrar edilecek öğedir |
| **Son düşüş** | Son 30–60 saniyede dikleşme | Bitti sinyali veren cümle (02 A4) |

   Ortalama eğim = (0:30'daki yüzde − video sonundan 30 sn önceki yüzde) ÷ aradaki dakika. İlk saniyelerdeki düşüş her videoda vardır; olay sayılmaz, 0:30 değeri olarak kaydedilir.
5. **Blok kaybını oku.** İmza formatın blokları işaret noktalarıyla sınırlıdır: kurulum (0:30 → kronometre başı), görev (kronometre başı → karşılaştırma başı), karşılaştırma (→ "yapamadığı şey" başı), son bölüm (→ video sonundan 30 sn önce). Tabloda `CM–CP` sütunları 28. gün değerlerinden hesaplar; sıra videoda farklıysa (FT3) formül geçersizdir, elle hesapla ve `Not` sütununa yaz:

   `blok kaybı % = (baştaki % − sondaki %) ÷ baştaki % × 100` ve `dakika başına = blok kaybı ÷ blok süresi (dk)`

   Bu, bloğun başındaki ve sonundaki tutma yüzdesi arasındaki göreli farktır; "bloğa girenlerin yüzde kaçı çıktı" **değildir.** Tutma eğrisi bir kohort izlemez: bölüm (chapter) başlığından ya da aramadan o ana gelenler, ileri-geri saranlar ve tekrar izleyenler de sayılır; değer negatif çıkabilir. Bölüm başlığı eklenen videoyu `Not` sütununda işaretle. Dakika başına oran farklı uzunluktaki videoların **aynı blok türünü** kıyaslamayı sağlar (APV bunu yapamaz); blok türleri birbiriyle kıyaslanmaz (Bölüm 5, adım 3-f). Tablo `aylik-degerlendirme.md` Bölüm 3'tedir.
6. **Her olaya tek hipotez, tek satır.** Video kartındaki tutma tablosuna: zaman · tür · seste/ekranda ne vardı · senaryo paragrafının etiketi (yeni / kanıt / geçiş; 01 belgesi 7.5) · olası neden. Neden bir **hipotezdir**; grafik "ne oldu"yu gösterir, "neden"i göstermez.
7. **Bulguyu kural olarak yaz.** Biçim:

```text
KURAL ADAYI [no]: [blok türü]nde [şunu yap / yapma].
Kanıt: KM-0NN [d:ss, tür, kaç puan] · KM-0NN [...] · KM-0NN [...]
Karşı örnek: [aynı öğeyi içerip düşüş olmayan video; yoksa "yok"]
Durum: ipucu (1–2 video) / bulgu (3 video) → işlendiği yer: [01 belgesi 7.5 maddesi / senaryo şablonundaki tutma notu]
```

   İpucu video kartında kalır. Üç videoda tekrar eden ve karşı örneği olmayan aday performans kaydı §5.1'e "bulgu" olarak geçer; ancak o zaman 01 belgesi 7.5'teki kontrol listesine ya da `senaryo-sablonu.md` içindeki tutma notlarına madde olarak eklenir. Karşı örnek satırı zorunludur: aynı cümle türü başka videoda düşüş yaratmadıysa neden cümle değil, o videodaki başka bir şeydir.
8. **Bir sonraki senaryoyu yazmadan önce** §5.1'i ve son üç kartın kural adaylarını oku (01 belgesi 7.5, adım 4 ile aynı kural).

---

## 8. Çeyreklik strateji değerlendirmesi (tahmini 3 saat)

02 B1 aşama geçişini takvime değil veri yeterliliğine bağlar; çeyreklik oturum da öyle: yaklaşık 13 haftada bir, ama en yakın **aşama kapısına** denk getirilir. İlk üçü: KM-010'un 28. günü dolduğunda (Aşama 1 çıkışı), KM-020'nin 28. günü dolduğunda (kategori kararı, 02 B1 Aşama 2b), KM-030 dolaylarında (Aşama 3'e geçiş). O ayın aylık oturumu çeyrekliğin ilk 90 dakikasıdır; takvimdeki yeri Bölüm 5'in başındadır.

| Konu | Soru | Veri | Karar kuralı |
|---|---|---|---|
| **Kategori portföyü** | Hangi kategori kanalı taşıyor, hangisi denenmemiş? | Kategori başına: video sayısı, `BF` ve `BG` medyanı, en düşük–en yüksek değer, karşılaştırmaya ulaşan % | 02 B4 "kaç videoda karar verilir" tablosu. Üretim payları 02 B1'deki aşama dağılımına göre |
| **Seri kararları** | Hangi seri sürer, hangisi kapanır, yenisi açılır mı? | Seri (oynatma listesi) grubu: bitiş ekranı tıklaması (`AT`), Önerilen'de kendi videolarının payı; `BK` yalnızca ölçüm varsa | Seri ancak 3 videodan sonra değerlendirilir. Kapatma: 3 videoda geçiş göstergeleri alt üçte birde ve yorum/arama teriminde talep izi yok |
| **Konumlandırma** | Kanalı izleyen kişi, hedeflediğim kişi mi? | Kitle kartları (yaş, coğrafya); yorumlarda anılan meslek ve görevler (video kartları); arama terimleri; izleyicinin izlediği diğer kanallar | Hedefle gerçek ayrışıyorsa önce **paketi ve konuyu** hedefe çek; nişi değiştirme kararı 30 videodan önce verilmez (02 B1) |
| **Format** | İmza formatın hangi bloğu geriliyor? | Her blok türünün (`CM–CP`) çeyrek medyanı ↔ kendi önceki çeyrek medyanı; blok türleri birbiriyle kıyaslanmaz | Önceki çeyreğine göre kötüleşen ya da medyandan sapan videosu en çok olan blok için sıradaki FT testi |
| **Hedef metrikler** | Bu aşamanın odak metriği doğru mu, hedefi ne? | 02 B1'deki aşama odak metrikleri | Aşağıda |
| **Eşikler** | V1–V4 ve bu belgedeki tahmini eşikler kanalın hacmine uyuyor mu? | Son çeyrekte kaç videonun 7. günde V1/V2'yi sağladığı | Videoların yarısından azı 7. günde sağlıyorsa okuma noktası 28. gün olarak kalır; eşik düşürülmez (02 B5) |
| **Sistem maliyeti** | Analiz süreleri tutuyor mu? | Haftalık rutinin gerçek süresi (kart, "Analiz" satırı) | 30 dakikayı düzenli aşıyorsa sütun azalt; süreyi uzatma |

**Hedeflerin yeniden belirlenmesi** **[Tahmini yöntem]:** Dışarıdan kıyas kullanılmaz. En fazla iki metrik seçilir ve yalnızca **ham oran** sütunlarından: 30. sn'de kalan % (`U`), karşılaştırmaya ulaşan % (`AD`), 1.000 görüntüleme başına abone (`BG`). Görüntüleme ve `÷ medyan` sütunları hedef olmaz: ilki kanal büyüdükçe kendiliğinden artar, ikincisi kayan medyana bölündüğü için yapı gereği 1 dolayında kalır. Hedef nokta değil **yön ve alt sınırdır:** "bu çeyreğin medyanı geçen çeyreğin medyanının üstünde ve 13 videonun en az 8'i eski medyanı geçiyor". Hiçbir şey değişmese de bu koşul yaklaşık 10'da 3 olasılıkla tutar; yön göstergesidir, kanıt değil. Tutmazsa hedef düşürülmez; o metriğin bağlı olduğu blok için FT testi öne alınır.

**"Kanıt yeterli mi" ölçütü.** Stratejik bir karar (kategoriye ağırlık, seri kapatma, format değişikliği) ancak beş sorunun hepsine "evet" denirse verilir; biri "hayır" ise karar ertelenir ve eksik kanıtı üretecek video plana yazılır.

1. Her grupta en az 3 video (kategori medyanı karar tablosunda kullanılacaksa 5) var mı?
2. O videoların her birinde ilgili metriğin asgari verisi (V1–V4, olay sayısı ≥ 10) sağlanmış mı?
3. Format testiyse: 3 videonun en az 2'sinde beklenen yönde mi (02 B4)? Grup kıyasıysa: grupların değer aralıkları ayrık mı ve karşılaştırma oturumdan önce yönüyle yazılmış mıydı (Bölüm 3, kural 11)?
4. Çapraz kontrol yapıldı mı; fark başka bir etiketle, mevsimle ya da kanalın büyüme eğilimiyle açıklanamıyor mu?
5. Karar geri alınabilir mi? Alınamıyorsa (niş, kapak kalıbının toptan değişmesi) 02 B4'teki daha yüksek eşik (30+ video, 5 kazananı belli test) aranır.

Çıktı tek sayfadır: portföy tablosu, en fazla üç stratejik karar (her biri beş sorunun cevabıyla), iki hedef metrik, "bu çeyrekte bilerek yapmayacaklarım" satırı. Performans kaydı §5.1 ve §5.2 güncellenir.

---

## 9. Yapay zekâ destekli analiz

**Ne zaman:** Haftalık özet prompt'u rutinin dışında, isteğe bağlıdır; 30 dakikayı uzatmaz. Kalıp bulma prompt'u aylık oturumun 3. adımından **sonra**, kendi tablonla karşılaştırmak için kullanılır. Tek videonun **yorumu** kütüphanedeki **P10**'un işidir; A1 yorum yapmaz, iki videonun tablo satırını okur ve Studio'da bakılacak yerleri listeler. Yorum özetleri için **P9**.

**Beş kural** (`prompt-kutuphanesi.md` ortak kurallarına ek):

1. Her sohbet yeni açılır ve önce **P0** yapıştırılır.
2. **Hesabı tablo yapar, asistan okur.** Medyan, oran ve sıralama elektronik tabloda hesaplanıp yapıştırılır (kütüphane ortak kural 5: asistana saydırma). Asistanın verdiği her sayı, yapıştırdığın tabloda aynen bulunmalıdır; bulunmuyorsa çıktıyı kullanma.
3. **Asistan neden bilmez.** Elindeki tek şey senin yapıştırdığın sayılardır; videoyu izlemedi, izleyiciyi tanımıyor, YouTube'un iç işleyişini görmüyor. Çıktıdaki her "çünkü" bir hipotezdir ve ancak Bölüm 6'daki kanıt adımıyla ya da 02 B4'teki testle doğrulanır.
4. Yapıştırdığın veride izleyiciye ait kişisel bilgi (kullanıcı adı, e-posta) olmaz. Çıktı performans kaydına **senin cümlenle** ve "yapay zekâ önerisi, sınanmadı" notuyla girer.
5. **Az sütun, dikey yapıştır.** 95 sütunlu satır yapıştırılmaz; geniş satırda sütun kayması olağan hatadır. Her prompt'un istediği sütunlar `sütun adı: değer` biçiminde alt alta verilir.

### A1 — Haftalık özet

```text
Aşağıda YouTube kanalımın analiz tablosundan satırlar var. Görevin tabloyu OKUMAK; neden açıklamak değil.

SÜTUN AÇIKLAMASI: "7g" = yayından sonraki ilk 7 gün, "28g" = ilk 28 gün. "Üçte bir" sütunları videonun kanalın son 10 videosu içindeki yerini verir: düşük / normal / yüksek. "÷ medyan" sütunları, değerin kendinden önceki en fazla 10 videonun medyanına oranıdır (1,00 = medyan); yalnızca farkın büyüklüğünü gösterir. Ondalık ayırıcı virgüldür. Boş = henüz bakılmadı ya da kıyas kümesi yok. "test", "[ölçüm yok]", "[yok]" = sayı değil; hesaba katma.
ASGARİ VERİ KURALLARIM: CTR yalnızca "V1" = E ise (planlanan kaynakta gösterim 1.000 ve üstü) yorumlanır; toplam gösterime bakma. "V2" = H ise tutma ve izlenme süresi, "V3" = H ise abone oranı yorumlanmaz.

Her video için yalnızca şu sütunları, "sütun adı: değer" biçiminde alt alta veriyorum: No, Kat., Rol, Planlanan birincil kaynak, Gerçekleşen birincil kaynak, 7g ham değerler, Plan. kaynak gösterim ve CTR, üçte bir sütunları, ÷ medyan sütunları, V1–V3.
BU HAFTA 7. GÜNÜ DOLAN VİDEO: [SÜTUNLAR]
BU HAFTA 28. GÜNÜ DOLAN VİDEO: [SÜTUNLAR]
SÜREN TEST / DENEME: [VAR: ne, hangi videolarda / YOK]

İSTEDİĞİM ÇIKTI:
1. OKUNABİLİRLİK: Her iki video için hangi metrikler asgari veriyi sağlıyor, hangileri sağlamıyor? Sağlamayanları sonraki maddelerde hiç kullanma.
2. ETİKETLER: Okunabilir metriklerden hangilerinin üçte bir etiketi "düşük" ya da "yüksek"? Yalnızca tablodaki değerleri aktar: "[sütun adı]: [etiket] ([÷ medyan değeri])". Yoksa "düşük ya da yüksek etiket yok" yaz.
3. ZİNCİR: Gösterim → planlanan kaynakta CTR → 30. saniye → ortalama görüntüleme süresi sırasında ilk "düşük" halka hangisi?
4. PLAN–GERÇEK: 28 günlük videoda planlanan birincil kaynak ile gerçekleşen aynı mı?
5. BAKMAM GEREKEN ÜÇ ŞEY: Bu tabloyla cevaplanamayan ama Studio'da kontrol edebileceğim en fazla üç soru. Her biri "şu ekranda şuna bak" biçiminde.
6. KARARDAN ÖNCE TEK HÜCRE: Kararımı vermeden önce bakmam gereken tek hücreyi ya da ekranı söyle. Karar ya da müdahale önerme; kararı ben vereceğim.

KURALLAR:
- Tabloda olmayan hiçbir sayı yazma; hesap yapma, yuvarlama yapma.
- "Çünkü", "nedeniyle", "sayesinde" kullanma. Bir neden öne süreceksen "HİPOTEZ:" diye başlat ve hangi veriyle sınanacağını yaz.
- Sektör ortalaması, "iyi CTR" eşiği ya da başka kanallarla kıyas yazma.
- YouTube'un öneri sisteminin ne yaptığı hakkında iddiada bulunma.
- Tek videodan çıkan şeye "ipucu" de.
```

### A2 — Kalıp bulma

```text
Aşağıda kanalımın analiz tablosu (video başına bir satır) ve benim hesapladığım grup medyanları var. Görevin benim göremediğim örüntü ADAYLARINI ve benim çıkarımlarımdaki zayıf noktaları bulmak.

TABLO (28 günlük verisi olan bütün videolar; yalnızca No + etiket sütunları + sonuç sütunları; ondalık ayırıcı virgül): [TABLO]
BENİM HESAPLADIĞIM GRUP TABLOSU (etiket | değer | taşıyan / taşımayan | video sayısı | medyan | en düşük | en yüksek; her değer için iki satır): [GRUP TABLOSU]
BENİM ÇAPRAZ TABLOM (etiket değeri × etiket değeri | birlikte kaç video): [ÇAPRAZ TABLO]
OTURUMDAN ÖNCE YAZDIĞIM KARŞILAŞTIRMALAR (yönüyle): [EN FAZLA 3 ya da "yok"] · BAKTIĞIM ÇİFT SAYISI: [ÇİFT]
BENİM ŞU ANKİ ÇIKARIMIM: [1–3 CÜMLE ya da "henüz yok"]
ETİKET SÜTUNLARI: Kat., Rol ve bu ayın etiketi: [ ].
SONUÇ SÜTUNLARI: Görüntüleme ÷ medyan 28g · Karşılaştırmaya ulaşan % 28g · 1000 gör. başına abone 28g · Prompt tıkl. / 1000 gör. 28g.

İSTEDİĞİM ÇIKTI:
1. YAPIŞIK ETİKETLER: Verdiğim çapraz tabloda, bir etiket değerinin bütün videoları tek bir başka değerle birlikte gelen çiftleri listele (kendin sayma; tablodaki sayıları kullan). Bunlar birbirinden ayrıştırılamaz; sonraki maddelerde tek etiket gibi ele al.
2. ÖRÜNTÜ ADAYLARI (en fazla 5): Her biri için: etiket değeri | sonuç sütunu | taşıyanların en düşük–en yüksek değeri | taşımayanların en düşük–en yüksek değeri (ikisi de grup tablosundan aynen) | aralıklar çakışıyor mu (EVET/HAYIR) | ÖN KAYITLI ya da TARAMA.
   Aday sayılma koşulu: her iki grupta en az 3 video VE aralıklar çakışmıyor. Koşulu sağlamayan hiçbir şeyi aday olarak yazma; "koşulu sağlayan örüntü yok" demek geçerli bir cevaptır. Oturumdan önce yazdığım karşılaştırmalar dışındaki her adayı TARAMA diye etiketle.
3. ALTERNATİF AÇIKLAMALAR: Her aday için, etiketin kendisi dışında farkı açıklayabilecek en az iki şey (yayın sırası / kanalın büyümesi, konu ailesi, süre, yapışık etiket, tatil haftası). Hangisinin daha olası olduğuna karar verme.
4. AYRIŞTIRAN VİDEO: Her aday için, adayı alternatif açıklamadan ayıracak tek bir video tarifi: hangi etiket sabit kalır, hangisi değişir, hangi sonuç sütununa bakılır.
5. ÇIKARIMIMIN ELEŞTİRİSİ: Yazdığım çıkarım tabloyla çelişiyor mu, koşulu sağlamayan gruba mı dayanıyor? Karşı örnek olan videoları numarasıyla yaz.
6. TABLODA EKSİK OLAN: Bu soruları cevaplamak için gereken ama tabloda bulunmayan en fazla üç bilgi.

KURALLAR:
- Kendin medyan, ortalama ya da yüzde hesaplama; yalnızca verdiğim grup tablosundaki sayıları ve tablodaki ham değerleri kullan. Bir hesaba ihtiyaç duyarsan "ŞUNU HESAPLA:" diye bana iş olarak yaz.
- Her iddianın yanında dayandığı video numaraları olsun. Numarasız iddia yazma.
- "X, Y'yi artırıyor / düşürüyor / sağlıyor" gibi nedensellik bildiren cümle kurma. Kalıp: "X etiketli videolarda Y daha yüksek gözlendi (n = …); neden bilinmiyor."
- "Çoğu", "genellikle", "belirgin" gibi oran sözcükleri kullanma; sayıyı yaz.
- Toplam video sayısı [N]; bu küçük bir örnektir. Çıktının ilk satırı şu olsun: "Bu çıktı [N] videoya dayanır; her madde sınanmamış adaydır."
- Yönü önceden yazılmamış bir karşılaştırmada 3'e 3 videoda aralıkların ayrık çıkması 10 çiftten 1'inde tesadüfen olur; baktığım çift sayısına göre kaç TARAMA adayının tesadüf olabileceğini ilk satırın altına yaz. TARAMA adayına "ipucu" deme; "yeni videolarda tekrar ederse ipucu olur" yaz.
- Başka kanallardan, genel YouTube tavsiyelerinden ya da sektör verisinden hiçbir şey ekleme.
```

### A3 — Teşhis (karşı görüş)

P10 tek videoyu yorumlar. Bu prompt, Bölüm 6'da kanıtını topladığın bir teşhisi **çürütmeye çalışır**; müdahaleden önce son kontroldür.

```text
Bir YouTube videosunun düşük performansı için teşhis koydum. Görevin teşhisimi çürütmeye çalışmak; onaylamak değil.

VİDEO: [KM-NO · BAŞLIK] · Kategori: [ ] · Kurgu: [ ] · Rol: [ ] · Süre: [ ] · Yayından beri: [7 / 28] gün
BELİRTİ: [ör. "Gösterim ÷ medyan 7g = 0,41; CTR ÷ medyan = 1,05"]
TOPLADIĞIM KANIT (her satır: ne baktım → ne gördüm):
[KANIT 1]
[KANIT 2]
[KANIT 3]
KAYNAK BAZINDA TABLO (kaynak | gösterim | CTR | görüntüleme | ort. gör. süresi): [TABLO]
TUTMA GÖZLEMLERİM (zaman → tür → o anda seste/ekranda ne vardı): [GÖZLEMLER ya da "grafik yok"]
AYNI YAŞTAKİ KIYAS VİDEOLARI (satırlar): [SATIRLAR]
TEŞHİSİM: [tek cümle]
PLANLADIĞIM MÜDAHALE: [tek değişken] · NASIL SINAYACAĞIM: [metrik, süre]

İSTEDİĞİM ÇIKTI:
1. VERİ YETERLİ Mİ: Teşhisin dayandığı her metrik için asgari veri sağlanmış mı (CTR için o kaynakta 1.000 gösterim; tutma için 100 görüntüleme; abone oranı için 300 görüntüleme ve en az 10 abone)? Sağlanmayan varsa teşhisin o kısmını "okunmaz" say ve bunu ilk satırda söyle.
2. KANIT–TEŞHİS BAĞI: Her kanıt satırı için: teşhisi destekliyor / desteklemiyor / ilgisiz. Gerekçeyi yalnızca verdiğim sayılardan kur.
3. RAKİP AÇIKLAMALAR: Aynı belirtiyi üretebilecek, benim teşhisimden farklı en fazla üç açıklama. Her biri için: verdiğim kanıtla çelişiyor mu, çelişmiyorsa onu benim teşhisimden ayıracak TEK ek gözlem nedir ve nerede bakılır.
4. EN UCUZ AYIRICI KONTROL: Müdahaleden önce 10 dakikada yapabileceğim, teşhisimi en çok güçlendirecek ya da çürütecek tek kontrol.
5. MÜDAHALE DENETİMİ: Planladığım müdahale gerçekten tek değişken mi? Sınama planım teşhisi rakip açıklamalardan ayırır mı, yoksa hangisi doğru olursa olsun aynı sonucu mu verir?
6. HÜKÜM: Şu üçünden biri: "müdahale et" / "önce 4. maddedeki kontrolü yap" / "veri yetersiz, 28. günü bekle". Tek cümle gerekçe.

KURALLAR:
- Bana katılmak zorunda değilsin; teşhisi destekleyen kanıt zayıfsa açıkça söyle.
- Verdiğim kanıtta olmayan bir olguyu varsayma (ör. "kapak muhtemelen okunmuyor"). Bilmediğin şeyi 3. maddede "bakılması gereken" olarak yaz.
- YouTube'un sistemi hakkında kesin cümle kurma; "cezalandırdı", "öne çıkardı", "algoritma sevmedi" gibi ifadeler yasak.
- Genel YouTube tavsiyesi, sektör ortalaması, "iyi CTR" eşiği yazma.
- Sayı üretme; yalnızca verdiklerimi kullan.
```

---

## 10. İlk 10 video için analiz takvimi

Hafta numarası = o perşembe yayınlanan video (1. hafta KM-001). Bir videonun 7. günü bir sonraki, 28. günü dört sonraki haftada dolar. Takvim 02 B1 Aşama 1 ve B5 kıyas merdiveniyle aynıdır; burada haftaya dökülmüş hâlidir.

| Hafta | Elde olan veri | Bakılır | Bakılmaz / yapılmaz |
|---|---|---|---|
| **1** | KM-001 yayında | Teknik kontrol (02 B5 "1. saat"); cumartesi 48 saat: gösterim geliyor mu, 0:30. Etiketleri (A–O) yaz | CTR, abone, gerçek zamanlı kart, günlük Studio kontrolü |
| **2–4** | 1–3 videonun 7. günü | Sayıları gir. Tutma grafiği varsa 0:30 ve üç işaret noktası; alt sınırı geçen olay varsa en fazla üçü (Bölüm 7). Arama terimleri, yorumlar. Üretim süresi (kart). Ön ↔ kesin değer farkını not et | Videolar arası kıyas; "düşük/yüksek" etiketi; paket değişikliği (yalnız açık hata) |
| **5** | KM-001'in 28. günü; ilk aylık oturum (kısa sürüm; Bölüm 5) | İlk 28g satırı; planlanan ↔ gerçekleşen kaynak; `BL` kuyruk oranı | Kategori kıyası; grup medyanı; izleyici türü kartlarından sonuç |
| **6** | 5 videonun 7. günü | Aynı. `÷ medyan` ve üçte bir sütunları gelecek hafta dolmaya başlar | — |
| **7** | KM-006'nın 7. günü: **ilk kanal içi kıyas** (2. basamak) | `CD`, `CE`, `CF`, `BE` etiketleri (`BA` aynı kaynakta 6 video birikince); zincirde ilk "düşük" halka. Giriş koşulu ve asgari veri varsa karar tablosuna göre tek müdahale | Kategori bazında kıyas (hiçbir kategoride 5 video yok); yerleşik test |
| **8–9** | 7–8 videonun 7. günü, 4–5 videonun 28. günü | 9. haftada ikinci aylık oturum (kısa sürüm; tutma grafiği olan 3+ video varsa blok kaybı tablosunun ilk hâli) | Uç grup kıyası (yeterli video yok) |
| **10** | KM-010 yayında; KM-006'nın 28. günü → 6 videoda 28g; `BF` ilk kez dolar | Aşama 1 çıkış koşulu sağlandı mı (02 B1). G için 28g grup medyanı **yazılır** (n = 3: KM-002, 005, 006); karar için kullanılmaz. B için 7g medyanı 11., 28g medyanı 14. haftada | K, M, P hakkında hüküm (birer video); İ (hiç video yok) |
| **11–13** | Kalan videoların 28. günü | Haftalık rutin sürer | — |
| **14** | KM-010'un 28. günü; `CL` dolar, `BF` yalnızca 5 videoda | **İlk tam aylık oturum (90 dk) + ilk çeyreklik oturum.** Portföy ve blok kaybı 10 videoyla: "format çalışıyor mu". Uç gruplar `CL` ile üçte bir olarak; sonuç yalnızca "izle" | Niş ya da kapak kalıbı değişikliği; kategori durdurma; "ayrıştırıyor" hükmü |
| **18** | `BF` dolu 9 video (KM-006–014) | Kalıp bulma ilk kez `BF` ile; ön kayıtlı karşılaştırmalar | "Ayrıştırıyor" hükmü (20 videodan önce yok) |

**Veri azken işe yarayan dört şey** (hepsi örneklem eşiğine takılmaz):

1. **Tutma grafiğinin şekli.** Yüzdelerin kendisi oynaktır ama aynı blokta aynı türde düşüşün iki üç videoda tekrar etmesi, CTR'den çok daha erken okunur. Grafik hiç çıkmıyorsa "veri yok" yazılır.
2. **Arama terimleri ve yorumlardaki cümleler.** Sayı değil dil verisidir; tek bir sorgu bile başlık yazımını düzeltir.
3. **Plan–gerçek uyumu.** Rol tahminin tutuyor mu; yön bilgisi yeter.
4. **Kendi üretim verin.** Aşama süreleri ilk videodan itibaren tam ölçülür ve hiçbir eşiğe bağlı değildir (performans kaydı, video kartı).

**Grafik de yoksa:** hedef kitleden iki kişiye videoyu izlet; nerede telefona uzandıklarını ya da ileri sardıklarını zaman damgasıyla not etmelerini iste. Bu **veri değildir**, iki kişilik gözlemdir; video kartına "izleyici gözlemi (n = 2)" diye yazılır ve yalnızca senaryo kontrolüne (01 belgesi 7.5) girdi olur.

**İlk 10 videoda hiç bakılmayanlar:** abone sayısı ve toplam görüntüleme (02 B1: odak değil), düzenli izleyici sayısı (tanım gereği sıfır; 02 A5), yayın saati denemeleri (02 B9), Studio'nun "tipik performans" kıyası tek başına (bütün YouTube'a göredir; 02 A4), başka kanalların herkese açık sayıları (02 A3), RPM.

---

## Doğrulanacaklar (ilk Studio oturumunda, 02 belgesindeki listeye ek)

1. Gelişmiş mod: "Karşılaştır" menüsünde yayından sonraki aynı süreye göre hizalama seçenekleri var mı; grup oluşturma nerede; dışa aktarma biçimleri ve satır sınırı → [9717005](https://support.google.com/youtube/answer/9717005)
2. Kanal düzeyi Analytics sekmeleri: kanal geneli trafik kaynağı ve arama terimi raporunun yeri (Gelişmiş mod → Trafik kaynağı; İçerik sekmesindeki kart)
3. Video düzeyinde tarih seçicide "İlk 24 saat / İlk 7 gün / İlk 28 gün" hazır aralıkları var mı; Studio verisinin gecikmesi (ilk üç videoda ön ↔ kesin değer farkı)
4. Tutma grafiğinin adım aralığı (video süresi ÷ 100 mü); raporda izleyici kesimi (abone / abone olmayan, yeni / geri dönen) seçilebiliyor mu; eğri dışa aktarılabiliyor mu → [9314415](https://support.google.com/youtube/answer/9314415)
5. Gelişmiş modda "Abonelik durumu", "Abonelik kaynağı" ve "Cihaz türü" boyutlarının Türkçe adları; video düzeyinde "geri dönen izleyici" satırı var mı (02 belgesi Ek, madde 3)
6. Kitle sekmesinde "kitlenizin izlediği kanallar / videolar" kartları bu kanal büyüklüğünde görünüyor mu
7. Kazanç sekmesinde İş Ortağı Programı eşiklerine ilerleme göstergesi; RPM ve oynatma başına BGBM tanımlarının tam metni → [9314357](https://support.google.com/youtube/answer/9314357); video içi reklam arası koşulu → [6175006](https://support.google.com/youtube/answer/6175006). Dört bağlantının doğru sayfaya gittiği de teyit edilmedi
8. Türkçe işlev adları ve CSV'nin kendi bölge ayarında doğru açıldığı (ondalık virgül, noktalı virgül ayırıcı, Türkçe karakterler): kurulumun 2. adımındaki sınama; `TOPLA.ÇARPIM`, `FİLTRE`, `HİPERGEOM.DAĞ` adları sürüme göre değişebilir

## Diğer belgelerde gereken güncellemeler

Bu belge aşağıdaki dosyalara dokunmaz; uyum için sahiplerinin işlemesi gerekir.

- **`README.md`:** belge dizinine 05 belgesi, `analiz-tablosu.csv` ve `aylik-degerlendirme.md`; "tek kaynak" tablosuna "analiz tablosunun sütunları ve formülleri → 05 belgesi Bölüm 2" ve "7g / 28g tanımı → 05 belgesi Bölüm 1" satırları.
- **`sablonlar/performans-kaydi.md`:** kullanım notundaki "kanalın tek takip şablonu budur" cümlesi; §1, §2 sayılarının ve karttaki "Metrikler" tablosunun 7 gün / 28 gün sütunlarının analiz tablosunda tutulduğu, §5.3 kategori tablosunun "Özet" sayfasıyla karşılandığı notu; Bölüm 0'a "tutma grafiği adım aralığı" satırı.
- **`02-buyume-stratejisi.md`:** B8'deki "tek şablon" cümlesi ve kanal düzeyi "Erişim → YouTube araması" yolu; B5 ve B8'de 7. gün okumasının ön değer olduğu; B2'deki haftalık toplam süreye aylık +70 dk, çeyreklik +3 saat ve teşhis oturumu (03 belgesi 2.1 ile birlikte).
- **`01-icerik-uretim-sistemi.md` 7.5:** olay sayılmanın izleyici alt sınırı ve eşleştirmenin pencere düzeyinde yapıldığı.
