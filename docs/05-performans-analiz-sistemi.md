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

**Doğrulama durumu:** YouTube Yardım sayfaları (support.google.com) bu belge yazılırken de açılamadı; resmî sayfaların varlığı ve başlıkları yalnızca arama sonuçlarından görüldü. Bu yüzden **[Resmî]** etiketli her Studio özelliği ayrıca **[DOĞRULA]** taşır (02 belgesindeki "[Resmî — sayfada teyit et]" ile aynı anlam). Studio'daki sekme ve düğme adları Türkçe arayüzde beklenen karşılıklardır; birebir bulamazsan aynı kavramı ara (02 belgesi Ek, madde 12). Bu belgedeki bütün sayısal eşikler **[Tahmini]**dir; YouTube'un açıkladığı sınırlar değildir.

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
| 7. gün değerleri | Video → Analytics, tarih aralığı "Yayınlandığından beri" | Perşembe (yayın + 7) | Analiz tablosu P–X; video kartı | Haftanın tek kararı |
| 28. gün değerleri, trafik payları, arama terimleri | Aynı; Erişim → Trafik kaynağı türleri | Perşembe (yayın + 28) | Analiz tablosu Y–AW; video kartı | Kart kapanışı; aylık analiz |
| Tutma grafiği, işaret noktaları | Video → Analytics → Etkileşim | 7. gün (V2 varsa), 28. gün | Video kartı "Tutma grafiği" | Bir sonraki senaryo (Bölüm 7) |
| Arama terimleri, yorumlar | Erişim → YouTube araması; Yorumlar | Haftalık | `fikir-havuzu.md` (en fazla 3 satır) | Konu seçimi |
| Kanal tabanı, izleyici türleri, kitle kartları | Analytics → Genel Bakış; Kitle | Aylık | `aylik-degerlendirme.md`; performans kaydı §5.3 | Sürdür / durdur / dene |
| Toplu sağlama | Gelişmiş mod → dışa aktarma | Aylık, 10 dk | Ayrı sayfa ("ham"); elle girilenle karşılaştırılır | Veri temizliği |
| Prompt tıklaması | Kısa bağlantı aracının paneli (performans kaydı Bölüm 0) | 7. ve 28. gün | Analiz tablosu X, AU | Prompt'un değeri; bülten eşiği |
| Gelir, RPM | Analytics → Gelir (yalnızca para kazanma açıldıktan sonra) | Aylık | Analiz tablosu AV–AW | Bölüm 6, D8 |

**Studio'nun üç aracı ve ne için kullanılacağı:**

- **Gelişmiş mod.** Herhangi bir rapor kartının altındaki "Daha fazla göster" ya da sağ üstteki "Gelişmiş mod" ile açılır; boyut (video, trafik kaynağı, coğrafya, abonelik durumu, tarih…) ve metrik seçilir. **[Resmî][DOĞRULA]** [Learn how to use Advanced mode for analytics reports](https://support.google.com/youtube/answer/9717005). Kullanım: bir videonun kaynak bazında gösterim/CTR/AVD tablosu; kaynağa tıklayarak arama terimleri ve öneren videolar.
- **Karşılaştırma.** Gelişmiş modda "Karşılaştır": iki video, iki grup ya da iki dönem yan yana gelir **[Resmî][DOĞRULA]** (aynı sayfa). Karşılaştırma menüsünde videoları yayından sonraki aynı süreye göre (ilk 24 saat / 7 gün / 28 gün) hizalayan seçenekler olup olmadığı doğrulanamadı **[DOĞRULA]**; varsa "aynı yaşta kıyas" kuralını tek tıkla sağlar, yoksa tarih aralığını elle yayın tarihine göre kur.
- **Gruplar.** Gelişmiş modda videolardan grup oluşturulabiliyor **[Resmî][DOĞRULA]** (aynı sayfa). Her kategori (B, G, K, M, İ, P) ve her seri için bir grup aç; aylık değerlendirmede kategori toplamı tek seçimle gelir.
- **Dışa aktarma.** Gelişmiş modda üstteki indirme düğmesi → "Geçerli görünümü dışa aktar" → Google E-Tablolar ya da .csv **[Resmî][DOĞRULA]** (aynı sayfa; biçim seçenekleri ikincil kaynaklardan). Satır sınırı olduğu ikincil kaynaklarda yazıyor; bu kanalın video sayısında sorun olmaz.

**Dışa aktarmanın yapamadığı şey:** Dışa aktarılan tablo, seçili **takvim aralığının** toplamıdır; "her videonun kendi ilk 7 günü" tek tabloda gelmez. Bu yüzden 7. ve 28. gün değerleri her perşembe elle okunur (haftada iki video: 7. gün için 9, 28. gün için en fazla 25 hücre). Perşembeyi kaçırırsan: Video → Analytics → tarih seçici → özel aralık → yayın günü ile yayın + 7 (ya da + 28). Studio verisi son bir iki gün için eksik gelebilir **[Yaygın gözlem]**; her videoyu aynı anda (yayın + 7, perşembe rutini) okursan bu eksiklik bütün videolarda aynı yönde olur ve kıyası bozmaz.

---

## 2. Veri modeli: `analiz-tablosu.csv`

### 2.1 Performans kaydıyla ilişkisi

`performans-kaydi.md` kendi kullanım notunda tabloların büyüyünce "aynı sütunlarla bir elektronik tabloya" taşınmasını ister. `analiz-tablosu.csv` o tablodur: performans kaydının **§1 (7. gün özeti)** ve **§2 (28. gün trafik payları)** tabloları ile video kartındaki kimlik alanlarının tek satırda birleşmiş hâli. İkinci bir takip şablonu değildir.

| Ne | Nerede tutulur |
|---|---|
| Sayılar ve etiketler (video başına bir satır) | `03_KAYITLAR/analiz-tablosu` (elektronik tablo) — §1 ve §2'nin yerine; iki yere birden yazma |
| Tutma grafiği notları, yorumlar, değişiklik günlüğü, çıkarım, üretim süresi | `03_KAYITLAR/performans-kaydi.md` video kartı (değişmez) |
| Bulgular, açık sorular, aylık bakış (§5) | `performans-kaydi.md` §5; aylık oturumun çalışma kâğıdı `aylik-degerlendirme.md` |

Sütun adları performans kaydındaki adlarla aynıdır; tek fark dönem ekidir (`7g`, `28g`). Özel değerler de aynıdır: `test` (yerleşik test süren videonun CTR'si; 02 B4), `[ölçüm yok]` (yöntem kurulmamış; 0 yazılmaz), `[yok]` (özellik kanalda yok, ör. gelir). Formüller metin hücreleri kendiliğinden dışarıda bırakır.

**Kurulum (bir kez, 15 dk):** CSV noktalı virgülle ayrılmış, ondalık ayırıcısı virgül, UTF-8'dir. Türkçe bölge ayarlı Excel doğrudan açar. Google E-Tablolar'da önce Dosya → Ayarlar → Yerel ayar: Türkiye, sonra Dosya → İçe aktar **[DOĞRULA]**. İki örnek satırı sil, 2.3'teki formülleri 2. satıra yapıştır ve aşağı doğru doldur. Süreler saniye olarak girilir (9 dk 45 sn = 585); yüzdeler yüzde işareti olmadan (4,6).

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

**Grup 2 — Performans metrikleri (P–AW).** Tanımlar 02 belgesi Bölüm A'da; burada yalnızca hangi kontrolde doldurulduğu yazılı. Asgari doldurma kuralı (02 B8) geçerlidir: boş hücre "bakılmadı" demektir, sıfır değil.

| Sütun | Ad | Ne zaman |
|---|---|---|
| P–X | Gösterim · CTR % · Görüntüleme · Ort. gör. süresi (sn) · Ort. gör. % · 30. sn'de kalan % · Abone (+) · Yorum · Prompt tıkl. — hepsi `7g` | 7. gün |
| Y–AC | Gösterim · CTR % · Görüntüleme · Ort. gör. süresi (sn) · Ort. gör. % — `28g` | 28. gün |
| AD | Karşılaştırmaya ulaşan % 28g | 28. gün; video kartındaki "karşılaştırmanın başladığı an" değeri (02 A3: kanalın ana metriği) |
| AE–AF | Abone (+) · Abone (−) 28g | 28. gün |
| AG–AM | Trafik payları: Göz atma · Önerilen · YouTube araması · Shorts feed'i · Harici · Kanal sayfası · Diğer (% 28g) | 28. gün; yalnızca en büyük üç kaynak, kalanı boş (02 B8) |
| AN | Gerçekleşen birincil kaynak | 28. gün |
| AO–AP | Yeni izleyici · Geri dönen izleyici 28g | 28. gün; hangi Studio satırından doldurulacağı 02 belgesi Ek, madde 3 **[DOĞRULA]** |
| AQ–AU | Beğeni · Paylaşım · Yorum · Bitiş ekranı tıkl. % · Prompt tıkl. — `28g` | 28. gün |
| AV–AW | Tahmini gelir · RPM 28g | Para kazanma açılana kadar `[yok]` |

**Grup 3 — Türetilmiş göstergeler (AX–BQ).** Formülle hesaplanır; elle yazılmaz. `BR` serbest not sütunudur.

### 2.3 Formüller

Formüller 2. satır için yazılmıştır; aşağı doğru doldur. İşlev adları Türkçe Excel'e göredir. Google E-Tablolar Türkçe arayüzde aynı adları kullanır **[DOĞRULA]**; bir ad tanınmazsa Dosya → Ayarlar'dan İngilizce işlev adlarını aç ve parantez içindeki adı kullan: ORTANCA (MEDIAN), EĞER (IF), EĞERHATA (IFERROR), YADA (OR), VE (AND), DEĞİL (NOT), ESAYIYSA (ISNUMBER), BAĞ_DEĞ_SAY (COUNT), KAYDIR (OFFSET), SATIR (ROW), MİN (MIN), MAK (MAX), TAMSAYI (INT), YUVARLA (ROUND), KAREKÖK (SQRT), TOPLA (SUM), RANK.EŞİT (RANK.EQ), ÇOKEĞERSAY (COUNTIFS), FİLTRE (FILTER), YÜZDEBİRLİK.DAHİL (PERCENTILE.INC). Formüllerin mantığı İngilizce adlarla LibreOffice'te sınandı; Türkçe adlarla Excel'de ve E-Tablolar'da sınanmadı **[DOĞRULA]**.

**a) Kanal medyanına oran** (AZ, BA, BB, BC, BD, BF, BH). Videonun değeri ÷ **kendinden önceki** en fazla 10 videonun aynı yaştaki medyanı. 1,00 = medyanla aynı; 0,60 = medyanın yüzde 60'ı. Önceki videolardan en az 5'inde değer yoksa hücre boş kalır (02 B5, 1. basamak: "yalnızca kaydet"). Video kendi kıyas kümesine girmez; aksi hâlde aykırı bir video kendi ölçütünü de çeker. `BB2` (Görüntüleme ÷ medyan 7g) için:

```text
=EĞERHATA(EĞER(YADA(DEĞİL(ESAYIYSA(R2));BAĞ_DEĞ_SAY(KAYDIR(R2;-MİN(10;SATIR()-2);0;MİN(10;SATIR()-2);1))<5);"";R2/ORTANCA(KAYDIR(R2;-MİN(10;SATIR()-2);0;MİN(10;SATIR()-2);1)));"")
```

Diğerleri aynı formüldür; yalnızca `R` harfi değişir: `AZ` → P (gösterim) · `BA` → Q (CTR) · `BC` → S (ort. gör. süresi) · `BD` → U (30. sn) · `BF` → AA (görüntüleme 28g) · `BH` → BG (1.000 görüntüleme başına abone).

**b) Üçte bir etiketi** (`BE2`). 02 B5'teki işlemsel tanımın formülü: video ve kendinden önceki 9 video içinde en düşük ⌊n/3⌋ değerden biriyse "düşük", en yüksek ⌊n/3⌋ değerden biriyse "yüksek". Kümede 6'dan az değer varsa boş kalır.

