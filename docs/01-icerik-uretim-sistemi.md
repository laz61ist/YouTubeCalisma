# 01 — İçerik Üretim Sistemi

**Kanal:** Kısa Mesai · **Vaat:** "Aynı işi yarı sürede bitir." · **Belge tarihi:** 2026-11-16

Bu belge tek bir soruya cevap verir: bir fikir, tıklanan ve sonuna kadar izlenen bir videoya hangi adımlarla dönüşür? Sıra sabittir:

**Fikir filtresi → Paket (başlık + kapak) → Hook + açılış sahnesi → Kurgu iskeleti → Tutma araçları → CTA → Çekim**

Paket yazılmadan senaryoya, senaryo bitmeden çekime geçilmez.

### Bu belgedeki sayılar ve yer tutucular

- Başlık ve kapaklardaki süreler **çalışma değeridir**. Yayınlanan sayı, çekimde kronometreyle ölçülen sayıdır. Ölçüm farklı çıkarsa başlık ve kapak ölçüme göre değişir, ölçüm başlığa göre değil. Biçimi göstermek için belgede tek bir ortak örnek kullanılır: **"3 sa → 12 dk" (çalışma değeri)**. Başka her yerde yer tutucu vardır.
- `[ELLE SÜRE]` = aynı işin yapay zekâsız yapıldığında aldığı, ayrıca ölçülmüş süre. `[YZ SÜRE]` = yapay zekâyla, kontrol ve düzeltme dâhil ölçülen süre. `[N]` = çekimde ya da sayımda ortaya çıkacak adet. `[ÇEKİMDE ÖLÇ]` = çekimde ölçülecek değer. `[ÇEKİMDE: …]` = çekimde ne olduysa ona göre yazılacak ya da silinecek cümle.
- **Sonuç bildiren hiçbir cümle çekimden önce yazılmaz.** "Hata çıktı", "iki slaytı elle düzelttim", "en çok kullandığım sekizinci sırada" gibi cümleler bu belgede yalnızca koşullu yer tutucu olarak durur.
- "Tahmini" yazan her eşik başlangıç varsayımıdır; ilk 10 videonun verisiyle yeniden ayarlanır.
- **[Resmî]** = YouTube'un kendi yardım sayfalarında / Studio arayüzünde açıkladığı şey. **[Gözlem]** = sektörde yaygın kabul gören ama YouTube'un taahhüt etmediği pratik. Resmî maddelerin kaynak bağlantıları ve doğrulama durumu `02-buyume-stratejisi.md` içindedir.

### Terimler ve kodlar

| Terim / kod | Anlamı |
|-------------|--------|
| **prompt** | Seslendirmede ilk geçtiği yerde bir kez açıklanır: "prompt, yani yapay zekâya yazdığın talimat". Sonrasında hep "prompt". Başlıkta ve kapakta da "prompt". |
| **e-posta** | Belgenin ve seslendirmenin dili. "Mail" yalnızca izleyicinin kendi cümlesi tırnak içinde aktarılırken geçer ("Müşteriye teklif maili yaz."). |
| **sabitlenmiş yorum** | Videonun altına sabitlenen ilk yorum. |
| **metin bloğu** | Kapakta tek bakışta okunan yazı kümesi (bkz. 3.2). |
| **B, G, K, M, İ, P** | İçerik kategorileri: başlangıç, görev, araç testi, meslek, işletme, kariyer. Tek harf yalnızca kategori için kullanılır. |
| **F1–F16** | Başlık formülleri (2.2). |
| **Yerleşim A / B / C** | Kapak yerleşimleri; A1–A3, B1–B3, C1–C3 bunların örnekleridir (3.3). |
| **H1–H10** | Hook kalıpları (Bölüm 4). **SH1–SH4:** Shorts açılış kalıpları (4.4). |
| **S1–S6** | Açılış sahneleri (Bölüm 5). |
| **KG1–KG7** | Kurgu iskeletleri (Bölüm 6). |

---

## 1. Fikir filtresi (fikir başına tahmini 15 dakika)

Her fikir önce tek cümleye indirilir. İki kalıptan biri kullanılır:

- **Süre kalıbı:** "[Kim], [hangi işi] [elle süre] yerine [yeni süre]de bitiriyor."
- **Çıktı kalıbı:** "[Kim], [hangi çıktıyı] [vasat hâl] yerine [gönderilebilir hâl]e getiriyor; fark [neyle] gösteriliyor."

İkisi de yazılamıyorsa fikir henüz video değildir, konudur. Çıktı kalıbındaki son parça zorunludur: fark ya bir hakemle (kör seçim, uzman, önceden yazılmış ölçüt listesi) ya da ekranda yan yana duran iki çıktıyla gösterilir. Seçilen kalıp kapaktaki çiftin türünü de belirler (bkz. 3.1).

### 1.1 Veto soruları (biri "hayır" ise puanlamaya geçme)

| # | Soru | "Hayır" ise |
|---|------|-------------|
| V1 | Görev ekran kaydıyla baştan sona gösterilebiliyor mu? | Fikri at veya gösterilebilir bir alt göreve indir |
| V2 | Farkı çekimden önce ölçebilecek durumda mıyım? (Süre kalıbında: işi elle kendim yapabiliyor ya da yapan birine yaptırabiliyor muyum? Çıktı kalıbında: hakem ya da ölçüt listesi belli mi?) | Ölçüm yolu bulunana kadar beklet. Ölçümün kendisi burada yapılmaz; paket aşamasında, çekimden önce yapılır (bkz. 2.1 adım 8) |
| V3 | Kullanacağım veri gerçekçi ama kişisel/gizli bilgi içermiyor mu? | Örnek veri seti hazırla, sonra puanla |
| V4 | Sonuç kötü çıksa bile yayınlayabileceğim bir video olur mu? | Olmuyorsa bu bir deney değil reklamdır; at |

### 1.2 Puanlama tablosu (her ölçüt 0–2 puan, toplam 16)

| Ölçüt | 0 puan | 1 puan | 2 puan |
|-------|--------|--------|--------|
| **1. Sorun tanıdıklığı** — ideal izleyici bu işi yapıyor mu? | Çok az kişinin işi | Belli bir meslek yapıyor ya da iş seyrek (yılda birkaç kez) | Beyaz yakalının çoğu haftada en az bir kez yapıyor (e-posta, Excel, rapor, sunum) |
| **2. Arama dili** — izleyici bunu aracın adıyla değil sorunun adıyla arar mı? | Sadece araç/özellik adı | Araç + sorun karışık | Saf sorun cümlesi ("excel raporu hızlı hazırlama") |
| **3. Ölçülebilir fark** — süre farkı, hakemli kalite farkı ya da önce/sonra çıktı farkı tek bakışta anlaşılır mı? | Fark yok, ölçülemiyor ya da yalnızca "bence daha iyi" | Fark var ama görmek için açıklama gerekiyor | Fark kapakta tek çiftle anlatılıyor: iki süre, bir hakem kararı ya da yan yana iki çıktı |
| **4. Görsel kanıt** — önce/sonra ekranda yan yana gösterilebilir mi? | Sonuç soyut | Sonuç gösterilir ama anlatım ister | Tek karede "öncesi karışık, sonrası temiz" görünür |
| **5. "Yapamadığı şey"** — dürüst bir sınır/başarısızlık bölümü çıkar mı? | Çıkmıyor | Sınır var ama genel ("kontrol et") | Göreve özgü, öğretici bir sınır bekleniyor (yanlış formül, uydurma rakam, bozuk Türkçe, sorumluluk devredilemiyor) |
| **6. Kopyalanabilir çıktı** — izleyici videodan bir prompt/şablonla ayrılır mı? | Yok | Var ama kişiye özel uyarlama çok | Kopyala-yapıştır çalışır, 1–2 alan değiştirilir |
| **7. Seri ve Shorts potansiyeli** — 2–3 Shorts ve bir devam videosu çıkar mı? | Tek atımlık | Shorts çıkar, devam çıkmaz | İkisi de çıkar (ör. "muhasebeci" → "İK", "satış") |
| **8. Üretim maliyeti** — tek kişi bunu bir haftalık takvime sığdırır mı? | Dış uzmana ya da birden çok güne yayılan çekime bağlı | Özel veri seti / örnek malzeme ya da bir tanıdığın kısa yardımı gerek | Elde olan malzemeyle bir günde çekilir |

**Ölçütler nasıl doldurulur (tahminle değil):**

- **Ölçüt 2 (2 dakika):** YouTube arama kutusuna sorun cümlesinin ilk iki kelimesini yaz ("excel rapor", "cv hazırlama"). Otomatik tamamlamada görev cümlesine benzer bir öneri çıkıyorsa 2; yalnızca araç adıyla birlikte çıkıyorsa 1; hiç çıkmıyorsa 0. Çıkan önerileri fikir kartına aynen kopyala; izleyici cümlesi (2.1 adım 1) oradan beslenir. **[Gözlem]** Otomatik tamamlama o ifadenin arandığına dair kaba bir işarettir; hacim göstermez.
- **Ölçüt 3:** Fikir cümlesinin "yerine" kelimesinden önceki ve sonraki parçalarını kapak çifti olarak yaz (bkz. 3.1). Yazılabiliyorsa en az 1; çift, açıklama gerektirmeden anlaşılıyorsa 2.
- **Ölçüt 5:** 10 dakikalık kaba bir ön deneme yap; karşılaştığın ilk sınırı not et. Ön deneme yapılmadan 2 verilmez.
- **Ölçüt 7:** Üç aday Shorts anını birer satırla yaz (bkz. 4.4). Üçü yazılamıyorsa en fazla 1.
- **Ölçüt 8:** Çekimden önce hazırlanması gereken her şeyi listele (veri seti, elle ölçüm, görüşme, deney günleri).

### 1.3 Eşik (tahmini; ilk 10 videodan sonra yeniden ayarlanır)

| Toplam | Karar |
|--------|-------|
| **12–16** | Çek. Paket aşamasına geç. |
| **9–11** | Düşük puanlı ölçütü düzelt (çoğu zaman görevi daraltmak ya da farkı ölçülebilir kılmak yeter), yeniden puanla. |
| **0–8** | Arşive at; üç ay sonra tekrar bak. |

Ek kural: **Ölçüt 1 ya da ölçüt 3'ten 0 alan fikir toplamı ne olursa olsun çekilmez.** Kanalın vaadi bu iki ölçüte dayanır: tanıdık bir iş ve ölçülmüş bir fark.

Ölçüt 8'den 0 alan fikir çekilebilir, ama **art arda iki hafta** takvime konmaz ve hazırlığına yayın tarihinden en az iki hafta önce başlanır.

### 1.4 İlk 10 videonun puanları ve iki karşı örnek

Puanlar ön değerlendirmedir (tahmini); ölçüt 2 ve 5 yukarıdaki yöntemle doğrulandıkça güncellenir.

