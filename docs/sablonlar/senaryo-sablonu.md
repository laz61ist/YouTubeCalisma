# Senaryo — KM-[NO] · [BAŞLIK]

> Kullanım: `02_senaryo/senaryo_v1.md` olarak kopyala. Kilitlenince `senaryo_KILIT.md` adıyla kaydet. Dolu örnekler: `senaryolar/`.

| | |
|---|---|
| **Kategori** | [B/G/K/M/İ/P] |
| **Hedef süre** | [ ] dk |
| **Kelime sayısı** | [ ] (sesli okumada ölçülen süre: [ ] dk [ ] sn) |
| **Brief** | `01_brief/video-brief.md` |
| **Sürüm / tarih** | v[ ] · [YYYY-AA-GG] |
| **Durum** | Taslak / Sesli okundu / KİLİT / Yer tutucular doldu |

## Sütunlar nasıl kullanılır

| Sütun | Ne yazılır |
|-------|-----------|
| **SES** | Kelimesi kelimesine okunacak metin. Konuşur gibi; bir cümlede bir fikir. Okunuşu zor kelimenin yanına köşeli parantezle okunuş notu. |
| **EKRAN** | O cümle söylenirken ekranda ne var: hangi kayıt dosyası, hangi büyütme, hangi grafik (kronometre, alt bant, kart). Kurguda başka belgeye bakmaya gerek kalmamalı. |
| **Tutma notu** | Bu satır izleyiciyi neden tutuyor ya da neden kaybedebilir: açık döngü, yeni bilgi, görsel değişim, ödeme (verilen sözün tutulması). Boşsa satırın varlık nedenini sorgula. |

Kurallar:

- Ekranda **en geç tahmini 20–30 saniyede bir** görsel değişiklik (büyütme, kesme, grafik). Ekran sütununda art arda üç satır "aynı görüntü" yazıyorsa bölümü kısalt.
- Ölçüm, sonuç ve aracın verdiği cevap çekimden önce **yer tutucudur.** Tahminle doldurma.
- Yapay zekâ taslağından gelen görüş, deneyim ve sonuç cümleleri silinir; yerlerine yer tutucu konur.

## Blok biçimi (uzun senaryolarda)

SES metni uzun olan senaryolarda üç sütunlu tablo yerine aynı üç alan, bölüm başlığının altında üç blok olarak yazılabilir: `**SES**` (alıntı bloğu), `**EKRAN**` (madde listesi), `**Tutma notu**` (tek paragraf). `senaryolar/` klasöründeki üç senaryo bu biçimdedir. Blok biçiminde de şunlar zorunludur: yer tutucu listesi, bölüm başına hedef süre, çekim (kayıt) listesi, iddia–kaynak tablosu, kısa video işaretleri. Bölümlerin bu şablondaki karşılığı her senaryonun sonundaki "Şablon eşlemesi" tablosunda yazar.

## Yer tutucu listesi

Çekimden sonra hepsi dolmuş olmalı. Dolunca "Değer" sütununa yaz, senaryoda bul-değiştir yap.

| Yer tutucu | Anlamı | Kaynak | Değer |
|------------|--------|--------|-------|
| `[ELLE SÜRE]` | Görevin elle süresi | `olcum.md` | |
| `[YZ SÜRE]` | Kronometre koşusunun süresi | `olcum.md` | |
| `[TUR SAYISI]` | Düzeltme turu sayısı | `olcum.md` | |
| `[KURULUM SÜRE]` | Prompt'u ilk kez hazırlama süresi (ön denemeler + yazım) | `olcum.md` Bölüm 1 | |
| `[N] deneme` | Süreli koşudan önceki ön deneme sayısı | `olcum.md` Bölüm 1 | |
| `[ÇEKİMDE ÖLÇ: ...]` | Çekimde gözlenecek diğer değerler | Ham kayıt, zaman kodu | |
| `[ARAÇ CEVABI: ...]` | Aracın gerçekten yazdığı metinden alıntı | `arac-ciktilari.md` | |
| `[HATA: ...]` | Yapamadığı şey bölümündeki gerçek hata | Ham kayıt, zaman kodu | |
| `[TARİH]` | Çekim ayı ("Kasım 2026 itibarıyla") | | |

## Kronometre Yarışı dışındaki yapılar

Aşağıdaki bölümler Kronometre Yarışı (KG1) içindir. Başka bir hikâye yapısında Bölüm 1, 5, 6 ve 7 aynen kalır; **Bölüm 2–4 şöyle değişir** (iskeletlerin dakika planı: `01-icerik-uretim-sistemi.md` Bölüm 6; üretim farkları: `03-yapim-is-akisi.md` Bölüm 1.11):

