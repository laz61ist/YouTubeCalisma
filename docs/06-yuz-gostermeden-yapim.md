# 06 — Kameraya Çıkmadan Video Üretimi

**Kanal:** Kısa Mesai · **Yazım tarihi:** 2026-11-16 · **Kapsam:** yüz göstermeden üretimin adım adım uygulaması

Bu belge `03-yapim-is-akisi.md` belgesinin yerine geçmez; onun yüz göstermeyen üretime özel uygulama kılavuzudur. Yapım hattının aşamaları, süre bütçesi, klasör düzeni, adlandırma, varlık kütüphanesi ve kurgu ön ayarları 03 belgesindedir; burada yalnızca oraya eklenenler yazılıdır. Çelişki görürsen 03 belgesi ve `README.md` içindeki "tek kaynak" tablosu geçerlidir.

### İşaretler ve doğrulama durumu

| Etiket | Anlamı |
|---|---|
| **[Resmî — sayfada teyit et]** | Belirli bir resmî sayfaya dayanan iddia; bağlantı verildi ama sayfa bu oturumda açılamadı (aşağıdaki not). Uygulamadan önce bağlantıyı aç. |
| **[Yaygın gözlem]** | Platformun ya da araç üreticisinin taahhüt etmediği, üreticiler arasında genel kabul gören pratik. Kendi verinle sına. |
| **[Tahmini]** | Bu belgede yapılmış tahmin; varsayımı yanında yazılıdır. İlk 3–4 videoda ölçüp düzelt. |
| **[DOĞRULA]** | Karardan ya da yayından önce senin kontrol etmen gereken nokta. |

> **Doğrulama notu:** Bu belge yazılırken support.google.com, elevenlabs.io, learn.microsoft.com ve docs.cloud.google.com çalışma ortamından açılamadı. Politika ve araç iddiaları web aramasının sonuç özetlerine ve ikincil kaynaklara dayanır; hiçbiri bu yüzden düz **[Resmî]** etiketi taşımıyor. Toplu liste: belgenin sonundaki "Doğrulanacaklar".

---

## 0. Önce karar: bu belge hangi durumda, nasıl kullanılır

Kısa Mesai zaten yüz göstermeyen bir kanal olarak tasarlandı (01 belgesi Bölüm 3: "Yüz zorunlu değil; kullanılmıyorsa görsel kanıt onun yerini tutar"). Ses konusunda iki yol var:

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
2. KM-010'dan sonra: seslendirme aşaması üç video üst üste 03 belgesindeki 55 dakikayı belirgin aşıyor (ölçüt: 80 dakika **[Tahmini]**) **ve** 2.2'deki deneme testinde en az bir ses eşiği geçiyor.
3. KM-010'dan sonra: kör dinleme testinde (2.2, adım 5) iki dinleyiciden ikisi de sentetik sesi "rahat dinlenir" buluyor ve kendi kaydına tercih ediyor.

**Pilot ve geri dönüş (B → A).** Geçişi tek videoda değil, art arda **üç** uzun videoda dene; sesi video içinde karıştırma. Üç videonun 0:30 tutması ve ortalama izlenme yüzdesi kanal medyanının altındaysa (okuma kuralı: 02 belgesi Bölüm A) ya da yorumlarda ses şikâyeti üç videoda toplam 5'i geçiyorsa **[Tahmini eşik]** Yol A'ya dön. Üç video küçük bir örnektir; sonucu "kanıt" değil "işaret" olarak oku.

---

## 1. Yüzsüz format: dört görsel katman

### 1.1 Katmanlar ve oranlar

Oranlar, katmanın **ana görüntü** olduğu sürenin video süresine payıdır; bindirmeler (alt bant, vurgu kutusu, kronometre çerçevesi) ekran kaydının üstünde durduğu için ayrıca sayılmaz. Hepsi **[Tahmini]** başlangıç değeridir; varsayım: 10–12 dakikalık, Kronometre Yarışı ya da liste yapısında bir video.

| Katman | Pay | 12 dk'lık videoda | Ne zaman | Neden |
|---|---|---|---|---|
| **1. Ekran kaydı (ana katman)** | %70–80 | tahmini 8,5–9,5 dk | Görevin yapıldığı, prompt'un yazıldığı, çıktının kontrol edildiği her an | Kanalın kanıtı budur; yüzün yerini "gerçekten yapılıyor" görüntüsü tutar |
| **2. Metin ve veri grafikleri (tam ekran)** | %8–12 | tahmini 1–1,5 dk | Karşılaştırma tablosu, "yapamadığı şey" kartı, prompt kartı, formül kartı, bitişteki büyük sayı | İzleyicinin ekran görüntüsü alacağı kareler; sayıyı tek bakışta verir |
| **3. Animasyon / hareketli grafik** | %3–8 | tahmini 20–60 sn | Ekranda gösterilemeyen bir fikri anlatırken (ör. "aynı sohbete kötü deneme yazınca sonraki cevap neden değişir") | Ekran kaydının anlatamadığı tek şey soyut ilişkidir; yalnızca o zaman |
| **4. Bağlam sahnesi (stok ya da kendi çekimin)** | %0–5 | en çok tahmini 35 sn, tek plan en çok 5 sn | Hook'ta işin gerçek hayattaki yerini göstermek, desen kırıcı (senaryo 01, 5:40'taki masa çekimi) | Uzun ekran kaydından sonra görüntü türünü değiştirir. Süs olarak kullanılmaz (Bölüm 4) |

Kurallar:

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

---

## 2. Yapay zekâ seslendirme (Yol B)

### 2.1 Araç kategorileri ve Türkçe desteği

