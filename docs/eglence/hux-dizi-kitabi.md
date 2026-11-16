# HUX — Dizi Kitabı (Bal Porsuğu)

İngilizce, yatay (16:9), **bölüm başı yaklaşık 15 dakika**, stilize 3D çizgi film. Bu dosya dizinin anayasasıdır: ton, karakterler, tasarım, sezon planı ve 1. bölümün iskeleti burada. Yeni oturumda bu dosyayı göstererek devam edebilirsin.

**Tek cümle:** Her işe kafa üstü dalan, inatçı ama altın kalpli bir bal porsuğu olan Hux, ormanla çayırın buluştuğu küçük bir vadide arkadaşlarıyla birlikte bal peşinde koşar, başını belaya sokar ve her seferinde bir arkadaşlığı biraz daha büyütür.

**Neden bal porsuğu:** Gerçekte korkusuz, inatçı, bala düşkün ve "bal kılavuzu" kuşuyla ortak çalışan bir hayvan. Bu özellikler kavga için değil, komedi için kullanılıyor: Hux'un korkusuzluğu onu hep tuhaf durumlara sokar, arkadaşları da onu kurtarır.

---

## 1. Ton kuralları

Dizi **eğlenceli ve dostane**; saldırgan değil. Her bölüm yazılırken bu kurallar geçerli:

- **Kimse kimseye saldırmaz, kimse yaralanmaz.** Kovalamaca, düşme, çamura batma gibi zararsız fiziksel komedi var; ısırma, pençe, kan, dövüş yok.
- **Kötü karakter yok.** Rekabet var (en çok balı kim bulacak?), ama rakipler hep arkadaş.
- **Sorunlar birlikte çözülür.** Her bölümün sonunda biri bir şey öğrenir ya da bir arkadaşlık güçlenir.
- **Mizah karakterden gelir:** Hux'un inadı, Pip'in gevezeliği, Bruno'nun uykuculuğu, Dot'un kuralları, Willow'un utangaçlığı, Sylvia'nın dedikodusu.
- **Dişler ve pençeler öne çıkmaz.** Tasarımlarda keskin diş gösterilmez; kurt ve ayı yumuşak, sevimli çizilir.
- Her yaştan izleyiciye uygun; ama çocuklara özel ("Made for Kids") değil, aileyle izlenen bir çizgi film tonu.

---

## 2. Görsel stil

Karikatür: büyük kafalar, abartılı ifadeler, kısa bacaklar, iri gözler. Dokular gerçekçi (kürk, yaprak, ışık). Tamamen bize özel tasarım; var olan bir filmin karakterine benzemesin.

Her sahne prompt'unun başına eklenecek **stil bloğu** (`[STYLE]`):

```
Cinematic 16:9. Stylized 3D animated feature-film look: cute caricatured animals with oversized heads, big friendly expressive eyes, exaggerated poses and expressions, short stubby limbs, no sharp teeth shown; realistic soft fur texture and warm light. Setting: a sunny valley where a pine forest meets a wildflower meadow, a small stream and pond, a giant old hollow oak tree with a beehive. Animals walk on four legs and talk; no clothes. Cheerful, friendly mood. Shallow depth of field, smooth camera. No subtitles, no on-screen text, no music.
```

**Karikatürleri ben mi çıkaracağım?** Görseli ben üretemiyorum. Ben her karakterin tasarımını, kişiliğini ve **model sayfası prompt'unu** yazıyorum (aşağıda). Sen bunları Gemini görsel modeline (Nano Banana) ya da Midjourney'e verirsin, her karakter için 4–8 sürüm çıkar, beğendiğini seçersin; o görsel artık "resmî model" olur ve bütün dizi boyunca her sahneye referans olarak yüklenir. Seçilen görseller `docs/eglence/hux-modeller/` klasörüne konursa sonraki oturumlarda ben de görebilirim.

---

## 3. Karakterler

Kadro bilerek küçük: 6 ana karakter. Yapay zekâ videoda bir sahnede ne kadar az karakter olursa tutarlılık o kadar iyi kalır.

