# 06 — Kameraya Çıkmadan Video Üretimi

**Kanal:** Kısa Mesai · **Yazım tarihi:** 2026-11-16 · **Kapsam:** yüz göstermeden üretimin adım adım uygulaması

Bu belge `03-yapim-is-akisi.md` belgesinin yerine geçmez; onun yüz göstermeyen üretime özel uygulama kılavuzudur. Yapım hattının aşamaları, süre bütçesi, klasör düzeni, adlandırma, varlık kütüphanesi ve kurgu ön ayarları 03 belgesindedir; burada yalnızca oraya eklenenler yazılıdır. Çelişki görürsen 03 belgesi ve `README.md` içindeki "tek kaynak" tablosu geçerlidir.

### İşaretler ve doğrulama durumu

Etiket seti 02 belgesindeki "Kaynak ve doğrulama durumu" tablosundakidir: **[Resmî — sayfada teyit et]** (resmî sayfaya dayanan iddia; bağlantı verildi ama sayfa bu çalışma ortamından açılamadı, uygulamadan önce aç) ve **[Yaygın gözlem]** (platformun ya da araç üreticisinin taahhüt etmediği, yaygın kabul gören pratik). Bu belge iki etiket daha kullanır: **[Tahmini]** (varsayımı yanında yazılı tahmin; ilk 3–4 videoda ölçüp düzelt) ve **[DOĞRULA]** (karardan ya da yayından önce senin kontrol edeceğin nokta).

> **Doğrulama notu:** support.google.com, blog.youtube, elevenlabs.io, learn.microsoft.com, docs.cloud.google.com, docs.aws.amazon.com ve obsproject.com çalışma ortamından açılamadı. Politika ve araç iddiaları arama sonuç özetlerine, ikincil kaynaklara ve yazım tarihinden önceki genel bilgiye dayanır; bu yüzden hiçbiri düz **[Resmî]** etiketi taşımıyor. Yol B'yi açmadan önce YouTube Yardım'ın 14328491 (beyan) ve 1311392 (para kazanma politikaları) numaralı sayfalarını kendin oku; okuyana kadar 7.4'teki kanal kuralı geçerlidir. Toplu liste belgenin sonundadır.

## 0. Önce karar: bu belge hangi durumda, nasıl kullanılır

Kanalın formatı ekran kaydı + seslendirmedir (senaryo 01'in başlık satırı: ekran kaydı, tek kısa masa üstü çekim, yüz yok); kapakta da yüz zorunlu değildir (01 belgesi Bölüm 3, kapak öğeleri tablosu). Ses konusunda iki yol var:

| | **Yol A — kendi sesin** | **Yol B — yapay zekâ seslendirme** |
|---|---|---|
| Konumu | 03 belgesi 4.3'teki karar; varsayılan | Senin açıkça istediğin alternatif; bu belgenin 2. bölümü |
| İlk 10 video | Geçerli yol | 03 belgesi 4.3 "ilk 10 videoda kullanılmaz" der. Yine de açarsan bu, o karardan **bilinçli sapmadır**: tarihi ve gerekçeyi `sablonlar/performans-kaydi.md` Bölüm 0'a yaz |
| Beyan | "Hayır" | 03 belgesi 4.4 A'daki kanal kuralı: Studio'da "Evet" + açıklamada tek cümle |
| Bu belgede geçerli bölümler | 1, 3–10 (2. bölümden yalnızca 2.3 yazım kuralları işe yarar) | Tamamı |

Artı ve eksilerin ana tablosu 03 belgesi 4.3'tedir; tekrar edilmedi. Oraya eklenenler:

- **Yol B'nin artısı:** oda, mikrofon ve gürültü sorunu yoktur; gece ya da ortak ofiste üretilebilir; tek cümle düzeltmesi ton tutturma derdi olmadan yapılır; sesin tanınmasını istemiyorsan (işveren, müşteri) gizlilik sağlar.
- **Yol B'nin eksisi:** senaryonun ikinci bir "okunuş" sürümünü tutmak gerekir (2.3); ses, aracın ses motoru güncellenince değişebilir **[Yaygın gözlem]**; aynı hazır sesi başka kanallar da kullanır; her yüklemede beyan ve diğer platformlarda etiket işi doğar (03 belgesi 4.4 C).

**Geçiş ölçütü (A → B).** Şu üç koşuldan biri varsa Yol B'yi aç:

1. Kendi sesinle kayıt fiilen mümkün değil (ortam, sağlık, gizlilik). Bu durumda ilk videodan itibaren Yol B; sapmayı kaydet.
2. KM-010'dan sonra: kendi sesinle seslendirme üç video üst üste 80 dakikayı aşıyor (03 belgesindeki bütçe 55 dk) **ve** 2.2'deki testte en az bir ses eşiği geçiyor **ve** bir deneme videosunda Yol B toplamı (okunuş metni + üretim + ses işlemi; Bölüm 8, satır 8–10) ölçülmüş olarak kendi sesle süreden en az 15 dakika kısa **[Tahmini eşikler]**. Ölçülmüş fark yoksa süre, geçiş gerekçesi değildir (Bölüm 8'in sonu).
3. KM-010'dan sonra: kör dinlemede (2.2'nin sonu) en az beş dinleyicinin çoğu sentetik sesi "rahat dinlenir" buluyor ve kendi kaydına tercih ediyor.

**Pilot ve geri dönüş (B → A).** Geçişi tek videoda değil, art arda **üç** uzun videoda dene; sesi video içinde karıştırma. Üç videonun 0:30 tutması ve ortalama izlenme yüzdesi kanal medyanının altındaysa (okuma kuralı: 02 belgesi Bölüm A) ya da ses hakkında yorum yazan en az üç ayrı kişi var ve bu yorumların çoğu olumsuzsa **[Tahmini eşik]** Yol A'ya dön. Yeni kanalda yorum sayısı bu eşiğe çoğu zaman ulaşmaz; o durumda karar tutma verisine ve kör dinlemeye kalır. Üç video küçük bir örnektir; sonucu "kanıt" değil "işaret" olarak oku.

## 1. Yüzsüz format: dört görsel katman

### 1.1 Katmanlar ve oranlar

Oranlar, katmanın **ana görüntü** olduğu sürenin video süresine payıdır; bindirmeler (alt bant, vurgu kutusu, kronometre çerçevesi) ekran kaydının üstünde durduğu için ayrıca sayılmaz. Hepsi **[Tahmini]** başlangıç değeridir; varsayım: 10–12 dakikalık, Kronometre Yarışı ya da liste yapısında bir video.

| Katman | Pay | 12 dk'lık videoda | Ne zaman | Neden |
|---|---|---|---|---|
| **1. Ekran kaydı (ana katman)** | en az %70 (tipik %75–90) | en az tahmini 8,5 dk | Görevin yapıldığı, prompt'un yazıldığı, çıktının kontrol edildiği her an | Kanalın kanıtı budur; yüzün yerini "gerçekten yapılıyor" görüntüsü tutar |
| **2. Metin ve veri grafikleri (tam ekran)** | %8–15 | tahmini 1–1,8 dk | Karşılaştırma tablosu, "yapamadığı şey" kartı, prompt kartı, formül kartı, bitişteki büyük sayı | İzleyicinin ekran görüntüsü alacağı kareler; sayıyı tek bakışta verir |
| **3. Animasyon / hareketli grafik** | %0–8 (çoğu videoda sıfır) | en çok tahmini 60 sn | Ekranda gösterilemeyen bir fikri anlatırken (ör. "aynı sohbete kötü deneme yazınca sonraki cevap neden değişir"); ölçüt 5.4 | Ekran kaydının anlatamadığı tek şey soyut ilişkidir; yalnızca o zaman |
| **4. Bağlam sahnesi (stok ya da kendi çekimin)** | %0–5 | en çok tahmini 35 sn, tek plan en çok 5 sn | Hook'ta işin gerçek hayattaki yerini göstermek, desen kırıcı (senaryo 01, 5:40'taki masa çekimi) | Uzun ekran kaydından sonra görüntü türünü değiştirir. Süs olarak kullanılmaz (Bölüm 4) |

Bantlar alt ve üst sınırdır, hedef değildir; toplam her videoda 100'dür ve 1. katmanın üst sınırı yoktur. KM-001 örneğinde (Bölüm 8) dağılım tahmini %86 / %10 / %0 / %4'tür; payı tutturmak için animasyon ya da stok eklenmez.

- Bir bölümde ana katman en fazla bir kez değişir; geri dönüş ekran kaydınadır.
- 4. katmanda **önce kendi çekimin** (el, masa, kâğıt, klavye; yüz yok), o yoksa stok. Kendi çekimin kanıt sayılır, stok sayılmaz.
- Senaryo yazarken EKRAN alanına katman numarasını yaz (`[K1]`, `[K2]`…). Senaryo kilitlenince say: K1 %70'in altındaysa video bu kanalın videosu olmaktan çıkıyor; K4 %5'i geçiyorsa stok plan çıkar.
- Oranları `performans-kaydi.md` içindeki "öğrenilenler" satırına yaz; tutma grafiğinde düşüş bir katman değişimine denk geliyorsa orayı işaretle.

### 1.2 Yüzsüz kanalın güven açığı ve kapatma yolları

Yüz yokken izleyici "bunu kim yaptı, gerçekten yaptı mı" sorusuna başka yerden cevap arar. Her satır bir üretim işidir:

| Açık | Kapatan şey | Uygulama |
|---|---|---|
| "Kim konuşuyor?" | **Ses kimliği** | Tek ses, her videoda aynı. Yol B'de: aynı ses adı, aynı ayarlar, `tts-kaydi.md` içinde yazılı (2.5). Ses değiştirmek kanal adını değiştirmek gibidir; yalnızca seri sınırında yapılır |
| "Bu kanal mı, başka biri mi?" | **Tutarlı görsel dil** | Lacivert + sarı, tek yazı tipi, sabit grafik seti (Bölüm 5); kronometre hep sağ üstte, alt bant hep sol altta |
| "Gerçekten yaptı mı?" | **Gerçek ekran** | Süreli koşu tek kesintisiz kayıt (03 belgesi Aşama 4); üretilmiş arayüz görüntüsü yok (03 belgesi 4.1) |
| "Süre doğru mu?" | **Gerçek ölçüm** | Kronometre kayda gömülü; hızlandırma etiketli; açıklamada "Nasıl ölçtüm" bloğu (`sablonlar/yayin-metaverisi.md` Bölüm 3) |
| "Bir insan var mı?" | **İnsan izi** | Elle yazılmış kâğıt, masa çekimi, yazım hatasıyla yazılan prompt'un düzeltilmesi, yorumlara yazılı ve imzalı cevap, tarihli düzeltme notu (03 belgesi 4.2, madde 5) |
| "Sentetik ses mi?" (Yol B) | **Açık söylemek** | Açıklamada sabit cümle + kanalın "Hakkında" metninde üretim yöntemi: "Ekran kayıtları ve ölçümler bana ait; seslendirme sentetiktir." Saklanan şey güveni düşürür, söylenen düşürmez **[Yaygın gözlem]** |

## 2. Yapay zekâ seslendirme (Yol B)

### 2.1 Araç kategorileri ve Türkçe desteği

