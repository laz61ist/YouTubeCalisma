# 03 — Yapay Zekâ Destekli Yapım İş Akışı

**Kanal:** Kısa Mesai · **Vaat:** "Aynı işi yarı sürede bitir." · **Belge tarihi:** 2026-11-16

Bu belge, bir fikrin yayınlanmış uzun videoya ve ondan kesilen kısa videolara hangi sırayla, kaç saatte ve hangi dosyalarla dönüştüğünü tarif eder. Ne çekileceği ve nasıl paketleneceği `01-icerik-uretim-sistemi.md` içindedir; burada **nasıl üretileceği** var.

Şablonlar ayrı dosyalardadır:

| Dosya | Ne zaman açılır |
|-------|-----------------|
| `sablonlar/video-brief.md` | Aşama 1–2 (fikir ve paket) |
| `sablonlar/senaryo-sablonu.md` | Aşama 3 |
| `sablonlar/olcum.md` | Elle koşu ve Aşama 4 (kanalın tek ölçüm kaydı) |
| `sablonlar/kronometre.html` | Elle koşu ve Aşama 4 (kayda gömülen kronometre) |
| `sablonlar/izin-onay.md` | Videoda başka birinin sözü, sesi, görüntüsü ya da ölçümü varsa |
| `sablonlar/prompt-kutuphanesi.md` | Her aşamada, ilgili prompt numarasıyla |
| `sablonlar/prompt-dosyasi.md` | Aşama 8 (izleyiciye verilen prompt sayfası ve dizin) |
| `sablonlar/yayin-metaverisi.md` | Aşama 8 |
| `sablonlar/performans-kaydi.md` | Aşama 9 |
| `sablonlar/kalite-kontrol-listeleri.md` | Senaryo, çekim, seslendirme, kurgu, kapak, yayın, 48 saat, kısa video ve LinkedIn aşamalarının sonunda ("bitti" kapısı). Araştırma, paketleme ve analiz için ayrı liste yoktur; o aşamaların "bitti" tanımı bu belgededir. |

### Bu belgedeki işaretler ve sınırlar

- **Süreler tahminidir.** Tek kişilik, ekran kaydı + seslendirme ağırlıklı bir üretim için başlangıç varsayımıdır. İlk 4 videoda her aşamanın gerçek süresini `performans-kaydi.md` içindeki üretim tablosuna yaz, bütçeyi ona göre düzelt.
- **[Resmî]** = YouTube'un kendi yardım sayfalarında / Studio arayüzünde açıkladığı şey. **[Gözlem]** = sektörde yaygın kabul gören, YouTube'un taahhüt etmediği pratik.
- **Doğrulama sınırı:** Bu belge yazılırken YouTube Yardım sayfaları (support.google.com) ve araçların kendi yardım siteleri doğrudan açılamadı; yalnızca web araması yapılabildi. "Arama sonucu üzerinden" yazan maddeler, ilgili sayfanın arama sonucunda görünen özetine dayanır; sayfanın tamamı okunmamıştır. Politika ve özellik maddelerinde "yayın öncesi kontrol et" notu vardır; araçların durumu Bölüm 3.2'deki tabloda tek tek yazılıdır.
- `[ÇEKİMDE ÖLÇ]`, `[ELLE SÜRE]`, `[YZ SÜRE]` yer tutucuları 01 numaralı belgedeki anlamlarıyla kullanılır. Bu belge bir yer tutucu daha ekler: `[KURULUM SÜRE]` = prompt'u ilk kez hazırlamak için harcanan, `olcum.md` içinde ayrıca tutulan süre.
- **Sayı tutarlılığı** bu belgede tek bir kontrolün adıdır; tanımı Bölüm 4.2'dedir, başka yerlerde yalnızca adıyla anılır.

---

## 0. İlk yayından önce: tek seferlik kurulum

Bu işler haftalık bütçenin dışındadır ve bir kez yapılır. Toplam **tahmini 8–9 saat**; ilk videonun üretim haftasından **en az bir hafta önce** bitmiş olmalı, çünkü kanal doğrulamalarının bir kısmı bekleme süresi ister.

### 0.1 Kanal özellik erişimi (30 dk + bekleme)

Sıfırdan açılan kanalda bu iş akışının üç dayanağı kendiliğinden açık gelmez: **özel kapak**, **sabit yorum** ve **açıklamadaki tıklanabilir bağlantı**.

- **[Resmî — arama sonucu üzerinden; sayfa açılamadı]** YouTube Yardım'daki "Orta düzey ve gelişmiş özelliklere erişim" sayfasına göre telefon doğrulaması orta düzey özellikleri açar. Gelişmiş özellikler (sayfanın verdiği örnekler: sabit yorum, daha yüksek günlük yükleme sınırı) için ya yeterli kanal geçmişi ya da kimlik/video doğrulaması gerekir; kimlik ve video doğrulaması her üreticiye sunulmaz.
- **[Gözlem — ikincil kaynaklar]** Özel kapak orta düzey özellikler arasında sayılıyor. Açıklamadaki tıklanabilir bağlantının hangi düzeyde olduğu konusunda ikincil kaynaklar çelişiyor. Shorts'taki "ilgili video" bağlantısı için koşul doğrulanamadı.

Yapılacaklar:

1. Studio → Ayarlar → Kanal → Özellik uygunluğu. Telefon doğrulamasını yap.
2. Aynı ekranda gelişmiş özellikler için sana sunulan yolu (kimlik / video doğrulaması) tamamla. Sunulmuyorsa kanal geçmişi birikene kadar Bölüm 0.3'teki yedek plan geçerli.
3. **Gizli test videosu (20 dk):** 1 dakikalık herhangi bir ekran kaydını "gizli" olarak yükle ve dört şeyi dene: (a) özel kapak yüklenebiliyor mu, (b) açıklamaya yazdığın bağlantı tıklanabiliyor mu, kısaltılmış bağlantı da tıklanabiliyor mu, (c) kendi yorumunu sabitleyebiliyor musun, (d) senaryo metnini altyazı olarak yapıştırıp "otomatik senkronize et" seçeneği Türkçe için çalışıyor mu (Aşama 6, adım 7). Sonuçları `performans-kaydi.md` Bölüm 0'a yaz.
4. `02-buyume-stratejisi.md` sonundaki "Doğrulanacaklar listesi"ni aynı oturumda geç.

### 0.2 Politika okuması (30 dk)

Bu belgedeki politika maddeleri ikincil kaynaklara dayanıyor. İlk videodan önce YouTube Yardım'da şu sayfaları oku, Bölüm 4.4'ü okuduğuna göre düzelt:

- "Değiştirilmiş veya sentetik içerik kullanımını açıklama"
- "YouTube kanalından para kazanma politikaları" → "Özgün olmayan içerik" ve "Yeniden kullanılan içerik"
- "YouTube İş Ortağı Programı'na genel bakış ve uygunluk" → güncel eşikler ve **duyurulmuş değişiklikler** (Bölüm 4.4 D)

### 0.3 Yedek plan: bir özellik açık değilse

| Açık olmayan | İlk videolarda ne yapılır |
|--------------|---------------------------|
| Özel kapak | Yayın ertelenir. Kapak kanalın paketinin yarısıdır; telefon doğrulaması tamamlanmadan ilk video yayınlanmaz. |
| Açıklamada tıklanabilir bağlantı | Prompt'un **tam metni** açıklamaya yazılır (bu zaten varsayılandır; Bölüm 5.5) ve videodaki prompt kartı okunacak kadar ekranda tutulur. Dizin bağlantısı açıklamada düz metin olarak kalır; videoda "bağlantıya tıkla" denmez, "prompt açıklamada yazılı" denir. |
| Sabit yorum | Soru, açıklamanın üçüncü satırına ve videonun kapanış cümlesine taşınır. Yorum yine yazılır, sabitlenemese de. |
| Shorts "ilgili video" | Yönlendirme yalnızca sözlüdür: "Tam hâli kanaldaki uzun videoda." |

### 0.4 Üretim altyapısı (tahmini 7–8 saat)

