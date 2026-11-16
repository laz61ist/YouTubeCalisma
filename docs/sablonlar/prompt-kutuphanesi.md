# Prompt Kütüphanesi — Kısa Mesai

> Kullanım: Her prompt tam metindir; kod bloğunu kopyala, köşeli parantezli alanları doldur. Hangi sohbet asistanını kullandığın fark etmez. Her üretim oturumunda **yeni bir sohbet** aç, önce P0'ı yapıştır.

## Ortak kurallar

1. **Asistan senin kanal verini, YouTube arama hacmini ya da bir testin sonucunu bilmez.** Sayı, sonuç ya da alıntı üretirse kullanma. Prompt'ların hepsi bunu yasaklar; yine de çıktıyı kontrol et.
2. Çıktı bir **taslaktır.** Yayına giden her cümle senin elinden geçer.
3. Prompt'lara gerçek müşteri/şirket verisi, kişisel bilgi yapıştırma.
4. Bir prompt iki kez üst üste işe yaramaz çıktı verdiyse düzeltmekle uğraşma; işi elle yap, prompt'u bu dosyada güncelle ve altına tarihli not düş.
5. **Asistana saydırma.** Dil modelleri karakter, kelime ve yorum sayısını güvenilir saymaz; "say, tahmin etme" demek sayımı doğru yapmaz. Karakter sayısı için Studio'daki sayacı ya da tabloda `=UZUNLUK()` işlevini, kelime sayısı için belge düzenleyicinin sayacını kullan; yorumları karar verecek kadar önemliyse kendin say. Prompt'lardaki kelime sınırları ("en fazla 12 kelime") asistana verilen yaklaşık hedeftir, ölçüm değildir.