| Yapı | Bölüm 2 (görev ve veri) | Bölüm 3 (gövde) | Bölüm 4 (karşılaştırma) | Ölçüm cümlesi |
|------|-------------------------|-----------------|--------------------------|---------------|
| **KG3 Hata Listesi** (Yayın 1, 6, 10) | Tek görev ve ilk (vasat) cevap; elle süre varsa hook'ta | Madde başına aynı kalıp: ne değişti → cevap nasıl değişti. Maddeler "ayrı sohbet · süre dışı" kayıtlardır; süreli akış varsa tek ve ayrıdır | İlk ve son cevap yan yana; süre yalnızca süreli akıştan | "Maddeleri ayrı ayrı gösterdim; süre tek seferlik kayıttan." |
| **KG6 Kör Test** (Yayın 3) | Kurallar, testten önce yazılmış ölçütler, test tarihi, ikinci puanlayıcı | Görev başına: prompt → üç cevap yan yana → iki puanlayıcının puanı → tablo | Toplam tablo; isimlerin açılması | "Elle süre yok; ölçülen şey ölçütlere göre puan." Kazanan senaryoda yer tutucudur |
| **KG7 Adım Adım Başlangıç** (Yayın 4) | İzleyicinin kendi işinden seçeceği görev | Adım başına: göster → alıştırma kartı | Deneme izleyicisinin uygulama süresi | "Bu süre bir kişinin ilk denemesidir." |
| **KG5 Meslek Vakası** (Yayın 7) | İş haritası: işler, elle süreler, her birinin yanında "ölçüm" ya da "beyan" etiketi | İş başına mini koşu: görev → prompt → çıktı → kontrol → süre | Devretme kararı (devredilir / kontrolle / devredilmez) ve toplam tablo; beyan süreler ayrı satırda | "Şu süreleri ben ölçtüm, şunları bir muhasebeci söyledi." |
| **KG2 Önce/Sonra + hakem** (Yayın 8) | İki sürümün nasıl hazırlandığı; "önce" sürümünün elle süresi | Hazırlık koşusu; sonra hakemin kör değerlendirmesi | Hakemin kararı ve gerekçesi: `[ÇEKİMDE: hakem ne dediyse]` | "Hakem hangisinin hangisi olduğunu bilmiyordu." |
| **KG4 Süreli Deney** (Yayın 9) | Kurallar, sayılacak metrikler, taban ölçümü | Gün gün: yalnızca yeni bir şey öğreten anlar | Sayım tablosu, tabanla karşılaştırma | "Taban, deneyden önceki haftanın elle ortalamasıdır." |

Bu yapılarda kapaktaki `[ELLE SÜRE] → [YZ SÜRE]` çifti yalnızca iki süre de ölçülmüşse kullanılır; ölçülmediyse çıktı çifti ya da soru çifti (01 belgesi Bölüm 3.1).

---

## Bölüm 1 — Hook ve görev tanımı (0:00–0:30; en çok 35 sn)

Amaç: İlk cümlede görev ve ölçülecek şey (süre kalıbında süre; çıktı kalıbında önce/sonra ya da hakem). Kanal adı, selamlama, "bu videoda" yok. Kalıp seçimi ve kontrol listesi: 01 belgesi 4.2–4.3; ilk cümle en fazla 12 kelime, en fazla 2 sözlü açık döngü, ilk 60 saniyede hiçbir istek (CTA) yok.

| # | SES | EKRAN | Tutma notu |
|---|-----|-------|------------|
| 1.1 | [Görev + elle süre. Örn. "Bu tabloyu rapora çevirmek geçen ay `[ELLE SÜRE]` sürdü."] | [Elle koşunun hızlandırılmış kaydı; sağ üstte kronometre "ELLE" etiketiyle akıyor] | Başlığın sözünü kendi kelimeleriyle tekrar eder; izleyici doğru videoda olduğunu anlar. |
| 1.2 | [Aynı iş, yeni süre: "Aynı işi şimdi yapay zekâyla yapacağım; kronometre açık."] | [Kesme: boş sohbet ekranı; kronometre 00:00, etiket "YAPAY ZEKÂ"] | Açık döngü: kaç dakika sürecek? |
| 1.3 | [Dürüstlük sözü: "Sonda süreyi ve kaliteyi yan yana koyacağım; bir de beceremediği yeri göstereceğim."] | [Karşılaştırma tablosunun boş hâli 2 sn; "Yapamadığı şey" kartı 1 sn] | İkinci açık döngü: nerede beceremedi? Sona kadar izleme nedeni. |