| Yayın | Fikir cümlesi (kısaltılmış) | Kalıp | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | Toplam | Karar |
|-------|-----------------------------|-------|---|---|---|---|---|---|---|---|--------|-------|
| 1 | Müşteriye teklif yazan biri, tek satırlık isteğin verdiği vasat cevabı yedi değişiklikle bugün gönderilebilir bir teklif e-postasına çeviriyor; fark ilk ve son cevabın yan yana gösterilmesiyle ortaya çıkıyor | Çıktı (önce/sonra) | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 1 | 14 | Çek |
| 2 | Ofis çalışanı, dağınık satış dökümünü [ELLE SÜRE] yerine [YZ SÜRE]de yönetici özetine çeviriyor | Süre | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 15 | Çek |
| 3 | Türkçe iş yazan biri, beş işte üç aracın cevabını isim görmeden puanlıyor; fark ölçüt listesi ve ikinci bir kör puanlayıcıyla gösteriliyor | Çıktı (hakem) | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 13 | Çek (ilk hâli 11'di; aşağıya bak) |
| 4 | Hiç kullanmamış biri, ilk vasat cevabı kendi işinden bir görevde kullanılabilir cevaba çeviriyor; fark aynı görevin ilk ve son cevabıyla gösteriliyor | Çıktı (önce/sonra) | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 2 | 13 | Çek |
| 5 | Ofis çalışanı, yönetim sunumunu [ELLE SÜRE] yerine [YZ SÜRE]de hazırlıyor | Süre | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 15 | Çek |
| 6 | Excel kullanan biri, hatırlamadığı formülü tarif ederek yazdırıyor ve yanlış sonucu kontrol adımıyla yakalıyor | Çıktı (önce/sonra) | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 14 | Çek |
| 7 | Muhasebeci, her ay tekrar eden [N] işi [ELLE SÜRE] yerine [YZ SÜRE]de bitiriyor; hangisinin devredilmeyeceği gösteriliyor | Süre | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 0 | 12 | Çek (sınırda; hazırlık iki hafta önce başlar) |
| 8 | İş arayan biri, CV'sini elle ve yapay zekâyla iki sürümde hazırlıyor; farkı hangisinin hangisi olduğunu bilmeyen bir İK uzmanı gösteriyor | Çıktı (hakem) | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 13 | Çek (hazırlık iki hafta önce başlar) |
| 9 | Ofis çalışanı, bir haftalık iş e-postalarını e-posta başına [ELLE SÜRE] yerine [YZ SÜRE]de yazıyor | Süre | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 0 | 13 | Çek (deney yayından önceki hafta yapılır) |
| 10 | Ofis çalışanı, on tekrar eden işi on hazır prompt'la yaptırıyor; her prompt'ta önce/sonra çıktı gösteriliyor | Çıktı (önce/sonra) | 2 | 1 | 1 | 1 | 1 | 2 | 2 | 2 | 12 | Çek (sınırda) |
| — | Yeni çıkan bir modelin özellik turu | Yazılamıyor | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 2 | 5 | At (ölçüt 3 = 0) |
| — | Toplantı notunu aksiyon listesine çevirmek | Süre | 2 | 2 | 1 | 2 | 1 | 2 | 1 | 2 | 13 | Çek |

**Filtrenin fikri değiştirdiği yer — Yayın 3.** "Üç aracı karşılaştırıyorum" hâliyle puan 11'di: ölçüt 3 = 1 (puanı tek başıma veriyorum, fark "bence"ye yakın), ölçüt 6 = 1 (izleyici elinde bir şeyle ayrılmıyor). İki düzeltme yapıldı: (a) puanlama ölçütleri testten önce yazılır ve aynı cevapları, araç adlarını görmeyen ikinci bir kişi de puanlar; (b) beş görevin prompt'ları ve "hangi iş için hangisi" tablosu açıklamaya konur. Puan 13'e çıktı. "Model özellik turu"nun atılıp Yayın 3'ün kalmasının nedeni de budur: ilki bir aracı anlatır, ikincisi tanıdık beş işte ölçülmüş bir fark gösterir.

**Sınırdaki iki video.** Yayın 7'yi güvenceye almanın yolu ölçüt 8'dir: görüşülecek muhasebeci çekimden iki hafta önce ayarlanır. Yayın 10'da ölçüt 3 ve 4, her prompt'un yanında önceki videolardan gerçek bir önce/sonra kesiti gösterilerek 2'ye çıkar; kesit bulunamayan prompt listeye girmez.

---

## 2. Paketleme önce: başlık + kapak videodan önce yazılır

### 2.1 Süreç (fikir başına tahmini 40–50 dakika; elle ölçüm hariç)

1. **İzleyici cümlesi (2 dk):** İzleyicinin sorunu kendi ağzından nasıl söylediğini yaz. Örn. "Her ay sonu aynı raporu saatlerce hazırlıyorum." Kaynağı varsa (yorum, otomatik tamamlama önerisi) yanına not et.
2. **Arama doğrulaması (5 dk):** İzleyici cümlesinin çekirdeğini (2–3 kelime) YouTube aramasına yaz. Üç şeyi not et: (a) otomatik tamamlamanın önerdiği ifadeler, (b) ilk 10 sonuçtan kaçının Türkçe olduğu ve kaçının aynı görevi baştan sona gösterdiği, (c) bu sonuçların başlıklarında tekrar eden kelimeler. Karar: sonuçlarda görevi ölçümle gösteren video yoksa başlığa görev adını aynen koy; çok varsa başlıkta kanalın farkını öne çıkar (kronometre, kontrol dâhil süre, "yapamadığı şey"). Hiç öneri ve sonuç çıkmıyorsa bu video arama için değil öneri/ana sayfa için paketlenir; başlıkta sorun cümlesi kalır ama arama trafiği beklenmez.
3. **10 başlık (10 dk):** 2.2'deki formüllerden en az 5 farklısını kullanarak 10 başlık yaz. İlk aklına gelen genelde en sıradan olandır; onuncuya kadar git.
4. **Eleme (5 dk):** Her başlığı 2.4'teki hata listesinden geçir, 3 tanesini bırak.
5. **3 kapak eskizi (10 dk):** Kâğıda veya boş bir tuvale, 3.3'teki üç yerleşimden birer eskiz. Sadece kutu ve metin; tasarım değil.
6. **Çift kontrolü (3 dk):** Süre **en fazla bir yerde** durur.
   - Kapak süre çifti taşıyorsa ("[ELLE SÜRE] → [YZ SÜRE]") başlık görevi ve bağlamı söyler; başlıkta süre yoktur.
   - Başlık süre taşıyorsa (F1, F11, F12) kapak çifti süresizdir: çıktı çifti ("DAĞINIK → ÖZET") kullanılır.
   - Süre kalıbıyla yazılmış fikirlerde kanalın varsayılanı birincisidir: süre kapakta, görev başlıkta.
   - Çıktı kalıbıyla yazılmış fikirlerde süre ne kapakta ne başlıkta yer alır; videoda ölçülür ve ne çıktıysa söylenir.
7. **Vaat testi (2 dk):** "Bu başlık ve kapağın verdiği sözü videonun hangi dakikasında tutuyorum?" Cevap bir zaman damgası olmalı. Yoksa paket ya da video yanlış.
8. **Ölçüm (süre ayrıca tutulur):** Elle süre, hakem görüşü ya da ölçüt listesi çekimden önce alınır. Elle ölçüm çoğu zaman işin en uzun adımıdır; takvimdeki yeri için `03-yapim-is-akisi.md` Bölüm 7.1'e bak. Ölçülen değer paketteki bütün yer tutuculara aynı biçimde yazılır.
9. **Senaryoya geç.** Hook'un ilk cümlesi, başlığın verdiği sözü kendi kelimeleriyle tekrar eder (bkz. Bölüm 4).

Yayın sonrası: **[Resmî]** Studio'daki başlık/kapak testi özelliği en fazla 3 varyantı karşılaştırır ve kazananı tıklanma oranına göre değil izlenme süresine göre seçer; yani tık tuzağı paket testte de kazanmaz. Hazırladığın üç paketten ikisini ya da üçünü oraya yükle. Uygunluk koşulları ve sıfırdan kanal için gerçekçi beklenti `02-buyume-stratejisi.md` B4'te; özelliğin hesabında açık olup olmadığını Studio'da kontrol et.

### 2.2 Başlık formülleri

Her formül kanalın imzasından en az bir zorunlu parça taşır: **ölçülmüş süre**, **kontrolün süreye dâhil olması**, **tek ve gerçek görev**, **hakem** ya da **"yapamadığı şey"**. "Bu kanalda farkı" sütunu doldurulamayan bir başlık, formüle uysa bile kullanılmaz. Köşeli parantezli değerler çekimde ölçülür.

| # | Formül | Örnek | Bu kanalda farkı (zorunlu parça) | Ne zaman |
|---|--------|-------|----------------------------------|----------|
| F1 | **[Elle süre]lik [iş]i [yeni süre]de bitirmek** | [ELLE SÜRE]'lik Excel İşini [YZ SÜRE]'de Bitirmek | İki süre de ölçülmüş; yeni süre kontrol dâhil. Kapak süresiz olur | G kategorisi; süre başlıkta taşınacaksa |
| F2 | **[Araç]ı yanlış kullanıyorsun: aynı görevde [N] [düzeltme]** | ChatGPT'yi Yanlış Kullanıyorsun: Sonucu Değiştiren 7 Alışkanlık | Yedi ayrı örnek değil, tek gerçek görev; ilk ve son cevap yan yana; iddia videoda gösterilemezse başlık değişir | B kategorisi; "denedim, vasat" diyen izleyici |
| F3 | **[A], [B], [C]: [belirli iş]te kör test, [N] gerçek iş** | ChatGPT, Gemini, Claude: Türkçe Kör Test, 5 Gerçek İş | İsimler kapalı; ölçütler testten önce yazılı; kazanan başlıkta yok | K kategorisi |
| F4 | **[Meslek] için yapay zekâ: [N] iş, biri devredilmez** | Muhasebeciler İçin Yapay Zekâ: Her Ay Tekrarlanan [N] İş, Biri Devredilmez | Her iş kronometreli; devredilmeyen iş başlıkta söz veriliyor | M serisi. "Biri devredilmez" yalnızca çekimde böyle çıktıysa |
| F5 | **[Süre] boyunca [şey]i yapay zekâya yaptırdım: [N] adet, [N] tanesini kendim yaptım** | Bir Hafta E-postalarımı Yapay Zekâya Yazdırdım: [N] E-posta, [N] Tanesini Kendim Yazdım | Sayım gerçek; başarısız olanlar başlıkta | Deney videoları |
| F6 | **[İki sürüm hazırladım], [uzman] hangisini seçti?** | Elle Yazılmış CV mi, Yapay Zekâ CV'si mi? İK Uzmanı Hangisini Seçti | Uzman hangisinin hangisi olduğunu bilmiyor; karar videodan önce bilinmiyor | Dış hakemli videolar |
| F7 | **Hiç [yapmamış] biri için [konu]: ilk gerçek iş, [süre]de** | Hiç Kullanmamış Biri İçin Yapay Zekâ: İlk Gerçek İşin 30 Dakikada | Tanıtım turu değil; video izleyicinin kendi işinden bir görevle bitiyor. Süre, izleyicinin uygulama süresi olarak ölçülmüş | Giriş videoları, arama trafiği |
| F8 | **[İş]i yapay zekâya yaptırmak: çalışan [N], çalışmayan [N] örnek** | Excel Formülünü Yapay Zekâya Yazdırmak: Çalışan [N], Çalışmayan [N] Örnek | Çalışmayanlar başlıkta; sayılar çekimden sonra yazılır | "Yapamadığı şey"i güçlü konular |
| F9 | **Her gün kullandığım [N] prompt: her biri gerçek bir işte** | Her Gün Kullandığım 10 Prompt: Her Biri Gerçek Bir İşte | Liste değil; her prompt bir önce/sonra çıktısıyla | Kaynak videoları, kaydetme davranışı |
| F10 | **[Sorun cümlesi]? [Çözümün adı], kronometreyle** | Toplantı Notları Yığılıyor mu? Aksiyon Listesine Çevirmeyi Kronometreyle Denedim | İzleyicinin cümlesi + ölçüm sözü | Arama ağırlıklı konular |
| F11 | **[İş]: elle [süre], yapay zekâyla [süre] — fark nerede?** | Aylık Rapor: Elle [ELLE SÜRE], Yapay Zekâyla [YZ SÜRE] — Fark Nerede? | Süre dökümü (prompt, uygulama, kontrol) videoda ayrı ayrı. Kapak süresiz olur | Kalite karşılaştırması vurgulanacaksa |
| F12 | **Kontrol dâhil [N] dakikada [somut çıktı]** | Kontrol Dâhil [YZ SÜRE]'de Yönetim Sunumu: Boş Sayfadan Son Slayta | "Kontrol dâhil" ifadesi başlıkta. Kapak süresiz olur | Tek çıktılı görevler |
| F13 | **[Araç]ın [iş]te yapamadığı [N] şey** | Yapay Zekânın Excel'de Yapamadığı [N] Şey | "Yapamadığı şey" bölümlerinden derlenir; her madde yayınlanmış bir videodaki gerçek bulgu | En az 5 video yayınlandıktan sonra |
| F14 | **[Küçük işletme türü] için: [iş]i [süre]de** | Tek Kişilik E-ticaret İçin: [N] Ürün Açıklaması [YZ SÜRE]'de | Adet ve süre ölçülmüş; kaçının elle düzeltildiği videoda | İ kategorisi |
| F15 | **[İş]: [N] dakika iş, [N] dakika kontrol** | Aylık Raporu Yapay Zekâya Yaptırdım: [N] Dakika İş, [N] Dakika Kontrol | Kontrol süresi ayrı ölçülüp başlığa çıkıyor | Hata riski yüksek işler (rakam, formül, mevzuat) |
| F16 | **[İş alanı]nda yapay zekâya devretmediğim [N] iş (ve nedeni)** | Muhasebede Yapay Zekâya Devretmediğim [N] İş ve Nedeni | Sorumluluk sınırı konusu; her madde denenmiş ve neden devredilmediği gösterilmiş | M serisinin devam videoları |

### 2.3 Başlık yazım kuralları

- **Önce sorun ya da sonuç, sonra araç.** İdeal izleyici sorunu arar. "Excel raporu" başa, "ChatGPT" sona. İstisna: F2 ve F3, aracın adının kendisi sorunun parçası olduğunda.
- **Kritik kelimeler ilk 40–45 karakterde.** **[Gözlem]** Mobilde ve önerilen video sütununda başlıkların sonu kesilir; kesilme noktası cihaza göre değişir. Yayından önce Studio önizlemesinde ve telefonda kontrol et.
- **Bir başlıkta en fazla bir sayı çifti.** Süre çifti varsa üçüncü sayı ("7 adımda") eklenmez.
- **Türkçe yazım:** "yapay zekâ" şapkalı; başlıkta her kelimenin ilk harfi büyük; TAMAMI BÜYÜK kelime yok.
- **Sayı ölçülmüş olmalı ve her yerde aynı olmalı.** Ölçüm 14 dakika çıktıysa başlık, kapak, seslendirme ve açıklama "14 dakika" der. Yuvarlama izleyici lehine değil gerçeğe doğru yapılır.
- **Sonucu varsayan başlık çekimden sonra yazılır.** "Biri devredilmez", "çalışmayan [N]", "[N] tanesini kendim yazdım" gibi parçalar ancak gerçekleştiyse başlığa girer.

### 2.4 Kaçınılacak başlık hataları

| Hata | Kötü örnek | Neden kötü | Düzeltilmişi |
|------|-----------|------------|--------------|
| Araç adıyla açmak | "ChatGPT ile Excel Kullanımı" | İzleyici sorunu arıyor; fayda yok | "Dağınık Satış Dökümünden Yönetici Özetine: Kronometreyle Denedim" |
| Abartı sıfatı | "İNANILMAZ Yapay Zekâ Hilesi!" | Kanal tonuna aykırı; vaat belirsiz | Sıfatı sil, ölçümü koy |
| Sahte aciliyet / korku | "Bunu Öğrenmezsen İşsiz Kalacaksın" | İzleyicinin korkusunu sömürür; video bu sözü tutamaz | "Her Gün Kullandığım 10 Prompt: Her Biri Gerçek Bir İşte" |
| Panik çerçevesi | "Yarın Sunum Var, Hiçbir Şey Hazır Değil" | Sakin tona aykırı; telaş satıyor | "Yönetim Sunumu: Boş Sayfadan Son Slayta, Kronometreyle Denedim" |
| "Zengin ol" vaadi | "Yapay Zekâyla Ayda 50 Bin TL" | Kanalın açıkça reddettiği vaat | P kategorisinde bile iş/süre odaklı kal |
| Ölçülmemiş sayı | "10 Saniyede Rapor" | Kronometre videoda yalanlar; güven biter | Ölçülen süreyi yaz |
| Sonucu önceden varsaymak | "İK Uzmanı Nereden Anladı?" | Uzman anlamamış olabilir; başlık çekimden önce yazılmış | "İK Uzmanı İkisini Ayırt Edebildi mi?" |
| Hatasız sonuç vaadi | "Ne İstediğini Yaz, Formülü Al" | Videonun kendisi formülün yanlış çıkabildiğini gösteriyor | "Excel Formülünü Yapay Zekâya Yazdırmak ve Doğru mu Diye Kontrol Etmek" |
| Belirsiz zamir | "Bunu Bilmiyordum" | Arama dili yok, merak boş | Görevi adlandır |
| Süreyi iki yerde harcamak | Kapak: "3 sa → 12 dk", başlık: "3 Saatlik İşi 12 Dakikada" | İki alan aynı bilgiyi taşıyor | Süre kapakta kalsın, başlık görevi söylesin (ya da tersi; bkz. 2.1 adım 6) |
| Çok geniş konu | "Yapay Zekâ Rehberi" | Kim için, hangi iş için belli değil | Bir görev, bir kişi |
| Sürüm numarasına bağlanmak | "ChatGPT [sürüm] İncelemesi" | Birkaç ayda eskir; sorun odaklı değil | Göreve bağla, sürümü açıklamaya yaz |
| Her videoda aynı kalıp | 10 videonun 10'u F1 | Kanal sayfası tekdüze görünür | Art arda en fazla 2 video aynı formül |

---

## 3. Kapak görseli sistemi

### 3.1 Sabit kalıp: dönüşüm çifti

Kanalın tanınma işareti renk değil, **"X → Y" çiftidir**: önce ne vardı, sonra ne oldu. Her kapakta tam bir çift bulunur ve kapağın en büyük öğesidir. Çiftin türü, fikir cümlesinin kalıbını izler (Bölüm 1):

| Çift türü | Biçim | Ne zaman |
|-----------|-------|----------|
| **Süre çifti** | "[ELLE SÜRE] → [YZ SÜRE]" — biçim örneği: "3 sa → 12 dk" (çalışma değeri) | Fikir **süre kalıbıyla** yazıldıysa (kronometre yarışı, meslek videosu, deney) ve süre başlıkta taşınmıyorsa. Kanalın imza kapağı budur. |
| **Çıktı çifti** | "VASAT → İŞE YARAR", "DAĞINIK → ÖZET", "SIFIRDAN → İLK İŞ" | Fikir **çıktı kalıbıyla** yazıldıysa ya da süre başlıkta taşınıyorsa. |
| **Soru çifti** | "A B C → ?", "A B → ?" | Sonucu bir hakemin ya da kör testin belirlediği videolarda. Sağ taraf her zaman soru işaretidir; kazanan kapakta gösterilmez. |

Üç kural:

- **Süre farkının çıkıp çıkmayacağı belirsizse süre kapağa konmaz.** Çıktı kalıbındaki bir videoda elle süre yine ölçülür ve videoda söylenir, ama paket ona dayanmaz (örnek: senaryo 01, 2.8 kural 3 — süre yarıdan kısa da çıksa uzun da çıksa kapak aynı kalır).
- **"→" yalnızca "önce → sonra" anlamında kullanılır.** "0 → 30 dk" gibi, önce/sonra olmayan bir bilgiyi okla yazmak yasaktır; kalıbı tanıyan izleyici bunu "sıfır saatlik iş otuz dakikaya çıktı" diye okur.
- **Art arda iki kapak aynı yerleşimde olmaz** (3.3). Süre çifti, süre kalıbındaki videolar için saklanır; her kapağa konursa imza olmaktan çıkar.

**[Resmî]** YouTube özel küçük resimler için 1280×720 piksel, 16:9 oranını önerir; dosya boyutu sınırı için güncel yardım sayfasına bak.

| Öğe | Kural |
|-----|-------|
| **Zemin** | Koyu lacivert, düz veya çok hafif geçişli. Fotoğraf arka plan yok. |
| **Çift** | En kalın kesim. Kapağın en büyük öğesi; kapak yüksekliğinin tahmini üçte biri. Ok ve "sonra" parçası sarı; "önce" parçası Yerleşim B'de beyaz/soluk, diğer yerleşimlerde sarı. |
| **Etiket** | Beyaz, en fazla 2 kelime, çiftin üstünde veya altında: "AYLIK RAPOR", "SUNUM", "5 GÜN". Zorunlu değil. |
| **Görsel kanıt** | Kapağın bir yarısında gerçek ekran görüntüsünden kırpılmış, büyütülmüş tek parça (tablo köşesi, slayt, sohbet kutusu). Okunması gerekmez, türü anlaşılsın yeter. |
| **Boş bölge** | Sağ alt köşe boş bırakılır; YouTube süre etiketi oraya biner. |
| **Yüz** | Zorunlu değil. Kullanılmıyorsa görsel kanıt onun yerini tutar. |

### 3.2 Metin kuralları

- **Metin bloğu sayısı:** Çift tek blok sayılır. Yanına **en fazla 2 kelimelik tek bir etiket** gelir. Kapakta toplam **en fazla 2 metin bloğu** olur. Görsel kanıtın içindeki ekran yazısı (soluk, okunması beklenmeyen; ör. sohbet kutusundaki tek satır) blok sayılmaz; okunması bekleniyorsa sayılır ve etiketin yerini alır. Cümle yazılmaz.
- **Yazı tipi:** Tek aile, her yerde aynı: **Inter** (çift için en kalın kesim, etiket için bir alt kesim). Türkçe harfleri (İ, ı, ğ, ş, â) seçtiğin kesimde yazıp kontrol et; lisans koşulunu indirdiğin kaynaktan doğrula. Aile bir kez seçilir ve `03-yapim-is-akisi.md` 6.3'te anlatılan renk/yazı tipi notuna yazılır; kronometre grafiği ve bölüm kartları da aynı aileyi kullanır.
- **Asgari harf yüksekliği:** 1280×720 tuvalde çiftin büyük harf yüksekliği en az `[TASARIMDA ÖLÇ: kapak 160 px genişliğe küçültüldüğünde 1 saniyede okunan en küçük değer]` pikseldir; etiket bu değerin yarısından küçük olamaz. Değer ilk kapakta ölçülür, nota yazılır, sonraki kapaklarda alt sınır olarak kullanılır.
- **Renk sayısı:** Lacivert, sarı, beyaz. Dördüncü renk yalnızca "öncesi" görselinde (soluk gri) kullanılır.
- **Kontrast (sayısal ölçüt):** Çift ile zemin arasındaki karşıtlık oranı (WCAG formülü) **en az 7:1**; etiket için de aynı. Başlangıç önerisi ve bu belge için hesaplanmış oranları: sarı `#FFD400` / lacivert `#0B1F3A` = 11,5:1; beyaz `#FFFFFF` / aynı lacivert = 16,5:1; soluk gri `#8A94A6` / aynı lacivert = 5,4:1 (bu yüzden gri yalnızca "öncesi" görselinde kullanılır, metinde değil). Farklı ton seçersen oranı herhangi bir karşıtlık hesaplayıcısıyla yeniden ölç. Metin doğrudan lacivert zemin üstünde durur; ekran görüntüsünün üstüne bindirilecekse arkasına lacivert bant konur.
- **Mobil okunurluk testi (her kapak için zorunlu):** Kapağı yaklaşık 160 piksel genişliğe küçült ve telefonda YouTube ana sayfasındaki bir kapağın yanına koy. Çift 1 saniyede okunmuyorsa büyüt veya etiketi at. Açık ve koyu temada ayrı ayrı bak.
- **Birimler:** "sa", "dk", "gün" — noktasız, küçük harf. Sayılar ölçümden gelir.
- **Yasaklar:** Kırmızı ok/daire, şaşkın yüz, emoji, araç logolarının kapağın ana öğesi olması, başlığın aynısını yazmak, kazananı ya da hakem kararını göstermek.

### 3.3 Üç yerleşim

Yerleşim, çiftin kapakta nasıl durduğunu belirler. Aşağıdaki örneklerdeki bütün süre ve adetler yer tutucudur.

#### Yerleşim A — "Çift + kanıt"

Çift bir yarıda büyük, görsel kanıt öbür yarıda. Süre çiftinin doğal yeri: kronometre videoları (G), meslek videoları (M), deneyler.

| Örnek | Tarif |
|-------|-------|
| **A1 — Excel raporu** | Üst-orta: sarı "[ELLE SÜRE] → [YZ SÜRE]". Sol alt: soluk, hafif eğik dağınık Excel parçası (karışık tarihler sarı çerçeveli). Sağ: temiz, küçük özet tablo. Etiket: "DOSYAYI YÜKLEMEDEN". |
| **A2 — Sunum** | Sol: sarı "[ELLE SÜRE] → [YZ SÜRE]". Sağ: üst üste dizilmiş 3 slayt küçük resmi; en öndeki net. Etiket: "SUNUM". |
| **A3 — Muhasebeci** | Sol: beyaz "MUHASEBECİ", altında sarı "[ELLE SÜRE] → [YZ SÜRE]" ([N] işin toplamı). Sağ: banka ekstresi görünümlü tablonun kırpılmış parçası. |

#### Yerleşim B — "Bölünmüş: önce | sonra"

Kapak dikey bir çizgiyle ikiye bölünür: sol soluk/gri "öncesi", sağ parlak "sonrası". Çiftin "önce" parçası sol yarının, "sonra" parçası sağ yarının üstünde durur; sarı ok çizginin üzerindedir. Çıktı ve soru çiftlerinin doğal yeri.

| Örnek | Tarif |
|-------|-------|
| **B1 — Vasat cevap** | Sol yarı gri, soluk: tek satırlık sohbet kutusu ("Müşteriye teklif maili yaz."; görsel kanıt). Üstünde beyaz "VASAT". Sağ yarı sarı çerçeveli: altı yedi satırlık, yapılandırılmış prompt kutusu (satırlar okunmak zorunda değil). Üstünde sarı "İŞE YARAR". Çift: "VASAT → İŞE YARAR". Etiket yok. (Senaryo 01 ile aynı.) |
| **B2 — CV** | Sol: bir CV, üstünde beyaz "A". Sağ: öbür CV, üstünde beyaz "B" (ikisi de aynı parlaklıkta; hangisinin elle yazıldığı belli olmaz). Çizginin altında sarı ok ve sarı "?". Çift: "A B → ?". Etiket: "İK SEÇTİ". |
| **B3 — Sıfırdan başlangıç** | Sol: boş sohbet kutusu, üstünde beyaz "SIFIRDAN". Sağ: bitmiş kısa bir e-posta, üstünde sarı "İLK İŞ". Çift: "SIFIRDAN → İLK İŞ". Etiket: "5 ADIM". |

#### Yerleşim C — "Sayım / kutular"

Kapakta 2–3 eşit kutu ya da kart destesi. Araç testleri (K) ve kaynak videoları için.

| Örnek | Tarif |
|-------|-------|
| **C1 — Kör test** | Üç eşit dikey sütun, her birinde beyaz harf: "A", "B", "C" (araç adı ve logo yok). Sütunların sağında sarı ok ve sarı "?". Çift: "A B C → ?". Etiket: "TÜRKÇE TEST". |
| **C2 — 10 prompt** | Sol: üst üste dizilmiş 3 prompt kartı (lacivertin açık tonu, metin yerine beyaz çizgiler). Çift: "10 PROMPT → 10 İŞ". Etiket yok. |
| **C3 — Formül** | Sağda formül çubuğunun kırpılmış görüntüsü. Çift: "TARİF → FORMÜL". Etiket: "KONTROLLÜ". |

### 3.4 Kapak kontrol listesi (yayın öncesi)

- [ ] Tam bir dönüşüm çifti var; ok "önce → sonra" anlamında.
- [ ] Çiftin türü fikir cümlesinin kalıbıyla aynı (süre / çıktı / soru).
- [ ] Süre en fazla bir yerde: ya kapakta ya başlıkta; çıktı kalıbındaki videoda hiçbirinde.
- [ ] En fazla 2 metin bloğu (çift + en fazla 2 kelimelik etiket).
- [ ] Karşıtlık oranı en az 7:1; harf yüksekliği nottaki alt sınırın üstünde.
- [ ] 160 piksele küçültülmüş hâlde çift 1 saniyede okunuyor.
- [ ] Sağ alt köşe boş.
- [ ] Kapaktaki her sayı videoda kronometreyle görünüyor; kazanan ya da hakem kararı kapakta yok.
- [ ] Bir önceki kapakla aynı yerleşimde değil.

---

## 4. Hook kütüphanesi (ilk 30–35 saniye)

Her hook üç işi sırayla yapar: **(1) başlık/kapağın sözünü onaylar, (2) kanıtı veya riski gösterir, (3) videonun sonunda ne olacağını söyler.** Selamlama, kanal tanıtımı, "bugün sizlerle" yok.

### 4.1 Sonuç cümlesi kuralı

1. **Hook iki geçişte yazılır.** Çekimden önce iskelet (görev, ölçülecek şey, sondaki söz); çekimden sonra sonuç cümleleri. Aşağıdaki metinlerde `[ÇEKİMDE: …]` ile işaretli her cümle ikinci geçişte ya gerçeğe göre yazılır ya da silinir.
2. **Hata bilerek veriye konduysa videoda söylenir.** Tuzaklı veri kullanmak serbesttir; gizlemek değildir. Örnek uygulama: `docs/senaryolar/02-3-saatlik-excel-isi-10-dakikada.md`, "Kontrol ve sessiz hata" bölümü ("bu satırları veriye bilerek koydum") ve aynı bölümün, yapay zekâ tuzağı baştan yakalarsa okunacak ikinci metni.
3. **Beklenen sonuç çıkmazsa hook değişir, çekim tekrarlanmaz.** Aynı prompt'u istenen sonuç çıkana kadar yeniden çalıştırmak, sonucu uydurmakla aynı şeydir. Sonuca göre hangi cümlenin okunacağı çekimden önce karar tablosuna bağlanabilir (örnek: senaryo 01, 2.8 "Karar kuralları").
4. **İzleyici hakkında ölçülmemiş genelleme yok.** "Çoğu kişi şunu yazıyor", "herkese vasat cevap verir" ölçülmemiş iddialardır. İki güvenli biçim: birinci tekil ("benim de ilk yazdığım şuydu") ya da konuşanı içine alan birinci çoğul ("çoğumuz şunu yazıyoruz") ve hemen ardından ekranda gerçek çıktı.

### 4.2 Kalıplar

Metinler seslendirme iskeletidir; köşeli parantezler çekimde doldurulur.

#### H1 — Görev + süre (süre kalıbının varsayılanı)
**Kullanım:** G kategorisi, kronometre yarışı.
> "Bu, bir satış ekibinin aylık raporu. Ham veri burada: [SATIR SAYISI] satır. Aynı raporu geçen hafta elle hazırladım; [ELLE SÜRE] sürdü. Şimdi kronometreyi başlatıyorum ve aynı raporu yapay zekâyla hazırlıyorum. Kontrol için harcadığım süre de kronometreye dâhil. Sonda iki raporu yan yana koyup rakamları tek tek karşılaştıracağım. [ÇEKİMDE: hata çıktıysa → 'Yolda bir hata çıktı; nerede olduğunu kontrol adımında göstereceğim.' Çıkmadıysa sil.]"

#### H2 — Sonucu önce göster
**Kullanım:** Çıktısı görsel olan işler (sunum, CV, rapor).
> "Bu [N] slaytlık sunumu, kontrol dâhil [YZ SÜRE]'de hazırladım. Elle hazırladığım sürüm [ELLE SÜRE] sürmüştü. Benim yazdığım tek şey şu [N] satırlık prompt; yani yapay zekâya verdiğim talimat. Şimdi başa dönüyorum ve boş sayfadan buraya nasıl geldiğimi adım adım gösteriyorum. [ÇEKİMDE: elle düzeltilen slayt olduysa → '[N] slaytı elle düzeltmem gerekti; hangileri olduğunu ve nedenini de göstereceğim.' Olmadıysa → 'Sonda elle hazırladığımla yan yana koyacağım.']"

#### H3 — Yanlış kullanım aynası
**Kullanım:** B kategorisi; "denedim, vasat" diyen izleyici.
> "Çoğumuz ChatGPT'ye şunu yazıyoruz: 'Müşteriye teklif maili yaz.' Aldığımız cevap da bu: [ÇEKİMDE: gerçek cevabın ekranda işaretlenen kusurları]. Bu hâliyle gönderilemez. Sorunun büyük kısmı bu tek satırda. Bu teklifi önce elle yazdım: [ELLE SÜRE] sürdü. Şimdi aynı isteği [N] küçük değişiklikle yeniden yazacağım; her değişiklikten sonra cevabın nasıl değiştiğini ekranda göreceksin. Sonda üç şey var: ölçtüğüm süre, yapay zekânın bu işte yapamadığı şey ve kopyalayabileceğin prompt."

Notlar: (1) Tırnak içindeki "mail" izleyicinin kendi dilidir; anlatımın geri kalanı "e-posta" der. (2) Yapay zekâyla ölçülen süre hook'ta söylenmez, sona saklanır; böylece süre küçük de çıksa büyük de çıksa hook aynı kalır. (3) Yayın 1'de okunacak tam metin ve ikinci cümlenin ön teste göre üç sürümü senaryo 01'dedir.

#### H4 — İtirazı ilk cümlede söyle
**Kullanım:** Giriş videoları, şüpheci izleyici.
> "Yapay zekâyı denedin, vasat cevap verdi, kapattın. İlk denemede çoğu zaman vasat cevap gelir; bende de öyle olmuştu. Bu videoda hiçbir şey bilmediğini varsayıyorum. Video [N] dakika; durdurup uygulayarak izlersen toplam [UYGULAMA SÜRESİ] sürer. Sonunda kendi işinden bir görevi, kendi metninle, baştan sona yaptırmış olacaksın. [ÇEKİM GÜNÜ DOĞRULA: 'İlk adım için hesap açman gerekmiyor.']"

Notlar: (1) `[UYGULAMA SÜRESİ]`, videoyu hiç görmemiş bir deneme izleyicisinin durdurup uygulayarak bitirme süresidir; başlıktaki "30 dakika" bu ölçüme göre düzeltilir. (2) Hesap cümlesi bir ürünün o günkü davranışına dair iddiadır; çekim günü, videoda kullanılan araçta, çıkış yapılmış bir tarayıcıda denenir. Doğru değilse cümle silinir.

#### H5 — Kör test
**Kullanım:** K kategorisi, araç karşılaştırmaları.
> "Üç araca aynı beş işi verdim. İsimleri kapattım: A, B, C. İşler şunlar: şikâyet e-postasına cevap, toplantı özeti, Excel formülü, resmî dilekçe, ürün açıklaması. Puanı, testten önce yazdığım üç ölçüte göre veriyorum; ölçütler birazdan ekranda. Önce sen seç, sonra isimleri açacağım. [ÇEKİMDE: üçünün de aynı hatayı yaptığı bir iş çıktıysa → 'Bir işte üçü de aynı hatayı yaptı; onu da göstereceğim.' Çıkmadıysa sil.]"

#### H6 — Deney beyanı
**Kullanım:** Süreli deneyler (bir hafta, 30 gün).
> "Pazartesiden cumaya, işte yazdığım bütün e-postaları yapay zekâya yazdırdım. Kural şuydu: taslağı o yazar, ben en fazla bir dakika düzeltirim. Kaç e-posta yazdım, e-posta başına süre ne kadar değişti ve kaçını silip kendim yazmak zorunda kaldım; hepsini saydım. [ÇEKİMDE: kayda değer bir olay olduysa somut yaz → 'Çarşamba günü bir e-postayı (ne olduysa) yüzünden baştan yazdım.' Olmadıysa sil.] Sonda buna devam edip etmeyeceğimi söyleyeceğim."

Not: İçeriği söylenmeyen merak cümlesi ("çarşamba günü olan şeyi beklemiyordum") kullanılmaz; olay ya adıyla söylenir ya hiç söylenmez.

#### H7 — Meslek çağrısı
**Kullanım:** M serisi.
> "Muhasebeciysen ayın ilk haftasını biliyorum. [GÖRÜŞMEDEN: muhasebecinin saydığı üç iş]. Bu videoda her ay tekrar eden [N] işi alıyorum ve her birini kronometreyle yapay zekâya yaptırıyorum. Elle süreleri [KAYNAK: kendi ölçümüm / görüştüğüm muhasebecinin beyanı]; hangisi olduğu ekranda yazıyor. [ÇEKİMDE: devredilmeyen iş çıktıysa → '[N] tanesini devretmeni önermiyorum; hangisi olduğunu ve nedenini sonda söyleyeceğim.' Çıkmadıysa sil.]"

Not: "Biliyorum" cümlesi ancak o meslekten en az bir kişiyle görüşüldüyse okunur.

#### H8 — Başarısızlıkla aç
**Kullanım:** "Yapamadığı şey"i güçlü videolar; formül, hesap, mevzuat konuları.
> "Bu formülü yapay zekâ yazdı. Düzgün görünüyor, hata vermiyor ve sonucu yanlış. [ÇEKİMDE: nasıl fark edildiği, tek cümle.] Bu videoda Excel formülü yazdırmanın işe yarayan yolunu gösteriyorum; ama önce bu hatanın neden olduğunu ve [ÇEKİMDE ÖLÇ] saniyelik bir kontrolle nasıl yakalandığını görmen gerekiyor."

Not: Hook'un tamamı koşulludur; yalnızca çekimde gerçekten böyle bir hata yakalandıysa kullanılır. Hata veriye bilerek konan bir tuzaktan çıktıysa ikinci cümlenin ardından söylenir: "Bu tuzağı veriye ben koydum."

#### H9 — Sayım / envanter
**Kullanım:** Liste ve kaynak videoları.
> "Geçen ay yapay zekâya yazdığım prompt'ları saydım: [N] tane. [SAYIMDAN: sayım ne gösterdiyse, ör. '(N) tanesi aynı on kalıbın tekrarıydı.'] Bu videoda en çok kullandığım on kalıbı, her birini gerçek bir işte kullanarak gösteriyorum. Hepsi açıklamada; kopyalayıp köşeli parantezleri kendi işine göre doldurman yeterli. En çok kullandığım, [SAYIMDAN: sıra]. sırada."

Not: "Saydım" diyorsan gerçekten say (sohbet geçmişinden, bir ay); sayım tablosu dosyada durur.

#### H10 — Dış hakem
**Kullanım:** Sonucu bir uzmanın değerlendirdiği videolar.
> "Aynı kişi için iki CV hazırladım. Birini elle, birini yapay zekâyla. İkisini de, hangisinin hangisi olduğunu söylemeden bir İK uzmanına gönderdim ve tek soru sordum: hangisini görüşmeye çağırırdın? Cevabını ve gerekçesini videonun sonunda kendi sözleriyle duyacaksın."

Not: Uzman gerçek olmalı, görüşü kayıtlı/yazılı alınmalı, yayın için izni olmalı. Uzman bulunamazsa bu hook ve bu video çekilmez.

### 4.3 Seçim tablosu ve kontrol listesi

| Video türü | Birinci tercih | Yedek |
|------------|----------------|-------|
| Kronometre görevi (G kategorisi) | H1 | H2 |
| Başlangıç / doğru kullanım (B kategorisi) | H3 | H4 |
| Araç testi (K kategorisi) | H5 | H8 |
| Meslek serisi (M kategorisi) | H7 | H1 |
| Deney | H6 | H9 |
| Liste / kaynak | H9 | H3 |
| Uzman değerlendirmeli | H10 | H2 |

Hook kontrol listesi (kütüphanedeki kalıplar ve senaryo dosyalarındaki hook'lar aynı listeyle sayılır):

- [ ] İlk cümle 12 kelimeyi geçmiyor ve "merhaba" ile başlamıyor.
- [ ] İlk 10 saniyede izleyici **görevi ve ölçülecek şeyi** duydu ya da gördü: süre, hakem kararı ya da önce/sonra.
- [ ] Sonda ne göreceği söylendi (karşılaştırma, hata, kazanan, karar).
- [ ] En az bir açık döngü açıldı (bkz. 7.1) ve videoda kapanıyor.
- [ ] Hook'taki her iddia videoda ekranda kanıtlanıyor; `[ÇEKİMDE: …]` cümlelerinin hepsi ya dolduruldu ya silindi.
- [ ] İzleyici hakkında ölçülmemiş genelleme yok ("çoğu kişi", "herkes").
- [ ] Yer tutucular gerçek değerlerle doldurulmuş hâliyle sesli okunduğunda 35 saniyeyi geçmiyor (dakikada 130 kelime hızında tahmini 65–75 kelime; kendi hızını bir kez ölç).

### 4.4 Shorts açılışları ve paketi

Her uzun videodan 2–3 Shorts kesilir. Kesim akışı `03-yapim-is-akisi.md` 5.2'de, ölçümü `02-buyume-stratejisi.md` A10'da; burada yalnızca açılış ve paket kuralı var.

**Seçim:** Üç aday an fikir filtresinde (ölçüt 7) yazılır, senaryoda zaman damgasıyla işaretlenir. Bir uzun videonun üç Shorts'u üç ayrı türden seçilir: bir **tek ipucu**, bir **hata / "yapamadığı şey"**, bir **önce/sonra**. Hangi türün uzun videoya daha çok izleyici taşıdığı 02 belgesindeki format testiyle izlenir.

**Açılış kuralları:**

- İlk karede sonuç, hata ya da önce/sonra görünür; ekran kaydının "açılma" anı değil. **[Gözlem]** Shorts'ta kapağın işini ilk 1–2 saniye görür.
- Uzun videodan yalnızca görüntü alınır; **seslendirme ayrıca kaydedilir**, çünkü uzun videodaki cümleler ("az önceki cevap", "ilk dört adım") tek başına anlaşılmaz. İlk cümle en fazla 10 kelimedir, uzun videoyu görmemiş biri için anlaşılır ve görevi ya da sonucu içerir.
- Ekranın üst bandında 3–5 kelimelik sabit yazı durur (görevin adı); ses kapalı izleyen için.
- Süre yalnızca uzun videonun paketi süre taşıyorsa söylenir; çıktı kalıbındaki videoların Shorts'unda süre iddiası olmaz.
- Kapanış tek başına tamamdır (ipucu verilmiş, hata gösterilmiş olur); son cümle uzun videoya ne için gidileceğini söyler. "Devamı kanalda" diye yarım bırakılmaz.

| Kod | Kalıp | İlk kare | İlk cümle iskeleti | Kapanış |
|-----|-------|----------|--------------------|---------|
| **SH1** | Tek satır | Prompt'un eklenen satırı sarı çerçevede | "İsteğinin sonuna bu tek cümleyi ekle." | Satır 2 saniye sabit kare (ekran görüntüsü alınabilsin) + "Diğerleri uzun videoda." |
| **SH2** | Sessiz hata | İşaretli yanlış hücre / yanlış cümle | "Bu hücrede hata mesajı yok. Ama sonuç yanlış." | Kontrol yöntemi tek satır + "İşin tamamı uzun videoda." |
| **SH3** | Önce / sonra | Bölünmüş ekran: dağınık girdi ve temiz çıktı | "Bu tabloyu elle [ELLE SÜRE]'de temizledim. Aynı iş, kronometreyle." | Kronometrenin durduğu kare + "Prompt uzun videoda." |
| **SH4** | Yapamadığı şey | "Yapamadığı şey" bölüm kartı ya da hatalı çıktı | "Yapay zekâ bu işin şu kısmını yapamadı." | Neden yapamadığı tek cümle + "Yapabildiği kısım uzun videoda." |

SH2 ve SH4 yalnızca çekimde gerçekten yaşanan bir hata/sınır varsa kesilir. Shorts başlığı görev cümlesidir (tahmini 40 karakter altı), içindeki sayı ölçümle aynıdır; her Shorts'a uzun video "ilgili video" olarak bağlanır (özelliğin hesabında açık olup olmadığı Studio'da kontrol edilir).

---

## 5. Açılış sahneleri: ilk 5 saniyede ekranda ne var?

Kural: **İlk 2 saniyede hareket ve okunur tek bir şey olmalı: bir sayı, bir önce/sonra, işaretli bir hata ya da izleyicinin kendi ekranında gördüğü şeyin aynısı (tek satırlık istek, dağınık tablo).** Logo animasyonu, boş masaüstü, tarayıcı açılışı yok. Açılış müziği kullanılacaksa hook'tan sonra, en fazla 2–3 saniye.

| # | Kalıp | 0–2. saniye | 2–5. saniye | Eşleşen hook |
|---|-------|-------------|-------------|--------------|
| **S1** | **Kronometre + ham iş** | Tam ekran ham dosya (karışık Excel), yavaş kayar; sorunlu hücreler sarı çerçeveli. Üstte sarı etiket: "Elle: [ELLE SÜRE]". | Sağ üstte sarı kronometre 00:00 belirir ve çalışmaya başlar. | H1, H7 |
| **S2** | **Bitmiş çıktı** | Bitmiş sunum/rapor tam ekran, hızlı kaydırma (3 slayt); köşede "[YZ SÜRE]" etiketi. | Ekran boş sayfaya "geri sarar"; kronometre 00:00. | H2 |
| **S3** | **Bölünmüş ekran: vasat / iyi** | Sohbet kutusuna izleyicinin tanıdığı tek satır yazılır; gerçek cevap akmaya başlar (hızlandırılmış, "hızlandırıldı" notuyla). | Cevaptaki kusurlar sarıyla işaretlenir; ekran bölünür: solda gri filtreli bu cevap, sağda henüz bulanık duran son hâl, ortada sarı ok. | H3, H4 |
| **S4** | **Hata vurgusu** | Hücredeki yanlış sonuç sarı çerçeveyle işaretli olarak açılır; formül çubuğu görünür. | Yanına doğru değer belirir; ikisi arasındaki fark tek satır yazıyla gösterilir. | H8 |
| **S5** | **Gün sayacı / takvim** | Beş kutulu haftalık şerit: Pzt–Cum; altında sayaç "E-posta: [N]" sıfırdan toplam değere hızla sayar. | Kutular sırayla dolar; her kutuda o günün adedi. | H6, H9 |
| **S6** | **Kör test panosu** | Üç pencere yan yana, başlıkları "A", "B", "C"; araç adları sarı bantla kapalı. Üçünde de aynı prompt yazılı, cevaplar akıyor. | Altta boş puan tablosu belirir: "A: 0 · B: 0 · C: 0". | H5, H10 |

Teknik notlar:

- Ekran kaydını en az %125–150 yakınlaştırmayla al veya kurguda kırp; telefonda metin okunmalı.
- İlk 5 saniyede imleç gezinmesi olmasın; ne gösterilecekse hazır açık olsun.
- Kronometre grafiği tek bir şablon dosyasıdır; her videoda aynı konumda (sağ üst), aynı yazı tipinde durur.
- Ses: ilk kelime ilk karede başlar. Sessiz açılış yok.

---

## 6. Hikâye kurguları (7 iskelet)

Dakikalar 8–14 dakikalık video için tahminidir; görev uzunluğuna göre ±1 dakika oynar. Her kurguda kanalın imza öğeleri bulunur: **gerçek görev + ölçülmüş başlangıç (elle süre ya da "önce" çıktısı) → kronometre → süre/kalite karşılaştırması → "yapamadığı şey" → kopyalanabilir prompt.**

İskeletlerdeki "ilk deneme eksik çıkar", "bir hata bulunur" gibi beklentiler plan değil olasılıktır. Çekimde gerçekleşmeyen bölüm atlanır; süresi bir sonraki bölüme eklenmez, video kısalır.

### 6.1 Kronometre kuralı (bütün kurgular için tek tanım)

| Durum | Kronometre | Ekranda nasıl görünür |
|-------|------------|-----------------------|
| İzleyicinin işi yaparken gerçekten yapacağı her adım: malzemeyi bulup kopyalama, prompt yazma, cevabı bekleme, soruları cevaplama, çıktıyı uygulama, kontrol, düzeltme | **Sayar** | Sarı rakamlar, sağ üst |
| Görüntü hızlandırıldı ya da bekleme kesildi | **Saymaya devam eder**; rakamlar da hızlanır ya da ileri atlar | Yanında "hızlandırıldı" notu (ya da "×N"). Kronometre bu yüzden video süresinden hızlı ilerler |
| Yalnızca video için yapılan gösterim: bilerek yazılan kötü örnek, tek tek adımların katkısını göstermek için ayrı sohbette deneme, açıklama kartı, "yapamadığı şey" için ek deneme | **Durur** | Rakamlar gri; karede etiket: "Ayrı sohbet · süre dışı" |
| Bir sonraki sefer için bir kez yapılan yatırım (ör. prompt'u şablona çevirme) | **Durmuştur; ayrı ölçülür** | Süre dökümünün altında ayrı satır: "Şablon (bir kez): [ŞABLON SÜRE]" |
| Çalışma bitti | **Durur ve büyür** | Tam ekran sarı sayı; altında süre dökümü (prompt · bekleme · uygulama · kontrol · düzeltme) |

Uygulama kuralları:

- **Süreli akış tek, kesintisiz bir kayıttır**; `[YZ SÜRE]` yalnızca ondan okunur. Kötü örnekler ve katkı gösterimleri ayrı kayıtlardır. Kötü deneme süreli sohbete yazılmaz: hem süreyi şişirir hem sonraki cevapları etkiler.
- Süreli kayıttan önce prova yapılmaz; prova süreyi olduğundan kısa gösterir. Prova gerekiyorsa farklı bir kopya üzerinde yapılır ve açıklamada belirtilir.
- **Sıra etkisi söylenir:** elle yol önce yapıldığı için yapay zekâlı turda malzeme tanıdıktır. Bu, karşılaştırma bölümünde bir cümleyle söylenir ve açıklamaya yazılır.
- Kronometrenin neyi saydığı videonun ilk dakikasında izleyiciye bildirilir: ya tek cümleyle sesli ya da kronometrenin yanında sabit bir notla ("Süre tek seferlik kayıttan").

### KG1 — Kronometre Yarışı

**Kullanım:** G kategorisinin varsayılanı. Tek görev, tek çıktı.

| Zaman | Bölüm | Ekranda / anlatımda |
|-------|-------|---------------------|
| 0:00–0:30 | Hook | H1 veya H2. Görev, elle süre, sondaki karşılaştırma sözü. |
| 0:30–1:15 | Görevin tanımı | Ham veri, istenen çıktı, "iyi" sayılma ölçütü (3 madde: doğru rakam, okunur biçim, yöneticiye gönderilebilir). Kronometre kuralı. Gizlilik notu: örnek veri, gerçek şirket değil. |
| 1:15–2:00 | Elle yol | Elle yapılışın hızlandırılmış görüntüsü; sürenin nereye gittiği üç kalemde. |
| 2:00–4:30 | 1. tur: ilk prompt | Prompt yazılır, cevap gelir, uygulanır. Çıktı ölçütlerle karşılaştırılır. `[ÇEKİMDE: eksik varsa eksik gösterilir; yoksa doğrudan kontrole geçilir]` |
| 4:30–7:00 | 2. tur: kontrol ve düzeltme | Kontrol adımı ekranda gerçekten yapılır (satır sayısı, en küçük/en büyük değer, iki yoldan toplam). Düzeltme gerekiyorsa prompt'a eklenen satırlar tek tek gösterilir. Bu bölümde bir desen kırıcı (bkz. 7.3). |
| 7:00–8:30 | 3. tur: son hâl | Çıktı tamamlanır. Kronometre durur: büyük sarı sayı. |
| 8:30–10:00 | Karşılaştırma | Elle yapılan ve yapay zekâyla yapılan yan yana. Süre dökümü + 3 kalite ölçütü tablo hâlinde. Elle yapılanın daha iyi olduğu bir nokta da söylenir. |
| 10:00–11:15 | Yapamadığı şey | Çekimde karşılaşılan sınır, nasıl fark edildi, nasıl önlenir. |
| 11:15–12:00 | Prompt + köprü | Son prompt ekranda tam hâliyle; açıklamada kopyalanabilir. Sonraki videoya köprü cümlesi, bitiş ekranı. |

**Tam senaryo örneği:** `docs/senaryolar/02-3-saatlik-excel-isi-10-dakikada.md`. Senaryoda turlar, işin doğasına göre adımlara bölünmüştür (temizle → kontrol → birleştir → özetle → yorumla); iskelet aynıdır.

### KG2 — Önce / Sonra (+ hakem)

**Kullanım:** Sürenin değil kalitenin öne çıktığı işler: CV, e-posta, sunum metni, ürün açıklaması.

| Zaman | Bölüm | Ekranda / anlatımda |
|-------|-------|---------------------|
| 0:00–0:30 | Hook | H2 veya H10. İki sürüm 2 saniye yan yana gösterilir; hangisinin hangisi olduğu ve hakem kararı sona saklanır. |
| 0:30–1:30 | "Önce" | Başlangıç malzemesi tam ekran. Üç somut kusur sarıyla işaretlenir. |
| 1:30–2:15 | Ölçüt | "İyi" neye göre? Hakemin (ya da çekimden önce yazılmış listenin) 3 ölçütü ekranda sabit kalır (köşede küçük kontrol listesi). |
| 2:15–5:00 | Dönüşüm 1 | Birinci kusurun düzeltilmesi: prompt → çıktı → ölçüt işaretlenir. Kronometre çalışır. |
| 5:00–7:30 | Dönüşüm 2–3 | Kalan kusurlar. Her biri bitince köşedeki listede bir kutu dolar. |
| 7:30–9:00 | Yan yana | Önce/sonra bölünmüş ekran, kaydırmalı karşılaştırma. Toplam süre. |
| 9:00–10:30 | Hakem / dış göz | Uzmanın gerçek yorumu (yazılı ya da sesli, izinli). Uzman yoksa ölçütlere göre öz değerlendirme yapılır ve "bunu ben değerlendirdim, tarafsız değilim" denir. |
| 10:30–11:30 | Yapamadığı şey | Çıktıda doğrulanması gereken kısım (ör. CV'ye girdide olmayan bir yetkinlik eklenmiş mi) ve kontrol yöntemi. `[ÇEKİMDE: bulunan gerçek örnek]` |
| 11:30–12:15 | Prompt + köprü | Prompt, sonraki video. |

### KG3 — Hata Listesi (7 alışkanlık / 10 prompt)

**Kullanım:** B kategorisi, liste ve kaynak videoları. Liste videolarında izleyici sıkılınca atlamaya başlar; bu yüzden sıralama ve tempo bu kurgunun kendisidir. Aşağıdaki dakikalar 7 maddelik sürümün, yani senaryo 01'in dakikalarıdır (toplam tahmini 12:15).

| Zaman | Bölüm | Ekranda / anlatımda |
|-------|-------|---------------------|
| 0:00–0:35 | Hook | H3 veya H9. Tek satırlık istek, gerçek cevabı, elle süre, sondaki üç söz. |
| 0:35–1:05 | İlk cevap ve sabit görev | Kötü cevabın kusurları işaretlenir. Bütün maddelerde kullanılacak tek görev tanıtılır (ör. yeni bir müşteriye, beş kalem ürün için teklif e-postası). Kurallar seslendirilmez; ekran notuna yazılır ("Örnek veri · firma ve kişi kurgusal"). |
| 1:05–2:25 | Madde 1 | Hata adı → düzeltme → çıktı farkı. En uzun işlenen maddelerden biri: bağlam ve malzeme burada verilir. |
| 2:25–3:30 | Madde 2 | Aynı şablon. |
| 3:30–4:30 | Madde 3 | Aynı şablon; ara vaat burada ya da 6. maddenin sonunda (bkz. 7.2). |
| 4:30–5:40 | Madde 4 | Süreli kaydın ilk gerçek etkileşimi (ör. yapay zekânın sorduğu sorular). Kronometre vurgusu: `[ARA SÜRE]`. |
| 5:40–6:10 | Desen kırıcı | Ekran kaydından çıkılan tek sahne (kısa masa üstü çekim). Özet tekrarı değil, yeni bir kanıt getirir; listenin kalanını çerçeveler ("geriye üç adım kaldı, üçü de cevap geldikten sonrasıyla ilgili"). |
| 6:10–7:15 | Madde 5 | Cevabı düzelttirme. |
| 7:15–8:35 | Madde 6 | Kontrolle ilgili madde; bir sayı ekranda elle doğrulanır. |
| 8:35–9:35 | Madde 7 | İzleyicinin yanında götüreceği madde (şablon). Süreli kaydın dışında, ayrı ölçülür. |
| 9:35–10:05 | Süre ve kalite karşılaştırması | Kronometrenin son değeri ve süre dökümü. Baştaki kötü cevap, elle yazılan ve son çıktı yan yana; elle yazılanın üstün olduğu bir nokta da söylenir. |
| 10:05–11:20 | Yapamadığı şey | Bütün maddelere rağmen düzelmeyen, bu çekimde görülmüş şeyler. Bölümün sonunda yorum sorusu. |
| 11:20–12:15 | Kopyalanabilir prompt + köprü | Bütün maddeler tek prompt'ta; sonraki video. Vedalaşma yok. |

Her maddenin bir **hata adı** ve bir **çözüm adı** vardır ("Soru sordurmamak → Önce soru sordur"); seslendirme, ekrandaki kutu, bölüm listesi ve Shorts yalnızca bu adları kullanır. Sayaç ("3/7") ekranın köşesinde sabit durur.

Sıralama kuralı: maddeler **üst üste biniyorsa** (her madde aynı prompt'a bir parça ekliyorsa; senaryo 01) sıra işin mantık sırasıdır. Maddeler **bağımsızsa** (10 prompt): ekranda en görünür farkı yaratan madde başa, en çok kullanılan madde sona yakına, en zayıf madde ortaya ve en kısa hâliyle. Hangisinin "en güçlü" olduğu çekimden sonra belirlenir.

**10 maddelik sürüm:** Madde başına 45–60 saniye (toplam tahmini 7:30–10:00); hook, sabit bağlam, özet ve "yapamadığı şey" ile video tahmini 10:30–13:00. Ara vaatler 3., 6. ve 9. maddede verilir; desen kırıcı 5. ile 6. madde arasına girer. Bir madde 60 saniyeyi aşıyorsa ya ikiye bölünür ya listeden çıkar.

**Tam senaryo örneği:** `docs/senaryolar/01-chatgptyi-yanlis-kullaniyorsun.md` (7 maddelik sürüm). Aynı iskeletin üç işli sürümü: `docs/senaryolar/03-prompt-yazmanin-tek-formulu.md` (yedek video; bkz. Bölüm 9).

### KG4 — Süreli Deney (bir hafta / 30 gün)

**Kullanım:** F5 başlıklı videolar. Çekim günlere yayılır; her gün 2–3 dakikalık ham kayıt + günlük not tutulur.

Deneyden önce: (1) kurallar ve sayılacak metrikler yazılır, deney sırasında değiştirilmez; (2) "süre değişti" diyebilmek için **karşılaştırma tabanı** ölçülür: deneyden önceki hafta aynı tür işte elle ortalama süre (`[ELLE SÜRE]`, en az `[N]` örnek); (3) günlük sayım tablosu açılır.

**Bir haftalık sürüm:**

| Zaman | Bölüm | Ekranda / anlatımda |
|-------|-------|---------------------|
| 0:00–0:30 | Hook | H6. Kural, süre, sayılacak şeyler. |
| 0:30–1:30 | Kurallar | 3 kural ekranda (ör. "taslağı o yazar", "en fazla 1 dk düzeltme", "göndermeden önce okurum"). Ölçülecek 3 metrik: adet, e-posta başına süre, elle yeniden yazılan sayısı. Karşılaştırma tabanı. |
| 1:30–3:00 | Gün 1 | Kurulum ve o gün ne olduysa. Günün sayacı. |
| 3:00–4:30 | Gün 2 | Kurulumda değişen bir şey olduysa (ör. üslup satırı eklendi) o değişiklik ve etkisi. |
| 4:30–6:30 | En çok şey öğreten gün (hangisi çıkarsa) | Deneyin en öğretici olayı: bir başarısızlık ya da beklenmedik kolaylık. Kurguda ortaya yerleştirilir; takvimdeki günü ekranda yazar. Böyle bir gün çıkmadıysa bu bölüm iki sıradan güne bölünür. |
| 6:30–8:00 | Kalan günler | Hızlandırılmış; yalnızca yeni bir şey öğreten anlar. |
| 8:00–9:30 | Sayım | Tablo: gün gün adet, süre, elle yeniden yazılan. Toplamlar `[ÇEKİMDE ÖLÇ]`; tabanla karşılaştırma. |
| 9:30–10:45 | Yapamadığı şey | Elle yazmak zorunda kalınan e-postalar ve ortak özellikleri. `[ÇEKİMDE: hiç çıkmadıysa bu söylenir ve bölüm, en çok düzeltme gereken türe ayrılır]` |
| 10:45–11:30 | Karar | "Devam ediyor muyum? Hangi tür işte evet, hangisinde hayır." |
| 11:30–12:15 | Prompt + köprü | Deney sonunda oluşan son prompt; sonraki video. |

**30 günlük sürüm:** Günler haftalara toplanır; tek tek gün yalnızca bir kural değiştiğinde ya da sayım tablosunda sıçrama olduğunda gösterilir.

| Zaman | Bölüm | Ekranda / anlatımda |
|-------|-------|---------------------|
| 0:00–0:30 | Hook | H6'nın 30 günlük uyarlaması: kural, süre, sayılacak şeyler, sondaki karar. |
| 0:30–1:30 | Kurallar ve taban | 3 kural, 3 metrik, deneyden önceki haftanın tabanı. 30 kutulu takvim şeridi ekranda. |
| 1:30–3:15 | Hafta 1: kurulum | İlk prompt, ilk günlerin sayımı. Haftanın tek öğretici anı. Hafta sonu sayaç. |
| 3:15–5:00 | Hafta 2: ilk kural değişikliği | Neyi neden değiştirdim; değişiklikten önceki ve sonraki sayım yan yana. `[ÇEKİMDE: değişiklik olmadıysa haftanın en çok düzeltme gereken işi]` |
| 5:00–6:45 | Hafta 3: alışkanlık mı, yük mü? | Kullanımın düştüğü ya da arttığı işler; hangi işte bıraktım. Desen kırıcı: sayım tablosundaki en belirgin sıçramaya yakınlaştırma. |
| 6:45–8:15 | Hafta 4: oturmuş hâl | Son haftanın tipik bir günü baştan sona, gerçek hızda 60–90 saniye. |
| 8:15–9:45 | Sayım | 30 günün tablosu haftalık toplamlarla; tabanla karşılaştırma. Bütün değerler `[ÇEKİMDE ÖLÇ]`. |
| 9:45–11:00 | Yapamadığı şey | 30 gün boyunca devredilemeyen iş türleri ve ortak özellikleri. |
| 11:00–11:45 | Karar | Hangi işlerde kalıcı, hangilerinde bıraktım; bir ay sonra neyi ölçeceğim. |
| 11:45–12:30 | Prompt + köprü | 30 günün sonunda kalan prompt'lar; sonraki video. |

30 günlük deney ölçüt 8'den 0 alır; kanalın ilk 10 videosunda yoktur. Çekimi sürerken haftalık videolar aksamamalıdır; aksıyorsa deney uzatılır, yayın değil.

### KG5 — Meslek Vaka Çalışması

**Kullanım:** M serisi ve İ kategorisi. Bir meslek, o mesleğin tekrar eden 3–5 işi.

| Zaman | Bölüm | Ekranda / anlatımda |
|-------|-------|---------------------|
| 0:00–0:30 | Hook | H7. Mesleğin adı ilk 3 saniyede. |
| 0:30–1:15 | İş haritası | Mesleğin tekrar eden [N] işi ekranda liste; her birinin yanında elle süre ve kaynağı: "ölçüm" (kendin yaptın) ya da "beyan" (o meslekten biri söyledi). İkisi ekranda farklı etiketle durur. |
| 1:15–3:15 | İş 1 | Mini kronometre yarışı: görev → prompt → çıktı → kontrol → süre. |
| 3:15–5:00 | İş 2 | Aynı şablon. |
| 5:00–6:45 | İş 3 | + ara vaat: sondaki "devretme kararı" bölümü. |
| 6:45–8:15 | İş 4 | Kısa tutulur. |
| 8:15–10:00 | Devretme kararı | Her iş için üçlü karar: devredilir / kontrolle devredilir / devredilmez; gerekçesiyle (mevzuat, sorumluluk, doğruluk). `[ÇEKİMDE: devredilmeyen iş çıktıysa bu bölüm ona ayrılır ve "yapamadığı şey" bölümü olur]` |
| 10:00–11:00 | Toplam tablo | [N] iş, elle toplam / yeni toplam. Kontrol süresi dâhil; "beyan" süreler ayrı satırda. |
| 11:00–11:45 | Gizlilik ve sorumluluk | Müşteri verisi, kişisel veri, meslek sorumluluğu: neyi yüklemezsin. |
| 11:45–12:30 | Prompt paketi + köprü | [N] prompt açıklamada; "sıradaki meslek" için yorum sorusu. |

Not: Meslek videolarında mevzuat/vergi/hukuk bilgisi yapay zekâ çıktısı olarak **doğrulanmadan** verilmez; video "taslak üretir, sorumluluk sende" çizgisinde kalır. Bu kurgu için tam senaryo henüz yazılmadı.

### KG6 — Kör Test (araç karşılaştırması)

**Kullanım:** K kategorisi. 5 görev × 3 araç. Zaman hesabı: görev başına 1:45, yani araç başına tahmini 20 saniye ekran süresi. Bu yüzden cevapların tamamı okunmaz; her cevabın yalnızca **belirleyici pasajı** (1–2 cümle) sarıyla işaretlenir, tam cevaplar açıklamadaki dosyada durur.

| Zaman | Bölüm | Ekranda / anlatımda |
|-------|-------|---------------------|
| 0:00–0:30 | Hook | H5. Beş iş, kapalı isimler, sondaki açılış. |
| 0:30–1:00 | Kurallar ve ölçütler | Testten önce yazılmış 3 ölçüt (ör. doğru bilgi, gönderilebilir Türkçe, istenen biçim); her biri 0–2 puan. Test tarihi ve kullanılan planlar ekranda. İkinci puanlayıcı tanıtılır. |
| 1:00–2:45 | Görev 1 | **Prompt** 10 sn → **üç cevap yan yana** 60 sn (her cevapta belirleyici pasaj işaretlenir) → **puan** 20 sn (iki puanlayıcının puanı) → **tablo** 15 sn güncellenir. |
| 2:45–4:30 | Görev 2 | Aynı şablon. |
| 4:30–6:15 | Görev 3 | Aynı şablon. Ardından yorum sorusu: "Şu ana kadar hangisini seçtin: A, B, C?" |
| 6:15–8:00 | Görev 4 | Aynı şablon. Desen kırıcı: iki puanlayıcının en çok ayrıştığı cevap tam ekran. `[ÇEKİMDE: ayrışma olmadıysa en yakın farkla kazanılan görev]` |
| 8:00–9:45 | Görev 5 | Aynı şablon. Tablo son hâlini alır. |
| 9:45–10:30 | İsimler açılır | Sarı bantlar kalkar; son tablo araç adlarıyla. |
| 10:30–11:15 | Yapamadığı şey | `[ÇEKİMDE: üçünün de zorlandığı ya da aynı hatayı yaptığı görev; yoksa en düşük toplam puanlı görev ve nedeni]` |
| 11:15–12:00 | Hangi iş için hangisi | Görev türüne göre karar tablosu. Sınır cümlesi: "Bu sonuç bu tarihte, bu beş işte, bu planlarla geçerli." |
| 12:00–12:30 | Prompt + köprü | Beş prompt ve tam cevaplar açıklamada; sonraki video. |

Sığma kuralı: ham kurgu 14 dakikayı aşıyorsa görev sayısı 4'e iner (puan farkını en az etkileyen görev çıkar ve çıkarıldığı videoda söylenir). Görev başına süre 1:45'in altına indirilmez; cevaplar okunamaz hâle gelir.

Dürüstlük kuralları: ölçütler ve görevler testten önce yazılıp tarihli bir dosyada saklanır; her araç aynı prompt'la, yeni sohbette, bir kez çalıştırılır; puanlayıcılar araç adını görmez; araçların sürüm/plan bilgisi açıklamaya yazılır, seslendirmeye girmez.

### KG7 — Adım Adım Başlangıç (uygulamalı)

**Kullanım:** Giriş videoları. İzleyici videoyu durdurarak uygular; başlıktaki süre izleyicinin **uygulama süresidir**, video süresi değil.

| Zaman | Bölüm | Ekranda / anlatımda |
|-------|-------|---------------------|
| 0:00–0:30 | Hook | H4. Video süresi ve uygulama süresi ayrı ayrı söylenir. |
| 0:30–1:15 | Ne lazım | Hangi araç, hesap gerekip gerekmediği `[ÇEKİM GÜNÜ DOĞRULA]`, neyi yapıştırmayacağın (kişisel veri, gizli şirket bilgisi). Köşede "Adım 0/5". |
| 1:15–2:45 | Adım 1: İlk soru | Bilerek tek satırlık bir soru; gelen cevap gösterilir. "Kapattığın yer burası." **Alıştırma kartı** (10 sn): "Durdur. Kendi işinden bir soruyu tek satırla yaz." |
| 2:45–4:30 | Adım 2: Kime, ne biçimde | Aynı soruya okuyan kişi ve çıktı biçimi eklenir; cevap değişir. Alıştırma kartı. |
| 4:30–6:15 | Adım 3: Malzeme ver | Kendi notunu/metnini yapıştırma; "bunun dışında bilgi ekleme" satırı. Alıştırma kartı. |
| 6:15–8:00 | Adım 4: Düzelttir | İlk cevabı silmeden geri bildirim verme; iki turda değişim. Alıştırma kartı. |
| 8:00–10:00 | Adım 5: Kendi işinden bir görev | İzleyici kendi görevini seçer; ekranda örnek olarak bir e-posta baştan sona yapılır. Alıştırma kartı: "Durdur. Kendi görevini dört adımla yaz." |
| 10:00–10:45 | Önce / sonra | Adım 1'deki ilk cevap ile Adım 5'teki son cevap yan yana. |
| 10:45–11:45 | Yapamadığı şey | Yeni başlayanın bilmesi gereken üç sınır: akıcı ama yanlış bilgi, güncel/şirkete özel bilgi, gizlilik. Her biri ekranda bir örnekle. |
| 11:45–12:30 | Prompt + köprü | Dört adımın boş şablonu; sonraki video. |

Alıştırma kartı sabit bir grafiktir: lacivert zemin, sarı "Durdur ve yaz", altında tek cümlelik görev ve tahmini süre. Kartların toplam tahmini süresi ile video süresinin toplamı `[UYGULAMA SÜRESİ]` olur; bu değer videoyu görmemiş bir deneme izleyicisiyle ölçülür ve başlıktaki süre ona göre yazılır.

### Kurgu seçim tablosu

| Videonun özü | Kurgu |
|--------------|-------|
| Tek görev, süre farkı | KG1 |
| Kalite farkı, çıktı görsel, hakem var | KG2 |
| Birden çok alışkanlık / prompt | KG3 |
| Zamana yayılan kullanım | KG4 |
| Bir mesleğin birden çok işi | KG5 |
| Birden çok aracın aynı işlerde karşılaştırması | KG6 |
| Sıfırdan başlayan izleyicinin uygulayarak izlediği video | KG7 |

---

## 7. İzleyici tutma araçları

**[Resmî]** Studio'daki izleyici tutma grafiği videonun hangi anlarında izleyicinin kaldığını, geri sardığını veya ayrıldığını gösterir. Aşağıdaki araçların işe yarayıp yaramadığı bu grafikten okunur. Araçların kendisi **[Gözlem]** niteliğindedir; hiçbiri YouTube'un garanti ettiği bir mekanizma değildir.

### 7.1 Açık döngüler

Açık döngü: cevabı sonra verilecek, belirli bir soru. Kural: **her döngü videoda kapanır ve kapanış, açılıştaki söze birebir karşılık gelir.**

İki türü vardır. **Yapısal döngü** ekranda görünür ve izleyicinin aklında tutmasını gerektirmez: kronometrenin son değeri, "3/7" sayacı, ilerleme çubuğu, puan tablosu, açılışta bulanık gösterilen son çıktı. **Sözlü döngü** bir cümleyle açılır ve izleyici onu hatırlamak zorundadır.

| Döngü | Tür | Ne zaman açılır | Ne zaman kapanır | Cümle / görüntü |
|-------|-----|-----------------|------------------|-----------------|
| **Süre döngüsü** | Yapısal | Hook | Karşılaştırma bölümü | "Elle [ELLE SÜRE] sürdü." Kronometre 00:00'da bekler. |
| **Son çıktı döngüsü** | Yapısal | Hook (bulanık kare) | Karşılaştırma bölümü | Bölünmüş ekranın sağında bulanık duran son hâl; karşılaştırmada netleşir. |
| **Karşılaştırma döngüsü** | Sözlü | Hook | Karşılaştırma bölümü | "Sonda iki raporu yan yana koyup rakamları tek tek karşılaştıracağım." |
| **Hata döngüsü** | Sözlü | Hook ya da görev tanımı | Kontrol adımı / "yapamadığı şey" | `[ÇEKİMDE: hata çıktıysa]` "Yolda bir toplam yanlış çıktı. Nerede olduğunu kontrol adımında göstereceğim." |
| **Sıra döngüsü** (liste) | Sözlü | Madde 3 civarı ya da sondan bir önceki madde | İlgili madde | "Son madde, diğer altısını bir sonraki sefer tek adıma indiriyor." |
| **Karar döngüsü** (deney) | Sözlü | Kurallar bölümü | Karar bölümü | "Hafta sonunda buna devam edip etmeyeceğime karar vereceğim." |

Sınır: **aynı anda en fazla 2 sözlü döngü.** Üçüncüsü açılacaksa önce biri kapanır. Yapısal döngüler bu sınıra girmez. Hata döngüsü yalnızca gerçek bir hata varsa açılır; izleyiciye "bakalım benden önce bulacak mısın" diye oyun kurulmaz.

### 7.2 Ara vaatler

Ara vaat: önümüzdeki 1–2 dakikada izleyicinin ne kazanacağını söyleyen tek cümle. Bölüm geçişlerinde ve işin sıkıcı kısmından hemen önce kullanılır.

- Kurulumdan önce: "Kurulum kısa; ardından ilk sonucu göreceksin."
- İkinci tura geçerken: "Şu an elimizdeki rapor yöneticiye gönderilemez. `[ÇEKİMDE: eklenen satır sayısı]` satır ekleyeceğim; değişimi ekranda göreceksin."
- Liste ortasında: "Geriye üç adım kaldı. Üçü de cevap geldikten sonrasıyla ilgili."
- Karşılaştırmadan önce: "Kronometre durdu. Şimdi asıl soru: hızlı olan, doğru da mı?"

Kural: ara vaat somut bir çıktı, kontrol ya da süre içerir ve çekimde gerçekleşmiş bir şeye dayanır. "Birazdan çok ilginç bir şey göstereceğim" ara vaat değildir.

### 7.3 Desen kırıcılar

Desen kırıcı: ekranın veya anlatımın alışılmış akışını bozan değişiklik. Amaç dikkat çekmek değil, **yeni bir bilgi türüne geçildiğini işaretlemek**.

| Kırıcı | Ne zaman | Örnek |
|--------|----------|-------|
| **Yakınlaştırma** | Çıktıda bakılması gereken tek hücre/cümle varken | Formül çubuğuna %200 yakınlaş; "Burası." |
| **Kronometre vurgusu** | Bölüm sonlarında | Kronometre 2 saniyeliğine ekranın ortasına büyür: "[ARA SÜRE]. Elle bu noktada hâlâ veriyi temizliyordum." (İkinci cümle yalnızca elle kayıtta gerçekten öyleyse.) |
| **Başarısız deneme** | Videonun ortası (tahmini %40–55) | "Bu işe yaramadı. Neden yaramadığını göstereyim." Kronometre durur. |
| **Bölünmüş ekran** | Karşılaştırma anları | Sol: önce, sağ: sonra; kaydırma çubuğu. |
| **Tam ekran metin kartı** | Bölüm başlıkları, kural cümleleri | Lacivert zemin, sarı tek cümle: "Tahmin etme; belirsiz diye işaretle." |
| **Ekran dışı kısa sahne** | Liste videolarının ortası | Üstten masa çekimi, tahmini 30 sn, yüz yok (senaryo 01, 5:40–6:10). Müzik kesilir. |
| **Elle yapılışın hızlandırılmış görüntüsü** | Yapay zekâ cevabı beklenirken | Sağ alt köşede küçük pencere: aynı işin elle yapılışı hızlandırılmış. |
| **Ses değişimi** | Uzun ekran kaydı bölümlerinde, hata anında | Müzik kısa süre kesilir; yalnızca seslendirme. |

Kural: aynı kırıcı art arda iki kez kullanılmaz. Süs amaçlı geçiş efekti, ses efekti yağmuru, "meme" görseli kullanılmaz.

### 7.4 Tempo kuralları

Sayılar başlangıç varsayımıdır (tahmini); kendi tutma grafiğine göre ayarla.

- **Bekleme süresi kesilir, kronometre kesilmez.** Yapay zekânın cevap yazışı hızlandırılır veya atlanır; kronometrenin bu sırada nasıl davrandığı 6.1'de tanımlıdır.
- **Ekranda 20–30 saniyeden uzun hiçbir şey değişmeden durmaz** (yakınlaştırma, vurgu kutusu, kırpma veya kart).
- **Bir bölüm, bir fikir.** Bir bölümde ikinci fikir başlıyorsa bölüm ikiye ayrılır.
- **Cümle uzunluğu:** Seslendirmede cümle başına tahmini 15 kelime sınırı. Yan cümle zinciri yazılmaz.
- **Prompt okunmaz, gösterilir.** Uzun prompt sesli baştan sona okunmaz; ekranda görünür, anlatım yalnızca kritik 1–2 satırı söyler. Tamamı açıklamada. İzleyicinin prompt'u okuması için bırakılan sessiz ekran süresi senaryoda ayrıca yazılır.
- **Tıklama ve menü gezintisi kesilir.** "Dosya, yükle, seç, aç" adımları tek bir kesmeyle geçilir; yalnızca ilk kez gösterilen adım gerçek hızda kalır.
- **Bölümler işaretlenir.** Açıklamaya zaman damgalı bölümler yazılır. **[Resmî]** YouTube, açıklamadaki zaman damgalarından video bölümleri oluşturur (ilk damga 0:00 olmalı; güncel koşullar için yardım sayfasına bak). Bu, atlayan izleyicinin videodan çıkmak yerine ilgili bölüme gitmesini sağlar.

### 7.5 "Sıkılma noktası" kontrolü

**Çekimden önce (senaryo üzerinde, 10 dk):**

1. Senaryoyu sesli oku, süre tut.
2. Her paragrafın yanına şu üç kelimeden birini yaz: **yeni** (yeni bilgi), **kanıt** (ekranda sonuç), **geçiş** (bağlama/açıklama).
3. Art arda iki **geçiş** varsa biri silinir veya tek cümleye iner.
4. 90 saniye boyunca hiç **kanıt** yoksa araya bir çıktı gösterimi konur.
5. "Bu paragrafı silsem izleyici bir şey kaybeder mi?" Cevap hayırsa silinir.

**Kurgudan sonra (ham kurgu üzerinde):**

1. Videoyu 1,5× hızda, gürültülü bir ortamda, telefonda izle.
2. Telefona uzanmak veya ileri sarmak istediğin her anın zaman damgasını yaz.
3. Her damga için tek karar: **kes**, **kısalt** veya **desen kırıcı ekle**.

**Yayından sonra (48 saat ve 7. gün):**

Tanımlar (tahmini; ilk 10 videodan sonra kanalın kendi medyanlarıyla sayısallaştırılır):

- **Giriş kaybı:** Tutma grafiğinin 0:30'daki değeri. Her videoda aynı noktadan okunur ve performans kaydına yazılır.
- **Belirgin düşüş:** Grafikte yaklaşık 10 saniyelik bir aralıkta eğimin, öncesindeki ve sonrasındaki bölüme göre gözle görülür dikleştiği nokta. Video başına **en çok 3** tanesi işlenir; en dik olandan başlanır.
- **Belirgin yükseliş:** Eğrinin yukarı döndüğü nokta (izleyici geri sarmış ya da bölüme atlamıştır).

Adımlar:

1. **Bu videoda** hook'un hangi cümlesinde düşüşün başladığını bul (zaman damgasını senaryo metniyle eşleştir). Sonraki hook'ta o cümle türünü kullanma ya da yerini değiştir.
2. Her belirgin düşüş için o saniyede ekranda ne olduğunu ve senaryoda paragrafın etiketini (yeni / kanıt / geçiş) yaz.
3. Her belirgin yükseliş için de aynısını yaz. Bunlar sonraki videoda öne çekilecek öğelerdir.
4. Bulguları tek satır hâlinde "öğrenilenler" kaydına ekle (`docs/sablonlar/performans-kaydi.md`). Bir örüntü üç videoda tekrar etmeden kural hâline getirilmez. Sonraki senaryo bu kayıt okunduktan sonra yazılır.

---

## 8. Harekete geçirici çağrılar (CTA)

Tek kural: **video başına en fazla 3 sözlü CTA vardır: prompt dosyası, yorum sorusu, sonraki video. Abone çağrısı her zaman yalnızca görseldir (alt bant ve bitiş ekranındaki düğme).** Her CTA izleyiciye ne kazanacağını söyler; "destek olmak için" gerekçesi kullanılmaz. Ana CTA sonraki videodur ve videonun son sesli cümlesidir.

### 8.1 Abone (görsel)

- **Nereye:** İlk somut sonuç gösterildikten hemen sonra (KG1'de 2. turun sonu, KG3'te 2. maddenin sonu) 5–7 saniyelik alt bant; ayrıca bitiş ekranındaki abone düğmesi. Hook'ta ve ilk dakikada yok.
- **Alt bant metni:** Kanalın abone gerekçesi, tek satır: "Her hafta bir iş, kronometreyle." Ekran akışı durmaz, seslendirme çağrıya değinmez.
- **Sözlü hâli (istisna):** Yalnızca **yorum sorusu kullanılmayan** videoda, yorum sorusunun yerine ve bir sonraki somut görevle birlikte söylenir. Böylece sözlü CTA sayısı yine 3'ü geçmez.
  - "Gelecek hafta aynı testi sunum hazırlama için yapıyorum; abone olursan Abonelikler sekmende görürsün."
  - Meslek serisinde: "Bu seri her ay başka bir meslekle devam ediyor; abone olursan yayınlandığında Abonelikler sekmende görürsün."
- **Söz verilmeyen şey:** Aboneliğin, videonun ana sayfada ya da bildirimde çıkmasını sağlayacağı. **[Gözlem]** Abone olmak videonun izleyiciye önerilmesini garanti etmez; izleyiciye tutulabilecek tek söz, videonun Abonelikler sekmesinde listeleneceğidir.

### 8.2 Sonraki video (ana CTA, sözlü)

- **Nereye:** Prompt gösterildikten sonra, videonun son sesli cümlesi olarak; cümle biterken bitiş ekranı açıktır. Vedalaşma cümlesi ("görüşürüz", "izlediğiniz için teşekkürler") yok; izleyici bunu duyduğu an kapatır.
- **Kural:** Önerilen video, bu videonun bıraktığı açık soruya cevap verir. Bitiş ekranında tek video öne çıkar. Hedef video henüz yayınlanmadıysa bitiş ekranına yayınlanmış en ilgili video konur ve hedef yayınlanınca güncellenir; hangisinin geçici olduğu paket kartında yazar (Bölüm 9).
- **[Resmî]** Bitiş ekranı videonun son 5–20 saniyesine eklenir (güncel koşul için 02 belgesi B3'teki kaynağa bak); son sahneyi bu süreyi karşılayacak şekilde kurgula.
- **Örnekler:**
  - "Bugün malzeme küçüktü: beş satır fiyat. Gerçek Excel dosyaları böyle olmuyor. Gelecek hafta dağınık bir satış dökümünü aynı kronometreyle deniyoruz."
  - "Bugün tek bir araç kullandım. Aynı Türkçe işleri üç ayrı araca verdiğim video ekranda."
  - "Burada formülü yapay zekâ yazdı. Uçtan uca bir raporda aynı kontrolü nasıl yaptığım şu videoda."

### 8.3 Yorum sorusu (sözlü)

- **Nereye:** "Yapamadığı şey" bölümünün sonunda, izleyicinin söyleyecek bir şeyi olduğu an (senaryo 01, 10:05–11:20). Soru alt bantta yazılı olarak da görünür. Kör testte soru daha erken, isimler açılmadan önce sorulur. Yorum sorusu videonun son cümlesi yapılmaz; son cümle sonraki videodur.
- **Kural:** Cevabı tek satır olan, belirli bir soru. Cevaplar sonraki videoların fikir filtresine girer; bu izleyiciye açıkça söylenir. Aynı soru sabitlenmiş yorumda da durur.
- **Örnekler:**
  - "İşinde en çok vaktini alan yazı işi hangisi? Yoruma yaz; sıradaki videoları o cevaplara bakarak seçeceğim."
  - "Kör testte hangisini seçtin: A, B, C? İsimleri açmadan önce yaz."
  - "Bu prompt'u kendi verinle denediysen ve çalışmadıysa, ne oldu yaz. Çalışmayan örnekleri ayrı bir videoda toplayacağım."
- İlk saatlerde gelen yorumlara cevap ver.

### 8.4 Prompt dosyası ve e-posta listesi (sözlü, tek cümle)

- **Nereye:** Sözlü olarak yalnızca bir kez: prompt ekranda tam hâliyle göründüğü an. Yazılı olarak üç yerde: açıklamanın ilk satırlarında, sabitlenmiş yorumda, prompt kartının üst/alt satırında ("Açıklamada kopyalanabilir hâli var").
- **Kural:** Prompt'un kendisi her zaman açıklamada ücretsiz ve e-posta istemeden durur. E-posta karşılığı verilen şey **fazlası**dır: bütün videoların prompt'larının tek dosyada toplanmış, güncellenen hâli. Videodaki vaat ("kopyalanabilir prompt") e-posta duvarının arkasına konmaz. E-posta listesi daveti yazılı kalır; sözlü cümle yalnızca prompt'un nerede olduğunu söyler.
- **Örnekler:**
  - (sözlü, prompt göründüğünde) "Şu an ekranda. Açıklamada da kopyalanabilir hâli var."
  - (yazılı, açıklama ve sabitlenmiş yorum) "Kanaldaki bütün prompt'lar tek dosyada ve her videoyla güncelleniyor: [bağlantı]. E-posta adresinle alırsın; haftada bir e-postadan fazlası gelmez."
- **İstisna:** Kaynak videosunda (Yayın 10) ana CTA prompt dosyasıdır; e-posta daveti orada sözlü de söylenir ve yorum sorusu kullanılmaz.
- Hukuki not: e-posta toplarken açık rıza ve aydınlatma metni gerekir (KVKK ve ticari elektronik ileti kuralları). Formu yayınlamadan önce güncel yükümlülükleri kontrol et; bu belge hukuki tavsiye değildir. Kurulum ayrıntısı 02 belgesi B7'de.

### 8.5 CTA yerleşim özeti

| Zaman | CTA | Sözlü / görsel | Rol |
|-------|-----|----------------|-----|
| İlk somut sonuçtan sonra | Abone alt bandı | Görsel | Yan |
| "Yapamadığı şey"in sonunda | Yorum sorusu | Sözlü (1) + alt bant + sabitlenmiş yorum | Yan |
| Prompt tam hâliyle göründüğünde | "Açıklamada kopyalanabilir hâli var" | Sözlü (2) + kart üstünde yazılı | Yan (bilgi) |
| Son sesli cümle, bitiş ekranı açılırken | Sonraki video | Sözlü (3) + bitiş ekranı kartı | **Ana** |
| Bitiş ekranı | Abone düğmesi | Görsel | Yan |
| Açıklama + sabitlenmiş yorum | Prompt dosyası (e-posta) | Yazılı | Yan |

### 8.6 Yapılmayacaklar

- Videonun ilk 60 saniyesinde herhangi bir şey istemek.
- "Beğenmeyi ve zile basmayı unutmayın" kalıbı; gerekçesiz toplu istek.
- "Abone olmazsan kaçırırsın", "son şans", "yakında kaldırıyorum" gibi sahte aciliyet.
- "Abone olursan ana sayfana düşer" gibi, YouTube adına tutulamayacak söz.
- Prompt'u yalnızca e-posta karşılığı vermek (videonun vaadini bozar).
- Tartışma kışkırtan yorum sorusu ("Sence yapay zekâ işimizi alacak mı?"); kanalın konusu iş, kehanet değil.
- Bitiş ekranında ikiden fazla seçenek sunmak.
- Videonun sonunda özet okumak ("bu videoda şunları gördük..."); izleyiciye çıkış işareti verir. Kapanış bir teslimatla (prompt) yapılır.

---

## 9. İlk 10 video için paket kartları

Sıra, kanalın yayın sırasıdır; parantez içindeki numara fikir havuzundaki numara, kart başlığı fikir havuzundaki çalışma adıdır. Yayın başlığı kartın "Başlıklar" satırından seçilir.

**Tam senaryosu yazılmış videolar:** Yayın 1 → `docs/senaryolar/01-chatgptyi-yanlis-kullaniyorsun.md`; Yayın 2 → `docs/senaryolar/02-3-saatlik-excel-isi-10-dakikada.md`. Bu iki videoda okunacak metnin tek kaynağı senaryo dosyasıdır; kart hook metnini kopyalamaz, senaryoya atıf verir. Kart ile senaryo arasında fark doğarsa senaryo geçerlidir ve kart aynı gün ona göre güncellenir. Diğer sekiz videonun tam senaryosu henüz yazılmadı.

**Yedek video:** `docs/senaryolar/03-prompt-yazmanin-tek-formulu.md` (dört parçalı prompt formülü; B kategorisi, KG3'ün üç işli sürümü) ilk 10 listesinin dışındadır ve yeri şöyle belirlenir:

- **Stok:** Çekilip hazır bekler. Yayın 3'ten sonraki herhangi bir hafta üretim aksarsa o hafta yayınlanır. Yayın 3 haftasına konmaz (Yayın 2'nin kapanışı o hafta için araç karşılaştırması sözü verir) ve Yayın 1'den önce yayınlanmaz (köprü cümlesi ona dayanır).
- **Aksama olmazsa:** Yayın 9 ile Yayın 10 arasında yayınlanır; ilk tur 11 videoya çıkar, Yayın 9 kaydırılmaz. Kapanışı Yayın 10'a bağlanır; daha erken yayınlanırsa köprü cümlesi ve bitiş ekranı Yayın 1'e döner (senaryo dosyasında yedek metin yazılı).
- **Kapak:** Araya girdiği iki kapakla aynı yerleşimde olmaz (3.1).

**Kapak sırası** (art arda aynı yerleşim yok): B · A · C · B · A · C · A · B · A · C.

Kartlardaki bütün süreler ve adetler yer tutucudur. "Neden çeker" satırlarında **Varsayım** diye işaretlenen cümleler ölçülmemiştir; yanındaki adımla yayından önce yoklanır.

### Yayın 1 — (1) ChatGPT'yi Yanlış Kullanıyorsun: Sonucu Değiştiren 7 Alışkanlık

| Alan | İçerik |
|------|--------|
| **Fikir cümlesi** | Müşteriye teklif yazan biri, tek satırlık "teklif maili yaz" isteğinin verdiği vasat cevabı yedi değişiklikle bugün gönderilebilir bir teklif e-postasına çeviriyor; fark ilk ve son cevabın yan yana gösterilmesiyle ortaya çıkıyor. (Çıktı kalıbı.) |
| **Başlıklar** | Senaryo 01, "Başlık seçenekleri": A) ChatGPT'yi Yanlış Kullanıyorsun: Sonucu Değiştiren 7 Alışkanlık (F2; varsayılan) · B) ChatGPT Neden Vasat Cevap Veriyor? 7 Düzeltme · C) Aynı Soru, 7 Küçük Değişiklik: ChatGPT'den İşe Yarar Cevap Almak (ön testte tek satırlık istek "yanlış kullanım" iddiasını taşıyacak kadar kötü sonuç vermezse). Hiçbiri süre vaat etmez. |
| **Kapak** | Yerleşim B (B1): sol gri "VASAT" + tek satırlık sohbet kutusu; sağ sarı çerçeveli "İŞE YARAR" + yapılandırılmış prompt; ortada sarı ok. Süre kapakta yok. Ayrıntı: senaryo 01, "Kapak tarifi". |
| **Hook** | H3 — bkz. senaryo 01, 0:00–0:35. İkinci cümle ön teste göre seçilir (senaryo 01, 2.8 kural 1). Metin burada tekrar edilmez. |
| **Açılış** | S3 (bölünmüş ekran: vasat / iyi): tek satır yazılır, gerçek cevap gelir, 0:12'de ekran bölünür; sağda son e-posta bulanık durur. |
| **Kurgu** | KG3 — Hata Listesi; yedi maddenin hepsi aynı teklif e-postası üzerinde (yeni müşteri, beş kalem ürün). Elle süre hook'ta söylenir; yapay zekâyla ölçülen süre sonda açıklanır. Süre kalıbı Yayın 2'ye saklanır. |
| **Neden çeker** | İdeal izleyicinin yaşadığı şeyi ("denedim, vasat") başlıkta adlandırıyor ve suçu izleyiciye değil alışkanlığa yüklüyor. **Varsayım:** "ChatGPT nasıl kullanılır" türü sorgular Türkçede aranıyor. Yoklama: 2.1 adım 2. |
| **Dikkati nasıl canlı tutar** | Tek görev yedi kez iyileşiyor; her maddede ekrandaki cevap değişiyor ve köşede "3/7" sayacı ilerliyor; 5:40'ta ekran dışı kısa sahne. |
| **Sona kadar nasıl izletir** | Son madde diğer altısını bir sonraki sefer tek adıma indiriyor (6. maddenin sonunda söylenir). Hook'ta bulanık gösterilen son e-posta ve ölçülen süre ancak karşılaştırma bölümünde (9:35) açılıyor; ardından "yapamadığı şey" geliyor. |
| **CTA ve bitiş ekranı** | Sözlü: yorum sorusu, "yapamadığı şey"in sonunda ("İşinde en çok vaktini alan yazı işi hangisi?") → "açıklamada kopyalanabilir hâli var" (özet prompt göründüğünde) → son cümle: Yayın 2 (dağınık satış dökümü, aynı kronometreyle). Sesli abone çağrısı ve vedalaşma yok. Bitiş ekranı: Yayın 2; yayınlanmadıysa yalnızca abone düğmesi, yayınlanınca eklenir. |
| **Shorts** | Senaryo 01, Bölüm 5: (1) "Yazmadan önce bu cümleyi ekle" — SH1; (2) "'Emin misin?' diye sorma" — tek ipucu (kontrol isteği); (3) "'Teklif maili yaz' neden işe yaramıyor?" — masa çekimi. Üçünün seslendirmesi ayrı kaydedilir; süre iddiası yok. |

### Yayın 2 — (4) 3 Saatlik Excel İşini 10 Dakikada Bitirmek

| Alan | İçerik |
|------|--------|
| **Fikir cümlesi** | Ofis çalışanı, dağınık bir aylık satış dökümünü dosyayı yüklemeden temizleyip özetini [ELLE SÜRE] yerine [YZ SÜRE]de çıkarıyor. (Süre kalıbı.) |
| **Başlıklar** | Senaryo 02, "Başlık seçenekleri". Kapak süre çiftini taşıdığı için kapakla birlikte kullanılacak başlık: B) Dağınık Satış Dökümünden Yönetici Özetine: Kronometreyle Denedim. A) [ELLE SÜRE]'lik Excel İşini [YZ SÜRE]'de Bitirmek (F1) yalnızca süresiz kapakla ("DAĞINIK → ÖZET") eşleşir ve başlık/kapak testinin ikinci paketidir. Arama varyantı: C) Excel'de Veri Temizleme ve Tablo Birleştirme: Dosyayı Yapay Zekâya Yüklemeden. |
| **Kapak** | Yerleşim A (A1): süre çifti "[ELLE SÜRE] → [YZ SÜRE]", solda dağınık Excel parçası, sağda temiz özet tablo, etiket "DOSYAYI YÜKLEMEDEN". Kanalın imza kapağı ilk kez burada görünür. Ayrıntı: senaryo 02, "Kapak tarifi". |
| **Hook** | H1 — bkz. senaryo 02, 0:00–0:30. Metin burada tekrar edilmez. Hatayla ilgili cümle senaryodaki koşula bağlıdır: tuzak veriye bilerek konmuştur ve kontrol bölümünde söylenir. |
| **Açılış** | S1 (kronometre + ham iş): kirli tablo, sarı çerçeveler, "Elle: [ELLE SÜRE]". |
| **Kurgu** | KG1 — Kronometre Yarışı; senaryoda adımlara bölünmüş hâli. |
| **Neden çeker** | Dağınık Excel dökümü ideal izleyicinin tanıdığı bir yük; "dosyayı yüklemeden" ifadesi "şirket dosyamı oraya veremem" itirazına kapakta cevap veriyor. **Varsayım:** bu itiraz yaygın. Yoklama: Yayın 1'in yorumlarında gizlilik sorusu geliyor mu. |
| **Dikkati nasıl canlı tutar** | Kronometre ve ilerleme çubuğu sürekli ekranda; her adım kontrolle bitiyor; ortada kontrol adımı ve tuzağın açıklanması. |
| **Sona kadar nasıl izletir** | Kronometrenin son değeri, "dosyayı yüklemeden nasıl?" sorusu ve eşleşmeyen satırların ne olacağı; sonuncusu "yapamadığı şey"de kapanır. |
| **CTA ve bitiş ekranı** | Sözlü: yorum sorusu ("Excel'de en çok vaktini alan iş hangisi?"; Yayın 6'nın örnekleri oradan seçilir) → "şablon açıklamada" → son cümle: Yayın 3 (aynı Türkçe işler üç araçta). Bitiş ekranı: Yayın 3; yayınlanana kadar Yayın 1. |
| **Shorts** | Senaryo 02, Bölüm 5: (1) sessiz tarih hatası — SH2; (2) prompt'taki "Excel Türkçe" satırı — SH1 (koşullu); (3) iki yoldan toplam — tek ipucu. |

### Yayın 3 — (3) ChatGPT / Gemini / Claude: Türkçede Hangisi Daha İyi?

| Alan | İçerik |
|------|--------|
| **Fikir cümlesi** | Türkçe iş yazan biri, beş gerçek işte üç aracın cevabını isim görmeden puanlıyor; fark, önceden yazılmış ölçütler ve ikinci bir kör puanlayıcıyla gösteriliyor. (Çıktı kalıbı, hakemli.) |
| **Başlıklar** | 1) ChatGPT, Gemini, Claude: Türkçe Kör Test, 5 Gerçek İş (F3) · 2) Aynı 5 İşi Üç Yapay Zekâya Verdim, İsimleri Kapattım · 3) Türkçe İş Yazışmasında Hangi Yapay Zekâ? İsimleri Kapatıp Denedim |
| **Kapak** | Yerleşim C (C1): üç sütun "A", "B", "C"; soru çifti "A B C → ?"; etiket "TÜRKÇE TEST". Kazanan ve logolar gösterilmez. |
| **Hook** | H5; beş iş listesi ikinci cümlede. Koşullu son cümle yalnızca gerçekten olduysa. |
| **Açılış** | S6 (kör test panosu). |
| **Kurgu** | KG6 — Kör Test: 5 görev × 3 araç, görev başına 1:45; 14 dakikayı aşarsa 4 görev. |
| **Neden çeker** | "Hangisini kullanmalıyım" sorusuna kapalı isimlerle, kanalın kendi lehine yönlendiremeyeceği bir düzenekle cevap veriyor. **Varsayım:** bu soru Türkçede aranıyor ve mevcut videolar Türkçe iş görevleriyle test etmiyor. Yoklama: yayından önce YouTube aramasında "chatgpt gemini claude karşılaştırma" ve "türkçe yapay zeka hangisi" ile ilk 10 sonuca bak; kaçı Türkçe görevle, kaçı kör test. |
| **Dikkati nasıl canlı tutar** | İzleyici her görevde kendi tahminini yapıyor; puan tablosu her görevden sonra güncelleniyor. |
| **Sona kadar nasıl izletir** | İsimler ancak beşinci görevden sonra açılıyor (9:45); ardından "hangi iş için hangisi" tablosu geliyor. |
| **CTA ve bitiş ekranı** | Sözlü: yorum sorusu erken, 3. görevden sonra ("Hangisini seçtin: A, B, C?") → "beş prompt ve tam cevaplar açıklamada" → son cümle: Yayın 4 ("Aracı seçtin; ilk gerçek işini nasıl yaptıracağın şu videoda"). Bitiş ekranı: Yayın 4; yayınlanana kadar Yayın 1. |
| **Shorts** | (1) Tek görevde üç cevabın belirleyici pasajları, isimler kapalı; son karede isimler açılır — önce/sonra türü. (2) Kullanılan beş prompt'tan biri — SH1. (3) `[ÇEKİMDE: üçünün de zorlandığı görev çıktıysa]` — SH4. |
| **Notlar** | Test tarihi, kullanılan plan (ücretsiz/ücretli) ve model adı ekranda ve açıklamada yazılır; sonuç "bu tarihte, bu beş işte" diye sınırlandırılır. Ölçütler testten önce yazılır ve videoda gösterilir. İkinci puanlayıcı araç adlarını görmez. Hiçbir sonuç çekimden önce yazılmaz. |

