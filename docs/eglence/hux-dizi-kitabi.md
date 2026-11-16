# HUX — Dizi Kitabı (Bal Porsuğu)

İngilizce, yatay (16:9), **bölüm başı yaklaşık 15 dakika**, stilize 3D çizgi film. Bu dosya dizinin anayasasıdır: karakterler, tasarım, sezon planı ve 1. bölümün iskeleti burada. Yeni oturumda bu dosyayı göstererek devam edebilirsin.

**Tek cümle:** Korku nedir bilmeyen, inatçı ve her işe kafa üstü dalan bir bal porsuğu olan Hux, kuraklıkla boğuşan küçük bir savan su başı topluluğunda hem başbelası hem de herkesin gizlice güvendiği kahramandır.

**Neden bal porsuğu:** Gerçek hayatta aslanlara kafa tutan, kobra zehrine dayanıklı, arı sokmasını umursamayan ve "bal kılavuzu" kuşuyla ortaklık kuran bir hayvan. Bu gerçeklerin her biri hazır bir bölüm fikri; izleyici "bu doğru mu?" diye merak edip araştırır, yorum yazar.

---

## 1. Görsel stil

Karikatür: büyük kafalar, abartılı ifadeler, kısa bacaklar, iri gözler. Ama dokular gerçekçi (kürk, toz, ışık). Tamamen bize özel tasarım; var olan bir filmin karakterine benzemesin.

Her sahne prompt'unun başına eklenecek **stil bloğu** (`[STYLE]`):

```
Cinematic 16:9. Stylized 3D animated feature-film look: caricatured animals with oversized heads, big expressive eyes, exaggerated poses and expressions, short stubby limbs; realistic fur texture, dust and warm light. Setting: a dry African savanna around a small muddy watering hole, a giant baobab tree, red earth, golden-hour light. Animals walk on four legs and talk; no clothes. Shallow depth of field, smooth camera. No subtitles, no on-screen text, no music.
```

**Karikatürleri ben mi çıkaracağım?** Görseli ben üretemiyorum. Ben her karakterin tasarımını, kişiliğini ve **model sayfası prompt'unu** yazıyorum (aşağıda). Sen bunları Gemini görsel modeline (Nano Banana) ya da Midjourney'e verirsin, her karakter için 4–8 sürüm çıkar, beğendiğini seçersin; o görsel artık "resmî model" olur ve bütün dizi boyunca her sahneye referans olarak yüklenir. Seçilen görseller `docs/eglence/hux-modeller/` klasörüne konursa sonraki oturumlarda ben de görebilirim.

---

## 2. Karakterler

Kadro bilerek küçük: 6 ana karakter. Yapay zekâ videoda bir sahnede ne kadar az karakter olursa tutarlılık o kadar iyi kalır.