| İş | Tahmini süre | Bitti sayılır |
|----|--------------|---------------|
| Çekim profili: ayrı tarayıcı profili, bildirim ayarları, kayıt çözünürlüğü, imleç boyutu (Aşama 4) | 45 dk | 10 saniyelik deneme kaydı telefonda okunuyor |
| Kronometre: `kronometre.html` dosyasını aç, pencereyi kayıt karesinin sağ üstüne yerleştir, başlat/durdur tuşunu dene | 20 dk | Deneme kaydında rakamlar görünüyor ve gerçek süreyle aynı |
| Ses: mikrofon yeri, oda, ses zinciri ön ayarı (Bölüm 6.4) | 45 dk | 1 dakikalık deneme telefonda ve kulaklıkta dinlendi |
| Kurgu proje şablonu: kanal düzeni, yakınlaştırma ön ayarları, dikey zaman çizelgesi, dışa aktarma ön ayarları | 60 dk | Boş şablon kayıtlı |
| Grafik varlıkları: kronometre çerçevesi ve etiketleri, alt bant, karşılaştırma tablosu, "yapamadığı şey" kartı, prompt kartı, vurgu kutusu (Bölüm 6.3) | 120 dk | Hepsi şablonda, tek tıkla eklenebiliyor |
| Kapak şablonu: üç yerleşim, renk ve yazı tipi notu | 60 dk | Sayıyı değiştirip 2 dakikada dışa aktarabiliyorsun |
| Kurgusal şirket ve ilk iki veri seti (Bölüm 4.5) | 60 dk | `00_VARLIKLAR/ornek-veri` içinde, cevap anahtarıyla |
| Prompt dosyası sayfası, dizin, tıklama sayan kısa bağlantı (Bölüm 5.5) | 30 dk | Gizli sekmede giriş istemeden açılıyor; bir tıklama sayıldı |
| Altyazı aracı kabul testi (Bölüm 3.2'deki 15 dakikalık test) | 20 dk | 1 dakikalık kendi sesinle Türkçe döküm denendi |

---

## 1. Uçtan uca hat

```
1 Konu araştırması → 2 Paketleme → 3 Hazırlık + elle koşu + senaryo → 4 Çekim (ekran kaydı)
→ 5 Seslendirme → 6 Kurgu → 7 Kapak → 8 Yayınlama → 9 Performans analizi
→ 10 Kısa formata uyarlama: kesim + dağıtım (Shorts, LinkedIn; sonra TikTok ve Reels)
```

Sıra hakkında iki karar:

1. **Çekim seslendirmeden önce gelir.** Bu kanalda senaryonun bazı satırları ancak çekimde dolar (ölçülen süre, aracın gerçekten verdiği cevap, yaptığı hata). Sesi çekimden önce kaydedersen ya uydurursun ya yeniden kaydedersin.
2. **Kapak eskizi Aşama 2'de, son kapak Aşama 7'de yapılır.** Eskiz videonun yönünü belirler; son kapaktaki sayı ve ekran görüntüsü ise çekimden gelir.

Aşağıdaki süreler **başlangıç profili** içindir: Kronometre Yarışı yapısında (KG1), **8–10 dakikalık** uzun video, **2 kısa video**, dağıtım yalnızca Shorts + LinkedIn. İlk 4 video bu profille üretilir. Başka hikâye yapılarında neyin değiştiği Bölüm 1.11'de, 12–14 dakikalık videonun ek maliyeti tablonun altındadır.

| # | Aşama | Tahmini süre | Çıktı |
|---|-------|--------------|-------|
| 1 | Konu araştırması | 30 dk | Puanlanmış fikir + doldurulmuş brief (üst yarı) |
| 2 | Paketleme | 30 dk | 3 başlık, 3 kapak eskizi, vaat testi |
| 3a | Hazırlık | 45 dk | Örnek veri, cevap anahtarı, kanıt planı, çekim profili kontrolü |
| 3b | **Elle koşu** | **görev süresi + 15 dk** (görev en fazla 60 dk; Bölüm 7.1) | `[ELLE SÜRE]`, elle koşu kaydı |
| 3c | Senaryo | 90 dk | Kilitli senaryo |
| 4 | Çekim | 50 dk | Ham ekran kayıtları, dolu `olcum.md` |
| 5 | Seslendirme | 55 dk | Temizlenmiş ses dosyası |
| 6 | Kurgu | 150 dk | Dışa aktarılmış video + altyazı dosyası |
| 7 | Kapak | 25 dk | 2–3 kapak varyasyonu |
| 8 | Yayınlama | 30 dk | Prompt dosyası yayında; zamanlanmış video |
| 9 | Performans analizi | 20 dk | Performans kaydında dolu satır + 1 çıkarım |
| 10a | Kısa video kesimi | 50 dk (2 × 25 dk) | 2 dikey ana dosya |
| 10b | Dağıtım | 20 dk | Shorts ve LinkedIn'e zamanlanmış kısa videolar |
| 10c | LinkedIn metin gönderisi | 15 dk | Gönderi |
| — | Yayın günü | 15 dk | Sabit yorum, ilk yorumlara yanıt |

**Toplam (tahmini):** elle koşu hariç **10 sa 25 dk**; elle koşu dahil, 60 dakikalık görevle **11 sa 40 dk**. Kontrol listelerini işaretleme süresi aşama sürelerinin içindedir (Bölüm 7.2).

Bu sayıya eklenenler:

| Ek | Süre (tahmini) | Ne zaman |
|----|----------------|----------|
| 12–14 dakikalık video | +65 dk (senaryo +20, seslendirme +15, kurgu +30) | 5. videodan sonra, 8–10 dakikalık videoların üretim süresi ölçülünce |
| Üçüncü kısa video | +25 dk kesim, +5 dk dağıtım | Bütçe tutuyorsa |
| TikTok ve Reels dağıtımı | +10–15 dk | Shorts + LinkedIn dağıtımı ölçümde 20 dakikanın altına inince (Bölüm 5.3) |
| Bülten sayısı | +20 dk | KM-011'den itibaren (Bölüm 5.6) |

---

### Aşama 1 — Konu araştırması

| | |
|---|---|
| **Amaç** | İzleyicinin kendi cümlesiyle aradığı, kronometreyle gösterilebilir tek bir görev seçmek. |
| **Girdi** | Fikir havuzu, önceki videoların yorumları, YouTube arama önerileri, performans kaydındaki çıkarımlar. |
| **Çıktı** | 01 belgesindeki filtreden 16 üzerinden 12+ puan almış bir fikir; `video-brief.md` üst yarısı dolu. |
| **Tahmini süre** | 30 dk |

**Adımlar**

1. YouTube arama kutusuna sorun cümlesinin ilk kelimelerini Türkçe yaz ("excel raporu ...", "toplantı notu ..."), otomatik tamamlama önerilerini olduğu gibi kopyala. Gizli sekmede yap; kendi geçmişin önerileri etkilemesin.
2. Aynı sorguyu Google Trends'te "YouTube araması" filtresiyle, Türkiye için aç; yalnızca **göreli** ilgiye ve ilgili sorgulara bak. Sorgu çok dar ise veri çıkmaz; bu, fikri öldürmez.
3. Sorgunun ilk sayfasındaki videolara bak: kaç tanesi Türkçe, kaç tanesi görevi baştan sona gösteriyor, kaç tanesi araç tanıtımı? Boşluk "görevi gerçek veriyle, süre tutarak gösteren yok" ise fikir güçlüdür.
4. Kendi kanalının ve benzer Türkçe videoların yorumlarından izleyici cümlelerini topla (Prompt P9 ile özetlet).
5. Fikri brief'teki iki kalıptan biriyle tek cümleye indir; süreler yer tutucu kalır: "[Kim], [hangi işi]; elle: [ELLE SÜRE], yapay zekâyla: [YZ SÜRE]."
6. 01 belgesindeki veto sorularını ve 8 ölçütlü puanlamayı doldur.
7. **Ön deneme (10 dk):** Görevi yapay zekâ aracıyla kabaca bir kez dene. Çekimde kullanacağın verinin **kendisini değil**, küçük bir parçasını ya da farklı bir kopyasını kullan. Hiç çalışmıyorsa veya fark küçükse fikir burada ölür; senaryodan sonra değil. Denemenin tarihini ve süresini brief'e yaz; çekimden sonra `olcum.md` içindeki "ön denemeler" tablosuna geçer.

**Yapay zekânın yaptığı:** Yorumları temalara ayırmak, bir konunun alt görevlerini listelemek, izleyici cümlesi varyasyonları üretmek (Prompt P1, P9).

**İnsanın mutlaka yaptığı:** Arama önerilerine kendi gözüyle bakmak, rakip videoları izlemek, puanlamayı yapmak, ön denemeyi çalıştırmak. Yapay zekâya "bu konu Türkiye'de ne kadar aranıyor" diye sorma; elinde bu veri yok, uydurur.

**"Bitti" tanımı:** Tek cümle yazıldı, puan 12+, ön deneme çalıştı ve kaydedildi, brief'in "Fikir" ve "İzleyici" bölümleri dolu.

---

### Aşama 2 — Paketleme

| | |
|---|---|
| **Amaç** | Başlık ve kapağı senaryodan önce sabitlemek; videonun tutacağı sözü belirlemek. |
| **Girdi** | Brief'in üst yarısı, izleyici cümlesi. |
| **Çıktı** | 3 başlık adayı, 3 kapak eskizi, vaat testinin cevabı (hangi bölümde söz tutuluyor). |
| **Tahmini süre** | 30 dk |

**Adımlar:** 01 belgesi Bölüm 2.1'deki dokuz adım aynen uygulanır. Burada yalnızca üretim tarafı:

1. Prompt P2 ile 15 başlık adayı üret; en az 5'ini sil, 3–4 tanesini kendin yeniden yaz. Yapay zekânın ilk listesi çoğunlukla kanal tonundan daha abartılı çıkar; sıfatları sil. Her adayın formül numarasını (F1–F16) brief'e yaz.
2. Kapak eskizini tasarım aracında değil kâğıtta ya da boş bir tuvalde kutularla çiz. Bu aşamada renk, font, hizalama yok.
3. Başlıkları telefonda not uygulamasına yapıştırıp bak: ilk 40–45 karakterde görev görünüyor mu? Karakter sayısını tabloda `=UZUNLUK()` ile ya da Studio'daki sayaçla ölç; asistanın yazdığı sayıya güvenme.
4. Brief'in "Başlık/kapak" ve "Vaat testi" alanlarını doldur.

**Yapay zekânın yaptığı:** Başlık varyasyonu, kapak etiketi için 1–2 kelimelik seçenekler (Prompt P2, P6).

**İnsanın mutlaka yaptığı:** Eleme, ton kontrolü, sayının ölçülmüş olup olmadığının kontrolü. Henüz ölçülmemiş sayı başlıkta `[YZ SÜRE]` olarak kalır.

**"Bitti" tanımı:** 3 başlık + 3 eskiz var; başlık ile kapak aynı bilgiyi tekrar etmiyor; vaat testinin cevabı bir bölüm adı.

---

### Aşama 3 — Hazırlık, elle koşu ve senaryo

| | |
|---|---|
| **Amaç** | Çekimde doğaçlamaya yer bırakmayan, yer tutucuları belli bir senaryo; ölçülmüş bir elle süre. |
| **Girdi** | Dolu brief, ön deneme notları. |
| **Çıktı** | Örnek veri seti ve cevap anahtarı, `[ELLE SÜRE]` ölçümü ve kaydı, kilitli senaryo (SES / EKRAN / Tutma notu sütunlarıyla). |
| **Tahmini süre** | Hazırlık 45 dk + elle koşu (görev süresi + 15 dk) + senaryo 90 dk |

**3a. Hazırlık (45 dk)**

1. **Örnek veri (20 dk):** Kurgusal şirket, gerçekçi ama kişisel veri içermeyen tablo/e-posta/belge. `00_VARLIKLAR/ornek-veri` içinde uygun set varsa onu kullan; yoksa yapay zekâya ürettir (Prompt P12).
2. **Tuzaklar ve cevap anahtarı (10 dk):** Veriye elle 2–3 "tuzak" yerleştir: tutarsız tarih biçimi, boş hücre, bariz aykırı değer. Hangi satırda ne olduğunu ayrı bir `cevap-anahtari.md` dosyasına yaz; toplamları tabloda kendin hesapla. Aracın tuzakları yakalayıp yakalamadığı "yapamadığı şey" bölümünün malzemesidir.
3. **Kanıt planı (5 dk):** Brief'teki tabloyu doldur: hangi iddia, hangi ekran kaydıyla kanıtlanacak.
4. **Çekim düzeni kontrolü (10 dk):** Çekim profilini aç, kronometre penceresini yerine koy, 10 saniyelik deneme kaydı al (Aşama 4, adım 1–3). Elle koşu da bu düzenle kaydedilir.

**3b. Elle koşu (görev süresi + 15 dk)**

5. `olcum.md` şablonunu video klasörüne kopyala, "Elle koşu" bölümünü aç.
6. Kronometreyi "ELLE" etiketiyle başlat, görevi yapay zekâsız baştan sona yap, ekranı kaydet. Düşünme, yanlış yapıp düzeltme, kontrol süreye dahildir. Bu kayıt hızlandırılmış B-roll olur.
7. Biter bitmez süreyi ve nerede zaman kaybettiğini `olcum.md` içine yaz (15 dk'nın 5'i). Kalan 10 dk kurulum ve dosya adlandırmadır.

Görev 60 dakikadan uzunsa bu oturum haftaya sığmaz; hangi yolla ölçüleceği Bölüm 7.1'de.

**3c. Senaryo (90 dk)**

8. **İskelet (15 dk):** Senaryo şablonundaki bölümleri başlıklarıyla yaz; her bölüme tek cümle.
9. **Taslak (40 dk):** Prompt P4 ile iskeletten taslak al (5 dk). Taslağı **kendi cümlelerinle baştan yaz** (35 dk); taslak yapıyı hızlandırır, sesini vermez. Sonuç, ölçüm ve görüş satırlarına yapay zekâ bir şey yazdıysa sil, yer tutucu koy. 10 dakikada toparlanmayan taslağı at, iskeletten kendin yaz.
10. **Sesli okuma (20 dk):** Senaryoyu baştan sona yüksek sesle oku, süreyi ölç; dilin takıldığı her cümleyi kısalt. İlk senaryoda kelime sayısını okuma süresine böl, **kendi dakikada kelime hızını** bul ve P0'a yaz; P4 hedef uzunluğu bundan hesaplar.
11. **Eleştiri turu (10 dk):** Prompt P5 ile eleştiri al; önerilerden en fazla 3'ünü uygula.
12. **Kilit (5 dk):** `kalite-kontrol-listeleri.md` → "Senaryo kilidi".

Senaryoda kronometre koşusunun prompt'ları önceden yazılıdır. Bu, ölçümün koşulunu değiştirir ve videoda söylenir (Aşama 4, "Ölçümün dürüstlük kuralı").

**Yapay zekânın yaptığı:** Örnek veri üretimi, iskeletten taslak, tekrar ve dolgu avı, "burada izleyici neden çıkar" eleştirisi, hook varyasyonları (Prompt P3, P4, P5, P12).

**İnsanın mutlaka yaptığı:** Elle koşu, tuzakların yerleştirilmesi, kanıt planı, son yazım, sesli okuma. Hook'un ve "yapamadığı şey" bölümünün son hâli insan elinden çıkar.

**"Bitti" tanımı:** Senaryo kilidi listesinin kapısı tamam; yer tutucuların hepsi listelenmiş; sesli okuma süresi hedef aralıkta (ilk 4 videoda 8–10 dk); `olcum.md` içinde elle koşu satırı dolu.

---

### Aşama 4 — Çekim (ekran kaydı)

| | |
|---|---|
| **Amaç** | Görevin gerçekten yapıldığı, kesintisiz ve okunaklı ekran kaydı; gerçek ölçüm. |
| **Girdi** | Kilitli senaryo, örnek veri, temiz çekim profili. |
| **Çıktı** | Bölüm bölüm ham kayıtlar, dolu `olcum.md`, aracın verdiği cevapların metin kopyası. |
| **Tahmini süre** | 50 dk (ön kontrol 8, süreli koşu tahmini 10–15, `olcum.md` 5, ek çekimler 12, yer tutucuları doldurma 10) |

**Adımlar**

1. **Çekim profili:** Ayrı tarayıcı profili (yer imi çubuğu kapalı, kişisel hesap adı görünmüyor), bildirimler kapalı, masaüstü boş. İmleci işletim sisteminin erişilebilirlik ayarından büyüt (Windows: Ayarlar → Erişilebilirlik → Fare işaretçisi; macOS: Sistem Ayarları → Erişilebilirlik → Ekran → İmleç boyutu). Deneme kaydında büyütülmüş imlecin göründüğünü kontrol et. Tıklama vurgusu istiyorsan kurguda ekle; OBS Studio'da yerleşik imleç vurgusu yoktur, üçüncü taraf betik ya da eklenti gerekir ve bunların bir kısmı yalnızca Windows'ta çalışır.
2. **Çözünürlük ve okunabilirlik:**
   - Ekranın izin veriyorsa kaydı **2560×1440 ya da daha yüksek** çözünürlükte al, kurgu zaman çizelgesini 1080p tut. Kurguda %133'e kadar büyütme kayıpsız olur; %200 büyütme için 4K kayıt gerekir.
   - Ekranın 1080p ise büyütmeyi kurguda değil **çekimde** yap: tarayıcı yakınlaştırması %175–200, pencere dar. Kurgudaki büyütmeyi %130 ile sınırla; üstü yazıyı bulandırır.
   - 30 kare/sn. Ayarları bir kez yap, profil olarak kaydet.
   - Deneme karesini kurgudaki en büyük yakınlaştırma ön ayarıyla büyüt, telefona at: yazı okunuyor mu?
3. **Kronometre kayda gömülür.** `kronometre.html` dosyasını küçük bir tarayıcı penceresinde aç, kayıt karesinin sağ üst köşesine yerleştir; çalışma penceresi onu örtmesin (pencereyi "her zaman üstte" tutabiliyorsan tut; işletim sisteminde yerleşik değilse çalışma penceresini bir şerit dar bırak). Kronometre görüntünün parçası olduğu için kurguda kesim, hızlandırma ve bekleme atlama rakamları kendiliğinden doğru bırakır. Kurguda yalnızca çerçeve, "ELLE / YAPAY ZEKÂ" etiketi ve "hızlandırıldı ×N" notu eklenir; **rakam kurguda yazılmaz.**
4. **Süreli koşu tek, kesintisiz kayıttır.** Neyin sayıldığı 01 belgesi Bölüm 6.1'de tanımlıdır: izleyicinin işi yaparken gerçekten yapacağı ilk adımda (malzemeyi açma, prompt'u yazma ya da yapıştırma) kronometre başlar; cevabı bekleme, uygulama, kontrol ve düzeltme turları dahildir; işe yarar çıktı elindeyken durur. Koşu **yeni, boş bir sohbette** yapılır.
5. Koşu bittiğinde hemen `olcum.md` içindeki "Yapay zekâ koşusu" bölümünü doldur: tarih, araç ve o gün arayüzde görünen model adı, başlangıç/bitiş, toplam süre, düzeltme turu, karşılaşılan hata, **ön deneme sayısı ve toplam süresi**, **prompt hazır mıydı**.
6. Aracın cevaplarını metin olarak da kaydet (kopyala-yapıştır → `arac-ciktilari.md`). Kurguda büyütme, açıklamada alıntı ve prompt dosyası için gerekir.
7. **Süre dışı ek çekimler (ayrı kayıtlar, kronometre durmuş):** önce/sonra karşılaştırma ekranı, "yapamadığı şey" için ek deneme, prompt'un tam ekran görüntüsü. Bunlar süreli sohbete yazılmaz; kurguda "Ayrı sohbet · süre dışı" etiketi alır (01 belgesi 6.1).
8. Çekimden hemen sonra senaryodaki yer tutucuları doldur; ölçüm başlıktaki çalışma sayısından farklıysa başlık ve kapak değişir.

**Ölçümün dürüstlük kuralı**

Süreli koşu ilk deneme değildir: en az bir ön deneme yapılmış ve prompt senaryoda önceden yazılmıştır. `[ELLE SÜRE]` düşünme süresini içerir, `[YZ SÜRE]` prompt'u tasarlama süresini içermez. Karşılaştırma bu hâliyle yapay zekâ lehine yanlıdır; yanlılık gizlenmez, ölçülür ve söylenir:

- **`[KURULUM SÜRE]`** = ön denemelerin toplam süresi + prompt'u yazıp düzeltme süresi. `olcum.md` içinde ayrı satırdır.
- **Videoda sabit cümle** (karşılaştırma bölümünde, bir kez): "Prompt'u önceden [N] denemede hazırladım; bu süre hazır prompt'la. İlk kez yapan için hazırlık dahil [KURULUM SÜRE] daha ekle."
- **Karşılaştırma tablosunda ayrı satır:** "İlk kurulum (bir kez): [KURULUM SÜRE]". Kapağa ve başlığa giren süre `[YZ SÜRE]` değeridir; kurulum satırı videoda ve açıklamadaki "Nasıl ölçtüm" bloğunda durur.
- **Sıra etkisi** de aynı yerde tek cümleyle söylenir: elle koşu önce yapıldığı için yapay zekâlı turda malzeme tanıdıktı.
- Süreli koşuyu bir nedenle tekrar çektiysen (kayıt bozuldu, araç hata verdi) `olcum.md` içine kaçıncı koşu olduğunu ve nedenini yaz; daha iyi çıkan koşuyu seçmek için tekrar çekilmez. Kullanılan koşu ilk koşu değilse videoda söylenir.

**Yapay zekânın yaptığı:** Bu aşamada üretimde rolü yok; videonun **konusu** olarak ekranda. Çekim sonrası yer tutucuları doldururken cümle önerisi alınabilir, sayı ve sonuç elle girilir.

**İnsanın mutlaka yaptığı:** Koşunun kendisi, ölçüm, hata notu, `olcum.md`.

**"Bitti" tanımı:** Süreli koşu baştan sona tek dosyada ve kronometre karede; `olcum.md` dolu (ön deneme ve kurulum satırları dahil); senaryoda yer tutucu kalmadı; ham dosyalar adlandırılıp yedeklendi.

---

### Aşama 5 — Seslendirme

| | |
|---|---|
| **Amaç** | Sakin, net, işini bilen bir iş arkadaşı gibi duyulan ses. |
| **Girdi** | Yer tutucuları dolmuş senaryo. |
| **Çıktı** | Bölüm bölüm kaydedilmiş, temizlenmiş, seviyesi eşitlenmiş ses. |
| **Tahmini süre** | 55 dk (kayıt 30 + temizlik 15 + baştan sona dinleme 10). 8–10 dakikalık metin, hook'un üç denemesi ve cümle tekrarlarıyla kayıt tek başına 25–30 dk tutar. |

**Adımlar**

1. Aynı oda, aynı mikrofon mesafesi (bir karış), aynı saat dilimi. Halı, perde, kıyafet dolabı yankıyı azaltır; pahalı mikrofondan önce oda gelir.
2. Bölüm bölüm kaydet. Hata yaptığında durma: bir saniye sus, cümleyi baştan söyle, devam et. Kurguda dalga biçiminde boşluktan bulursun.
3. Hook'u (ilk 30 saniye) en az 3 kez kaydet, en doğal olanı seç.
4. Temizlik: gürültü azaltma, seviye eşitleme, sessizlik kırpma. Ön ayar olarak kaydet, her videoda aynı zincir.
5. Baştan sona bir kez kulaklıkla dinle; tekrar kaydedilecek cümleleri aynı oturumda, aynı mesafeden kaydet.