### Yayın 4 — (6) Hiç Kullanmamış Biri İçin Yapay Zekâ: 30 Dakikada Başlangıç

| Alan | İçerik |
|------|--------|
| **Fikir cümlesi** | Hiç kullanmamış biri, ilk vasat cevabı kendi işinden bir görevde kullanılabilir cevaba çeviriyor; fark aynı görevin ilk ve son cevabıyla gösteriliyor. (Çıktı kalıbı.) |
| **Başlıklar** | 1) Hiç Kullanmamış Biri İçin Yapay Zekâ: İlk Gerçek İşin [UYGULAMA SÜRESİ]'de (F7; çalışma değeri "30 Dakikada") · 2) Yapay Zekâya Sıfırdan Başlamak: İlk Gün Yapılacak 5 Şey · 3) Yapay Zekâyı Denedin, Bıraktın mı? Baştan, Doğru Sırayla |
| **Kapak** | Yerleşim B (B3): sol boş sohbet kutusu + "SIFIRDAN", sağ bitmiş kısa e-posta + "İLK İŞ"; etiket "5 ADIM". Uygulama süresi yalnızca başlıkta; "0 → 30 dk" biçimi kullanılmaz (bkz. 3.1). |
| **Hook** | H4. Video süresi ile uygulama süresi ayrı söylenir; hesap cümlesi çekim günü doğrulanır, doğru değilse silinir. |
| **Açılış** | S3; sağ tarafta bitmiş görev, altında "Adım 5'in sonunda" etiketi. |
| **Kurgu** | KG7 — Adım Adım Başlangıç: 5 adım, her adımın sonunda alıştırma kartı. Video tahmini 12–13 dk; "30 dakika" izleyicinin uygulama süresidir ve bir deneme izleyicisiyle ölçülür. |
| **Neden çeker** | Geride kalma kaygısına abartısız bir çıkış sunuyor: tanıtım turu değil, bitince elde bir iş var. **Varsayım:** "yapay zeka nasıl kullanılır" ve "hiç kullanmamış" ifadeleri aranıyor. Yoklama: otomatik tamamlama (1.2, ölçüt 2). |
| **Dikkati nasıl canlı tutar** | Her adım "durdur ve yaz" kartıyla bitiyor; köşede "Adım 2/5" ilerleme çubuğu duruyor. |
| **Sona kadar nasıl izletir** | Beşinci adım izleyicinin kendi işinden bir görev; önceki dört adım o göreve hazırlık olarak sunuluyor. Sonda ilk ve son cevap yan yana. |
| **CTA ve bitiş ekranı** | Sözlü: yorum sorusu ("Beşinci adımda hangi görevi seçtin?") → "boş şablon açıklamada" → son cümle: Yayın 1 ("İlk işini yaptırdın; sonucu değiştiren yedi alışkanlık şu videoda"). Bitiş ekranı: Yayın 1. |
| **Shorts** | (1) Adım 2'deki tek satır (kime, ne biçimde) — SH1. (2) Adım 1 cevabı ile Adım 5 cevabı — SH3'ün süresiz sürümü. (3) "Akıcı ama yanlış" sınırının örneği — SH4 `[ÇEKİMDE: örnek çıktıysa]`. |