| Karakter | Hayvan | Kişilik | Ses tarifi (her prompt'ta aynen) |
|---|---|---|---|
| **Hux** (ana kahraman) | Bal porsuğu | Korkusuz, inatçı, plan yapmaz, önce dalar sonra düşünür. Kaba görünür ama arkadaşları için her şeyi yapar. Yalnız kalmaktan korkar, bunu asla söylemez. | `a gravelly, low, unbothered male voice, slow and confident` |
| **Pip** | Bal kılavuzu kuşu (küçük kahverengi kuş) | Hux'un ortağı. Durmadan konuşan, planlı, biraz korkak bir "fikir adamı". Kovanları o bulur, işi Hux'a yaptırır. | `a fast, chirpy, high male voice, always talking` |
| **Bruno** | Boz ayı | Kocaman, yumuşak kalpli, uykucu. Bal konusunda Hux'un dostça rakibi: ikisi de aynı kovanın peşinde. Yavaş konuşur, en komik anda uyuyakalır. | `a deep, slow, warm, sleepy male voice` |
| **Willow** | Kurt (genç dişi) | Utangaç, nazik, çok iyi kalpli. Uluyamıyor; denediğinde komik bir hıçkırık çıkıyor. Seyircinin gözü ve grubun kalbi. | `a soft, gentle, shy young female voice` |
| **Officer Dot** | Mirket | Vadinin kendini atamış güvenlik görevlisi. Kurallara aşık, sürekli dikilip etrafı kolaçan eder. Hux onun bitmeyen dosyası, ama gizlice onu sever. | `a crisp, bossy, fast female voice` |
| **Sylvia** | Yılan (kobra) | Vadinin dedikoducusu. Zarif, alaycı, her şeyi bilir; kimseye zararı yok, sadece hikâye yaymayı sever. Hux'u eğlenceli bulur. | `a silky, slow, amused female voice with a slight hiss` |

Tekrarlayan yan unsur: **Queen Beatrix ve kovanı** (yaşlı meşe ağacındaki arılar). Konuşmaz; tek bir büyük arı olarak kaşlarıyla ve vızıltısıyla oynar. Bal maceralarının karşı tarafı, ama her bölüm sonunda bir anlaşmaya varılır.

### Model sayfası prompt'ları

Her karakter için önce bu prompt'la tasarımı seç, sonra aynı görseli yükleyip "ifade sayfası" iste (aşağıda).

```
HUX: Character model sheet of an original cute caricatured honey badger. Stocky low body, oversized round head, black fur with a thick silver-white stripe from the top of the head down the back, small round ears, a small notch in the left ear, half-lidded confident eyes, a lopsided friendly grin with no sharp teeth, big digging claws. Front view, side view, three-quarter view, back view on a plain light grey background. Stylized 3D animated feature-film look, realistic soft fur texture, 16:9.
```

```
PIP: Character model sheet of an original cute caricatured honeyguide bird. Tiny round brown body, pale chest, oversized head, huge shiny eyes, short pink beak, one feather sticking up on the head like a cowlick, restless energetic posture. Front, side, three-quarter and in-flight views on a plain light grey background. Stylized 3D animated feature-film look, 16:9.
```

```
BRUNO: Character model sheet of an original cute caricatured brown bear. Huge round soft body, big round belly, small round ears, oversized head, sleepy half-closed gentle eyes, a little honey smudge on his snout, calm sweet smile with no teeth visible, big soft paws. Front, side, three-quarter, back and sitting views on a plain light grey background. Stylized 3D animated feature-film look, realistic soft fur texture, 16:9.
```

```
WILLOW: Character model sheet of an original cute caricatured young grey wolf. Slim lanky body, oversized fluffy head, very big soft ears, huge gentle shy eyes, small black nose, fluffy cream-coloured chest, bushy tail often tucked shyly, no sharp teeth shown. Front, side, three-quarter, back and sitting views on a plain light grey background. Stylized 3D animated feature-film look, realistic soft fur texture, 16:9.
```

```
DOT: Character model sheet of an original cute caricatured meerkat. Very upright posture, thin body, oversized head, dark eye patches, alert wide eyes, a small twig held in her mouth like a whistle, tiny chest puffed out proudly. Standing upright front, side, three-quarter, and on-all-fours views on a plain light grey background. Stylized 3D animated feature-film look, 16:9.
```

```
SYLVIA: Character model sheet of an original cute caricatured cobra. Elegant slim olive-green body, small rounded hood with a subtle pale pattern, heavy-lidded amused eyes with long lashes, friendly smirk, no fangs visible. Coiled, raised and sliding poses on a plain light grey background. Stylized 3D animated feature-film look, 16:9.
```

İfade sayfası (her karakter için, seçilen model görseli yüklenerek):

```
Same character as the reference image. Expression sheet: neutral, happy, laughing, surprised, embarrassed, sad, determined, sleeping. Plain light grey background, same style, 16:9.
```

Mekân referansları:

```
THE VALLEY: Wide establishing shot of a sunny valley where a pine forest meets a wildflower meadow, a small clear stream flowing into a pond, a giant old hollow oak tree with a huge beehive hanging from a branch, a mossy flat rock by the pond, a small hill with a lookout stump on top. Golden morning light, cheerful mood. Stylized 3D animated feature-film look, 16:9.
```

```
HUX'S BURROW: Inside a cosy underground burrow under the roots of a pine tree, roots hanging from the ceiling, a small pile of honeycomb in the corner, a bed of dry grass and leaves, warm light falling through the round entrance. Stylized 3D animated feature-film look, 16:9.
```

---

## 4. Kaç sezon, kaç bölüm?

| | Bölüm | Süre | Ne zaman |
|---|---|---|---|
| **Sezon 1 — "Dry Summer"** | **6 bölüm** | her biri ~15 dk (toplam ~90 dk) | İki haftada bir bölüm → yaklaşık 3 ay |
| Sezon 2 — "Autumn Leaves" | 6 bölüm | ~15 dk | Sezon 1 tutarsa |
| Sezon 3 — "First Snow" | 6 bölüm | ~15 dk | Sezon 2 tutarsa |

İlk taahhüt yalnızca **Sezon 1**. Sezon 2 ve 3 kısa bir yön olarak duruyor; 1. sezonun izlenme verisine göre (en çok tutan karakter, en çok izlenen bölüm) yazılacak.

### Sezon 1 — "Dry Summer"

Sezonun omurgası: Sıcak bir yaz; vadinin göleti her bölüm biraz daha küçülüyor. Her bölüm kendi içinde tamamlanır; finalde gölet kurur ve herkes birlikte çalışır.

| # | Bölüm | Hikâye |
|---|---|---|
| 1 | **The Sweetest Heist** | Pip, Hux'u yaşlı meşedeki dev kovana götürür; ama Bruno da aynı kovanın peşindedir. İki bal düşkünü yarışırken kovan dalından kopar ve vadinin her yerine bal saçılır. Arılar kızgın, Dot sinirli; Hux, Bruno ve Pip ortalığı birlikte toplar ve kraliçe arıyla ilk "bal anlaşmasını" yapar. |
| 2 | **The Big Sleep** | Hux bir oturuşta bir kovan dolusu bal yer ve iki gün uyur. Arkadaşları onun vadiden sonsuza dek gittiğini sanıp bir "veda töreni" düzenler; Hux tam herkes onun hakkında güzel şeyler söylerken uyanır ve arkadaşlarının onu ne kadar sevdiğini duyar. |
| 3 | **Deputy Hux** | Officer Dot, Hux'u "terbiye etmek" için yardımcı görevli yapar. Hux kuralları harfiyen uygular: Bruno'ya "izinsiz uyuma" cezası bile keser. Vadi birkaç saat içinde birbirine girer; Dot kuralların arkadaşlık için var olduğunu öğrenir. |
| 4 | **Stuck Together** | Hux ve Bruno, kimin daha iyi bal bulduğunu kanıtlamak için yarışırken aynı çukura düşer ve gece boyunca orada kalırlar. Rekabetin altından gerçek bir dostluk çıkar; sabah onları Willow'un burnu bulur. |
| 5 | **Willow's Howl** | Dolunay gecesi bütün kurtlar uluyacak; Willow uluyamıyor. Hux ona "ulumayı" öğretmeye kalkar, sonuç felaket ve çok komik. Sonunda Willow uluma yerine kendine özgü bir şarkı söyler ve bütün vadi ona eşlik eder. |
| 6 | **Dry Summer** (sezon finali) | Gölet tamamen kurur. Hux'un tek bildiği şey kazmak. Bütün kadro (kovan dahil) ilk kez birlikte çalışır; Sylvia'nın dedikoduları yeraltındaki bir kaynağın yerini ele verir, Bruno ağır taşları taşır, Hux kazar, su fışkırır. Son sahnede ilk yağmur damlası düşer. |

**Sezon 2 — "Autumn Leaves" (yön):** Kış hazırlığı. Bruno kış uykusuna yatmadan önce arkadaşlarıyla "son büyük macera"yı yapmak ister. Vadiye yeni, yalnız bir karakter taşınır (örneğin bir kirpi) ve grup onu aralarına alır.

**Sezon 3 — "First Snow" (yön):** İlk kar. Bruno uyuyor, grup onu uyandırmadan kışı geçirmeye çalışıyor; Hux karı ilk kez görüyor.

---

## 5. 15 dakikalık bölümün yapısı

Her bölüm aynı iskeleti kullanır; izleyici ritmi tanır ama hikâye hep yenidir.

| Bölüm parçası | Süre | Ne olur |
|---|---|---|
| Soğuk açılış | 0:00–1:00 | Bölümün sorusunu açan komik bir an. Selamlama yok. |
| Kısa jenerik | 1:00–1:15 | 15 saniyelik logo + tema müziği (her bölümde aynı). |
| 1. perde | 1:15–5:00 | Sorun ortaya çıkar, Hux'un kötü planı. |
| 2. perde | 5:00–11:00 | Plan çöker, işler büyür; ortada beklenmedik bir dönüş (~8:00). |
| 3. perde | 11:00–14:00 | Arkadaşlar birlikte çözer; biri bir şey öğrenir (ama Hux pek değişmez). |
| Kapanış şakası | 14:00–15:00 | Bölümün ilk espirisine geri dönen kısa, sıcak bir son. |

---

## 6. Bölüm 1 — "The Sweetest Heist" (iskelet)

Bu sekans listesi senaryonun omurgasıdır; sahne sahne Veo prompt'ları bir sonraki adımda bu listeden yazılacak (15 dakika ≈ 110 sahne).

| Zaman | Sekans | Ne olur |
|---|---|---|
| 0:00 | Soğuk açılış | Şafak. Pip, Hux'un yuvasının girişinde zıplayıp onu uyandırmaya çalışır; Hux uykusunda homurdanarak reddeder. Pip "honey" kelimesini fısıldar, Hux'un tek gözü açılır. |
| 1:00 | Jenerik | HUX logosu, tema müziği. |
| 1:15 | Vadi | Dünya tanıtımı: Officer Dot gölet başında sıra düzeni kurar, Willow suya bakıp kendi yansımasından utanır, Sylvia yeni dedikoduyu yayar, Bruno bir kayanın üstünde horlar. Gölet geçen yaza göre küçük (sezon omurgası). |
| 3:00 | Plan | Pip planını anlatır (kurgu: Pip'in hayal ettiği kusursuz soygun, gösterişli). Hux'un planı tek kelime: "Climb." |
| 4:00 | Rakip | Ağacın dibine vardıklarında Bruno'yu orada bulurlar; o da aynı kovanın peşindedir. "Ben önce gördüm" tartışması: yarış başlar. |
| 5:00 | Tırmanış yarışı | Hux tırmanır, Bruno ağacı sallayarak balı düşürmeye çalışır, Pip ikisine de yol gösterir. Queen Beatrix ilk kez görünür ve kaşını kaldırır. |
| 7:00 | Arılar | Arılar vızıldayarak kovalar; Hux umursamaz, Bruno gölete atlayıp saklanır, Pip Willow'un kabarık tüylerine dalar. Willow'un utangaç kahkahası ilk kez duyulur. |
| 8:00 | Dönüş | Hux kovanı çekerken dal kırılır; kovan aşağı yuvarlanır ve vadinin her yerine bal saçılır. Dot'un gözetleme kütüğü balın içinde kalır. |
| 9:00 | Yapış yapış vadi | Herkes bala yapışır: Bruno'nun pençeleri yere, Dot'un düdüğü ağzına, Sylvia kendi kuyruğuna. Kahkahalı bir kaos. |
| 11:00 | Dot'un toplantısı | Dot acil durum toplantısı yapar; suç Hux'a atılır. Sylvia herkesin gizlice bal yaladığını ortaya döker; herkes suçlu çıkar. |
| 12:30 | Çözüm | Hux, Bruno ve Pip birlikte kovanı ağaca geri taşır. Queen Beatrix ile "bal anlaşması" yapılır: her hafta biraz bal, karşılığında Hux kovanı korur. Hux balı herkesle paylaşır. |
| 14:00 | Kapanış | Gün batımı. Hux ve Bruno sırt sırta oturmuş, tıka basa doymuş; Bruno uyuyakalır. Pip gelir: "Big news. Bigger hive." Hux'un tek gözü açılır. Karartma. |

**İlk espirinin geri dönüşü:** Açılış ve kapanış aynı kadraj (Hux'un tek gözünün açılması).

---

## 7. Üretim gerçekleri (15 dakika ne demek?)

| | Tahmin |
|---|---|
| Sahne sayısı | 15 dk ≈ 110 klip (8 saniyelik) |
| Toplam üretim | Denemelerle 250–350 video üretimi |
| Diyalog satırı | 150–200 replik |
| Süre (tek kişi) | Bölüm başına 2–3 hafta |
| Maliyet | Video kredisi en büyük kalem; abonelik planının aylık üretim sınırını bölüm başı 300 üretime göre kontrol et |

**Ses için yol (uzun bölümde şart):** 15 dakikada karakter sesinin klipten klibe değişmesi kabul edilemez. Bu yüzden:

1. Önce bütün diyaloğu ElevenLabs'te her karakterin sabit sesiyle üret (bir "radyo tiyatrosu" kaydı gibi).
2. Bu ses kaydını kurguda zaman çizelgesine koy; bölümün ritmi buradan çıkar.
3. Görüntü kliplerini üret; konuşan sahnelerde dudak eşlemeyi sesle yap (Kling ya da Hedra'nın ses dosyasıyla dudak eşleme özelliği). Veo'yu konuşmasız sahneler ve hareket için kullan.

| İş | Araç |
|---|---|
| Karakter modelleri, mekânlar | Gemini görsel modeli (Nano Banana) ya da Midjourney |
| Konuşmasız sahneler, hareket | Google Veo, görselden videoya |
| Konuşan sahneler | Kling ya da Hedra, ses dosyasıyla dudak eşleme |
| Sesler | ElevenLabs (6 sabit ses) |
| Tema müziği ve sahne müzikleri | Suno |
| Kurgu | DaVinci Resolve (15 dakikalık projede CapCut'tan daha rahat) ya da CapCut |
| Senaryo ve sahne prompt'ları | Claude Opus 5.5 |

**Tanıtım:** Ana ürün 15 dakikalık bölüm. Her bölümden 2–3 kısa sahne Shorts olarak "bölümün tamamı kanalda" diye yayınlanabilir; amaç izleyiciyi uzun bölüme taşımak.

---

## 8. Sıradaki adımlar

1. Bölüm 3'teki 6 model sayfası ve 2 mekân prompt'unu üret, her karakter için en iyisini seç ve ifade sayfasını çıkar.
2. Seçilen görselleri `docs/eglence/hux-modeller/` klasörüne koy.
3. Bölüm 1'in tam senaryosunu (bütün replikler) ve sahne sahne prompt'larını yazdır.
4. Önce yalnızca soğuk açılışı (ilk 1 dakika, ~8 sahne) üret; karakterler tutarlı ve komik çıkıyorsa bölümün kalanına geç.

---

## Verdiğim kararlar

- **Domuz (Gus) çıkarıldı; kurt (Willow) ve ayı (Bruno) eklendi.** Gus'un "grubun kalbi" rolü Willow'a geçti.
- **Aslan (Barnaby) çıkarıldı.** Ayı geldiği için kadro 6'da kaldı; aslanın "kibirli rakip" rolü yerine Bruno'nun dostça bal rekabeti geldi. Bu dostane tona daha uygun.
- **Mekân savandan orman–çayır vadisine taşındı.** Kurt ve ayı savanda yaşamaz; çizgi film dünyasında mirket ve kobra bu vadide sorun yaratmaz, ama kurt ve ayının savanda olması göze batardı.
- **Kobra artık ısırmıyor.** Eski 2. bölüm ("Snakebite") yerine "The Big Sleep" yazıldı: aynı veda töreni esprisi, ama Hux fazla bal yediği için uyuyor. Sylvia artık zararsız bir dedikoducu.
- **Ton kuralları eklendi** (bölüm 1): saldırı, yaralanma, kötü karakter yok; dişler ve pençeler öne çıkmıyor; her bölüm arkadaşlıkla bitiyor.
- **Willow dişi yazıldı.** Kadroda 3 erkek, 3 dişi karakter dengesi için.
- **Sezon adları vadiye uyarlandı:** "Dry Summer", "Autumn Leaves", "First Snow". Mevsimler hem görsel çeşitlilik hem doğal bir sezon omurgası veriyor (Bruno'nun kış uykusu 3. sezonun konusu).
- **Dil İngilizce.** Hayvan komedisi dünya çapında izlenir; Türkçe dublaj sonradan ElevenLabs ile eklenebilir (YouTube çok dilli ses kanalı destekliyor).
- **Sezon 1 = 6 bölüm.** 15 dakikalık bölümün yapımı tek kişiyle 2–3 hafta sürüyor; 6 bölüm yaklaşık 3 ayda bitiyor ve izleyici verisi toplamak için yeterli.
- **Konuşan sahnelerde ses önce, görüntü sonra.** 15 dakikalık bölümde karakter sesinin değişmesi diziyi bozar.
- **Karakterler özgün tasarım.** Her birine ayırt edici bir özellik verildi (Hux'un çentikli kulağı, Bruno'nun burnundaki bal lekesi, Willow'un dev kulakları, Dot'un dal düdüğü vb.).
- **"Honey badger don't care" internet esprisi kullanılmadı.** Başkasına ait ünlü bir videonun cümlesi.