| İş tanımı | Kategori → örnek | Türkçe için bilinen | Durum |
|---|---|---|---|
| Doğal tonlamalı anlatım üretmek, tek cümleyi yeniden üretmek | Üretken ses platformu → ElevenLabs | Yazım tarihinden önceki bilgiye göre ses motorları: Multilingual v2 (Türkçe dâhil 29 dil olarak bilinir), Flash/Turbo v2.5 ve v3 (daha geniş dil listesi). Hangisinin Türkçede daha iyi olduğu ancak 2.2'deki testle anlaşılır | **[DOĞRULA]** Yardım merkezindeki (help.elevenlabs.io) "What languages do you support?" makalesi ve [modeller sayfası](https://elevenlabs.io/docs/models); ikisini de aç. Ücretsiz planın ticari kullanım hakkı vermediği ve atıf istediği, ticari lisansın ücretli planlarla geldiği bilinir **[DOĞRULA: fiyat ve koşullar sayfası]** |
| Duraklama ve okunuşu işaretleme diliyle (SSML) denetlemek | Bulut metin okuma servisi → Microsoft Azure AI Speech, Google Cloud Text-to-Speech, Amazon Polly | Üçünde de `tr-TR` sesleri vardır. Bilinen adlar: Azure'da AhmetNeural ve EmelNeural; Polly'de Filiz (standart) ve Burcu (nöral). SSML desteği **ses ailesine göre değişir**: en yeni ailelerde kısıtlı olabilir ya da hiç olmayabilir (ör. Google'ın Chirp 3 HD seslerinin SSML kabul etmediği, Polly'nin nöral seslerinin etiketlerin yalnızca bir kısmını desteklediği bilinir) | **[Resmî — sayfada teyit et]** [Azure](https://learn.microsoft.com/azure/ai-services/speech-service/language-support?tabs=tts) · [Google](https://docs.cloud.google.com/text-to-speech/docs/list-voices-and-types) · [Polly](https://docs.aws.amazon.com/polly/latest/dg/available-voices.html). Seçtiğin Türkçe seste `<break>` ve okunuş etiketlerinin çalıştığını testte dene; ücretsiz kota, ödeme yöntemi şartı ve ticari kullanım koşulu **[DOĞRULA]** |
| Kurgudan çıkmadan hızlı taslak ses almak | Kurgu aracına gömülü metin okuma (ör. CapCut'taki özellik; araç 03 belgesi 3.2'de öneri listesinden çıkarıldı) | Doğrulanmadı | **Bu kanalda yayın sesi olarak kullanılmaz:** ses kimliği kurgu aracına bağlanır, ayar ve lisans kaydı tutulamaz |
| Metni dışarı göndermeden, çevrimdışı üretmek | Açık kaynak yerel ses motoru → Piper, XTTS-v2 | Piper'ın `tr_TR` ses paketleri vardır; XTTS-v2 Türkçeyi destekler. Kurulum komut satırı ister; teknik olmayan kullanıcı için ilk tercih değildir | Piper: her ses paketinin lisansı ayrıdır **[DOĞRULA]**. XTTS-v2: model lisansı ticari kullanıma kapalı olarak bilinir; para kazanan kanalda kullanma **[DOĞRULA]** |

Seçim sırası: önce 2.2'deki test, sonra lisans, en son fiyat. Lisansta bakılacak üç cümle **[DOĞRULA]**: (1) seçtiğin planda üretilen ses para kazanan bir kanalda kullanılabiliyor mu; (2) atıf zorunlu mu; (3) aboneliği bıraktığında daha önce ürettiğin dosyaları yayında tutabiliyor musun. Ticari kullanım hakkı vermeyen planda üretilen ses yalnızca test içindir, yayına girmez.

### 2.2 On beş dakikalık Türkçe deneme testi

**Ön hazırlık (süreye dâhil değil; ilk seferde tahmini 15–20 dk [Tahmini]):** üç aracı seç, hesapları aç, her birinde Türkçe, sakin, orta hızda bir ses belirle ve adını not et. Öneri: bir üretken ses platformu (ElevenLabs) + iki bulut servisi (Azure AI Speech, Google Cloud Text-to-Speech). Bulut hesabı çoğunlukla ödeme yöntemi ister; hesap açmak istemiyorsan servisin tanıtım sayfasında ya da ses galerisinde tarayıcıdan denenen bir alan var mı bak **[DOĞRULA: deneme alanının varlığı ve dosya indirmeye izin verip vermediği]**. İndirme yoksa sesi OBS ile kaydet; puanlama için yeter.

Aynı paragrafı üç araçta okut. Paragraf bu kanalın gerçek zorluklarını içerir; değiştirmeden kullan (sayılar test içindir, hiçbir videonun ölçümü değildir):

> Bu teklifi elle yazmak 47 dakika sürdü. ChatGPT'ye aynı işi verdim; 14 dakikada bitti. Peki sonuç aynı mı? Hayır. Excel'deki KDV sütununu yanlış topladı, %20'lik satırı iki kez saydı. Hâlâ kullanırım, ama kontrol etmeden göndermem. İşin değişmediğini ertesi gün İK'ya da gösterdim. Sırayla üç şey yaptım: malzemeyi verdim, çıktıyı tarif ettim, önce soru sordurdum. Prompt açıklamada.

Akış: **0–1. dk:** Paragrafı düz hâliyle üç araca yapıştır · **1–4. dk:** Üçünü üret, `test_arac1.wav` … olarak indir. Hiçbir ayara dokunma · **4–9. dk:** Her dosyayı kulaklıkla bir kez, telefon hoparlöründen bir kez dinle; ilk dokuz ölçütü puanla · **9–13. dk:** En iyi iki araçta yalnızca hatalı kelimeleri okunuş yazımıyla düzelt (2.3), yeniden üret: düzeltme tutuyor mu? · **13–15. dk:** Puanları, ses adlarını ve tarihi `00_VARLIKLAR/ses/ses-kimligi.md` içine yaz. Puanlama: her ölçüt 0 (kabul edilemez) · 1 (düzeltmeyle olur) · 2 (sorunsuz).

| Ölçüt | Paragrafta neye bak |
|---|---|
| Sayı + ek | "47 dakika", "14 dakikada", "%20'lik": doğru okuyor mu, eki sayıya bağlıyor mu |
| İngilizce ad + Türkçe ek | "ChatGPT'ye", "Excel'deki": ad anlaşılır mı, ek doğal bağlanıyor mu |
| Kısaltma | "KDV", "İK'ya": harf harf Türkçe okuyor mu ("ka de ve" ya da "ke de ve"; seçtiğini sözlüğe yaz). İngilizce harf adlarıyla okuyorsa 0 |
| Soru tonu | "Peki sonuç aynı mı?": ton soru gibi mi |
| Tek kelimelik cümle | "Hayır.": yutuluyor ya da abartılıyor mu |
| Düzeltme işareti ve Türkçe harfler | "Hâlâ" ("hala" gibi okumuyor mu), "İşin", "değişmediğini" |
| Sıralama | "malzemeyi verdim, çıktıyı tarif ettim, önce soru sordurdum": üç öğe ayrışıyor mu |
| Ton | Kanalın tonu: sakin, abartısız. Reklam sesi ya da haber spikeri gibi mi |
| Yorgunluk | İkinci dinlemede rahatsız eden metalik tını, nefes taklidi, cümle sonu yükselmesi var mı |
| Düzeltilebilirlik (yalnızca ilk iki araç) | 9–13. dakikadaki düzeltme tuttu mu |

**Eşik [Tahmini]:** ilk dokuz ölçütte 18 üzerinden en az 13 ve hiçbirinde 0 yok; ayrıca düzeltilebilirlik en az 1. Eşiği geçen yoksa Yol B'yi bugün açma; testi üç ay sonra tekrarla.

**Kör dinleme (isteğe bağlı, geçiş kararı için):** Aynı paragrafı kendi sesinle de kaydet. Hedef kitleden en az beş kişiye hangisinin hangisi olduğunu söylemeden dinlet; tek soru: "Hangisini 10 dakika dinlersin?"

### 2.3 Seslendirme için senaryo yazım kuralları

Senaryonun SES alanı (`sablonlar/senaryo-sablonu.md`) **görünen metindir**: altyazıya, açıklamaya ve prompt dosyasına o gider. Ses motoruna giden metin ayrı bir dosyadır: `02_senaryo/KM-[NO]_tts-metni.md`. Kilitli senaryodan türetilir, senaryo değişirse yeniden türetilir; tersine düzeltme yapılmaz.

| Konu | Görünen metin | Okunuş metni (ses motoruna giden) | Not |
|---|---|---|---|
| Sayı | 14 dakika | on dört dakika | Bütün sayıları yazıyla yaz; aracın tahminine bırakma |
| Sayı + ek | 3'te, 2026'da | üçte, iki bin yirmi altıda | Kesme işaretini kaldır |
| Yüzde | %20 | yüzde yirmi | |
| Süre ve saat | 13 dk 20 sn · 2:25 | on üç dakika yirmi saniye · iki yirmi beş | "dk", "sn" kısaltması okunuş metninde kalmaz |
| Para | 1.250 TL | bin iki yüz elli lira | Binlik noktası ondalık sanılabilir |
| Sıra ve aralık | 3. adım · 8–14 dk | üçüncü adım · sekiz ile on dört dakika arası | Tire okunmaz ya da "eksi" okunur |
| Kısaltma | KDV, İK, vb., örn. | ka de ve, insan kaynakları, ve benzeri, örneğin | Kısaltmayı aç; harf harf okunacaksa sözlükte seçtiğin okunuşla hecele |
| İngilizce araç adı | ChatGPT, Excel, Claude | sözlükteki okunuş (2.4) | Okunuşu bir kez seç, her videoda aynı |
| Ad + ek | ChatGPT'ye, Claude'a | okunuş + ek, kesme işaretsiz | Ek, yazıma değil **okunuşun** son sesine uyar: okunuş "çetcipiti" ünlüyle bittiği için "çetcipitiye"; "Claude" "klod" okunduğu için "kloda" ("klode" değil) |
| Dosya adı, bağlantı, kod | `olcum.md`, kısa bağlantı | Okutma; "açıklamadaki bağlantı" de | Ekranda gösterilir |
| Parantez, tırnak, madde işareti | (isteğe bağlı), "…" | Cümleyi parantezsiz yeniden kur; alıntıyı "şunu yazdım:" diye tanıt | Tırnak tonu değiştirmez |

Noktalama, vurgu ve duraklama:

- **Bir cümle, bir fikir; en çok 15–18 kelime [Tahmini].** Uzun cümlede ses motoru nefes yerini kendisi seçer ve çoğu zaman yanlış seçer **[Yaygın gözlem]**.
- **Virgül kısa, nokta uzun duraklamadır.** Duraklama istediğin yerde cümleyi böl. Üç nokta, uzun tire ve noktalı virgülün etkisi araçtan araca değişir; kullanmadan önce dene.
- **Vurguyu söz dizimiyle ver.** Türkçede vurgu yüklemin hemen önündeki öğeye düşer. "Yapay zekâ bu işi **14 dakikada** bitirdi" süreyi, "Bu işi 14 dakikada **yapay zekâ** bitirdi" yapanı vurgular. Büyük harf ya da yıldızla vurgu işaretleme; çoğu araç bunu okumaz ya da yanlış okur **[Yaygın gözlem]**. **Sayıyı cümlenin sonuna yakın koy ve sayıdan sonra cümleyi bitir.** Sayıdan sonra gelen uzun kuyruk sayıyı gömer.
- **Duraklama işareti:** okunuş metninde kendi işaretini kullan: `[D1]` kısa (tahmini 0,3 sn), `[D2]` bölüm arası (tahmini 0,7 sn), `[D3]` kart ya da sessiz ekran için (süreyi yanına yaz: `[D3: 4 sn]`). Seçtiğin ses SSML destekliyorsa (2.1) `[D1]`/`[D2]` üretimden önce `<break time="300ms"/>` gibi etiketlere çevrilir (tam örnek 2.5); desteklemiyorsa sessizlik kurguda eklenir. `[D3]` her durumda kurguda eklenir: ses dosyası orada bölünür.
- **Yer tutucular** (`[YZ SÜRE]`, `[ÇEKİMDE …]`) dolmadan okunuş metni üretilmez. 03 belgesindeki sıra geçerlidir: çekim → yer tutucular → seslendirme.

Dönüşümü elle yapma; sohbet asistanına yaptır, sonra denetle. Kopyalanabilir prompt:

> Aşağıda bir video senaryosunun görünen metni ve telaffuz sözlüğüm var. Metni ses motoru için okunuş metnine çevir. Yalnızca şunları yap: sayıları, yüzdeleri, süreleri ve para tutarlarını yazıyla yaz; kısaltmaları aç; sözlükteki kelimeleri okunuş yazımıyla değiştir ve ekleri okunuşun son sesine göre uydur; kesme işaretlerini kaldır. Cümle ekleme, çıkarma, sırayı değiştirme. En sonda değiştirdiğin her yeri "önce → sonra" listesi olarak ver. Görünen metin: [YAPIŞTIR] Sözlük: [YAPIŞTIR]

"Önce → sonra" listesindeki her sayıyı `olcum.md` ile tek tek karşılaştır; karşılaştırmadan üretime verme. Sözlükte olmayan yeni kelimeyi listeden yakala ve 2.4'e ekle.

### 2.4 Telaffuz sözlüğü

Dosya: `00_VARLIKLAR/ses/telaffuz-sozlugu.md`. Her yeni kelime ilk karşılaşıldığında eklenir; okunuş metni türetilirken 2.3'teki prompt'a girdi olarak verilir.

```
| Görünen | Okunuş yazımı | Ekli örnek | Araç / ses | Denendi | Not |
|---------|---------------|------------|------------|---------|-----|
| ChatGPT | [DENE: "çet ci pi ti" / "çetcipiti"] | [ ]ye | [ ] | [tarih] | bitişik mi ayrı mı daha doğal |
| Excel   | [DENE: "eksel"]                     | [ ]de  | [ ] | [tarih] |  |
| Claude  | [DENE: "klod"]                      | [ ]a   | [ ] | [tarih] |  |
| prompt  | [DENE: olduğu gibi]                 | [ ]u   | [ ] | [tarih] | çoğul: prompt'lar |
| PDF     | [DENE: "pe de fe" → ek -yi / "pi di ef" → ek -i] | [ ] | [ ] | [tarih] | KDV için de aynı seçim: "ka de ve" / "ke de ve" → -yi |
| hâlâ    | [DENE: olduğu gibi / "haalaa"]      | —      | [ ] | [tarih] | "hala" okuyorsa |
```

Kurallar: okunuşu **kendi seçtiğin araç ve seste** deneyip yaz, tabloyu tahminle doldurma. Kısaltmada hangi okunuşu seçtiysen görünen metindeki ek de ona göre yazılır ("PDF'yi" ya da "PDF'i"); altyazı ile ses aynı eki taşır. Ses ya da ses motoru değişirse sözlüğün tamamını yeniden dinle (tahmini 10 dk). Araçta yerleşik bir telaffuz sözlüğü özelliği varsa onu kullan ama bu dosyayı yine tut, çünkü araç değişir, dosya kalır **[DOĞRULA: özelliğin Türkçede çalışıp çalışmadığı]**.

### 2.5 Parça parça üretim, adlandırma, kayıt

Bu bölümün dosyaları 03 belgesi 6.1'deki ağaca ektir: `00_VARLIKLAR/ses/` (`ses-kimligi.md`, `telaffuz-sozlugu.md`), video klasöründe `02_senaryo/KM-[NO]_tts-metni.md` ve `04_ses/tts-kaydi.md`.

**İlk üretim, araç türüne göre** (ekran ve düğme adları **[DOĞRULA: aracın güncel arayüzü]**):

- *Üretken ses platformu:* metinden sese ekranını aç → sesi ve ses motorunu seç → hız ve kararlılık gibi ayarları ilk videoda bir kez belirle, `ses-kimligi.md` içine yaz, sonra dokunma → bölümün okunuş metnini yapıştır → üret → dinle → indir.
- *Bulut metin okuma servisi:* servisin tarayıcıdaki deneme ya da ses galerisi ekranını aç → Türkçe sesi seç → metni SSML olarak yapıştır → dinle → indir. Azure sözdizimiyle örnek (ses adı ve her etiketin o seste çalıştığı **[DOĞRULA]**; aynı metin + aynı ses + aynı ayarın her üretimde aynı sonucu verip vermediği de):

```
<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="tr-TR"><voice name="tr-TR-EmelNeural"><prosody rate="-5%">
Bu işi <sub alias="çetcipitiye">ChatGPT'ye</sub> verdim.<break time="300ms"/> On dört dakikada bitti.
</prosody></voice></speak>
```

1. **Parça birimi bölümdür**, cümle ya da paragraf değil. Bütün metni tek seferde üretme (uzun metinde ton ve hız kayabilir, tek hata her şeyi yeniden ürettirir); çok küçük parçalara da bölme: ayrı üretilen parçalar arasında ton, hız ve seviye farkı duyulur **[Yaygın gözlem]**.
2. Her parçayı indirir indirmez, **bir önceki parçanın son cümlesiyle art arda** dinle. Ton ya da hız farkı duyuluyorsa parçayı yeniden üret. Araç "önceki/sonraki metin" bağlamı ya da sabit tohum (seed) veriyorsa kullan **[DOĞRULA]**.
3. Tek cümle düzeltmesinde hatalı cümleyi önündeki ve arkasındaki cümleyle birlikte üret, ortadakini kesip yerine koy. Aynı cümleyi en fazla **üç kez** yeniden üret; üçüncüde de olmuyorsa cümleyi yeniden yaz (önce görünen metinde, sonra okunuş metninde). Sayıyı tek kelime olarak üretip yapıştırma; ton tutmaz.
4. Hook'u 03 belgesi Aşama 5'teki gibi üç kez üret, en sakin olanı seç.
5. Adlandırma 03 belgesi 6.2 kalıbıyla; tür `tts`, deneme `tN`: `KM-001_b4-kosu_tts_t2.wav`. Ham parçalar `04_ses/ham/`, işlenmiş bölümler `04_ses/temiz/KM-001_b4-kosu_tts_temiz.wav`.
6. Biçim: aracın verdiği en yüksek kaliteli biçimi al (sıkıştırılmamış varsa onu, yoksa en yüksek bit hızlı MP3) ve yeniden MP3'e çevirme. Örnekleme hızını zorlama; kurgu aracı 48 kHz zaman çizelgesine kendisi çevirir. Hangi biçimin hangi planda açık olduğu **[DOĞRULA]**.
7. `04_ses/tts-kaydi.md` dosyasına yaz: tarih · araç · ses adı · ses motoru adı ve sürümü · hız ve diğer ayarlar · yeniden üretilen cümle sayısı · toplam süre. Kanal düzeyindeki sabitler (ses adı, ayarlar, lisans planı, 2.2 test puanı) `ses-kimligi.md` içinde durur. Kayıt tutarlılık içindir; para kazanma başvurusunda incelemeci yalnızca yayındaki içeriği görür, bu kayıtlar ancak ret hâlinde itirazda üretim sürecini göstermeye yarayabilir **[Yaygın gözlem; itiraz yöntemi DOĞRULA]**.

### 2.6 Ses sonrası işlem

Sentetik ses temiz gelir; 03 belgesi 6.4'teki zincirden gürültü azaltma çıkar, gerisi kalır. Araç: 03 belgesi 3.3'teki ses düzenleyici (Audacity) ya da kurgu aracının ses sayfası.

| İş | Nasıl | Hedef |
|---|---|---|
| Sessizlik standardı | Parçaların başındaki ve sonundaki boşluğu kırp; cümle arası ve paragraf arası boşluğu elle eşitle | Cümle arası tahmini 0,25–0,4 sn, bölüm arası 0,6–0,8 sn **[Tahmini başlangıç]**; hepsi aynı |
| Seviye | Parçaları tek dosyada birleştir, bölümler arası seviye farkını eşitle, sonra sıkıştırma + sınırlayıcı | 03 belgesi 6.4'teki ses yüksekliği hedefi |
| Tempo | Hız değişikliğini araçta, **üretimden önce** yap. Kurguda zaman esnetme yalnızca küçük düzeltme için | Esnetme tahmini ±%5'i geçmesin; ötesinde ses bozulur **[Yaygın gözlem]** |
| Kesim yerleri | Dalga biçiminde sıfır geçişinde kes, 5–10 ms geçiş ekle | Tıkırtı yok |
| Son dinleme | Baştan sona kulaklıkla, 1× hızda; elinde görünen metin | Okunan her sayı `olcum.md` ile aynı |

### 2.7 Kendi sesini klonlama

Ara yol: ses senindir ama kayıt yapmazsın. Karar vermeden önce:

- **Rıza ve etik.** Yalnızca **kendi** sesini klonla. Başkasının sesi (eş, arkadaş, seslendirme sanatçısı) için yazılı, kapsamı belli, geri alınabilir izin gerekir; `sablonlar/izin-onay.md` buna göre genişletilir. Tanınmış birinin sesine benzeyen hazır ses kullanma. Ses örneğini yüklediğin aracın, kaydını nasıl sakladığını ve başka amaçla kullanıp kullanmadığını oku **[DOĞRULA]**. Ses kişisel veridir; hukuki tavsiye değildir, başkasının sesini işleyeceksen bir hukukçuya danış.
- **Beyan.** YouTube'un yardım sayfasının arama özetinde **başkasının** sesini klonlamak beyan gerektiren örnekler arasında; kendi ses klonun için kaynaklar çelişiyor (03 belgesi 4.4 A). Kanal kuralı değişmez: klon dâhil her sentetik ses için "Evet" + açıklama cümlesi.
- **Kalite.** Klonun kalitesi verdiğin kaydın kalitesidir: yankısız oda, tek mesafe, kanalın tonunda okunmuş metin. Kötü odada kaydedilmiş örnek, kötü odayı da klonlar **[Yaygın gözlem]**. Türkçe klon kalitesi araçtan araca değişir; 2.2'deki testi klonla da yap **[DOĞRULA]**.
- **Dürüstlük.** Klon sesle "bunu ben söyledim" izlenimi doğar. Videoda söylenen her cümle senin onayladığın kilitli senaryodan gelir; klona senaryo dışı cümle söyletilmez. **Sıra.** 03 belgesi 4.3 klonu ilk 10 videoda kullanmaz. Sonrasında açılacaksa 0. bölümdeki pilot kuralı geçerlidir.

## 3. Ekran kaydı

Çekim profili, çözünürlük, kronometrenin kayda gömülmesi, süreli koşu ve ölçümün dürüstlük kuralı 03 belgesi Aşama 4'tedir. Buradakiler ona ektir.

### 3.1 Kayıt öncesi masaüstü hazırlığı (ek maddeler)

| Konu | İş | Kontrol |
|---|---|---|
| Örnek hesap | Videoda görünen her araç için kanala ait ayrı hesap aç (ör. `kisamesai.cekim@…`); profil adı "Kısa Mesai", profil resmi kanal logosu | Hesap menüsü açıldığında kişisel ad yok |
| Sohbet geçmişi | Çekim hesabında geçmişi boş tut ya da kenar çubuğunu kapat | Kenar çubuğunda eski sohbet başlığı yok |
| Otomatik tamamlama ve pano | Çekim profilinde adres çubuğu önerilerini, kayıtlı form verilerini ve parola önerilerini kapat; çekimden önce panoya zararsız bir metin kopyala | Adres çubuğuna bir harf yaz: kişisel adres çıkmıyor; yanlışlıkla yapıştırınca kişisel veri çıkmıyor |
| Dosya pencereleri ve ofis yazılımı | Çekim için ayrı klasör; dosya penceresini "Son kullanılanlar" görünmeyecek şekilde o klasörde aç. Excel/Word başlık çubuğundaki hesap adına ve "son dosyalar" listesine bak | Dosya seçme penceresinde kişisel klasör adı yok; kurgusal şirket adına açılmış profil ya da adı kırpan kayıt alanı |
| Sistem çubuğu | Saat, takvim, Wi-Fi adı, pil; işletim sisteminin "rahatsız etmeyin" kipi | Kayıt alanı sistem çubuğunu dışarıda bırakıyor ya da çubuk gizli |
| Kurgusal veri | Kişi adları, telefon, e-posta, vergi numarası biçimindeki alanlar açıkça kurgusal (03 belgesi 4.5) | Gerçek bir kişi ya da şirketle karışmıyor |

### 3.2 Kayıt ayarları (ek)

- **Kayıt alanı:** tam ekran yerine 16:9 sabit bir bölge ya da tek pencere; sistem çubuğu ve bildirim alanı dışarıda kalır. **Sistem sesini kaydetme** (bildirim sesi riski); Yol B'de mikrofon kanalını da kapat.
- **Kare hızı sabit olsun.** Telefonla çekilen masa görüntüsü değişken kare hızlı olabilir; kurguda ses kayması görürsen dosyayı kurgudan önce sabit 30 kare/sn'ye dönüştür **[Yaygın gözlem]**.
- **Kayıt biçimi:** çökme hâlinde dosyanın kurtarılabildiği bir kap biçimi seç. OBS Studio'da: Ayarlar → Çıkış → Kayıt → Kayıt biçimi: "Hybrid MP4" (sürümünde varsa) ya da MKV; düz MP4 seçme, çökmede dosya açılmayabilir. MKV seçtiysen Ayarlar → Gelişmiş → Kayıt altındaki otomatik MP4'e dönüştürme (remux) kutusunu işaretle. Kaynak: [OBS bilgi bankası, Hybrid MP4](https://obsproject.com/kb/hybrid-mp4) **[Resmî — sayfada teyit et; menü adlarını ve sürümündeki varsayılanı DOĞRULA]**.
- **Her kayıt bir iş:** süreli koşu tek dosya; her ek gösterim ayrı dosya. Uzun tek kayıt, kurguda aranan anı bulmayı zorlaştırır.

### 3.3 Önce ses mi, önce görüntü mü

İki tür kayıt vardır ve sıraları terstir:

| Kayıt türü | Sıra | Neden |
|---|---|---|
| **Kanıt kaydı** (süreli koşu, elle koşu, "yapamadığı şey" anı) | **Önce görüntü, sonra ses** | Sonuç çekimde ortaya çıkar; senaryodaki sayı ve cümle ona göre yazılır. Sese uydurmak için yeniden çekilmez |
| **Anlatım kaydı** (bir menünün yeri, prompt'un parça parça gösterilmesi, önce/sonra ekranı) | **Önce ses, sonra görüntü** | Ses dosyasının süresi bellidir; görüntüyü ona göre çekmek kurguda esnetme ve dondurma ihtiyacını azaltır |

Anlatım kaydını sese göre çekme yöntemi: bölümün temiz ses dosyasını kulaklıkta çal, aynı anda ekranı kaydet, her cümlede söylenen şeyi ekranda yap. İlk tur prova, ikinci tur kayıt. Hareketler yavaş ve tek tek: imleç hedefe gider, yarım saniye durur, tıklar. İki yolda da anlatım kayıtlarına ses kilitlendikten (6.2) sonra başla. Yol B'de kilit ayrıca önemlidir: yeniden üretilen cümlenin süresi ve tonlaması her üretimde değişir **[Yaygın gözlem]**; kilitten sonra cümle değiştirirsen o bölümün görüntüsünü yeniden hizalamayı göze alırsın.

### 3.4 İmleç ve yakınlaştırma vurguları

Yakınlaştırma ön ayarları ve büyütme sınırları 03 belgesi 6.4'te, "tek karede tek vurgu" kuralı 6.3'tedir. Ek olarak:

- **İmleç anlatıcının parmağıdır.** Çekimde imleci okunacak metnin üstünde gezdirme; hedefin yanında dursun. Boşta kalan imleci ekranın aynı köşesine park et.
- **Yakınlaştırmayı cümleye bağla.** Büyütme, hedefin adı söylenmeden yarım saniye önce başlar, cümle bitince geri çekilir. Tahmini 0,4–0,6 sn yumuşak geçiş **[Tahmini]**; daha hızlısı sarsar, daha yavaşı geciktirir.
- **Art arda iki büyütme arasında tam ekrana dön** ya da doğrudan kes; büyütülmüş hâlde kaydırma (pan) izleyiciyi yorar **[Yaygın gözlem]**.
- **Vurgu sırası:** önce yakınlaştır, yetmiyorsa vurgu kutusu, o da yetmiyorsa çevreyi karart. Üçü aynı anda kullanılmaz.
- **Yazma anları:** uzun bir prompt'un yazılışını hızlandır (etiketle), son satırın yazılışını gerçek hızda bırak.

### 3.5 Bekleme sürelerini kurguda yönetmek

Kural 03 belgesinde yazılı (Aşama 4 adım 3, Aşama 6 adım 2, 6.3): kronometre kayda gömülüdür, rakam kurguda yazılmaz; hızlandırılan ya da beklemesi kesilen her bölüm "hızlandırıldı ×N" etiketi taşır; hızlandırmada rakam hızlı akar, kesimde ileri atlar. Bu belgenin eklediği: **N = bölümün gerçek süresi ÷ ekranda kaldığı süre, yukarı yuvarlanır** (90 saniyelik bekleme ekranda 6 saniye kaldıysa ×15). Tek kesintisiz olması gereken **ham kayıttır**; kurguda süreli koşu parçalar hâlinde ve başka kayıtlarla dönüşümlü kullanılabilir. Koşul: gizli kesim yok; her kesim ve hızlandırma etiketli, kronometredeki atlama görünür. Tablolardaki eşikler **[Tahmini]**; ilk videoların tutma grafiğinde bekleme anlarına bak ve düzelt.

| Aracın cevabını bekleme (gerçek süre) | Ne yapılır | Ekranda |
|---|---|---|
| 3 saniyeye kadar | Dokunma | — |
| 3–15 sn | Gerçek hızda bırak, seslendirmeyi üstüne koy ("cevap gelirken şuna bak") | — |
| 15–60 sn | İlk 2 sn gerçek hız → ortası hızlandırılmış → son 2 sn gerçek hız | "hızlandırıldı ×N"; kronometre hızlı akar |
| 60 sn üstü | İlk 2 sn ve son 2 sn gerçek hız, ortası kesilir | "hızlandırıldı ×N"; kronometre ileri atlar, kesim yerine geçiş efekti konmaz |

| Bekleme dışı an | Ne yapılır | Ekranda |
|---|---|---|
| Uzun yazma ya da yapıştırma | Hızlandır; son satır gerçek hızda (3.4) | "hızlandırıldı ×N" |
| Sessiz okuma, elle kontrol | İlk 2 sn ve son 2 sn gerçek hız, ortası hızlandırılmış; neyin kontrol edildiği seslendirmede söylenir | "hızlandırıldı ×N" |
| Koşudan başka bir kayda geçiş ve dönüş | Koşu o noktada kesilir, dönüşte kaldığı yerden ya da ilerisinden sürer | Süre dışı kayıtta kronometre durmuş görünür + "Ayrı sohbet · süre dışı" etiketi (03 belgesi 6.3); dönüşteki rakam farkı kapatılmaz |
| Koşunun videoya girmeyen kısmı | Atlanabilir; atlanan kısımda hata ya da düzeltme turu olduysa seslendirmede söylenir | Atlamadan sonraki ilk karede kronometre kadrajda |

Yasaklar (dürüstlük):

- Süreli kayıtta **kare dondurma, yavaşlatma ve döngü yok.** Seslendirme uzun geldiyse görüntüyü dondurma (kronometre de donar ve yanlış süre gösterir); cümleyi kısalt ya da o cümleyi süre dışı bir kaydın üstüne taşı.
- Kronometrenin üstü hiçbir grafikle örtülmez; yakınlaştırmada kadraj dışında kalıyorsa kronometrenin küçük bir kopyası (aynı kayıttan kırpılmış; kanalı 6.1'de) sağ üstte tutulur. Kopya kayıttan gelir, yazılmaz.
- Hızlandırma katsayısı etikette gerçek değerdir; "×4" yazıp ×8 uygulanmaz.

### 3.6 Hassas bilgiyi kapatma

Önce çekimde önle (3.1); kurguda kapatma ikinci savunmadır.

1. **Bulanıklık yerine dolu kutu.** Küçük metnin üstündeki bulanıklık ve mozaik bazı durumlarda geri okunabilir **[Yaygın gözlem]**; lacivert, opak bir kutu kullan.
2. Kutu, kaydırma ve pencere hareketiyle birlikte hareket etmeli: kutunun konumuna hareketin başında ve sonunda anahtar kare koy (ya da kurgu aracının izleme özelliğini kullan **[DOĞRULA: sürümünde]**), sonra bölümü kare kare ileri sar, sızan kare var mı bak.
3. Kutu her zaman **en üstteki görüntü klibinin üstünde** durur (kanalı 6.1'de). Yakınlaştırılmış kopyada aynı bilgi büyüyerek yeniden görünür; kutuyu kopyanın ölçeğine göre yeniden boyutlandır.
4. Kapatılan alan büyükse kayıt alanını kırp ya da bölümü yeniden çek; ekranın dörtte biri kutuyla kaplı bir video kanıt değeri taşımaz.
5. Aynı kontrolü kapak ve kısa videolar için ayrıca yap; onlar başka kareden üretilir. Ham kayıt arşivde kapatılmamış durur; ham dosyayı kimseyle paylaşma.

## 4. Stok görüntü

### 4.1 Ne zaman kullanılır, ne zaman kullanılmaz

| Kullanılır | Kullanılmaz |
|---|---|
| Hook'ta işin gerçek hayattaki yerini 3–5 saniyede göstermek (ör. masada birikmiş faturalar) ve kendi çekimin yoksa | Seslendirme sürerken ekranı doldurmak için |
| Bölüm geçişinde tek plan, desen kırıcı olarak | Kanıt yerine: araç arayüzü, "sonuç" görüntüsü, çalışan bir ekran (03 belgesi 4.1) |
| Kısa videonun ilk karesinde bağlam | Duygu göstermek için (sevinen, şaşıran, başını tutan insanlar) |
| | Kapakta ana öğe olarak (01 belgesi Bölüm 3) |

Sınır: 1.1'deki %5 ve plan başına 5 saniye. Senaryo 01'de stok plan **yoktur**; desen kırıcı kendi masa çekimindir. Bir videoda stok kullanmadan bitirebiliyorsan bitir.

### 4.2 Arama yöntemi

1. Senaryoda `[K4]` işaretli her satır için **nesne ve eylem** yaz, kavram değil: "verimlilik" değil, "elle doldurulan kâğıt form, üstten". Arama İngilizce yapılır; nesne + açı + ortam ("handwritten invoice desk top view").
2. Filtre: yatay, en az 1080p, insan yüzü yok ya da tanınmıyor, marka ve ekran içeriği görünmüyor. Aynı videodaki planlar aynı ışık ve renk sıcaklığında olsun; lacivert + sarı palete uymayan planı hafif soluklaştır.
3. Türkiye'ye uymayan ayrıntılara bak: priz tipi, para birimi, yabancı dilde belge, ofis mimarisi. Uymuyorsa yakın plan seç ya da kendi masanı çek.
4. Plan başına en çok 5 dakika ara **[Tahmini]**; bulamıyorsan o satırı ekran kaydına ya da karta çevir.

### 4.3 Klişe stoktan kaçınma

Kullanılmayanlar: el sıkışan takım elbiseliler, mavi ışıklı robot eli ve beyin görselleri, havada uçuşan ikili kodlar, toplantı masasında gülen ekip, klavyeye hızlı yazan eller (hızlandırılmış), büyüteçle grafiğe bakan kişi. Sınama sorusu: "Bu planı başka on kanalda gördüm mü?" Evetse çıkar. Yapay zekâyı anlatmak için yapay zekâ görseli kullanılmaz; kanalın yapay zekâ görüntüsü, ekrandaki gerçek sohbet penceresidir.

### 4.4 Lisans türleri ve kayıt tutma

Genel bilgidir, hukuki tavsiye değildir; her dosyanın lisansını indirdiğin gün kendi sayfasından oku.

| Tür | Anlamı | Bu kanalda |
|---|---|---|
| Telifsiz (royalty-free) | Bir kez lisanslanır, kullanım başına ödeme yoktur. "Ücretsiz" demek değildir; koşulları vardır | Asıl kullanılacak tür |
| Ücretsiz stok sitesinin kendi lisansı | Siteye özgü metin; çoğunlukla ticari kullanıma izin verir, kısıtları vardır (yeniden dağıtım, kişilerin onay izlenimi, marka) | Metni oku; "ücretsiz" yazması yetmez |
| Creative Commons | CC0 (kamu malı feragati; serbest), BY (atıf şart), NC (ticari kullanım yok), ND (değiştirme yok), SA (aynı lisansla paylaş) | Bu kanalda yalnızca CC0 ve CC BY; BY'de atıf açıklamaya yazılır. NC, ND ve SA içerenler kullanılmaz (SA, videonun tamamını aynı lisansla paylaşma yükümlülüğü doğurabilir) |
| Yalnızca editoryal | Haber/yorum amaçlı; tanıtım ve ticari kullanım yok | Kullanma |
| Hak yönetimli | Süre, bölge ve mecra bazında lisans | Bu kanalın ihtiyacı değil |

Ayrıca: lisans görüntüyü kapsar, içindeki **kişiyi, markayı ve mülkü** her zaman kapsamaz (model/mülk izni ayrı konudur). Yüzü görünen kişi içeren planı kullanma.

Kayıt: `00_VARLIKLAR/stok/lisans-kaydi.md` (03 belgesi 6.1 ağacına ek; müzikteki `muzik/lisans-notu.md` ile aynı mantık). Lisans sayfasının ekran görüntüsünü de al: koşullar sonradan değişebilir, itirazda elindeki kanıt indirme günündeki metindir.

```
| Dosya adı | Kaynak site | Sayfa bağlantısı | Üretici | Lisans adı | İndirme tarihi | Lisans sayfası görüntüsü | Atıf gerekli mi | Kullanıldığı video |
|-----------|-------------|------------------|---------|------------|----------------|--------------------------|-----------------|--------------------|
| stok_fatura-masa_01.mp4 | [ ] | [ ] | [ ] | [ ] | [YYYY-AA-GG] | lisans_[tarih].png | [ ] | KM-0[ ] |
```

### 4.5 Kaynak kategorileri

| Kategori | Örnek | Durum |
|---|---|---|
| **Kendi çekimin** | Telefonla üstten masa, el, kâğıt | Lisans sorunu yok; kanıt değeri var. İlk tercih |
| **Ücretsiz stok siteleri** | Pexels, Pixabay, Mixkit | İkincil kaynaklara göre üçü de ticari kullanıma izin veriyor ve atıf zorunlu tutmuyor; kısıtlar ve bazı içeriklerde farklı lisans olabileceği belirtiliyor. Lisans metinleri okunamadı **[DOĞRULA]**: [Pexels](https://www.pexels.com/license/) · [Pixabay](https://pixabay.com/service/license-summary/) · [Mixkit](https://mixkit.co/license/) |
| **Abonelikli ya da tek tek satın alınan stok** | (kategori; örnek adlar 9.2'de) | Lisans kapsamı, abonelik bitince kullanım hakkı ve YouTube'da telif talebi temizleme yöntemi plana göre değişir **[DOĞRULA]** |

### 4.6 Yapay zekâ ile üretilmiş görsel ve video

- **Kanıt yerine asla:** arayüz, sonuç, belge, "müşteri" görüntüsü üretilmez (03 belgesi 4.1).
- **Yalnızca açıkça temsilî ve gerçekçi olmayan** görseller: çizim tarzı, düz renkli, palete uygun. Gerçekçi üretilmiş sahne kullanırsan 03 belgesi 4.4 A'daki kanal kuralı devreye girer: Studio'da "Evet" + açıklamada cümle.
- Ekranda küçük etiket: "Temsilî görsel · yapay zekâyla üretildi". Politika istemese de kanal ister. Üreten aracın çıktı üzerindeki kullanım koşulunu oku (ticari kullanım, plan farkı) **[DOĞRULA]**; `lisans-kaydi.md` içine araç adı, tarih ve kullandığın istem yazılır.
- Tanınan kişi, marka, logo ya da korunan bir karaktere benzeyen çıktı kullanılmaz.

## 5. Animasyon ve hareketli grafik

### 5.1 Sabit grafik seti: tasarım tarifleri

Varlıkların listesi ve kullanım kuralı 03 belgesi 6.3'tedir; aşağıdaki ölçüler onların 1920×1080 zaman çizelgesindeki tasarım tarifidir. Renkler: 01 belgesi Bölüm 3'teki başlangıç önerisi (lacivert `#0B1F3A`, sarı `#FFD400`, beyaz `#FFFFFF`); kendi seçtiğin kodlar `00_VARLIKLAR/kapak/renk-notu.md` içindekilerdir. Ölçüler **[Tahmini]** başlangıçtır; telefonda okunabilirlik testiyle kesinleşir.

| Grafik | Tasarım | Hareket | Nasıl üretilir |
|---|---|---|---|
| **Kronometre çerçevesi** | Rakam kayıttan gelir (`sablonlar/kronometre.html`). Kurguda eklenen: kronometre penceresinin çevresine 4 px sarı çerçeve; altında lacivert şerit üstünde sarı etiket ("ELLE" / "YAPAY ZEKÂ"), harf yüksekliği tahmini 28 px | Yok; koşu boyunca sabit | Kurgu aracının şekil + metin öğesi |
| **Alt bant** | Sol alt; kenarlardan 80 px içeride; lacivert dikdörtgen tahmini 560×84 px, solunda 8 px sarı dikey şerit; beyaz metin "3 / Yapay zekâyla koşu", harf yüksekliği tahmini 36 px | Soldan 0,3 sn'de girer, 3 sn durur, 0,3 sn'de çıkar | Şekil + metin; giriş/çıkış anahtar karesi |
| **Önce / sonra bölünmüş ekran** | Ekran dikey ikiye bölünür; ortada 6 px sarı çizgi; sol üstte gri etiket "ÖNCE", sağ üstte sarı etiket "SONRA"; iki tarafta **aynı** büyütme oranı ve aynı kırpma | Çizgi ortadan açılır (0,4 sn); istenirse çizgi soldan sağa kayarak "sonra"yı açar | İki kayıt iki kanalda, her biri yarıya kırpılmış; çizgi ve etiketler şablondan |
| **Adım sayacı** | Sol üst; lacivert yuvarlak köşeli kutu tahmini 120×64 px; sarı metin "3/7". "Hızlandırıldı ×N" etiketi bunun **altında** durur | Rakam değişirken 0,2 sn büyüyüp küçülür | Metin öğesi; her madde için kopyası |
| **Formül kartı** | Tam ekran lacivert; üstte sarı başlık; altında yan yana eşit kutular (ör. 4 parça), her kutuda tek kelime + bir satır açıklama; kutu çerçevesi sarı, metin beyaz | Kutular soldan sağa 0,3 sn arayla belirir; anlatılan kutu sarı dolguya döner (metni lacivert olur) | Sunum yazılımında çizilir, saydam zeminli görüntü olarak dışa aktarılır ya da kurguda şekillerle kurulur |
| **Vurgu kutusu** | 4 px sarı çerçeve, köşeler 6 px yuvarlak, dolgu yok; hedefin 8 px dışında | 0,2 sn'de belirir, cümle boyunca durur. Yanıp sönmez | Şekil öğesi; boyutu her kullanımda elle ayarlanır |

Yerleşim kuralları: sağ üst kronometrenindir; sol üst adım sayacı ve hız etiketinin; sol alt alt bandın; **sağ alt boş kalır** (kanala filigran tanımlıysa oynatıcıda sağ altta görünür **[Yaygın gözlem]**; son 15–20 saniyede bitiş ekranı öğeleri de ekrana yerleşir: 03 belgesi 6.3). Alt orta, altyazı alanıdır; grafik koyma. Alt bandı altyazı açıkken telefonda dene: altyazı satırıyla çakışıyorsa bandı tahmini 160 px yukarı al **[Tahmini]**. Metin kutularında kenar boşluğu en az harf yüksekliğinin yarısı.

### 5.2 Şablon olarak saklama

1. Her grafiği kurgu aracında **bir kez** kur, 03 belgesi 6.1'deki `00_VARLIKLAR/proje-sablonu/` içindeki uzun video şablonuna koy; ayrıca aracın projeler arası paylaşılan öğe kutusuna kaydet (DaVinci Resolve'da bu işi gören özellik "Power Bin" adıyla geçer **[DOĞRULA: kullandığın sürümde]**).
2. Dışarıda üretilen görseller (formül kartı zemini, etiketler) saydam zeminli PNG olarak `00_VARLIKLAR/grafik/` içinde; kaynak dosyası (sunum ya da tasarım dosyası) yanında. Adlandırma: `GR_altbant_v1`, `GR_formul-4parca_v1`. Tasarım değişirse sürüm artar, eski sürüm silinmez; yayınlanmış videonun projesi eski sürümü arar.
3. Şablonda her grafiğin metni yer tutucudur ("BÖLÜM ADI"); yayına yer tutucuyla çıkmamak için kurgu kapısına madde eklendi (Bölüm 10).
4. Dikey şablonda aynı setin 1080×1920 sürümü ayrı durur; yatay grafiği dikeye sığdırmaya çalışma (yerleşim 6.8).

### 5.3 Kod bilmeden hareketli grafik yolları

| Yol | İş | Ne zaman |
|---|---|---|
| **Kurgu aracının kendi metin, şekil ve anahtar kare araçları** | Konum, boyut ve saydamlığı iki zaman noktasında tanımlarsın; araç arasını doldurur | Sabit setin tamamı. İlk tercih |
| **Sunum yazılımı** (PowerPoint, Keynote, Google Slaytlar, LibreOffice Impress) | Kartı slayt olarak çiz; görüntü olarak dışa aktar. Basit giriş animasyonlarını slaytta oynatıp ekran kaydıyla al | Formül kartı, şema, tablo |
| **Tarayıcıda açılan sayfa + ekran kaydı** | `kronometre.html` ile aynı yöntem: bir sohbet asistanına "lacivert zeminde, sarı çubukların sırayla dolduğu tek dosyalık bir sayfa" yazdır, tarayıcıda aç, kayıt aracıyla çek | Sayaç, dolan çubuk, basit veri grafiği. Kanalın konusuyla da uyumlu |
| **Tablo yazılımının grafiği** | Ölçüm verisini (`olcum.md`) tabloya gir, çubuk grafik çiz, renkleri palete çevir, görüntü olarak al | Süre karşılaştırması |
| **Tarayıcı tabanlı tasarım aracı** | Hazır hareketli öğeler | Yalnızca öğenin lisansı ve saydam dışa aktarma koşulu okunduysa **[DOĞRULA]** (03 belgesi 3.2, Canva satırı) |

Veri grafiği kuralları: eksen sıfırdan başlar; iki çubuk aynı ölçekte; sayı çubuğun üstünde yazılı ve `olcum.md` ile aynı; yuvarlama 03 belgesi Aşama 7'deki kurala göre; "İlk kurulum" süresi ayrı çubuk ya da ayrı satır olarak görünür.

### 5.4 Açıklayıcı animasyon ne zaman değer

Üç sorunun üçüne de "evet" ise yap: (1) anlatılan şey ekran kaydıyla **gösterilemiyor** mu (soyut ilişki, görünmeyen süreç); (2) açıklama **en az üç videoda** yeniden kullanılacak mı (ör. "yeni sohbet neden önemli"); (3) üretimi **tahmini 45 dakikanın** altında mı **[Tahmini]**. Birine "hayır" ise tek karelik şema + seslendirme yeterlidir. Karakter animasyonu, 3B, logo animasyonu ve intro bu kanalda yoktur (03 belgesi 6.3: "Intro yok"). Yapılan her açıklayıcı animasyon `00_VARLIKLAR/grafik/aciklayici/` içine girer ve kullanıldığı videolar not edilir.

## 6. Kurgu montajı

Kurgunun adım sırası ve süreleri 03 belgesi Aşama 6'da, kanal düzeni ve ön ayarlar 6.4'tedir. Aşağıdakiler yüzsüz üretimin eklediği ayrıntılardır.

### 6.1 Zaman çizelgesi düzeni ve dört temel işlem

Kanal düzeni 03 belgesi 6.4'tedir (V1 ekran, V2 büyütme/kopya, V3 grafik, V4 altyazı; A1 ses, A2 müzik, A3 efekt). Yüzsüz üretimin kullanım kuralı ve eki:

- **V1 ana görüntüdür:** ekran kaydı (K1) ve onun yerini alan tam ekran kart (K2), animasyon (K3), bağlam sahnesi (K4). Böylece "V1'de boşluk var mı" tek kontroldür. Klipleri katmana göre renklendir (K1 mavi, K2 sarı, K3 yeşil, K4 gri): zaman çizelgesine uzaktan bakınca 1.1'deki oranı görürsün. **V2:** yakınlaştırılmış kopya ve önce/sonra'nın ikinci yarısı.
- **Ek iki kanal (03 belgesi 6.4'e öneri; kabul edilirse orası ve proje şablonu güncellenir):** V2 ile V3 arasına `KAPAT` (kapatma kutuları) ve `KR` (kronometrenin kırpılmış kopyası). Alttan üste sıra: V1 → V2 → KAPAT → KR → V3 → V4. Aynı anda yakınlaştırma, kutu ve kronometre kopyası gerektiğinde tek kanala sığmazlar; kutu kopyanın altında kalırsa veri sızar.
- **A1:** Yol B'de bölüm bölüm `_tts_temiz.wav` dosyaları. **A3:** efektler ve masa çekiminin ortam sesi.

DaVinci Resolve'da dört temel işlem (panel ve menü adları İngilizce arayüze göredir **[DOĞRULA: sürümünde]**):

- **Yakınlaştırma:** klibi seç → Inspector → Transform → Zoom ve Position'ın yanındaki anahtar kare (elmas) düğmesi; büyütmenin başında ve sonunda birer değer gir; yumuşak geçiş için anahtar kareye sağ tıkla → Ease In / Ease Out.
- **Hızlandırma:** bıçak aracıyla beklemenin başından ve sonundan kes → ortadaki parçaya sağ tıkla → Change Clip Speed → yüzdeyi gir (×8 için %800); arkadaki kliplerin kayması için "Ripple" seçeneği işaretli olsun.
- **Opak kutu:** Effects → Generators → Solid Color'ı `KAPAT` kanalına sürükle → Inspector'da rengi lacivert yap → Cropping ile boyutlandır, Transform → Position ile yerleştir; hareket ediyorsa Position'a anahtar kare.
- **Kronometre kopyası:** süreli koşu klibini Alt (macOS: Option) tuşuyla `KR` kanalına sürükleyip kopyala → Inspector → Cropping ile yalnızca kronometreyi bırak. Yakınlaştırma V1/V2'deki klibe uygulanır, kopyaya uygulanmaz.

### 6.2 Ses merkezli kurgu sırası (Yol B farkları)

1. Bölüm ses dosyalarını A1'e diz; aralarına `[D2]`, kart yerlerine `[D3]` sürelerini koy. Yol B'de "yanlış denemeleri atma" adımı yoktur; onun yerine **okunuş kontrolü** vardır: A1'i baştan sona dinle, hatalı cümleyi şimdi yeniden üret (2.5, madde 3). Görüntü dizildikten sonra ses değişirse her şey kayar.
2. A1'i kilitle. Bundan sonra ses yalnızca tek cümle değiştirilerek güncellenir; yeni cümlenin süresi büyük olasılıkla eskisinden farklı çıkar, o bölümün görüntüsü yeniden hizalanır.
3. Kanıt kayıtlarını (3.3) sese hizala: önce süreli koşu, çünkü gizli kesim kaldırmayan odur. Ses koşudan kısaysa 3.5'teki iki tablo; uzunsa cümleyi kısalt ya da süre dışı kayda taşı.
4. Anlatım kayıtlarını yerleştir; eksik kalan görüntüyü not et, hepsini tek oturumda sese göre çek (3.3).
5. Sonra 03 belgesindeki sıra: yönlendirme → sabit grafikler → müzik → altyazı → telefonda izleme.

### 6.3 Tempo

Tek kaynak `sablonlar/senaryo-sablonu.md`: ekranda en geç tahmini 20–30 saniyede bir görsel değişiklik. Katmana göre ek başlangıç değerleri, hepsi **[Yaygın gözlem]** ve **[Tahmini]**; kanalın kendi tutma grafiğiyle düzeltilir:

| Durum | Başlangıç değeri |
|---|---|
| Hook (ilk 30 sn) | 4–8 saniyede bir değişiklik (kesme, büyütme ya da grafik) |
| Ekran kaydı, anlatım bölümü | 10–20 saniyede bir büyütme ya da vurgu |
| Süreli koşu | Gizli kesim yok; her kesim ve hızlandırma etiketli, kronometre atlaması görünür (3.5). Değişiklik büyütme ve etiketle gelir |
| Tam ekran kart | Okuma süresi: kelime başına tahmini 0,4 sn + 1 sn. İstisna: "yapamadığı şey" kartı ve prompt kartı 03 belgesi 6.3'teki sürelerle |
| Bağlam sahnesi | Plan başına 3–5 sn |
| Sessiz ekran | Tek seferde en çok tahmini 6–8 sn; uzunsa müzik hafifçe yükselir |

Yüzsüz videoda yüzün taşıdığı ritmi ses taşır. Sentetik ses tekdüze kalabildiği için **[Yaygın gözlem]** değişimi görüntü ve sessizlik üstlenir: bölüm sonlarında yarım saniyelik tam sessizlik, "yapamadığı şey" kartından önce müziğin kesilmesi (03 belgesi 6.3).

### 6.4 Altyazı

İki yol 03 belgesi Aşama 6, adım 6'dadır. Yol B'de tercih **senaryodan senkronizasyondur**: görünen metin zaten kelimesi kelimesine doğrudur ve sentetik ses temiz olduğu için hizalama kolaylaşır **[Yaygın gözlem]**; Türkçe için çalışıp çalışmadığı 03 belgesi 0.1'deki gizli test videosunda sınanır **[DOĞRULA]**.

- Altyazı kaynağı her zaman **görünen metindir**, okunuş metni değil; okunuş yazımı altyazıya sızarsa "çet ci pi ti" ekranda görünür. Sayılar altyazıda rakamla ("14 dakika"), seste yazıyla; ikisi aynı değerdir.
- Seslendirme aracın altyazı ya da zaman damgası dosyası veriyorsa kullanılabilir **[DOĞRULA: seçtiğin araçta]**; içindeki metni görünen metinle değiştir. Yatay videoda altyazı gömülmez, dosya olarak yüklenir; dikeyde gömülür (03 belgesi 6.4).

### 6.5 Müzik ve efekt

Kaynak ve seviye 03 belgesi 3.1, 6.3 ve 6.4'tedir. Ek: sentetik sesin altında müzik, sesin "boşlukta" durmasını azaltır **[Yaygın gözlem]**; yine de konuşmanın belirgin altında. YouTube Ses Kitaplığı'ndaki bazı parçalar atıf ister; parça sayfasındaki lisans türünü `muzik/lisans-notu.md` içine yaz, gerekiyorsa atfı açıklamaya ekle **[Resmî — sayfada teyit et: Studio → Ses Kitaplığı, lisans sütunu]**. Ücretsiz efekt sitelerinden alınan seslerin lisansı da kayda girer; "telifsiz" yazan bir video ya da oynatma listesinden müzik indirilmez.

### 6.6 Renk ve ses seviyesi hedefleri

- **Renk:** ekran kaydına renk düzeltme uygulanmaz (arayüz renkleri gerçeği göstersin). Yalnızca bağlam sahneleri palete yaklaştırılır. Açık temalı arayüz ile lacivert kartlar arasındaki parlaklık sıçraması göz yorar; kartlara 0,2 sn'lik geçiş koy. Çekimde açık ya da koyu temadan birini seç ve bütün videolarda aynı kalsın.
- **Ses yüksekliği:** hedef 03 belgesi 6.4'te yazılıdır ve **[Yaygın gözlem]** düzeyindedir. YouTube'un oynatmada ses yüksekliğini normalleştirdiği, yüksek gelen içeriği kıstığı ama düşük geleni yükseltmediği yaygın olarak aktarılır; resmî bir sayfayla teyit edilemedi **[DOĞRULA]**. Pratik kontrol: videoyu gizli olarak yükle, oynatıcıda sağ tık → "Meraklısı için istatistikler" penceresinde ses satırına ("Volume / Normalized" ve yanındaki "content loudness" değeri) bak; eksi değer videonun hedefin altında kaldığını ve kısılmadığını gösterir **[Yaygın gözlem]**. Ardından aynı nişten iki videoyla art arda dinle; dinlerken oynatıcı ayarlarındaki "Sabit ses düzeyi" seçeneğini üç videoda da kapalı tut, açıkken duyduğun seviye ölçtüğün seviye değildir **[DOĞRULA: ayarın adı ve cihazındaki varlığı]**.
- Yol B'de ses dosyaları araçtan farklı seviyelerde gelebilir; ölçümü birleştirilmiş dosyada yap, parçada değil.

### 6.7 Dışa aktarma

Ayarlar 03 belgesi 6.4'tedir. Başlangıç değerleri, [YouTube'un önerilen yükleme kodlama ayarları](https://support.google.com/youtube/answer/1722171) sayfasının bilinen içeriğine göre **[Resmî — sayfada teyit et]**: kap MP4, video H.264, ses AAC-LC, 48 kHz, stereo; 1080p ve 30 kare/sn için video 8 Mb/sn, stereo ses 384 kb/sn. Ek kontroller:

- Sentetik ses tek kanallıysa iki kanala eşit dağıt.
- Ekran kaydında ince yazı düşük bit hızında bozulur; önerilen değerin altına inme. Dışa aktarılan dosyada en küçük yazılı kareyi durdur ve %100'de bak; dosyada bozuksa bit hızını yükselt. Dosya temiz ama yüklenmiş videoda yazı bozuksa 1440p dışa aktarmayı bir kez dene **[Yaygın gözlem]**; kalıcı olacaksa 03 belgesi 6.4 güncellenir.
- YouTube yükleme sonrası yeniden kodlar; yüksek çözünürlük işlemesi bitmeden videoyu kimseye gösterme ve zamanlamayı buna göre yap (`kalite-kontrol-listeleri.md` Bölüm 7'deki "yeterince önce yüklendi" maddesi).

### 6.8 Kısa videolar: yüzsüz üretimin farkları

Kesim adımları 03 belgesi Aşama 10'da, türler ve açılış 01 belgesi 4.4'tedir. Ek:

1. **Görüntü** uzun videonun ham kaydından yeniden çerçevelenir. Süre iddiası taşıyan kısa videoda kronometre kadraja sığmıyorsa aynı kayıttan kırpılmış kopyası başlık bandının hemen altına konur; rakam yazılmaz.
2. **Yerleşim (1080×1920):** üstte başlık bandı, ortada ekran bölgesi, altta gömülü altyazı (03 belgesi 6.4'teki dikey stil). Alt kenar ve sağ kenar platform arayüzüyle örtülür; oraya yazı ve kronometre koyma. Güvenli alanı tahminle değil, gizli yüklenmiş bir denemede telefonda gör **[DOĞRULA: güncel arayüz]**.
3. **Ses, Yol A:** yeni açılış cümlesi kendi sesinle kaydedilir (03 belgesi Aşama 10, adım 4).
4. **Ses, Yol B:** kısa videonun görünen metni ayrı yazılır; ondan `02_senaryo/KM-[NO]_K1_tts-metni.md` türetilir (2.3) ve **tek parça** üretilir. Ses kimliği ve ayarlar uzun videoyla aynı; açılış cümlesi üç kez üretilir. Uzun videonun ses dosyasından kesilip yapıştırılmaz (01 belgesi 4.4: seslendirme ayrıdır; 7.5). Ek süre tahmini kısa video başına 8 dk **[Tahmini]**.
5. **Gömülü altyazı** görünen metinden gelir; yazımı elle düzelt, sayılar rakamla.
6. **Beyan ve etiket, Yol B:** Shorts yüklemesinde de Studio beyanı "Evet" + açıklamada sentetik ses satırı (7.2, 7.4); diğer platformlarda yükleme ekranındaki etiket 03 belgesi 4.4 C'ye göre. Sıra: önce YouTube, sonra diğerleri; her birinde ne işaretlediğini `yayin-metaverisi.md` Bölüm 9'a yaz.

## 7. Yayına hazırlık

Yayınlama adımları 03 belgesi Aşama 8'de, doldurulacak form `sablonlar/yayin-metaverisi.md` dosyasında, kapı `sablonlar/kalite-kontrol-listeleri.md` Bölüm 7'dedir. Yüzsüz üretimin eklediği işler:

### 7.1 Dışa aktarılan dosyanın kontrolü (10 dk + video süresi)

1. Dosya süresi kurgu süresiyle aynı; sonda fazladan siyah kare ya da sessizlik yok.
2. İlk kare siyah değil: Shorts akışında ve bazı paylaşım önizlemelerinde ilk kare görünür **[Yaygın gözlem]**. Kapak her zaman elle yüklenir (01 belgesi Bölüm 3); otomatik kare seçeneklerine güvenilmez.
3. Son 30 saniyede ses–görüntü kayması yok (değişken kare hızlı kaynak belirtisi, 3.2).
4. Kare kare gezinme: her kapatma kutusu yerinde (3.6); kişisel veri sızıntısı yok.
5. Telefonda 1× izleme (03 belgesi Aşama 6, adım 7): bu, yüzsüz videoda en önemli kontroldür çünkü videonun tamamı okunacak yazıdır.

### 7.2 Kapak, başlık, açıklama, bölümler

Kurallar 01 belgesi Bölüm 3 ve `yayin-metaverisi.md` Bölüm 1–4'tedir. Yüzsüz kanal için ek: kapakta yüzün yerini "X → Y" çiftindeki gerçek ekran parçası tutar; stok insan fotoğrafı ve üretilmiş yüz kullanılmaz. Yol B'de açıklamaya şu sabit satır eklenir (yeri: "Nasıl ölçtüm" bloğunun altı):

> Seslendirme sentetiktir ([araç adı]). Ekran kayıtları, ölçümler ve senaryo bana aittir.

### 7.3 Altyazı dosyası

`KM-[NO]_SON_tr.srt` ya da senkronize edilen görünen metin (6.4). Yüklemeden sonra üç noktada (baş, orta, son) zamanlamayı kontrol et; `yayin-metaverisi.md` Bölüm 8'deki satırı işaretle.

### 7.4 "Değiştirilmiş veya sentetik içerik" beyanı

Politikanın özeti, karar tablosu ve kanal kuralı 03 belgesi 4.4 A'dadır; Studio'daki alan `yayin-metaverisi.md` Bölüm 8'de işaretlenir. Kaynaklar **[Resmî — sayfada teyit et]**: [YouTube Yardım: değiştirilmiş veya sentetik içeriğin beyanı](https://support.google.com/youtube/answer/14328491) · ["Bu içerik nasıl üretildi" açıklamaları](https://support.google.com/youtube/answer/15447836) · [YouTube Blog duyurusu](https://blog.youtube/news-and-events/disclosing-ai-generated-content). Arama özetlerinde ve ikincil kaynaklarda görülen çerçeve: beyan, gerçek sanılabilecek gerçekçi içerik içindir; başkasının sesini klonlayarak seslendirme beyan gerektiren örneklerdendir; gerçekçi olmayan içerik ve küçük düzeltmeler kapsam dışıdır; beyan tek başına videonun erişimini ve para kazanma uygunluğunu etkilemez; YouTube beyan edilmemiş içeriğe kendisi de etiket koyabilir. Hazır bir sentetik sesle yapılan anlatımın tek başına beyan gerektirip gerektirmediği resmî örneklerde açıkça görülemedi; ikincil kaynaklar çelişiyor **[DOĞRULA]**. Sayfa okunana kadar kanal kuralı (politikadan sıkı) geçerlidir: Yol A'da "Hayır"; Yol B'de (hazır sentetik ses ya da kendi ses klonun) **"Evet"** + 7.2'deki açıklama satırı.

03 belgesindeki tabloda olmayan, bu belgenin getirdiği durumlar ve Studio'daki beyan (gerçekçi üretilmiş görsel 4.6'da; o tabloya göre "Evet"):

- Açıkça çizim tarzı temsilî görsel, hareketli grafik, stok görüntü → Hayır; ekrandaki "temsilî görsel" etiketi kanal kuralıdır
- Hızlandırma, bekleme kesme, kapatma kutusu, yakınlaştırma → Hayır (küçük düzeltme); "hızlandırıldı ×N" etiketi kanal kuralıdır

Beyan ile para kazanma ayrı konulardır (04 belgesi 2.5). Kısa videolar için 6.8, madde 6.

### 7.5 Para kazanma politikası riski: özgün olmayan ve tekrarlayan içerik

Politikanın özeti 03 belgesi 4.4 B'de, gelir tarafı 04 belgesi 2.5–2.6'dadır; kaynak **[Resmî — sayfada teyit et]** [YouTube kanal para kazanma politikaları](https://support.google.com/youtube/answer/1311392). Arama özetlerine göre kural yapay zekâ kullanımını değil, toplu üretilmiş, şablondan çıkmış gibi görünen ve videolar arasında anlamlı fark taşımayan içeriği hedefler; ikincil kaynaklarda en sık verilen örnek, başkasının metnini metin okuma motoruna verip stok görüntüyle yayınlamaktır. Yüzsüz olmak tek başına ölçüt değildir; riskli olan 03 belgesi 4.4 B'deki desendir. İkincil kaynaklarda yüzsüz ve sentetik sesli kanalların ret örnekleri sık anlatılır; oranı bilinmiyor.

Yol B bu kanalın risk yüzeyini büyütür: "sentetik ses + hazır görsel + asgari insan katkısı" deseninin üç ayağından birini eklemiş olursun. Diğer ikisini sıfırda tutan şeyler:

| Riskli desen | Bu kanalda karşılığı | Kanıtı nerede |
|---|---|---|
| Başkasının içeriğini okutmak | Senaryo kendi görevinden, kendi ölçümünden yazılır | `olcum.md`, ham kayıt (03 belgesi 6.2: silinmez) |
| Stok görüntü üstüne anlatım | Görüntünün en az %70'i kendi ekran kaydın (1.1) | Zaman çizelgesi, ham kayıt |
| Videolar arasında fark yok | Her videoda farklı görev, farklı veri, gerçekten yaşanmış farklı "yapamadığı şey" | `performans-kaydi.md`, `arac-ciktilari.md` |
| Ölçekte üretim | Haftada 1 uzun video; ritim 02 belgesi B2 | Yükleme geçmişi |
| İnsan katkısı görünmüyor | Elle koşu, kâğıt notlar, masa çekimi, yorumlara yazılı cevap, düzeltme notları | Videonun kendisi |
| Başkasının görüntüsünü kullanmak (ayrı başlık: yeniden kullanılan içerik; 03 belgesi 4.4 B) | Stok plan en çok %5 ve plan başına 5 sn (1.1, 4.1); başka kanalın kaydı ya da araç tanıtım videosundan görüntü yok | `stok/lisans-kaydi.md` |

Uygulama: Yol B'deyken haftalık yükleme sayısını artırma; kısa videoların seslendirmesini uzun videodan kopyalama (6.8). İncelemeci yalnızca yayındaki içeriği görür; `tts-kaydi.md` ve ham kayıtlar ret hâlinde itirazda üretim sürecini göstermek için saklanır **[Yaygın gözlem; itiraz yöntemi DOĞRULA]**. İnceleme sonucunu hiçbir önlem garanti etmez; bu liste riski azaltır, kaldırmaz.

### 7.6 Telif kontrolleri

Genel bilgidir, hukuki tavsiye değildir. Yayından önce bakılacak kayıtlar:

- **Lisans kayıtları:** sentetik ses planı → `ses-kimligi.md` (2.1) · müzik ve efekt → `muzik/lisans-notu.md` (6.5) · stok görüntü ve üretilmiş görsel → `stok/lisans-kaydi.md` (4.4, 4.6) · yazı tipinin videoda ve kapakta ticari kullanım izni → `kapak/renk-notu.md`.
- **Ekrandaki yazılım arayüzü ve logolar:** eğitim ve inceleme amaçlı gösterim yaygındır **[Yaygın gözlem]**; logo kapakta ana öğe olmaz (01 belgesi Bölüm 3), "resmî ortak" izlenimi verilmez.
- **Üçüncü taraf içerik:** başkasının videosu, makalesi, e-postası kayda girmez; kurgusal veri kullanılır (03 belgesi 4.5).

Yükleme akışındaki "Kontroller" adımı telif taraması yapar; reklam uygunluğu taraması yalnızca İş Ortağı Programı'ndaki kanallarda çıkar **[Resmî — sayfada teyit et: Studio yükleme akışı]**. Sonuç çıkmadan görünürlüğü zamanlama. Temiz sonuç, yayından sonra talep gelmeyeceğini garanti etmez; talep gelirse `lisans-kaydi.md` içindeki ekran görüntüsüyle itiraz edilir.

### 7.7 Zamanlama

Gün ve ritim: 02 belgesi B2 (perşembe; tek kaynak). Yüzsüz üretimin eklediği tek şey sıra (adım adları **[DOĞRULA: Studio arayüzü]**): dosya kontrolü (7.1) → yüklemeyi başlat → Ayrıntılar: metaveri + beyan (7.4) → Kontroller adımının sonucunu bekle (7.6) → Görünürlük: özel (gizli) olarak kaydet → işlemenin bitmesi → oynatıcıda ses ve altyazı kontrolü (6.6, 7.3) → görünürlüğü "zamanlanmış" yap.

## 8. Uçtan uca örnek: KM-001, kameraya çıkmadan

Örnek `senaryolar/01-chatgptyi-yanlis-kullaniyorsun.md` üzerinedir (tahmini 12:15). Yol B varsayılmıştır; Yol A'da 8–10. satırların yerini 03 belgesi Aşama 5 (55 dk) alır. Parantezdeki süreler 03 belgesinin bütçesidir; diğerleri **[Tahmini]** ve ilk videoda ölçülecek. Araç adları 03 belgesi 3.3'teki sıfır bütçe setidir.

| # | Adım | Araç | Süre (dk) | Çıktı dosyası |
|---|---|---|---|---|
| 1 | Brief, ön test (senaryo 01, 2.2–2.5) ve senaryo | Markdown şablonu, sohbet asistanı, tablo yazılımı | 45 + 90 (03 belgesi Aşama 3) | `01_brief/video-brief.md`, `02_senaryo/senaryo_v1.md` |
| 2 | Elle koşu: teklif e-postası yapay zekâsız yazılır, sorular kâğıda not edilir | OBS Studio + `kronometre.html` | görev süresi + 15 (Aşama 3) | `03_ham/KM-001_elle-kosu_ham.mp4`, `olcum.md`, kâğıt not |
| 3 | Ön kontrol, masaüstü hazırlığı (3.1), 10 saniyelik deneme kaydı | Çekim profili, çekim hesabı | 8 (Aşama 4) + 10 | — |
| 4 | Kayıt A: süreli akış, tek kesintisiz (senaryo 01, 2.6); hemen ardından `olcum.md` | OBS Studio + `kronometre.html` | 15 + 5 (Aşama 4) | `03_ham/KM-001_b3-kronometre-kosusu_ham.mp4`, `arac-ciktilari.md` |
| 5 | Kayıt B (dört prompt × üç deneme = 12 yeni sohbet) ve Kayıt C (kötü örnekler, ayrı sohbetler); süre dışı | OBS Studio + `kronometre.html` (karede, durmuş) | 40–60 (Aşama 4'teki "ek çekimler" bütçesi: 12) | `03_ham/KM-001_ek_b-p0…p3_ham.mp4`, `KM-001_ek_c-…_ham.mp4` |
| 6 | Yer tutucuları doldur, karar kurallarını uygula (senaryo 01, 2.8), senaryoyu kilitle | Markdown | 10 (Aşama 4) | `02_senaryo/senaryo_KILIT.md` |
| 7 | Masa çekimi: yapışkan not + elle koşudaki gerçek kâğıt, üstten, yüz yok; bir yatay bir dikey (senaryo 01, 5:40) | Telefon, masa lambası | 15 | `03_ham/KM-001_ek_masa_yatay.mp4`, `_dikey.mp4` |
| 8 | Okunuş metnini türet: 2.3'teki prompt, sözlük, `[D]` işaretleri; sayıları `olcum.md` ile karşılaştır | Sohbet asistanı, `telaffuz-sozlugu.md` | 15 | `02_senaryo/KM-001_tts-metni.md` |
| 9 | Sesi 13 bölüm hâlinde üret, parça sınırlarını dinle, hatalı cümleleri yeniden üret; hook üç kez (2.5) | Seçilen seslendirme aracı | 40 (ilk videoda daha uzun) | `04_ses/ham/KM-001_b1-hook_tts_t1.wav` … , `tts-kaydi.md` |
| 10 | Ses sonrası işlem ve baştan sona dinleme (2.6) | Audacity | 10 + 10 | `04_ses/temiz/KM-001_b1-hook_tts_temiz.wav` … |
| 11 | Kurgu 1: şablonu aç, sesi diz, okunuş kontrolü, A1'i kilitle (6.2) | DaVinci Resolve | 20 (Aşama 6, adım 1) | `05_proje/` |
| 12 | Kurgu 2: Kayıt A'yı hizala, bekleme ve kesimleri etiketle (3.5); eksik anlatım görüntülerini sese göre çek (3.3) | DaVinci Resolve, OBS Studio | 30 (adım 2) + 15 | `03_ham/KM-001_ek_anlatim-…_ham.mp4` |
| 13 | Kurgu 3: yakınlaştırma, vurgu, kapatma kutuları (3.4, 3.6, 6.1) | DaVinci Resolve | 30 (adım 3) | — |
| 14 | Kurgu 4: sabit grafikler: adım sayacı 1/7–7/7, önce/sonra bölünmüş ekran, karşılaştırma tablosu, "yapamadığı şey" kartı, prompt kartı | Proje şablonu (5.2) | 15 (adım 4) | — |
| 15 | Müzik, seviye, altyazı (6.4–6.6) | DaVinci Resolve, YouTube Ses Kitaplığı, görünen metin | 28 (adım 5–6) | `06_cikti/KM-001_SON_tr.srt` ya da görünen metin |
| 16 | Dışa aktar, dosya kontrolü (7.1), telefonda 1× izleme, düzeltme | DaVinci Resolve, telefon | 25 (adım 7) + 10 | `06_cikti/KM-001_SON_[tarih].mp4` |
| 17 | Kapak: gerçek ekran parçasıyla "Önce / Sonra" | Kapak şablonu | 25 (Aşama 7) | `06_cikti/KM-001_kapak_A.png`, `_B.png` |
| 18 | Metaveri, prompt dosyası, yükleme, beyan "Evet" + açıklama satırı, Kontroller, zamanlama (7.7) | YouTube Studio, `yayin-metaverisi.md` | 30 (Aşama 8) | `08_yayin/yayin-metaverisi.md` |
| 19 | İki kısa video (6.8): görüntü ham kayıttan, seslendirme ayrıca üretilir | Dikey zaman çizelgesi, seslendirme aracı | 50 (Aşama 10) + 2 × 8 | `07_kisa/KM-001_K1_…_dikey.mp4` |

**Toplam (3–18. satırlar, çekimden yayın hazırlığına):** tahmini 6 sa 55 dk (5. satıra göre 6 sa 45 dk – 7 sa 5 dk). 03 belgesi 2.1'in aynı aşamalar için bütçesi 5 sa 10 dk'dır (çekim 50 + seslendirme 55 + kurgu 150 + kapak 25 + yayın 30). **Fark: tahmini +1 sa 45 dk [Tahmini]**; dökümü: Kayıt B ve C +28–48 dk ve masa çekimi +15 dk (senaryo 01'e özgü), masaüstü hazırlığı +10, sese göre ek anlatım çekimi +15, dosya kontrolü +10 (bu belgenin ekleri), Yol B seslendirmesi +20. Yol A'da fark tahmini +1 sa 25 dk'dır. Takvimde yeri: pazartesi oturumu (03 belgesinde çekim + seslendirme, 1 sa 45 dk) 3–10. satırlarla tahmini 3 sa 10 dk'ya çıkar; sığmıyorsa 5 ve 7. satırlar pazar günü senaryodan sonraya alınır. Salıya +15 dk, çarşambaya +10 dk eklenir. Haftalık bütçenin tek kaynağı 03 belgesi 2.1'dir; fark ilk videoda ölçülür, doğrulanırsa orası güncellenir.

**Kronometre notu.** Kronometre çekimde kayda gömülür (03 belgesi Aşama 4); senaryo 01 2.1'deki eski "kurgu grafiğidir" ifadesi 2026-11-16'da buna göre düzeltildi. Kayıt B ve C çekilirken `kronometre.html` karede **durmuş hâlde** açık tutulur (03 belgesi 6.3: süre dışı kayıtlarda kronometre durmuş görünür); sayfa durduğunda rakamları kendiliğinden gri gösterir (01 belgesi 6.1). Kurguda yalnızca "Ayrı sohbet · süre dışı" etiketi eklenir; rakam yazılmaz, rengi kurguda değiştirilmez.

Bu videoda katman dökümü (senaryo 01'in süre dökümüne göre, **[Tahmini]**): ekran kaydı ≈ %86; tam ekran kartlar (karşılaştırma, "yapamadığı şey" kartı, prompt kartı) tahmini 60–75 sn ≈ %8–10; açıklayıcı animasyon yok; bağlam sahnesi 30 sn (masa çekimi, kendi görüntün) ≈ %4; stok plan yok.

Yol B'nin seslendirme toplamı (8–10. satırlar) tahmini 75 dakikadır; 03 belgesindeki kendi sesle 55 dakikadan **kısa değildir.** 03 belgesi 4.3'teki "haftada 20–30 dk kazanç" tahmini bu yüzden ilk videolar için geçerli sayılmaz; iki tahmin de ölçülene kadar **[Tahmini]** kalır. Sözlük oturdukça sürenin düşmesi beklenir; üçüncü videoda hâlâ 55 dakikanın üstündeyse Yol B'nin süre gerekçesi yoktur, geriye yalnızca ortam ve gizlilik gerekçeleri kalır (0. bölümdeki ölçüt 2).

## 9. İki araç seti

Genel araç seti, doğrulama tablosu ve "üç video üst üste ölçülmüş darboğaz olmadan satın alma" kuralı 03 belgesi Bölüm 3'tedir. Aşağıdakiler yüzsüz üretimin eklediği satırlardır. Fiyat yazılmadı; "ücretsiz" bilgisi yalnızca 03 belgesi 3.2'de durumu yazılı araçlar için verildi.

### 9.1 Sıfır bütçe seti

| Araç | Bu kanalda tam olarak ne için | Durum |
|---|---|---|
| OBS Studio + `sablonlar/kronometre.html` | Süreli koşuyu ve anlatım kayıtlarını sabit kare hızında, süre görüntünün parçasıyken kaydetmek | Açık kaynak, ücretsiz (03 belgesi 3.2) |
| Telefon kamerası | Üstten masa çekimi; stok yerine kendi bağlam sahnen | — |
| Kendi sesin + Audacity (Yol A) | Seslendirme. **Sıfır bütçede yayınlanabilirliği kesin olan tek seslendirme yolu** | Açık kaynak, ücretsiz (03 belgesi 3.2) |
| Bir seslendirme aracının ücretsiz kullanımı | Yalnızca 2.2'deki test; ücretsiz planda üretilen ses yayına girmez | Örnek araçta (ElevenLabs) ücretsiz planın ticari kullanım hakkı vermediği bilinir **[DOĞRULA: fiyat ve koşullar sayfası]** |
| Yol B için sıfır bütçe adayı: SSML'li bulut metin okuma servisinin aylık ücretsiz kotası | Yayın sesi | Kota miktarı, ödeme yöntemi şartı ve ticari kullanım koşulu doğrulanamadı **[DOĞRULA]**; doğrulanana kadar sıfır bütçede yayınlanabilir Yol B yoktur |
| DaVinci Resolve (ücretsiz sürüm) | Ses merkezli kurgu, sabit grafik seti, kapatma kutuları, dikey sürüm | Ücretsiz sürüm var (03 belgesi 3.2) |
| LibreOffice Impress ya da elindeki sunum yazılımı | Formül kartı, şema ve tabloyu çizip görüntü olarak almak | LibreOffice açık kaynak ve ücretsizdir (uzun süredir sabit bilgi) |
| Tarayıcı + sohbet asistanı | Okunuş metnini türetmek (2.3); tek dosyalık hareketli sayfa (sayaç, çubuk) üretip ekran kaydıyla almak | — |
| Altyazı, müzik, kapak | 03 belgesi 3.3'teki setle aynı: senaryodan senkronizasyon ya da Buzz · YouTube Ses Kitaplığı · GIMP ya da tarayıcı tabanlı tasarım aracı | 03 belgesi 3.2 |
| Pexels / Pixabay / Mixkit | Yalnızca kendi çekimin yoksa, tek bağlam planı | Lisans metni **[DOĞRULA]** (4.5) |

### 9.2 Rahat çalışma seti

Her satır ölçülmüş bir darboğaza bağlıdır. Örnek adlar yalnızca aramaya başlangıç içindir: 03 belgesi 3.2'deki doğrulama tablosunda yoklar, özellikleri ve koşulları doğrulanmadı; 3.2'deki 15 dakikalık kabul testinden geçmeden alınmaz **[DOĞRULA]**.

| Ölçülen darboğaz | Eklenecek şey | Bu kanalda tam olarak ne için |
|---|---|---|
| Yol B seçildi ve test eşiği geçildi | Üretken ses platformunun ticari kullanıma izin veren planı (örnek: ElevenLabs; plan koşulu **[DOĞRULA]**) | Tek sabit sesle anlatım ve tek cümle düzeltmesi |
| Duraklama ve okunuşu elle düzeltmek her videoda 20 dakikayı aşıyor | SSML destekli bulut metin okuma servisi (Azure AI Speech, Google Cloud Text-to-Speech ya da Amazon Polly; seçtiğin seste SSML desteği **[DOĞRULA]**) | Duraklamayı ve okunuşu metnin içinde işaretleyerek ses almak |
| Yakınlaştırma ve imleç vurgusu kurguda 30 dakikayı aşıyor | Otomatik yakınlaştırma ve imleç vurgusu olan ticari ekran kayıt aracı (örnek: Screen Studio, Camtasia) | Anlatım kayıtlarında yönlendirme süresini kısaltmak. Süreli koşu yine kronometre karedeyken, kesintisiz kaydedilir |
| Kendi çekimin yetmiyor, ücretsiz sitelerde aynı planlar dönüyor | Abonelikli stok kitaplığı (örnek: Storyblocks, Envato, Artlist) | Videoda en çok bir iki bağlam planı |
| Ses Kitaplığı'nda uygun parça tekrar ediyor | Lisanslı müzik aboneliği (03 belgesi 3.3; örnek: Epidemic Sound, Artlist) | Fon müziği; kanalın talep temizleme yöntemi plana göre değişir |
| Masa çekimi karanlık ya da titrek | Telefon için üstten çekim kolu ve tek ışık | Desen kırıcı sahneler ve kısa videoların ilk karesi |
| Sabit set dışında grafik ihtiyacı üç videoda tekrarlandı | Hareketli grafik şablon paketi ya da tasarım aracının ücretli planı (lisans **[DOĞRULA]**) | Açıklayıcı animasyon (5.4) |

## 10. Yüzsüz üretime özel kalite kontrol ve sık yapılan hatalar

### 10.1 Ek kontrol maddeleri

`sablonlar/kalite-kontrol-listeleri.md` içindeki kapıların yerine geçmez; ilgili kapıya **eklenir**. Orada yazılı maddeler tekrar edilmedi. Seslendirme maddeleri Yol B içindir ve mevcut kapıdaki "kayıt ortamı" ile "hook 3 kez kaydedildi" maddelerinin karşılığıdır.

- [ ] **Senaryo kilidi:** EKRAN alanındaki her satırda katman işareti var (`[K1]`–`[K4]`); K1 payı en az %70, K4 payı en çok %5; stok ya da üretilmiş görsel isteyen satırda nesne + eylem tarifi yazılı
- [ ] **Çekim öncesi:** Çekim hesabı açık: hesap menüsü, dosya penceresi, adres çubuğu önerileri ve pano kişisel veri göstermiyor (3.1); kayıt alanı sistem çubuğunu dışarıda bırakıyor; sistem sesi kapalı
- [ ] **Çekim öncesi:** Süre dışı kayıtlarda `kronometre.html` karede ve durmuş
- [ ] **Seslendirme:** Okunuş metni kilitli senaryodan türetildi; yer tutucu yok; "önce → sonra" listesindeki sayılar `olcum.md` ile karşılaştırıldı
- [ ] **Seslendirme:** Ses adı, ses motoru ve ayarlar `ses-kimligi.md` ile aynı; `tts-kaydi.md` dolduruldu; yeni kelimeler sözlüğe eklendi
- [ ] **Seslendirme:** Hook üç kez üretildi; parça sınırları art arda dinlendi; sessizlikler standart sürede, `[D3]` süreleri dizimde bırakıldı
- [ ] **Kurgu:** Süreli kayıtta kare dondurma, yavaşlatma, döngü ve etiketsiz kesim yok; kronometre hiçbir grafikle örtülmüyor (3.5)
- [ ] **Kurgu:** Kapatma kutuları opak ve en üstteki görüntünün üstünde; kare kare kontrol edildi (3.6)
- [ ] **Kurgu:** Şablondan gelen hiçbir grafikte yer tutucu metin kalmadı ("BÖLÜM ADI", "0/0"); önce/sonra ekranında iki taraf aynı büyütme ve kırpmada
- [ ] **Kurgu:** Bağlam sahneleri ve üretilmiş görseller `lisans-kaydi.md` içinde; üretilmiş görselde "temsilî görsel" etiketi var
- [ ] **Kurgu:** Altyazı metni görünen metinden; okunuş yazımı sızmadı
- [ ] **Yayın öncesi:** Yol B: beyan "Evet"; açıklamada sentetik ses satırı var (7.2); kısa videolar için diğer platformların etiketi not edildi (6.8)
- [ ] **Yayın öncesi:** Sentetik ses planı, yazı tipi ve stok lisansları kayıtlı (7.6)
- [ ] **Yayın öncesi:** Gizli yüklemede oynatıcıdan ses seviyesi kontrol edildi; ilk kare siyah değil

### 10.2 Sık yapılan 10 hata

1. **Ekranı stokla doldurmak.** Seslendirme sürerken "boş kalmasın" diye stok plan dizmek kanıtı görüntüden çıkarır ve özgün olmayan içerik desenine yaklaştırır. Boşluk varsa senaryo uzundur (4.1, 7.5).
2. **Kanıt kaydını sese uydurmak için yeniden çekmek.** İkinci koşu daha hızlı çıkar; ölçüm bozulur (3.3; 03 belgesi Aşama 4).
3. **Çekim hesabı yerine kişisel hesapla kaydetmek.** Sonradan kutuyla kapatılacak alan büyür, kanıt değeri düşer; önlem çekimdedir (3.1).
4. **Bulanıklığa güvenmek** ya da kutuyu yakınlaştırılmış kopyada unutmak (3.6).
5. **Süreli koşuyu etiketsiz kesmek ya da kare dondurmak.** Kronometre yanlış süre gösterir; kanalın tek iddiası zedelenir (3.5).
6. **Kapakta stok insan yüzü ya da üretilmiş yüz kullanmak.** Yüzün yerini gerçek ekran parçası tutar (7.2).
7. **Sentetik sesi saklamak.** Beyanı "Hayır" işaretlemek ya da açıklamaya yazmamak; fark edildiğinde kaybedilen şey güvendir (1.2, 7.4).
8. **Görünen metni olduğu gibi ses motoruna vermek** ya da okunuş yazımını altyazıya sızdırmak; okunuş metni ve sözlük bu işi bir kez yapar (2.3, 2.4, 6.4).
9. **Sesi, hızı ya da ses motorunu video ortasında ya da videodan videoya değiştirmek;** hızı kurguda esneterek ayarlamak; ses adını ve lisans planını kaydetmemek. Yüzsüz kanalda ses kimliktir (1.2, 2.5, 2.6).
10. **Yüzün yokluğunu efektle ya da her videoda yeni grafikle kapatmaya çalışmak.** Hızlı kesim, ses efekti, yanıp sönen kutu kanalın sakin tonuyla çelişir; güven açığını kapatan gerçek ekran, gerçek ölçüm ve tutarlı sestir (1.2, 5.2).

## Doğrulanacaklar ve diğer belgelere işlenecekler

| # | Konu | Nerede kontrol edilir | Bu belgede |
|---|---|---|---|
| 1 | Hazır sentetik sesle anlatım beyan gerektiriyor mu; kendi ses klonu; beyanın erişime ve para kazanmaya etkisi | YouTube Yardım [14328491](https://support.google.com/youtube/answer/14328491) ve [15447836](https://support.google.com/youtube/answer/15447836) | 2.7, 7.4 |
| 2 | Özgün olmayan içerik tanımı ve örnekleri; ret hâlinde itiraz yöntemi | [YouTube Yardım 1311392](https://support.google.com/youtube/answer/1311392) | 2.5, 7.5 |
| 3 | Önerilen yükleme kodlama ayarları (bit hızı, ses) | [YouTube Yardım 1722171](https://support.google.com/youtube/answer/1722171) | 6.7 |
| 4 | Oynatmada ses yüksekliği normalleştirmesi; "Sabit ses düzeyi" ayarının adı ve varlığı | Resmî sayfa bulunamadı; gizli yüklemede oynatıcı istatistikleri ve oynatıcı ayarları | 6.6 |
| 5 | Seçilen seslendirme aracında Türkçe desteği, ses motoru adları, ücretsiz planın ticari kullanım koşulu, indirme biçimleri, bağlam/tohum özelliği, abonelik bitince haklar; yerel motor seçilirse Piper ses paketinin ve XTTS-v2 modelinin lisansı | Aracın dil listesi, modeller, fiyat ve kullanım koşulları sayfaları | 2.1, 2.5, 9 |
| 6 | Bulut servislerinin güncel `tr-TR` ses listesi, seçilen seste SSML desteği, ücretsiz kota ve ödeme yöntemi şartı, tarayıcıdan deneme alanı | Bölüm 2.1'deki üç bağlantı; servislerin fiyat sayfaları | 2.1, 2.2, 2.5, 9.1 |
| 7 | Ses klonlamada örnek kaydın saklanması ve kullanımı; aracın rıza doğrulaması | Aracın gizlilik ve kullanım koşulları | 2.7 |
| 8 | Pexels, Pixabay, Mixkit lisans metinleri | Bölüm 4.5'teki bağlantılar | 4.5 |
| 9 | Senaryodan altyazı senkronizasyonu Türkçede çalışıyor mu | 03 belgesi 0.1'deki gizli test videosu | 6.4 |
| 10 | OBS Studio kayıt biçimi seçenekleri ve varsayılanı; Resolve'da menü adları, izleme özelliği ve projeler arası öğe kutusu | [obsproject.com/kb/hybrid-mp4](https://obsproject.com/kb/hybrid-mp4); kullandığın sürümün arayüzü | 3.2, 3.6, 5.2, 6.1 |
| 11 | Studio yükleme akışındaki adımların sırası ve adları; Kontroller adımının kapsamı; Shorts'ta güvenli alan | Studio, yükleme ekranı; telefonda gizli deneme | 6.8, 7.6, 7.7 |

Durum, 2026-11-16 tutarlılık kontrolünden sonra. İşlenenler: `senaryolar/01-…` 2.1'deki "kronometre bir kurgu grafiğidir" ifadesi 03 belgesi Aşama 4'e göre düzeltildi; 03 belgesi 4.3'e bu belgenin 0. ve 8. bölümlerine atıf, 2.1'e süre eklerine atıf eklendi; `README.md` dizini ve "tek kaynak" tablosu güncellendi. Açık kalanlar, ilgili belgede karara bağlanmalıdır:

- **03 belgesi 2.1:** Yüzsüz üretim ekleriyle süre farkının bütçeye işlenmesi (ilk videoda ölçüldükten sonra) (bu belgede 8).
- **03 belgesi 6.1, 6.2:** Yeni klasör ve dosyalar (`00_VARLIKLAR/ses/`, `00_VARLIKLAR/stok/`, `grafik/aciklayici/`, `tts-metni.md`, `tts-kaydi.md`); `tts` türü (bu belgede 2.5, 4.4, 5.4). 03 belgesi 6.3, 6.4 ve kurgu kapısı: ×N'in hesaplanışı; `KAPAT` ve `KR` kanalları; 1440p dışa aktarma (denenirse) (bu belgede 3.5, 6.1, 6.7).
- **`sablonlar/prompt-kutuphanesi.md`:** Okunuş metni prompt'u (bu belgede 2.3).
- **`sablonlar/kalite-kontrol-listeleri.md`:** 10.1'deki ek maddeler ilgili kapılara eklenmedi; Yol B açılırsa ya da ilk çekimden önce eklenir.