### Yayın 5 — (11) 10 Dakikada Sunum

| Alan | İçerik |
|------|--------|
| **Fikir cümlesi** | Ofis çalışanı, aylık özet tablodan yönetim sunumunu [ELLE SÜRE] yerine [YZ SÜRE]de hazırlıyor. (Süre kalıbı.) |
| **Başlıklar** | Kapak süre çiftini taşıdığı için kapakla birlikte: 1) Yönetim Sunumu: Boş Sayfadan Son Slayta, Kronometreyle Denedim. Süresiz kapakla ("BOŞ SAYFA → [N] SLAYT") eşleşen test paketi: 2) Kontrol Dâhil [YZ SÜRE]'de Yönetim Sunumu: Boş Sayfadan Son Slayta (F12). 3) Sunum Yarına Yetişecek mi? Boş Sayfadan Son Slayta, Kronometreyle |
| **Kapak** | Yerleşim A (A2): süre çifti "[ELLE SÜRE] → [YZ SÜRE]", sağda üç slayt küçük resmi, etiket "SUNUM". |
| **Hook** | H2. Slayt ve satır sayıları çekimden; "elle düzeltilen slayt" cümlesi koşullu. |
| **Açılış** | S2 (bitmiş çıktı, sonra geri sarma). |
| **Kurgu** | KG1; görev Yayın 2'deki özet tablonun sunumu (iki video aynı örnek şirketi kullanır). Üç tur: iskelet → metin → görsel düzen. |
| **Neden çeker** | Bitmiş sunumu ilk saniyede gösteriyor. **Varsayım:** "boş sayfa" kaygısı ve "sunum hazırlama" araması ideal izleyicide yaygın. Yoklama: 2.1 adım 2. |
| **Dikkati nasıl canlı tutar** | Üç aşama ayrı ayrı kronometreleniyor; her aşama sonunda slaytlar gözle görülür değişiyor. |
| **Sona kadar nasıl izletir** | Elle hazırlanan sunumla yan yana karşılaştırma ve `[ÇEKİMDE: elle düzeltilen slaytlar varsa]` bunların "yapamadığı şey"de gösterilmesi. |
| **CTA ve bitiş ekranı** | Sözlü: yorum sorusu ("Sunumlarında en çok vakit alan kısım hangisi: içerik mi, tasarım mı?") → "prompt açıklamada" → son cümle: Yayın 2 ("Bu sunumdaki rakamların geldiği özeti nasıl çıkardığım şu videoda"). Bitiş ekranı: Yayın 2. |
| **Shorts** | (1) Boş sayfadan iskelete geçiş, kronometreli — SH3. (2) İskelet prompt'unun tek kritik satırı — SH1. (3) `[ÇEKİMDE: elle düzeltilen slayt varsa]` — SH4. |