```text
=EĞERHATA(EĞER(YADA(DEĞİL(ESAYIYSA(R2));BAĞ_DEĞ_SAY(KAYDIR(R2;-MİN(9;SATIR()-2);0;MİN(9;SATIR()-2)+1;1))<6);"";EĞER(RANK.EŞİT(R2;KAYDIR(R2;-MİN(9;SATIR()-2);0;MİN(9;SATIR()-2)+1;1);1)<=TAMSAYI(BAĞ_DEĞ_SAY(KAYDIR(R2;-MİN(9;SATIR()-2);0;MİN(9;SATIR()-2)+1;1))/3);"düşük";EĞER(RANK.EŞİT(R2;KAYDIR(R2;-MİN(9;SATIR()-2);0;MİN(9;SATIR()-2)+1;1);0)<=TAMSAYI(BAĞ_DEĞ_SAY(KAYDIR(R2;-MİN(9;SATIR()-2);0;MİN(9;SATIR()-2)+1;1))/3);"yüksek";"normal")));"")
```

Başka bir metrik için `R`yi değiştir. Bu etiket **toplam** değere bakar; karar tablosu kaynak bazında okuma ister (02 B5), o yüzden etiket ön elemedir, hüküm değildir.

**c) Kısa formüller**

| Sütun | Gösterge | Formül (2. satır) | Ne söyler |
|---|---|---|---|
| AX | Süre bandı | `=EĞER(J2="";"";EĞER(J2<600;"<10 dk";EĞER(J2<720;"10–12 dk";"12+ dk")))` | Gruplama etiketi (FT4) |
| AY | CTR ± puan 7g | `=EĞER(VE(ESAYIYSA(P2);ESAYIYSA(Q2);P2>0);1,96*KAREKÖK(Q2/100*(1-Q2/100)/P2)*100;"")` | CTR'nin örneklem payı (Bölüm 3, kural 2) |
| BG | 1.000 gör. başına abone 28g | `=EĞER(VE(ESAYIYSA(AE2);ESAYIYSA(AA2);AA2>0);AE2/AA2*1000;"")` | Aboneye dönüşüm |
| BI | Etkileşim / 1.000 gör. 28g | `=EĞER(VE(BAĞ_DEĞ_SAY(AQ2:AS2)=3;ESAYIYSA(AA2);AA2>0);TOPLA(AQ2:AS2)/AA2*1000;"")` | Beğeni + paylaşım + yorum |
| BJ | Prompt tıkl. / 1.000 gör. 28g | `=EĞER(VE(ESAYIYSA(AU2);ESAYIYSA(AA2);AA2>0);AU2/AA2*1000;"")` | İzleyici prompt'u almaya gitti mi |
| BK | Geri dönen izleyici payı % 28g | `=EĞER(VE(ESAYIYSA(AO2);ESAYIYSA(AP2);AO2+AP2>0);AP2/(AO2+AP2)*100;"")` | Video kimi getirdi: yeni mi, tanıyan mı |
| BL | 28g ÷ 7g görüntüleme | `=EĞER(VE(ESAYIYSA(R2);ESAYIYSA(AA2);R2>0);AA2/R2;"")` | 1'e yakın: video ilk haftada bitti. Büyüdükçe: uzun kuyruk |
| BM | Kuyruk payı % (8–28. gün) | `=EĞER(VE(ESAYIYSA(R2);ESAYIYSA(AA2);AA2>0);(AA2-R2)/AA2*100;"")` | Aynı bilginin yüzde hâli |
| BN | Plan tuttu mu | `=EĞER(YADA(M2="";AN2="");"";EĞER(M2=AN2;"E";"H"))` | Rol tahmini doğru muydu (02 B3) |
| BO | V1 ön koşulu | `=EĞER(ESAYIYSA(P2);EĞER(P2>=1000;"E";"H");"")` | Toplam gösterim 1.000'in altındaysa hiçbir kaynakta V1 sağlanamaz |
| BP | V2 | `=EĞER(ESAYIYSA(R2);EĞER(R2>=100;"E";"H");"")` | Tutma ve AVD okunur mu |
| BQ | V3 | `=EĞER(ESAYIYSA(AA2);EĞER(AA2>=300;"E";"H");"")` | Abone oranı ve bitiş ekranı okunur mu |