| No | İş | Aşama |
|----|----|-------|
| P0 | Kanal bağlamı (her sohbetin başına) | Hepsi |
| P1 | Konu araştırması ve görev daraltma | 1 |
| P2 | Başlık üretimi | 2 |
| P3 | Hook varyasyonları | 3 |
| P4 | Senaryo taslağı | 3 |
| P5 | Senaryo eleştirisi | 3 |
| P6 | Kapak metni | 2, 7 |
| P7 | Açıklama ve bölüm listesi | 8 |
| P8 | Kısa videoya kesilecek anları bulma | 10 |
| P9 | Yorum özetleme | 1, 9 |
| P10 | Performans yorumu | 9 |
| P11 | LinkedIn gönderisi | 10 |
| P12 | Örnek veri seti | 3 |
| P13 | Bülten sayısı (KM-011'den itibaren) | 10 |

---

## P0 — Kanal bağlamı

Her yeni sohbetin ilk mesajı. Diğer prompt'lar bunun yapıştırıldığını varsayar.

`[DAKİKADA KELİME]` senin ölçümündür: ilk senaryonu baştan sona sesli oku, kelime sayısını (belge düzenleyicinin sayacından) okuma süresine böl, sonucu buraya bir kez yaz. Ölçene kadar satırı sil; hazır bir "ortalama konuşma hızı" yazma, kişiden kişiye değişir.

```text
Bundan sonraki isteklerimde aşağıdaki kanal bağlamını esas al. Bu mesaja yalnızca "Anlaşıldı" diye cevap ver.

KANAL: "Kısa Mesai" — Türkçe YouTube kanalı. Tek kişi üretiyor. Yüz yok; ekran kaydı + seslendirme.
NİŞ: Teknik olmayan çalışanlar ve küçük işletmeler için işte pratik yapay zekâ kullanımı.
VAAT: "Aynı işi yarı sürede bitir."
İZLEYİCİ: 26–42 yaş beyaz yakalı, serbest çalışan ya da küçük işletme sahibi. Excel, e-posta, rapor, sunumla uğraşıyor. Yapay zekâ sohbet araçlarını denedi, "vasat cevap veriyor" deyip bıraktı. Sorunu arar, aracın adını değil.
TON: Sakin, net, abartısız; işini bilen bir iş arkadaşı gibi. "Sen" diye hitap eder.
YASAKLAR: "Zengin ol" vaadi, tık tuzağı, sahte aciliyet, korku ("işsiz kalacaksın"), abartı sıfatları (inanılmaz, şok, efsane, mucize), TAMAMI BÜYÜK HARF kelime.
İMZA FORMAT: Açılışta gerçek bir görev ve elle süresi → ekranda kronometre → sonda süre ve kalite karşılaştırması → "yapamadığı şey" bölümü → kopyalanabilir prompt.
KAPAK KALIBI: Koyu lacivert zemin, sarı metin: "[ELLE SÜRE] → [YZ SÜRE]" (ör. "3 sa → 12 dk").
KONUŞMA HIZIM: dakikada [DAKİKADA KELİME] kelime.

SENİN İÇİN KURALLAR:
1. Test sonucu, ölçüm, süre, istatistik, arama hacmi, alıntı ya da kişisel deneyim UYDURMA. Böyle bir bilgi gerekiyorsa yerine köşeli parantezli yer tutucu yaz: [ÇEKİMDE ÖLÇ], [ELLE SÜRE], [YZ SÜRE], [KAYNAK GEREKLİ].
2. Emin olmadığın şeyi emin gibi yazma; "bilmiyorum, şunu kontrol et" de.
3. Türkçe yaz. "yapay zekâ" şapkalı yazılır. Araç adlarında sürüm numarası ve fiyat kullanma.
4. Dolgu ve motivasyon cümlesi yazma. İstenen biçimin dışına çıkma.
```

---

## P1 — Konu araştırması ve görev daraltma

Ne zaman: Aşama 1. Girdi olarak **kendi topladığın** arama önerilerini ve yorum cümlelerini verirsin.

```text
Bir konu alanını, kanalın formatına uyan tek görevlik video fikirlerine daraltmama yardım et.

KONU ALANI: [KONU ALANI — ör. "Excel'de aylık raporlama"]
HEDEF MESLEK/DURUM: [KİM — ör. "küçük bir toptancıda satış destek uzmanı"]

YOUTUBE ARAMA ÖNERİLERİ (kendim topladım, tarih: [TARİH]):
[ARAMA ÖNERİLERİ LİSTESİ]

İZLEYİCİ CÜMLELERİ (yorumlardan / sohbetlerden, olduğu gibi):
[İZLEYİCİ CÜMLELERİ]

RAKİP GÖZLEMİM (aynı aramada ilk sayfada ne gördüm):
[RAKİP GÖZLEMİ]

İSTEDİĞİM ÇIKTI:
1. Bu konu alanında, ekran kaydıyla baştan sona gösterilebilecek 8 somut görev listele. Her görev için tek satır: görev | girdi (hangi dosya/veri) | beklenen çıktı.
2. Her görev için şu kalıpta tek cümle yaz: "[Kim], [hangi işi] yapıyor; elle: [ELLE SÜRE], yapay zekâyla: [YZ SÜRE]." Süreleri yer tutucu olarak bırak; tahmin yazma.
3. Her görev için: yapay zekânın bu görevde hata yapması en olası yer neresi? (Bu, "yapamadığı şey" bölümü için sınayacağım hipotez; kesin bilgi gibi yazma, "sınanacak:" diye başlat.)
4. Her görev için izleyicinin aramada yazabileceği 2 ifade öner. Yalnızca yukarıdaki arama önerileri ve izleyici cümlelerinden türet; arama hacmi hakkında yorum yapma.
5. En sonda: bu 8 görevden hangi 3'ü kanalın formatına en uygun ve neden? Gerekçeyi şu ölçütlere bağla: sorun tanıdıklığı, süre farkının kapakta anlaşılırlığı, önce/sonra görsel kanıtı, kopyalanabilir çıktı.

Çıktıyı bir tablo + altında 3 maddelik öneri olarak ver.
```

---

## P2 — Başlık üretimi

Ne zaman: Aşama 2. Çıktının en az üçte birini sil; kalanları kendin yeniden yaz.

Formül numaraları `01-icerik-uretim-sistemi.md` Bölüm 2.2'deki F1–F16 ile aynıdır; brief'e ve performans kaydına bu numarayı yaz. Karakter sayısını ve ilk 45 karakterde ne göründüğünü asistana sorma: seçtiğin başlıkları tabloya yapıştır, `=UZUNLUK()` ile say ya da Studio'daki sayaca bak, telefonda nasıl kesildiğine kendin bak.

```text
Aşağıdaki video için başlık adayları yaz.

GÖREV (tek cümle): [GÖREV CÜMLESİ]
İZLEYİCİNİN SORUNU KENDİ AĞZINDAN: [İZLEYİCİ CÜMLESİ]
KATEGORİ: [B/G/K/M/İ/P]
ELLE SÜRE: [ELLE SÜRE ya da "henüz ölçülmedi"]
YAPAY ZEKÂYLA SÜRE: [YZ SÜRE ya da "henüz ölçülmedi"]
KAPAKTA YAZACAK METİN: [KAPAK METNİ — başlık bunu tekrar etmemeli]

KURALLAR:
- Önce sorun ya da sonuç, sonra araç adı. Araç adı hiç olmasa da olur.
- Görevi anlatan kritik kelimeler başlığın başında olsun; araç adı ve ek bilgi sona.
- Bir başlıkta en fazla bir sayı çifti.
- Ölçülmemiş süreyi sayıyla yazma; [ELLE SÜRE] / [YZ SÜRE] yer tutucusunu kullan.
- Her kelimenin ilk harfi büyük. Ünlem, soru işareti yığını, TAMAMI BÜYÜK kelime yok.
- Kanalın yasaklı vaat ve sıfatlarını kullanma. Sürüm numarası yok.
- Kapaktaki metni tekrar etme; kapak sayıyı söyler, başlık görevi ve bağlamı.

İSTEDİĞİM ÇIKTI:
15 başlık. Aşağıdaki formüllerden en az 6 farklısını kullan; kategoriye uymayanı zorlama. Her başlığın yanına formül numarasını yaz.
F1  [Elle süre]lik [iş]i [yeni süre]de bitirmek
F2  [Araç]ı yanlış kullanıyorsun: aynı görevde [N] [düzeltme]
F3  [A], [B], [C]: [belirli iş]te kör test, [N] gerçek iş
F4  [Meslek] için yapay zekâ: [N] iş, biri devredilmez
F5  [Süre] boyunca [şey]i yapay zekâya yaptırdım: [N] adet, [N] tanesini kendim yaptım
F6  [İki sürüm hazırladım], [uzman] hangisini seçti?
F7  Hiç [yapmamış] biri için [konu]: ilk gerçek iş, [süre]de
F8  [İş]i yapay zekâya yaptırmak: çalışan [N], çalışmayan [N] örnek
F9  Her gün kullandığım [N] prompt: her biri gerçek bir işte
F10 [Sorun cümlesi]? [Çözümün adı], kronometreyle
F11 [İş]: elle [süre], yapay zekâyla [süre] — fark nerede?
F12 Kontrol dâhil [N] dakikada [somut çıktı]
F13 [Araç]ın [iş]te yapamadığı [N] şey
F14 [Küçük işletme türü] için: [iş]i [süre]de
F15 [İş]: [N] dakika iş, [N] dakika kontrol
F16 [İş alanı]nda yapay zekâya devretmediğim [N] iş (ve nedeni)
Süre taşıyan formüllerde (F1, F11, F12) kapak süresiz olur; KAPAKTA YAZACAK METİN süre çiftiyse bu formülleri kullanma. Adet ve süre gereken her yerde yer tutucu bırak: [N], [ELLE SÜRE], [YZ SÜRE].

Tablo sütunları: # | Başlık | Formül (F no). Karakter sayısı yazma; sayamazsın.
Tablonun altına: en güçlü bulduğun 3 başlığı ve her biri için tek cümlelik gerekçe yaz. Tıklanma oranı tahmini yapma.
```

---

## P3 — Hook varyasyonları

Ne zaman: Aşama 3, iskelet yazıldıktan sonra. Seçtiğin hook'u kendi cümlelerinle yeniden yaz ve sesli oku.

```text
Aşağıdaki video için ilk 30 saniyenin (hook) varyasyonlarını yaz.

BAŞLIK: [BAŞLIK]
KAPAK METNİ: [KAPAK METNİ]
GÖREV: [GÖREV CÜMLESİ]
ELLE SÜRE: [ELLE SÜRE]
YAPAY ZEKÂYLA SÜRE: [YZ SÜRE ya da "çekimde ölçülecek"]
VİDEONUN SONUNDA GÖSTERİLECEK ŞEY: [SON ÖDEME — ör. "iki raporun yan yana karşılaştırması ve hatalı toplam"]
İLK 5 SANİYEDE EKRANDA OLACAK GÖRÜNTÜ: [AÇILIŞ GÖRÜNTÜSÜ]

KURALLAR:
- İlk cümle en fazla 12 kelimedir; görevi ve ölçülecek şeyi söyler (süre kalıbında süre; çıktı kalıbında önce/sonra ya da hakem). Selamlama, kanal adı, "bu videoda", "merhaba arkadaşlar" yok.
- İlk cümle başlığın verdiği sözü kendi kelimeleriyle tekrar eder.
- Her varyasyonda en az bir açık döngü olsun (sonda kapanacak bir soru).
- Hook, "yapamadığı şey" bölümünün geleceğini haber verir.
- Konuşma dili; cümle başına en fazla 14 kelime. Toplam 55–75 kelime.
- Ölçülmemiş sayı yerine yer tutucu. Abartı ve yasaklı ifadeler yok.

İSTEDİĞİM ÇIKTI:
6 varyasyon, her biri farklı bir açıyla:
1. Süreyle açan ("Bu iş [ELLE SÜRE] sürdü.")
2. Sorun cümlesiyle açan (izleyicinin kendi ağzından)
3. Sonuçla açan (bitmiş çıktıyı göstererek)
4. Hatayla açan (yapay zekânın beceremediği yeri öne alarak)
5. Karşılaştırmayla açan (iki çıktı yan yana)
6. Soruyla açan (cevabı videoda olan tek soru)

Her varyasyon için iki sütunlu tablo ver: SES | EKRAN. Altına tek satır: "Açık döngü: ..." ve "Kapanacağı bölüm: ...".
```

---

## P4 — Senaryo taslağı

Ne zaman: Aşama 3, iskeletten sonra. **Taslak yapıyı verir; metni sen yeniden yazarsın.**

Asistanın tuttuğu uzunluk yaklaşıktır. Gerçek süreyi sesli okumada ölçersin; taslağın kelime sayısına belge düzenleyicinin sayacından bak. Kronometre Yarışı dışındaki hikâye yapılarında "BÖLÜM SIRASI" kuralını `senaryo-sablonu.md` içindeki uyarlama tablosuna göre değiştir.

```text
Aşağıdaki iskeletten bir senaryo taslağı yaz.

BAŞLIK: [BAŞLIK]
HEDEF UZUNLUK: [HEDEF SÜRE] dakika; konuşma hızım kanal bağlamında yazılı. Hız yazılı değilse uzunluğu ben ayarlarım; kelime sayısı tahmini yürütme.
GÖREV: [GÖREV CÜMLESİ]
ÖRNEK VERİ: [VERİ TANIMI — kaç satır, hangi sütunlar, içindeki tuzaklar]
KULLANILACAK ARAÇ(LAR): [ARAÇLAR]
SEÇİLEN HOOK: [HOOK METNİ]
BÖLÜM İSKELETİ (her bölüm için tek cümle):
[İSKELET]
ÖN DENEMEDE GÖZLEDİKLERİM (kendi notlarım):
[ÖN DENEME NOTLARI]
KULLANACAĞIM PROMPT'LAR (videoda gösterilecek):
[VİDEODAKİ PROMPT'LAR]

BİÇİM:
Her bölüm için üç sütunlu tablo: SES | EKRAN | Tutma notu.
- SES: kelimesi kelimesine okunacak metin; konuşma dili, kısa cümle, "sen" hitabı.
- EKRAN: o cümle söylenirken ekranda ne var (hangi kayıt, hangi büyütme, hangi grafik: kronometre, alt bant, karşılaştırma tablosu, "yapamadığı şey" kartı, prompt kartı).
- Tutma notu: bu satır izleyiciyi neden tutar (açık döngü, yeni bilgi, görsel değişim, ödeme).

KESİN KURALLAR:
1. Ölçüm, süre, sonuç, aracın verdiği cevap ve yaşanan hata için ASLA içerik uydurma. Yer tutucu kullan: [ELLE SÜRE], [YZ SÜRE], [TUR SAYISI], [ÇEKİMDE ÖLÇ: ne ölçülecek], [ARAÇ CEVABI: neye bakılacak], [HATA: ne aranacak].
2. Benim adıma görüş ya da deneyim cümlesi yazma ("bence", "yıllardır", "her zaman kullanırım"). Görüş gereken yere [GÖRÜŞ: konu] yaz.
3. İstatistik, araştırma, alıntı yok.
4. Bölüm sırası: Hook → Görev ve veri → Yapay zekâyla koşu → Süre ve kalite karşılaştırması → Yapamadığı şey → Kopyalanabilir prompt → Kapanış ve sonraki video.
5. "Yapay zekâyla koşu" bölümünde her adım izleyiciye bir şey öğretsin: prompt neden böyle yazıldı, cevap nasıl kontrol edildi.
6. Kapanışta özet tekrarı yok; tek cümle sonuç + bir sonraki video.
7. EKRAN sütununda art arda üç satır aynı görüntü olmasın.

En sona iki liste ekle:
A) Kullandığın tüm yer tutucular ve her birinin çekimde nasıl doldurulacağı.
B) Senaryoda kaynağı gereken olgusal iddialar (varsa) — satır numarasıyla.
```

---

## P5 — Senaryo eleştirisi

Ne zaman: Aşama 3, sesli okumadan sonra. Tercihen taslağı yazan sohbetten **farklı, yeni** bir sohbette çalıştır. Önerilerden en fazla 3'ünü uygula.

```text
Aşağıdaki senaryoyu, videoyu yarıda bırakmaya hazır sabırsız bir izleyicinin gözüyle eleştir. Övgü yazma; yalnızca sorun ve düzeltme.

İZLEYİCİ: [İZLEYİCİ TANIMI — ör. "muhasebe bürosunda çalışan, ChatGPT'yi iki kez deneyip bırakmış biri"]
BAŞLIK VE KAPAĞIN VERDİĞİ SÖZ: [BAŞLIK] / [KAPAK METNİ]
HEDEF SÜRE: [HEDEF SÜRE] dakika

SENARYO:
[SENARYO METNİ]

ŞU SIRAYLA DEĞERLENDİR:
1. SÖZ: Başlık ve kapağın verdiği söz hangi satırda tutuluyor? Çok mu geç? Tutulmuyorsa açıkça söyle.
2. İLK 30 SANİYE: İlk cümle görevi ve süreyi söylüyor mu? Silinebilecek kelime/cümle hangileri?
3. ÇIKIŞ NOKTALARI: İzleyicinin videodan çıkma olasılığı en yüksek 5 yeri satır numarasıyla göster. Her biri için: neden çıkar (tekrar, yavaş giriş, soyut anlatım, ekranda değişiklik yok, söz gecikiyor) ve somut düzeltme (sil / kısalt / öne al / ekrana şunu koy).
4. DOLGU: Bilgi taşımayan, tekrar eden ya da motivasyon amaçlı cümleleri satır numarasıyla listele.
5. TON: Abartı, tık tuzağı, sahte aciliyet, "zengin ol" iması ya da izleyiciyi küçümseyen ifade var mı?
6. KANIT: Kanıtı ekranda gösterilmeyen iddialar hangileri? Yer tutucu olması gerekirken sayı/sonuç yazılmış satır var mı?
7. ANLAŞILIRLIK: Teknik olmayan biri için açıklanmadan geçilen terimler hangileri?
8. EKRAN: Art arda aynı görüntünün kaldığı, görsel değişim olmayan uzun kısımlar hangileri?

ÇIKTI BİÇİMİ:
- Önce tek paragraflık hüküm: bu senaryonun en büyük tek sorunu ne?
- Sonra tablo: Satır | Sorun | Tür | Önerilen düzeltme.
- En sonda: yalnızca 3 değişiklik yapabilecek olsam hangileri?

Senaryoyu yeniden yazma. Tutma oranı ya da izlenme tahmini verme; bunu bilemezsin.
```

---

## P6 — Kapak metni

Ne zaman: Aşama 2 (eskiz) ve Aşama 7 (son kapak). Kapağın ana metni sabit kalıptır; bu prompt yalnızca görev etiketini ve küçük ek metni üretir.

```text
Kapak görseli için kısa metin seçenekleri yaz.

BAŞLIK (kapak bunu tekrar etmemeli): [BAŞLIK]
ANA METİN (sabit kalıp, değiştirme): "[ELLE SÜRE] → [YZ SÜRE]"
GÖREV: [GÖREV CÜMLESİ]
KAPAKTA GÖRÜNECEK EKRAN PARÇASI: [GÖRSEL KANIT — ör. "karışık tablo köşesi ve temiz rapor"]

KURALLAR:
- Görev etiketi 1–2 kelime, büyük harfle yazılacak, telefonda küçük boyutta okunacak. Türkçe karakterler doğru (İ, Ş, Ğ, Ü, Ö, Ç).
- Kapakta dönüşüm çifti dışında en fazla 2 kelimelik tek etiket (toplam en fazla 2 metin bloğu; 01 belgesi 3.2).
- Başlıktaki kelimeleri tekrar etme.
- Abartı sıfatı, ünlem, soru işareti yok.
- Sayı uydurma; ana metindeki yer tutuculara dokunma.

İSTEDİĞİM ÇIKTI:
1. 10 görev etiketi seçeneği (1–2 kelime).
2. 5 küçük ek etiket seçeneği (ör. "7 alışkanlık", "tek prompt", "1 hata") — yalnızca videoda gerçekten varsa kullanacağım; içerik uydurma, [N] yer tutucusu bırak.
3. Üç kapak varyasyonu tarifi: her biri için ana metnin konumu, etiketin konumu, ekran parçasının konumu ve boyutu. Yalnızca düzen tarif et; renk paleti sabit (koyu lacivert zemin, sarı ana metin, beyaz etiket).
4. Her varyasyon için: başparmak tırnağı boyutunda ilk okunan öğe ne olur?
```

---

## P7 — Açıklama ve bölüm listesi

Ne zaman: Aşama 8. Zaman damgalarını kurgudan **kendin** alırsın; asistan yalnızca bölüm adlarını ve metni yazar.

Açıklamanın ilk iki satırının "daha fazla göster"den önce sığıp sığmadığına yayın önizlemesinde, karakter sınırlarına Studio'daki sayaçtan bak; asistanın yazdığı karakter sayısını kullanma. Bölüm sürelerini (en az 10 saniye) zaman damgalarından kendin kontrol et.

```text
Yayınlanacak video için açıklama metni ve bölüm listesi hazırla.

BAŞLIK: [BAŞLIK]
ÖLÇÜMLER (olcum.md dosyasından, aynen kullan): elle [ELLE SÜRE], yapay zekâyla [YZ SÜRE], düzeltme turu [TUR SAYISI]
ÖLÇÜM KOŞULU (olcum.md dosyasından): ön deneme sayısı [N], kurulum süresi [KURULUM SÜRE], elle süreyi ölçen [KENDİM / İŞİ YAPAN KİŞİ]
KULLANILAN ARAÇLAR VE ÇEKİM TARİHİ: [ARAÇLAR] / [TARİH]
YAPAMADIĞI ŞEY (gerçekleşen): [HATA ÖZETİ]
VİDEODAKİ PROMPT'UN TAM METNİ: [PROMPT METNİ]
PROMPT DOSYASI BAĞLANTISI: [PROMPT KISA BAĞLANTISI]
İLGİLİ VİDEOLAR: [İLGİLİ VİDEO ADLARI VE BAĞLANTILARI]
ZAMAN DAMGALARI VE O ANDA OLAN ŞEY (kurgudan aldım):
[ZAMAN DAMGASI LİSTESİ — ör. "0:00 hook; 0:32 veri tanıtımı; 1:15 ilk prompt; ..."]
TRANSKRİPT (bölüm adları için):
[TRANSKRİPT]

İSTEDİĞİM ÇIKTI:
1. AÇIKLAMANIN İLK İKİ SATIRI (iki kısa cümle; ne kadar kısa o kadar iyi): görev + ölçülen sonuç. İzleyicinin aramada yazacağı ifadeyi doğal biçimde içersin. Başlığı kelimesi kelimesine tekrar etme.
2. KISA ÖZET (3–4 cümle): ne yapıldı, ne ölçüldü, nerede takıldı. Verdiğim ölçümlerin dışında sayı yazma.
3. PROMPT BLOĞU: "Videodaki prompt (kopyala, köşeli parantezli yerleri doldur):" satırı + verdiğim prompt metni, tek harfini değiştirmeden + "Düzenli hâli ve bütün prompt'lar:" satırı + bağlantı.
4. BÖLÜMLER: Verdiğim zaman damgalarını aynen kullan, yeni zaman damgası uydurma. İlk satır 0:00 olmalı. Her bölüm adı 2–5 kelime; izleyicinin atlamak isteyeceği yeri anlatsın ("Yapamadığı şey", "Kopyalanabilir prompt" gibi).
5. NASIL ÖLÇTÜM BLOĞU: çekim tarihi, araçlar, elle süreyi kimin ölçtüğü, "Prompt'u önceden [N] denemede hazırladım; bu süre hazır prompt'la. İlk kez yapan için hazırlık dâhil [KURULUM SÜRE] daha ekle." cümlesi, "Araçlar güncellendikçe sonuçlar değişebilir." Verdiğim değerlerin dışında sayı yazma.
6. SABİT YORUM için 3 seçenek: izleyiciye kendi işiyle ilgili, cevabı bir sonraki videoya fikir verecek tek soru. "Beğenmeyi unutma" türü çağrı yazma.
7. 5–8 arama ifadesi önerisi (etiket alanı için), yalnızca transkriptte geçen kavramlardan.

Açıklamada abartı, yasaklı vaat, emoji yığını ve fiyat bilgisi olmasın. Düz metin ver; YouTube açıklamaları Markdown işlemez.
```

---

## P8 — Kısa videoya kesilecek anları bulma

Ne zaman: Aşama 10, kurgu bittikten sonra. Adayları **kendin izleyip** seçersin.

```text
Aşağıdaki uzun video transkriptinden, dikey kısa videoya dönüşebilecek anları bul.

VİDEO BAŞLIĞI: [BAŞLIK]
ÖLÇÜMLER: elle [ELLE SÜRE], yapay zekâyla [YZ SÜRE]
HEDEF SÜRE (kısa video başına): [SÜRE ARALIĞI — ör. "25–50 saniye"]
ZAMAN KODLU TRANSKRİPT:
[TRANSKRİPT]

SEÇİM ÖLÇÜTLERİ:
- Uzun videoyu izlememiş biri için kendi başına anlaşılır olmalı.
- Tek bir fikir: ya bir sonuç (önce/sonra), ya bir hata ("yapamadığı şey"), ya tek bir prompt.
- Ekranda görsel bir değişim içermeli (çıktının belirmesi, hatanın işaretlenmesi, kronometrenin durması).
- Dikey çerçevede okunabilecek kadar dar bir ekran bölgesine odaklanmalı.

İSTEDİĞİM ÇIKTI:
6 aday. Her biri için:
1. Başlangıç–bitiş zaman kodu (yalnızca transkriptteki zaman kodlarını kullan; uydurma).
2. Tür: önce/sonra (sonuç) / hata ya da "yapamadığı şey" / tek ipucu (bir prompt satırı, bir alışkanlık, bir kontrol).
3. Transkriptten birebir alıntı (ilk ve son cümle).
4. Eksik bağlam: uzun videoyu görmeyen biri neyi anlamaz?
5. Yeni açılış cümlesi önerisi (yeniden seslendireceğim): en fazla 10 kelime (01 belgesi 4.4), görev ya da sonuç; sayı yalnızca uzun videonun paketi süre taşıyorsa. Yalnızca yukarıdaki ölçümleri kullan.
6. Ekrandaki üst başlık yazısı (en fazla 6 kelime).
7. Dikey çerçevede büyütülmesi gereken ekran bölgesi.
8. Son cümle: uzun videoya sözlü yönlendirme (en fazla 10 kelime; "tam hâli kanaldaki uzun videoda" anlamında).

En sonda: 6 adaydan birbirini tekrar etmeyen en iyi 3'ünü ve hangisinin uzun videodan ÖNCE yayınlanmaya uygun olduğunu (sonucu tamamen vermeden merak bırakan) gerekçesiyle söyle. İzlenme tahmini yapma.
```

---

## P9 — Yorum özetleme

Ne zaman: Aşama 9 (kendi videon) ve Aşama 1 (konu araştırması; benzer videoların yorumları). Yorumları kullanıcı adları olmadan yapıştır.

Çıktıdaki yorum sayıları **yaklaşıktır.** Performans kaydına yazacağın ya da bir karara dayanak yapacağın sayıyı (ör. "bu soruyu kaç kişi sordu") kendin say.

```text
Aşağıdaki YouTube yorumlarını özetle.

VİDEO: [BAŞLIK]
YORUMLARIN KAYNAĞI: [KENDİ VİDEOM / BENZER BİR VİDEO]
YORUM SAYISI: [N]
YORUMLAR (kullanıcı adları çıkarıldı):
[YORUMLAR]

İSTEDİĞİM ÇIKTI:
1. TEMALAR: Yorumları 4–7 temaya ayır. Her tema için: tema adı | yaklaşık kaç yorum ("yaklaşık" diye etiketle) | 2 birebir alıntı.
2. SORULAR: İzleyicilerin sorduğu soruları olduğu gibi listele. Aynı soruyu soranları birleştir; birden fazla kişi sorduysa "birden fazla" diye işaretle ve o yorumları birebir alıntıla ki kendim sayabileyim.
3. İTİRAZLAR VE DÜZELTMELER: "Bu yanlış", "bende çalışmadı", "şu eksik" türü yorumlar. Her biri için: iddia ne, kontrol etmem gereken şey ne. Kimin haklı olduğuna karar verme; kontrol listesi çıkar.
4. İZLEYİCİNİN KENDİ İŞİ: Yorumlarda geçen meslekler, görevler, araçlar (ör. "ben muhasebeciyim", "e-fatura listesi için lazım").
5. İZLEYİCİ DİLİ: Sorunu anlatırken kullandıkları ifadeler (başlık ve hook yazarken kullanacağım), birebir.
6. VİDEO FİKİRLERİ: Yalnızca yorumlarda açıkça istenen ya da en az iki kişinin sorduğu konulardan en fazla 5 fikir. Her biri: "[Kim], [hangi işi] yapıyor; elle: [ELLE SÜRE], yapay zekâyla: [YZ SÜRE]." kalıbında, süreler yer tutucu.
7. CEVAP BEKLEYENLER: Benim yanıt vermem gereken yorumlar (soru, hata bildirimi), öncelik sırasıyla.

KURALLAR: Yorumlarda olmayan bir şeyi ekleme. Verdiğin her sayı yaklaşıktır; yanına "yaklaşık" yaz ve çıktının başında tek satırla şunu belirt: "Sayılar yaklaşıktır; karar vermeden önce kendin say. Bu, toplam [N] yorumluk küçük bir örnektir, genelleme yapılamaz." "Çoğu", "pek çok" gibi oran bildiren ifade kullanma.
```

---

## P10 — Performans yorumu

Ne zaman: Aşama 9; 48 saat, 7 gün ve 28 gün kontrollerinde. Sayıları YouTube Studio'dan **kendin** kopyalarsın.

```text
Bir YouTube videosunun performans verilerini yorumlamama yardım et. Kanal yeni ve küçük; veri gürültülü. Kesin hüküm verme; hipotez üret ve her hipotezi nasıl sınayacağımı söyle.

VİDEO: [BAŞLIK] · Kategori: [B/G/K/M/İ/P] · Süre: [VİDEO SÜRESİ]
YAYINDAN BERİ GEÇEN SÜRE: [48 saat / 7 gün / 28 gün]
BU VİDEODA SINADIĞIM HİPOTEZ: [HİPOTEZ]

BU VİDEONUN VERİLERİ (YouTube Studio'dan):
- Gösterim: [ ]
- Gösterim tıklama oranı (CTR): [ ]
- Görüntüleme: [ ]
- Ortalama görüntüleme süresi: [ ]
- Ortalama görüntüleme yüzdesi: [ ]
- 30. saniyede kalan izleyici oranı: [ ]
- Trafik kaynakları (pay): Göz atma [ ] · Önerilen [ ] · YouTube araması [ ] · Shorts feed'i [ ] · Harici [ ] · Diğer [ ]
- Öne çıkan arama terimleri: [ ]
- Kazanılan abone: [ ]
- Yeni / geri dönen izleyici: [ ] / [ ]
- Prompt kısa bağlantısı tıklaması (kısaltıcının panelinden; ölçüm kurulmadıysa "ölçüm yok" yaz, 0 yazma): [ ]
- Yorum sayısı: [ ]

TUTMA GRAFİĞİ GÖZLEMLERİM (zaman damgası → o anda ekranda/seste ne vardı):
[TUTMA GÖZLEMLERİ — ör. "0:22 dik düşüş → veri tanıtımı başlıyor"; "4:10 yükseliş → hata anı"]

KANALIN ÖNCEKİ VİDEOLARI (aynı zaman noktasındaki değerler; karşılaştırma için):
[ÖNCEKİ VİDEOLAR TABLOSU — başlık | gösterim | gösterim tıklama oranı (CTR) | ort. görüntüleme yüzdesi | 30. sn | abone]

BAŞLIK/KAPAK DEĞİŞİKLİĞİ YAPILDI MI: [HAYIR / EVET: tarih ve ne değişti]

İSTEDİĞİM ÇIKTI:
1. VERİ YETERLİLİĞİ: Bu sayılarla hangi sorulara cevap verilebilir, hangilerine verilemez? Gösterim çok düşükse CTR yorumunun güvenilmez olduğunu açıkça söyle.
2. ÖNCEKİ VİDEOLARLA FARK: Hangi metrik kanalın önceki videolarından belirgin biçimde ayrışıyor? Yalnızca verdiğim tabloya dayan. Tablo boşsa ya da 5'ten az video varsa karşılaştırmanın zayıf olduğunu belirt.
3. PAKET mi İÇERİK mi: Sorun (varsa) gösterimde mi, tıklamada mı, ilk 30 saniyede mi, gövdede mi? Her biri için hangi veri bunu gösteriyor?
4. TUTMA: Verdiğim düşüş/yükseliş noktaları için olası nedenler (en fazla 2'şer) ve bir sonraki videoda sınanacak değişiklik.
5. HİPOTEZ: Sınadığım hipotez hakkında bu veri ne söylüyor: destekliyor / desteklemiyor / karar verilemez?
6. TEK DEĞİŞİKLİK: Bir sonraki videoda değiştirmem gereken TEK şey ve bunun hangi metrikte görülmesini bekleyeceğim.
7. BU VİDEO İÇİN EYLEM: Başlık ya da kapak değiştirilmeli mi? Öneriyorsan tek değişken öner ve ne kadar bekleyip neye bakacağımı söyle.

KURALLAR:
- Sektör ortalaması, "iyi CTR şudur" türü eşik ya da kıyas uydurma. Yalnızca benim verilerime dayan.
- YouTube'un öneri sisteminin iç işleyişi hakkında kesin iddiada bulunma; bir şeyi YouTube'un resmî açıklaması olarak sunacaksan öyle olduğundan emin değilsen "yaygın gözlem" de.
- Tek videodan çıkan sonuca "ipucu" de; "bulgu" deme.
```

---

## P11 — LinkedIn gönderisi

Ne zaman: Aşama 10c, uzun video yayınlandıktan sonra. Çıkan iki taslaktan birini seç ve kendi cümlelerinle yeniden yaz; "BENİM GÖZLEMİM" alanını asistana yazdırma. Akış: `03-yapim-is-akisi.md` Bölüm 5.4.

```text
Aşağıdaki videodan bir LinkedIn metin gönderisi taslağı yaz. Gönderi, videoyu izlemeyen biri için de kendi başına değer taşımalı.

GÖREV: [GÖREV CÜMLESİ]
ÖLÇÜMLER (aynen kullan): elle [ELLE SÜRE], yapay zekâyla [YZ SÜRE], düzeltme turu [TUR SAYISI]
YAPAMADIĞI ŞEY (gerçekleşen): [HATA ÖZETİ]
PROMPT'UN İSKELETİ: [PROMPT ÖZETİ]
BENİM GÖZLEMİM (kendi cümlelerimle): [GÖZLEM]

KURALLAR:
- Birinci tekil kişi; iş arkadaşına anlatır gibi. "Sen" hitabı.
- İlk iki satır sorunu söyler; "devamını gör"den önce okunan kısım bu.
- 120–180 kelime. Kısa paragraflar; her paragraf en fazla 2 satır.
- Verdiğim ölçümlerin ve gözlemin dışında sayı, sonuç, deneyim ekleme.
- Abartı ("oyunun kuralları değişti", "herkes bunu bilmeli"), emoji yığını, etiket yığını yok. En fazla 3 etiket.
- Gövdede dış bağlantı yok; bağlantıyı ilk yoruma kendim koyacağım.
- Kapanış: iş arkadaşına sorulacak türden gerçek bir soru. "Katılıyor musunuz?" değil.

İSTEDİĞİM ÇIKTI: 2 farklı taslak (biri sonuçla, biri hatayla açılan) + her biri için ilk yoruma konacak tek cümle.
```

---

## P12 — Örnek veri seti

Ne zaman: Aşama 3a (hazırlık), `00_VARLIKLAR/ornek-veri` içinde uygun set yoksa. Çıkan veriyi tabloya aç, toplamları kendin hesapla, tuzakların cevap anahtarındaki satırlarda gerçekten durduğunu gözle kontrol et; asistanın "yerleştirdim" dediği tuzak bazen yerinde olmaz.

```text
Bir video çekimi için kurgusal, gerçekçi bir örnek veri seti üret.

KURGUSAL ŞİRKET: [ŞİRKET TANIMI — ör. "Ankara'da ofis malzemeleri toptancısı, 12 çalışan"]
VERİ TÜRÜ: [TÜR — ör. "aylık satış tablosu"]
SÜTUNLAR: [SÜTUNLAR]
SATIR SAYISI: [N]
DÖNEM: [DÖNEM]
VİDEODA YAPILACAK GÖREV: [GÖREV CÜMLESİ]

KURALLAR:
- Gerçek şirket, marka, kişi adı kullanma. Kişi adı gerekiyorsa açıkça kurgusal, yaygın adlar kullan; T.C. kimlik no, telefon, e-posta, IBAN gibi alanlar üretme.
- Tutarlar ve adetler bu ölçekte bir işletme için akla yatkın olsun; Türk lirası, Türkçe tarih ve sayı biçimi (gün.ay.yıl; binlik ayırıcı nokta, ondalık virgül).
- Veride anlamlı örüntüler olsun: [İSTENEN ÖRÜNTÜLER — ör. "bir ürün grubunda düşüş, bir bölgede artış, bir grupta yüksek iade"].
- Veriye şu sorunları bilerek yerleştir: [TUZAKLAR — ör. "3 satırda farklı tarih biçimi, 2 boş hücre, 1 bariz aykırı değer, 1 yinelenen satır"].

İSTEDİĞİM ÇIKTI:
1. Veriyi CSV olarak, kod bloğu içinde ver (noktalı virgül ayırıcı).
2. Ayrı bir "cevap anahtarı" ver: yerleştirdiğin örüntüler ve sorunlar hangi satırlarda. (Bunu videoda aracın bulup bulmadığını denetlemek için kullanacağım.)
3. Toplam ve ara toplamları kendin hesaplayıp yazma; ben tabloda hesaplayacağım.
```

---

## P13 — Bülten sayısı

Ne zaman: KM-011'den itibaren, yayından sonraki cumartesi (Aşama 10; akış ve şablon: `03-yapim-is-akisi.md` Bölüm 5.6). Taslağı kendi cümlelerinle yeniden yaz; "videoda yer almayan not" satırını asistan yazmaz.

```text
Aşağıdaki videodan haftalık e-posta bülteni için düz metin taslağı yaz. Okuyan kişi videoyu izlememiş olabilir; e-posta tek başına işe yaramalı.

GÖREV: [GÖREV CÜMLESİ]
ÖLÇÜMLER (olcum.md dosyasından, aynen kullan): elle [ELLE SÜRE], yapay zekâyla [YZ SÜRE], düzeltme turu [TUR SAYISI]
PROMPT'UN TAM METNİ (tek harfini değiştirme): [PROMPT METNİ]
YAPAMADIĞI ŞEY (gerçekleşen): [HATA ÖZETİ]
VİDEO BAĞLANTISI: [BAĞLANTI]

KURALLAR:
- Düz metin; görsel, emoji, kalın yazı yok. Kısa paragraflar.
- Sıra: (1) bu haftanın görevi ve ölçülen süreler, iki cümle; (2) "Prompt:" başlığı ve prompt'un tam metni; (3) "Takıldığı yer:" tek cümle; (4) video bağlantısı; (5) kapanış sorusu: "Bu e-postayı yanıtla: senin işinde en çok vakit alan iş hangisi?"
- Verdiğim ölçümlerin dışında sayı, sonuç ya da deneyim ekleme. Benim adıma görüş yazma.
- "Sen" hitabı; abartı, sahte aciliyet ("son şans", "kaçırma") ve satış dili yok.
- Listeden çıkma satırı yazma; onu gönderim aracı ekler.

İSTEDİĞİM ÇIKTI:
1. Üç konu satırı seçeneği: görev + ölçülen süre; videonun başlığının kopyası olmasın; tamamı büyük harf ve ünlem yok.
2. E-postanın gövdesi, yukarıdaki sırayla.
3. Gövdede prompt metnini değiştirdiysen ya da kısalttıysan bunu açıkça söyle.
```

---

## Değişiklik günlüğü

Bir prompt'u değiştirdiğinde buraya yaz; hangi videoda neden değiştiği üç ay sonra hatırlanmaz.

| Tarih | Prompt | Ne değişti | Neden (hangi videoda ne oldu) |
|-------|--------|-----------|-------------------------------|
| 2026-11-16 | P3, P6, P8, P10 | P3: ilk cümle 12 kelime ve "ölçülecek şey"; P6: kapakta çift dışında en fazla 2 kelimelik tek etiket; P8: tür adları ve 10 kelimelik açılış; P10: "gösterim tıklama oranı (CTR)" | Yayın öncesi belge tutarlılığı: sınırlar 01 belgesi 3.2, 4.3 ve 4.4 ile eşitlendi (video yok) |
| | | | |