| Karakter | Hayvan | Kişilik | Ses tarifi (her prompt'ta aynen) |
|---|---|---|---|
| **Hux** (ana kahraman) | Bal porsuğu | Korkusuz, inatçı, kibar değil ama adil; plan yapmaz, kapıyı kırar. Altında: yalnız kalmaktan korkar, bunu asla söylemez. | `a gravelly, low, unbothered male voice, slow and confident` |
| **Pip** | Bal kılavuzu kuşu (küçük kahverengi kuş) | Hux'un ortağı. Durmadan konuşan, planlı, korkak bir dolandırıcı. Arı kovanlarını o bulur, işi Hux'a yaptırır. | `a fast, chirpy, high male voice, always talking` |
| **King Barnaby** | Aslan | Kibirli, kendini kral ilan etmiş, yelesine düşkün. Hux'tan gizlice ödü kopar. | `a booming, theatrical, pompous male voice` |
| **Sylvia** | Kobra | Zarif, alaycı, tehlikeli. Zehrinin Hux'a işlememesini kişisel hakaret sayar. Düşman mı dost mu, belli değil. | `a silky, slow, amused female voice with a slight hiss` |
| **Officer Dot** | Mirket | Su başının kendi kendini atamış güvenlik görevlisi. Kurallara aşık, sürekli dikilip etrafı kolaçan eder. Hux onun bitmeyen dosyası. | `a crisp, bossy, fast female voice` |
| **Gus** | Yaban domuzu | Hux'un en yakın arkadaşı. Her şeyden korkar, çok iyi kalplidir, ağlak. Seyircinin gözü. | `a soft, wobbly, nervous male voice` |

Tekrarlayan yan unsur: **Queen Beatrix ve kovanı** (baobab ağacındaki arılar). Konuşmaz; tek bir büyük arı olarak kaşlarıyla ve vızıltısıyla oynar. Her bal soygununun karşı tarafı.

### Model sayfası prompt'ları

Her karakter için önce bu prompt'la tasarımı seç, sonra aynı görseli yükleyip "ifade sayfası" iste (aşağıdaki ikinci satır).

```
HUX: Character model sheet of an original caricatured honey badger. Stocky low body, oversized head, black fur with a thick silver-white stripe from the top of the head down the back, small round ears, a scar notch in the left ear, narrow half-lidded unimpressed eyes, a slightly crooked confident grin showing one tooth, big digging claws. Front view, side view, three-quarter view, back view on a plain light grey background. Stylized 3D animated feature-film look, realistic fur texture, 16:9.
```

```
PIP: Character model sheet of an original caricatured honeyguide bird. Tiny round brown body, pale chest, oversized head, huge shiny eyes, short pink beak, one feather sticking up on the head like a cowlick, restless energetic posture. Front, side, three-quarter and in-flight views on a plain light grey background. Stylized 3D animated feature-film look, 16:9.
```

```
BARNABY: Character model sheet of an original caricatured male lion. Skinny body with an enormous, perfectly groomed golden mane that is clearly too big for him, long chin, raised nose, half-closed proud eyes. Front, side, three-quarter and back views on a plain light grey background. Stylized 3D animated feature-film look, realistic fur texture, 16:9.
```

```
SYLVIA: Character model sheet of an original caricatured cobra. Elegant slim olive-brown body, wide hood with a subtle pale pattern, heavy-lidded amused eyes with long lashes, small smirk. Coiled, raised-hood and sliding poses on a plain light grey background. Stylized 3D animated feature-film look, 16:9.
```

```
DOT: Character model sheet of an original caricatured meerkat. Very upright posture, thin body, oversized head, dark eye patches, alert wide eyes, one twig held in her mouth like a whistle, tiny chest puffed out. Standing upright front, side, three-quarter, and on-all-fours views on a plain light grey background. Stylized 3D animated feature-film look, 16:9.
```

```
GUS: Character model sheet of an original caricatured warthog. Round heavy body, short legs, oversized head, small curved tusks, big watery worried eyes, tuft of mane on the head, tail that sticks straight up when scared. Front, side, three-quarter and back views on a plain light grey background. Stylized 3D animated feature-film look, 16:9.
```

İfade sayfası (her karakter için, seçilen model görseli yüklenerek):

```
Same character as the reference image. Expression sheet: neutral, angry, scared, laughing, smug, sad, surprised, sleeping. Plain light grey background, same style, 16:9.
```

Mekân referansları:

```
WATERING HOLE: Wide establishing shot of a small muddy watering hole in a dry African savanna, cracked red earth around it, a giant baobab tree with a huge beehive hanging from a branch, a low rocky outcrop with a flat top (the lion's "throne rock"), a termite mound, scattered acacia trees, golden-hour light. Stylized 3D animated feature-film look, 16:9.
```

```
HUX'S BURROW: Inside a cosy underground burrow dug into red earth, roots hanging from the ceiling, a pile of stolen honeycomb in the corner, a bed of dry grass, light falling through the entrance. Stylized 3D animated feature-film look, 16:9.
```

---

## 3. Kaç sezon, kaç bölüm?

| | Bölüm | Süre | Ne zaman |
|---|---|---|---|
| **Sezon 1 — "Dry Season"** | **6 bölüm** | her biri ~15 dk (toplam ~90 dk) | İki haftada bir bölüm → yaklaşık 3 ay |
| Sezon 2 — "The Rains" | 6 bölüm | ~15 dk | Sezon 1 tutarsa |
| Sezon 3 — "The Crossing" | 6 bölüm | ~15 dk | Sezon 2 tutarsa |

İlk taahhüt yalnızca **Sezon 1**. Sezon 2 ve 3 kısa bir yön olarak duruyor; 1. sezonun izlenme verisine göre (en çok tutan karakter, en çok izlenen bölüm) yazılacak.

### Sezon 1 — "Dry Season"

Sezonun omurgası: Kurak mevsim geliyor, su başı her bölüm biraz daha küçülüyor. Her bölüm kendi içinde tamamlanır; finalde su biter ve herkes Hux'a muhtaç kalır.

| # | Bölüm | Hikâye |
|---|---|---|
| 1 | **The Sweetest Heist** | Pip, Hux'u baobabın tepesindeki dev kovana götürür. Soygun felaketle biter: Hux yüzlerce arı sokmasını umursamaz ama kovan düşer, King Barnaby'nin "taht kayasına" bal yağar. Herkes tanışır; Hux su başının bir numaralı başbelası ilan edilir. |
| 2 | **Snakebite** | Sylvia, Hux'u ısırır. Hux bayılır (gerçek: bal porsukları kobra ısırığından sonra bir süre baygın kalıp uyanabilir). Herkes onu öldü sanıp cenaze töreni yapar; Hux tam veda konuşmaları sırasında uyanır ve herkesin onun hakkında gerçekte ne düşündüğünü duyar. |
| 3 | **Deputy Hux** | Officer Dot, Hux'u "ıslah etmek" için yardımcı görevli yapar. Hux kuralları harfiyen uygular: Barnaby'ye bile ceza keser. Su başı birkaç saat içinde karışır. |
| 4 | **The Lion's Share** | Barnaby küçülen suya vergi koyar. Hux karşı çıkar; ikisi kavga ederken bir çukura düşüp gece boyunca orada mahsur kalır. Barnaby'nin kibrinin altındaki yalnız aslan ortaya çıkar. |
| 5 | **Brave Gus** | Gus, Hux gibi korkusuz olmak ister. Hux ona "cesaret dersi" verir, işler kontrolden çıkar. Sonunda Hux'u bir tehlikeden kurtaran, korktuğu için dikkatli davranan Gus olur. |
| 6 | **Dry Season** (sezon finali) | Su başı tamamen kurur. Hux'un tek bildiği şey kazmak. Bütün kadro (Queen Beatrix'in kovanı dahil) ilk kez birlikte çalışır; Hux yeraltından suyu bulur. Son sahnede ilk yağmur damlası düşer → Sezon 2'ye köprü. |