### Yayın 6 — (21) Excel Formülünü Yapay Zekâya Yazdırmak

| Alan | İçerik |
|------|--------|
| **Fikir cümlesi** | Excel kullanan biri, hatırlamadığı formülü tarif ederek yazdırıyor ve yanlış sonucu kontrol adımıyla yakalıyor; fark yanlış ve doğru sonucun yan yana gösterilmesiyle ortaya çıkıyor. (Çıktı kalıbı.) |
| **Başlıklar** | 1) Excel Formülünü Yapay Zekâya Yazdırmak ve Doğru mu Diye Kontrol Etmek · 2) Excel Formülünü Yapay Zekâya Yazdırmak: Çalışan [N], Çalışmayan [N] Örnek (F8; sayılar çekimden sonra) · 3) DÜŞEYARA'yı Hatırlamıyorum: Yapay Zekâya Formül Yazdırmanın Kontrollü Yolu |
| **Kapak** | Yerleşim C (C3): çıktı çifti "TARİF → FORMÜL", sağda formül çubuğu kırpması, etiket "KONTROLLÜ". |
| **Hook** | H8 — yalnızca çekimde gerçek bir hata yakalandıysa; yakalanmadıysa H1'in formül uyarlaması (görev: [N] formül ihtiyacı; ölçülecek şey: formül başına süre ve kontrol). |
| **Açılış** | S4 (hata vurgusu) ya da, H1 kullanılırsa, S1. |
| **Kurgu** | KG3: 5–6 formül ihtiyacı, kolaydan zora; her biri "ne istiyorum → nasıl tarif ettim → formül → kontrol". |
| **Neden çeker** | Formülü hatırlamak yerine tarif etmek ve sonucu kontrol etmek, "körü körüne güvenme" kaygısına cevap veriyor. **Varsayım:** formül hatırlayamama yaygın ve "düşeyara nasıl yapılır" türü sorgular aranıyor. Yoklama: otomatik tamamlama + Yayın 2'nin yorum sorusuna gelen cevaplar (örnekler oradan seçilir). |
| **Dikkati nasıl canlı tutar** | Her formül kendi başına 60–90 saniyelik kapalı bir mini görev; izleyici işine yarayanı beklerken diğerlerini de izliyor. |
| **Sona kadar nasıl izletir** | Son bölüm, bütün formüller için kullanılan ortak kontrol yöntemi; hook'ta söz verilen şey bu. |
| **CTA ve bitiş ekranı** | Sözlü: yorum sorusu ("Senin yazdıramadığın formül hangisi?") → "formül prompt'u açıklamada" → son cümle: Yayın 2 ("Tek tek formülleri gördük; uçtan uca bir işte aynı kontrolü nasıl yaptığım şu videoda"). Bitiş ekranı: Yayın 2. |
| **Shorts** | (1) Prompt'taki "Excel Türkçe, ayırıcı noktalı virgül" satırı — SH1 (Yayın 2'de kullanıldıysa burada başka bir satır seçilir). (2) `[ÇEKİMDE: yanlış sonuç veren formül çıktıysa]` — SH2. (3) Ortak kontrol yöntemi, tek başına — tek ipucu. |
| **Notlar** | Türkçe Excel'de işlev adları (DÜŞEYARA, EĞER) ve ayraç (noktalı virgül) farkı çekimde test edilir; yapay zekânın bunu doğru yapıp yapmadığı `[ÇEKİMDE ÖLÇ]`. Senaryo 02 ile ayrım: orada uçtan uca iş akışı, burada tek tek formül türleri. |