`BL` için "iyi" bir değer yoktur; arama rolündeki videoda yüksek, öneri rolündeki videoda düşük çıkması beklenir **[Yaygın gözlem]**. Yalnızca aynı roldeki videolar arasında kıyaslanır.

**d) Grup medyanı (aylık analiz için, ayrı sayfada).** Örnek: G kategorisinin 28 günlük görüntüleme medyanı ve o medyanın kaç videoya dayandığı:

```text
=ORTANCA(FİLTRE(Veri!AA2:AA200;(Veri!D2:D200="G")*ESAYIYSA(Veri!AA2:AA200)))
=ÇOKEĞERSAY(Veri!D2:D200;"G";Veri!AA2:AA200;">0")
```

`FİLTRE` eski Excel sürümlerinde yoktur; orada `=ORTANCA(EĞER((Veri!D2:D200="G")*ESAYIYSA(Veri!AA2:AA200);Veri!AA2:AA200))` formülünü Ctrl+Shift+Enter ile gir. Medyanın yanına **her zaman** video sayısını yaz; sayısız medyan okunmaz.

---

## 3. Okuma kuralları

02 belgesi A2 (CTR'nin dört okuma kuralı), B5 (kıyas merdiveni, V1–V4) ve performans kaydının altı okuma kuralı geçerlidir. Aşağıdakiler onlara eklenir.

**1. Örneklem eşiği önce, yorum sonra.** Bir sayıya bakmadan önce `BO–BQ` sütunlarına bak. V1–V4 video başına okuma eşiğidir (02 B5); gruplar için ek eşikler **[Tahmini]**:

| Karar | Asgari | Mantığı |
|---|---|---|
| Bir etiketin grup medyanını **yazmak** | Grupta 3 video | 02 B8: 3'ten az videolu kategori yorumlanmaz |
| İki grubu **karşılaştırmak** | Her grupta 3 video ve değerlerde tam ayrışma | 3'e 3 videoda bir grubun bütün değerlerinin diğerinin bütün değerlerinden yüksek çıkması tesadüfen 20 dizilişten 1'inde olur (6 değerden 3'ünü seçmenin 20 yolu vardır). Tek bir çakışma bu güvenceyi ortadan kaldırır |
| Grup medyanını **karar tablosunda** kullanmak | Grupta 5 video | 02 B4 ile aynı |
| Bir **oranı** (abone/1.000 gör., bitiş ekranı tıklaması) yorumlamak | Paydaki olay sayısı en az 10 | Seyrek olaylarda sayım hatası kabaca olay sayısının karekökü kadardır; 10 olayda bu yaklaşık üçte bir, 4 olayda yarı yarıya oynama demektir. 10'un altında oranı değil, sayının kendisini yaz |

**2. CTR'yi payıyla birlikte oku.** `AY` sütunu, CTR'nin yalnızca örneklem büyüklüğünden kaynaklanan oynama payını verir (yüzde 95 aralığının yarı genişliği, puan olarak). İki videonun CTR farkı bu payların toplamından küçükse **fark yok** say. Pay bir alt sınırdır: aynı kişiye birden çok gösterim yapıldığı için gerçek belirsizlik daha büyüktür **[Tahmini]**. Evrensel bir "iyi CTR" eşiği yoktur (02 A2, B9).

**3. Ortalama değil medyan; toplam değil oran.** Görüntüleme dağılımı çarpıktır (02 B9); tek bir video ortalamayı çeker. Tabloda ortalama sütunu yoktur. Kanal büyürken ham sayılar yeni videoların lehine kayar; dönemler arası kıyasta ham görüntüleme yerine `÷ medyan` sütunlarını kullan.

**4. Benzeri benzerle.** Üç eşleşme aranır: **aynı yaş** (7g ile 7g), **aynı trafik kaynağı** (arama CTR'si ile Göz atma CTR'si kıyaslanmaz), **aynı rol** (`L` sütunu). Yüzdeler için dördüncüsü: **aynı süre bandı** (`AX`); farklı uzunlukta APV kıyaslanmaz, AVD saniye olarak yan yana yazılır (02 A3).

**5. Karışım etkisi.** Toplam CTR, hiçbir kaynakta CTR değişmeden de düşebilir: gösterimin daha büyük kısmı CTR'si doğal olarak düşük bir kaynağa (çoğunlukla Göz atma) kaymıştır. Toplam CTR'deki her değişimde önce kaynak paylarına bak; kaynak içi CTR değişmemişse yorum "paket bozuldu" değil, "karışım değişti"dir. "Gösterim arttıkça CTR düşer" kuralı (02 A2, kural 1) bunun en sık görülen hâlidir.

**6. Ortalamaya dönüş.** Olağandışı iyi bir videodan sonraki video, hiçbir şey değişmese de daha zayıf görünür; tersi de doğrudur. Bu yüzden kıyas kümesi tek video değil son 10 videodur ve "geçen haftaya göre düştü" cümlesi karar gerekçesi olmaz.

**7. Mevsimsellik.** Hedef kitle çalışan kesim olduğu için resmî tatil haftaları, bayram tatilleri, yaz izin dönemi ve yılbaşı haftasında izleme davranışının değişmesi beklenir **[Tahmini — kendi verinle sına]**. Sınama yöntemi: Gelişmiş mod → tarih aralığı son 90 gün → **28 günden eski videoların** toplam günlük görüntülemesi ("taban trafiği"). Yeni videonun zayıf haftasında taban da aynı oranda düştüyse neden mevsimdir; yeni videoya müdahale edilmez ve o hafta `BR` sütununa "tatil haftası" yazılır. Taban düzken yeni video düşükse neden videodadır.

**8. Tek değişken.** Bir bulguyu sınamak için aynı anda tek şey değişir; sınırlar 02 B4'tedir (aynı anda en fazla 1 format testi + 1 elle paket testi). Analiz açısından sonucu: iki etiketi aynı anda değişen iki video arasındaki fark **hiçbir** etikete yazılamaz.

**9. Etiketler birbirine yapışıktır.** İlk 10 videoda kategori, kurgu ve başlık formülü büyük ölçüde birlikte değişir (G videoları çoğunlukla KG1). Bir etiketi "nedeni" saymadan önce çapraz tabloya bak (Bölüm 5, adım 3); iki etiket hep birlikte geliyorsa ayrıştırılamaz, ayrıştıran bir video planlanır.

**10. İpucu → bulgu → kural.** Tek video ipucudur; aynı yönde, asgari verisi tam üç video bulgudur (performans kaydı, okuma kuralı 4); bulgu ancak 02 B4'teki test koşuluyla kanal kuralı olur ve ilgili belgeye işlenir.

---

## 4. Haftalık değerlendirme (30 dakika)

02 B8'deki rutinin **kendisidir**; süre, sıra ve asgari doldurma kuralı aynıdır. Burada her adımın ekranı, okunacak hücreler ve cevaplanacak soru yazılı. Kronometreyle yapılır.

| Dk | Soru | Ekran | Ne yazılır |
|---|---|---|---|
| 0–3 | **S1. Kanal tabanı olağan mı?** | Analytics → Genel Bakış, son 7 gün ↔ önceki 7 gün | Yalnızca olağandışı sıçrama/düşüş ve hangi videodan geldiği. Olağandışı yoksa hiçbir şey |
| 3–13 | **S2. 7 günlük video zincirin hangi halkasında kanaldan ayrıştı?** | Video → Analytics → Erişim (gösterim, CTR, kaynak tablosu); Etkileşim (tutma grafiği, bitiş ekranı) | Analiz tablosu P–X · karttaki planlanan kaynağın gösterimi/CTR'si ve işaret noktaları |
| 13–21 | **S3. 28 günlük video planlanan kaynaktan trafik aldı mı, dersi ne?** | Aynı ekranlar; Erişim → Trafik kaynağı türleri → kaynağa tıkla | Analiz tablosu Y–AU · kartın 28. gün sütunu · tek cümle ders · kart kapanır |
| 21–26 | **S4. İzleyici bu hafta ne istedi?** | Erişim → YouTube araması (terimler); Yorumlar | `fikir-havuzu.md`, en fazla 3 satır |
| 26–28 | **S5. Süren deneme ne durumda?** | Video ayrıntıları → test sonucu; test kartı | Test kartı (02 B4) |
| 28–30 | **Karar** | — | Tek cümle (aşağıda) |

**S2 nasıl cevaplanır (10 dakikanın dökümü):**

1. Sayıları gir (4 dk). `BO` ve `BP` "H" ise ilgili metrik bugün okunmaz; hücreyi doldur, yorumu 28. güne bırak.
2. Zinciri soldan sağa oku (02 A0): `AZ` gösterim → `BA` CTR → `BD` 30. sn → `BC` ort. gör. süresi. **İlk** ayrışan halkayı bul. Çalışma kuralı **[Tahmini]**: oran 0,67'nin altı ya da 1,5'in üstü "ayrışmış" sayılır (medyanın üçte iki ile bir buçuk katı arası olağan oynama kabul edilir; KM-015'ten sonra kendi dağılımına göre daralt). `BE` etiketi aynı bilgiyi görüntüleme için verir.
3. Ayrışan halka için kaynak tablosunu aç ve **planlanan birincil kaynağın** satırını oku (2 dk). Toplamdaki ayrışma o kaynakta da var mı?
4. Tutma grafiğinde dört işaret noktasını oku (3 dk; V2 yoksa atla).
5. Ayrışma varsa 02 B5 karar tablosundaki satırı bul; satır müdahale gerektiriyorsa ve video KM-006 ya da sonrasıysa **tek** müdahale. Ayrıntılı teşhis (Bölüm 6) bu 10 dakikaya sığmaz; aylık oturuma ya da ayrı bir 20 dakikaya bırakılır ve karar cümlesine "teşhis bekliyor" yazılır.

**Karar cümlesi (çıktı):** Video kartındaki "Çıkarım" tablosuna ve bir sonraki perşembe ilk okunacak yere yazılır.

```text
KM-[sıradaki no]'da [tek değişken]i [nasıl] yapacağım; [metrik]in [kıyas noktası]na göre [yön] olmasını bekliyorum; [tarih]te (yayın + [7/28]) bakacağım. Dayanak: [KM-no, metrik, değer] — [ipucu / bulgu].
```

Geçerli karar örnekleri: bir senaryo kuralı, bir test başlatma, "bu hafta değişiklik yok; KM-0NN'nin 28. gününü bekliyorum". Geçersiz: iki değişken içeren cümle; metrik ve tarih içermeyen cümle; "daha iyi kapak yapacağım".

**Haftalık rutinde yapılmayanlar:** grup medyanı hesaplamak, kategori kıyaslamak, eski videoların paketini gözden geçirmek, gelire bakmak. Hepsi aylık oturumun işidir.

---

## 5. Aylık değerlendirme (90 dakika)

Ayın son yayınından sonraki ilk perşembe ya da cumartesi yapılır; çalışma kâğıdı `sablonlar/aylik-degerlendirme.md`. 02 B8'deki "ayda bir, 20 dakika" bakışı bu oturumun **ikinci adımıdır**; ayrıca yapılmaz. 28 günlük verisi olan video sayısı 6'nın altındayken (kabaca ilk iki ay) yalnızca adım 1, 2 ve 7–8 yapılır (formda Bölüm 0, 1 ve 7); oturum 30–40 dakikada biter.

| Dk | Adım | Çıktı |
|---|---|---|
| 0–10 | **1. Veri hazırlığı.** Boş kalmış 28g hücrelerini tamamla. Gelişmiş moddan video tablosunu dışa aktar, elle girdiğin üç videoyu rastgele seçip karşılaştır | Temiz tablo |
| 10–30 | **2. Aylık bakış.** Performans kaydı §5.3 (izleyici türleri, vekil göstergeler, kategori dağılımı, stok) | §5.3 satırı |
| 30–55 | **3. Kalıp bulma** (aşağıda) | Grup tablosu, ortak özellik tablosu |
| 55–65 | **4. Trafik karışımı** | Kaynak payları, plan–gerçek uyumu |
| 65–75 | **5. Kitle ve abone dönüşümü** | Üç satırlık not |
| 75–80 | **6. Gelir** (para kazanma açıksa; değilse bu 5 dakika adım 3'e eklenir) | RPM satırı |
| 80–90 | **7–8. Sürdür / durdur / dene + gelecek ayın içerik kararları** | Liste ve plan |

### Adım 3 — Başarılı içerik kalıplarını bulma

**a) Etikete göre gruplama.** Her etiket sütunu (D kategori, E kurgu, F başlık formülü, G kapak çifti, I hook, L rol, AX süre bandı, K konu ailesi) için grup medyanlarını çıkar (2.3-d). Dört sonuç sütunu yeter: `BF` görüntüleme ÷ medyan 28g, `AD` karşılaştırmaya ulaşan %, `BG` 1.000 görüntüleme başına abone, `BJ` prompt tıklaması. 3'ten az videolu gruba medyan yazılmaz; "n yetersiz" yazılır. E-Tablolar'da özet tablo medyanı doğrudan verir; Excel özet tablosunda medyan yoktur, formül kullanılır **[DOĞRULA]**.

**b) Medyan karşılaştırma.** İki grup arasında fark aranırken medyanların yanına her grubun **en düşük ve en yüksek** değerini yaz. Aralıklar iç içeyse fark iddia edilmez (Bölüm 3, kural 1). Aralıklar ayrıksa "ipucu" yazılır ve çapraz kontrole geçilir.

**c) Çapraz kontrol.** Fark görünen etiket başka bir etiketle birlikte mi geliyor? `=ÇOKEĞERSAY(Veri!D2:D200;"G";Veri!E2:E200;"KG1")` türü sayımlarla 2×2 tablo kur. G videolarının tamamı KG1 ise "G iyi" ile "KG1 iyi" ayrıştırılamaz; "dene" listesine ayrıştıran video yazılır (KG3 kurgulu bir G videosu gibi).

**d) En iyi ve en kötü yüzde 20.** 28 günlük verisi olan videoları `BF` sütununa göre sırala (ham görüntülemeye göre değil; ham sıralama kanal büyüdükçe yeni videoları öne alır). `BF` dolu video sayısı 10'un altındaysa bu adım yapılmaz. Uç grup büyüklüğü: video sayısının beşte biri, en az 2 video. Aynı işlemi ikinci kez `BG` (abone dönüşümü) için yap; iki sıralamada da uçta olan videolar ayrıca işaretlenir.