**Sezon 2 — "The Rains" (yön):** Yağmurlar gelir, su başı göle döner; yeni ve tehlikeli bir komşu gelir (timsah). Hux ilk kez yenemeyeceği bir rakiple karşılaşır.

**Sezon 3 — "The Crossing" (yön):** Büyük göç sürüsü bölgeden geçer; Hux'un küçük topluluğu bir anda kalabalıklaşır, Barnaby tahtını kaybetme korkusu yaşar.

---

## 4. 15 dakikalık bölümün yapısı

Her bölüm aynı iskeleti kullanır; izleyici ritmi tanır ama hikâye hep yenidir.

| Bölüm parçası | Süre | Ne olur |
|---|---|---|
| Soğuk açılış | 0:00–1:00 | Bölümün sorusunu açan komik bir an. Jenerik yok, selamlama yok. |
| Kısa jenerik | 1:00–1:15 | 15 saniyelik logo + tema müziği (her bölümde aynı). |
| 1. perde | 1:15–5:00 | Sorun ortaya çıkar, Hux'un kötü planı. |
| 2. perde | 5:00–11:00 | Plan çöker, işler büyür; ortada beklenmedik bir dönüş (~8:00). |
| 3. perde | 11:00–14:00 | Doruk ve çözüm; bir karakter bir şey öğrenir (ama Hux pek değişmez). |
| Kapanış şakası | 14:00–15:00 | Bölümün ilk espirisine geri dönen kısa bir son. |