### Yayın 7 — (27) Muhasebeciler İçin Yapay Zekâ

| Alan | İçerik |
|------|--------|
| **Fikir cümlesi** | Muhasebeci, her ay tekrar eden [N] işi [ELLE SÜRE] yerine [YZ SÜRE]de bitiriyor; hangisinin devredilmeyeceği gerekçesiyle gösteriliyor. (Süre kalıbı.) |
| **Başlıklar** | 1) Muhasebeciler İçin Yapay Zekâ: Her Ay Tekrarlanan [N] İş (F4; "Biri Devredilmez" eki çekimde öyle çıktıysa) · 2) Muhasebe Bürosunda Yapay Zekâ: Hangi İş Devredilir, Hangisi Devredilmez · 3) Muhasebecinin Ay Başı: [N] İşi Kronometreyle Yapay Zekâya Yaptırdım |
| **Kapak** | Yerleşim A (A3): beyaz "MUHASEBECİ", süre çifti "[ELLE SÜRE] → [YZ SÜRE]" ([N] işin toplamı), sağda ekstre görünümlü tablo. Elle süreler ölçüm değil "beyan" ise süre çifti kullanılmaz; çıktı çifti "[N] İŞ → DEVRET?" kullanılır. |
| **Hook** | H7. İş örnekleri görüşmeden; süre kaynağı (ölçüm / beyan) ekranda. |
| **Açılış** | S1; ham iş yerine iş haritası listesi ve yanında elle süreler. |
| **Kurgu** | KG5 — Meslek Vaka Çalışması. Tam senaryo henüz yazılmadı. |
| **Neden çeker** | Mesleğin adı başlıkta; izleyici "bu benim için" kararını hemen veriyor. **Varsayım:** genel yapay zekâ videolarında muhasebeye özel iş örneği az. Yoklama: YouTube aramasında "muhasebeciler için yapay zeka" ile ilk 10 sonuca bak; kaçı işi ekranda baştan sona yapıyor. |
| **Dikkati nasıl canlı tutar** | Art arda mini yarışlar; her işin sonunda toplam süre tablosuna bir satır ekleniyor. |
| **Sona kadar nasıl izletir** | Devretme kararı bölümü (8:15) ve ardından gizlilik/sorumluluk; her iş için "devredilir mi" sorusu baştan açık bırakılıyor. |
| **CTA ve bitiş ekranı** | Sözlü: yorum sorusu ("Sıradaki meslek hangisi olsun? Mesleğini ve en çok vakit alan işini yaz.") → "[N] prompt açıklamada" → son cümle: Yayın 2 ("Ekstre gibi dağınık tabloları temizlemenin tamamı şu videoda"). Bitiş ekranı: Yayın 2. |
| **Shorts** | (1) En büyük süre farkı çıkan iş, kronometreli — SH3. (2) `[ÇEKİMDE: devredilmeyen iş çıktıysa]` nedeni — SH4. (3) Gizlilik kuralı: neyi yapıştırmazsın — tek ipucu. |
| **Notlar** | İşler, çekimden önce en az bir muhasebeciyle konuşularak belirlenir; hook'taki örnekler o görüşmeye göre yazılır. Mevzuat bilgisi yapay zekâ çıktısı olarak verilmez. Müşteri verisi kullanılmaz; örnek veri hazırlanır. Görüşme çekimden iki hafta önce ayarlanır (1.3). |