**e) Ortak özellik tablosu.** Her etiket değeri için üç sayı yan yana yazılır:

| Özellik | En iyi %20'de | En kötü %20'de | Bütün videolarda (taban) | Ayrıştırıyor mu |
|---|---|---|---|---|
| ör. Kapak çifti = süre | [x] / [uç grup] | [y] / [uç grup] | [z] / [toplam] | E / H |

Bir özellik ancak şu üç koşul birlikte sağlanırsa "ayrıştırıyor" sayılır **[Tahmini]**: en iyi gruptaki payı tabandaki payından yüksek; en kötü gruptaki payı tabandakinden düşük (ya da tersi); özelliği taşıyan en az 3 video var. Taban sütunu olmadan bu tablo yanıltır: videoların çoğu KG1 ise en iyilerin çoğunun KG1 olması hiçbir şey söylemez. Tablodan sonra en iyi ve en kötü videoların kartlarındaki "Çıkarım" satırlarını alt alta oku; etiketlerin yakalamadığı ortak nokta (aynı örnek şirket, aynı tür "yapamadığı şey", aynı haftada tatil) çoğu zaman oradadır.

**f) Blok kaybı tablosu.** Video kartlarındaki işaret noktalarından her blok için "bloğa giren izleyicinin yüzde kaçı blok içinde çıktı" hesaplanır (Bölüm 7, adım 5). Hangi bloğun kanal genelinde en çok kaybettirdiği buradan görülür; 02 B1 Aşama 1'in sorusunun ("format çalışıyor mu") cevabı bu tablodur.