## Bölüm 2 — Görev ve veri (hedef: [ ] sn)

Amaç: İzleyicinin kendi işini görmesi. Kısa tut.

| # | SES | EKRAN | Tutma notu |
|---|-----|-------|------------|
| 2.1 | [Veriyi tanıt: ne, kaç satır, ne isteniyor] | [Örnek veri dosyası; ilgili sütunlar sarı kutuyla] | Tanıdıklık: "benim tablom da böyle". |
| 2.2 | [Elle yaparken zaman nereye gidiyor] | [Elle koşudan 2–3 hızlandırılmış kesit; alt bant: "1 / Elle"] | Sorunu somutlaştırır. |
| 2.3 | [Geçiş: "Şimdi aynı dosyayla..."] | [Alt bant: "2 / Yapay zekâyla"] | Bölüm işareti; izleyici nerede olduğunu bilir. |

## Bölüm 3 — Yapay zekâyla koşu (hedef: [ ] dk)

Amaç: Videonun gövdesi. Her adımda izleyici bir şey öğrenir; yalnızca "bakın yapıyor" değil.

| # | SES | EKRAN | Tutma notu |
|---|-----|-------|------------|
| 3.1 | [İlk prompt'u neden böyle yazdığını söyle] | [Prompt yazılırken yakınlaştırma (kayıt çözünürlüğünün izin verdiği ön ayar); kayda gömülü kronometre başlıyor] | Yeni bilgi: prompt'un mantığı. |
| 3.2 | [İlk cevap hakkında: `[ARAÇ CEVABI: ...]`] | [Cevap akarken "hızlandırıldı ×N" etiketi; kronometre gerçek süreyi sayıyor] | Görsel değişim + ilk ara sonuç. |
| 3.3 | [Neyin eksik/yanlış olduğunu göster] | [Hatalı kısım sarı kutuyla] | Küçük gerilim: düzelecek mi? |
| 3.4 | [Düzeltme prompt'u ve gerekçesi] | [İkinci prompt; kronometre görünür] | Öğretici an: nasıl düzeltilir. |
| 3.5 | [Çıktıyı kontrol et: `[ÇEKİMDE ÖLÇ: doğruluk kontrolünün sonucu]`] | [Çıktı ile kaynak veri yan yana; kontrol edilen 2–3 değer işaretli] | Güven: izleyici kontrolün yapıldığını görür. |
| 3.6 | ["Kronometreyi durduruyorum."] | [Kronometre durur: `[YZ SÜRE]`; kısa ses efekti] | Birinci açık döngünün ödemesi. |

*(Gerektiği kadar satır ekle. Uzun bölümü ara başlıkla böl; her ara başlıkta alt bant. İlk somut sonuçtan hemen sonraki satırın EKRAN sütununa 5–7 saniyelik görsel abone alt bandını yaz: "Her hafta bir iş, kronometreyle." SES bu çağrıya değinmez; 01 belgesi 8.1.)*

## Bölüm 4 — Süre ve kalite karşılaştırması (hedef: [ ] sn)

| # | SES | EKRAN | Tutma notu |
|---|-----|-------|------------|
| 4.1 | [Süre: "Elle `[ELLE SÜRE]`, yapay zekâyla `[YZ SÜRE]`; `[TUR SAYISI]` düzeltme turu dâhil."] | [Karşılaştırma tablosu: Süre satırı doluyor] | Başlığın sözü tutuluyor (vaat testi burada). |
| 4.1b | [Ölçüm koşulu, sabit cümle: "Prompt'u önceden `[N]` denemede hazırladım; bu süre hazır prompt'la. İlk kez yapan için hazırlık dâhil `[KURULUM SÜRE]` daha ekle. Elle yolu önce yaptığım için dosyayı da tanıyordum."] | [Tablonun altında ayrı satır: "İlk kurulum (bir kez): `[KURULUM SÜRE]`"] | Yanlılığı izleyiciden önce sen söylersin; güven. |
| 4.2 | [Kalite: elle yapılanla farkı dürüstçe söyle; `[ÇEKİMDE ÖLÇ]`] | [İki çıktı yan yana; farklar kutuyla] | Abartısız değerlendirme güveni artırır. |
| 4.3 | [Geçiş: "Ama bir yerde takıldı."] | ["Yapamadığı şey" kartı] | İkinci açık döngüye köprü. |

## Bölüm 5 — Yapamadığı şey (hedef: [ ] sn)

Amaç: Çekimde gerçekten yaşanan bir sınır. Genel uyarı ("her zaman kontrol edin") tek başına yetmez.

| # | SES | EKRAN | Tutma notu |
|---|-----|-------|------------|
| 5.1 | [Ne oldu: `[HATA: ...]`] | [Hatanın yaşandığı anın ham kaydı, büyütülmüş] | İkinci açık döngünün ödemesi. |
| 5.2 | [Neden önemli: iş bağlamında sonucu ne olurdu] | [Hatalı değerin gittiği yer: rapor/e-posta] | İzleyicinin kendi riskine bağlar. |
| 5.3 | [Nasıl yakalanır / ne yapmalı] | [Kontrol adımı ekranda] | Uygulanabilir çıkarım. |
| 5.4 | [Yorum sorusu: cevabı tek satır olan, belirli bir soru + cevapların ne için kullanılacağı. Kör testte bu satır isimler açılmadan önceye taşınır.] | [Soru alt bantta yazılı; aynı soru sabitlenmiş yorumda] | Sözlü CTA 1/3 (01 belgesi 8.3). İzleyicinin söyleyecek bir şeyi olduğu an. |

## Bölüm 6 — Kopyalanabilir prompt (hedef: [ ] sn)

| # | SES | EKRAN | Tutma notu |
|---|-----|-------|------------|
| 6.1 | [Prompt'un son hâlini tanıt; hangi alanların değişeceğini söyle] | [Prompt kartı; değişecek alanlar sarı] | Elle tutulur çıktı; kaydetme nedeni. |
| 6.2 | ["Kopyalanabilir hâli açıklamada."] | [Kart altında: "Açıklamada kopyalanabilir hâli var"] | Sözlü CTA 2/3 (01 belgesi 8.4). Tek ve net yönlendirme. |

## Bölüm 7 — Kapanış ve sonraki video (hedef: 20–30 sn)

Amaç: Özet tekrarı ve vedalaşma yok. Son sesli cümle sonraki videodur (ana CTA; 01 belgesi 8.2). Sesli abone çağrısı yok; abone düğmesi bitiş ekranında görsel olarak durur.

| # | SES | EKRAN | Tutma notu |
|---|-----|-------|------------|
| 7.1 | [Bu videonun açık bıraktığı soru, tek cümle; özet değil] | [Sonraki videonun malzemesinden 2–3 saniyelik görüntü] | Kapanış hissi vermeden sonraki videoya gerekçe. |
| 7.2 | [Sonraki video: bu işin devamı olan görev ve neden izlemeli. Videonun son sesli cümlesi.] | [Bitiş ekranı (son 15–20 sn): önerilen tek video solda, abone düğmesi sağda] | Sözlü CTA 3/3. Oturumu uzatır. |

---

## Çekim listesi (EKRAN sütunundan derlenir)

| # | Kayıt | Dosya adı | Çekildi |
|---|-------|-----------|---------|
| 1 | Elle koşu (kronometre karede, "ELLE" etiketiyle) | `KM-[NO]_elle-kosu_ham.mp4` | [ ] |
| 2 | Süreli koşu (tek kayıt, yeni sohbet, kronometre karede) | `KM-[NO]_b3-kronometre-kosusu_ham.mp4` | [ ] |
| 3 | Veri tanıtımı | | [ ] |
| 4 | Önce/sonra karşılaştırma | | [ ] |
| 5 | Hata anı yakın çekim (süre dışı, ayrı kayıt) | | [ ] |
| 6 | Prompt tam ekran | | [ ] |
| 7 | Kısa video için dar pencere / yüksek yakınlaştırmayla yeniden çekim (kayıt 1080p ise) | | [ ] |

## İddia–kaynak tablosu (doğruluk kontrolü)

| Satır | İddia | Kaynak (`çekim` + zaman kodu / `olcum.md` / birincil kaynak bağlantısı / `görüş`) |
|-------|-------|-------|
| | | |
| | | |

## Kısa video işaretleri

Senaryoyu yazarken kısa videoya dönebilecek satır aralıklarını işaretle.

| Aday | Satırlar | Tür (önce/sonra / hata–yapamadığı şey / tek ipucu; 01 belgesi 4.4) | Kendi başına anlaşılır mı? |
|------|----------|--------------------------------------------|----------------------------|
| K1 | | | |
| K2 | | | |
| K3 | | | |