### Yayın 8 — (8) Yapay Zekâyla CV Hazırladım, İK Uzmanına Gösterdim

| Alan | İçerik |
|------|--------|
| **Fikir cümlesi** | İş arayan biri, aynı kişinin CV'sini elle ve yapay zekâyla iki sürümde hazırlıyor; farkı, hangisinin hangisi olduğunu bilmeyen bir İK uzmanı gösteriyor. (Çıktı kalıbı, hakemli.) |
| **Başlıklar** | 1) Yapay Zekâyla CV Hazırladım, İK Uzmanına Gösterdim · 2) Elle Yazılmış CV mi, Yapay Zekâ CV'si mi? İK Uzmanı Hangisini Seçti (F6) · 3) CV'mi Yapay Zekâya Yazdırdım: İK Uzmanı İkisini Ayırt Edebildi mi? |
| **Kapak** | Yerleşim B (B2): iki CV, üstlerinde "A" ve "B"; soru çifti "A B → ?"; etiket "İK SEÇTİ". Uzmanın kararı kapakta yok. |
| **Hook** | H10. |
| **Açılış** | S6'nın iki pencereli sürümü: iki CV yan yana, üstlerinde "A" ve "B". |
| **Kurgu** | KG2 — Önce/Sonra + hakem. |
| **Neden çeker** | Dış hakem sonucu belirsiz kılıyor; kanal kendi lehine karar veremiyor ve izleyici bunu biliyor. **Varsayım:** "cv hazırlama" aranan bir sorgu. Yoklama: 2.1 adım 2. |
| **Dikkati nasıl canlı tutar** | Uzmanın değerlendirme ölçütleri baştan gösteriliyor; her dönüşüm adımında "bu ölçütü geçer mi" sorusu açık kalıyor. |
| **Sona kadar nasıl izletir** | Uzmanın kararı ve gerekçesi yalnızca 9:00'daki hakem bölümünde. |
| **CTA ve bitiş ekranı** | Sözlü: yorum sorusu, hakem bölümünden önce ("Sen hangisini seçerdin: A mı, B mi?") → "CV prompt'u açıklamada" → son cümle: Yayın 9 ("CV'yi gönderirken yazacağın e-postayı da yazdırdım; bir haftalık e-posta deneyi şu videoda"). Bitiş ekranı: Yayın 9; yayınlanana kadar Yayın 1. |
| **Shorts** | (1) İki CV yan yana, "hangisini çağırırdın?"; son karede uzmanın kararı — önce/sonra türü. (2) Uzmanın tek cümlelik ölçütü (izinli alıntı) — tek ipucu. (3) `[ÇEKİMDE: yapay zekâ girdide olmayan bir bilgi eklediyse]` — SH4. |
| **Notlar** | Uzman gerçek kişi olmalı; yorumu yazılı/sesli kayıtla ve yayın izniyle alınır. Üçüncü başlık bir soru olarak kalır; cevabı başlığa yazılmaz. Uzman bulunamazsa video ertelenir, kurgu uydurulmaz. CV'deki kişi kurgusal veya kendi CV'n olur. Uzman çekimden iki hafta önce ayarlanır (1.3). |