| İş tanımı | Kategori → örnek | Türkçe için bilinen | Durum |
|---|---|---|---|
| Doğal tonlamalı anlatım üretmek, tek cümleyi yeniden üretmek | Üretken ses platformu → ElevenLabs | Kendi duyuru yazısına göre Multilingual v2 ses motoru Türkçeyi destekliyor; yardım sayfasının arama özetine göre daha yeni motorlar daha geniş dil listesi taşıyor | **[Resmî — sayfada teyit et]** [dil listesi](https://elevenlabs.io/docs/help-center/other/what-languages-do-you-support). Hangi motorun Türkçede daha iyi olduğu, ücretsiz kullanım ve ticari kullanım koşulu doğrulanamadı **[DOĞRULA]** |
| Duraklama ve okunuşu işaretleme diliyle (SSML) denetlemek | Bulut metin okuma servisi → Microsoft Azure AI Speech, Google Cloud Text-to-Speech, Amazon Polly | Üçünde de `tr-TR` sesleri olduğu uzun süredir bilinen bilgidir; Azure için arama özetlerinde iki Türkçe ses adı (AhmetNeural, EmelNeural) görüldü | **[Resmî — sayfada teyit et]** [Azure](https://learn.microsoft.com/azure/ai-services/speech-service/language-support?tabs=tts) · [Google](https://docs.cloud.google.com/text-to-speech/docs/list-voices-and-types) · [Polly](https://docs.aws.amazon.com/polly/latest/dg/ph-table-turkish.html). Güncel ses listesi ve en yeni ses ailelerinde Türkçe olup olmadığı **[DOĞRULA]** |
| Kurgudan çıkmadan hızlı taslak ses almak | Kurgu ya da tasarım aracına gömülü metin okuma (kategori) | Doğrulanmadı | Ad verilmedi; 03 belgesi 3.2'deki 15 dakikalık kabul testinden geçir |
| Metni dışarı göndermeden, çevrimdışı üretmek | Açık kaynak yerel ses motoru (kategori) | Türkçe ses paketi bulunan projeler olduğu biliniyor; kalite ve lisans doğrulanmadı | **[DOĞRULA]** Ses paketinin lisansı ticari kullanıma izin veriyor mu |

Seçim sırası: önce 2.2'deki test, sonra lisans, en son fiyat. Lisansta bakılacak üç cümle **[DOĞRULA]**: (1) seçtiğin planda üretilen ses para kazanan bir kanalda kullanılabiliyor mu; (2) atıf zorunlu mu; (3) aboneliği bıraktığında daha önce ürettiğin dosyaları yayında tutabiliyor musun.

### 2.2 On dakikalık Türkçe deneme testi

Aynı paragrafı üç araçta okut. Paragraf bu kanalın gerçek zorluklarını içerir; değiştirmeden kullan:

> Bu teklifi elle yazmak 47 dakika sürdü. ChatGPT'ye aynı işi verdim; 14 dakikada bitti. Peki sonuç aynı mı? Hayır. Excel'deki KDV sütununu yanlış topladı, %20'lik satırı iki kez saydı. Hâlâ kullanırım, ama kontrol etmeden göndermem. Sırayla üç şey yaptım: malzemeyi verdim, çıktıyı tarif ettim, önce soru sordurdum. Prompt açıklamada.

(Sayılar test içindir; hiçbir videonun ölçümü değildir.)

| Dk | İş |
|---|---|
| 0–1 | Paragrafı düz hâliyle üç araca yapıştır; her birinde Türkçe, sakin, orta hızda bir ses seç |
| 1–4 | Üçünü üret, `test_arac1.wav` … olarak indir. Hiçbir ayara dokunma |
| 4–7 | Kulaklıkla bir kez, telefon hoparlöründen bir kez dinle; aşağıdaki tabloyu doldur |
| 7–9 | En iyi iki araçta yalnızca hatalı kelimeleri okunuş yazımıyla düzelt (2.3), yeniden üret: düzeltme tutuyor mu? |
| 9–10 | Puanı ve tarihi `tts-kaydi.md` içine yaz |

Her ölçüt 0 (kabul edilemez) · 1 (düzeltmeyle olur) · 2 (sorunsuz):

| Ölçüt | Paragrafta neye bak |
|---|---|
| Sayı + ek | "47 dakika", "14 dakikada", "%20'lik": doğru okuyor mu, eki sayıya bağlıyor mu |
| İngilizce ad + Türkçe ek | "ChatGPT'ye", "Excel'deki": ad anlaşılır mı, ek doğal bağlanıyor mu |
| Kısaltma | "KDV": harf harf Türkçe mi okuyor ("ka de ve") |
| Soru tonu | "Peki sonuç aynı mı?": ton soru gibi mi |
| Tek kelimelik cümle | "Hayır.": yutuluyor ya da abartılıyor mu |
| Düzeltme işareti ve Türkçe harfler | "Hâlâ", "ı/İ", "ğ": "hala" gibi okumuyor mu |
| Sıralama | "malzemeyi verdim, çıktıyı tarif ettim, önce soru sordurdum": üç öğe ayrışıyor mu |
| Ton | Kanalın tonu: sakin, abartısız. Reklam sesi ya da haber spikeri gibi mi |
| Yorgunluk | İkinci dinlemede rahatsız eden metalik tını, nefes taklidi, cümle sonu yükselmesi var mı |
| Düzeltilebilirlik | 7–9. dakikadaki düzeltme tuttu mu |

**Eşik [Tahmini]:** 20 üzerinden en az 15 ve hiçbir ölçütte 0 yok. Eşiği geçen yoksa Yol B'yi bugün açma; testi üç ay sonra tekrarla.

**Adım 5 (isteğe bağlı, geçiş kararı için):** Aynı paragrafı kendi sesinle de kaydet. Hedef kitleden iki kişiye hangisinin hangisi olduğunu söylemeden dinlet; tek soru: "Hangisini 10 dakika dinlersin?"

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
| Kısaltma | KDV, İK, vb., örn. | ka de ve, insan kaynakları, ve benzeri, örneğin | Kısaltmayı aç; harf harf okunacaksa hecele |
| İngilizce araç adı | ChatGPT, Excel, Claude | sözlükteki okunuş (2.4) | Okunuşu bir kez seç, her videoda aynı |
| Ad + ek | ChatGPT'ye, Excel'de | okunuş + ek, kesme işaretsiz | Ek, **okunuşun** son sesine göre uyar: "Excel'de" → "eksel de" değil "ekselde" |
| Dosya adı, bağlantı, kod | `olcum.md`, kısa bağlantı | Okutma; "açıklamadaki bağlantı" de | Ekranda gösterilir |
| Parantez, tırnak, madde işareti | (isteğe bağlı), "…" | Cümleyi parantezsiz yeniden kur; alıntıyı "şunu yazdım:" diye tanıt | Tırnak tonu değiştirmez |

Noktalama, vurgu ve duraklama:

- **Bir cümle, bir fikir; en çok 15–18 kelime [Tahmini].** Uzun cümlede ses motoru nefes yerini kendisi seçer ve çoğu zaman yanlış seçer **[Yaygın gözlem]**.
- **Virgül kısa, nokta uzun duraklamadır.** Duraklama istediğin yerde cümleyi böl. Üç nokta, uzun tire ve noktalı virgülün etkisi araçtan araca değişir; kullanmadan önce dene.
- **Vurguyu söz dizimiyle ver.** Türkçede vurgu yüklemin hemen önündeki öğeye düşer. "Yapay zekâ bu işi **14 dakikada** bitirdi" süreyi, "Bu işi 14 dakikada **yapay zekâ** bitirdi" yapanı vurgular. Büyük harf ya da yıldızla vurgu işaretleme; çoğu araç bunu okumaz ya da yanlış okur **[Yaygın gözlem]**.
- **Sayıyı cümlenin sonuna yakın koy ve sayıdan sonra cümleyi bitir.** Sayıdan sonra gelen uzun kuyruk sayıyı gömer.
- **Duraklama işareti:** okunuş metninde kendi işaretini kullan: `[D1]` kısa (tahmini 0,3 sn), `[D2]` bölüm arası (tahmini 0,7 sn), `[D3]` kart ya da sessiz ekran için (süreyi yanına yaz: `[D3: 4 sn]`). Araç SSML destekliyorsa `[D1]`/`[D2]` üretimden önce `<break time="300ms"/>` gibi etiketlere çevrilir; desteklemiyorsa sessizlik kurguda eklenir. `[D3]` her durumda kurguda eklenir: ses dosyası orada bölünür.
- **Yer tutucular** (`[YZ SÜRE]`, `[ÇEKİMDE …]`) dolmadan okunuş metni üretilmez. 03 belgesindeki sıra geçerlidir: çekim → yer tutucular → seslendirme.

### 2.4 Telaffuz sözlüğü

Dosya: `00_VARLIKLAR/ses/telaffuz-sozlugu.md`. Her yeni kelime ilk karşılaşıldığında eklenir; okunuş metni üretilirken bul-değiştir ile uygulanır.

```
| Görünen | Okunuş yazımı | Ekli örnek | Araç / ses | Denendi | Not |
|---------|---------------|------------|------------|---------|-----|
| ChatGPT | [DENE: "çet ci pi ti" / "çetcipiti"] | [ ]'ye | [ ] | [tarih] | bitişik mi ayrı mı daha doğal |
| Excel   | [DENE: "eksel"]                     | [ ]de  | [ ] | [tarih] |  |
| Claude  | [DENE: "klod"]                      | [ ]a   | [ ] | [tarih] |  |
| prompt  | [DENE: olduğu gibi]                 | [ ]u   | [ ] | [tarih] | çoğul: prompt'lar |
| PDF     | [DENE: "pe de fe"]                  | [ ]i   | [ ] | [tarih] |  |
| hâlâ    | [DENE: olduğu gibi / "haalaa"]      | —      | [ ] | [tarih] | "hala" okuyorsa |
```

Kurallar: okunuşu **kendi seçtiğin araç ve seste** deneyip yaz, tabloyu tahminle doldurma; ses ya da ses motoru değişirse sözlüğün tamamını yeniden dinle (tahmini 10 dk); araçta yerleşik bir telaffuz sözlüğü özelliği varsa onu kullan ama bu dosyayı yine tut, çünkü araç değişir, dosya kalır **[DOĞRULA: özelliğin Türkçede çalışıp çalışmadığı]**.

### 2.5 Parça parça üretim, adlandırma, kayıt

1. Okunuş metnini bölüm bölüm, bölüm içinde paragraf paragraf üret. Tek seferde bütün metni üretme: uzun metinde ton ve hız kayabilir, tek hata bütün dosyayı yeniden ürettirir **[Yaygın gözlem]**.
2. Her parçayı indirir indirmez dinle. Hatalı cümleyi en fazla **üç kez** yeniden üret; üçüncüde de olmuyorsa cümleyi yeniden yaz (önce görünen metinde, sonra okunuş metninde).
3. Hook'u 03 belgesi Aşama 5'teki gibi üç kez üret, en sakin olanı seç.
4. Adlandırma 03 belgesi 6.2 kalıbına uyar; tür `tts`, paragraf `pNN`, sürüm `vN`: `KM-001_b04p02_tts_v2.wav`. Ham parçalar `04_ses/ham/`, birleştirilmiş bölümler `04_ses/temiz/KM-001_b04_tts_TEMIZ.wav`.
5. Biçim: araç izin veriyorsa sıkıştırılmamış WAV, 48 kHz; yalnızca MP3 veriyorsa en yüksek kaliteyi al ve bir daha MP3'e çevirme.
6. `04_ses/tts-kaydi.md` dosyasına yaz: tarih · araç · ses adı · ses motoru adı ve sürümü · hız ve diğer ayarlar · yeniden üretilen cümle sayısı · toplam süre. Kanal düzeyindeki sabitler (ses adı, ayarlar, lisans planı) `00_VARLIKLAR/ses/ses-kimligi.md` içinde durur. Bu kayıt hem tutarlılık hem de para kazanma incelemesinde "nasıl ürettim" sorusunun cevabıdır.

### 2.6 Ses sonrası işlem

Sentetik ses temiz gelir; 03 belgesi 6.4'teki zincirden gürültü azaltma çıkar, gerisi kalır.

| İş | Nasıl | Hedef |
|---|---|---|
| Sessizlik standardı | Parçaların başındaki ve sonundaki boşluğu kırp; cümle arası ve paragraf arası boşluğu elle eşitle | Cümle arası tahmini 0,25–0,4 sn, bölüm arası 0,6–0,8 sn **[Tahmini başlangıç]**; hepsi aynı |
| Seviye | Parçaları tek dosyada birleştir, bölümler arası seviye farkını eşitle, sonra sıkıştırma + sınırlayıcı | 03 belgesi 6.4'teki ses yüksekliği hedefi |
| Tempo | Hız değişikliğini araçta, **üretimden önce** yap. Kurguda zaman esnetme yalnızca küçük düzeltme için | Esnetme tahmini ±%5'i geçmesin; ötesinde ses bozulur **[Yaygın gözlem]** |
| Kesim yerleri | Dalga biçiminde sıfır geçişinde kes, 5–10 ms geçiş ekle | Tıkırtı yok |
| Son dinleme | Baştan sona kulaklıkla, 1× hızda; elinde görünen metin | Okunan her sayı `olcum.md` ile aynı |

Araç: 03 belgesi 3.3'teki ses düzenleyici (Audacity) ya da kurgu aracının ses sayfası.

### 2.7 Kendi sesini klonlama

Ara yol: ses senindir ama kayıt yapmazsın. Karar vermeden önce:

- **Rıza ve etik.** Yalnızca **kendi** sesini klonla. Başkasının sesi (eş, arkadaş, seslendirme sanatçısı) için yazılı, kapsamı belli, geri alınabilir izin gerekir; `sablonlar/izin-onay.md` buna göre genişletilir. Tanınmış birinin sesine benzeyen hazır ses kullanma. Ses örneğini yüklediğin aracın, kaydını nasıl sakladığını ve başka amaçla kullanıp kullanmadığını oku **[DOĞRULA]**. Ses kişisel veridir; hukuki tavsiye değildir, başkasının sesini işleyeceksen bir hukukçuya danış.
- **Beyan.** YouTube'un yardım sayfasının arama özetinde **başkasının** sesini klonlamak beyan gerektiren örnekler arasında; kendi ses klonun için kaynaklar çelişiyor (03 belgesi 4.4 A). Kanal kuralı değişmez: klon dâhil her sentetik ses için "Evet" + açıklama cümlesi.
- **Kalite.** Klonun kalitesi verdiğin kaydın kalitesidir: yankısız oda, tek mesafe, kanalın tonunda okunmuş metin. Kötü odada kaydedilmiş örnek, kötü odayı da klonlar **[Yaygın gözlem]**. Türkçe klon kalitesi araçtan araca değişir; 2.2'deki testi klonla da yap **[DOĞRULA]**.
- **Dürüstlük.** Klon sesle "bunu ben söyledim" izlenimi doğar. Videoda söylenen her cümle senin onayladığın kilitli senaryodan gelir; klona senaryo dışı cümle söyletilmez.
- **Sıra.** 03 belgesi 4.3 klonu ilk 10 videoda kullanmaz. Sonrasında açılacaksa 0. bölümdeki pilot kuralı geçerlidir.

### 2.8 Yaygın hatalar

1. Görünen metni olduğu gibi ses motoruna vermek (sayı, kısaltma, kesme işareti hataları).
2. Okunuş yazımının altyazıya sızması ("çet ci pi ti" altyazıda görünür). Altyazı her zaman görünen metinden üretilir.
3. Video ortasında ses, hız ya da ses motoru değiştirmek.
4. Yer tutucular dolmadan üretmek; sonra sayıyı tek kelime olarak yeniden üretip yapıştırmak (ton tutmaz; cümlenin tamamını yeniden üret).
5. Hızı kurguda esneterek ayarlamak.
6. Sessiz ekran sürelerini (`[D3]`) unutup sesi kesintisiz dizmek; izleyici prompt'u okuyamaz.
7. Lisans planını ve ses adını kaydetmemek; altı ay sonra aynı sesi bulamamak.
8. Hazır seslerin "heyecanlı tanıtım" tonunu seçmek; kanalın tonu sakin ve abartısızdır.

---

## 3. Ekran kaydı

Çekim profili, çözünürlük, kronometrenin kayda gömülmesi, süreli koşu ve ölçümün dürüstlük kuralı 03 belgesi Aşama 4'tedir. Buradakiler ona ektir.

### 3.1 Kayıt öncesi masaüstü hazırlığı (ek maddeler)

| Konu | İş | Kontrol |
|---|---|---|
| Örnek hesap | Videoda görünen her araç için kanala ait ayrı hesap aç (ör. `kisamesai.cekim@…`); profil adı "Kısa Mesai", profil resmi kanal logosu | Hesap menüsü açıldığında kişisel ad yok |
| Sohbet geçmişi | Çekim hesabında geçmişi boş tut ya da kenar çubuğunu kapat | Kenar çubuğunda eski sohbet başlığı yok |
| Otomatik tamamlama | Çekim profilinde adres çubuğu önerilerini, kayıtlı form verilerini ve parola önerilerini kapat | Adres çubuğuna bir harf yaz: kişisel adres çıkmıyor |
| Dosya pencereleri | Çekim için ayrı klasör; "Son kullanılanlar" görünmeyecek şekilde dosya penceresini o klasörde aç | Dosya seçme penceresinde kişisel klasör adı yok |
| Ofis yazılımı | Excel/Word başlık çubuğundaki hesap adı ve "son dosyalar" listesi | Kurgusal şirket adına açılmış profil ya da adı kırpan kayıt alanı |
| Sistem çubuğu | Saat, takvim, Wi-Fi adı, pil; işletim sisteminin "rahatsız etmeyin" kipi | Kayıt alanı sistem çubuğunu dışarıda bırakıyor ya da çubuk gizli |
| Pano | Çekimden önce panoya zararsız bir metin kopyala | Yanlışlıkla yapıştırınca kişisel veri çıkmıyor |
| Kurgusal veri | Kişi adları, telefon, e-posta, vergi numarası biçimindeki alanlar açıkça kurgusal (03 belgesi 4.5) | Gerçek bir kişi ya da şirketle karışmıyor |

### 3.2 Kayıt ayarları (ek)

- **Kayıt alanı:** tam ekran yerine 16:9 sabit bir bölge ya da tek pencere; sistem çubuğu ve bildirim alanı dışarıda kalır.
- **Kare hızı sabit olsun.** Telefonla çekilen masa görüntüsü değişken kare hızlı olabilir; kurguda ses kayması görürsen dosyayı kurgudan önce sabit 30 kare/sn'ye dönüştür **[Yaygın gözlem]**.
- **Sistem sesini kaydetme** (bildirim sesi riski); Yol B'de mikrofon kanalını da kapat.
- **Kayıt biçimi:** çökme hâlinde dosyanın kurtarılabildiği bir kap biçimi seç (OBS Studio'da varsayılanı ve "kayıttan sonra mp4'e dönüştür" seçeneğini kontrol et **[DOĞRULA]**).
- **Her kayıt bir iş:** süreli koşu tek dosya; her ek gösterim ayrı dosya. Uzun tek kayıt, kurguda aranan anı bulmayı zorlaştırır.

### 3.3 Önce ses mi, önce görüntü mü

İki tür kayıt vardır ve sıraları terstir:

| Kayıt türü | Sıra | Neden |
|---|---|---|
| **Kanıt kaydı** (süreli koşu, elle koşu, "yapamadığı şey" anı) | **Önce görüntü, sonra ses** | Sonuç çekimde ortaya çıkar; senaryodaki sayı ve cümle ona göre yazılır. Sese uydurmak için yeniden çekilmez |
| **Anlatım kaydı** (bir menünün yeri, prompt'un parça parça gösterilmesi, önce/sonra ekranı) | **Önce ses, sonra görüntü** | Ses dosyasının süresi bellidir; görüntüyü ona göre çekmek kurguda esnetme ve dondurma ihtiyacını azaltır |

Anlatım kaydını sese göre çekme yöntemi: bölümün temiz ses dosyasını kulaklıkta çal, aynı anda ekranı kaydet, her cümlede söylenen şeyi ekranda yap. İlk tur prova, ikinci tur kayıt. Hareketler yavaş ve tek tek: imleç hedefe gider, yarım saniye durur, tıklar. Yol B'de bu yöntem daha kolaydır çünkü ses yeniden üretilince süresi değişmez; Yol A'da ses kaydı bitmeden anlatım kayıtlarına başlama.

### 3.4 İmleç ve yakınlaştırma vurguları

Yakınlaştırma ön ayarları ve büyütme sınırları 03 belgesi 6.4'te, "tek karede tek vurgu" kuralı 6.3'tedir. Ek olarak:

- **İmleç anlatıcının parmağıdır.** Çekimde imleci okunacak metnin üstünde gezdirme; hedefin yanında dursun. Boşta kalan imleci ekranın aynı köşesine park et.
- **Yakınlaştırmayı cümleye bağla.** Büyütme, hedefin adı söylenmeden yarım saniye önce başlar, cümle bitince geri çekilir. Tahmini 0,4–0,6 sn yumuşak geçiş **[Tahmini]**; daha hızlısı sarsar, daha yavaşı geciktirir.
- **Art arda iki büyütme arasında tam ekrana dön** ya da doğrudan kes; büyütülmüş hâlde kaydırma (pan) izleyiciyi yorar **[Yaygın gözlem]**.
- **Vurgu sırası:** önce yakınlaştır, yetmiyorsa vurgu kutusu, o da yetmiyorsa çevreyi karart. Üçü aynı anda kullanılmaz.
- **Yazma anları:** uzun bir prompt'un yazılışını hızlandır (etiketle), son satırın yazılışını gerçek hızda bırak.

### 3.5 Bekleme sürelerini kurguda yönetmek

Kural 03 belgesinde yazılı: kronometre gerçek süreyi gösterir, rakam kurguda yazılmaz, hızlandırılan ya da beklemesi kesilen her bölüm "hızlandırıldı ×N" etiketi taşır. Uygulama kararı:

| Bekleme (gerçek süre) | Ne yapılır | Ekranda |
|---|---|---|
| 3 saniyeye kadar | Dokunma | — |
| 3–15 sn | Gerçek hızda bırak, seslendirmeyi üstüne koy ("cevap gelirken şuna bak") | — |
| 15–60 sn | İlk 2 sn gerçek hız → ortası hızlandırılmış → son 2 sn gerçek hız | "hızlandırıldı ×N" etiketi; kronometre hızlı akar |
| 60 sn üstü | Ortasını kes | "bekleme kesildi" notu; kronometre ileri atlar, atlama gizlenmez |

Eşikler **[Tahmini]**; ilk videoların tutma grafiğinde bekleme anlarına bak ve düzelt.

Yasaklar (dürüstlük):

- Süreli kayıtta **kare dondurma yok.** Seslendirme uzun geldiyse görüntüyü dondurma (kronometre de donar ve yanlış süre gösterir); cümleyi kısalt ya da o cümleyi süre dışı bir kaydın üstüne taşı.
- Süreli kayıtta **yavaşlatma ve döngü yok.**
- Kronometrenin üstü hiçbir grafikle örtülmez; yakınlaştırmada kadraj dışında kalıyorsa kronometrenin küçük bir kopyası (aynı kayıttan kırpılmış, V2 kanalında) sağ üstte tutulur. Kopya kayıttan gelir, yazılmaz.
- Hızlandırma katsayısı etikette gerçek değerdir; "×4" yazıp ×8 uygulanmaz.

### 3.6 Hassas bilgiyi kapatma

Önce çekimde önle (3.1); kurguda kapatma ikinci savunmadır.

1. **Bulanıklık yerine dolu kutu.** Küçük metnin üstündeki bulanıklık ve mozaik bazı durumlarda geri okunabilir **[Yaygın gözlem]**; lacivert, opak bir kutu kullan.
2. Kutu, kaydırma ve pencere hareketiyle birlikte hareket etmeli: kutuyu yerleştirdikten sonra bölümü kare kare ileri sar, sızan kare var mı bak.
3. Yakınlaştırılmış kopyada (V2) aynı bilgi yeniden görünür; kutuyu iki kanalda da kontrol et.
4. Kapatılan alan büyükse kayıt alanını kırp ya da bölümü yeniden çek; ekranın dörtte biri kutuyla kaplı bir video kanıt değeri taşımaz.
5. Aynı kontrolü kapak ve kısa videolar için ayrıca yap; onlar başka kareden üretilir.
6. Ham kayıt arşivde kapatılmamış durur; ham dosyayı kimseyle paylaşma.

---

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
2. Filtre: yatay, en az 1080p, insan yüzü yok ya da tanınmıyor, marka ve ekran içeriği görünmüyor.
3. Aynı videodaki planlar aynı ışık ve renk sıcaklığında olsun; lacivert + sarı palete uymayan planı hafif soluklaştır.
4. Türkiye'ye uymayan ayrıntılara bak: priz tipi, para birimi, yabancı dilde belge, ofis mimarisi. Uymuyorsa yakın plan seç ya da kendi masanı çek.
5. Plan başına en çok 5 dakika ara **[Tahmini]**; bulamıyorsan o satırı ekran kaydına ya da karta çevir.

### 4.3 Klişe stoktan kaçınma

Kullanılmayanlar: el sıkışan takım elbiseliler, mavi ışıklı robot eli ve beyin görselleri, havada uçuşan ikili kodlar, toplantı masasında gülen ekip, klavyeye hızlı yazan eller (hızlandırılmış), büyüteçle grafiğe bakan kişi. Sınama sorusu: "Bu planı başka on kanalda gördüm mü?" Evetse çıkar. Yapay zekâyı anlatmak için yapay zekâ görseli kullanılmaz; kanalın yapay zekâ görüntüsü, ekrandaki gerçek sohbet penceresidir.

### 4.4 Lisans türleri ve kayıt tutma

Genel bilgidir, hukuki tavsiye değildir; her dosyanın lisansını indirdiğin gün kendi sayfasından oku.

| Tür | Anlamı | Bu kanalda |
|---|---|---|
| Telifsiz (royalty-free) | Bir kez lisanslanır, kullanım başına ödeme yoktur. "Ücretsiz" demek değildir; koşulları vardır | Asıl kullanılacak tür |
| Ücretsiz stok sitesinin kendi lisansı | Siteye özgü metin; çoğunlukla ticari kullanıma izin verir, kısıtları vardır (yeniden dağıtım, kişilerin onay izlenimi, marka) | Metni oku; "ücretsiz" yazması yetmez |
| Creative Commons | CC0 (serbest), BY (atıf şart), NC (ticari kullanım yok), ND (değiştirme yok), SA (aynı lisansla paylaş) | NC ve ND içerenler para kazanan kanalda kullanılmaz; BY ise atıf açıklamaya yazılır |
| Yalnızca editoryal | Haber/yorum amaçlı; tanıtım ve ticari kullanım yok | Kullanma |
| Hak yönetimli | Süre, bölge ve mecra bazında lisans | Bu kanalın ihtiyacı değil |

Ayrıca: lisans görüntüyü kapsar, içindeki **kişiyi, markayı ve mülkü** her zaman kapsamaz (model/mülk izni ayrı konudur). Yüzü görünen kişi içeren planı kullanma.

Kayıt: `00_VARLIKLAR/stok/lisans-kaydi.md` (müzik için 03 belgesindeki `muzik/lisans-notu.md` ile aynı mantık).

```
| Dosya adı | Kaynak site | Sayfa bağlantısı | Üretici | Lisans adı | İndirme tarihi | Lisans sayfası görüntüsü | Atıf gerekli mi | Kullanıldığı video |
|-----------|-------------|------------------|---------|------------|----------------|--------------------------|-----------------|--------------------|
| stok_fatura-masa_01.mp4 | [ ] | [ ] | [ ] | [ ] | [YYYY-AA-GG] | lisans_[tarih].png | [ ] | KM-0[ ] |
```

Lisans sayfasının ekran görüntüsünü al: koşullar sonradan değişebilir, itiraz gerektiğinde elindeki kanıt indirme günündeki metindir.

### 4.5 Kaynak kategorileri

| Kategori | Örnek | Durum |
|---|---|---|
| **Kendi çekimin** | Telefonla üstten masa, el, kâğıt | Lisans sorunu yok; kanıt değeri var. İlk tercih |
| **Ücretsiz stok siteleri** | Pexels, Pixabay, Mixkit | İkincil kaynaklara göre üçü de ticari kullanıma izin veriyor ve atıf zorunlu tutmuyor; kısıtlar ve bazı içeriklerde farklı lisans olabileceği belirtiliyor. Lisans metinleri okunamadı **[DOĞRULA]**: [Pexels](https://www.pexels.com/license/) · [Pixabay](https://pixabay.com/service/license-summary/) · [Mixkit](https://mixkit.co/license/) |
| **Abonelikli stok kitaplıkları** | (kategori; ad verilmedi) | Lisans kapsamı, abonelik bitince kullanım hakkı ve YouTube'da telif talebi temizleme yöntemi plana göre değişir **[DOĞRULA]** |
| **Tek tek satın alınan stok** | (kategori) | Nadir kullanılan tek plan için |

### 4.6 Yapay zekâ ile üretilmiş görsel ve video

- **Kanıt yerine asla:** arayüz, sonuç, belge, "müşteri" görüntüsü üretilmez (03 belgesi 4.1).
- **Yalnızca açıkça temsilî ve gerçekçi olmayan** görseller: çizim tarzı, düz renkli, palete uygun. Gerçekçi üretilmiş sahne kullanırsan 03 belgesi 4.4 A'daki kanal kuralı devreye girer: Studio'da "Evet" + açıklamada cümle.
- Ekranda küçük etiket: "Temsilî görsel · yapay zekâyla üretildi". Politika istemese de kanal ister.
- Üreten aracın çıktı üzerindeki kullanım koşulunu oku (ticari kullanım, plan farkı) **[DOĞRULA]**; `lisans-kaydi.md` içine araç adı, tarih ve kullandığın istem yazılır.
- Tanınan kişi, marka, logo ya da korunan bir karaktere benzeyen çıktı kullanılmaz.

---

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

Yerleşim kuralları: sağ üst kronometrenindir; sol üst adım sayacı ve hız etiketinin; sol alt alt bandın; **sağ alt boş kalır** (kapaktaki kuralla aynı; YouTube'un süre etiketi ve bitiş ekranı öğeleri için). Alt orta, altyazı alanıdır; grafik koyma. Metin kutularında kenar boşluğu en az harf yüksekliğinin yarısı.

### 5.2 Şablon olarak saklama

1. Her grafiği kurgu aracında **bir kez** kur, 03 belgesi 6.1'deki `00_VARLIKLAR/proje-sablonu/` içindeki uzun video şablonuna koy; ayrıca aracın projeler arası paylaşılan öğe kutusuna kaydet (DaVinci Resolve'da bu işi gören özellik "Power Bin" adıyla geçer **[DOĞRULA: kullandığın sürümde]**).
2. Dışarıda üretilen görseller (formül kartı zemini, etiketler) saydam zeminli PNG olarak `00_VARLIKLAR/grafik/` içinde; kaynak dosyası (sunum ya da tasarım dosyası) yanında.
3. Adlandırma: `GR_altbant_v1`, `GR_formul-4parca_v1`. Tasarım değişirse sürüm artar, eski sürüm silinmez; yayınlanmış videonun projesi eski sürümü arar.
4. Şablonda her grafiğin metni yer tutucudur ("BÖLÜM ADI"); yayına yer tutucuyla çıkmamak için kurgu kapısına madde eklendi (Bölüm 10).
5. Dikey şablonda aynı setin 1080×1920 sürümü ayrı durur; yatay grafiği dikeye sığdırmaya çalışma.

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

Üç sorunun üçüne de "evet" ise yap:

1. Anlatılan şey ekran kaydıyla **gösterilemiyor** mu (soyut ilişki, görünmeyen süreç)?
2. Bu açıklama **en az üç videoda** yeniden kullanılacak mı (ör. "yeni sohbet neden önemli")?
3. Üretimi **tahmini 45 dakikanın** altında mı **[Tahmini]**?

Birine "hayır" ise: tek karelik şema + seslendirme yeterlidir. Karakter animasyonu, 3B, logo animasyonu ve intro bu kanalda yoktur (03 belgesi 6.3: "Intro yok"). Yapılan her açıklayıcı animasyon `00_VARLIKLAR/grafik/aciklayici/` içine girer ve kullanıldığı videolar not edilir.

---

## 6. Kurgu montajı

Kurgunun adım sırası ve süreleri 03 belgesi Aşama 6'da, kanal düzeni ve ön ayarlar 6.4'tedir. Aşağıdakiler yüzsüz üretimin eklediği ayrıntılardır.

### 6.1 Zaman çizelgesi katman düzeni (03 belgesi 6.4'e ek)

| Kanal | 03 belgesindeki rol | Yüzsüz üretimde içine giren |
|---|---|---|
| V1 | Ekran | Ekran kaydı (K1) **ve** onun yerini alan tam ekran kart (K2), animasyon (K3), bağlam sahnesi (K4). Ana görüntü hep V1'dedir; böylece "V1'de boşluk var mı" tek kontroldür |
| V2 | Büyütme / kopya | Yakınlaştırılmış kopya, önce/sonra'nın ikinci yarısı, kronometrenin kırpılmış kopyası, kapatma kutuları |
| V3 | Grafik | Bindirmeler: alt bant, adım sayacı, vurgu kutusu, etiketler |
| V4 | Altyazı | Dikey sürümde gömülü altyazı; yatayda boş |
| A1 | Ses | Seslendirme (Yol B'de bölüm bölüm `_TEMIZ.wav` dosyaları) |
| A2 | Müzik | |
| A3 | Efekt | Efektler ve masa çekiminin ortam sesi |

Klipleri katmana göre renklendir (K1 mavi, K2 sarı, K3 yeşil, K4 gri): zaman çizelgesine uzaktan bakınca 1.1'deki oranı görürsün.

### 6.2 Ses merkezli kurgu sırası (Yol B farkları)

1. Bölüm ses dosyalarını A1'e diz; aralarına `[D2]`, kart yerlerine `[D3]` sürelerini koy. Yol B'de "yanlış denemeleri atma" adımı yoktur; onun yerine **okunuş kontrolü** vardır: A1'i baştan sona dinle, hatalı cümleyi şimdi yeniden üret. Görüntü dizildikten sonra ses değişirse her şey kayar.
2. A1'i kilitle. Bundan sonra ses yalnızca tek cümle değiştirilerek güncellenir ve yeni cümle eskisiyle aynı süredeyse yerine konur; değilse o bölümün görüntüsü yeniden hizalanır.
3. Kanıt kayıtlarını (3.3) sese hizala: önce süreli koşu, çünkü kesilemeyen odur. Ses süreli koşudan kısaysa bekleme kuralları (3.5); uzunsa cümleyi kısalt ya da süre dışı kayda taşı.
4. Anlatım kayıtlarını yerleştir; eksik kalan görüntüyü not et, hepsini tek oturumda sese göre çek (3.3).
5. Sonra 03 belgesindeki sıra: yönlendirme → sabit grafikler → müzik → altyazı → telefonda izleme.

### 6.3 Tempo

Tek kaynak `sablonlar/senaryo-sablonu.md`: ekranda en geç tahmini 20–30 saniyede bir görsel değişiklik. Katmana göre ek başlangıç değerleri, hepsi **[Yaygın gözlem]** ve **[Tahmini]**; kanalın kendi tutma grafiğiyle düzeltilir:

| Durum | Başlangıç değeri |
|---|---|
| Hook (ilk 30 sn) | 4–8 saniyede bir değişiklik (kesme, büyütme ya da grafik) |
| Ekran kaydı, anlatım bölümü | 10–20 saniyede bir büyütme ya da vurgu |
| Süreli koşu | Görüntü kesilmez; değişiklik büyütme ve etiketle gelir |
| Tam ekran kart | Okuma süresi: kelime başına tahmini 0,4 sn + 1 sn; prompt kartı 03 belgesi 6.3'teki gibi |
| Bağlam sahnesi | Plan başına 3–5 sn |
| Sessiz ekran | Tek seferde en çok tahmini 6–8 sn; uzunsa müzik hafifçe yükselir |

Yüzsüz videoda yüzün taşıdığı ritmi ses taşır. Sentetik ses tekdüze kalabildiği için **[Yaygın gözlem]** değişimi görüntü ve sessizlik üstlenir: bölüm sonlarında yarım saniyelik tam sessizlik, "yapamadığı şey" kartından önce müziğin kesilmesi (03 belgesi 6.3).

### 6.4 Altyazı

İki yol 03 belgesi Aşama 6, adım 6'dadır. Yol B'de tercih **senaryodan senkronizasyondur**: görünen metin zaten kelimesi kelimesine doğrudur ve sentetik ses temiz olduğu için hizalama kolaylaşır **[Yaygın gözlem]**; Türkçe için çalışıp çalışmadığı 03 belgesi 0.1'deki gizli test videosunda sınanır **[DOĞRULA]**.

- Altyazı kaynağı her zaman **görünen metindir**, okunuş metni değil (2.8, madde 2).
- Seslendirme aracın altyazı ya da zaman damgası dosyası veriyorsa kullanılabilir **[DOĞRULA: seçtiğin araçta]**; içindeki metni görünen metinle değiştir.
- Sayılar altyazıda rakamla yazılır ("14 dakika"), seste yazıyla okunur; ikisi aynı değerdir.
- Yatay videoda altyazı gömülmez, dosya olarak yüklenir; dikeyde gömülür (03 belgesi 6.4).

### 6.5 Müzik ve efekt

Kaynak ve seviye 03 belgesi 3.1, 6.3 ve 6.4'tedir. Ek:

- Sentetik sesin altında müzik, sesin "boşlukta" durmasını azaltır **[Yaygın gözlem]**; yine de konuşmanın belirgin altında.
- YouTube Ses Kitaplığı'ndaki bazı parçalar atıf ister; parça sayfasındaki lisans türünü `muzik/lisans-notu.md` içine yaz ve atıf gerekiyorsa açıklamaya ekle **[Resmî — sayfada teyit et: Studio → Ses Kitaplığı, lisans sütunu]**.
- Ücretsiz efekt sitelerinden alınan seslerin lisansı da kayda girer; "telifsiz" yazan bir video ya da oynatma listesinden müzik indirilmez.

### 6.6 Renk ve ses seviyesi hedefleri

- **Renk:** ekran kaydına renk düzeltme uygulanmaz (arayüz renkleri gerçeği göstersin). Yalnızca bağlam sahneleri palete yaklaştırılır. Açık temalı arayüz ile lacivert kartlar arasındaki parlaklık sıçraması göz yorar; kartlara 0,2 sn'lik geçiş koy. Çekimde açık ya da koyu temadan birini seç ve bütün videolarda aynı kalsın.
- **Ses yüksekliği:** hedef 03 belgesi 6.4'te yazılıdır ve **[Yaygın gözlem]** düzeyindedir. YouTube'un oynatmada ses yüksekliğini normalleştirdiği, yüksek gelen içeriği kıstığı ama düşük geleni yükseltmediği yaygın olarak aktarılır; bu oturumda resmî bir sayfayla teyit edilemedi **[DOĞRULA]**. Pratik kontrol: videoyu gizli olarak yükle, oynatıcıda sağ tık → "Meraklısı için istatistikler" penceresindeki ses satırına bak; ardından aynı nişten iki videoyla art arda dinle.
- Yol B'de ses dosyaları araçtan farklı seviyelerde gelebilir; ölçümü birleştirilmiş dosyada yap, parçada değil.

### 6.7 Dışa aktarma

Ayarlar 03 belgesi 6.4'tedir; bit hızı için **[Resmî — sayfada teyit et]** [YouTube'un önerilen yükleme kodlama ayarları](https://support.google.com/youtube/answer/1722171). Ek kontroller:

- Ses: AAC, 48 kHz, stereo (sentetik ses tek kanallıysa iki kanala eşit dağıt) **[Resmî — sayfada teyit et, aynı sayfa]**.
- Ekran kaydında ince yazı, düşük bit hızında bozulur. Dışa aktarılan dosyada en küçük yazılı kareyi durdur ve %100'de bak; bozuksa bit hızını yükselt.
- YouTube yükleme sonrası yeniden kodlar; yüksek çözünürlük işlemesi bitmeden videoyu kimseye gösterme ve zamanlamayı buna göre yap (`kalite-kontrol-listeleri.md` Bölüm 7'deki "yeterince önce yüklendi" maddesi).

---

## 7. Yayına hazırlık

Yayınlama adımları 03 belgesi Aşama 8'de, doldurulacak form `sablonlar/yayin-metaverisi.md` dosyasında, kapı `sablonlar/kalite-kontrol-listeleri.md` Bölüm 7'dedir. Yüzsüz üretimin eklediği işler:

### 7.1 Dışa aktarılan dosyanın kontrolü (10 dk + video süresi)

1. Dosya süresi kurgu süresiyle aynı; sonda fazladan siyah kare ya da sessizlik yok.
2. İlk kare siyah değil (kapak yüklenmezse YouTube ilk karelerden seçer; ayrıca Shorts akışında ilk kare görünür).
3. Son 30 saniyede ses–görüntü kayması yok (değişken kare hızlı kaynak belirtisi, 3.2).
4. Kare kare gezinme: her kapatma kutusu yerinde (3.6); kişisel veri sızıntısı yok.
5. Telefonda 1× izleme (03 belgesi Aşama 6, adım 7): bu, yüzsüz videoda en önemli kontroldür çünkü videonun tamamı okunacak yazıdır.

### 7.2 Kapak, başlık, açıklama, bölümler

Kurallar 01 belgesi Bölüm 3 ve `yayin-metaverisi.md` Bölüm 1–4'tedir. Yüzsüz kanal için ek: kapakta yüzün yerini "X → Y" çiftindeki gerçek ekran parçası tutar; stok insan fotoğrafı ve üretilmiş yüz kullanılmaz. Yol B'de açıklamaya şu sabit satır eklenir (yeri: "Nasıl ölçtüm" bloğunun altı):

> Seslendirme sentetiktir ([araç adı]). Ekran kayıtları, ölçümler ve senaryo bana aittir.

### 7.3 Altyazı dosyası

`KM-[NO]_SON_tr.srt` ya da senkronize edilen görünen metin (6.4). Yüklemeden sonra üç noktada (baş, orta, son) zamanlamayı kontrol et; `yayin-metaverisi.md` Bölüm 8'deki satırı işaretle.

### 7.4 "Değiştirilmiş veya sentetik içerik" beyanı

Politikanın özeti ve kanal kuralı 03 belgesi 4.4 A'dadır; kaynak **[Resmî — sayfada teyit et]** [YouTube Yardım: değiştirilmiş veya sentetik içeriğin beyanı](https://support.google.com/youtube/answer/14328491) ve [YouTube Blog duyurusu](https://blog.youtube/news-and-events/disclosing-ai-generated-content). Bu oturumdaki arama özetinde de aynı çerçeve görüldü: beyan, gerçek sanılabilecek gerçekçi içerik içindir; başkasının sesini klonlayarak seslendirme beyan gerektiren örneklerdendir; gerçekçi olmayan içerik ve küçük düzeltmeler kapsam dışıdır. Hazır bir sentetik sesle yapılan anlatımın tek başına beyan gerektirip gerektirmediği resmî örneklerde açıkça görülemedi; ikincil kaynaklar çelişiyor **[DOĞRULA]**.

Bu belgedeki durumlar için karar (kanal kuralı politikadan sıkıdır):

| Videoda ne var | Studio'da beyan |
|---|---|
| Yol A: gerçek ekran + kendi sesin | Hayır |
| Yol B: hazır sentetik ses ya da kendi ses klonun | **Evet** + 7.2'deki açıklama satırı |
| Gerçekçi üretilmiş görsel ya da video (4.6) | **Evet** + açıklamada hangi bölümde |
| Açıkça çizim tarzı temsilî görsel, hareketli grafik, stok görüntü | Hayır (ekrandaki "temsilî görsel" etiketi kanal kuralıdır) |
| Bekleme hızlandırma, kapatma kutusu, yakınlaştırma | Hayır (küçük düzeltme); "hızlandırıldı" etiketi kanal kuralıdır |

Beyan ile para kazanma ayrı konulardır (04 belgesi 2.5). Kısa videoları başka platformlara gönderirken 03 belgesi 4.4 C tablosu geçerlidir.

### 7.5 Para kazanma politikası riski: özgün olmayan ve tekrarlayan içerik

Politikanın özeti 03 belgesi 4.4 B'de, gelir tarafı 04 belgesi 2.5–2.6'dadır; kaynak **[Resmî — sayfada teyit et]** [YouTube kanal para kazanma politikaları](https://support.google.com/youtube/answer/1311392). Arama özetlerine göre kural yapay zekâ kullanımını değil, toplu üretilmiş, şablondan çıkmış gibi görünen ve videolar arasında anlamlı fark taşımayan içeriği hedefler; ikincil kaynaklarda en sık verilen örnek, başkasının metnini metin okuma motoruna verip stok görüntüyle yayınlamaktır. İkincil kaynaklar yüzsüz kanalların bu denetimde daha sık incelendiğini de aktarıyor **[Yaygın gözlem]**.

Yol B bu kanalın risk yüzeyini büyütür: "sentetik ses + hazır görsel + asgari insan katkısı" deseninin üç ayağından birini eklemiş olursun. Diğer ikisini sıfırda tutan şeyler:

| Riskli desen | Bu kanalda karşılığı | Kanıtı nerede |
|---|---|---|
| Başkasının içeriğini okutmak | Senaryo kendi görevinden, kendi ölçümünden yazılır | `olcum.md`, ham kayıt (03 belgesi 6.2: silinmez) |
| Stok görüntü üstüne anlatım | Görüntünün en az %70'i kendi ekran kaydın (1.1) | Zaman çizelgesi, ham kayıt |
| Videolar arasında fark yok | Her videoda farklı görev, farklı veri, gerçekten yaşanmış farklı "yapamadığı şey" | `performans-kaydi.md`, `arac-ciktilari.md` |
| Ölçekte üretim | Haftada 1 uzun video; ritim 02 belgesi B2 | Yükleme geçmişi |
| İnsan katkısı görünmüyor | Elle koşu, kâğıt notlar, masa çekimi, yorumlara yazılı cevap, düzeltme notları | Videonun kendisi |

Uygulama: Yol B'deyken haftalık yükleme sayısını artırma; kısa videoların seslendirmesini uzun videodan kopyalama (01 belgesi 4.4: ayrı seslendirme); `tts-kaydi.md` ve ham kayıtları başvuru incelemesi için sakla. İnceleme sonucunu hiçbir önlem garanti etmez; bu liste riski azaltır, kaldırmaz.

### 7.6 Telif kontrolleri

Genel bilgidir, hukuki tavsiye değildir.

| Öğe | Kontrol | Kayıt |
|---|---|---|
| Sentetik ses | Planın para kazanan kanalda kullanıma izni (2.1) | `ses-kimligi.md` |
| Müzik ve efekt | Lisans türü, atıf | `muzik/lisans-notu.md` |
| Stok görüntü | Lisans, kişi/marka görünürlüğü | `stok/lisans-kaydi.md` |
| Yazı tipi | Lisansı videoda ve kapakta ticari kullanıma izin veriyor mu | `kapak/renk-notu.md` |
| Üretilmiş görsel | Aracın çıktı koşulu | `stok/lisans-kaydi.md` |
| Ekrandaki yazılım arayüzü ve logolar | Eğitim/inceleme amaçlı gösterim yaygındır **[Yaygın gözlem]**; logo kapakta ana öğe olmaz (01 belgesi Bölüm 3), "resmî ortak" izlenimi verilmez | — |
| Ekrandaki üçüncü taraf içerik | Başkasının videosu, makalesi, e-postası kayda girmez; kurgusal veri kullanılır (03 belgesi 4.5) | — |

Yüklemede Studio'nun kontrol adımı telif ve reklam uygunluğu için ön tarama yapar **[Resmî — sayfada teyit et: Studio yükleme akışı, "Kontroller" adımı]**; sonuç çıkmadan görünürlüğü zamanlama. Talep gelirse `lisans-kaydi.md` içindeki ekran görüntüsüyle itiraz edilir.

### 7.7 Zamanlama

Gün ve ritim: 02 belgesi B2 (perşembe; tek kaynak). Yüzsüz üretimin eklediği tek şey sıra: dışa aktarma kontrolü (7.1) → gizli yükleme → işlemenin bitmesi → oynatıcıda ses kontrolü (6.6) → beyan (7.4) → kontrol adımı (7.6) → zamanlama.

---

## 8. Uçtan uca örnek: KM-001, kameraya çıkmadan

Örnek `senaryolar/01-chatgptyi-yanlis-kullaniyorsun.md` üzerinedir (tahmini 12:15; senaryo 01'deki süre dökümü). Yol B varsayılmıştır; Yol A'da 6–8. satırların yerini 03 belgesi Aşama 5 alır. 03 belgesinde süresi yazılı aşamalarda o süre kullanıldı; diğerleri **[Tahmini]** ve ilk videoda ölçülecek. Araç adları 03 belgesi 3.3'teki sıfır bütçe setidir.

| # | Adım | Araç | Süre | Çıktı dosyası |
|---|---|---|---|---|
| 1 | Brief ve ön test (senaryo 01, 2.2–2.5) | Markdown şablonu, sohbet asistanı, tablo yazılımı | 03 belgesi Aşama 3 | `01_brief/video-brief.md` |
| 2 | Elle koşu: teklif e-postası yapay zekâsız yazılır, sorular kâğıda not edilir | OBS Studio + `kronometre.html` | görev süresi + 15 dk | `03_ham/KM-001_elle-kosu_ham.mp4`, `olcum.md`, kâğıt not |
| 3 | Masaüstü hazırlığı (3.1) ve 10 saniyelik deneme kaydı | Çekim profili, çekim hesabı | 10 dk [Tahmini] | — |
| 4 | Kayıt A: süreli akış, tek kesintisiz (senaryo 01, 2.6) | OBS Studio + `kronometre.html` | 03 belgesi Aşama 4 (50 dk, ek çekimler dâhil) | `03_ham/KM-001_b3-kronometre-kosusu_ham.mp4`, `arac-ciktilari.md` |
| 5 | Kayıt B ve C: katkı gösterimi ve kötü örnekler, süre dışı | OBS Studio | Aşama 4 içinde | `03_ham/KM-001_ek_b-p0…p3_ham.mp4`, `KM-001_ek_c-…_ham.mp4` |
| 6 | Yer tutucuları doldur, karar kurallarını uygula (senaryo 01, 2.8), senaryoyu kilitle | Markdown | Aşama 4 içinde (10 dk) | `02_senaryo/senaryo_KILIT.md` |
| 7 | Okunuş metnini türet: sayılar, kısaltmalar, sözlük, `[D]` işaretleri (2.3–2.4) | Metin düzenleyici, `telaffuz-sozlugu.md` | 15 dk [Tahmini] | `02_senaryo/KM-001_tts-metni.md` |
| 8 | Sesi 13 bölüm hâlinde üret, dinle, hatalı cümleleri yeniden üret; hook üç kez (2.5) | Seçilen seslendirme aracı | 40 dk [Tahmini; ilk videoda daha uzun] | `04_ses/ham/KM-001_b01p01_tts_v1.wav` … , `tts-kaydi.md` |
| 9 | Ses sonrası işlem ve baştan sona dinleme (2.6) | Audacity | 10 dk + 10 dk dinleme [Tahmini] | `04_ses/temiz/KM-001_b01_tts_TEMIZ.wav` … |
| 10 | Masa çekimi: yapışkan not + elle koşudaki gerçek kâğıt, üstten, yüz yok; bir yatay bir dikey (senaryo 01, 5:40) | Telefon, masa lambası | 15 dk [Tahmini] | `03_ham/KM-001_ek_masa_yatay.mp4`, `_dikey.mp4` |
| 11 | Kurgu 1: şablonu aç, sesi diz, okunuş kontrolü, A1'i kilitle (6.2) | DaVinci Resolve | 03 belgesi Aşama 6, adım 1 (20 dk) | `05_proje/` |
| 12 | Kurgu 2: Kayıt A'yı hizala, beklemeleri yönet (3.5); eksik anlatım görüntülerini sese göre çek (3.3) | DaVinci Resolve, OBS Studio | Aşama 6, adım 2 (30 dk) + 15 dk ek çekim [Tahmini] | `03_ham/KM-001_ek_anlatim-…_ham.mp4` |
| 13 | Kurgu 3: yakınlaştırma, vurgu, kapatma kutuları (3.4, 3.6) | DaVinci Resolve | Aşama 6, adım 3 (30 dk) | — |
| 14 | Kurgu 4: sabit grafikler: adım sayacı 1/7–7/7, önce/sonra bölünmüş ekran, karşılaştırma tablosu, "yapamadığı şey" kartı, prompt kartı | Proje şablonu (5.2) | Aşama 6, adım 4 (15 dk) | — |
| 15 | Müzik, seviye, altyazı (6.4–6.6) | DaVinci Resolve, YouTube Ses Kitaplığı, görünen metin | Aşama 6, adım 5–6 (28 dk) | `06_cikti/KM-001_SON_tr.srt` ya da görünen metin |
| 16 | Dışa aktar, dosya kontrolü (7.1), telefonda 1× izleme, düzeltme | DaVinci Resolve, telefon | Aşama 6, adım 7 (25 dk) + 10 dk | `06_cikti/KM-001_SON_[tarih].mp4` |
| 17 | Kapak: gerçek ekran parçasıyla "Önce / Sonra" | Kapak şablonu | 03 belgesi Aşama 7 (25 dk) | `06_cikti/KM-001_kapak_A.png`, `_B.png` |
| 18 | Metaveri, prompt dosyası, yükleme, beyan "Evet" + açıklama satırı, kontrol adımı, zamanlama | YouTube Studio, `yayin-metaverisi.md` | 03 belgesi Aşama 8 (30 dk) | `08_yayin/yayin-metaverisi.md` |
| 19 | Kısa videolar: görüntü uzun videodan, seslendirme ayrıca üretilir (01 belgesi 4.4) | Dikey zaman çizelgesi, seslendirme aracı | 03 belgesi Aşama 10 | `07_kisa/KM-001_K1_…_dikey.mp4` |

Bu videoda katman dökümü (senaryo 01'in süre dökümüne göre, **[Tahmini]**): bağlam sahnesi 30 sn (masa çekimi, kendi görüntün) ≈ %4; tam ekran kartlar (karşılaştırma, "yapamadığı şey" kartı, prompt kartı) tahmini 60–75 sn ≈ %8–10; açıklayıcı animasyon yok; stok plan yok; kalan tahmini %86 ekran kaydı.

Yol B'nin seslendirme toplamı (7–9. satırlar) tahmini 75 dakikadır; 03 belgesindeki kendi sesle 55 dakikadan **kısa değildir.** Sözlük oturdukça düşmesi beklenir; üçüncü videoda hâlâ 55 dakikanın üstündeyse Yol B'nin süre gerekçesi yoktur, geriye yalnızca ortam ve gizlilik gerekçeleri kalır.

---

## 9. İki araç seti

Genel araç seti, doğrulama tablosu ve "üç video üst üste ölçülmüş darboğaz olmadan satın alma" kuralı 03 belgesi Bölüm 3'tedir. Aşağıdakiler yüzsüz üretimin eklediği satırlardır. Fiyat yazılmadı; "ücretsiz" bilgisi yalnızca 03 belgesi 3.2'de durumu yazılı araçlar için verildi.

### 9.1 Sıfır bütçe seti

| Araç | Bu kanalda tam olarak ne için | Durum |
|---|---|---|
| OBS Studio | Süreli koşuyu ve anlatım kayıtlarını sabit kare hızında, kronometre karedeyken kaydetmek | Açık kaynak, ücretsiz (03 belgesi 3.2) |
| `sablonlar/kronometre.html` | Süreyi görüntünün parçası yapmak | Depoda |
| Telefon kamerası | Üstten masa çekimi; stok yerine kendi bağlam sahnen | — |
| Kendi sesin + Audacity (Yol A) | Seslendirme; sıfır bütçede varsayılan yol | Açık kaynak, ücretsiz (03 belgesi 3.2) |
| Bir seslendirme aracının deneme kullanımı (Yol B) | 2.2'deki testi yapmak | Ücretsiz katmanın varlığı, sınırı ve ticari kullanım izni doğrulanamadı **[DOĞRULA]**; izin yoksa yayında kullanılmaz |
| DaVinci Resolve (ücretsiz sürüm) | Ses merkezli kurgu, sabit grafik seti, kapatma kutuları, dikey sürüm | Ücretsiz sürüm var (03 belgesi 3.2) |
| LibreOffice Impress ya da elindeki sunum yazılımı | Formül kartı, şema ve tabloyu çizip görüntü olarak almak | LibreOffice açık kaynak ve ücretsizdir (uzun süredir sabit bilgi) |
| Tarayıcı + sohbet asistanı | Tek dosyalık hareketli sayfa (sayaç, çubuk) üretip ekran kaydıyla almak | — |
| Buzz ya da senaryodan senkronizasyon | Altyazı | 03 belgesi 3.2 |
| YouTube Ses Kitaplığı | Fon müziği | Studio içinde |
| Pexels / Pixabay / Mixkit | Yalnızca kendi çekimin yoksa, tek bağlam planı | Lisans metni **[DOĞRULA]** (4.5) |
| GIMP ya da tarayıcı tabanlı tasarım aracı | Kapak ve saydam zeminli etiketler | 03 belgesi 3.2 |

### 9.2 Rahat çalışma seti

Her satır ölçülmüş bir darboğaza bağlıdır.

| Ölçülen darboğaz | Eklenecek şey | Bu kanalda tam olarak ne için |
|---|---|---|
| Yol B seçildi ve test eşiği geçildi | Üretken ses platformunun ticari kullanıma izin veren planı (örnek: ElevenLabs; Türkçe desteği **[Resmî — sayfada teyit et]**, plan koşulu **[DOĞRULA]**) | Tek sabit sesle anlatım ve tek cümle düzeltmesi |
| Duraklama ve okunuşu elle düzeltmek her videoda 20 dakikayı aşıyor | SSML destekli bulut metin okuma servisi (Azure AI Speech, Google Cloud Text-to-Speech ya da Amazon Polly; Türkçe ses listesi **[DOĞRULA]**) | Duraklamayı ve okunuşu metnin içinde işaretleyerek tekrar üretilebilir ses almak |
| Yakınlaştırma ve imleç vurgusu kurguda 30 dakikayı aşıyor | Otomatik yakınlaştırma ve imleç vurgusu olan ticari ekran kayıt aracı (kategori; ad verilmedi, doğrulanmadı) | Anlatım kayıtlarında yönlendirme süresini kısaltmak. Süreli koşu yine kronometre karedeyken, kesintisiz kaydedilir |
| Kendi çekimin yetmiyor, ücretsiz sitelerde aynı planlar dönüyor | Abonelikli stok kitaplığı (kategori) | Videoda en çok bir iki bağlam planı |
| Ses Kitaplığı'nda uygun parça tekrar ediyor | Lisanslı müzik aboneliği (03 belgesi 3.3) | Fon müziği |
| Masa çekimi karanlık ya da titrek | Telefon için üstten çekim kolu ve tek ışık | Desen kırıcı sahneler ve kısa videoların ilk karesi |
| Sabit set dışında grafik ihtiyacı üç videoda tekrarlandı | Hareketli grafik şablon paketi ya da tasarım aracının ücretli planı (lisans **[DOĞRULA]**) | Açıklayıcı animasyon (5.4) |

---

## 10. Yüzsüz üretime özel kalite kontrol ve sık yapılan hatalar

### 10.1 Ek kontrol maddeleri

`sablonlar/kalite-kontrol-listeleri.md` içindeki kapıların yerine geçmez; ilgili kapıya **eklenir**. Orada yazılı maddeler tekrar edilmedi.

**Senaryo kilidine ek**

- [ ] EKRAN alanındaki her satırda katman işareti var (`[K1]`–`[K4]`); K1 payı en az %70, K4 payı en çok %5
- [ ] Stok ya da üretilmiş görsel isteyen her satırda nesne + eylem tarifi yazılı; "kavram" tarifi yok

**Çekim öncesine ek**

- [ ] Çekim hesabı açık: hesap menüsü, dosya penceresi, adres çubuğu önerileri ve pano kişisel veri göstermiyor (3.1)
- [ ] Kayıt alanı sistem çubuğunu dışarıda bırakıyor; sistem sesi kapalı

**Seslendirmeye ek (Yol B; mevcut kapıdaki "kayıt ortamı" ve "hook 3 kez kaydedildi" maddelerinin karşılığı)**

- [ ] Okunuş metni kilitli senaryodan türetildi; yer tutucu yok; bütün sayılar yazıyla
- [ ] Ses adı, ses motoru ve ayarlar `ses-kimligi.md` ile aynı; `tts-kaydi.md` dolduruldu
- [ ] Sözlükte olmayan yeni kelime eklendi ve dinlenerek doğrulandı
- [ ] Hook üç kez üretildi; cümle arası ve bölüm arası sessizlikler standart sürede
- [ ] `[D3]` sessiz ekran süreleri ses diziminde bırakıldı

**Kurguya ek**

- [ ] Süreli kayıtta kare dondurma, yavaşlatma, döngü yok; kronometre hiçbir grafikle örtülmüyor (3.5)
- [ ] Kapatma kutuları opak; V1 ve V2'de kare kare kontrol edildi (3.6)
- [ ] Şablondan gelen hiçbir grafikte yer tutucu metin kalmadı ("BÖLÜM ADI", "0/0")
- [ ] Önce/sonra ekranında iki taraf aynı büyütme ve kırpmada
- [ ] Bağlam sahneleri ve üretilmiş görseller `lisans-kaydi.md` içinde; üretilmiş görselde "temsilî görsel" etiketi var
- [ ] Altyazı metni görünen metinden; okunuş yazımı sızmadı

**Yayın öncesine ek**

- [ ] Yol B: beyan "Evet"; açıklamada sentetik ses satırı var (7.2); kısa videolar için diğer platformların etiketi not edildi (03 belgesi 4.4 C)
- [ ] Sentetik ses planı, yazı tipi ve stok lisansları kayıtlı (7.6)
- [ ] Gizli yüklemede oynatıcıdan ses seviyesi kontrol edildi; ilk kare siyah değil

### 10.2 Sık yapılan 10 hata

1. **Ekranı stokla doldurmak.** Seslendirme sürerken "boş kalmasın" diye stok plan dizmek; kanıtı görüntüden çıkarır ve özgün olmayan içerik desenine yaklaştırır. Boşluk varsa senaryo uzundur.
2. **Kanıt kaydını sese uydurmak için yeniden çekmek.** İkinci koşu daha hızlı çıkar; ölçüm bozulur (03 belgesi Aşama 4: daha iyi koşu seçilmez).
3. **Süreli kayıtta kare dondurmak.** Kronometre durur, video yanlış süre gösterir.
4. **Bulanıklığa güvenmek.** Küçük yazı bulanıklığın altından okunabilir; yakınlaştırılmış kopyada kutu unutulur.
5. **Sentetik sesi saklamak.** Beyanı "Hayır" işaretlemek ya da açıklamaya yazmamak; fark edildiğinde kaybedilen şey güvendir.
6. **Sesi video ortasında ya da videodan videoya değiştirmek.** Yüzsüz kanalda ses kimliktir.
7. **Okunuş metnini tutmamak.** Her videoda aynı kelimeyi yeniden düzeltmek; sözlük bu işi bir kez yapar.
8. **Grafik setini her videoda yeniden tasarlamak.** Şablon dışı her yeni grafik hem süreyi hem tutarlılığı yer; yeni grafik ancak üç videoda gerekecekse sete girer.
9. **Lisans kaydını sonraya bırakmak.** Altı ay sonra gelen talepte dosyanın nereden indirildiği hatırlanmaz; kayıt indirme anında yazılır.
10. **Yüzün yokluğunu efektle kapatmaya çalışmak.** Hızlı kesim, ses efekti, yanıp sönen kutu; kanalın sakin tonuyla çelişir. Güven açığını kapatan şey gerçek ekran, gerçek ölçüm ve tutarlı sestir (1.2).

---

## Doğrulanacaklar (bu belgeye özgü)

| # | Konu | Nerede kontrol edilir | Bu belgede |
|---|---|---|---|
| 1 | Hazır sentetik sesle anlatım beyan gerektiriyor mu; kendi ses klonu için durum | [YouTube Yardım 14328491](https://support.google.com/youtube/answer/14328491) | 2.7, 7.4 |
| 2 | Özgün olmayan içerik tanımı ve örnekleri | [YouTube Yardım 1311392](https://support.google.com/youtube/answer/1311392) | 7.5 |
| 3 | Önerilen yükleme kodlama ayarları (bit hızı, ses) | [YouTube Yardım 1722171](https://support.google.com/youtube/answer/1722171) | 6.7 |
| 4 | Oynatmada ses yüksekliği normalleştirmesi ve hedef düzey | Resmî sayfa bulunamadı; gizli yüklemede oynatıcı istatistikleri | 6.6 |
| 5 | Seçilen seslendirme aracında Türkçe desteği, hangi ses motoru, ücretsiz katman, ticari kullanım, abonelik bitince haklar | Aracın dil listesi, fiyat ve kullanım koşulları sayfaları | 2.1, 9 |
| 6 | Bulut servislerinin güncel `tr-TR` ses listesi ve SSML desteği | Bölüm 2.1'deki üç bağlantı | 2.1, 2.3 |
| 7 | Ses klonlamada örnek kaydın saklanması ve kullanımı; aracın rıza doğrulaması | Aracın gizlilik ve kullanım koşulları | 2.7 |
| 8 | Pexels, Pixabay, Mixkit lisans metinleri | Bölüm 4.5'teki bağlantılar | 4.5 |
| 9 | Senaryodan altyazı senkronizasyonu Türkçede çalışıyor mu | 03 belgesi 0.1'deki gizli test videosu | 6.4 |
| 10 | OBS Studio kayıt biçimi varsayılanı; Resolve'da projeler arası öğe kutusu | Kullandığın sürümün ayarları | 3.2, 5.2 |
| 11 | Studio yükleme akışındaki kontrol adımının kapsamı | Studio, yükleme ekranı | 7.6 |