### Adım 4 — Trafik kaynağı karışımı

1. Kanal düzeyi: Analytics → Erişim → Trafik kaynağı türleri, son 28 gün ↔ önceki 28 gün. Her kaynağın payını yaz; değişimi puan olarak not et.
2. Plan–gerçek: `BN` sütununda "E" oranı. Rol bazında ayrı say: arama rolündeki videoların kaçında birincil kaynak arama çıktı? Oran düşükse sorun videolarda değil, rol tahminindedir (02 B3).
3. Bağımlılık: tek bir kaynak görüntülemenin büyük çoğunluğunu veriyorsa ve o kaynak "Harici" ise YouTube içi keşif başlamamıştır (02 A6). Sayısal eşik yok; aydan aya yönüne bak.
4. Önerilen → kaynağa tıkla → kendi videolarının payı (02 A5 vekil göstergesi; §5.3'e yazılır).

### Adım 5 — Kitle ve abone dönüşümü

- **Kim izliyor:** Analytics → Kitle → yaş, cinsiyet, coğrafya, cihaz. Hedef (26–42, Türkiye, çalışan) ile örtüşme. Kartlar yeterli veri yokken boş gelir; boşsa "veri yok" yaz.
- **Başka ne izliyor:** Kitle → "Kitlenizin izlediği kanallar / videolar" kartları **[DOĞRULA: küçük kanalda görünmeyebilir]**. Görünüyorsa listeyi fikir havuzuna değil aylık forma yaz; konumlandırma sorusu çeyreklikte ele alınır.
- **Abone dönüşümü:** Gelişmiş mod → boyut "Abonelik durumu": görüntülemenin abone / abone olmayan payı. Boyut "Abonelik kaynağı" **[DOĞRULA]**: aboneler video sayfasından mı, kanal sayfasından mı geldi. Video bazında `BG` sıralaması: en çok abone getiren üç video ile en az getiren üç videonun rolü ve kurgusu ne?
- **Geri gelme:** `BK` ve üç vekil gösterge (02 A5). Düzenli izleyici sayısı ilk altı ayda sıfırdır; yorumlanmaz.

### Adım 6 — Gelir

Para kazanma açılana kadar atlanır. Açıldıktan sonra: Analytics → Gelir → aylık tahmini gelir, RPM ve video bazında dağılım. RPM, 1.000 görüntüleme başına sana kalan toplam gelirdir; oynatma başına BGBM (CPM) ise reklamverenin ödediği tutardır ve ikisi kıyaslanmaz **[Resmî][DOĞRULA]** [Understand ad revenue analytics](https://support.google.com/youtube/answer/9314357). Tabloya yalnızca RPM ve tahmini gelir yazılır. Gelir yöntemlerinin kendisi bu belgenin konusu değildir; teşhis için Bölüm 6, D8. Vergi ve beyan konuları için mali müşavire danış; bu belge mali tavsiye içermez.

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

02 B5'teki karar tablosu "belirti → müdahale" verir. Bu bölüm araya girer: müdahaleden önce **hangi kanıt toplanır ve iki olası neden nasıl ayrılır.** Ön koşullar aynıdır: KM-006 ve sonrası, asgari veri sağlanmış, yerleşik test sürmüyor. Her dalın sonunda iyileştirme ve onun nasıl sınanacağı yazılı; müdahale metni B5'te varsa yalnızca atıf verilir.

```
Görüntüleme düşük (BE = "düşük" ya da BB < 0,67)
├─ Gösterim de düşük ───────────────────────────── D1  paket mi, konu mu?
├─ Gösterim olağan, CTR düşük ──────────────────── D2
└─ Gösterim ve CTR olağan → sorun izlemede
     ├─ 30. sn düşük ───────────────────────────── D3
     └─ 30. sn olağan, gövdede kayıp ───────────── D4
Görüntüleme olağan ya da yüksek, ama…
├─ abone gelmiyor ──────────────────────────────── D5
├─ arama rolündeki videoda arama trafiği yok ───── D6
├─ Önerilen trafiği yok ────────────────────────── D7
└─ gelir düşük (para kazanma açıksa) ───────────── D8
```

**D1 — Gösterim yok: paket mi, konu mu?**
- *Kanıt:* (1) Gelişmiş modda videonun gösterimini kaynak ve gün kırılımıyla aç. (2) O kaynaklardaki CTR'yi ve `AY` payını oku. (3) Arama terimleri listesi. (4) Hedef sorguyu YouTube arama kutusuna yaz; otomatik tamamlamada çıkıyor mu. (5) Aynı konu ailesinden (`K`) başka video varsa onun `AZ` değeri.
- *Ayırıcı bulgu:* Gösterim hiç başlamadıysa paket henüz sınanmamıştır; "paket kötü" denemez. Gösterim geldi, CTR alt üçte birde kaldı, ardından gösterim yataylaştıysa → **paket.** Var olan gösterimde CTR ve tutma olağansa, terim listesi boşsa ve aynı konu ailesindeki öbür video da düşükse → **konu** (talep az ya da çerçeve izleyicinin dilinde değil). İkisi de olağan, yalnızca hacim küçükse → B5'in ilk satırı: bekle, pakete dokunma.
- *İyileştirme:* Paket → B5 "CTR düşük" satırları. Konu → aynı görevin izleyici diliyle yazılmış çerçevesini fikir havuzuna al; mevcut videoya dokunma.
- *Test:* Paket varsayımı aynı videoda sınanır (konu sabit, paket değişir): 02 B4 elle sıralı test, sonuç "zayıf kanıt". Konu varsayımı yeni videoda sınanır (paket kalıbı sabit, konu çerçevesi değişir): yeni videonun `AZ` değeri eskisinden yüksek mi.

**D2 — CTR düşük**
- *Kanıt:* (1) Kaynak bazında CTR ve V1. (2) İki videonun farkı `AY` paylarının toplamından büyük mü. (3) Kapağı telefonda, koyu modda, küçük boyutta aç (01 belgesi 3.4). (4) Arama kaynağıysa sorgunun sonuç sayfasının ekran görüntüsü. (5) Aynı kapak çifti türündeki (`G`) öbür videoların `BA` değeri.
- *Ayırıcı bulgu:* Yalnızca Göz atma'da düşükse paket soğuk kitleye konuşmuyor; yalnızca aramada düşükse sonuç sayfasında ayrışmıyor; toplamda düşük ama her kaynakta olağansa karışım etkisi (Bölüm 3, kural 5) → müdahale yok.
- *İyileştirme ve test:* B5'in ilgili satırı; test B4 (koşul varsa yerleşik, yoksa elle sıralı; önce kapak, sonra başlık).

**D3 — İlk 30 saniyede kayıp**
- *Kanıt:* (1) Grafikte düşüşün en dik olduğu aralığı bul: 0–5 sn, 5–15 sn, 15–30 sn. (2) Altyazı dosyasından o aralıktaki cümleyi oku (Bölüm 7). (3) Kaynak bazında AVD: kayıp bir kaynağa mı özgü. (4) CTR'nin konumu (`BA`). (5) Tutma raporunda izleyici kesimi seçilebiliyorsa abone / abone olmayan ayrımı **[DOĞRULA]**.
- *Ayırıcı bulgu:* 0–5 sn + yüksek CTR → paket–açılış uyumsuzluğu (B5). 5–15 sn → ilk cümle görevi söylemiyor. 15–30 sn → kurulum uzun; sonuç görüntüsü geç geliyor. Kayıp yalnızca Harici kaynaktaysa sorun videoda değil, gönderi metnindedir (02 A6).
- *İyileştirme:* 01 belgesi Bölüm 4 ve 5 (hook ve açılış sahnesi kuralları); B5'in iki "ilk 30 sn" satırı.
- *Test:* FT1 (02 B4): 3 video, 2/3 kuralı, metrik `U` / `BD`.

**D4 — Ortada uçurum ya da sürekli eğim**
- *Kanıt:* Bölüm 7'deki eşleştirme; düşüşün türü (basamak mı, eğim mi, çukur + toparlanma mı); aynı blok türünün önceki videolardaki kaybı (blok kaybı tablosu).
- *Ayırıcı bulgu:* Yalnız bu videoda varsa o ana özgü (bekleme, erken CTA, konu dışı açıklama). Aynı blok türünde 3 videoda tekrar ediyorsa format sorunu.
- *İyileştirme:* Ana özgü → B5 "ortada basamak düşüş" satırı (bölüm başlığı ekle). Format → 01 belgesi 7.5 kontrolüne madde; FT2 / FT3 / FT4.
- *Test:* İlgili FT kartı; metrik blok kaybı yüzdesi (toplam APV değil).

**D5 — İzlenme iyi ama abone yok**
- *Kanıt:* (1) V3 ve "olay sayısı ≥ 10" kuralı; sağlanmıyorsa teşhis yapılmaz. (2) Abonelik durumu kırılımı: görüntülemenin ne kadarı zaten abone? Çoğu aboneyse düşük yeni abone doğaldır. (3) Trafik kaynağı: arama kaynaklı izleyici tek seferlik çözüm alır **[Yaygın gözlem]**; `BG` yalnızca aynı roldeki videolarla kıyaslanır. (4) Bitiş ekranı tıklama oranı. (5) Videoda bir sonraki görevin vaadi var mı (01 belgesi 8.2).
- *Ayırıcı bulgu:* Bitiş ekranı tıklaması da düşükse izleyici kanalda kalmıyor → seri bağlantısı eksik. Bitiş ekranı olağan, abone düşükse → abone olma gerekçesi söylenmiyor (02 B7).
- *İyileştirme:* 02 B7 ve B3; mevcut videoda bitiş ekranı hedefi ve sabitlenmiş yorumun "sıradaki adım" bloğu değiştirilebilir.
- *Test:* FT7 ya da tek değişkenli önce/sonra (bitiş ekranı hedefi); metrik `AT` ve `BG`, 28 gün.

**D6 — Arama trafiği yok**
- *Kanıt:* (1) Video arama rolünde miydi (`L`)? Değilse belirti değil. (2) 28. gün terim listesi. (3) Hedef sorgunun otomatik tamamlamadaki yazımı ile başlıktaki yazım. (4) Gizli pencerede sorguyu ara, sonuç sayfasını kaydet; sıralama kişiye ve konuma göre değişir, tek aramayla hüküm verilmez. (5) Arama trafiği yavaş birikir **[Yaygın gözlem]**; 28. günde yoksa 90. günde bir kez daha bak.
- *Ayırıcı bulgu:* Sorgu otomatik tamamlamada yoksa talep yok (konu). Var ama terim listesinde başka sorgular çıkıyorsa video başka bir niyetle eşleşmiş → başlık/açıklama dili. Aramada gösterim var, CTR düşükse → D2.
- *İyileştirme:* B5 "arama videosu, terim listesi boş" satırı.
- *Test:* Tek değişiklik (başlık yazımı), 28 gün sonra arama kaynaklı gösterim; "zayıf kanıt" olarak kaydedilir.

**D7 — Öneri trafiği yok**
- *Kanıt:* (1) Önerilen → kaynağa tıkla: hangi videolar öneriyor, kendi videoların var mı. (2) Videonun aynı sorunu sürdüren bir "kardeşi" yayında mı (02 A7). (3) Bitiş ekranı tıklama oranı. (4) Kanalda 28 günlük verisi olan kaç video var.
- *Ayırıcı bulgu:* İlk 10 videoda Önerilen payının küçük olması beklenen sıradır (02 A6) → teşhis değil, bekleme. Kardeş video varken bile liste boşsa → bağlantı (bitiş ekranı, sözlü geçiş, oynatma listesi) kurulmamış. Liste alakasız videolardan oluşuyorsa → konu sinyali dağınık (02 A11).
- *İyileştirme:* 02 B3 (seri mimarisi, oturum uzatma); devam videosu.
- *Test:* Devam videosu yayınlandıktan 28 gün sonra iki videonun Önerilen listesinde birbirini gösterip göstermediği ve "kendi videolarından gelen pay".

**D8 — Gelir düşük** (yalnızca para kazanma açıkken)
- *Kanıt:* Gelir = (görüntüleme ÷ 1.000) × RPM. Önce hangisinin düşük olduğunu ayır. RPM düşükse: (1) video bazında RPM sıralaması; (2) görüntülemenin Shorts / uzun video payı (ikisinin RPM'i aynı terazide tartılmaz **[Yaygın gözlem]**); (3) videonun para kazanma simgesi (sınırlı reklam var mı); (4) aynı ayın geçen yılı yoksa önceki üç ay: reklam harcaması dönemseldir **[Yaygın gözlem]**; (5) coğrafya dağılımı; (6) video içi reklam aralarının yerleşimi (uzunluk koşulu ve ayarlar için **[Resmî][DOĞRULA]** [Manage mid-roll ad breaks](https://support.google.com/youtube/answer/6175006)).
- *Ayırıcı bulgu:* RPM bütün videolarda birlikte düştüyse neden dönem ya da kitledir; müdahale yok. Tek videoda düşükse o videonun reklam uygunluğu ya da reklam arası yerleşimi.
- *İyileştirme:* Konuyu RPM'e göre seçme; kanalın vaadi görevdir. Reklam arası otomatik yerleştirildiyse doğal bölüm geçişlerine elle taşı.
- *Test:* Tek videoda, tek değişiklik, önce/sonra 28 gün; RPM ile birlikte o videonun blok kaybına da bak (reklam arası tutmayı düşürdüyse kazanç yanıltıcıdır). Kanıt zayıftır; dönem etkisini taban RPM ile kontrol et.

---

## 7. Tutma grafiği analiz yöntemi

Şekil sözlüğü 02 A4'te, yayın sonrası adımlar ve "belirgin düşüş" tanımı 01 belgesi 7.5'tedir. Burada grafiğin senaryoyla **saniye saniye** nasıl eşleştirileceği ve bulgunun nasıl kurala dönüşeceği yazılı. Ön koşul V2; grafik yoksa hücreye "veri yok" yazılır. Okuma zamanı 28. gün (7. günde yalnızca işaret noktaları).

1. **Zaman damgalı metni hazırla.** Videonun düzeltilmiş altyazı dosyası (`06_cikti/` içindeki .srt; 03 belgesi Aşama 6) her cümlenin başlangıç saniyesini verir. Dosyayı metin olarak aç; grafikle yan yana koy. Ek hazırlık gerekmez.
2. **Grafiği aç ve imleci gezdir.** Video → Analytics → Etkileşim → tutma grafiği. İmleç her noktada zamanı ve yüzdeyi gösterir. Studio arayüzü eğriyi saniye saniye dışa aktarmaz **[DOĞRULA]**; değerler elle okunur.
3. **Önce dört sabit işaret noktası** (02 A4), sonra **en fazla üç olay** (01 belgesi 7.5 sınırı). Her olay için dört şey yaz: başlangıç saniyesi, bitiş saniyesi, baştaki ve sondaki yüzde.
4. **Olayın türünü ölçerek adlandır** **[Tahmini tanımlar]**:

| Tür | Ölçüsü | İlk bakılacak yer |
|---|---|---|
| **Basamak** | 15 saniyeden kısa aralıkta, videonun kendi ortalama eğiminin en az üç katı diklikte düşüş | .srt'de o saniyedeki cümle: geçiş cümlesi, CTA, "şimdi…" ile başlayan duyuru |
| **Sürekli eğim** | 1 dakikadan uzun, ortalamadan dik ama basamaksız iniş | Blok bütün olarak: tempo, bekleme, kanıtsız geçen süre (01 belgesi 7.4) |
| **Çukur + toparlanma** | Düşüşten sonra eğri yeniden yükselir | İzleyici ileri sarmış; çukurdaki bölüm atlanabilir bulunmuş |
| **Tümsek** | Eğri yukarı döner | Geri sarma: ekrandaki prompt, tablo ya da hızlı geçilen adım |
| **Düzlük** | Eğim sıfıra yakın, 30 saniyeden uzun | O blokta ne yapıldıysa tekrar edilecek öğedir |
| **Son düşüş** | Son 30–60 saniyede dikleşme | Bitti sinyali veren cümle (02 A4) |

   Ortalama eğim = (0:30'daki yüzde − video sonundan 30 sn önceki yüzde) ÷ aradaki dakika. İlk saniyelerdeki düşüş her videoda vardır; olay sayılmaz, 0:30 değeri olarak kaydedilir.
5. **Blok kaybını hesapla.** İmza formatın blokları işaret noktalarıyla zaten sınırlıdır: kurulum (0:30 → kronometre başı), görev (kronometre başı → karşılaştırma başı), karşılaştırma (→ "yapamadığı şey" başı), son bölüm (→ video sonundan 30 sn önce). Sıra videoda farklıysa (FT3) blokları videodaki sırayla yaz. Her blok için:

   `blok kaybı % = (baştaki % − sondaki %) ÷ baştaki % × 100` ve `dakika başına = blok kaybı ÷ blok süresi (dk)`

   Bu oran, farklı uzunlukta videoların aynı blok türünü kıyaslamayı sağlar; APV bunu yapamaz. Tablo `aylik-degerlendirme.md` Bölüm 3'tedir.
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

## 8. Çeyreklik strateji değerlendirmesi (yarım gün)

02 B1 aşama geçişini takvime değil veri yeterliliğine bağlar; çeyreklik oturum da öyle: yaklaşık 13 haftada bir, ama en yakın **aşama kapısına** denk getirilir. İlk üçü: KM-010'un 28. günü dolduğunda (Aşama 1 çıkışı), KM-020'nin 28. günü dolduğunda (kategori kararı, 02 B1 Aşama 2b), KM-030 dolaylarında (Aşama 3'e geçiş). O ayın aylık oturumu çeyrekliğin ilk 90 dakikasıdır.

| Konu | Soru | Veri | Karar kuralı |
|---|---|---|---|
| **Kategori portföyü** | Hangi kategori kanalı taşıyor, hangisi denenmemiş? | Kategori başına: video sayısı, `BF` ve `BG` medyanı, en düşük–en yüksek değer, karşılaştırmaya ulaşan % | 02 B4 "kaç videoda karar verilir" tablosu. Üretim payları 02 B1'deki aşama dağılımına göre |
| **Seri kararları** | Hangi seri sürer, hangisi kapanır, yenisi açılır mı? | Seri (oynatma listesi) grubu: bitiş ekranı tıklaması, Önerilen'de kendi videolarının payı, seri içi videoların `BK` değeri | Seri ancak 3 videodan sonra değerlendirilir. Kapatma: 3 videoda geçiş göstergeleri alt üçte birde ve yorum/arama teriminde talep izi yok |
| **Konumlandırma** | Kanalı izleyen kişi, hedeflediğim kişi mi? | Kitle kartları (yaş, coğrafya); yorumlarda anılan meslek ve görevler (video kartları); arama terimleri; izleyicinin izlediği diğer kanallar | Hedefle gerçek ayrışıyorsa önce **paketi ve konuyu** hedefe çek; nişi değiştirme kararı 30 videodan önce verilmez (02 B1) |
| **Format** | İmza formatın hangi bloğu kaybettiriyor? | Blok kaybı tablosunun çeyrek medyanları | En çok kaybettiren blok için sıradaki FT testi |
| **Hedef metrikler** | Bu aşamanın odak metriği doğru mu, hedefi ne? | 02 B1'deki aşama odak metrikleri | Aşağıda |
| **Eşikler** | V1–V4 ve bu belgedeki tahmini eşikler kanalın hacmine uyuyor mu? | Son çeyrekte kaç videonun 7. günde V1/V2'yi sağladığı | Videoların yarısından azı 7. günde sağlıyorsa okuma noktası 28. gün olarak kalır; eşik düşürülmez (02 B5) |
| **Sistem maliyeti** | Analiz süreleri tutuyor mu? | Haftalık rutinin gerçek süresi (kart, "Analiz" satırı) | 30 dakikayı düzenli aşıyorsa sütun azalt; süreyi uzatma |

**Hedeflerin yeniden belirlenmesi** **[Tahmini yöntem]:** Dışarıdan kıyas kullanılmaz. En fazla iki metrik seçilir (aşamanın odak metriklerinden). Her biri için geçen çeyreğin üst üçte bir sınırı hesaplanır: `=YÜZDEBİRLİK.DAHİL(aralık;2/3)`. Gelecek çeyreğin hedefi: **medyanı bu sınıra taşımak.** Yani "geçen çeyrekte iyi sayılan video, bu çeyrekte olağan video olsun". Hedef sayı değil dağılım kaymasıdır; tek bir yüksek videoyla tutturulamaz.

**"Kanıt yeterli mi" ölçütü.** Stratejik bir karar (kategoriye ağırlık, seri kapatma, format değişikliği) ancak beş sorunun hepsine "evet" denirse verilir; biri "hayır" ise karar ertelenir ve eksik kanıtı üretecek video plana yazılır.

1. Her grupta en az 3 video (kategori medyanı karar tablosunda kullanılacaksa 5) var mı?
2. O videoların her birinde ilgili metriğin asgari verisi (V1–V4, olay sayısı ≥ 10) sağlanmış mı?
3. Fark en az üç videonun ikisinde aynı yönde mi ve grupların değer aralıkları ayrık mı?
4. Çapraz kontrol yapıldı mı; fark başka bir etiketle, mevsimle ya da kanalın büyüme eğilimiyle açıklanamıyor mu?
5. Karar geri alınabilir mi? Alınamıyorsa (niş, kapak kalıbının toptan değişmesi) 02 B4'teki daha yüksek eşik (30+ video, 5 kazananı belli test) aranır.

Çıktı tek sayfadır: portföy tablosu, en fazla üç stratejik karar (her biri beş sorunun cevabıyla), iki hedef metrik, "bu çeyrekte bilerek yapmayacaklarım" satırı. Performans kaydı §5.1 ve §5.2 güncellenir.

---

## 9. Yapay zekâ destekli analiz

**Ne zaman:** Haftalık özet prompt'u rutinin dışında, isteğe bağlıdır; 30 dakikayı uzatmaz. Kalıp bulma prompt'u aylık oturumun 3. adımından **sonra**, kendi tablonla karşılaştırmak için kullanılır. Tek videonun yorumu için kütüphanedeki **P10** yeterlidir; burada tekrar edilmez. Yorum özetleri için **P9**.

**Dört kural** (`prompt-kutuphanesi.md` ortak kurallarına ek):

1. Her sohbet yeni açılır ve önce **P0** yapıştırılır.
2. **Hesabı tablo yapar, asistan okur.** Medyan, oran ve sıralama elektronik tabloda hesaplanıp yapıştırılır (kütüphane ortak kural 5: asistana saydırma). Asistanın verdiği her sayı, yapıştırdığın tabloda aynen bulunmalıdır; bulunmuyorsa çıktıyı kullanma.
3. **Asistan neden bilmez.** Elindeki tek şey senin yapıştırdığın sayılardır; videoyu izlemedi, izleyiciyi tanımıyor, YouTube'un iç işleyişini görmüyor. Çıktıdaki her "çünkü" bir hipotezdir ve ancak Bölüm 6'daki kanıt adımıyla ya da 02 B4'teki testle doğrulanır.
4. Yapıştırdığın veride izleyiciye ait kişisel bilgi (kullanıcı adı, e-posta) olmaz. Çıktı performans kaydına **senin cümlenle** ve "yapay zekâ önerisi, sınanmadı" notuyla girer.

### A1 — Haftalık özet

```text
Aşağıda YouTube kanalımın analiz tablosundan satırlar var. Görevin tabloyu OKUMAK; neden açıklamak değil.

SÜTUN AÇIKLAMASI: "7g" = yayından sonraki 7. gün, "28g" = 28. gün. "÷ medyan" sütunları, videonun değerinin kendinden önceki en fazla 10 videonun medyanına oranıdır (1,00 = medyan). Boş hücre = henüz bakılmadı. "test", "[ölçüm yok]", "[yok]" = sayı değil; hesaba katma.
ASGARİ VERİ KURALLARIM: Gösterim 1.000'in altındaysa CTR yorumlanmaz. Görüntüleme 100'ün altındaysa tutma ve izlenme süresi yorumlanmaz. Görüntüleme 300'ün altındaysa abone oranı yorumlanmaz.

BU HAFTA 7. GÜNÜ DOLAN VİDEO: [SATIR — başlık satırıyla birlikte]
BU HAFTA 28. GÜNÜ DOLAN VİDEO: [SATIR]
ÖNCEKİ VİDEOLAR (en fazla son 10): [SATIRLAR]
SÜREN TEST / DENEME: [VAR: ne, hangi videolarda / YOK]

İSTEDİĞİM ÇIKTI:
1. OKUNABİLİRLİK: Her iki video için hangi metrikler asgari veriyi sağlıyor, hangileri sağlamıyor? Sağlamayanları sonraki maddelerde hiç kullanma.
2. AYRIŞMA: Okunabilir metriklerden hangilerinde "÷ medyan" değeri 0,67'nin altında ya da 1,5'in üstünde? Yalnızca tablodaki değerleri aktar: "[sütun adı]: [değer]". Ayrışma yoksa "ayrışma yok" yaz.
3. ZİNCİR: Gösterim → CTR → 30. saniye → ortalama görüntüleme süresi sırasında ilk ayrışan halka hangisi?
4. PLAN–GERÇEK: 28 günlük videoda planlanan birincil kaynak ile gerçekleşen aynı mı?
5. BAKMAM GEREKEN ÜÇ ŞEY: Bu tabloyla cevaplanamayan ama Studio'da kontrol edebileceğim en fazla üç soru. Her biri "şu ekranda şuna bak" biçiminde.
6. KARAR TASLAĞI: Tek cümle, şu kalıpta: "KM-[no]'da [tek değişken]i [nasıl] yapacağım; [metrik]in [kıyas]a göre [yön] olmasını bekliyorum." Tablo bir karara dayanak vermiyorsa "bu hafta değişiklik yok" yaz; karar uydurma.

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

TABLO (28 günlük verisi olan bütün videolar; başlık satırıyla): [TABLO]
BENİM HESAPLADIĞIM GRUP MEDYANLARI (etiket | değer | video sayısı | medyan | en düşük | en yüksek): [GRUP TABLOSU]
BENİM ŞU ANKİ ÇIKARIMIM: [1–3 CÜMLE ya da "henüz yok"]
ETİKET SÜTUNLARI: Kat., Kurgu, Başlık formülü, Kapak çifti, Hook, Rol, Süre bandı, Konu ailesi.
SONUÇ SÜTUNLARI: Görüntüleme ÷ medyan 28g · Karşılaştırmaya ulaşan % 28g · 1000 gör. başına abone 28g · Prompt tıkl. / 1000 gör. 28g.

İSTEDİĞİM ÇIKTI:
1. YAPIŞIK ETİKETLER: Hangi etiket değerleri hep aynı videolarda birlikte geçiyor? Video numaralarıyla listele. Bunlar birbirinden ayrıştırılamaz; sonraki maddelerde tek etiket gibi ele al.
2. ÖRÜNTÜ ADAYLARI (en fazla 5): Her biri için: etiket değeri | sonuç sütunu | o etiketi taşıyan videoların numaraları ve değerleri | taşımayanların değerleri | iki grubun değer aralıkları çakışıyor mu (EVET/HAYIR).
   Aday sayılma koşulu: her iki grupta en az 3 video VE aralıklar çakışmıyor. Koşulu sağlamayan hiçbir şeyi aday olarak yazma; "koşulu sağlayan örüntü yok" demek geçerli bir cevaptır.
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
| **2–4** | 1–3 videonun 7. günü | Sayıları gir. Tutma grafiği varsa dört işaret noktası ve en fazla üç olay. Arama terimleri, yorumlar. Üretim süresi (kart) | Videolar arası kıyas; "düşük/yüksek" etiketi; paket değişikliği (yalnız açık hata) |
| **5** | KM-001'in 28. günü; ilk aylık oturum (kısa sürüm; Bölüm 5) | İlk 28g satırı; planlanan ↔ gerçekleşen kaynak; `BL` kuyruk oranı | Kategori kıyası; grup medyanı; izleyici türü kartlarından sonuç |
| **6** | 5 videonun 7. günü | Aynı. Formüllerin çalıştığını kontrol et: `÷ medyan` sütunları gelecek hafta dolacak | — |
| **7** | KM-006'nın 7. günü: **ilk medyan kıyası** (2. basamak) | `AZ–BD`, `BE`; zincirde ilk ayrışan halka. Asgari veri varsa karar tablosuna göre tek müdahale | Kategori bazında kıyas (hiçbir kategoride 5 video yok); yerleşik test |
| **8–9** | 7–8 videonun 7. günü, 4–5 videonun 28. günü | 9. haftada ikinci aylık oturum (kısa sürüm + blok kaybı tablosunun ilk hâli) | En iyi / en kötü %20 (yeterli video yok) |
| **10** | KM-010 yayında; KM-006'nın 28. günü → 6 videoda 28g | Aşama 1 çıkış koşulu sağlandı mı (02 B1). B ve G için grup medyanı **yazılır** (3+ video), karar için kullanılmaz | K, M, P hakkında hüküm (birer video); İ (hiç video yok) |
| **11–13** | Kalan videoların 28. günü | Haftalık rutin sürer | — |
| **14** | KM-010'un 28. günü | **İlk tam aylık oturum (90 dk) + ilk çeyreklik oturum.** Blok kaybı tablosu 10 videoyla okunur: "format çalışıyor mu" | Niş ya da kapak kalıbı değişikliği; kategori durdurma |

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
2. Tutma raporunda izleyici kesimi (abone / abone olmayan, yeni / geri dönen) seçilebiliyor mu; eğri dışa aktarılabiliyor mu → [9314415](https://support.google.com/youtube/answer/9314415)
3. Gelişmiş modda "Abonelik durumu" ve "Abonelik kaynağı" boyutlarının Türkçe adları
4. Kitle sekmesinde "kitlenizin izlediği kanallar / videolar" kartları bu kanal büyüklüğünde görünüyor mu
5. RPM ve oynatma başına BGBM tanımlarının tam metni; Türkçe arayüzdeki adları → [9314357](https://support.google.com/youtube/answer/9314357)
6. Video içi reklam arası koşulu ve bağlantının doğru sayfaya gidip gitmediği → [6175006](https://support.google.com/youtube/answer/6175006)
7. Türkçe işlev adları: formülleri kendi Excel / E-Tablolar sürümünde iki örnek satırla dene; `RANK.EŞİT`, `FİLTRE`, `YÜZDEBİRLİK.DAHİL` adları sürüme göre değişebilir
8. CSV'nin kendi bölge ayarında doğru açıldığı (ondalık virgül, noktalı virgül ayırıcı, Türkçe karakterler)