### Yayın 9 — (13) Bir Hafta Bütün E-postalarımı Yapay Zekâya Yazdırdım

| Alan | İçerik |
|------|--------|
| **Fikir cümlesi** | Ofis çalışanı, bir haftalık iş e-postalarını e-posta başına [ELLE SÜRE] yerine [YZ SÜRE]de yazıyor; kaçını kendisinin yazmak zorunda kaldığı sayılıyor. (Süre kalıbı.) |
| **Başlıklar** | 1) Bir Hafta Bütün E-postalarımı Yapay Zekâya Yazdırdım · 2) Bir Hafta E-postalarımı Yapay Zekâya Yazdırdım: [N] E-posta, [N] Tanesini Kendim Yazdım (F5; sayılar deneyden sonra) · 3) İş E-postalarını Yapay Zekâya Yazdırmak: Bir Haftalık Deney ve Sayımı |
| **Kapak** | Yerleşim A: süre çifti "[ELLE SÜRE] → [YZ SÜRE]" (e-posta başına ortalama), sağda kısa, temiz bir e-posta kırpması, etiket "5 GÜN". Taban ölçülmediyse süre çifti kullanılmaz; çıktı çifti "[N] E-POSTA → [N] ELLE" kullanılır. |
| **Hook** | H6. Olay cümlesi yalnızca gerçek ve adıyla söylenebilir bir olay varsa. |
| **Açılış** | S5 (gün sayacı). |
| **Kurgu** | KG4 — Süreli Deney, bir haftalık sürüm. |
| **Neden çeker** | E-posta ideal izleyicinin gündelik işi; deney, izleyicinin kendi yapmaya üşendiği sayımı onun yerine yapıyor. |
| **Dikkati nasıl canlı tutar** | Gün gün ilerleyen sayaç; prompt'ta değişiklik olan günler; ortada deneyin en çok şey öğreten günü (hangisi çıkarsa). |
| **Sona kadar nasıl izletir** | Hook'ta söz verilen sayım tablosu (8:00) ve "devam ediyor muyum" kararı (10:45). |
| **CTA ve bitiş ekranı** | Sözlü: yorum sorusu ("Yapay zekâya yazdırmayacağın e-posta türü hangisi?") → "haftanın sonunda kalan prompt açıklamada" → son cümle: Yayın 10 ("Bu prompt, her gün kullandığım on prompt'tan biri; hepsi şu videoda"). Bitiş ekranı: Yayın 10; yayınlanana kadar Yayın 1. |
| **Shorts** | (1) Üslup satırı eklenmeden ve eklendikten sonra aynı e-posta — SH1. (2) Dağınık taslak ve gönderilen hâl — SH3. (3) `[ÇEKİMDE: elle yazılmak zorunda kalınan e-posta olduysa]` türü ve nedeni — SH4. |
| **Notlar** | Deneyden önceki hafta aynı tür e-postalarda elle ortalama süre ölçülür (taban). Gerçek yazışmalar gösterilmez; alıcı adları, şirket bilgileri kapatılır veya e-postalar eşdeğer kurgusal örneklerle yeniden yazılır ve bu videoda söylenir. Günlük sayım tablosu deney boyunca tutulur. Deney, yayın haftasından önceki hafta yapılır. |

### Yayın 10 — (10) Her Gün Kullandığım 10 Prompt

| Alan | İçerik |
|------|--------|
| **Fikir cümlesi** | Ofis çalışanı, on tekrar eden işi on hazır prompt'la yaptırıyor; her prompt'ta gerçek bir işten önce/sonra çıktı gösteriliyor. (Çıktı kalıbı.) |
| **Başlıklar** | 1) Her Gün Kullandığım 10 Prompt: Her Biri Gerçek Bir İşte (F9) · 2) İşte En Çok Kullandığım 10 Prompt (Saydım) · 3) 10 Prompt, 10 Gerçek İş: Dosyası Açıklamada |
| **Kapak** | Yerleşim C (C2): çıktı çifti "10 PROMPT → 10 İŞ", solda üst üste üç prompt kartı. Etiket yok. |
| **Hook** | H9. Sayım gerçekten yapılır; adetler ve sıra sayımdan gelir. |
| **Açılış** | S5'in ızgara sürümü: 10 kartlık ızgara, kartlar sırayla açılır; altında sayaç "[N] prompt sayıldı". |
| **Kurgu** | KG3, 10 maddelik sürüm: madde başına 45–60 sn, ara vaatler 3., 6. ve 9. maddede, önceki 9 videodan gerçek kullanım kesitleriyle. |
| **Neden çeker** | Kaydedilip geri dönülen kaynak videosu; önceki dokuz videonun prompt'larını tek yerde topluyor ve yeni izleyiciye kanalın giriş kapısı oluyor. |
| **Dikkati nasıl canlı tutar** | Her prompt farklı bir işte (e-posta, Excel, sunum, toplantı notu) gösteriliyor; ekran her dakika başka bir uygulamaya geçiyor; köşede "4/10" sayacı. |
| **Sona kadar nasıl izletir** | En çok kullanılan prompt'un sırası hook'ta söyleniyor (sayımdan); finalde on prompt'un tek sayfalık özeti gösteriliyor. |
| **CTA ve bitiş ekranı** | Bu videoda ana CTA istisnai olarak prompt dosyasıdır ve e-posta daveti sözlü söylenir; yorum sorusu kullanılmaz. Sözlü: "on prompt açıklamada" → "bütün videoların prompt'ları tek dosyada; bağlantısı açıklamada" → son cümle: Yayın 1. Bitiş ekranı: Yayın 1. |
| **Shorts** | (1) En çok kullanılan prompt, tek başına — SH1. (2) Bir prompt'un önce/sonra çıktısı — SH3. (3) On prompt'a rağmen elle yapılan iş `[ÇEKİMDE: varsa]` — SH4. |

---

## 10. Tek sayfalık üretim kontrol listesi

Her video için sırayla:

1. [ ] Fikir cümlesi iki kalıptan biriyle yazıldı; veto soruları geçti; puan ≥ 12; ölçüt 1 ve 3 sıfır değil.
2. [ ] Arama doğrulaması yapıldı; 10 başlık yazıldı, 3'e indi; 3 kapak eskizi çizildi; vaat testi zaman damgasıyla cevaplandı.
3. [ ] Kapakta tam bir dönüşüm çifti var ve türü fikir cümlesinin kalıbıyla aynı; süre en fazla bir yerde (kapak ya da başlık).
4. [ ] Elle süre / hakem görüşü / ölçüt listesi çekimden önce alındı.
5. [ ] Hook kalıbı ve açılış sahnesi seçildi; hook, yer tutucular dolu hâliyle sesli okununca ≤ 35 sn.
6. [ ] Kurgu seçildi; iskelet dakikalarıyla dolduruldu; kronometrenin nerede sayıp nerede duracağı işaretlendi.
7. [ ] En fazla 2 sözlü açık döngü; her birinin kapanış zamanı yazılı.
8. [ ] Senaryoda yeni / kanıt / geçiş işaretlemesi yapıldı; art arda iki geçiş yok.
9. [ ] Çekimden sonra: bütün `[ÇEKİMDE: …]` cümleleri gerçeğe göre yazıldı ya da silindi; sonucu varsayan başlık parçaları doğrulandı.
10. [ ] "Yapamadığı şey" bölümü çekimde yaşanan gerçek bir bulguya dayanıyor; veriye bilerek konan tuzak videoda söylendi.
11. [ ] Prompt açıklamada, e-posta istemeden kopyalanabilir durumda.
12. [ ] En fazla 3 sözlü CTA; abone yalnızca görsel; ilk 60 saniyede istek yok; vedalaşma cümlesi yok; son sesli cümle sonraki video; bitiş ekranı hedefi kartla aynı.
13. [ ] Başlık, kapak, seslendirme ve açıklamadaki sayılar ölçümle ve birbiriyle aynı.
14. [ ] Kapak 3.4'teki listeden geçti.
15. [ ] 2–3 Shorts anı seçildi; seslendirmeleri ayrı kaydedildi; üçü üç ayrı türden.
16. [ ] Ham kurgu 1,5× hızda telefonda izlendi; işaretlenen anlar düzeltildi.
17. [ ] Yayından 48 saat ve 7 gün sonra tutma grafiği okundu; "öğrenilenler" kaydına bir satır eklendi.

---

## İlgili belgeler

- Tam senaryolar: `docs/senaryolar/01-chatgptyi-yanlis-kullaniyorsun.md` (Yayın 1), `docs/senaryolar/02-3-saatlik-excel-isi-10-dakikada.md` (Yayın 2), `docs/senaryolar/03-prompt-yazmanin-tek-formulu.md` (yedek video).
- `docs/02-buyume-stratejisi.md` — metriklerin okunması, başlık/kapak testi, bitiş ekranı ve e-posta listesi kurulumu, Shorts ölçümü, resmî kaynak bağlantıları.
- `docs/03-yapim-is-akisi.md` — üretim hattı, elle süre ölçümünün takvimi, kısa video kesim akışı, varlık kütüphanesi (kronometre, bölüm kartı, renk ve yazı tipi notu).
- `docs/sablonlar/video-brief.md` — fikir filtresi ve paket alanlarının doldurulduğu şablon; `docs/sablonlar/performans-kaydi.md` — "öğrenilenler" kaydı.