---

## 5. Bölüm 1 — "The Sweetest Heist" (iskelet)

Bu sekans listesi senaryonun omurgasıdır; sahne sahne Veo prompt'ları bir sonraki adımda bu listeden yazılacak (15 dakika ≈ 110 sahne).

| Zaman | Sekans | Ne olur |
|---|---|---|
| 0:00 | Soğuk açılış | Şafak. Pip kovanı gözetler, Hux'u uyandırmaya çalışır; Hux uyurken bile homurdanarak reddeder. Pip "bal" kelimesini söyler, Hux'un tek gözü açılır. |
| 1:00 | Jenerik | HUX logosu, tema müziği. |
| 1:15 | Su başı | Dünya tanıtımı: Officer Dot sıra düzeni kurar, Gus su içmeye korkar, Barnaby taht kayasından "kraliyet konuşması" yapar. Su başı geçen yıla göre küçük (sezon omurgası). |
| 3:00 | Plan | Pip planını anlatır (kurgu: Pip'in hayal ettiği kusursuz soygun). Hux'un planı tek kelime: "Climb." |
| 5:00 | Tırmanış | Hux baobaba tırmanır, Pip yönlendirir; Queen Beatrix ilk kez görünür ve kaşını kaldırır. |
| 6:30 | İlk saldırı | Arılar saldırır; Hux sokmaları umursamaz, Pip panikle kaçar. Gus aşağıdan izler, bayılır. |
| 8:00 | Dönüş | Hux kovanı çekerken dal kırılır; kovan Barnaby'nin taht kayasına düşer ve aslan balın içinde kalır. |
| 9:00 | Kaos | Arılar Barnaby'yi kovalar; bütün su başı birbirine girer; Officer Dot düdük çalar, kimse dinlemez. |
| 11:00 | Mahkeme | Barnaby "kraliyet mahkemesi" kurar; Sylvia jüri başkanı (eğlenerek). Hux suçlanır; Pip ortadan kaybolmuştur. |
| 12:30 | Çözüm | Gus titreyerek Hux'u savunur: Hux kimseye zarar vermedi, balı da paylaşacak. Hux istemeye istemeye balı herkese dağıtır. |
| 14:00 | Kapanış | Gece. Hux yuvasında sokmalardan şişmiş yüzüyle uzanır. Pip geri gelir: "Big news. Bigger hive." Hux'un tek gözü açılır. Karartma. |

**İlk espirinin geri dönüşü:** Açılış ve kapanış aynı kadraj (Hux'un tek gözünün açılması).

---

## 6. Üretim gerçekleri (15 dakika ne demek?)

| | Tahmin |
|---|---|
| Sahne sayısı | 15 dk ≈ 110 klip (8 saniyelik) |
| Toplam üretim | Denemelerle 250–350 video üretimi |
| Diyalog satırı | 150–200 replik |
| Süre (tek kişi) | Bölüm başına 2–3 hafta |
| Maliyet | Veo kredisi en büyük kalem; abonelik planının aylık üretim sınırını bölüm başı 300 üretime göre kontrol et |

**Ses için yol (uzun bölümde şart):** 15 dakikada Veo'nun her klipte farklı ses üretmesi kabul edilemez. Bu yüzden:

1. Önce bütün diyaloğu ElevenLabs'te her karakterin sabit sesiyle üret (bir "radyo tiyatrosu" kaydı gibi).
2. Bu ses kaydını kurguda zaman çizelgesine koy; bölümün ritmi buradan çıkar.
3. Görüntü kliplerini üret; konuşan sahnelerde dudak eşlemeyi sesle yap (Kling ya da Hedra'nın ses dosyasıyla dudak eşleme özelliği). Veo'yu konuşmasız sahneler ve hareket için kullan.

| İş | Araç |
|---|---|
| Karakter modelleri, mekânlar | Gemini görsel modeli (Nano Banana) ya da Midjourney |
| Konuşmasız sahneler, aksiyon | Google Veo, görselden videoya |
| Konuşan sahneler | Kling ya da Hedra, ses dosyasıyla dudak eşleme |
| Sesler | ElevenLabs (6 sabit ses) |
| Tema müziği ve sahne müzikleri | Suno |
| Kurgu | DaVinci Resolve (15 dakikalık projede CapCut'tan daha rahat) ya da CapCut |
| Senaryo ve sahne prompt'ları | Claude Opus 5.5 |

**Tanıtım:** Ana ürün 15 dakikalık bölüm. Her bölümden 2–3 kısa sahne Shorts olarak "bölümün tamamı kanalda" diye yayınlanabilir; amaç izleyiciyi uzun bölüme taşımak.

---

## 7. Sıradaki adımlar

1. Bölüm 2'deki 6 model sayfası ve 2 mekân prompt'unu üret, her karakter için en iyisini seç ve ifade sayfasını çıkar.
2. Seçilen görselleri `docs/eglence/hux-modeller/` klasörüne koy.
3. Bölüm 1'in tam senaryosunu (bütün replikler) ve sahne sahne prompt'larını yazdır.
4. Önce yalnızca soğuk açılışı (ilk 1 dakika, ~8 sahne) üret; karakterler tutarlı ve komik çıkıyorsa bölümün kalanına geç.

---

## Verdiğim kararlar

- **Dil İngilizce.** Meyve serisiyle aynı; hayvan komedisi dünya çapında izlenir ve İngilizce içerikte reklam geliri daha yüksektir. Türkçe dublaj sonradan ElevenLabs ile eklenebilir (YouTube çok dilli ses kanalı destekliyor).
- **Mekân Afrika savanı, bir su başı.** Bal porsuğunun gerçek yaşam alanı; tek bir merkez mekân üretimi kolaylaştırıyor ve kuraklık sezona doğal bir omurga veriyor.
- **6 ana karakter.** Bal porsuğunun gerçek doğasından çıkan rakipler ve ortaklar seçildi: aslan (meydan okuduğu), kobra (zehrine dayanıklı olduğu), bal kılavuzu kuşu (gerçek ortağı), arılar (soyduğu). Mirket ve yaban domuzu topluluğu ve kalbi temsil ediyor.
- **Sezon 1 = 6 bölüm.** 15 dakikalık bölümün yapımı tek kişiyle 2–3 hafta sürüyor; 6 bölüm yaklaşık 3 ayda bitiyor ve izleyici verisi toplamak için yeterli. 10–12 bölümlük bir sezon ilk denemede yarıda kalma riski taşır.
- **Sezon 2 ve 3 yalnızca yön olarak yazıldı.** Hangi karakterin tuttuğu belli olmadan ayrıntılandırmak boşa iş olur.
- **Konuşan sahnelerde ses önce, görüntü sonra.** 15 dakikalık bölümde karakter sesinin değişmesi diziyi bozar; bu nedenle meyve filmindeki "Veo'nun sesi + sonradan düzeltme" yolu yerine ses kaydı önce üretiliyor.
- **Karakterler özgün tasarım.** Var olan bir filme ya da maskota benzememeleri için her birine ayırt edici bir özellik verildi (Hux'un yırtık kulağı, Barnaby'nin vücuduna fazla büyük yelesi, Dot'un ağzındaki dal düdüğü vb.).
- **"Honey badger don't care" internet esprisi kullanılmadı.** Başkasına ait ünlü bir videonun cümlesi; Hux'un umursamazlığı kendi replikleriyle anlatılacak.
