# 02 — Büyüme Stratejisi

Kanal: **Kısa Mesai** · Belge tarihi: 2026-11-16 · İlgili belgeler: `01-icerik-uretim-sistemi.md` (paketleme, hook, CTA metinleri orada; burada tekrar edilmez), `03-yapim-is-akisi.md` (üretim aşamaları ve süre bütçesi), `sablonlar/performans-kaydi.md` (takip şablonu; bu belgedeki bütün "tabloya yaz" talimatları o dosyayı kasteder).

Bu belge iki şeyi yapar: (A) YouTube'da keşfin nasıl işlediğini, Studio'da neye bakılacağını anlatır; (B) Kısa Mesai için aşamalı, tek kişinin yürütebileceği bir büyüme planı verir.

### Kaynak ve doğrulama durumu

Bu belge yazılırken YouTube Yardım sayfaları (support.google.com) ve YouTube resmî blogu (blog.youtube) çalışma ortamından **doğrudan açılamadı**; resmî sayfaların içeriği yalnızca web araması sonuçlarındaki alıntılar ve özetler üzerinden kontrol edilebildi. Bu yüzden her iddia şu dört etiketten biriyle işaretlidir:

| Etiket | Anlamı |
|---|---|
| **[Resmî]** | YouTube Yardım / YouTube'un kendi açıklaması; arama sonuçlarındaki resmî sayfa alıntısıyla teyit edildi. Bağlantı verildi. |
| **[Resmî — sayfada teyit et]** | Belirli bir resmî sayfaya dayandırılan iddia; sayfa adı ve bağlantısı verildi ama sayfanın kendisi bu oturumda okunamadı. Uygulamadan önce bağlantıyı aç. |
| **[YouTube'a atfedilen — kaynak bulunamadı]** | Üretici çevrelerinde "YouTube böyle söyledi" diye aktarılan, ama bu belge için belirli bir resmî sayfa, blog yazısı ya da Creator Insider videosu gösterilemeyen iddia. Resmî sayma; yaygın gözlem gibi ele al. |
| **[Yaygın gözlem]** | YouTube'un resmen söylemediği, üreticiler ve analistler arasında genel kabul gören çıkarım. Kanalın kendi verisiyle sınanmalı. |

**Creator Insider ve resmî blog:** Bu belgede hiçbir Creator Insider videosu adıyla ve tarihiyle gösterilmiyor, çünkü hiçbiri bu oturumda izlenip teyit edilemedi; video adı uydurmak yerine ilgili iddialar yukarıdaki üçüncü etikete indirildi. Yükleme saati, ara verme ve paket değiştirme hakkındaki iddialar Creator Insider'a değil, aynı konuları yazılı olarak ele alan [YouTube performance FAQ & troubleshooting](https://support.google.com/youtube/answer/141805) sayfasına dayandırıldı. Resmî blogdan yalnızca bir yazının adresi arama sonuçlarında görüldü ([Related videos traffic guide](https://blog.youtube/creator-and-artist-stories/youtube-related-videos-traffic-guide/)); içeriği okunamadığı için hiçbir iddia ona dayandırılmadı, A7'de okuma önerisi olarak duruyor.

Studio'daki sekme ve metrik adları zaman içinde değişiyor. Aşağıdaki adlar Türkçe arayüzde beklenen karşılıklardır; birebir aynısını bulamazsan aynı kavramı ara.

Bu belgedeki tüm "kaç video", "kaç gün", "kaç gösterim" eşikleri **çalışma kuralıdır (tahmini)**; YouTube'un açıkladığı sınırlar değildir.

**Video adlandırma:** Videolar her yerde yayın sırasına göre `KM-001`, `KM-002`… diye ve kısa başlıkla anılır (03 belgesi ve performans kaydıyla aynı). Fikir havuzundaki numara bu belgede kullanılmaz. İlk 10: KM-001 Yanlış kullanıyorsun (B) · KM-002 3 saatlik Excel işi (G) · KM-003 Türkçede hangisi iyi (K) · KM-004 30 dakikada başlangıç (B) · KM-005 10 dakikada sunum (G) · KM-006 Excel formülü (G) · KM-007 Muhasebeciler (M) · KM-008 CV + İK uzmanı (P) · KM-009 Bir hafta e-posta (G) · KM-010 10 prompt (B).

---

# Bölüm A — YouTube'da büyüme nasıl işler

## A0. Tek cümlelik model

**[Resmî]** YouTube'un performans SSS'sinde özetle şu söyleniyor: sistem videoları kitlene "tanıtmaz"; kitlen YouTube'u ziyaret ettiğinde onlar için video "bulur". (Bu bir çeviri özetidir, birebir alıntı değildir.) Kaynak: [YouTube performance FAQ & troubleshooting](https://support.google.com/youtube/answer/141805), [YouTube's Recommendation System](https://support.google.com/youtube/answer/16533387).

**[Yaygın gözlem]** Üreticilerin bundan çıkardığı çalışma modeli: sistemin sorduğu soru "bu video iyi mi?" değil, "bu izleyici şu an bunu izlerse memnun kalır mı?"dır.

Pratik sonucu: her video şu zincirden geçer ve zincirin her halkası Studio'da ayrı bir metriktir.

```
Gösterim  →  Tıklama (CTR)  →  İzleme (tutma, süre)  →  Memnuniyet  →  Geri dönüş
(kime gösterildi) (paket çalıştı mı) (video sözünü tuttu mu) (anket, beğeni,    (aynı kişi
                                                             "ilgilenmiyorum")   yine geldi mi)
```

Zayıf halka neredeyse müdahale oraya yapılır (karar tablosu: Bölüm B5).

## A1. Gösterimler

- **Ne:** Kapağın YouTube içinde bir izleyiciye gösterilme sayısı. **[Resmî — sayfada teyit et]** Kapak en az 1 saniye ve en az yarısı görünür olduğunda sayılır; YouTube dışına gömülü oynatıcılar, bildirim/e-posta ve bitiş ekranı gibi bazı yüzeyler sayılmaz. Bu yüzden "görüntüleme" sayısı, "gösterim × CTR"den büyük çıkabilir. Kaynak: [Impressions & click-through-rate FAQs](https://support.google.com/youtube/answer/7628154).
- **Studio'da:** Analytics → **Erişim** → "Gösterimler" kartı ve altındaki huni ("Gösterimler ve izlenme süresine etkisi"). Video bazında: Video → Analytics → Erişim.
- **İyi işaret:** Gösterim yayından günler/haftalar sonra da artıyor ve artış **Göz atma** ya da **Önerilen** kaynağından geliyor (sistem videoyu yeni kitlelere açıyor).
- **Kötü işaret:** Gösterim ilk 48 saatten sonra düz çizgi ve tamamı abone/arama kaynaklı. Bu "ceza" değildir; sistem videoyu gösterebileceği başka izleyici kümesi bulamamıştır.
- **Kısa Mesai için:** İlk 10 videoda gösterim sayısı küçük olacak ve bu normal; kanalın henüz izleyici geçmişi yok. Bu aşamada gösterimi büyütmenin gerçekçi yolu aramadır (A9) — "excel formülü yapay zeka", "chatgpt ile sunum" gibi sorgular kanalın izleyici geçmişi olmasa da gösterim üretir.

## A2. Gösterim tıklama oranı (CTR)

- **Ne:** Gösterimlerin yüzde kaçının izlemeye dönüştüğü. Başlık + kapak paketinin, **gösterildiği kitleye** ne kadar uyduğunun ölçüsü.
- **Studio'da:** Analytics → Erişim → "Gösterim tıklama oranı".
- **Evrensel eşik yok.** **[Resmî]** YouTube, kanal ve videoların yarısında CTR'nin %2 ile %10 arasında olduğunu söylüyor; bu bir hedef değil, dağılım bilgisidir. Aynı sayfa CTR'nin içerik türüne, kitleye ve gösterimin YouTube'da nerede yapıldığına göre değiştiğini belirtir. Kaynak: [Impressions & click-through-rate FAQs](https://support.google.com/youtube/answer/7628154).
- **Okuma kuralları:**
  1. **CTR'yi tek başına okuma, gösterimle birlikte oku.** **[Resmî — sayfada teyit et]** (aynı sayfa) Az gösterimli videoda CTR yüksek çıkar çünkü gösterim çoğunlukla seni zaten tanıyan kişilere yapılır; video geniş kitleye açıldıkça CTR'nin düşmesi beklenen bir şeydir. "CTR düştü ama gösterim 5 katına çıktı" iyi haberdir; karar tablosunda bu durumun karşılığı "dokunma"dır.
  2. **Kaynak bazında kıyasla.** Arama CTR'si ile Göz atma CTR'si aynı terazide tartılmaz. Erişim → Trafik kaynakları tablosunda her kaynağın kendi CTR'si görünür.
  3. **Kıyas noktası kanalın kendi medyanıdır.** Aynı trafik kaynağı, yayından sonra aynı gün sayısı; kategori ayrımı ancak kategoride yeterli video olunca (kıyas merdiveni: B5). Az videoda ortalama yerine medyan kullan; tek bir aykırı değerli video ortalamayı bozar.
  4. **Asgari veri olmadan oran okuma.** 1.000 gösterimde %5 CTR 50 tıklamadır; bir puanlık fark 10 tıklamadan ibarettir. Asgari veri eşikleri B5'te.
- **İyi işaret:** Aynı kaynakta, benzer gösterim hacminde kanal medyanının üstünde CTR.
- **Kötü işaret:** Göz atma'da gösterim var, CTR o kaynaktaki kanal dağılımının alt üçte birinde (tanım: B5) → paket o kitleye bir şey söylemiyor. Ya da CTR yüksek ama ilk 30 saniye kaybı da yüksek → paket videonun vermediği bir şey vaat ediyor (Kısa Mesai'nin "tık tuzağı yok" kuralının ölçülebilir hali).
- **Kısa Mesai için:** Kapağın sabit öğesi "X → Y" dönüşüm çiftidir (süre, çıktı ya da soru çifti; hangisinin ne zaman kullanılacağı 01 belgesi 3.1'de; "3 sa → 12 dk" süre çiftinin biçim örneğidir). Varsayım: kalıp sabit kaldığı için videodan videoya değişen şey görev ve çiftin içeriği olur; bu da hangi **görevin** ilgi çektiğini daha temiz okumayı sağlar. Çift türü farklı videoların CTR'si yan yana konurken tür de not edilir.

## A3. İzlenme süresi, ortalama görüntüleme süresi, ortalama izlenme yüzdesi

- **Ne:** *İzlenme süresi* = toplam izlenen saat. *Ortalama görüntüleme süresi (AVD)* = görüntüleme başına dakika. *Ortalama izlenme yüzdesi (APV)* = videonun ortalama yüzde kaçının izlendiği.
- **Studio'da:** Analytics → **Etkileşim** → "İzlenme süresi (saat)" ve "Ortalama görüntüleme süresi". Ortalama izlenme yüzdesi: Video → Analytics → Etkileşim, ya da Gelişmiş mod → metrik ekle.
- **Okuma kuralı:** Farklı uzunluktaki videoları APV ile kıyaslama. 8 dakikalık videoda %50 = 4 dk; 14 dakikalık videoda %40 = 5,6 dk. İkincisi yüzdece düşük, süre olarak daha çok izlenmiş. İkisini yan yana yaz.
- **[Resmî]** YouTube, önerilerde yalnızca izlenme süresine değil memnuniyete de baktığını açıkça söylüyor (A11). **[Yaygın gözlem]** Videoyu şişirerek süre kazanmak işe yaramaz; uzatılan bölümde tutma düşer ve sonraki videoya geçiş azalır.
- **İyi işaret:** AVD (dakika olarak) aynı kaynakta kanal medyanının üstünde **ve** video uzadığında dakika olarak artıyor (12 dakikalık videonun AVD'si 8 dakikalık videonunkinden uzun). Arama kaynaklı AVD, Göz atma kaynaklı AVD'ye yakın ya da üstünde (arayan kişi aradığını buldu).
- **Kötü işaret:** Video uzadıkça AVD dakika olarak aynı kalıyor (eklenen dakikalar izlenmiyor). Bir kaynakta AVD o kaynağın kanal dağılımında alt üçte birde (B5): arama ise aranan cevap geç geliyor (B5'te satırı var), Göz atma ise paket yanlış kitleyi çağırıyor. İzlenme süresi artıyor ama bitiş ekranı tıklaması düşüyor (izleyici videoyu bitiriyor, kanalda kalmıyor).
- **Görüntüleme sayımı notu.** İkincil kaynaklara göre YouTube, herkese açık görüntüleme sayacını önce Shorts'ta (31 Mart 2025), sonra tüm formatlarda (24 Ağustos 2026) oynatma başladığı an sayacak şekilde değiştirdi ([Tubefilter](https://www.tubefilter.com/2025/03/26/youtube-shorts-views-counting-stats/), [vidIQ](https://vidiq.com/blog/post/youtube-view-count-update/), [PPC Land](https://ppc.land/youtube-counts-views-from-the-first-frame-across-all-formats-on-august-24/)); değişikliğin izleme sayfasındaki sayaçla ilgili olduğu yazılıyor. Studio'daki görüntüleme ve AVD rakamlarının bundan etkilenip etkilenmediği teyitsiz; kaynaklar uzun videoda "engaged views" tanımı konusunda birbiriyle çelişiyor. Uygulama: tabloya **Studio'daki** rakamı yaz, izleme sayfasındaki sayacı yazma; başka kanalların herkese açık sayılarıyla kıyas yapma.
- **Kısa Mesai için:** Ana metrik APV değil, **"sonda süre ve kalite karşılaştırması" bölümüne ulaşan izleyici oranı**. İmza formatın vaadi orada ödeniyor; izleyici oraya varmadan çıkıyorsa format çalışmıyor demektir.

## A4. İzleyici tutma grafiği

- **Ne:** Videonun her anında izleyicilerin yüzde kaçının hâlâ izlediğini gösteren eğri.
- **Studio'da:** Video → Analytics → Etkileşim (veya Genel Bakış) → "Kitleyi elde tutmayla ilgili önemli anlar". **[Resmî — sayfada teyit et]** Rapor dört an türü işaretler: **giriş** (ilk 30 saniyeden sonra hâlâ izleyenlerin yüzdesi), **en iyi anlar** (eğrinin düz gittiği yerler), **sıçramalar** (tekrar izlenen/paylaşılan yerler), **düşüşler** (atlanan ya da çıkılan yerler). Ayrıca aynı uzunluktaki YouTube videolarına göre "tipik" tutma kıyası verir. Kaynak: [Measure key moments for audience retention](https://support.google.com/youtube/answer/9314415).
- **Az görüntülemede grafik eksik olabilir.** Studio, görüntülemesi çok az olan videoda tutma grafiğini ya da "tipik" kıyasını göstermeyebilir **[Yaygın gözlem]**. Grafik yoksa hücreye "veri yok" yaz; tahmin yürütme.
- **Şekil sözlüğü:**

| Şekil | Olası anlam | Kısa Mesai'de tipik neden |
|---|---|---|
| İlk 30 sn'de dik düşüş | Paket–açılış uyumsuzluğu ya da yavaş giriş | Görev ve elle süresi ilk cümlede söylenmedi; selamlama/kanal tanıtımı var |
| Düz, hafif eğimli çizgi | İzleyici vaat edilen şeyi alıyor | Kronometre çalışıyor, adımlar net |
| Tek noktada basamak düşüş | O saniyede bir şey izleyiciyi kaybettirdi | Uzun yazma/bekleme anı hızlandırılmadı; sponsor/abone çağrısı; "şimdi teoriye geçelim" cümlesi |
| Tepe (sıçrama) | Tekrar izleme | Prompt ekranda; izleyici kopyalamak için geri sarıyor → prompt'u açıklamaya ve sabitlenmiş yoruma koy |
| Çukur ardından toparlanma | İzleyici ileri sardı | O bölüm atlanabilir; sonraki videoda kısalt |
| Son 30–60 sn'de dik düşüş | İzleyici "bitti" sinyalini aldı | "Evet, bu kadardı" cümlesi; sonraki video önerisi bu cümleden **önce** söylenmeli |

- **Kıyas:** Giriş yüzdesini kanalın kendi videoları arasında kıyasla. Studio'nun "tipik" kıyası yardımcıdır ama tüm YouTube'daki aynı uzunluktaki videolara göredir; eğitim/ekran kaydı içeriği için birebir emsal değildir.
- **Kısa Mesai için sabit işaret noktaları:** her videoda şu dört anın zaman damgasını ve o andaki tutma yüzdesini video kartına yaz: (1) 0:30, (2) kronometrenin başladığı an, (3) "yapamadığı şey" bölümünün başı, (4) süre/kalite karşılaştırmasının başı. 10 video sonunda formatın hangi bloğunun izleyici kaybettirdiği görünür.

## A5. Yeni, ara sıra ve düzenli izleyiciler

- **Ne:** **[Resmî]** YouTube kitleyi üç gruba ayırıyor: *yeni izleyiciler* (seçili dönemde kanalı ilk kez izleyenler), *ara sıra izleyenler* (casual; kanalı zaman zaman izleyenler) ve *düzenli izleyenler* (regular; kanalı uzun süredir tutarlı biçimde izleyenler). Kaynak: [Understand new, casual, & regular viewers](https://support.google.com/youtube/answer/10246996), [ipuçları](https://support.google.com/youtube/answer/13615784). Bu üçlü, eski "geri dönen izleyiciler" metriğinin yerini aldı; kırılım Kitle sekmesinde aylık dökümle gösteriliyor.
- **Eşikler (ikincil kaynaklara göre; resmî sayfada teyit et):** ara sıra izleyen = son 12 ayın 1–5 ayında izlemiş; düzenli izleyen = son 12 ayın 6 ya da daha fazla ayında izlemiş ([PPC Land](https://ppc.land/youtube-introduces-refined-viewer-analytics-with-casual-and-regular-metrics/)). Bir başka ikincil kaynak düzenli eşiğini 7+ ay veriyor. Kesin sayı için Studio'daki bilgi balonuna bak.
- **Bu tanımın yeni kanal için sonucu:** Altı ayrı ayda izlemiş olmak gerektiğinden, kanal açıldıktan sonraki **ilk yaklaşık 6 ayda düzenli izleyici sayısı sıfır görünür.** Bu bir sorun değil, tanımın aritmetiğidir. Haftada 1 video ritmiyle KM-030 yedinci aya denk gelir; düzenli izleyici sayısı ancak o sıralarda oluşmaya başlar. Bu yüzden ilk 30 videoda bu metrik hedef yapılmaz (B1).
- **[Resmî]** Aynı sayfaya göre düzenli izleyici sayısının kendisi erişimi ya da para kazanmayı doğrudan etkilemez; bu bir teşhis metriğidir.
- **Studio'da:** Analytics → **Kitle** → izleyici türü kartı (aylık). Video bazında Kitle sekmesinde hangi videonun yeni izleyici getirdiği görülebilir; video düzeyinde hâlâ "geri dönen izleyiciler" adlı bir satır olup olmadığı teyit edilemedi (Ek, madde 3).
- **Haftalık okunabilen vekil göstergeler** (aylık kırılımı beklemeden "aynı kişiler geri geliyor mu" sorusuna yaklaşmak için):
  1. Trafik kaynağında **Abonelik akışı + Bildirimler** kaynaklı görüntüleme (kanalı zaten tanıyan kişi geldi).
  2. **Bitiş ekranı öğesi tıklama oranı** (videodan sonra kanalda kaldı).
  3. Önerilen videolar kaynağında **kendi videolarından gelen pay** (aynı kişi art arda iki videonu izledi).
- **İyi işaret:** Ara sıra izleyen sayısı aydan aya artıyor; üç vekil gösterge video sayısıyla birlikte yükseliyor; yeni izleyici çizgisi yayın günlerinde sıçrıyor.
- **Kötü işaret:** Yeni izleyici geliyor ama ara sıra izleyen sayısı aydan aya düz ve Önerilen listesinde kendi videoların yok → videolar tek seferlik çözüm olarak tüketiliyor; kanal "seri" olarak algılanmıyor. Müdahale: B3 (seri mimarisi) ve B7.
- **Kısa Mesai için:** İzleyici "sorunu arar, aracı değil" tanımına uyduğu için varsayılan davranış tek videoyu izleyip çıkmaktır. Geri dönüşü üreten şey kanalın adı değil, **tekrarlanan format** (kronometre + karşılaştırma + prompt) ve **bir sonraki görevin vaadi**dir.

## A6. Trafik kaynakları — genel

- **Ne:** İzleyicinin videoya hangi yüzeyden geldiği: YouTube araması, Önerilen videolar, Göz atma özellikleri, Shorts feed'i, kanal sayfaları, abonelik akışı/bildirimler, harici.
- **Studio'da:** Analytics → Erişim → "Trafik kaynağı türleri" → "Daha fazla göster". Her kaynak satırında gösterim, CTR, görüntüleme, AVD ayrı görünür. Kaynak: [Understand your reach / traffic sources](https://support.google.com/youtube/answer/9314355) **[Resmî — sayfada teyit et]**.
- Sıfırdan başlayan bir eğitim kanalında beklenen sıra **[Yaygın gözlem]**: önce YouTube araması ve harici, sonra Önerilen, en son Göz atma. Sıra farklı çıkarsa sorun değil; önemli olan her videonun planlanan kaynağından trafik alıp almadığı (B3).
- **İyi işaret:** Videonun 28. gündeki birincil kaynağı, yayından önce yazdığın "planlanan birincil kaynak"la aynı. Kanal düzeyinde hiçbir kaynak tek başına trafiğin tamamı değil ve video sayısı arttıkça Önerilen + Göz atma payı büyüyor. Arama kaynaklı görüntüleme eski videolarda da sürüyor.
- **Kötü işaret:** Trafiğin tamamına yakını "Harici" ya da "Doğrudan/bilinmeyen" (videoyu yalnızca senin paylaştığın yerlerdeki kişiler izliyor; YouTube içinde keşif başlamamış). Arama videosu olarak planlanan videoda arama payı yok. Birincil kaynak her videoda başka (kanalın tekrar eden bir giriş kapısı yok).
- **Kısa Mesai için:** Harici trafiği LinkedIn gönderisi (03 belgesi) üretir; bu, ideal izleyiciyi getirdiği sürece değerlidir ama YouTube içi keşfin yerine geçmez. Harici kaynaklı AVD, videonun diğer kaynaklarındaki AVD'nin yarısından kısaysa (tahmini çalışma kuralı; asgari veri V2) gönderi yanlış beklentiyle tıklatıyor demektir; gönderi metnini videonun gerçek içeriğine yaklaştır.

## A7. Önerilen videolar

- **Ne:** Başka bir videonun yanında/altında ve video bitince çıkan öneriler.
- **Studio'da:** Trafik kaynağı → "Önerilen videolar" satırına tıkla → seni hangi videoların önerdiği listelenir.
- **[Resmî — sayfada teyit et]** Öneriler, izlenen videoyla konu ilişkisine ve izleyicinin geçmişine göre kişiselleştirilir ([YouTube's Recommendation System](https://support.google.com/youtube/answer/16533387)). **[Yaygın gözlem]** Bir kanalın kendi videoları birbirinin en güçlü öneri kaynağıdır; bunun koşulu aynı izleyicinin birden fazla videonu art arda izlemiş olmasıdır. Okuma önerisi (içeriği bu belge için okunamadı): YouTube resmî blogundaki [Related videos traffic guide](https://blog.youtube/creator-and-artist-stories/youtube-related-videos-traffic-guide/).
- **İyi işaret:** Önerilen listesinin ilk sıralarında **kendi videoların** var (oturum zinciri kurulmuş) ve zamanla nişteki başka kanalların videoları da listeye giriyor.
- **Kötü işaret:** Önerilen trafiği hiç yok ya da tamamı alakasız videolardan geliyor (konu sinyali dağınık).
- **Kısa Mesai için:** KM-002 (3 saatlik Excel işi) → KM-006 (Excel formülü) gibi **aynı sorunun devamı** olan çiftler kur; bitiş ekranı ve sözlü geçişle bağla.

## A8. Ana sayfa (Göz atma özellikleri)

- **Ne:** Ana sayfa, abonelik akışı, "Daha sonra izle" ve benzeri gezinme yüzeyleri. Studio'da "Göz atma özellikleri" olarak geçer.
- **Studio'da:** Trafik kaynağı → "Göz atma özellikleri" satırı; satıra tıklayınca alt yüzeyler (ana sayfa, abonelikler vb.) ayrışır.
- **[Resmî — sayfada teyit et]** Ana sayfa önerileri izleyicinin izleme geçmişine ve benzer izleyicilerin memnun kaldığı videolara dayanır ([YouTube's Recommendation System](https://support.google.com/youtube/answer/16533387)). İzleyici bir şey aramıyordur; kapak ve başlık soğuk bir kitleye kendini açıklamak zorundadır.
- **İyi işaret:** Göz atma payı video sayısıyla birlikte artıyor; yayından haftalar sonra Göz atma kaynaklı yeni gösterim dalgaları geliyor.
- **Kötü işaret:** Göz atma gösterimi var ama CTR kanalın arama CTR'sinin çok altında ve düşmeye devam ediyor → paket yalnızca konuyu zaten arayan kişiye anlamlı.
- **Kısa Mesai için:** Göz atma'ya uygun paket "araç adı"yla değil "görev + süre farkı"yla konuşur. "Excel'de ÇAPRAZARA formülü" arama paketidir; "3 saatlik rapor, 12 dakika" Göz atma paketidir. İkisi aynı videoda birleşebilir: görev kapakta, anahtar kelime başlıkta.

## A9. YouTube araması

- **Ne:** YouTube içi arama sonuçlarından gelen trafik.
- **Studio'da:** Trafik kaynağı → "YouTube araması" → izleyicinin yazdığı **arama terimleri** listelenir. Ek olarak Analytics'teki araştırma/ilham sekmesi (adı değişebiliyor) izleyicilerin YouTube'da ne aradığını gösterir.
- **[Resmî — sayfada teyit et]** Arama sıralamasında alaka (başlık, açıklama, video içeriğinin sorguyla eşleşmesi), etkileşim ve kalite birlikte değerlendirilir. Kaynak: [YouTube Search — How YouTube Works](https://www.youtube.com/howyoutubeworks/product-features/search/).
- **İyi işaret:** Arama terimleri listesi hedeflediğin sorgularla örtüşüyor; arama kaynaklı görüntüleme yayından aylar sonra da sürüyor (uzun kuyruk).
- **Kötü işaret:** Terim listesi boş ya da alakasız; ya da arama trafiği var ama AVD çok düşük (izleyici aradığını ilk 30 saniyede göremedi).
- **Kısa Mesai için:** Terim listesi bedava konu araştırmasıdır. Her hafta listeden, henüz videosu olmayan sorguları fikir havuzuna taşı. Türkçe sorgu yazımındaki varyasyonlara dikkat et ("yapay zeka" / "yapay zekâ", "chatgpt" / "chat gpt"); başlıkta izleyicinin yazdığı biçimi, açıklamada diğerini kullan.

## A10. Shorts akışı

- **Ne:** Dikey kaydırmalı akış. İzleyici seçmez; video önüne gelir, izler ya da kaydırır.
- **Studio'da:** Shorts videosu → Analytics → Erişim/Etkileşim → "Görüntülendi / kaydırılarak geçildi" oranı (viewed vs. swiped away) ve trafik kaynağında "Shorts feed'i". Kaynak: [Shorts analytics](https://support.google.com/youtube/answer/12942217) **[Resmî — sayfada teyit et]**.
- **Okuma:** Shorts'ta CTR'nin yerini "kaydırmadan kalma oranı" alır; ilk 1–2 saniye kapak işlevi görür. Görüntüleme sayımı için A3'teki nota bak.
- **[Yaygın gözlem]** Shorts izleyicisi ile uzun video izleyicisi büyük ölçüde ayrı davranır; Shorts abonesi otomatik olarak uzun video izleyicisine dönüşmez.
- **Köprü: "ilgili video" bağlantısı.** İkincil kaynaklara göre Shorts düzenlenirken Studio'da (bilgisayarda) aynı kanaldaki bir videoya tek bir "ilgili video" bağlantısı eklenebiliyor; bağlantı Shorts oynatıcısında kanal adının altında görünüyor ([Tubefilter](https://tubefilter.com/2023/09/01/youtube-related-links-multi-format-creators-shorts-live-long-form/), [vidIQ](https://vidiq.com/blog/post/youtube-related-links-connect-shorts-long-videos)). Yeni kanalda erişim koşulu teyit edilemedi; bir ikincil kaynak "gelişmiş özellikler" erişimi gerektiğini yazıyor. Kontrol: Studio → Ayarlar → Kanal → Özellik uygunluğu; ve bir Shorts'un ayrıntılar sayfasında "İlgili video" alanı görünüyor mu.
- **Bağlantı yoksa yedek yol:** Shorts'un son 2 saniyesinde uzun videonun **tam başlığı** hem sözle hem ekran yazısıyla verilir ("Tamamı kanalda: 3 Saatlik Excel İşini 10 Dakikada Bitirmek"). İzleyici kanal adına dokunup videoyu başlığından bulur.
- **Shorts açıklamasına ve yorumlarına bağlantı koyma.** YouTube'un 2023'te Shorts açıklama ve yorumlarındaki bağlantıları tıklanamaz yaptığı bildirildi ([Tubefilter](https://tubefilter.com/2023/09/01/youtube-related-links-multi-format-creators-shorts-live-long-form/)); kısıtın bugün sürüp sürmediği teyit edilemedi (ilk Shorts'ta dene). Bu yüzden B3'teki sabitlenmiş yorum kalıbı Shorts'a **uygulanmaz**; Shorts'ta sabitlenmiş yorum yalnızca prompt metnini ve uzun videonun tam başlığını düz yazı olarak taşır.
- **İyi işaret:** Kaydırmadan kalma oranı kanalın Shorts medyanının üstünde ve Shorts'tan uzun videoya geçiş var (uzun videonun trafik kaynağında "Shorts" satırı).
- **Kötü işaret:** Shorts görüntülemesi yüksek, uzun videolarda hiçbir iz yok ve Shorts kitlesinin demografisi ideal izleyiciden (26–42, çalışan) uzak.
- **Kısa Mesai için:** Shorts'un işi abone toplamak değil, **uzun videonun tek bir anını** (tek ipucu, hata / "yapamadığı şey" ya da önce/sonra; türler ve açılış kuralları 01 belgesi 4.4) göstermek ve ilgili video bağlantısıyla uzun videoya taşımaktır. Her Shorts tek başına anlamlı olmalı ("devamı kanalda" diye yarım bırakılmış klip değil).

## A11. Öneri sisteminin genel mantığı ve memnuniyet sinyalleri

**[Resmî]** YouTube'un açıkladıkları — kaynak: [YouTube's Recommendation System](https://support.google.com/youtube/answer/16533387), [performance FAQ](https://support.google.com/youtube/answer/141805):

- Sistem videoları kitleye tanıtmaz; kitle YouTube'a geldiğinde onlar için video bulur. Kişiselleştirmenin temeli izleyicinin kendi davranışıdır.
- Kullanılan sinyaller arasında izleme geçmişi, arama geçmişi, abonelikler, beğeni/beğenmeme, "İlgilenmiyorum" ve "Kanalı önerme" geri bildirimleri ve **memnuniyet anketleri** sayılır. Anketler, sistemin yalnızca izlenme süresini değil memnuniyeti de öğrenmesi içindir.
- Beğeni/beğenmeme tek başına belirleyici değildir; sıralamada değerlendirilen çok sayıda sinyalden biridir.

**[Resmî — sayfada teyit et]** (141805, zayıf performanslı videolarla ilgili SSS sorusu) Tek bir zayıf video kanalı başlı başına aşağı çekmez; sorun, izleyicilerin kanalın videoları kendilerine önerildiğinde izlemeyi bırakmasıyla başlar.

**[Yaygın gözlem]** Bu açıklamalardan üreticilerin çıkardığı çalışma ilkeleri:

1. **İzleyici kümesi tutarlılığı.** Kanal aynı tür izleyiciye aynı tür fayda verdikçe sistem "bu videoyu kime göstereceğini" daha kolay bulur. Konu dağınıklığı gösterimi düşürmez ama yanlış kişiye gösterim yaptırır; CTR ve tutma birlikte bozulur.
2. **Video bazında değerlendirme.** Her video kendi performansıyla dağıtılır. Ama zayıf video, kanalı tanıyan izleyicinin bir sonraki videoya tıklama ihtimalini düşürebilir.
3. **Memnuniyet doğrudan görülmez.** Anket sonuçları Studio'da yoktur; vekil göstergelere bakılır.

**Studio'da nerede görülür:** Öneri sisteminin kendisine ait bir rapor yok; etkisi üç yerde dolaylı okunur.

| Ne | Studio'da yer |
|---|---|
| Sistem videoyu yeni kitlelere açıyor mu | Video → Analytics → Erişim → trafik kaynağında Göz atma ve Önerilen gösterimlerinin günlük seyri |
| Seni hangi videolar öneriyor | Erişim → Trafik kaynağı → "Önerilen videolar" satırına tıkla |
| Memnuniyetin vekil göstergeleri | Etkileşim → bitiş ekranı öğesi tıklama oranı; Genel Bakış → beğeni oranı ("beğenenler / beğenmeyenler"); Kitle → bu videodan kazanılan ve kaybedilen abone; yorumlar |

- **İyi işaret:** Yüksek CTR'li videolarda 0:30 tutması düşmüyor (paket sözünü tutuyor); bitiş ekranı tıklaması ve beğeni oranı kanal medyanında ya da üstünde; "denedim, işe yaradı" türü yorumlar var; video yayından haftalar sonra Göz atma/Önerilen'den yeni gösterim alıyor.
- **Kötü işaret:** CTR yüksek, 0:30 tutması ve beğeni oranı kanalın alt üçte birinde (izleyici beklediğini bulamadı); bir videodan kaybedilen abone kazanılandan fazla; yorumlarda "başlıkta yazan şey videoda yok" türü itiraz; Önerilen listesi alakasız videolardan oluşuyor.

**Kısa Mesai için:** Kanalın tonu (abartısız, "yapamadığı şey" bölümü) memnuniyet sinyaliyle aynı yöne çalışır: izleyici vaat edilenden fazlasını değil, **tam vaat edileni** alır. Ölçüsü: yüksek CTR'li videolarda ilk 30 saniye tutmasının düşmemesi.

---

# Bölüm B — Kısa Mesai için uygulanabilir strateji

## B1. Aşamalı plan

Aşama geçişi takvimle değil **video sayısı + veri yeterliliği** ile olur.

### Aşama 1 — KM-001–010: "Format çalışıyor mu?"

| | |
|---|---|
| **Hedef** | İmza formatın (kronometre → karşılaştırma → yapamadığı şey → prompt) izlenebilir olduğunu kanıtlamak; kanal medyanını kurmak. |
| **Odak metrik** | (1) 0:30'daki tutma yüzdesi, (2) karşılaştırma bölümüne ulaşan izleyici yüzdesi, (3) arama terimleri listesi. Abone sayısı ve toplam görüntüleme **odak değil**. |
| **Yapılır** | Planlanan 10 videoyu sırayla yayınla. Her videoda A4'teki dört işaret noktasını kaydet. Her yoruma cevap ver. Arama terimlerinden fikir topla. Stok kuralına uy (B2). Oynatma listelerini ilk videodan itibaren kur (B3). Prompt dosyasını e-posta istemeden açık bağlantıyla paylaş (B7). |
| **Yapılmaz** | KM-001–005'te yayınlanmış videoya metrik gerekçesiyle müdahale (yalnızca kaydet; istisna: B5'teki açık hata durumları). Yerleşik başlık/kapak testi açmak (B4: taban medyan kurulmadan ve gösterim azken test hem sonuçsuz biter hem CTR kaydını bozar). Kategoriler arası "hangisi daha iyi" kararı vermek. Niş değiştirmek. Günlük Studio kontrolü. Shorts sayısını artırmak için uzun videoyu aksatmak. |
| **Çıkış koşulu** | 10 video yayında **ve** en az 6 videonun 28 günlük verisi var. |

İlk 10'un kategori dağılımı: **B** üç video (KM-001, KM-004, KM-010; geniş giriş kapısı), **G** dört video (KM-002, KM-005, KM-006 arama sorgusu olan görevler; KM-009 deney kurgusu), **K** bir video (KM-003), **M** bir video (KM-007), **P** bir video (KM-008), **İ** sıfır video. Sonuç: 10. videonun sonunda yalnızca B ve G hakkında kategori düzeyinde konuşulabilir; K, M ve P tek videoyla, İ hiç denenmemiş durumdadır.

### Aşama 2a — KM-011–022: "Eksik kategorileri üçe tamamla"

| | |
|---|---|
| **Hedef** | Her kategoride en az 3 video olsun ki kategoriler birbiriyle kıyaslanabilsin; bu sırada B ve G **varsayılan omurga** olarak sürsün. |
| **Odak metrik** | (1) Aylık "ara sıra izleyen" sayısı, (2) haftalık vekil göstergeler: abonelik akışı + bildirim kaynaklı görüntüleme, bitiş ekranı tıklama oranı, Önerilen'de kendi videolarından gelen pay (A5), (3) kanal geneli CTR ve tutma medyanı (aynı kaynak, aynı yaş). Düzenli izleyici sayısı bu aşamada sıfırdır; bakılmaz. |
| **Yapılır** | 12 videonun 9'u eksik kategorilere: İ'ye 3, K'ye 2, M'ye 2, P'ye 2; kalan 3'ü B/G devam videosu. Önerilen sıra: KM-011 İ · 012 M · 013 K · 014 İ · 015 P · 016 G · 017 M · 018 K · 019 İ · 020 P · 021 B · 022 G (eksik kategorilerin üçüncü videoları KM-020'ye kadar biter; son veri KM-024 haftasında dolar). Her yeni video bir öncekine ya da serideki bir videoya açıkça bağlanır. E-posta kayıt formunu aç (B7). Topluluk gönderilerini koşul sağlanınca başlat (B6). Yerleşik testi yalnızca asgari gösterim koşulunu sağlayan videolarda aç (B4). İlk 10'dan tutması üst üçte birde, CTR'si alt üçte birde olanların paketini yenile. |
| **Yapılmaz** | Tek videoya bakıp kategori hakkında hüküm vermek. Tek bir yüksek performanslı videoya bakıp bütün kanalı o konuya çevirmek. Yükleme sıklığını artırmak. |
| **Çıkış koşulu** | Altı kategorinin her birinde en az 3 video ve bunların 28 günlük verisi var. |

**İ kategorisinin ilk videoları (öneri; fikir filtresinden geçir):** KM-011 "Tek kişilik e-ticaret için ürün açıklamaları" (01 belgesi §2.2'deki küçük işletme başlık formülünün örneği; adet ve süre çekimde ölçülür), KM-014 müşteri şikâyetine/sorusuna cevap, KM-019 fiyat teklifi hazırlama. Üçü de arama videosu rolünde planlanır; hedef sorgular çekimden önce YouTube otomatik tamamlamasından doğrulanır.

### Aşama 2b — KM-023–030: "Çalışanı çoğalt"

| | |
|---|---|
| **Hedef** | Verinin gösterdiği en güçlü 2 kategoriyi seriye dönüştürmek; Önerilen trafiğinde kendi videolarını görmek. |
| **Odak metrik** | 2a ile aynı; ek olarak (4) kategori bazında görüntüleme, CTR ve tutma medyanı (3–4 videolu kategoride yalnızca yön bilgisi; karar kuralı B4). |
| **Yapılır** | Kategori kararı, KM-020'nin 28. günü dolduğunda (yaklaşık KM-024 haftası) verilir; o güne kadar B ve G sürer. Karardan sonra üretimin yaklaşık %70'i güçlü 2 kategoriye, %20'si diğerlerine, %10'u yeni format denemesine (tahmini dağılım; B4'teki test kaydıyla yönet). İzleyici görevlerini videoya çevirme döngüsünü işlet (B6). |
| **Yapılmaz** | Zayıf kategoriyi tamamen kapatmak (durdurma kuralı B4'te; 3 videodan az denenmişse karar verme). Güçlü kategori B ve G dışında çıkarsa bile B listesindeki "Buradan Başla" serisini güncel tutmayı bırakmak. |
| **Çıkış koşulu** | 30 video yayında; en az iki seride 5'er video; en az iki kategoride 5+ video (karar tablosunda kategori medyanı kullanılabilir). |

### Aşama 3 — KM-031+: "Sistemi işlet"

| | |
|---|---|
| **Hedef** | Arama + Önerilen + Göz atma arasında dengeli trafik; öngörülebilir video başı performans; izleyici isteklerinden beslenen konu hattı. |
| **Odak metrik** | (1) Son 10 videonun 28 günlük görüntüleme **medyanı** (tek video değil, taban yükseliyor mu), (2) Göz atma payı, (3) aylık ara sıra + düzenli izleyici sayısı (düzenli izleyici bu aşamada yeni oluşmaya başlar; ilk aylarda küçük sayı beklenir), (4) e-posta listesi büyümesi. |
| **Yapılır** | Çeyrekte bir kanal denetimi: en zayıf tutmalı 5 videonun ortak noktası, en çok yeni izleyici getiren 5 videonun ortak noktası. Eskiyen araç videolarını güncelle (yeni video + eskisinin açıklamasına ve sabitlenmiş yorumuna yönlendirme). Meslek serisini izleyici talebine göre genişlet. İkinci haftalık video yalnızca stok 4 videonun altına düşmüyorsa düşünülür. |
| **Yapılmaz** | İmza formatı "sıkıldım" diye bırakmak — değişiklik veriye dayanmalı. Kapak kalıbını toptan değiştirmek (test et, sonra geç). |

## B2. Yükleme sıklığı ve takvim

**Tutarlılık mı, sıklık mı?**

- **[Resmî — sayfada teyit et]** YouTube'un [Upload schedule tips](https://support.google.com/youtube/answer/13616979) sayfası belirli bir sıklık önermiyor; sürdürülebilir bir tempo seçmeyi öneriyor.
- **[YouTube'a atfedilen — kaynak bulunamadı]** "Öneri sistemi yükleme sıklığını başlı başına ödüllendirmez; her video izleyici tepkisiyle değerlendirilir." Bu, üretici çevrelerinde YouTube çalışanlarına atfedilerek aktarılıyor; bu belge için belirli bir kaynak gösterilemedi.
- **[Yaygın gözlem]** Düzenli yayın iki nedenle işe yarar: izleyicide geri gelme alışkanlığı oluşturur ve sana daha hızlı öğrenme döngüsü (daha çok veri noktası) verir.

Sonuç: **haftada 1 videoyu hiç aksatmamak, haftada 2 videoyu üç hafta sürdürüp bırakmaktan iyidir.** Kalite düşürerek sıklık artırma.

### Haftalık takvim

Üretim oturumları ve süreleri 03 belgesi §2.1'deki standart haftadır; süreler `sablonlar/performans-kaydi.md` içindeki aşama bütçesinden gelir (**tahmini; ilk 3 videoda kronometreyle ölç ve bütçeyi güncelle**). Elle süre ölçümü bütçe dışıdır; görevin kendi süresi kadar ek zaman alır. Bu belge takvime büyüme işlerini ekler. **Yayın günü perşembe**; analiz günü de perşembedir, çünkü bir önceki video o gün tam 7 günlük, dört önceki video tam 28 günlük olur.

**Varsayım A — tam zamanlı işi olan üretici (akşamlar + hafta sonu):**

Günler ve üretim süreleri 03 belgesi §2.1 ile birebir aynıdır (tek kaynak orasıdır; orada değişirse burası da değişir). N = bu perşembe yayınlanan video, N+1 = bu hafta üretilen ve gelecek perşembe yayınlanacak video, N−1 = geçen perşembe yayınlanan video.

| Gün | Üretim (03 belgesi §2.1; N+1) | Büyüme işi (bu belge) | Tahmini süre |
|---|---|---|---|
| Cumartesi | Araştırma + paketleme + hazırlık (1 sa 45 dk) + elle koşu (görev süresi + 15 dk) | N−1'e 48 saat bakışı (B5) · LinkedIn gönderisi · haftalık e-posta (Aşama 2a'dan itibaren, B7; süresi bütçe dışı) | 1 sa 45 dk + elle koşu + 5 dk + 15 dk |
| Pazar | Senaryo | — | 1 sa 30 dk |
| Pazartesi | Çekim + seslendirme | (İsteğe bağlı) N−1'in üçüncü Shorts'u yayında | 1 sa 45 dk |
| Salı | Kurgu 1 | N'nin ilk Shorts'u yayında (uzun videodan önce; geçen hafta zamanlandı) | 1 sa 20 dk |
| Çarşamba | Kurgu 2 + kapak | Görev anketi gönderisi (koşul sağlanınca, B6) | 1 sa 35 dk + 10 dk |
| **Perşembe** | N+1'in Shorts kesimi (2 video) | **N yayında:** teknik kontrol, sabitlenmiş yorum, ilk yorumlar (B5 "1. saat") · **haftalık analiz rutini (B8)** | 50 dk + 15 dk + 30 dk |
| Cuma | N+1'in yayın hazırlığı ve zamanlaması + Shorts dağıtımı | N'nin ikinci Shorts'u yayında (uzun videodan sonra) · sonuç kartı gönderisi (koşul sağlanınca) | 50 dk + 10 dk |
| Her gün | — | Yorum cevapları | 10 dk × 7 |

**Haftalık toplam (tahmini): 12 sa 10 dk + elle koşu.** Hesap: 03 belgesindeki 10 sa 25 dk'lık standart hafta (elle koşu hariç) − oradaki 20 dk'lık analiz kalemi + bu belgedeki 35 dk analiz (5 + 30) + 20 dk topluluk gönderisi + 70 dk yorum cevabı. Topluluk gönderileri başlamadan önce 11 sa 50 dk. Elle koşu bunun üstüne görev süresi + 15 dk ekler (en fazla 1 sa 15 dk); haftalık e-posta da bütçe dışıdır. En uzun gün cumartesidir (elle koşuyla en fazla 3 sa 35 dk); sığmıyorsa elle koşu bir önceki cuma akşamına alınır, senaryodan sonraya alınmaz (03 belgesi §2.1).

**Varsayım B — haftada iki tam gün ayırabilen üretici (serbest çalışan):**

| Gün | İş | Tahmini süre |
|---|---|---|
| 1. gün (ör. pazartesi) | Araştırma + paketleme + hazırlık + elle koşu + senaryo + çekim + seslendirme | 5 sa + elle koşu |
| 2. gün (ör. salı) | Kurgu 1 + kurgu 2 + kapak + yayın hazırlığı + Shorts kesimi ve dağıtımı | 4 sa 35 dk |
| Perşembe | Yayın + haftalık analiz rutini | 45 dk |
| Cumartesi | 48 saat bakışı + LinkedIn (+ e-posta, bütçe dışı) | 20 dk |
| Diğer | Yorumlar (günde 10 dk), gönderiler (20 dk), Shorts yayınları zamanlanmış | 1 sa 30 dk |

Toplam aynıdır; fark, üretimin iki blokta bitmesi ve stok biriktirmenin kolaylaşmasıdır.

- **Yayın günü ve saati:** Perşembe ve tek bir saat; 10 video boyunca değiştirme. Saatin kendisi uzun vadeli performansı belirlemez (B9); sabitlemenin amacı senin üretim ritmin, analiz gününün "yayın + 7"ye denk gelmesi ve izleyicinin alışkanlığı. KM-010'dan sonra Analytics → Kitle → "İzleyicilerinizin YouTube'da olduğu zamanlar" kartına bak: **kart veri gösteriyorsa** ve belirgin bir yoğunluk varsa saati bir kez ayarla. Kart yeterli izleyici verisi olmayan kanalda boş gelir; boşsa gün/saat değişmez, KM-030'da yeniden bakılır.
- **Shorts:** Uzun videodan kesilir; ayrı çekim yapılmaz. Haftada **2 Shorts esas, üçüncüsü isteğe bağlı** (03 belgesindeki kısma sırasında ilk vazgeçilen kalem). Varsayılan dağılım 03 belgesindeki gibi: biri uzun videodan önce (salı), biri sonra (cuma). Hangisinin uzun videoya daha çok izleyici taşıdığı açık sorudur; B4'te FT6 olarak test edilir, sonuç gelene kadar dağılım değişmez. Uzun video yetişmiyorsa ilk vazgeçilen şey Shorts'tur.
- **Stok kuralı (03 belgesi §2.2 ile aynı):** Kanal açılmadan önce 2 video bitmiş olsun; sonrasında her zaman yayına hazır en az 1 video stokta dursun. Stok 0'a düşerse o hafta yeni format denemesi yapılmaz, kapsamı küçük bir B videosu çekilir.
- **Aksama kuralı:** Bir hafta kaçarsa telafi için aynı hafta iki video yayınlanmaz; takvim kaldığı yerden devam eder.

## B3. İçerik rolleri, seri mimarisi, oturum uzatma

### Her videoya yayından önce tek bir birincil rol ata

| Rol | Amaç | Başlık/kapak mantığı | Başarı ölçüsü | Örnek |
|---|---|---|---|---|
| **Arama videosu** | Belirli bir sorguyu yazan kişiyi yakalamak; uzun kuyruk | İzleyicinin yazdığı sorgu başlıkta, mümkünse başta. Kapakta görev + süre. | 28 günde arama payı; arama terimlerinin hedefle örtüşmesi; aylar sonra süren görüntüleme | KM-006 Excel formülü, KM-005 Sunum, KM-004 Başlangıç; İ'de KM-011 Ürün açıklamaları (plan) |
| **Öneri/Göz atma videosu** | Bir şey aramayan ideal izleyiciyi durdurmak | Merak ya da sonuç başlıkta; araç adı ikincil. | Göz atma + Önerilen payı; yeni izleyici sayısı | KM-008 CV + İK uzmanı, KM-009 Bir hafta e-posta, KM-001 Yanlış kullanıyorsun |
| **Köprü videosu** | İkisinin arasında: aranan bir konu + hikâye/deney çerçevesi | Sorgu + sonuç | İki kaynakta da pay | KM-003 Türkçede hangisi iyi, KM-002 3 saatlik Excel işi |
| **Merkez (hub) videosu** | Serinin giriş kapısı; diğer videolara dağıtım | Geniş vaat | Bitiş ekranı ve oynatma listesi geçişi | KM-001 Yanlış kullanıyorsun, KM-010 10 prompt |

Video kartına "planlanan birincil kaynak" ve 28. günde "gerçekleşen birincil kaynak" yaz. Uyuşmuyorsa ya paket ya rol tahmini yanlıştı; ikisi de öğrenmedir.

### Oynatma listesi mimarisi

Liste adları izleyicinin sorununu söyler, kategori harfini değil. Başlangıç seti:

| Oynatma listesi | Kategori | İlk videolar | Sıra mantığı |
|---|---|---|---|
| **Buradan Başla: İşte Yapay Zekâyı Doğru Kullanmak** | B | KM-004 → KM-001 → KM-010 | Sıralı seri; hiç kullanmamış kişiden günlük kullanıma |
| **Excel ve Rapor İşleri: Yarı Sürede** | G | KM-002 → KM-006 | Sorundan çözüme; yeni Excel videoları buraya |
| **Sunum, E-posta, Yazışma** | G | KM-005, KM-009 | Bağımsız görevler |
| **Hangi Araç? Türkçe Testler** | K | KM-003 | En yeni üstte |
| **Mesleğine Göre Yapay Zekâ** | M | KM-007 | Meslek adıyla; talep geldikçe büyür |
| **Kariyer: CV, Mülakat, Ek Gelir** | P | KM-008 | Bağımsız |
| **Küçük İşletme ve E-ticaret: Tek Kişilik Ekip İçin** | İ | KM-011 (Aşama 2a'da açılır) | İş türüne göre: ürün metni, müşteri yazışması, teklif |

Kurallar:
- Her video **tam bir** ana listeye girer (ikincil listeye de eklenebilir).
- **Açıklamadaki ve sabitlenmiş yorumdaki** video bağlantıları oynatma listesi parametresiyle (`&list=…`) verilir ki bir sonraki video otomatik sırada olsun. Bitiş ekranı için böyle bir ayar yoktur; oradaki seçim aşağıda.
- Tek videolu liste kanal sayfasında gösterilmez; ikinci video gelince raf olarak eklenir.
- "Buradan Başla" listesi resmî seri olarak işaretlenebiliyorsa işaretle (oynatma listesi ayarları → seri seçeneği; mevcutsa).
- Liste açıklamasının ilk cümlesi kime ve hangi sonuç için olduğunu söyler: "Excel'de saatler süren işleri yapay zekâyla kısaltmak isteyenler için; her videoda süre ölçümü ve kopyalanabilir prompt var."

### Oturum uzatma: bitiş ekranı + sabitlenmiş yorum + sözlü geçiş

1. **Sözlü geçiş (en etkilisi) [Yaygın gözlem].** Prompt gösterildikten sonra, videonun **son sesli cümlesi** olarak bir sonraki videoyu tek cümleyle ve nedeniyle söyle; vedalaşma cümlesi yoktur (yer ve sıra kuralı: 01 belgesi 8.2 ve 8.5). Örnek: "Bu tabloyu yaptık; formülleri de aynı yöntemle yazdırmak istersen ekrandaki video tam onu yapıyor." Cümle biterken bitiş ekranı açık olsun. (CTA metinleri: 01 belgesi §8.2.)
2. **Bitiş ekranı.** **[Resmî — sayfada teyit et]** Videonun son 5–20 saniyesine eklenir ([Add end screens](https://support.google.com/youtube/answer/6388789)). Öğe olarak ya **belirli bir video** ya da **bir oynatma listesi** seçilir; video öğesini "liste içinden" açtırmanın ayarı yoktur. Varsayılan düzen: 1 belirli video (sözlü geçişte adı geçen "sonraki adım") + abone düğmesi. Oynatma listesi öğesinin daha çok oturum üretip üretmediği B4'te FT7 olarak test edilir. "İzleyici için en iyisi" seçeneğini ikinci öğe olarak ancak 15+ video olduğunda ekle; öncesinde sistemin seçeceği anlamlı bir aday yok. Öğeler ekrandaki içeriğin üstüne binmesin diye son 15 saniyenin görsel şablonunu sabit tut.
3. **Sabitlenmiş yorum.** Her uzun videoda aynı üç bloklu kalıp (prompt, sıradaki adım, soru):
   ```
   Videodaki prompt (kopyala-yapıştır): ↓
   [prompt metni]

   Sıradaki adım: [sonraki video başlığı] → [bağlantı, &list= parametreli]

   [Videoda sorulan yorum sorusu, aynı kelimelerle; ör. "İşinde en çok vaktini alan yazı işi hangisi? Sıradaki videoları buradaki cevaplara bakarak seçeceğim."]
   ```
   Aşama 1'de "sıradaki adım" bloğunun altına tek satır eklenebilir: "Bütün prompt'lar tek dosyada: [açık bağlantı]". Aşama 2a'dan itibaren bu satır kayıt formuna gider: "Bütün prompt'lar tek dosyada, yenileri e-postayla: [bağlantı]" (B7). Prompt'un yorumda olması tutma grafiğindeki "geri sarma" ihtiyacını karşılar ve yorum bölümüne inme nedenidir. Bu kalıp Shorts'ta kullanılmaz (A10).
4. **Kartlar.** Yalnızca videoda başka bir videoya sözlü atıf yapılan anda ("bunu şu videoda ayrıntılı gösterdim"). Sebepsiz kart ekleme.
5. **Ölçüm.** Video → Analytics → Etkileşim → bitiş ekranı öğesi tıklama oranı. Kanalın alt üçte birinde kalan videolarda önce sözlü geçişin varlığını ve son sesli cümle biterken bitiş ekranının açık olup olmadığını kontrol et.

## B4. İçerik test sistemi

### Başlık/kapak testi — YouTube Studio'nun yerleşik özelliği

Güncel durum (2026-11 itibarıyla, arama sonuçlarındaki resmî sayfa alıntılarına göre):

- **[Resmî]** Studio'da videoya **en fazla 3 başlık ve kapak** varyantı eklenip test edilebiliyor; test bitince **en yüksek izlenme süresini** getiren başlık ya da başlık+kapak kombinasyonu tüm izleyicilere gösteriliyor. Özellik yalnızca **bilgisayarda** Studio üzerinden kullanılabiliyor. Kaynak: [A/B test titles & thumbnails](https://support.google.com/youtube/answer/16391400).
- **[Resmî]** Test sürerken videonun başlığı ya da kapağı elle değiştirilirse **test kendiliğinden durur** ve yeniden başlatılması gerekir (aynı sayfa). Sonuç: testli videoya B5'teki paket müdahalesi yapılmaz.
- **[Resmî]** Test dışı kalanlar: çocuklara özel olarak işaretlenmiş, yetişkin kitleye ayarlanmış ve gizli videolar; Shorts da desteklenmiyor. Kaynak: [Test & compare thumbnails](https://support.google.com/youtube/answer/13861714). İkincil kaynaklar bitmemiş prömiyerleri ve planlı canlı yayınları da sayıyor; liste dışı videoların durumu belirsiz.
- **Sonuç nasıl okunur:** Studio sonucu CTR olarak değil, varyant başına **izlenme süresi payı** olarak verir. Kazananın izlenme süresine göre seçilmesi Kısa Mesai'nin lehine: yalnızca tıklatıp izletmeyen varyantın kazanma ihtimali düşer. Ama izlenme süresi tıklama sayısı × izleme süresidir; çok tıklanan varyant kısa izlense de kazanabilir. Bu yüzden kazanan varyantın tutmasını ayrıca kontrol et.
- **Teyit edilemeyenler:** Uygunluk koşulu (ikincil kaynaklar çelişiyor: bir kısmı "gelişmiş özellikler" erişimi yeterli diyor, bir kısmı Ortak Programı şartı olduğunu yazıyor); testin azami süresi (ikincil kaynaklar iki haftaya kadar sürebildiğini, varyantlar arası fark küçükse testin uzadığını yazıyor); sonuç etiketlerinin Türkçe adları. Video ayrıntıları sayfasında kapak/başlık alanında test seçeneği görünüyorsa erişimin vardır; görünmüyorsa Studio → Ayarlar → Kanal → Özellik uygunluğu sayfasına bak.

**Kısa Mesai test kuralları:**

1. Test başına **tek değişken**. Dönüşüm çifti kalıbı sabit olduğu için test edilecek eksenler bellidir (örnekler süre çiftli bir G videosu içindir):

| Eksen | Varyant A | Varyant B |
|---|---|---|
| Kapaktaki rakam çerçevesi | "3 sa → 12 dk" | "%93 daha kısa" ya da yalnızca "12 dk" |
| Kapaktaki görev görseli | Bitmiş çıktı (tablo/sunum) | Dağınık "önce" hali |
| Başlıkta özne | Görev başta ("3 Saatlik Excel İşini…") | Araç başta ("ChatGPT ile Excel…") |
| Başlıkta çerçeve | Sonuç ("…10 Dakikada Bitirmek") | Deney ("…Denedim: Gerçekten Kısalıyor mu?") |

   Rakamlar çekimde ölçülen gerçek değerlerdir; test için rakam uydurulmaz.
2. **Yerleşik test ne zaman açılır:** Aşama 1'de açılmaz. Aşama 2a'dan itibaren yalnızca şu koşulda: son 5 videonun 7 günlük gösterim medyanı varyant başına en az 1.000 gösterim düşecek kadar yüksek (2 varyant için 2.000; tahmini çalışma kuralı). Koşul sağlanıyorsa 2 varyant kullan (3 değil — gösterimi üçe bölmek sonucu geciktirir). Yerleşik test, aşağıdaki "aynı anda 1 paket testi" sınırından **muaftır**: her test kendi videosunun içinde, aynı dönemde ve aynı kitlede yürür; videolar birbirini etkilemez.
3. **Testli videonun kaydı:** Video kartına "test sürüyor (E/H)" ve "test bitiş tarihi" yaz. Test sürerken videonun CTR'si iki varyantın karışımıdır; 7. gün CTR hücresine "test" yaz ve o değeri kanal medyanına **katma**. Test bitince kazanan paketle geçen ilk 7 günün kaynak bazında CTR'sini "test sonrası CTR" olarak ayrı yaz; bu değer videonun yaşı farklı olduğu için yalnızca başka "test sonrası" değerlerle kıyaslanır. Tutma ve AVD testli videoda da normal okunur.
4. Özellik erişilemezse ya da gösterim koşulu sağlanmıyorsa **elle sıralı test:** yalnızca yayından en az 7 gün geçmiş ve gösterimi yataylaşmış videoda; tek değişken değiştir; değişiklikten önceki ve sonraki 7 günü **aynı trafik kaynağında** CTR ve AVD ile kıyasla; her iki dönemde de o kaynakta en az 1.000 gösterim (tahmini) yoksa sonucu "okunmaz" yaz. Sıralı test, dönemler arası farklardan (hafta sonu, gündem) etkilenir; sonucu "zayıf kanıt" olarak kaydet. Aynı anda en fazla **1 elle paket testi** yürüt.
5. **Kural olma şartı:** Bir eksen **kazananı belli olan 3 testte** aynı yönde sonuç verirse kanal kuralı olur ve 01 belgesindeki başlık/kapak kurallarına eklenir. Sonuçsuz biten testler sayılmaz, tekrar edilir de sayılmaz; yalnızca "sonuçsuz" diye kaydedilir. Kazananı belli 3 testte karışık sonuç → eksen önemli değil, bırak. Gösterim düşük kaldıkça hiçbir eksen kurala dönüşmeyebilir; bu durumda kapak kalıbı olduğu gibi kalır ve çaba format testlerine kayar.

### Format testi

Yerleşik araç yok; test birimi videodur.

- **Bir seferde tek değişken**, en az **3 video** dene, aynı kategoride ve benzer rolde (arama/öneri) kontrol videolarıyla kıyasla. 1 videoyla karar verilmez; konu etkisi format etkisini bastırır.
- Sıradaki format hipotezleri (öneri). Kodlar "FT" ile başlar; 01 belgesindeki F1–F16 başlık formülleriyle karışmasın:

| # | Değişken | Kontrol | Deneme | Bakılacak metrik |
|---|---|---|---|---|
| FT1 | Açılış | Görev + elle süre (H1) | Sonucu önce göster (H2) | 0:30 tutma |
| FT2 | Kronometre görünürlüğü | Sürekli ekranda | Yalnızca başta/sonda | Orta bölüm eğimi |
| FT3 | "Yapamadığı şey" konumu | Sonda | Ortada, karşılaştırmadan önce | Karşılaştırmaya ulaşma oranı |
| FT4 | Uzunluk | 8–10 dk | 12–14 dk | AVD (dakika) ve bitiş ekranı tıklaması |
| FT5 | Shorts türü (01 belgesi 4.4) | Önce/sonra | Tek ipucu | Kaydırmadan kalma; uzun videoya geçiş |
| FT6 | Shorts zamanlaması | İlk Shorts uzun videodan önce (salı) | İki Shorts da uzun videodan sonra (cuma, pazartesi) | Uzun videonun trafik kaynağında Shorts kaynaklı görüntüleme (7. gün) |
| FT7 | Bitiş ekranı öğesi | Belirli video | Oynatma listesi | Bitiş ekranı öğesi tıklama oranı; videodan sonra kanalda izlenen süre (ölçülebiliyorsa) |

  FT6, `sablonlar/performans-kaydi.md` §5.2'deki 1 numaralı açık sorunun kendisidir; sonuç oraya yazılır.
- Aynı anda en fazla 1 format testi + 1 elle paket testi yürüt. Daha fazlası hangi değişikliğin neyi etkilediğini okunmaz kılar. FT5–FT7 uzun videonun gövdesine dokunmadığı için FT1–FT4'ten biriyle aynı anda yürüyebilir, ama birbirleriyle aynı anda yürümez.

### Hipotez–kayıt şablonu

Her test için bir kart (performans kaydında §5.2'nin altına; §5.2'deki satır kartın özetidir):

```
Test no / başlangıç tarihi:
Tür: [paket-yerleşik | paket-elle | format]
Hipotez: "[değişiklik] yaparsam [metrik], [kıyas noktası]na göre [yön] olur, çünkü [neden]."
Değişken (tek):
Sabit tutulanlar:
Videolar (deneme):            Videolar (kontrol):
Birincil metrik:              İkincil metrik (yan etki kontrolü):
Asgari veri sağlandı mı (B5 eşikleri): [E/H — H ise sonuç "okunmaz"]
Karar kuralı (önceden yaz): "3 videonun en az 2'sinde … ise kabul."
Yerleşik testse — varyant başına izlenme süresi payı: A % …  B % …  (Studio'nun verdiği sonuç etiketi: …)
Yerleşik testse — test bitiş tarihi / kazanan varyantın 0:30 tutması:
Sonuç (rakamlarla):
Karar: [kural oldu | reddedildi | sonuçsuz — sayılmaz]
Nereye işlendi: [01 belgesi § …]
```

Örnek doldurulmuş hipotez: "Açılışta bitmiş tabloyu ilk 5 saniyede gösterirsem (H2), G kategorisi videolarında 0:30 tutması kanalın G medyanına göre yükselir, çünkü izleyici sonucun kendi işine benzediğini hemen görür." Karar kuralı: "3 G videosunun en az 2'sinde 0:30 tutması G medyanının üstünde ve AVD düşmemişse H2, G kategorisinin varsayılan açılışı olur." (G'de 5+ video olduğu için kategori medyanı kullanılabilir.)

### Kaç videoda karar verilir (çalışma kuralları, tahmini)

| Karar | Asgari veri |
|---|---|
| Tek videonun paketini değiştirmek | KM-006 ve sonrası; 7 gün + gösterim yataylaşmış + ilgili kaynakta asgari gösterim (B5) |
| Paket ekseni kanal kuralı olur | Kazananı belli 3 testte aynı yön |
| Format değişikliği kalıcı olur | 3 deneme videosu, 2/3 kuralı; her videoda asgari veri sağlanmış |
| Kategoriye ağırlık vermek | O kategoride 3+ video, 28'er günlük veri (bu yüzden karar Aşama 2b'de) |
| Kategoriyi durdurmak | 3+ video, hepsi kanalın alt üçte birinde **ve** yorum/arama teriminde talep izi yok |
| Karar tablosunda kategori medyanı kullanmak | O kategoride 5+ video |
| Kapak kalıbını toptan değiştirmek | 30+ video ve en az 5 videoda kazananı belli yerleşik test |

## B5. Performans optimizasyonu

### Kontrol rutini

| Zaman | Süre | Bakılan | Yapılabilecek müdahale |
|---|---|---|---|
| **1. saat** (perşembe) | 15 dk | **Metrik değil, teknik kontrol.** Video herkese açık mı; kapak telefonda okunuyor mu (koyu modda da); başlık kesiliyor mu; bölümler (chapter) çalışıyor mu; altyazı; bitiş ekranı; sabitlenmiş yorum; oynatma listesi; Shorts'lar zamanlandı mı. İlk yorumlara cevap. | Yalnızca hata düzeltme. Studio verisi bu aşamada gecikmeli ve çok küçük örneklem; CTR'ye bakıp karar verme. |
| **48 saat** (cumartesi) | 5 dk | Üç şey: gösterim geliyor mu (hangi kaynaktan), 0:30 tutması, tutma grafiğinde teknik soruna işaret eden basamak düşüş. Karta yalnızca gösterim ve 0:30 değeri yazılır. | **Karar noktası değil.** Müdahale yalnızca açık hata varsa: kapak mobilde okunmuyor, başlık videonun konusunu söylemiyor, ilk 30 sn'de ses/görüntü sorunu. |
| **7. gün** (perşembe, B8 içinde) | 10 dk | Planlanan birincil kaynağın gösterimi ve CTR'si; işaret noktaları; arama terimleri; bitiş ekranı tıklaması; yorumlardaki tekrar eden soru. | KM-001–005: yalnızca kaydet. KM-006+: asgari veri varsa karar tablosuna göre **tek** müdahale. Yerleşik test sürüyorsa pakete dokunma. |
| **28. gün** (perşembe, B8 içinde) | 8 dk | Nihai rakamlar; planlanan ↔ gerçekleşen birincil kaynak; kazanılan abone; videodan çıkan ders (tek cümle). 7. günde asgari veriye ulaşmamış metrikler burada okunur. | Paket yenileme adayı listesine alma ya da "tamam" işaretleme. Arama videosuysa açıklama/başlıkta gerçek arama terimlerine göre ince ayar. |

### Kıyas merdiveni: "düşük" ve "yüksek" neye göre?

Sıfırdan başlayan kanalda kıyas noktası video sayısıyla birlikte oluşur. Hangi basamakta olduğunu bilmeden karar tablosunu kullanma.

| Basamak | Ne zaman | Kıyas noktası | İzin verilen müdahale |
|---|---|---|---|
| **1** | KM-001–005 | Yok. Yalnızca kaydet. | Yalnızca açık hata (kontrol rutinindeki 48 saat satırı). |
| **2** | KM-006'dan itibaren | **Kanal geneli + aynı kaynak + aynı yaş:** o güne kadar 7. günü (ya da 28. günü) dolmuş son 10 videonun (10'dan azsa hepsinin) dağılımı. Kategori ayrımı yapılmaz. | Karar tablosu, asgari veri şartıyla. |
| **3** | Bir kategoride 5+ video olunca (B1'deki sırayla en erken G'de, KM-016 ile; B'de Aşama 2b içinde) | O kategori için **kategori + aynı kaynak** medyanı. Diğer kategoriler 2. basamakta kalır. | Aynı. |

**İşlemsel tanımlar:**

- **Düşük** = değer, kıyas kümesinin en alt üçte birinde. (6–8 videoluk kümede en düşük iki değerden biri; 9–10 videoluk kümede en düşük üç değerden biri.) **Yüksek** = en üst üçte bir. Arası **normal**.
- "Belirgin" sözcüğü bu belgede kullanılmaz; ya alt üçte birdedir ya değildir.
- 7. günde "düşük" çıkan ama asgari verisi olmayan metrik için müdahale edilmez; 28. günde yeniden okunur. 28. günde de asgari veri yoksa hücreye "okunmaz" yazılır.

**Okuma için asgari veri (tahmini çalışma kuralı; KM-010'dan sonra kanalın gerçek hacmine göre güncelle):**

| Kod | Metrik | Asgari veri | Gerekçe |
|---|---|---|---|
| **V1** | Kaynak bazında CTR | O kaynakta en az 1.000 gösterim | %5 CTR'de 50 tıklama; altında bir puanlık fark birkaç tıklamadır |
| **V2** | Tutma işaret noktaları, AVD | En az 100 görüntüleme **ve** Studio tutma grafiğini gösteriyor | 100'ün altında tek izleyici eğriyi yüzde bir puandan fazla oynatır |
| **V3** | Bitiş ekranı tıklama oranı; 1000 görüntüleme başına abone | En az 300 görüntüleme | Olay seyrek; küçük sayıda tek tıklama oranı ikiye katlar |
| **V4** | Shorts kaydırmadan kalma oranı | En az 500 Shorts görüntülemesi | Akış dağıtımı ilk yüzlerde çok oynak **[Yaygın gözlem]** |

İlk 10 videonun çoğu 7. günde bu eşiklere ulaşmıyorsa eşikleri düşürme; okuma noktasını 28. güne kaydır ve Aşama 1'in odak metriklerini (0:30 tutma, arama terimleri) kullanmaya devam et.

### Karar tablosu: belirti → olası neden → müdahale

"Düşük/yüksek/normal" yukarıdaki tanımla okunur. Tablo KM-006'dan itibaren kullanılır. Yerleşik test süren videoda paket müdahalesi yapılmaz.

| Belirti | Asgari veri | Olası neden | Önce kontrol et | Müdahale |
|---|---|---|---|---|
| **Gösterim düşük**, CTR ve tutma normal | V2 (CTR için V1 yoksa "okunmaz" say) | Konuya talep az ya da sistem henüz kitle bulamadı | Arama terimleri: sorgu var mı? Kaynak dağılımı: yalnızca abone mi? | Videonun paketine dokunma. Videodan tek bir önce/sonra anını Shorts olarak kes, ilgili video bağlantısını ekle (yoksa A10'daki yedek yol); 7 gün sonra uzun videonun trafik kaynağında Shorts kaynaklı görüntüleme var mı bak. Aynı konunun daha çok aranan çerçevesini fikir havuzuna yaz (ör. meslek adı yerine görev adı). |
| **Gösterim düşük**, arama videosu, terim listesi boş | 28. gün | Başlık izleyicinin yazdığı sorguyla eşleşmiyor | YouTube arama kutusunda otomatik tamamlamaya bak | Başlığı izleyicinin yazdığı biçime çek; açıklamanın ilk iki cümlesine sorguyu doğal biçimde yaz. |
| **CTR düştü, gösterim arttı** | — | Video daha geniş, seni tanımayan kitleye açılıyor (A2) | Artan gösterim Göz atma/Önerilen'den mi? | **Dokunma.** Tabloya "genişleme" notu düş. |
| **Gösterim var, CTR düşük** (Göz atma/Önerilen) | V1 | Paket soğuk kitleye bir şey söylemiyor | Kapak telefonda küçük boyutta okunuyor mu? Görev ilk bakışta anlaşılıyor mu? | Koşulu sağlıyorsa yerleşik test; yoksa 7. günden sonra tek değişkenli elle değişiklik (önce kapak, sonra başlık). |
| **CTR düşük** (arama) | V1 | Arama sonuçlarında rakiplerden ayrışmıyor | Aynı sorguyu ara, sonuç sayfasının ekran görüntüsünü al | Kapakta süre farkını büyüt; başlığa ayırt edici öğe ekle ("Türkçe", "formül bilmeden"). |
| **Arama payı yüksek, AVD düşük** | V2 | Arayan kişi cevabı geç buluyor | Aranan şey videoda hangi dakikada gösteriliyor? | Sonraki arama videolarında aranan cevabı ilk 30 saniyeye taşı. Mevcut videoda bölüm (chapter) başlıklarını sorgu diliyle yeniden yaz ("Formülü yazdırma", "Hata verirse") ki arayan kişi doğru yere atlasın. |
| **CTR yüksek, ilk 30 sn kaybı yüksek** | V1 + V2 | Paket–açılış uyumsuzluğu | Başlıktaki vaat ilk 15 saniyede söyleniyor/gösteriliyor mu? | Öncelik: sonraki videolarda açılışı düzelt. Mevcut videoda paketi videonun gerçekten verdiği şeye yaklaştır. Studio düzenleyicide baştan kırpma mümkünse giriş boşluğunu kes. |
| **CTR normal, ilk 30 sn kaybı yüksek** | V2 | Yavaş giriş | Selamlama, kanal tanıtımı, "bu videoda şunları göreceğiz" listesi var mı? | Sonraki videoda görev + elle süre ilk cümle; sonuç görüntüsü ilk 5 saniye. Format testi FT1. |
| **Ortada basamak düşüş** | V2 | Belirli bir an | O saniyeyi izle: bekleme, tekrar, konu dışı açıklama, erken CTA? | Mevcut videoda o noktaya bölüm (chapter) başlığı ekle ki izleyici atlayıp devam etsin. Sonraki videolar için 01 belgesi §7.5 "sıkılma noktası" kontrolüne madde ekle. |
| **Ortada sürekli dik eğim** | V2 | Tempo ya da değer yoğunluğu düşük | Adım başına süre; yapay zekânın cevap yazmasını bekleme anları hızlandırılmış mı? | Kurgu kuralı: bekleme anları hızlandırılır, her 60–90 sn'de (tahmini) bir ara sonuç gösterilir. FT2/FT4 testi. |
| **Tutma normal ya da yüksek, bitiş ekranı tıklaması düşük** | V3 | Veda sinyali erken; önerilen video alakasız | Bitiş ekranı açılmadan "bu kadardı" deniyor mu? | Bitiş ekranındaki videoyu daha yakın bir "sonraki adım"la değiştir (yayın sonrası değiştirilebilir). Sonraki videolarda sözlü geçiş. |
| **Görüntüleme normal ya da yüksek, 1000 görüntüleme başına abone düşük** | V3 | İzleyici tek seferlik çözüm aldı | Videoda seri vaadi var mı? | B7. Sabitlenmiş yoruma ve bitiş ekranına seri bağlantısı. |
| **Yeni izleyici geliyor, vekil göstergeler (A5) düz** | Aylık bakış; en az 10 video | Kanal seri olarak algılanmıyor | Son 5 video birbirine bağlı mı? | B3 seri mimarisi; aynı sorunun devam videosu. |
| **Shorts: kaydırma oranı yüksek** | V4 | İlk 1–2 saniye boş | İlk karede sonuç ya da süre farkı var mı? | İlk kareye "önce/sonra" görüntüsü ve ekran yazısı; giriş cümlesini at. |
| **Shorts izleniyor, uzun videoya geçiş yok** | V4 | Köprü yok | İlgili video bağlantısı eklendi mi? Yoksa tam başlık sözle ve yazıyla veriliyor mu? | Bağlantıyı ekle ya da yedek yolu uygula (A10); Shorts'u "tek adım"a indir, bütünü uzun videoda bırak. |
| **Her şey normal, taban yükselmiyor** | — | Video sayısı az; öğrenme döngüsü henüz kısa | Hangi aşamadasın? | Yayındaki videolara müdahale yok. B4'te sıradaki testi başlat; Aşama 2b'deysen kategori kararını ver. |

**Müdahale disiplini:** video başına aynı anda tek değişiklik; değişiklik tarihini video kartındaki değişiklik günlüğüne yaz; etkisini 7 gün sonra aynı kaynakta oku.

## B6. İzleyici etkileşimi

### Yorum stratejisi

- **Cevap kuralı:** İlk 30 videoda her gerçek yoruma cevap. Cevap bir soruyla ya da somut ek bilgiyle biter; "teşekkürler" tek başına cevap değildir.
- **Yorumu tetikleyen soru** videonun içinde ve sabitlenmiş yorumda aynıdır ve **cevabı kolay, kişisel, sayısal**dır: "Bu işi sen şu an kaç dakikada yapıyorsun?", "Mesleğin ne, en çok vakit alan işin hangisi?" Genel "ne düşünüyorsunuz" sorusu sorulmaz. (Metinler: 01 belgesi §8.3.)
- **Üç etiketle işle** (video kartındaki "Yorumlar" tablosuna; GÖREV olanlar ayrıca `fikir-havuzu.md` dosyasına; bu, senin tutacağın çalışma dosyasıdır ve bu depoda henüz yoktur: ilk GÖREV yorumunda `docs/` altında aç, satır başına tarih · kaynak · izleyici cümlesi · 01 belgesi Bölüm 1 filtre puanı yaz):

| Etiket | Örnek yorum | Ne yapılır |
|---|---|---|
| **GÖREV** | "Stok takibini de böyle yapabilir miyiz?" | Fikir havuzuna; kaç kişi istediğini say |
| **İTİRAZ** | "Bende böyle çıkmadı / yanlış hesapladı" | Cevapla, nedenini sor; tekrar ediyorsa "yapamadığı şey" bölümüne ya da ayrı videoya malzeme |
| **KANIT** | "Denedim, raporu 20 dakikada bitirdim" | Kalple işaretle; izin isteyerek topluluk gönderisinde/sonraki videoda ekran görüntüsü olarak kullan |

- **Kalp ve sabitleme:** En iyi GÖREV sorusunu geçici olarak sabitlemek yerine sabitlenmiş yorum kalıbını koru; iyi yorumları kalple işaretle (yorum sahibine bildirim gider).
- **Yapılmaz:** Yorum karşılığı çekiliş/vaat; kendi yorumuna sahte hesaptan cevap; olumsuz ama haklı yorumu silme.

### Topluluk gönderileri (Gönderiler sekmesi)

**Erişim:** Koşullar değişti ve teyit edilemedi; ikincil kaynakların bir kısmı abone eşiği kalmadığını ve "gelişmiş özellikler" erişiminin yettiğini yazıyor, bir kısmı farklı yazıyor. Kendi hesabında kontrol: Studio → Ayarlar → Kanal → Özellik uygunluğu; ve Studio'da "Oluştur → Gönderi oluştur" seçeneği görünüyor mu.

**Başlangıç koşulu:** Abonesi olmayan kanalda gönderi kimseye ulaşmaz. Sıra şöyle:

1. **Aşama 1:** Gönderi yok. Görev sorusu yalnızca sabitlenmiş yorumda ve videoda sorulur.
2. **Sonuç kartı** gönderisi, özellik erişilebilir olduğunda ve Aşama 2a başladığında başlar (ankete göre daha az etkileşim ister; bir görsel ve bir bağlantıdır).
3. **Anket**, art arda iki sonuç kartı gönderisi en az 20'şer etkileşim (beğeni + yorum; tahmini çalışma kuralı) aldıktan sonra başlar. Öncesinde aynı soru sabitlenmiş yorumda seçenekli sorulur: "Sıradaki test hangisi olsun: A) … B) … C) …?"

Haftada en fazla 2 gönderi, her birinin tek işi olsun:

| Gönderi türü | Gün | Örnek |
|---|---|---|
| **Görev anketi** | Çarşamba. Anket, **yaklaşık 3 hafta sonra** yayınlanacak videonun konusunu seçer (1 videoluk stok + 1 haftalık üretim + pay). | "Üç hafta sonraki videoda hangisini kronometreyle test edeyim? A) Toplantı notundan tutanak B) Müşteri şikâyetine cevap C) Aylık satış raporu D) Başka — yoruma yaz" |
| **Sonuç kartı** | Cuma (yayın günü +1) | Videonun karşılaştırma tablosunun tek görseli + prompt'un ilk satırı + video bağlantısı |
| **Elle süre sorusu** (ayda 1, anket yerine) | Çarşamba | "[görev]i elle kaç dakikada yapıyorsun?" → cevaplar sonraki videonun açılış cümlesine dayanak |

- Gönderide zamanı söyle ("üç hafta sonraki video"); izleyici sonucu ertesi hafta beklemesin.
- Anket sonucunu ilgili videoda **adıyla an**, ama oy sayısına uygun dille: oy azsa "Ankette bu çıktı" de; "en çok bunu istediniz" cümlesi ancak oy sayısı ekranda gösterilebilecek kadar anlamlıysa (ve sayıyla birlikte) kullanılır. Beş oyu "en çok istenen" diye sunmak kanalın abartısız tonuna aykırıdır.

### İzleyici görevini videoya çevirme döngüsü

```
1. TOPLA   → yorum (GÖREV etiketi), anket, arama terimleri, e-posta cevapları
2. PUANLA  → 01 belgesi §1 fikir filtresi; ek ölçüt: kaç ayrı kişi istedi
3. DUYUR   → topluluk gönderisi ya da sabitlenmiş yorum: "Bunu çekiyorum, [tarih] dolayında yayında"
4. ÇEK     → videonun açılışında kaynağı söyle: "Bu görev yorumlardan geldi: …"
             (isim anmak için yorum sahibinden izin; yoksa "bir izleyici")
5. KAPAT   → orijinal yoruma video bağlantısıyla cevap yaz
6. KAYDET  → video kartında "fikir kaynağı = izleyici"
```

Aşama 2b'den itibaren hedef: her 4 videodan en az 1'i bu döngüden çıksın (tahmini oran; izleyici kaynaklı videoların performansını ayrı izle ve orana göre ayarla). Müşteri verisi içeren görevlerde gerçek dosya istenmez; görev anonimleştirilmiş örnek veriyle yeniden kurulur.

## B7. İzleyiciyi aboneye ve geri gelen izleyiciye çevirme

### Abone olma nedeni

İzleyici videoya değil, **gelecekteki videolara** abone olur. Kanalın abone gerekçesi tek cümle ve her yerde aynı:

> "Her hafta gerçek bir iş görevini kronometreyle test ediyorum: ne kadar kısalıyor, nerede yanılıyor, hangi prompt'la."

Bu cümle kanal açıklamasının ilk satırı, fragmanın son cümlesi ve abone CTA'sının gerekçesidir. Abone CTA'sı videoda **değer teslim edildikten sonra** gelir ve varsayılan olarak yalnızca görseldir (alt bant + bitiş ekranı düğmesi). Sözlü hâli yalnızca yorum sorusu kullanılmayan videoda, bir sonraki somut görevle birlikte söylenir: "Haftaya [görev]i test ediyorum; abone olursan Abonelikler sekmende görürsün." (Kural ve metin varyantları: 01 belgesi §8.1.)

**Ölçüm:** Video → Analytics → Kitle → "Aboneler" (bu videodan kazanılan). Kıyas için "1000 görüntüleme başına abone"yi hesapla; asgari veri V3, kıyas B5 merdivenine göre.

### Seri vaadi

- Her video bir serinin parçası olarak sunulur: "Excel serisinin 2. videosu" ifadesi başlıkta değil, videonun ilk dakikasında ve açıklamada geçer (başlıkta bölüm numarası soğuk izleyiciyi uzaklaştırabilir **[Yaygın gözlem]**).
- Her videonun sonunda **bir sonraki videonun görevi** söylenir; henüz yayınlanmadıysa tarihle: "Bir sonraki video: [görev]. Perşembe yayında."
- "Mesleğine Göre" serisinde sıradaki mesleği izleyici belirler (sabitlenmiş yorum sorusu; koşul sağlanınca anket) — abone olmanın somut nedeni: "senin mesleğin sıraya girsin."

### Kanal sayfası

| Öğe | İçerik |
|---|---|
| **Banner** | Vaat + ritim: "Aynı işi yarı sürede bitir · Her perşembe yeni görev testi". Lacivert + sarı. Mobil güvenli alanda okunur olmalı. |
| **Kanal açıklaması (ilk 2 satır)** | Abone gerekçesi cümlesi + kime olduğu ("Excel, e-posta, rapor ve sunumla çalışan; kod yazmayan herkes için"). |
| **Fragman (abone olmayanlar için)** | 45–60 sn (tahmini). Yapı: (1) tek bir görevin elle süresi → (2) kronometreli hızlı kesit → (3) karşılaştırma ekranı → (4) "yapamadığı şeyi de gösteriyorum" → (5) abone gerekçesi cümlesi. Selamlama ve özgeçmiş yok. İlk 5 video yayınlanınca gerçek kesitlerden kurulur; öncesinde KM-001 fragman yerine konur. |
| **Öne çıkan video (aboneler için)** | En yeni video (otomatik) ya da "Buradan Başla" listesi. |
| **Raflar (sırayla)** | 1) Buradan Başla, 2) Excel ve Rapor İşleri, 3) Mesleğine Göre, 4) Hangi Araç?, 5) Küçük İşletme ve E-ticaret, 6) Shorts. En az 2 videosu olan liste raf olur. |
| **Bağlantılar** | Tek bağlantı. Aşama 1: prompt dosyasının açık bağlantısı. Aşama 2a'dan itibaren: prompt dosyası kayıt sayfası. |

Fragman ve öne çıkan video ayarı: Studio → Özelleştirme → Ana sayfa sekmesi **[Resmî — sayfada teyit et]** ([Customize channel layout](https://support.google.com/youtube/answer/3219384)).

### Ücretsiz prompt dosyası ve e-posta listesi

**Neden:** YouTube aboneliği izleyiciye ulaşmayı garanti etmez; e-posta listesi platformdan bağımsız, doğrudan bir kanaldır ve en ilgili izleyiciyi görünür kılar.

**Ne zaman:** İki adımda açılır.

| Aşama | Dosya | Kayıt formu | Bağlantının gittiği yer | Ölçülen |
|---|---|---|---|---|
| **Aşama 1 (KM-001–010)** | Var; ilk videodan itibaren. Her videoyla büyür. | **Yok.** E-posta istenmez. | Dosyanın kendisi (salt okunur, açık bağlantı) | Prompt dosyası tıklaması (kısa bağlantı ile, video bazında) |
| **Aşama 2a'dan itibaren** | Aynı dosya | Açılır | Kayıt sayfası; dosyanın açık bağlantısı eski videolarda çalışmaya devam eder | Tıklama + e-posta kaydı |

Gerekçe: ilk 10 videoda trafik azdır ve form + otomasyon + hukuki hazırlık, formatı kanıtlama işinden zaman çalar; dosyaya gelen tıklama sayısı ise formun açılmaya değip değmeyeceğini önceden gösterir.

- **Mıknatıs:** "Kısa Mesai Prompt Dosyası" — videolarda kullanılan prompt'ların tek dosyada, görev adına göre dizilmiş, kopyalanabilir hali. İlk sürüm: KM-001'in prompt'ları + "boşlukları doldur" kalıbı.
- **Videodaki prompt her aşamada açıklamada ve sabitlenmiş yorumda açık durur.** Kayıt formu açıldıktan sonra da dosya, videodaki prompt'u e-postanın arkasına saklamaz; kayıt olana "hepsi bir arada + yenileri e-postayla" verir. Aksi, kanalın "tık tuzağı yok" tonuyla çelişir.
- **Kurulum (Aşama 2a, asgari):** tek alanlı kayıt formu (yalnızca e-posta) → otomatik teslim e-postası (dosya bağlantısı) → her yeni videoda kısa e-posta. Araç seçimi `03` iş akışı belgesinin konusu; burada koşul: çift onay (double opt-in) ve tek tıkla abonelikten çıkma desteklesin.
- **Hukuki not:** Türkiye'de e-posta adresi toplamak KVKK kapsamında aydınlatma ve açık rıza gerektirir; ticari nitelikli e-posta gönderimi için İleti Yönetim Sistemi (İYS) yükümlülüğü doğabilir. Kendi durumun (şahıs/şirket, gönderi niteliği) için yayına almadan önce bir uzmana ya da resmî kaynaklara danış; bu belge hukuki görüş değildir.
- **Yerleşim (her iki aşamada aynı yerler; yalnızca bağlantının hedefi değişir):** açıklamanın ilk 3 satırından biri; sabitlenmiş yorumun "sıradaki adım" bloğunun altındaki satır (B3); videoda prompt ekranda gösterilirken tek cümle (01 belgesi §8.4); kanal sayfası bağlantısı.
- **Haftalık e-posta kalıbı (Aşama 2a'dan itibaren; cumartesi, 5 satır):** bu haftanın görevi ve ölçülen süre farkı → prompt → "yapamadığı şey" tek cümle → video bağlantısı → "Bu e-postayı yanıtla: en çok vakit alan işin ne?" (B6 döngüsünün dördüncü kaynağı).

## B8. Haftalık 30 dakikalık analiz rutini ve takip kaydı

### Rutin (her perşembe, kronometreyle — fazlası analiz değil oyalanmadır)

Perşembe yayın günüdür; bir önceki video tam 7 günlük, dört önceki video tam 28 günlüktür. Böylece "aynı yaşta kıyasla" kuralı kendiliğinden sağlanır. Yayın bir hafta kayarsa analiz de kayar; kıyas yine "yayın + 7" ve "yayın + 28" üzerinden yapılır.

| Dk | Adım | Studio'da yer | Çıktı |
|---|---|---|---|
| 0–3 | **Kanal nabzı:** son 7 gün ↔ önceki 7 gün; görüntüleme, izlenme süresi, abone. **Yalnızca bak.** | Analytics → Genel Bakış | Yazılacak bir şey yok; olağandışı bir sıçrama/düşüş varsa hangi videodan geldiğini not et |
| 3–13 | **7. günü dolan video:** özet tablo satırı; planlanan birincil kaynağın gösterimi + CTR'si; işaret noktaları; bitiş ekranı tıklaması. | Video → Analytics → Erişim; Etkileşim | Performans kaydı §1 satırı + video kartı; B5 merdivenine göre en fazla 1 müdahale |
| 13–21 | **28. günü dolan video:** nihai rakamlar; en büyük üç kaynağın payı; gerçekleşen birincil kaynak; tek cümle ders. | Aynı | §2 satırı + kartın 28. gün sütunu; kart kapatılır |
| 21–26 | **Arama terimleri + yorumlar:** yeni sorgular ve GÖREV yorumları. | Erişim → YouTube araması; Yorumlar | `fikir-havuzu.md` dosyasına en fazla 3 yeni satır |
| 26–28 | **Test kaydı:** süren testin durumu; biten varsa karar. | Video ayrıntıları → test sonucu; test kartı | Test kartı güncellenir |
| 28–30 | **Haftanın tek kararı:** bir sonraki videoda değiştireceğim tek şey. | — | Video kartındaki "Çıkarım" tablosu; bir sonraki perşembe ilk okunacak şey |

**Asgari doldurma kuralı (rutini 30 dakikada tutan şey):** Performans kaydındaki her hücre her kontrolde doldurulmaz.

- **48 saat sütunu:** yalnızca gösterim ve 30. saniyede kalan %. Diğer hücreler boş kalır.
- **7. gün:** özet tablo (§1) satırı + kartta planlanan birincil kaynağın gösterimi ve CTR'si + üç işaret noktası (kronometre, "yapamadığı şey", karşılaştırma). Trafik kaynakları tablosunun 48 saat ve 7 gün sütunları doldurulmaz.
- **28. gün:** kartın 28. gün sütunu + trafik kaynaklarında yalnızca payı en yüksek üç kaynak (kalanı boş) + en çok getiren 3 arama terimi.
- Beğeni, paylaşım, kaybedilen abone yalnızca 28. günde yazılır.

**Ayda bir (ek 20 dk; performans kaydı §5.3):** Kitle sekmesinden yeni / ara sıra / düzenli izleyici sayıları (A5; ilk 6 ayda düzenli sütununa 0 yazmak normaldir); üç vekil göstergenin aylık seyri; kategori medyanları (3'ten az videolu kategori yorumlanmaz); paket yenileme adayları (tutması üst üçte birde, CTR'si alt üçte birde olan videolar); B5'teki asgari veri eşiklerinin kanalın gerçek hacmine göre gözden geçirilmesi.

### Takip kaydı

**Tek şablon: `sablonlar/performans-kaydi.md`.** Sütunlar, video kartı, üretim süresi bütçesi, diğer platformlar ve okuma kuralları oradadır; bu belge ayrı bir tablo tanımlamaz. Bu belgenin gerektirdiği ve o şablonda bulunan ek alanlar:

| Alan | Şablonda yeri | Bu belgede kullanıldığı yer |
|---|---|---|
| Rol (arama / öneri / köprü / merkez) | Video kartı, kimlik tablosu | B3 |
| Planlanan birincil kaynak · hedef sorgu | Video kartı, kimlik tablosu | B3, B5 |
| Gerçekleşen birincil kaynak (28. gün) | Video kartı, kimlik tablosu | B3 |
| Oynatma listesi · bitiş ekranı öğesi ve hedefi | Video kartı, kimlik tablosu | B3, FT7 |
| Yerleşik test sürüyor mu (E/H) · bitiş tarihi · test sonrası CTR | Video kartı, kimlik tablosu | B4 |
| Fikir kaynağı (plan / arama terimi / izleyici) | Video kartı, kimlik tablosu | B6 |
| Kronometrenin başladığı an · karşılaştırmanın başladığı an (zaman, %) | Video kartı, tutma grafiği | A4 |
| Abonelik akışı + bildirim kaynaklı görüntüleme · Önerilen'de kendi videolarından gelen pay | §5.3 aylık bakış | A5, B1 |
| Yeni / ara sıra / düzenli izleyici (aylık) | §5.3 aylık bakış | A5 |
| Hipotez kartı (B4) | §5.2'nin altı | B4 |

Kıyas kuralları iki belgede aynıdır: KM-001–005 yalnızca kayıt, KM-006'dan itibaren kanal medyanı, aynı yaşta kıyas, az gösterimde oran okunmaz.

## B9. Yaygın büyüme yanılgıları ve gerçekte olan

"Kısa Mesai'de karşılığı" sütunundaki kurallar, ortadaki iddianın etiketine bağlı değildir; iddia teyit edilemese de kural geçerlidir.

| Yanılgı | Gerçekte olan | Kısa Mesai'de karşılığı |
|---|---|---|
| **"Etiketler keşfi belirler."** | **[Resmî — sayfada teyit et]** YouTube Yardım, etiketlerin keşifte asgari rol oynadığını, esas olarak yaygın yanlış yazımlar için yararlı olduğunu söylüyor ([Add tags to videos](https://support.google.com/youtube/answer/146402)). Başlık, kapak ve açıklama daha önemli. | 3–5 etiket: yazım varyantları ("yapay zeka", "chat gpt"). Etikete 1 dakikadan fazla harcama. |
| **"Doğru saatte yüklemezsen video ölür."** | **[Resmî — sayfada teyit et]** [Performans SSS'si](https://support.google.com/youtube/answer/141805), yayın saatiyle ilgili soruda, yayın saatinin videonun uzun vadeli performansını etkilediğinin bilinmediğini söylüyor. **[Yaygın gözlem]** Saat en fazla ilk saatlerdeki izlenme hızını değiştirir. | Sabit gün/saat senin ritmin ve analiz günün içindir. Saat denemeleriyle vakit harcama. |
| **"Algoritma beni cezalandırdı / gölge yasak."** | **[Resmî]** Sistem videoyu kitleye tanıtmaz, kitle için bulur (141805). **[Yaygın gözlem]** Düşüş çoğunlukla şunlardan biridir: konuya ilgi az, paket gösterildiği kitleye uymadı, tutma zayıf, ya da geçen haftaki video olağandışı iyiydi ve kıyas bozuk. Görüntüleme dağılımı çarpıktır; çoğu video kanal ortalamasının altında kalır, birkaçı ortalamayı çeker. | "Düştü" demeden önce karar tablosundaki satırı bul. Kıyası medyanla yap. |
| **"Ara verirsen kanal sıfırlanır."** | **[Resmî — sayfada teyit et]** [Performans SSS'si](https://support.google.com/youtube/answer/141805), ara vermeyle ilgili soruda, ara veren binlerce kanalda ara süresi ile görüntüleme değişimi arasında ilişki bulunmadığını söylüyor. **[Yaygın gözlem]** Ara sonrası düşüş olursa nedeni izleyicinin alışkanlığının ve ilgisinin değişmesidir. | Hasta/izin haftasında takvim kayar; telafi videosu yok (B2). |
| **"Daha sık yükle, daha hızlı büyü."** | **[YouTube'a atfedilen — kaynak bulunamadı]** Sistemin sıklığı başlı başına ödüllendirmediği. **[Yaygın gözlem]** Sıklık yalnızca kalite korunuyorsa daha çok öğrenme fırsatı verir; zayıf videolar kanalı tanıyan izleyicinin tıklama alışkanlığını aşındırabilir. | Haftada 1 + Shorts. İkinci video ancak stok ≥ 4 ise. |
| **"İyi CTR şu yüzdedir."** | **[Resmî]** YouTube yalnızca dağılım bilgisi veriyor (kanalların yarısı %2–10 arası) ve CTR'nin içerik, kitle ve yüzeye göre değiştiğini söylüyor ([7628154](https://support.google.com/youtube/answer/7628154)). | Kıyas: aynı kaynak + aynı yaş + kanal dağılımı (B5 merdiveni). |
| **"Shorts aboneleri uzun videoyu büyütür."** | **[Yaygın gözlem]** Shorts ve uzun video izleyicileri büyük ölçüde ayrı davranır; köprü kurulmadıkça geçiş sınırlıdır. | Shorts = uzun videonun tek anı + ilgili video bağlantısı (ya da tam başlık). Shorts abone sayısını başarı ölçüsü sayma. |
| **"İlk saatler her şeyi belirler."** | **[Yaygın gözlem]** Eğitim/arama içeriğinde görüntülemenin önemli kısmı haftalar ve aylar içinde gelir; videolar sonradan da açılabilir. | 1. saat kontrolü teknik kontroldür. Karar 7. ve 28. günde. |
| **"Abone sayısı erişimi belirler."** | **[Resmî]** Abonelikler, sistemin kullandığı sinyallerden yalnızca biri olarak sayılıyor ([16533387](https://support.google.com/youtube/answer/16533387)). **[YouTube'a atfedilen — kaynak bulunamadı]** "Abone sayısı önerilerde belirleyici değildir" biçimindeki açık ifade. | Odak: A5'teki vekil göstergeler ve aylık ara sıra izleyen sayısı. |
| **"Başlık/kapak değiştirmek videoyu sıfırlar."** | **[Resmî — sayfada teyit et]** [Performans SSS'si](https://support.google.com/youtube/answer/141805), başlık/kapak değişikliğiyle ilgili soruda, değişikliğin kendisinin videoyu yeniden sıralatmadığını; performansın, izleyiciler yeni pakete farklı tepki verdiği için (iyi ya da kötü yönde) değişebileceğini ve işleyen pakete dokunmamayı önerdiğini söylüyor. | Değiştir, ama tek değişken ve kayıtla (B4, B5). İyi giden videonun paketine dokunma. |
| **"Açıklamaya anahtar kelime doldur."** | **[Resmî — sayfada teyit et]** Alakasız/tekrarlı anahtar kelime doldurma, YouTube'un spam ve yanıltıcı uygulamalar politikasına aykırı ([Spam, deceptive practices, & scams policies](https://support.google.com/youtube/answer/2801973)). | Açıklama şablonu: ilk 2 cümle doğal dille görev + sonuç; sonra prompt, bölümler, bağlantılar. |
| **"Beğeni ve yorum iste, algoritma sever."** | **[Resmî]** Beğeni/beğenmeme çok sayıda sinyalden biri; sistem memnuniyeti ölçmeye çalışır (16533387). **[Yaygın gözlem]** Zorla istenen etkileşim memnuniyet üretmez. | Yorum sorusu gerçek bilgi toplar (B6); "beğenmeyi unutmayın" cümlesi yok. |
| **"Trend araç çıktı, hemen video."** | **[Yaygın gözlem]** Haber trafiği kısa ömürlüdür ve kanalı "araç haberi" kitlesine tanıtır. | İzleyici "sorunu arar, aracı değil". Yeni araç ancak mevcut bir görev videosunun kronometresine girerse konu olur (K kategorisi). |

---

## Ek — Doğrulanacaklar listesi (ilk Studio oturumunda, tahmini 30 dk)

Bu belgede **[Resmî — sayfada teyit et]**, **[YouTube'a atfedilen — kaynak bulunamadı]** ya da "teyit edilemedi" notu taşıyan maddeler. support.google.com ve blog.youtube çalışma ortamının ağ izin listesinde olmadığı için açılamadı; tarayıcıdan kontrol et ve belgeyi güncelle:

1. Gösterim sayım kuralları (1 saniye / %50 görünürlük) ve sayılmayan yüzeyler → [7628154](https://support.google.com/youtube/answer/7628154)
2. Tutma raporundaki dört "önemli an" tanımı; az görüntülemede grafiğin gösterilmediği eşik → [9314415](https://support.google.com/youtube/answer/9314415)
3. Yeni / ara sıra / düzenli izleyici eşikleri (1–5 ay / 6+ ay mı, 7+ ay mı) → [10246996](https://support.google.com/youtube/answer/10246996). Ayrıca: Studio'da kanal ya da video düzeyinde hâlâ "geri dönen izleyiciler" adıyla bir satır var mı? Varsa performans kaydındaki "Geri dönen izleyici" hücreleri o satırdan, yoksa ara sıra + düzenli toplamından doldurulur.
4. A/B testi: uygunluk koşulu, azami süre, fark küçükken uzama, prömiyer/planlı canlı/liste dışı video durumu, sonuç etiketlerinin Türkçe adları → [16391400](https://support.google.com/youtube/answer/16391400), [13861714](https://support.google.com/youtube/answer/13861714)
5. Görüntüleme sayımı değişikliği (2025 Shorts, 2026 tüm formatlar): resmî duyuru; Studio'daki görüntüleme ve AVD'nin etkilenip etkilenmediği; "engaged views" metriğinin uzun videodaki tanımı ve Türkçe adı → Studio'da metrik açıklaması + YouTube Yardım
6. Gönderiler (topluluk) sekmesi erişim koşulu → Studio → Ayarlar → Kanal → Özellik uygunluğu; Studio → Oluştur
7. Performans SSS'sindeki ilgili soruların tam metni: yayın saati, ara verme, başlık/kapak değiştirme, zayıf performanslı video; ve A0'daki "tanıtmaz, bulur" cümlesinin özgün hâli → [141805](https://support.google.com/youtube/answer/141805)
8. Etiketler → [146402](https://support.google.com/youtube/answer/146402); yükleme programı → [13616979](https://support.google.com/youtube/answer/13616979); anahtar kelime doldurma → [2801973](https://support.google.com/youtube/answer/2801973)
9. Shorts analizleri → [12942217](https://support.google.com/youtube/answer/12942217). "İlgili video" bağlantısı: yeni kanalda erişim koşulu; bağlantının oynatıcıda nerede göründüğü. Shorts açıklama ve yorumlarındaki bağlantılar bugün tıklanabiliyor mu?
10. "How YouTube recommendations work" başlıklı Yardım sayfası ([16089387](https://support.google.com/youtube/answer/16089387)): bu adres arama sonuçlarında doğrulanamadı ve bu belgede hiçbir iddia ona dayandırılmadı. Sayfa varsa A11'e kaynak olarak eklenebilir.
11. Kaynağı bulunamayan atıflar (sıklık, abone sayısı): Creator Insider kanalında ya da [YouTube resmî blogunda](https://blog.youtube/) karşılığı var mı? Bulunursa video adı + tarihle belgeye işle ve etiketi yükselt; bulunamazsa etiket olduğu gibi kalır.
12. Türkçe Studio arayüzündeki güncel sekme/metrik adları (bu belgedeki adları gerçek adlarla değiştir)