**Yapay zekânın yaptığı:** Gürültü temizleme, sessizlik kesme, dolgu sesi ("ııı") işaretleme, yazıya dökme.

**İnsanın mutlaka yaptığı:** Konuşmanın kendisi (bu kanal için karar ve gerekçe: Bölüm 4.3), son dinleme.

**"Bitti" tanımı:** Seslendirme kapısı tamam (`kalite-kontrol-listeleri.md` Bölüm 4): tek parça dinlemede tekrar kaydedilecek cümle yok; seviye bölümler arasında tutarlı; dosya adlandırıldı.

---
### Aşama 6 — Kurgu

| | |
|---|---|
| **Amaç** | Sesi omurga alıp ekranı ona göre dizmek; izleyicinin gözünü her an doğru yere götürmek. |
| **Girdi** | Temiz ses, ham ekran kayıtları, varlık kütüphanesi, proje şablonu. |
| **Çıktı** | Dışa aktarılmış video, düzeltilmiş altyazı dosyası (.srt), bölüm zaman damgaları. |
| **Tahmini süre** | 150 dk (8–10 dakikalık video için) |

**Adımlar (sırayı bozma)**

1. **Proje şablonunu aç, sesi diz (20 dk).** Boş proje açma; kanal düzeni, alt bant, müzik kanalı hazır gelsin. Sesi diz, yanlış denemeleri at. Görüntüye dokunma.
2. **Kaba görüntü (30 dk):** Ekran kayıtlarını sese hizala. Bekleme anlarını (aracın cevap üretmesi) hızlandır ya da kes; her birine "hızlandırıldı ×N" etiketi koy. Kronometre kayıtta gömülü olduğu için rakamlar kendiliğinden hızlanır ya da ileri atlar; elle düzeltme yapma.
3. **Yönlendirme (30 dk):** Yakınlaştırma, vurgu kutusu, imleç takibi. Kural: izleyicinin okuması gereken her şey ekranın en az üçte birini kaplamalı. Büyütme sınırı kayıt çözünürlüğüne bağlıdır (Bölüm 6.4).
4. **Sabit grafikler (15 dk):** Kronometre çerçevesi ve etiketi, alt bantlar, karşılaştırma tablosu (kurulum satırıyla), "yapamadığı şey" kartı, prompt kartı. Hepsi şablondan; yalnızca metin değişir.
5. **Müzik ve ses seviyesi (8 dk):** Müzik konuşmanın belirgin altında; hook'ta ve bölüm geçişlerinde biraz yukarı.
6. **Altyazı (20 dk):** İki yoldan biri:
   - **Senaryodan senkronizasyon:** Senaryonun SES sütununu düz metin olarak YouTube Studio'da altyazı ekranına yapıştır, "otomatik senkronize et"i seç. **[Resmî — arama sonucu üzerinden]** YouTube Yardım'a göre bu yol, metnin dili konuşma tanımanın desteklediği bir dilse ve videoda konuşulan dille aynıysa çalışır. Türkçe için çalışıp çalışmadığını Bölüm 0.1'deki gizli test videosunda sına; çalışıyorsa süre 10 dakikaya iner, çünkü metin zaten doğrudur.
   - **Otomatik döküm + düzeltme:** Whisper tabanlı bir araçla (Bölüm 3.1) .srt üret; özel adları ve terimleri elle düzelt ("prompt", araç adları, "yapay zekâ"). 10 dakikalık Türkçe döküm için 20 dk ayır.
7. **Telefonda izleme ve düzeltme (25 dk):** Dışa aktar, telefona at, 1× hızda baştan sona izle (video süresi kadar sürer; hızlandırma). Okunmayan yazı, uzun bekleme, senkron kayması için not al; yalnızca bu notları düzelt, yeniden dışa aktar.
8. **Kurgu kapısı (2 dk):** `kalite-kontrol-listeleri.md` → "Kurgu".

**Yapay zekânın yaptığı:** Yazıya dökme ve metin üzerinden kesme, sessizlik atma, altyazı taslağı, bölüm başlığı önerisi (Prompt P7).

**İnsanın mutlaka yaptığı:** Neyin büyütüleceğine karar vermek, karşılaştırma tablosundaki sayıları `olcum.md` ile karşılaştırmak, telefonda izleme.

**"Bitti" tanımı:** Kurgu kapısı tamam; telefonda izleme notları kapandı; ikinci bir "son rötuş" turu açılmadı.

---

### Aşama 7 — Kapak

| | |
|---|---|
| **Amaç** | Aşama 2'deki eskizi, ölçülen sayı ve gerçek ekran görüntüsüyle son hâline getirmek. |
| **Girdi** | Kapak şablon dosyası, `olcum.md`, çekimden bir ekran görüntüsü. |
| **Çıktı** | 2–3 varyasyon (16:9, en az 1280×720; güncel boyut ve dosya sınırı için Studio'daki yükleme ekranına bak), biri ana kapak. |
| **Tahmini süre** | 25 dk |

**Adımlar**

1. Şablonu çoğalt, sayıyı `olcum.md` içindekiyle değiştir. **Yuvarlama kuralı:** yapay zekâ süresi her zaman **yukarı**, elle süre her zaman **aşağı** yuvarlanır; iddia hiçbir zaman ölçümden iyi görünmez.

   | Ölçüm | Kapakta |
   |-------|---------|
   | Yapay zekâyla 13 dk 20 sn | 14 dk (bir üst tam dakika) |
   | Yapay zekâyla 13 dk 40 sn | 14 dk |
   | Elle 2 sa 40 dk | 2,5 sa (bir alt yarım saat) |
   | Elle 47 dk | 45 dk (bir saatin altında: bir alt 5 dakika) |

   Başlıkta, açıklamada ve kısa videolarda aynı yuvarlanmış değer kullanılır; ham değer `olcum.md` içinde ve açıklamadaki "Nasıl ölçtüm" bloğunda durur.
2. Görev etiketini (1–2 kelime) ve ekran görüntüsü parçasını yerleştir.
3. Varyasyonları 01 belgesi Bölüm 3'teki üç yerleşime (A / B / C) ve dönüşüm çifti kuralına göre üret.
4. Kapağı ekranda başparmak tırnağı boyutuna küçült; sayı hâlâ okunuyor mu?
5. Önceki kapaklarla yan yana koy: aynı kanaldan olduğu belli, ama bir öncekinin kopyası değil.

**Yapay zekânın yaptığı:** Etiket metni seçenekleri (Prompt P6), arka plan temizleme/büyütme gibi teknik işler. **Kapaktaki ekran görüntüsü gerçek çekimden gelir;** üretilmiş sahte arayüz görüntüsü kullanma.

**İnsanın mutlaka yaptığı:** Sayı ve yuvarlama kontrolü, küçük boyut testi, seçim.

**"Bitti" tanımı:** Kapak ve başlık kapısı tamam.

---

### Aşama 8 — Yayınlama

| | |
|---|---|
| **Amaç** | Videoyu eksiksiz metaveriyle, izleyicinin sözü hemen bulacağı şekilde yayına almak. |
| **Girdi** | Video dosyası, kapak, .srt (ya da senaryo metni), zaman damgaları, `olcum.md`, çekimde kullanılan prompt'lar. |
| **Çıktı** | Yayında prompt dosyası; zamanlanmış video; oynatma listesine eklenmiş; performans kaydında açık satır. |
| **Tahmini süre** | 30 dk (prompt dosyası 10 + metaveri 10 + yükleme ve ayarlar 10) |

**Ön koşul:** Bölüm 0'daki kanal kurulumu tamam. İlk videoda bu, yayın öncesi kapının ilk maddesidir.

**Adımlar**

1. **Prompt dosyası (10 dk):** Bölüm 5.5'teki akış. Prompt'u yeni bir sohbette yeniden dene, `prompt-dosyasi.md` şablonunu doldur, sayfayı yayınla, dizine ekle, bu video için kısa bağlantıyı oluştur, gizli sekmede aç.
2. `yayin-metaverisi.md` şablonunu doldur (açıklama taslağı için Prompt P7; ölçümleri ve bağlantıları elle kontrol et). Prompt'un **tam metni** açıklamada durur; bağlantı ek olarak verilir.
3. Videoyu yükle, altyazıyı ekle, bölümleri açıklamaya yaz. **[Resmî — yayın öncesi doğrula]** Bölümlerin otomatik oluşması için bilinen koşullar: ilk zaman damgası 0:00, en az üç zaman damgası, her bölüm en az 10 saniye.
4. "Değiştirilmiş içerik" sorusunu Bölüm 4.4'e göre yanıtla.
5. Bitiş ekranı ve kartları ekle; oynatma listesine koy.
6. Zamanla. Yayın günü ve saati sabit olsun; hangi saat olduğu veri gelene kadar ikincil. Studio'daki "izleyicileriniz ne zaman YouTube'da" raporu dolunca oradan ayarla.
7. Yayın öncesi kapıyı işaretle; **sayı tutarlılığı** kontrolü buradadır.
8. Yayına girince (yayın günü, 15 dk) sabit yorumu yaz ve sabitle; sabitleme açık değilse Bölüm 0.3.

**Yapay zekânın yaptığı:** Açıklama taslağı, bölüm başlıkları, sabit yorum sorusu için seçenekler (Prompt P7).

**İnsanın mutlaka yaptığı:** Prompt'un yeniden denenmesi, bağlantı testi, beyan kararı, sayı tutarlılığı.

**"Bitti" tanımı:** Yayın öncesi kapı tamam; video zamanlandı; `performans-kaydi.md` içinde satır açıldı.

---

### Aşama 9 — Performans analizi

| | |
|---|---|
| **Amaç** | Her videodan bir sonraki videoyu değiştirecek **tek** çıkarım almak. |
| **Girdi** | YouTube Studio verileri, yorumlar, brief'teki hipotez, kısa bağlantının tıklama sayısı. |
| **Çıktı** | Performans kaydında 48 saat / 7 gün / 28 gün satırları; bir çıkarım; gerekiyorsa bir paket değişikliği. |
| **Tahmini süre** | Haftada 20 dk (48 saat kontrolü 10 dk + geçmiş videoların 7/28 gün satırları 10 dk). Kapsamlı haftalık rutin `02-buyume-stratejisi.md` B8'dedir. |

**Adımlar**

1. **48 saat:** Gösterim, tıklanma oranı, ortalama görüntüleme süresi, ilk 30 saniyede kalan izleyici oranı, trafik kaynakları. Tutma grafiğinde en dik iki düşüşün zaman damgasını ve o anda ekranda ne olduğunu yaz.
2. Yorumları oku, soruları yanıtla; tekrar eden soru bir sonraki videonun adayıdır.
3. **7 gün:** Aynı metrikler + kazanılan abone + prompt bağlantısı tıklaması. Tıklama sayısı YouTube Studio'dan **gelmez;** kısa bağlantı aracının panelinden okunur (Bölüm 5.5). Kısa bağlantı kurulmadıysa hücreye `[ölçüm yok]` yaz, 0 yazma. Kanal medyanıyla karşılaştır (ilk 5 videoda medyan anlamlı değil; yalnızca kaydet).
4. **28 gün:** Arama ve önerilen trafik payı; hangi arama terimleri getirmiş.
5. Verileri Prompt P10'a yapıştırıp yorum iste; yorumu sorgula, tek çıkarımı kendin yaz.
6. Başlık/kapak değişikliği kararı: tek seferde tek değişken, değişiklik tarihini kayda yaz.

**Yapay zekânın yaptığı:** Yapıştırılan sayılardan örüntü önerisi, yorum temaları (Prompt P9, P10). P9'un verdiği yorum sayıları yaklaşıktır; bir karar o sayıya dayanacaksa yorumları kendin say.

**İnsanın mutlaka yaptığı:** Sayıları Studio'dan almak (yapay zekâ kanal verini göremez), tutma düşüşünde ekranda ne olduğuna bakmak, çıkarımı yazmak. Küçük kanalda tek videonun verisi gürültülüdür; 3 videoda tekrar eden örüntüye "bulgu", tek videodakine "ipucu" de.

**"Bitti" tanımı:** Kayıtta ilgili satır dolu; "bir sonraki videoda değiştireceğim tek şey" cümlesi yazıldı.

---

### Aşama 10 — Kısa formata uyarlama: kesim ve dağıtım

| | |
|---|---|
| **Amaç** | Uzun videonun en güçlü 2 anını, kendi başına anlaşılır dikey videolara çevirmek ve hedef kitlenin olduğu yerlerde yayınlamak; LinkedIn için metin çıkarmak. |
| **Girdi** | Bitmiş uzun video projesi (hâlâ açık), zaman kodlu transkript, `olcum.md`, senaryodaki kısa video işaretleri. |
| **Çıktı** | 2 dikey ana dosya (filigransız), platform başına açıklama, zamanlanmış gönderiler, LinkedIn metin gönderisi. |
| **Tahmini süre** | Kesim 50 dk (2 × 25 dk) + dağıtım 20 dk + LinkedIn metni 15 dk |

**10a. Kesim (iki video için 50 dk: ortak adımlar 6 dk + video başına 22 dk)** — ayrıntılı kurallar Bölüm 5.2'de

1. Transkripti Prompt P8'e ver; 6 aday an iste (3 dk, iki kısa video için bir kez).
2. Adayları kendin izle, 2'sini seç (3 dk).
3. Dikey zaman çizelgesinde yeniden çerçevele: ilgili ekran bölgesi, üstte başlık bandı, altta altyazı (10 dk).
4. Yeni açılış cümlesini kaydet ve yerleştir (4 dk).
5. Gömülü altyazıyı ekle, yazımı elle düzelt (6 dk).
6. Filigransız dışa aktar, telefonda sessiz izle (2 dk).

**10b. Dağıtım (hafta başına 20 dk)**

7. `yayin-metaverisi.md` Bölüm 9'u doldur: Shorts başlığı ve açıklaması, LinkedIn video metni (5 dk).
8. Shorts'a yükle; "ilgili video"yu uzun videoya ayarla (özellik açıksa); zamanla (2 × 4 dk).
9. LinkedIn'e kısa videolardan birini yükle ya da metin gönderisine ekle; zamanla (5 dk).
10. Yayın sırasını ve tarihlerini `performans-kaydi.md` Bölüm 3'e yaz (2 dk).

İlk 4 hafta dağıtım **yalnızca Shorts + LinkedIn**'dir. TikTok ve Reels, bu iki platformun dağıtımı ölçümde 20 dakikanın altına indiğinde eklenir (Bölüm 5.3).

**10c. LinkedIn metin gönderisi (15 dk)** — Bölüm 5.4; taslak için Prompt P11.

**Yapay zekânın yaptığı:** Transkriptten aday an bulma, yeni açılış cümlesi ve üst başlık önerisi (P8); gömülü altyazı taslağı; LinkedIn taslağı (P11); platform açıklaması taslağı.

**İnsanın mutlaka yaptığı:** Adayı izleyip seçmek (P8 görüntüyü görmez; ses kapalıyken anlaşılırlığı yalnızca sen sınarsın), yeniden çerçeveleme kararı, açılış cümlesini kendi sesinle kaydetmek, kısa videodaki sayıyı `olcum.md` ile karşılaştırmak, yükleme ekranındaki yapay zekâ etiketi sorusunu yanıtlamak (Bölüm 4.4 C).

**"Bitti" tanımı:** Kısa video kapısı iki video için tek geçişte işaretlendi; dosyalar zamanlandı; her kısa videoda uzun videoya yönlendirme var; yayın sırası kayıtta.

---

### 1.11 Hikâye yapısına göre üretim farkları

Bölüm 1'deki süreler Kronometre Yarışı (KG1) içindir. İlk 10 videonun yalnızca ikisi (Yayın 2 ve 5) bu yapıdadır. Diğer yapılarda değişen adımlar ve tahmini süre farkı:

| Yapı (01 belgesi Bölüm 6) | İlk 10'da | Elle koşu | Çekimde değişen | Ek adım | Tahmini fark |
|---|---|---|---|---|---|
| **KG1 Kronometre Yarışı** | Yayın 2, 5 | Var; tek görev | — | — | Temel |
| **KG3 Hata Listesi** | Yayın 1, 6, 10 | Yayın 1'de tek görev (kısa). Yayın 6 ve 10'da görev başına ayrı elle süre yok; ölçülen şey "çalıştı / çalışmadı" ve madde başına önce/sonra çıktısı | Tek süreli akış + madde başına "ayrı sohbet · süre dışı" kısa kayıtlar | Yayın 10: önceki videoların ham kayıtlarından kesit bulmak | Çekim +25 dk, senaryo +15 dk; Yayın 10'da kurgu +30 dk, elle koşu 0 |
| **KG6 Kör Test** | Yayın 3 | Yok | 5 görev × 3 araç = 15 koşu; her araç için yeni sohbet, aynı prompt, aynı gün. Tek oturuma sığmaz | Ölçütleri testten önce yazmak; ikinci puanlayıcı bulmak, izin almak, kör puanlama oturumu | Çekim 50 dk → tahmini 150–180 dk (iki oturum); puanlama +45 dk; kurgu +45 dk (üçlü yan yana düzen) |
| **KG7 Adım Adım Başlangıç** | Yayın 4 | Yok | Adım başına kısa kayıt + alıştırma kartları | "30 dakika" iddiası için bir deneme izleyicisiyle uygulama süresini ölçmek (izinle) | Deneme oturumu +60 dk; kurgu +20 dk (kartlar) |
| **KG5 Meslek Vakası** | Yayın 7 | İş başına kısa elle ölçüm ya da meslekten birinin beyanı; ikisi ekranda ayrı etiketle | 3–5 mini koşu, her biri ayrı süreli kayıt | Meslekten kişi bulmak, görüşme, yazılı izin; mevzuat içeren cümlelerin birincil kaynaktan doğrulanması | Görüşme +45 dk; çekim +40 dk; doğrulama +30 dk |
| **KG2 Önce/Sonra + hakem** | Yayın 8 | "Önce" çıktısını elle hazırlamak elle koşunun yerini tutar | İki sürümün hazırlanışı + hakemin kör değerlendirmesinin kaydı | Hakem bulmak, yazılı izin (ses/görüntü kapsamıyla), değerlendirme oturumu | Oturum +45 dk; kurgu +30 dk (görüşme kaydı) |
| **KG4 Süreli Deney** | Yayın 9 | Taban ölçümü: deneyden önceki hafta aynı tür işte elle ortalama süre | Tek çekim oturumu yok; 5–7 gün boyunca günde 10–15 dk kayıt + günlük | Kuralları ve sayılacak metrikleri deneyden önce yazmak; günlük sayım tablosu | Günlük toplam +70–100 dk iki haftaya yayılır; kurgu +45 dk (malzeme seçimi) |

Bu yapılarda şablonların nasıl uyarlanacağı `senaryo-sablonu.md` içindeki "Kronometre Yarışı dışındaki yapılar" tablosundadır.

**İlk 10 video için önden başlatılacak işler** (yayın haftası = Y; üretim haftası = Y−1, stok kuralı gereği):

| Yayın | Ne | En geç ne zaman başlar |
|-------|----|------------------------|
| 3 (kör test) | Ölçütleri yaz; ikinci puanlayıcıyı ayarla; üç araçta hesapların açık olduğunu kontrol et | Y−3 |
| 4 (başlangıç) | Deneme izleyicisini bul (aracı hiç kullanmamış biri), oturum gününü belirle | Y−3 |
| 7 (muhasebeciler) | Meslekten kişiyi bul; `izin-onay.md` gönder; hangi işlerin süresini beyan edeceğini konuş | **Y−3** |
| 8 (CV + İK uzmanı) | Hakemi bul; `izin-onay.md` gönder; kör değerlendirme oturumunu takvime koy | **Y−3** |
| 9 (bir haftalık e-posta) | Taban haftası (elle süreler) | Y−4; deney haftası Y−3, üretim Y−2 ve Y−1 |
| 10 (10 prompt) | Önceki 9 videonun ham kayıtlarında kullanılacak kesitleri işaretle | Her videonun çekim sonrası kapısında, tek satır not |

Konuk bulunamazsa video ertelenir, yerine stoktaki yedek video (`senaryolar/03-prompt-yazmanin-tek-formulu.md`) girer. Konuğun yerine uydurma "bir uzman" konmaz.

---

## 2. Haftalık üretim takvimi

### 2.1 Standart hafta (tahmini 10 sa 25 dk + elle koşu)

Günler örnektir; oturumların **sırası** ve **bloklar hâlinde** yapılması önemlidir. Yayın günü perşembe varsayıldı. Takvim Bölüm 2.2'deki stok kuralına göre kurulur: **bu hafta üretilen video gelecek perşembe yayınlanır;** bu perşembe yayınlanan video geçen hafta bitmiştir.

Aşağıda N = bu perşembe yayınlanan video, N+1 = bu hafta üretilen video, N−1 = geçen perşembe yayınlanan video.

| Gün | Üretilen video (N+1) | Yayınlanan videolar (N ve N−1) | Süre |
|-----|----------------------|--------------------------------|------|
| Cumartesi | Araştırma + paketleme + hazırlık (1 sa 45 dk) | N−1: 48 saat kontrolü ve geçmiş satırlar (20 dk) + LinkedIn metin gönderisi (15 dk) | 2 sa 20 dk |
| Cumartesi | **Elle koşu: görev süresi + 15 dk** (en fazla 1 sa 15 dk) | — | ≤ 1 sa 15 dk |
| Pazar | Senaryo (1 sa 30 dk) | — | 1 sa 30 dk |
| Pazartesi | Çekim (50 dk) + seslendirme (55 dk) | — | 1 sa 45 dk |
| Salı | Kurgu 1: ses dizimi, kaba görüntü, yönlendirme (1 sa 20 dk) | N: uzun videodan **önce** gidecek kısa video yayında (geçen hafta kesildi ve zamanlandı) | 1 sa 20 dk |
| Çarşamba | Kurgu 2: grafik, müzik, altyazı, telefonda izleme (1 sa 10 dk) + kapak (25 dk) | — | 1 sa 35 dk |
| Perşembe | Kısa video kesimi, 2 video (50 dk); kurgu dün bitti, proje aynı hâliyle duruyor | **N yayında:** sabit yorum, ilk yorumlara yanıt (15 dk) | 1 sa 5 dk |
| Cuma | Yayın hazırlığı: prompt dosyası, metaveri, yükleme, gelecek perşembeye zamanlama (30 dk) + N+1'in kısa videolarının dağıtımı ve zamanlaması (20 dk) | N: uzun videodan **sonra** gidecek kısa video yayında (geçen hafta zamanlandı) | 50 dk |

Toplam: 11 sa 40 dk (60 dakikalık elle görevle). Elle koşusu olmayan yapılarda (Bölüm 1.11) 10 sa 25 dk.

Kısa videoların yayın dağılımı: uzun videodan **önce** 1 (merak uyandıran an, salı), **sonra** 1 (cuma). Üçüncü kısa video kesildiyse ertesi pazartesi. Hangisinin önce gittiğini kayda yaz; üç dört hafta sonra fark var mı bak.

En uzun gün cumartesidir (elle koşuyla 3 sa 35 dk). Sığmıyorsa elle koşu bir önceki haftanın cuma akşamına alınır; senaryodan sonraya **alınmaz**, çünkü senaryonun hook'u elle süreye yaslanır.

`02-buyume-stratejisi.md` B2'deki haftalık takvim bu tablonun üstüne büyüme işlerini (yorum cevapları, haftalık analiz rutini, topluluk gönderileri) ekler.

### 2.2 Önde gitme kuralı

Her zaman **yayına hazır 1 video stokta** olsun. İlk videoyu yayınlamadan önce 2 videoyu bitir: biri ilk perşembe yayınlanır, diğeri ikinci perşembenin videosudur ve sen o hafta üçüncüyü üretirsin. Hastalık, yoğun iş haftası ya da çöken bir deney ritmi bozmaz. Stok 0'a düşerse o hafta daha kısa bir B kategorisi videosu (ör. tek alışkanlık, tek prompt) çek ya da yedek videoyu yayınla; yayın atlamaktansa kapsamı küçült.

Stok kuralının ölçüme etkisi: çekim ile yayın arasında en az bir hafta vardır. Araç bu arada değiştiyse Bölüm 7.4'teki karar uygulanır; açıklamadaki "Çekim tarihi" satırı bu yüzden zorunludur.

### 2.3 Toplu üretim (batch)

| Ne | Sıklık | Gerekçe | Sınır |
|----|--------|---------|-------|
| **Araştırma + brief:** 4 fikir tek oturumda (tahmini 90 dk) | Ayda 1 | Süre kazancı yoktur (fikir başına 22 dk + haftalık 10 dk gözden geçirme, haftalık 30 dakikayla aynı). Gerekçe bağlam değiştirmemek ve dört fikri yan yana görüp sırayı doğru kurmaktır | Ön denemeyi fikir başına ayrı yap; araç davranışı çekim haftasına kadar değişebilir |
| **Senaryo:** 2 senaryo art arda | 2 haftada 1 | İkinci senaryo ilkinin ritmiyle yazılır | 2'den fazla senaryoyu önden yazma; ölçüm ve araç davranışı eskir |
| **Çekim + ses:** 2 video aynı oturumda | 2 haftada 1 | Kurulum, ses ayarı ve çekim profili bir kez yapılır; ses tonu tutarlı kalır | K kategorisi (araç testleri) toplu çekilmez; yayına yakın çekilir |
| **Kısa videolar:** uzun videonun kurgusu bittikten sonraki gün, proje hâlâ açıkken | Her hafta | Anı yeniden bulma maliyeti düşük | Kurgunun bittiği gün kesme; telefonda izleme notları kapanmadan kısa video çıkmaz |
| **Kapak:** şablondan, kurgu oturumunun sonunda | Her hafta | Tasarım aracını ayrıca açıp "biraz daha oynama" tuzağı kapanır | — |
| **Metaveri sabitleri:** açıklama alt bloğu, etiketler, bitiş ekranı düzeni | Bir kez | Her yayında aynı blok yapıştırılır | Üç ayda bir gözden geçir |

İki haftalık parti düzeni (isteğe bağlı), sayılar Bölüm 1'deki tablodan türetilmiştir:

| | İçerik | Tahmini süre |
|---|--------|--------------|
| **A haftası** | 2 × (araştırma 30 + paketleme 30 + hazırlık 45 + senaryo 90 + çekim 50 + seslendirme 55) | 10 sa + elle koşular |
| **B haftası** | 2 × (kurgu 150 + kapak 25 + yayınlama 30 + kısa kesim 50) + dağıtım 40 + LinkedIn 30 + analiz 40 + yayın günleri 30 | 10 sa 50 dk |
| **İki hafta** | | 20 sa 50 dk + elle koşular (standart iki haftayla aynı) |

Parti düzeninin toplam süreyi kısaltıp kısaltmadığı bilinmiyor. **Varsayım:** kurulum tekrarı azaldığı için iki haftada tahmini 20–30 dk kazanılır; ilk parti denemesinde gerçek süreleri üretim tablosuna yaz, kazanç yoksa standart haftaya dön. Parti düzeninde stok kuralı iki video olarak okunur: B haftasının sonunda iki video hazırdır. İlk 4 videoyu standart haftayla yap, süreçler oturunca partiyi dene.

### 2.4 Bütçe aşılırsa neyi kes

Haftada 10 saatin üstüne çıkamıyorsan sırayla: (1) LinkedIn'e video yükleme (metin gönderisi kalır), (2) ikinci kısa video, (3) üçüncü kapak varyasyonu, (4) kurgudaki süsleme (geçiş, ses efekti), (5) elle görevi küçültmek (Bölüm 7.1, C yolu). **Kesilmeyecekler:** elle koşu, süreli koşu, "yapamadığı şey" bölümü, telefonda izleme, prompt dosyası, sayı tutarlılığı.

---

## 3. Araç seti

### 3.1 Önce iş, sonra araç

Her satır önce yapılacak işi tarif eder. Araç değişirse iş tanımı aynı kalır; yeni aracı "bu işi yapıyor mu" diye sınarsın. Örnek olarak yalnızca Bölüm 3.2'de durumu yazılı araçlar anılır; durumu doğrulanamayan kategorilerde araç adı verilmez.

| Aşama | İş tanımı (araçtan bağımsız) | Önerilen kategori → örnek | Alternatif kategori → örnek |
|-------|------------------------------|---------------------------|------------------------------|
| Araştırma | İzleyicinin arama dilini ve rakip boşluğunu görmek | Platformun açık yüzeyleri → YouTube arama önerileri (gizli sekme) + Google Trends ("YouTube araması" filtresi) | Studio içindeki fikir yüzeyi → hesabında görünüyorsa ve Türkçe sorgu sonuç veriyorsa kullan; adı ve kapsamı 2026'da değişti (Bölüm 3.2). Anahtar kelime eklentileri → kategori olarak var, bu belgede doğrulanmadı |
| Paketleme, senaryo | Varyasyon üretmek, taslak çıkarmak, eleştiri almak | Genel amaçlı sohbet asistanı → ChatGPT, Claude veya Gemini (hangisi Türkçede daha iyi, kanalın 3. videosunun konusu; sonucu burada da kullan) | Belge düzenleyiciye gömülü asistan |
| Senaryo deposu | Senaryoyu tablo yapısında yazmak, sürümlemek | Düz Markdown dosyaları (bu depodaki şablonlar) | Bulut belge |
| Ekran kaydı | Ekranı en az 1080p (tercihen 1440p), sabit kare hızında kaydetmek | Açık kaynak kayıt yazılımı → OBS Studio | Kayıt + yerleşik düzenleme ve imleç vurgusu olan ticari araçlar (kategori; ad verilmedi) |
| Kronometre | Süreyi kayıt karesinin içinde, kesim ve hızlandırmaya dayanıklı göstermek | Ekranda duran zamanlayıcı penceresi → `sablonlar/kronometre.html` | Kayıt yazılımının metin/zamanlayıcı kaynağı (varsa) |
| Ses kaydı ve temizlik | Konuşmayı kaydetmek; gürültü, seviye, sessizlik | Ses düzenleyici → Audacity | Yapay zekâ ses iyileştirici (kategori; Türkçe konuşmada sonucu kendi sesinle sına) |
| Yazıya dökme, altyazı | Konuşmayı zaman kodlu Türkçe metne çevirmek | Senaryo metnini YouTube Studio'da otomatik senkronize etmek (Türkçe için ilk videoda sına) | Açık kaynak konuşma tanıma modeli → Whisper; masaüstü arayüzü olarak Buzz, Resolve içinde AutoSubs eklentisi |
| Kurgu | Sesi omurga alıp görüntüyü dizmek, büyütmek, grafik eklemek | Geleneksel zaman çizelgeli kurgu → DaVinci Resolve | Metin üzerinden kurgu aracı (kategori; Türkçe döküm kalitesi doğrulanamadı) |
| Kapak | Sabit şablondan sayı ve görsel değiştirerek 16:9 görsel çıkarmak | Tarayıcı tabanlı tasarım → Canva | Açık kaynak görüntü düzenleyici → GIMP |
| Yayın ve analiz | Yüklemek, zamanlamak, ölçmek | YouTube Studio | (Aynı) + kendi kayıt tablon (`performans-kaydi.md`) |
| Kısa video kesimi | Yatay kaynaktan dikey, altyazılı, kendi başına anlaşılır parça çıkarmak | Ana kurgu aracında dikey zaman çizelgesi (aynı proje) | Otomatik klip çıkarıcı → Opus Clip (ekran kaydında doğru bölgeyi seçip seçmediğini sına) |
| Dağıtım ve zamanlama | Aynı dosyayı filigransız, platform başına ayrı açıklamayla yayınlamak | Her platformun kendi zamanlayıcısı | Sosyal medya planlayıcı (kategori) |
| Prompt dosyası yayını | Kopyalanabilir metni giriş istemeden açılan bir sayfada sunmak | Herkese açık, yalnızca görüntülenebilir belge | Düz metin deposu ya da basit bir web sayfası |
| Tıklama ölçümü | Prompt bağlantısına kaç kez tıklandığını video bazında saymak | Tıklama istatistiği veren bağlantı kısaltıcı (kategori) | Ziyaret sayan basit bir sayfa (kategori) |
| Bülten (KM-011'den itibaren) | E-posta toplamak ve göndermek | Çift onay ve tek tıkla çıkma destekleyen bülten ya da e-posta pazarlama aracı (kategori; seçim ölçütleri Bölüm 5.6) | — |
| Müzik | Telif sorunu çıkarmayacak fon müziği | YouTube Ses Kitaplığı (Studio içinde) | Lisanslı müzik aboneliği (kategori) |

Yapay zekâ seslendirme araçları bu tabloda yoktur; ilk 10 videoda kullanılmaz (Bölüm 4.3).

### 3.2 Doğrulama durumu (2026-11-16)

Fiyat bilerek yazılmadı. Araçların kendi yardım siteleri bu belge yazılırken doğrudan açılamadı; aşağıdaki "doğrulanan" sütunu **web aramasının sonuç özetlerine** dayanır. **Kayıt olmadan önce aracın kendi sayfasından kontrol et.**

| Araç / konu | Arama sonucunda görülen | Doğrulanamayan / çelişkili | Bu belgedeki karar |
|-------------|--------------------------|----------------------------|--------------------|
| **YouTube otomatik altyazısı ve senaryodan senkronizasyon** | Bir üniversitenin erişilebilirlik rehberindeki eski liste Türkçeyi otomatik altyazı dilleri arasında sayıyor. YouTube Yardım özeti: senkronizasyon için metin, konuşma tanımanın desteklediği bir dilde ve videoda konuşulanla aynı dilde olmalı; bir saatten uzun ya da sesi kötü videolarda önerilmiyor. | YouTube'un güncel dil listesi açılamadı; Türkçe doğruluk düzeyi bilinmiyor. | Önerilen yol, **gizli test videosunda sınanması koşuluyla** (Bölüm 0.1). |
| **Whisper / Buzz** | Buzz'ın (chidiwilliams/buzz) depo açıklaması: Whisper tabanlı, çevrimdışı çalışır, TXT/SRT/VTT dışa aktarır; Windows, macOS ve Linux sürümleri var. | Lisansı depodan kontrol et. Türkçe doğruluk ses kalitesine bağlı; kendi sesinle 1 dakikalık deneme yap. | Alternatif altyazı yolu. |
| **DaVinci Resolve** | Ücretsiz sürüm var; otomatik yazıya dökme ücretli (Studio) sürümde, ücretsiz sürümde elle altyazı ve .srt içe aktarma var (ikincil kaynaklar). | Yerleşik yazıya dökmenin dil listesinde Türkçe bulunamadı. | Kurgu için önerilen; Türkçe altyazı için yerleşik özelliğe güvenme. |
| **AutoSubs (Resolve eklentisi)** | Güncel Resolve sürümlerini, ücretsiz sürüm dahil, desteklediği bir sürüm geçmişi kaydında görülüyor. | Türkçe doğruluk düzeyi. | Alternatif; 1 dakikalık denemeyle sına. |
| **OBS Studio** | Açık kaynak ve ücretsiz olduğu uzun süredir sabit bilgidir. Yerleşik imleç vurgusu yok; forumda açık özellik isteği var, çözüm üçüncü taraf betik/eklenti. | — | Önerilen kayıt aracı; imleç için işletim sistemi ayarı. |
| **Canva** | İkincil rehberlere göre ücretsiz planda YouTube kapağı için 1280×720 hazır boyut var ve PNG indirilebiliyor; ücretli öğe kullanılırsa temiz indirme için ödeme gerekiyor. | Canva'nın kendi sayfası açılamadı. Ticari kullanım koşulu okunmadı. | Önerilen, **şablonda yalnızca ücretsiz öğe ve kendi ekran görüntün varsa**. |
| **Opus Clip** | Yardım sayfasının arama özetinde ve sürüm notlarında Türkçe, desteklenen video dilleri arasında sayılıyor; sağdan sola diller desteklenmiyor. | Ücretsiz planda filigran ve ticari kullanım koşulu doğrulanamadı. Ekran kaydında doğru bölgeyi çerçeveleyip çerçevelemediği bilinmiyor. | Yalnızca kısa video kesimi 2 × 25 dakikayı ölçümde aşarsa denenecek alternatif. |
| **Descript** | Kendi tanıtım sayfaları Türkçe sesi yazıya döktüğünü söylüyor. | Yardım merkezindeki dil listesi açılamadı; kendi geri bildirim forumunda Türkçe dökümün zayıf olduğunu söyleyen kullanıcı yazıları var: **çelişkili.** | Örnek listesinden çıkarıldı; kategori ("metin üzerinden kurgu") duruyor. |
| **CapCut** | Kendi yardım sayfasının özeti: ücretsiz dışa aktarım çoğunlukla filigransız; şablonun bitiş klibi, atıf isteyen stok öğe ya da varsayılan bitiş logosu varsa filigran çıkabiliyor. | İkincil kaynaklar ücretsiz planın ticari kullanımı (para kazanan kanal dahil) kısıtladığını ve kullanım koşullarının yüklenen içerik için geniş bir lisans tanıdığını yazıyor; koşulların güncel metni okunamadı. Türkçe altyazı doğruluğu çelişkili. | **Öneri listesinden çıkarıldı.** Kullanmayı düşünürsen önce kullanım koşullarını ve malzeme lisansını kendin oku. |
| **Studio "İlham" / "Araştırma" sekmesi** | Google Yardım özeti: İlham sekmesi Ağustos 2026'dan itibaren kademeli olarak kaldırılıyor, fikir üretimi için Studio'daki sohbet yardımcısına yönlendiriliyor. Ağustos 2026 tarihli bir sektör haberine göre farklı içerikli yeni bir "Araştırma" sekmesi az sayıda kullanıcıyla deneniyor. | Türkçe sorgu desteği ve Türkiye'de erişim. | İkincil; hesabında varsa dene, akışı ona bağlama. |
| **Shorts azami süresi** | Birden çok ikincil kaynak 3 dakika diyor; arama sonuçlarında YouTube Yardım'ın "üç dakikalık Shorts" başlıklı sayfası görünüyor. | Sayfanın tamamı okunamadı. | Kanalın hedefi 25–50 sn; sınır pratikte bağlayıcı değil. |
| **Audacity, GIMP, Whisper (model)** | Bugün ayrıca sorgulanmadı. | Açık kaynak ve ücretsiz oldukları uzun süredir sabit bilgidir. Whisper'ın desteklediği diller arasında Türkçe vardır. | Kullanılabilir. |

Bu tabloda olmayan araçlar (bağlantı kısaltıcılar, sosyal medya planlayıcılar, bülten platformları, müzik abonelikleri, yapay zekâ ses iyileştiriciler) doğrulanmadı; bu yüzden Bölüm 3.1'de yalnızca kategori olarak geçer.

Yeni bir araç için 15 dakikalık kabul testi: (1) Türkçe karakterleri (ğ, ş, ı, İ, â) doğru işliyor mu? (2) 1 dakikalık kendi ses kaydınla altyazı doğruluğu nasıl? (3) Ücretsiz katmanda dışa aktarımda filigran ya da bitiş logosu var mı? (4) Kullanım koşulu ticari kullanım (para kazanan kanal) ve yüklediğin içeriğin lisansı için ne diyor? (5) Dosyalarını standart biçimde (.mp4, .wav, .srt, .png) geri alabiliyor musun? Sonucu tarihle bu tabloya ekle.

### 3.3 İki set

**En ucuz başlangıç seti** — ilk 10 video için yeterli:

| İş | Araç |
|----|------|
| Araştırma | YouTube arama önerileri + Google Trends ("YouTube araması" filtresi) |
| Yazım | Bir sohbet asistanının ücretsiz kullanımı (sınırları kontrol et) + bu depodaki Markdown şablonları |
| Ekran kaydı | OBS Studio + `kronometre.html` |
| Ses | Bilgisayara bağlı herhangi bir düzgün mikrofon ya da kulaklık mikrofonu + Audacity + yankısız bir köşe |
| Kurgu | DaVinci Resolve (ücretsiz sürüm) |
| Altyazı | Senaryodan senkronizasyon (çalışıyorsa) ya da Buzz ile döküm + elle düzeltme |
| Kapak | Tarayıcı tabanlı bir tasarım aracının ücretsiz kullanımı ya da GIMP; şablon bir kez kurulur |
| Müzik | YouTube Ses Kitaplığı |
| Dağıtım | YouTube Studio ve LinkedIn'in kendi zamanlayıcıları |
| Prompt dosyası | Herkese açık, yalnızca görüntülenebilir belge + tıklama sayan kısa bağlantı |

Bu sette para harcanacak ilk kalem araç değil, **ses**tir: düzgün bir USB mikrofon ve odadaki yankıyı azaltacak basit önlemler.

**Rahat çalışma seti** — bir darboğaz ölçüldükten sonra, o darboğaz için:

| Ölçülen darboğaz | Eklenecek şey |
|------------------|---------------|
| Asistanın kullanım sınırına takılıyorsun | Bir sohbet asistanının ücretli planı (hangisi: 3. videonun sonucuna göre) |
| Kurgu 3 saati aşıyor ve zamanın çoğu ses kesmeye gidiyor | Metin üzerinden kurgu aracı (Türkçe dökümü kabul testinden geçerse) ya da Resolve'un ücretli sürümü |
| Kısa video kesimi video başına 25 dakikayı aşıyor | Otomatik klip çıkarıcı (çıkardığı anı yine kendin seç) |
| Shorts + LinkedIn dağıtımı 20 dakikanın altına indi ve TikTok/Reels eklenecek | Önce platformların kendi zamanlayıcıları; dört platform toplamı 30 dakikayı aşarsa sosyal medya planlayıcı |
| Ses temizliği her videoda sorun | Yapay zekâ ses iyileştirici ya da daha iyi mikrofon/oda |
| Müzik seçimi tekrar ediyor, telif uyarısı geliyor | Lisanslı müzik aboneliği |

Kural: bir aracı, üç video üst üste aynı aşamada ölçülmüş zaman kaybı görmeden satın alma. Araç denemek de üretim süresinden yer.

---
## 4. Yapay zekâ kullanım ilkeleri

### 4.1 Nerede kullanılmaz

Kanalın bütün değeri "bunu gerçekten yaptım, şu kadar sürdü, şurada takıldı" cümlesinin doğru olmasına dayanır. Bu yüzden:

| Yapay zekâya yazdırılmaz | Neden | Yerine |
|--------------------------|-------|--------|
| **Ölçüm ve test sonucu** ("12 dakika sürdü", "Claude daha iyi çıktı") | Asistan testi yapmadı; akla yatkın bir sonuç uydurur | `[ÇEKİMDE ÖLÇ]` yer tutucusu; çekimden sonra elle doldur |
| **Deneyim** ("bir hafta kullandım, üçüncü gün şunu fark ettim") | Yaşanmamış deneyim | Deney günlüğünü kendin tut, asistana yalnızca toparlat |
| **Görüş ve tavsiye** ("bence muhasebeciler bunu kullanmamalı") | Görüş senin sorumluluğunda | Gerekçeni kendin yaz |
| **Üçüncü kişi sözü** (İK uzmanının yorumu, izleyici alıntısı) | Uydurma alıntı | Kayıtlı gerçek söz; `izin-onay.md` ile izni alınmış |
| **İstatistik ve kaynak** ("çalışanların yüzde şu kadarı...") | Uydurma sayı ve var olmayan kaynak riski | Kaynağı kendin aç, oku, açıklamaya bağlantısını koy; bulamıyorsan cümleyi çıkar |
| **Sayım** (karakter sayısı, yorum sayısı, kelime sayısı) | Dil modelleri güvenilir saymaz; "say" talimatı sayımı doğru yapmaz | Studio'daki sayaç, tabloda `=UZUNLUK()`, elle sayım |
| **"Yapamadığı şey" bölümü** | Asistan kendi hatasını genel geçer maddelerle anlatır | Çekimde gerçekten yaşanan hata |
| **Kapaktaki ve videodaki arayüz görüntüsü** | Sahte ekran görüntüsü kanıt değildir | Gerçek çekimden kare |

Kullanılır: yapı, varyasyon, taslak, eleştiri, özet, biçim dönüştürme, örnek (kurgusal) veri, yazıya dökme, ses temizliği.

### 4.2 Doğruluk kontrolü

Senaryo kilitlenmeden ve video yayınlanmadan önce:

1. **İddia listesi:** Senaryodaki her olgusal cümleyi işaretle. Her biri için kaynak sütununa şunlardan birini yaz: `çekim` (ham kayıtta zaman kodu), `olcum.md`, `birincil kaynak` (bağlantı), `görüş` (videoda görüş olduğu belli). Hiçbiri yazılamıyorsa cümle çıkar.
2. **Sayı tutarlılığı** (tek tanım): `olcum.md` kaynaktır. Başlık, kapak, video içi (seslendirme, kronometre, karşılaştırma tablosu), açıklama, sabit yorum, kısa videolar ve LinkedIn gönderisindeki her süre ve adet onunla aynıdır; yuvarlama Aşama 7'deki kurala göredir. Kontrol bir kez, **yayın öncesi kapıda** yapılır; kısa video ve LinkedIn kapıları yalnızca kendi içindeki sayıyı `olcum.md` ile karşılaştırır.
3. **Araç davranışı:** Videoda "şu özellik var/yok", "ücretsiz/ücretli" diyorsan çekim günü arayüzde gördüğünü söyle ve tarihi ekranda göster ("Kasım 2026 itibarıyla"). Fiyat söyleme; değişir, video kalır.
4. **Tekrar denemesi:** Kopyalanabilir prompt'u yayından önce **yeni bir sohbette** bir kez daha çalıştır. İzleyicinin elinde çalışmayan prompt, kanalın en pahalı hatasıdır.
5. **Yayın sonrası düzeltme:** Hata fark edilirse sabit yoruma ve açıklamanın başına tarihli düzeltme notu yaz; yorumu silme.

### 4.3 Yapay zekâ seslendirme mi, kendi sesin mi?

| | Kendi sesin | Yapay zekâ seslendirme |
|---|-------------|------------------------|
| **Güven** | "Bunu ben yaptım" cümlesi bir insandan gelir; kanalın iddiasıyla uyumlu | "Gerçek test" iddiasıyla sentetik ses arasında izleyicide soru işareti oluşabilir **[Gözlem]** |
| **Tanınırlık** | Yüz göstermeyen kanalda marka sestir | Aynı hazır sesi başka kanallar da kullanabilir |
| **Türkçe** | Doğal vurgu; "prompt", "ChatGPT", "Excel" gibi karışık dilli cümlelerde sorun yok | Türkçe–İngilizce karışık cümlelerde ve eklerde telaffuzu çekimden önce kendi senaryonla test etmen gerekir; sonuç araçtan araca değişir |
| **Hız** | Kayıt + dinleme + temizlik tahmini 55 dk | Üretim hızlı; ama telaffuz düzeltme ve yeniden üretme turları öngörülemez |
| **Düzeltme** | Tek cümle için yeniden kayıt; oda ve ton tutturmak gerekir | Tek cümle yeniden üretilir |
| **Politika** | Beyan sorusu doğmaz | YouTube'da beyan sorusu, Instagram ve TikTok'ta etiket sorusu doğar (Bölüm 4.4) |
| **Maliyet** | Mikrofon (bir kez) | Sürekli abonelik (fiyat ve koşulları kontrol et) |

**Karar: kendi sesin.** Gerekçe sırayla: (1) kanalın vaadi kişisel tanıklığa dayanıyor; (2) yüz yokken izleyicinin bağ kurduğu tek şey ses; (3) kazanılacak süre küçük (tahmini haftada 20–30 dk) ve özgün olmayan içerik algısı riskini artırıyor; (4) hedef kitle LinkedIn'de de var, orada "bir insan anlatıyor" sinyali daha da önemli.

Yapay zekânın seste yeri: temizlik, seviye, sessizlik kesme, yazıya dökme. Sesini beğenmiyorsan çözüm sentetik ses değil; daha yavaş konuşmak, daha kısa cümle yazmak ve hook'u üç kez kaydetmek.

**Ses klonu ve sentetik ses ilk 10 videoda kullanılmaz;** kendi sesinin klonuyla tek cümle düzeltmek de buna dahildir. Yayın sonrası fark edilen hata sesle değil yazıyla düzeltilir: sabit yoruma ve açıklamanın başına tarihli not (Bölüm 4.2, madde 5). 10. videodan sonra bu karar yeniden açılacaksa önce Bölüm 4.4 A'daki kanal kuralı uygulanır.

### 4.4 Politikalar: beyan, etiket, özgün olmayan içerik, İş Ortağı Programı

> **Doğrulama notu:** support.google.com bu belge yazılırken açılamadı. Aşağıdaki [Resmî] maddeler ilgili yardım sayfasının arama sonucunda görünen özetine ve ikincil haber kaynaklarına dayanır. Bölüm 0.2'deki okumayı yapınca bu bölümü düzelt.

**A. YouTube: değiştirilmiş veya sentetik içerik beyanı**

- **[Resmî — arama sonucu üzerinden]** Yükleme akışında, içeriğin gerçek sanılabilecek biçimde anlamlı ölçüde değiştirilip değiştirilmediğini ya da sentetik üretilip üretilmediğini soran bir beyan adımı vardır. Kapsam: gerçek bir kişiye söylemediği/yapmadığı bir şeyi yaptırmak, gerçek bir olayın ya da yerin görüntüsünü değiştirmek, gerçekte olmamış gerçekçi bir sahne üretmek. Yapay zekânın üretime yardımcı kullanımı (fikir, senaryo taslağı, otomatik altyazı), açıkça gerçek dışı içerik ve küçük düzeltmeler kapsam dışıdır.
- **[Resmî — arama sonucu üzerinden; ikincil kaynaklar çelişiyor]** Yardım sayfasının özetine göre **başkasının** sesini klonlayarak seslendirme ya da dublaj yapmak beyan gerektirir; **kendi** sesini klonlamak beyan gerektirmeyen örnekler arasında sayılır. En az bir ikincil kaynak kendi ses klonunu da beyan gerektirenler arasında gösteriyor.
- **Standart video** (gerçek ekran kaydı + kendi sesin + yapay zekâyla taslağı çıkarılmış senaryo): beyan sorusuna **"Hayır".**

**Kanal kuralı (politikadan sıkı, yardım sayfası okunana kadar değişmez):**

| Durum | Studio'daki beyan | Açıklamaya yazılır mı |
|-------|-------------------|------------------------|
| Videoda sentetik ya da klonlanmış ses var (kendi sesinin klonu dahil) | **Evet** | Evet: "Bu videonun [şu bölümünde] sentetik ses kullanıldı." |
| Gerçek bir kişinin (konuk, hakem) sesi ya da görüntüsü değiştirildi | **Evet**; ayrıca kişinin yazılı izni | Evet |
| Gerçekçi üretilmiş görüntü ya da video kullanıldı | **Evet** | Evet |
| Ekranda yapay zekânın ürettiği metin, tablo, sunum var (videonun konusu) | Hayır | Araç adı ve çekim tarihi zaten "Nasıl ölçtüm" bloğunda |
| Otomatik altyazı, ses temizliği, senaryo taslağı | Hayır | Hayır |

Politikadan bağımsız kanal kuralları: ekranda yapay zekâ çıktısı gösteriyorsan hangi araçtan ve hangi tarihte alındığını yaz. Hızlandırılmış bölüm "hızlandırıldı" etiketi taşır. Kronometre gerçek süreyi gösterir. Bunlar YouTube'un istediği için değil, kanalın iddiası için.

**B. YouTube: özgün olmayan içerik ve yeniden kullanılan içerik**

- **[Resmî — ikincil kaynaklarla doğrulandı]** YouTube, 15 Temmuz 2025'te para kazanma politikalarındaki "tekrarlayan içerik" (repetitious content) başlığını "özgün olmayan içerik" (inauthentic content) olarak yeniden adlandırdı ve bunun yeni bir kural değil, mevcut kuralın netleştirilmesi olduğunu açıkladı. Tanım: toplu üretilmiş ya da tekrarlayan, izleyicinin çoğu zaman spam olarak algıladığı içerik. Kural, içeriğin yapay zekâyla mı geleneksel yöntemle mi üretildiğine bakmaz; yapay zekâ kullanmak tek başına ihlal değildir. Haber kaynaklarına göre değerlendirme tek video değil **kanal düzeyinde** yapılır.
- **Bu kanal için riskli desenler:**
  - İmza formatın (kronometre → karşılaştırma → yapamadığı şey → prompt) her videoda aynı olması sorun değildir; sorun, videoların **içeriğinin** birbirinin kopyası olmasıdır. Her videoda farklı görev, farklı veri, gerçek ve farklı bir sonuç olmalı.
  - M (meslek) serisinde aynı senaryoyu meslek adını değiştirerek tekrar etme. "Muhasebeciler için" ile "İK için" videolarının görevleri, verileri ve hataları farklı olmalı.
  - Sentetik ses + hazır görsel + asgari insan katkısı birleşimi. Bölüm 4.3'teki kararın bir gerekçesi de budur.
  - Aynı kısa videonun küçük farklarla defalarca yüklenmesi.
- **Kısa videolar:** Kendi uzun videondan kesilen kısa videolar kendi özgün içeriğindir. Yine de her kısa video kendi başına anlaşılır olsun, yeni bir açılış cümlesi ve çerçeve taşısın **[Gözlem]**.
- **Yeniden kullanılan içerik:** Başkasının videosundan, ekran kaydından ya da müziğinden parça kullanacaksan anlamlı yorum/dönüştürme ve telif açısından ayrı değerlendir. Bu kanalın formatı buna ihtiyaç duymaz; duyarsa güncel politikayı oku.

**C. Diğer platformlar: yükleme ekranında yapılacak iş**

Standart kısa video (gerçek ekran kaydı + kendi sesin) için üç platformda da yapay zekâ etiketi **gerekmez;** ekranda yapay zekâ çıktısının görünmesi videoyu "yapay zekâyla üretilmiş" yapmaz. Sentetik ses ya da gerçekçi üretilmiş görüntü kullanırsan:

| Platform | Yükleme ekranında ne yapılır | Dayanak ve doğrulama durumu |
|----------|------------------------------|-----------------------------|
| **Instagram Reels** | Yapay zekâ etiketini aç (arayüzde "AI info" / "Made with AI" adlarıyla geçiyor) | **Arama sonucu üzerinden:** Meta ve Instagram yardım sayfalarının özetine göre dijital olarak üretilmiş ya da değiştirilmiş **gerçekçi video ve gerçekçi duyulan ses** için etiket zorunlu; etiketlememe yaptırıma yol açabilir; içerik otomatik de etiketlenebilir. Sentetik seslendirme bu tanıma girer. Yayından önce Instagram Yardım'da "yapay zekâ ile üretilen içeriği etiketleme" sayfasını oku. |
| **TikTok** | Gönderi ekranındaki "yapay zekâ ile üretilmiş içerik" anahtarını aç | **İkincil kaynaklar:** gerçekçi görüntü, ses ya da video içeren yapay zekâ üretimi içerik için etiket isteniyor; kaynak bilgisi taşıyan dosyalar otomatik etiketlenebiliyor. TikTok'un kendi sayfası okunmadı; yayından önce Topluluk Kuralları'ndaki ilgili başlığa bak. |
| **LinkedIn** | Yükleme ekranında bir etiket seçeneği çıkıyorsa aç; çıkmıyorsa gönderi metnine yaz ("Seslendirme sentetiktir.") | **Doğrulanamadı:** üretici tarafından uygulanan bir etiketin varlığı arama sonuçlarında bulunamadı. |

Bölüm 4.3'teki karar gereği bu tablo ilk 10 videoda devreye girmez; durum değişirse başvurulacak yer burasıdır.

**D. YouTube İş Ortağı Programı: duyurulmuş değişiklik**

**[Gözlem — ikincil haber kaynakları, resmî duyuru okunmadı]** Ağustos 2026 tarihli haberlere göre YouTube, 1 Şubat 2027'de yürürlüğe girecek İş Ortağı Programı değişiklikleri duyurdu. Haberlerde geçenler: yeni başvurular için izlenme süresi ve Shorts görüntüleme eşiklerinin yükseltilmesi (birden çok kaynakta "yaklaşık iki katı": 365 günde 8.000 saat ya da 90 günde 20 milyon Shorts görüntülemesi; 1.000 abone koşulu sürüyor), Shorts reklam geliri paylaşımı için ayrı bir süreklilik eşiği ve güncellenen koşulların 31 Ocak 2027'ye kadar Studio'dan kabul edilmesi. Mevcut üyelerin etkilenip etkilenmediği konusunda kaynaklar çelişiyor.

Bu kanal için sonucu: para kazanma başvurusu Şubat 2027'den sonra yapılacağı için **yeni eşikler geçerli olacaktır.** Bir gelir ya da başvuru tarihi hedefi koymadan önce sayıları resmî sayfadan doğrula (Bölüm 0.2); doğrulanmamış eşiği plana yazma.

### 4.5 Gizlilik ve veri

- Çekimde ve prompt'larda gerçek müşteri, çalışan, şirket verisi kullanma. Kurgusal veri setini bir kez iyi kur, birden çok videoda kullan (aynı kurgusal şirket, kanalın küçük bir sürekliliği olur).
- İzleyiciye de aynı uyarıyı videoda yap: şirket verisini bir yapay zekâ aracına yapıştırmadan önce şirketin kuralına bakmalı. Bu, hedef kitlenin gerçek sorusudur.
- Çekim profilinde kişisel hesap adı, e-posta, sohbet geçmişi görünmesin.
- **Üçüncü kişiler:** Videoda başka birinin sözü, sesi, görüntüsü, ekranı ya da ölçümü kullanılacaksa `izin-onay.md` çekimden önce imzalanır (ya da e-postayla yazılı onay alınır). Konuğun gerçek müşteri verisi, işyeri ekranı ya da meslek sırrı kayda girmez; konuk da kurgusal veriyle çalışır. Konuğun adının ve unvanının nasıl geçeceği formda yazılıdır; form `08_yayin/` klasöründe saklanır.

---

## 5. Yeniden kullanım

### 5.1 Bir uzun videodan çıkanlar

| Çıktı | Kaynak | Ne zaman | Tahmini süre |
|-------|--------|----------|--------------|
| **Prompt dosyası** | Çekimde kullanılan, yeniden denenmiş prompt'lar | Yayından önce (videonun parçası) | 10 dk (Aşama 8'in içinde) |
| **Kısa video 1: "Sonuç"** | Önce/sonra karşılaştırma anı + ölçülen süre | Kurgunun ertesi günü | 25 dk |
| **Kısa video 2: "Yapamadığı şey"** | Aracın hata yaptığı an | Kurgunun ertesi günü | 25 dk |
| **Kısa video 3: "Tek prompt"** (isteğe bağlı) | Kopyalanabilir prompt ve çıktısı | Bütçe tutuyorsa | 25 dk |
| **Dağıtım** | Kısa videoların platformlara yüklenmesi ve zamanlanması | Yayın hazırlığı günü | 20 dk |
| **LinkedIn metin gönderisi** | Videonun tek çıkarımı + ölçüm | Yayından 2 gün sonra | 15 dk |
| **Bülten sayısı** (KM-011'den itibaren) | Prompt + "yapamadığı şey" + video bağlantısı | Yayından sonraki cumartesi | 20 dk |
| **Belge/karusel** (isteğe bağlı) | Adım adım ekran görüntüleri | Video iyi gittiyse | 30 dk |

### 5.2 Kısa video akışı

Süreler Aşama 10a'dadır; burada her adımın kuralı var.

| # | Adım | Kural | Kim |
|---|------|-------|-----|
| 1 | Aday anları bul | Zaman kodlu transkripti Prompt P8'e ver; 6 aday iste. Senaryodaki "kısa video işaretleri" tablosuyla karşılaştır. | Yapay zekâ önerir |
| 2 | Seç | Adayları **kendin izle**. Ölçüt: ses kapalıyken ve uzun videoyu görmemiş biri için 3 saniyede ne olduğu anlaşılıyor mu? P8 görüntüyü görmez; bu kararı veremez. | İnsan |
| 3 | Dikey zaman çizelgesi | Ana kurgu projesinde 9:16 (1080×1920) zaman çizelgesi; seçilen anı kopyala. | İnsan |
| 4 | Yeniden çerçevele | Yatay ekran kaydı dikeyde okunmaz. İlgili bölgeyi (sohbet kutusu, tablo köşesi, formül çubuğu) büyüt; üstte sabit başlık bandı, ortada ekran, altta altyazı. Kayıt 1080p ise büyütme sınırı burada da geçerlidir: yazı bulanıyorsa o anı dar pencere ve %200 tarayıcı yakınlaştırmasıyla **yeniden çek**. Gömülü kronometre çerçeve dışında kalırsa süreyi başlık bandına yazıyla koy (`olcum.md` değeri). | İnsan |
| 5 | Yeni açılış cümlesi | Uzun videodaki cümle bağlama yaslanır. İlk cümleyi yeniden kaydet: görev + süre. Örnek: "Bu 400 satırlık tabloyu elle temizlemek [ELLE SÜRE] sürdü. Şimdi aynı işe bak." | Yapay zekâ önerir (P8), insan kaydeder |
| 6 | Gömülü altyazı | Dikey videoda zorunlu say. Sarı vurgu yalnızca sayıda ve anahtar kelimede. Taslağı araç üretir; yazımı sen düzeltirsin. | Yapay zekâ taslak, insan düzeltme |
| 7 | Kapanış | Son 2 saniye: sözlü yönlendirme ("Tam hâli ve prompt, kanaldaki uzun videoda."). Bitiş kartı, logo animasyonu yok. | İnsan |
| 8 | Dışa aktar | **Filigransız ana dosya;** her platforma bu dosyadan yüklenir. | İnsan |
| 9 | Bağla | Shorts'ta "ilgili video"yu uzun videoya ayarla. **[Arama sonucu üzerinden]** Özellik Studio'da (masaüstü) videonun ayrıntılar sekmesinden ayarlanıyor ve aynı kanaldaki bir videoya bağlanabiliyor; yeni kanalda açık olup olmadığını gizli test videosunda kontrol et (Bölüm 0.1). | İnsan |

Uzun video henüz yayında değilken (uzun videodan önce giden kısa video) "ilgili video" ayarlanamaz; uzun video yayına girince geri dönüp ayarla. Bu, yayın günü 15 dakikasının içindedir.

### 5.3 Platform başına farklar

Azami süreler sık değişir ve bu belge yazılırken hiçbir platformun kendi sayfası açılamadı; aşağıdaki sınırlar ikincil kaynaklardan derlenmiştir ve kaynaklar yer yer çelişir. Kanalın kısa videoları 25–50 saniye olduğu için **sınırların hiçbiri pratikte bağlayıcı değildir;** yalnızca 60 saniyeyi aşan bir kesim yapacaksan yükleme ekranındaki güncel sınıra bak.

| | YouTube Shorts | LinkedIn | Instagram Reels | TikTok |
|---|----------------|----------|-----------------|--------|
| **Ne zaman açılır** | 1. videodan itibaren | 1. videodan itibaren | Shorts + LinkedIn dağıtımı 20 dakikanın altına inince | Reels ile birlikte |
| **Oran** | 9:16 (1080×1920) | Dikey video akışta destekleniyor; kare (1:1) ya da 4:5 masaüstünde daha iyi oturabilir **[Gözlem]**. İlk ay yalnızca 9:16 ana dosyayı yükle; ayrı kare sürüm ek kurgu işidir, ancak ölçümle gerek görülürse | 9:16; profil ızgarasındaki kırpma için kapak karesini kontrol et | 9:16 |
| **Azami süre (ikincil kaynaklar)** | 3 dakika | Kaynaklar LinkedIn Yardım'a atıfla 15 dakika diyor; bazıları mobil yüklemede 10 dakika | Çelişkili: 3, 15 ve 20 dakika diyen kaynaklar var | Çelişkili: uygulama içi çekimde 10 dakika; dosya yüklemede 30–60 dakika diyen kaynaklar var |
| **Bu kanal için hedef süre (tahmini)** | 25–50 sn | 30–75 sn; biraz daha uzun bağlama tahammül var **[Gözlem]** | 25–45 sn | 25–50 sn |
| **İlk saniye** | Görev + sayı ekranda yazılı; ses başlamadan anlaşılsın | İlk satır metindir: gönderi metninin ilk iki satırı "devamını gör"den önce görünür; sorunu orada söyle | Aynı; kapak karesi ızgarada da görünür, sayı kapakta olsun | Aynı; ilk karede hareket (imleç, yazı yazılması) |
| **Altyazı** | Gömülü; alt kısımdaki arayüz öğelerinin altında kalmasın | Gömülü şart: akışta videolar çoğunlukla sessiz başlar **[Gözlem]** | Gömülü; sağ ve alt kenarlarda güvenli alan | Gömülü; sağ ve alt kenarlarda güvenli alan |
| **Üslup** | Kanal tonu; uzun videoya köprü | Yine "sen"; örnekler iş bağlamında; kişisel gözlem + ölçüm + tek çıkarım | Görsel düzen daha önemli; kapak karesi özenli | Daha konuşur gibi; aynı dürüstlük |
| **Açıklama metni** | Kısa; görev ve sonuç. Uzun videonun adı | 5–10 satırlık bağımsız metin; video izlenmese de değer taşısın | 1–2 cümle + birkaç etiket | 1–2 cümle + 3–5 ilgili etiket |
| **Bağlantı** | "İlgili video" özelliği `[hesabında açık mı kontrol et]` | Gönderi içindeki dış bağlantının erişimi düşürdüğü yaygın bir gözlemdir **[Gözlem]**; bağlantıyı ilk yoruma koymayı dene ve karşılaştır | Profil bağlantısı `[hesabında açık mı kontrol et]` | Profil bağlantısı `[hesabında açık mı kontrol et]`; ikincil kaynaklar kişisel hesaplarda takipçi eşiği olup olmadığı konusunda çelişiyor |
| **Yönlendirme cümlesi** (bağlantıya bağımlı değil) | "Tam hâli kanaldaki uzun videoda." | Bağlantıyı ilk yoruma kendin koy; "isteyen yoruma yazsın" türü yapay etkileşim isteme | "Tam hâli YouTube'da: Kısa Mesai diye ara." | "Tam hâli YouTube'da: Kısa Mesai diye ara." |
| **Yapay zekâ etiketi** | Bölüm 4.4 A | Bölüm 4.4 C | Bölüm 4.4 C | Bölüm 4.4 C |

**Filigran sorunu:** Bir platformun uygulamasından indirilen videoda o platformun filigranı olur. Instagram'ın geçmişte, başka uygulamaların filigranını taşıyan Reels'lerin daha az önerileceğini açıkladığı bilinir; diğer platformlar için resmî bir açıklama doğrulanamadı, yaygın gözlem aynı yöndedir **[Gözlem]**. Pratik kural tartışmasızdır: **her zaman kurgu aracından çıkan filigransız ana dosyayı yükle;** hiçbir platformdan indirip diğerine yükleme. Kurgu aracının ücretsiz katmanı dışa aktarımda kendi filigranını ya da bitiş logosunu ekliyorsa ya kapat ya aracı değiştir.

**Platform sırası ve açılma koşulu:** Önce Shorts (uzun videoyla aynı kanalı besler) ve LinkedIn (hedef kitle orada ve iş bağlamında). Dört hafta boyunca dağıtım süresini üretim tablosuna yaz. Ortalama 20 dakikanın altındaysa Reels ve TikTok'u aynı ana dosyayla ekle; değilse ekleme. Bütçe sıkışırsa önce TikTok ve Reels, sonra LinkedIn videosu bırakılır; LinkedIn metin gönderisi kalır.

### 5.4 LinkedIn gönderisi akışı

Video kırpması olmadan da çalışan metin gönderisi (15 dk). Adımlar:

1. `olcum.md` değerlerini ve çekimde yaşanan hatanın tek cümlelik özetini Prompt P11'e ver; iki taslak al (3 dk).
2. Taslaklardan birini seç, **kendi cümlelerinle yeniden yaz**; "Benim gözlemim" satırı asistandan gelmez (8 dk).
3. LinkedIn kapısını işaretle, zamanla (yayından 2 gün sonra, cumartesi), bağlantıyı ilk yoruma koy (4 dk).

```
[1. satır: izleyicinin sorunu, kendi cümlesiyle]
[2. satır: ne yaptım — görev + elle süre]

[3–5. satır: yapay zekâyla nasıl gitti — ölçülen süre, kaç düzeltme turu]

Yapamadığı şey: [tek cümle, somut]

Kullandığım prompt'un iskeleti:
[3–4 satır, kopyalanabilir]

[Kapanış: iş arkadaşına sorulacak türden gerçek bir soru]
```

Kurallar: ölçüm `olcum.md` ile aynı; "oyunun kuralları değişti" türünden abartı yok; kendi hesabından, birinci tekil kişiyle. Gönderiye kısa videonun dikey ana dosyası eklenebilir.

### 5.5 Prompt dosyası akışı

Prompt dosyası her videonun parçasıdır, yeniden kullanım değil. Üç yerde durur ve üçü de aynı metni taşır:

1. **Açıklamada tam metin.** Bağlantı tıklanmasa da izleyici prompt'a ulaşır (01 belgesi 8.4; Bölüm 0.3).
2. **Video sayfası:** `prompt-dosyasi.md` şablonuyla hazırlanan, giriş istemeden açılan sayfa.
3. **Dizin sayfası:** Bütün videoların prompt'larına tek bağlantıdan erişim; izleyici bir bağlantıyı kaydeder.

Adımlar (10 dk, Aşama 8'in ilk adımı):

| # | Adım | Süre | Kim |
|---|------|------|-----|
| 1 | `arac-ciktilari.md` ve senaryodan videoda kullanılan prompt'ları **harfi harfine** al. Kurgusal şirkete özgü yerleri köşeli parantezli alanlara çevir ("[SÜTUN ADLARI]"). | 2 dk | İnsan |
| 2 | Alanları kendi verinle doldurup **yeni bir sohbette** çalıştır. Çıktı videodakiyle aynı türden mi? Değilse prompt'u düzelt ve farkı sayfaya not düş. | 3 dk | İnsan |
| 3 | `prompt-dosyasi.md` şablonunu doldur: görev, prompt, doldurulacak alanlar, "şunu değiştirirsen şu olur", bilinen sınır (videodaki "yapamadığı şey"), çekim tarihi ve araç. | 3 dk | İnsan; "doldurulacak alanlar" tablosunun taslağını asistan çıkarabilir |
| 4 | Sayfayı yayınla, dizine en üste ekle, bu video için **ayrı bir kısa bağlantı** oluştur (`KM-004` gibi tanınır bir adla). Gizli sekmede aç: giriş istemeden açılıyor mu, kopyalama çalışıyor mu? | 2 dk | İnsan |

**Tıklama ölçümü.** YouTube Studio açıklamadaki bağlantıya kaç kez tıklandığını vermez; herkese açık bir belge de anonim ziyaretçi saymaz. Bu yüzden her videonun açıklamasına ve sabit yorumuna tıklama istatistiği veren bir kısa bağlantı konur; "prompt tıklaması" sütunu o panelden okunur. Dikkat edilecekler: (a) kısa bağlantının açıklamada tıklanabilir kaldığını gizli test videosunda dene; (b) panelin saydığı şey tıklamadır, tekil kişi değildir; botlar da sayılabilir, sayıyı yalnızca kendi videoların arasında kıyas için kullan; (c) kısa bağlantı kurulana kadar sütuna `[ölçüm yok]` yazılır. Ölçüm yöntemi `performans-kaydi.md` Bölüm 0'a bir kez yazılır.

Prompt'un tam metni açıklamada durduğu için bağlantı tıklaması prompt'u kullananların **alt sınırıdır;** çoğu izleyici açıklamadan kopyalar ve hiçbir yerde sayılmaz.

### 5.6 E-posta bülteni akışı

**Ne zaman başlar:** KM-011'den itibaren (`02-buyume-stratejisi.md` B7). İlk 10 videoda bülten yoktur; prompt dosyası e-posta istemeden açıktır. Başlatma eşiği ölçülebilir iki işarete bağlıdır: (a) son 5 videonun en az 3'ünde prompt kısa bağlantısı tıklanmış (sayı kaç olursa olsun sıfır değil), (b) yorumlarda "hepsini bir yerde toplasan" türü istek en az iki ayrı kişiden gelmiş (yorumları kendin say). İkisi de yoksa KM-015'te yeniden bak.

**Kurulum (bir kez, tahmini 2–3 saat; haftalık bütçenin dışında):**

| # | İş | Not |
|---|----|-----|
| 1 | Araç seç | Ölçütler: çift onay (kayıt olan kişi e-postasındaki bağlantıya tıklayarak onaylar), her e-postada tek tıkla çıkma, listeyi dışa aktarabilme, Türkçe karakterlerin konu satırında doğru görünmesi, gönderen adresi olarak kendi alan adını kullanabilme. Araç adı bu belgede verilmedi; hiçbirinin Türkçe arayüzü ve Türkiye'den kullanımı doğrulanmadı. Bölüm 3.2'deki kabul testini uygula. |
| 2 | Hukuki hazırlık | E-posta adresi kişisel veridir: KVKK kapsamında aydınlatma metni ve açık rıza gerekir. Gönderilerin ticari elektronik ileti sayılması hâlinde ayrıca onay alma, onayı kayıt altında tutma ve İleti Yönetim Sistemi (İYS) yükümlülükleri doğabilir. Kendi durumun (şahıs/şirket, gönderinin niteliği) için **formu yayınlamadan önce güncel mevzuata bak ya da bir uzmana danış;** bu belge hukuki görüş değildir. |
| 3 | Kayıt formu | Tek alan (e-posta). Formun üstünde ne geleceği yazılı: "Haftada bir e-posta: o haftanın prompt'u ve takıldığı yer." Aydınlatma metni bağlantısı ve rıza kutusu formda. |
| 4 | Karşılama e-postası | Otomatik; dizin sayfasının bağlantısını verir. Videodaki prompt'lar e-posta duvarının arkasına **konmaz;** kayıt olana verilen şey "hepsi bir arada + yenileri e-postayla"dır. |
| 5 | Bağlantıları güncelle | Açıklama alt bloğu, sabit yorum şablonu ve kanal sayfası bağlantısı kayıt sayfasına döner; eski videolardaki açık dizin bağlantısı çalışmaya devam eder. |

**Haftalık sayı (20 dk, cumartesi; 48 saat kontrolüyle aynı oturum):**

| # | Adım | Süre | Kim |
|---|------|------|-----|
| 1 | `olcum.md`, prompt sayfası ve "yapamadığı şey" özetini Prompt P13'e ver; taslak al | 3 dk | Yapay zekâ |
| 2 | Taslağı kendi cümlelerinle yeniden yaz; "videoda yer almayan not" satırını kendin ekle (çekimde olup videoya girmeyen bir gözlem; yoksa satırı sil) | 10 dk | İnsan |
| 3 | Konu satırını yaz: görev + ölçülen süre, başlığın kopyası değil. Kendine test e-postası gönder; telefonda aç, bağlantıları dene | 5 dk | İnsan |
| 4 | Gönder ya da zamanla; gönderim sayısını ve bir hafta sonra açılma/tıklama sayılarını performans kaydına yaz | 2 dk | İnsan |

Şablon (beş blok; düz metin, görsel yok):

```
Konu: [Görev], elle [ELLE SÜRE], yapay zekâyla [YZ SÜRE]

Bu hafta: [görev, tek cümle]. Elle [ELLE SÜRE] sürdü; yapay zekâyla [YZ SÜRE], [TUR SAYISI] düzeltme turuyla.

Prompt:
[kopyalanabilir tam metin]

Takıldığı yer: [yapamadığı şey, tek cümle] 

[İsteğe bağlı — videoda yer almayan not: tek paragraf]

Video: [bağlantı]

Bu e-postayı yanıtla: senin işinde en çok vakit alan iş hangisi?

[Listeden çıkma bağlantısı — araç ekler; göründüğünü kontrol et]
```

Kurallar: sayılar `olcum.md` ile aynı; haftada birden fazla e-posta yok; satış ortaklığı bağlantısı varsa açıkça yazılır; yanıt gelen e-postalar fikir havuzuna izleyici cümlesi olarak girer (kişinin adı olmadan).

---

## 6. Dosya düzeni, varlık kütüphanesi, kurgu ön ayarları

### 6.1 Klasör yapısı

```
KisaMesai/
├── 00_VARLIKLAR/
│   ├── grafik/          kronometre.html, kronometre çerçevesi, alt bant, kartlar, ok
│   ├── kapak/           kapak-sablon dosyası, yazı tipi, renk notu
│   ├── muzik/           3–4 parça + lisans-notu.md
│   ├── ses-efekti/      tık, geçiş (en fazla 3–4 ses)
│   ├── ornek-veri/      kurgusal şirketin tabloları, e-postaları, cevap anahtarları
│   └── proje-sablonu/   uzun-video şablonu, dikey şablon
├── 01_FIKIRLER/
│   └── fikir-havuzu.md
├── 02_VIDEOLAR/
│   └── KM-002_excel-3sa-10dk/
│       ├── 01_brief/        video-brief.md
│       ├── 02_senaryo/      senaryo_v1.md, senaryo_KILIT.md
│       ├── 03_ham/          ekran kayıtları, olcum.md, arac-ciktilari.md, cevap-anahtari.md
│       ├── 04_ses/          ham ve temiz ses
│       ├── 05_proje/        kurgu proje dosyası
│       ├── 06_cikti/        son video, .srt, kapaklar
│       ├── 07_kisa/         dikey ana dosyalar, açıklamalar
│       └── 08_yayin/        yayin-metaverisi.md, prompt-dosyasi.md, linkedin.md, izin-onay (varsa)
├── 03_KAYITLAR/
│   ├── performans-kaydi.md
│   └── prompt-dizini.md
└── 99_ARSIV/
```

### 6.2 Adlandırma

Kalıp: `KM-[no]_[bölüm]_[tür]_[sürüm].[uzantı]`

| Tür | Örnek |
|-----|-------|
| Video klasörü | `KM-002_excel-3sa-10dk` |
| Süreli koşu kaydı | `KM-002_b3-kronometre-kosusu_ham.mp4` |
| Elle koşu kaydı | `KM-002_elle-kosu_ham.mp4` |
| Süre dışı ek kayıt | `KM-002_ek_yapamadigi-sey_ham.mp4` |
| Ses | `KM-002_b1-hook_ses_t3.wav` (t3 = üçüncü deneme) |
| Son video | `KM-002_SON_2026-12-10.mp4` |
| Kapak | `KM-002_kapak_A.png`, `_B.png` |
| Kısa video | `KM-002_K1_sonuc_dikey.mp4`, `KM-002_K2_yapamadigi_dikey.mp4` |
| Altyazı | `KM-002_SON_tr.srt` |
| Prompt kısa bağlantısı | sonu `KM-002` ile biten bağlantı |

Kurallar: Türkçe karakter ve boşluk yok (araçlar arası taşımada sorun çıkarır); tarih `YYYY-AA-GG`; "son", "son2", "sonson" yok — yalnızca bir `SON` dosyası, öncekiler arşive. Video numarası **yayın sırasıdır**, fikir havuzundaki numara değil; fikir numarasını brief'e yaz.

Yedek: `03_ham` ve `06_cikti` yayından sonra harici diske/buluta. `05_proje` 90 gün sonra silinebilir; ham kayıt, `olcum.md` ve izin formları silinmez (kanıt).

### 6.3 Varlık kütüphanesi

Intro yok. Video doğrudan görevle açılır. Sabit olanlar:

| Varlık | Tarif | Kural |
|--------|-------|-------|
| **Kronometre** | **Çekimde kayda gömülür** (`kronometre.html`: lacivert zemin, sarı rakamlar, sağ üst köşe). Kurguda eklenen yalnızca çerçeve, "ELLE" / "YAPAY ZEKÂ" etiketi ve "×N" notudur. | Rakam kurguda yazılmaz ve düzeltilmez. Görüntü hızlandırılınca ya da bekleme kesilince rakamlar kendiliğinden hızlanır ya da atlar. Süre dışı kayıtlarda kronometre durmuş görünür; kurguda "Ayrı sohbet · süre dışı" etiketi eklenir (01 belgesi 6.1). Bitişteki tam ekran büyük sayı kurgu grafiğidir ve `olcum.md` değerini taşır. |
| **Alt bant** | Sol altta bölüm adı ("3 / Yapay zekâyla koşu"); 3 sn görünür, kaybolur. | Her bölüm başında. Tutma aracı: izleyici nerede olduğunu bilir. |
| **Karşılaştırma tablosu** | İki sütun: Elle / Yapay zekâyla. Satırlar: Süre, Düzeltme turu, Hata, Kalite notu. Altında ayrı satır: "İlk kurulum (bir kez): [KURULUM SÜRE]". | Sayılar `olcum.md` ile aynı. |
| **"Yapamadığı şey" kartı** | Tam ekran, lacivert zemin, sarı başlık. 1 saniye. | Her videoda aynı kart; izleyici bu bölümü beklemeyi öğrenir. |
| **Prompt kartı** | Eş aralıklı yazı tipiyle prompt, okunacak kadar ekranda (tahmini 4–6 sn) + "Açıklamada kopyalanabilir hâli var" satırı. | Prompt videodakiyle harfi harfine aynı. |
| **Vurgu kutusu ve ok** | Sarı çerçeve, sarı ok. | Tek karede en fazla bir vurgu. |
| **"Hızlandırıldı ×N" etiketi** | Küçük, sol üst. | Hızlandırılan ya da beklemesi kesilen her bölümde. |
| **Tarih etiketi** | "Kasım 2026 itibarıyla" | Araç davranışı/arayüzü gösterilen bölümlerde. |
| **Müzik** | 3–4 sakin, sözsüz parça; dönüşümlü. | Lisans kaynağı `lisans-notu.md` içinde. Konuşmanın belirgin altında. |
| **Ses efekti** | En fazla 3–4: kronometre başlat/durdur, kart geçişi. | Her kesimde efekt yok. |
| **Bitiş ekranı düzeni** | Son 15–20 sn: solda önerilen video, sağda abone düğmesi, arkada sakin ekran. | Seslendirme bitiş ekranında da sürer; "bir sonraki mantıklı video" sözle söylenir. |

Renk ve yazı tipi: lacivert ve sarının onaltılık kodlarını ve yazı tipi adını bir kez seç, `00_VARLIKLAR/kapak/renk-notu.md` içine yaz; her yerde aynısını kullan (`kronometre.html` içindeki iki renk değişkeni dahil). Sarı üzerine beyaz yazı kullanma (okunmaz); sarı üzerine lacivert, lacivert üzerine sarı/beyaz.

Bu varlıkların ilk kurulumu Bölüm 0.4'te bütçelenmiştir (grafikler tahmini 120 dk, proje şablonu 60 dk).

### 6.4 Kurgu ön ayarları

Bir kez kur, proje şablonu olarak kaydet:

| Ayar | Değer | Not |
|------|-------|-----|
| Ekran kaydı | Tercihen 2560×1440 ya da üstü, 30 kare/sn; ekran 1080p ise 1920×1080 | Zaman çizelgesi her iki durumda 1080p |
| Uzun video zaman çizelgesi | 1920×1080, 30 kare/sn | Ekran kaydıyla aynı kare hızı; farklı olursa imleç hareketi takılır |
| Dikey zaman çizelgesi | 1080×1920, 30 kare/sn | Aynı projede ikinci zaman çizelgesi |
| Kanal düzeni | V1 ekran, V2 büyütme/kopya, V3 grafik, V4 altyazı; A1 ses, A2 müzik, A3 efekt | Her videoda aynı; şablonda boş ve adlandırılmış gelsin |
| Yakınlaştırma ön ayarı | **1440p kayıtta:** %115 ve %133 (kayıpsız). **4K kayıtta:** %150 ve %200. **1080p kayıtta:** tek ön ayar, %130; daha fazlası çekimde tarayıcı yakınlaştırmasıyla | Yumuşak giriş-çıkış. Yüzdeler 1080p zaman çizelgesine sığdırılmış görüntüye göredir |
| Ses zinciri | Gürültü azaltma → seviye sıkıştırma → sınırlayıcı | Ön ayar olarak kayıtlı |
| Ses yüksekliği hedefi | Konuşma tümleşik yaklaşık −14 LUFS, tepe −1 dB altında | **[Gözlem]** YouTube'un oynatmada ses yüksekliğini normalleştirdiği ve bu düzeyin yaygın hedef olduğu kabul edilir; resmî taahhüt değildir. Kendi videonu başka kanalların videolarıyla art arda dinleyerek kontrol et. |
| Müzik seviyesi | Konuşmanın tahmini 20–25 dB altında | Telefon hoparlöründe konuşmayı örtmüyor mu, dinle |
| Altyazı stili (dikey) | Kalın sans-serif, beyaz, lacivert kutu; vurgu sarı; en fazla 2 satır | Stil olarak kayıtlı |
| Dışa aktarma (uzun) | H.264, .mp4, 1080p, kaynak kare hızı | Bit hızı için YouTube'un önerilen yükleme ayarları sayfasına bak **[Resmî — yayın öncesi doğrula]**. Ekran kaydında yazı keskinliği için bit hızını düşük tutma. |
| Dışa aktarma (dikey) | H.264, .mp4, 1080×1920 | Filigran/bitiş logosu kapalı |

---

## 7. Darboğazlar ve zaman tuzakları

### 7.1 En büyük maliyet: elle koşu

Kanalın kapağı "3 sa → 12 dk" diyor. O 3 saati ölçmek için görevi gerçekten elle yapmak gerekir. Elle koşu haftalık takvimde ayrı satırdır (Bölüm 2.1) ve bir **üst sınırı** vardır: **kendi yaptığın elle görev en fazla 60 dakika.** Haftalık toplam bu sınırla tahmini 11 sa 40 dk'dır; sınır aşılırsa hafta tutmaz.

| Yol | Nasıl | Haftaya maliyeti | Kapakta kullanılabilir mi |
|-----|-------|------------------|---------------------------|
| **C. Görevi küçült (varsayılan)** | "3 saatlik aylık rapor" yerine "45 dakikalık haftalık özet". | Görev süresi + 15 dk (en fazla 1 sa 15 dk) | Evet; kapak "45 dk → 6 dk" olur. Fark küçülür ama gerçek kalır. |
| **B. İşi yapan birine ölçtür** | Bir muhasebeci/İK'cı kendi ortamında, kurgusal veriyle yapar; süreyi ve ekran kaydını verir. `izin-onay.md` imzalanır. | Koordinasyon tahmini 30 dk; kişiyi bulmak Y−3'te başlar | Evet; videoda ve açıklamada kimin ölçtüğü söylenir. M serisi ve 60 dakikayı aşan görevler için doğru yol. |
| **A. Uzun görevi kendin yap** | Görevi baştan sona elle yap, kaydet. | Görev süresinin tamamı; o hafta üretim yapılmaz | Evet. **Yalnızca stoktan yayın yapılan bir haftada:** o hafta yeni video üretmezsin, stoktaki video yayınlanır, sen uzun elle koşuyu çekersin. Stok 2 videoya çıkmadan bu yola girme. |
| **D. Bir kısmını ölç, gerisini tahmin et** | 400 satırın 50'sini elle yap, süreyi çarp. | Kısa | **Hayır.** Videoda "tahmini" diyerek anlatılabilir; kapağa ve başlığa tahmin yazılmaz (01 belgesi, veto sorusu V2). |

İlk 10 videoda uygulama:

| Yayın | Elle koşu | Yol |
|-------|-----------|-----|
| 1 (7 alışkanlık) | Tek teklif e-postası; kısa | Kendin, C sınırının içinde |
| 2 (3 saatlik Excel işi) | "3 saat" çalışma başlığıdır. Senaryo dosyası 650 satırlık dosya için elle süreyi tahmini 30–60 dk öngörüyor (ölçülmeden bilinmez) | Kendin; sınırın içinde. Koşu 60 dakikayı aşarsa yarıda kesme, bitir: ilk iki video yayın başlamadan üretildiği için (Bölüm 2.2) o dönemde haftalık yayın baskısı yoktur. Başlık ve kapak ölçülen süreye göre değişir. |
| 3, 4, 10 | Elle koşu yok | — |
| 5 (sunum) | Tahmini 60 dakikanın üstünde olabilir | C: slayt sayısını sınırla; ya da B |
| 6 (Excel formülü) | Görev başına süre yerine çalıştı/çalışmadı | — |
| 7, 8 | Meslekten kişi / hakem | B |
| 9 (bir hafta e-posta) | Taban haftası | Günlük ölçüm, haftaya yayılır (Bölüm 1.11) |

Kural: uzun elle süresi olan iki videoyu arka arkaya planlama.

### 7.2 Mükemmeliyetçiliğin zaman yediği yerler

| Tuzak | Belirti | Sınır |
|-------|---------|-------|
| **Kurguda süsleme** | Geçiş, ses efekti, animasyon denemek | Proje şablonundaki varlıklar dışında yeni efekt yok. Kurgu 150 dk'yı aşarsa dışa aktar, telefonda izle, yalnızca notları düzelt. |
| **Seslendirmeyi baştan almak** | Tek cümle için bütün bölümü yeniden kaydetmek | Hook 3 deneme, diğer bölümler en fazla 2. Yanlış cümle tek başına yeniden kaydedilir. |
| **Kapakta piksel oynamak** | Yazıyı 2 piksel kaydırıp durmak | 25 dk. Şablonda yalnızca sayı, etiket ve ekran parçası değişir. |
| **Senaryoyu çekimden önce "bitirmek"** | Sonucu bilmeden sonuç cümlesi cilalamak | Yer tutucu bırak, kilitle, çek. |
| **Araç denemek** | Her hafta yeni kurgu/altyazı aracı | Üretim haftasında araç değiştirilmez. Araç denemesi ayda bir, ayrı 30 dk. |
| **Yapay zekâ taslağını düzeltmek** | Taslağı cümle cümle onarmak | Taslak yapı içindir. 10 dk'da toparlanmıyorsa at, iskeletten kendin yaz. |
| **İstatistik yenilemek** | Yayından sonra saatte bir Studio'ya bakmak | Yayın günü 1 kez (yorumlar için), sonra 48 saat ve 7 gün. Arada bakmak karar değiştirmez. |
| **Dört platformu eşit sevmek** | Her platform için ayrı kurgu | Tek dikey ana dosya; yalnızca açıklama metni değişir. Platform, ölçülmüş dağıtım süresi izin verince eklenir. |
| **Örnek veriyi yeniden kurmak** | Her videoda sıfırdan kurgusal şirket | Tek kurgusal şirket, birkaç veri seti; `00_VARLIKLAR/ornek-veri` içinden kullan. |
| **Kontrol listesini baştan sona okumak** | Her aşamada 20 madde işaretlemek | Her listenin yalnızca **kapısı** (en fazla 6 madde) her videoda işaretlenir; kapı başına tahmini 2 dk, haftada toplam 15–20 dk ve aşama sürelerinin içindedir. Listenin kalanı ilk 4 videoda ve sonra ayda bir denetimde okunur. |

### 7.3 Asla kısaltılmayacaklar

1. **Elle koşu ve süreli koşu.** Kanalın tek kanıtı.
2. **Ön deneme (Aşama 1, adım 7).** 10 dakika; çöken bir videonun senaryosuna ve çekimine harcanacak saatleri kurtarır.
3. **Senaryonun sesli okunması.** Yazıda iyi duran cümle ağızda takılır; kayıtta fark edilen cümle yeniden kayıt, yeniden temizlik ve kurguda yeniden hizalama demektir.
4. **Hook'un üç kez kaydedilmesi.** Videoyu açan herkes ilk saniyeleri görür; sonraki her bölümü daha azı.
5. **"Yapamadığı şey" bölümü.** Her videoda gerçek bir sınır. Bulunamadıysa yeterince zorlanmamıştır; bir tuzak veri daha dene.
6. **Prompt'un yeni sohbette yeniden denenmesi.**
7. **Telefonda baştan sona izleme.** Okunmayan ekran kaydı videoyu bitirir.
8. **Sayı tutarlılığı** (Bölüm 4.2).
9. **Ölçüm koşulunun söylenmesi:** ön deneme sayısı, hazır prompt, kurulum süresi (Aşama 4).
10. **48 saat kontrolünde tek çıkarımın yazılması.** Yazılmayan çıkarım bir sonraki videoya taşınmaz.

### 7.4 Bir şey ters giderse

| Durum | Karar |
|-------|-------|
| Çekimde yapay zekâ beklenenden kötü çıktı, fark küçük | Videoyu çevir: "Bu işte neden işe yaramadı" (01 belgesi, formül F8). Sonucu düzeltmek için koşuyu tekrarlayıp iyisini seçme. |
| Araç çekimle yayın arasında arayüz/model değiştirdi | Açıklamaya ve sabit yoruma tarihli not. Süreli koşuyu etkileyen bir değişiklikse koşuyu yeniden çek. |
| Hafta içi zaman kalmadı | Stoktaki videoyu yayınla (Bölüm 2.2). Stok yoksa kapsamı küçült; yarım videoyu yayınlama. |
| Konuk ya da hakem son anda çekildi | Video ertelenir, yedek video girer (Bölüm 1.11). Konuğun yerine isimsiz "bir uzman" yazılmaz. |
| Özel kapak, sabit yorum ya da tıklanabilir bağlantı açık değil | Bölüm 0.3. |
| Yayından sonra olgusal hata bulundu | Sabit yorum + açıklama başına tarihli düzeltme. Hata ölçümdeyse başlık ve kapağı da düzelt. |
| Kısa video uzun videodan çok daha iyi gitti | O anı konu alan bir uzun video fikri aç; fikir havuzuna gerekçesiyle yaz. |

---

## İlgili belgeler

- `01-icerik-uretim-sistemi.md` — fikir filtresi, paketleme, hook, kurgu yapıları (KG1–KG7), kronometre kuralı (6.1), tutma araçları, CTA
- `02-buyume-stratejisi.md` — haftalık takvimin büyüme işleri (B2), prompt dosyası ve e-posta listesinin aşamaları (B7), haftalık analiz rutini (B8), ilk Studio oturumunda doğrulanacaklar listesi
- `senaryolar/` — yazılmış senaryolar (şablonun dolu örnekleri)
- `sablonlar/` — bu belgedeki aşamaların doldurulabilir şablonları
