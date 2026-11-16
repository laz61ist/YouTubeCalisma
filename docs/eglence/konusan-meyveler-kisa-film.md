# Kısa Film — "Best Before"

İngilizce, yatay (16:9), yaklaşık **3 dakika 45 saniye**: 8 saniyelik 28 sahne. Karakterler `konusan-meyveler-pilot.md` dosyasındakilerle aynı (Lenny, Bea, Avo). Bu dosya tek başına yeterlidir; yeni oturumda bu dosyayı göstererek devam edebilirsin.

**Tek cümle:** Bea yarın banana bread yapılacağını duyar; ondan hiç hoşlanmayan Lenny ve Avo onu ekmek kutusuna saklamak için tezgâhta gece operasyonuna girişir — ta ki o ekmeği kimin yapmak istediğini öğrenene kadar.

**Neden bu hikâye:** Dizideki esprilerin (lekeler, "promotion", "Classic") hepsi tek bir hikâyede, başı–ortası–sonu olan bir yolculuğa dönüşür. Komediyle başlar, duygusal bir dönüşle biter; izleyici sonuna kadar kalır. İnsanlar yalnızca el olarak ve ekran dışı ses olarak görünür, yani yapay zekânın en çok bozduğu insan yüzü hiç yoktur. Tek mekân: mutfak tezgâhı.

---

## 1. Hikâyenin iskeleti

| Bölüm | Süre | Ne olur |
|---|---|---|
| Giriş | 0:00–0:56 | Sabah. Bea'nın lekeleri çoğalmış; anne telefonda "bu akşam banana bread yapacağım" der. |
| Plan | 0:56–1:20 | Avo, Bea giderse sıranın kendisine geleceğini fark eder; üçü Bea'yı ekmek kutusuna saklamaya karar verir. |
| Operasyon | 1:20–2:00 | Kolsuz bacaksız üç meyve tezgâhın öbür ucuna yuvarlanır: su birikintisi, kupa almaya gelen el, kesme tahtası rampası. |
| Dönüş | 2:00–2:56 | Anne muzları bulamaz; küçük kız "Muzları ben ezecektim, söz vermiştin" der. Bea saklandığı yerden bunu duyar ve geri dönmeye karar verir. |
| Final | 2:56–3:44 | Kız Bea'yı bulur, annesiyle birlikte ekmeği yapar. Fırından bir dilim Lenny ve Avo'ya bırakılır. Kâseye yeni, yeşil muzlar gelir; biri ilk lekesini görüp panikler. |

---

## 2. Hangi iş hangi modelle

Model adları Haziran 2026'ya kadarki bilgiye dayanır; aracı açtığında en yeni sürümü seç.

| İş | Araç | Not |
|---|---|---|
| Referans görseller (3 karakter, mutfak, ekmek kutusu) | Gemini görsel modeli (Nano Banana) | Bölüm 3; her sahnede ilgili referansı yükle |
| Meyvelerin konuştuğu sahneler | Google Veo, görselden videoya, diyalog prompt'ta | Dudak hareketi için diyalog prompt'ta kalmalı |
| Meyve seslerini sabitlemek | ElevenLabs Voice Changer (sesten sese) | Veo'nun sesini aynı karakter sesine çevirir; zamanlama ve dudak uyumu korunur. 3–4 dakikalık filmde ses kayması belli olur, bu adımı atlama |
| Anne ve kızın sesi (ekran dışı) | ElevenLabs, metinden sese | Bölüm 5'teki satırlar; kurguda yerleştir |
| Konuşmasız sahneler | Veo ya da Kling, görselden videoya | Yalnızca ortam sesi iste |
| Müzik | Suno | Bölüm 6 |
| Kurgu, altyazı, renk eşitleme | CapCut (ya da DaVinci Resolve) | Sahneler arası ışık farkını renk ayarıyla eşitle |
| Senaryoda değişiklik | Claude Opus 5.5 | Küçük düzeltme için Sonnet 5.5 yeter |

---

## 3. Referans görseller (16:9)

Pilottaki dikey görseller bu film için kullanılmaz; yataya göre yeniden üret.

```
LENNY: A bright yellow lemon with half-closed, unimpressed cartoon eyes and a flat mouth, sitting in a white ceramic fruit bowl on a sunlit wooden kitchen counter, white tiled wall behind. Photorealistic 3D animation, Pixar-like, shallow depth of field, cinematic 16:9.
```

```
BEA: A very ripe yellow banana covered in many small brown spots, with wide worried cartoon eyes and a trembling mouth, leaning on the edge of a white ceramic fruit bowl on a sunlit wooden kitchen counter, white tiled wall behind. Photorealistic 3D animation, Pixar-like, shallow depth of field, cinematic 16:9.
```

```
AVO: A dark green whole avocado with one raised eyebrow, narrow confident cartoon eyes and a smirk, sitting on a small folded linen napkin next to a white ceramic fruit bowl on a sunlit wooden kitchen counter. Photorealistic 3D animation, Pixar-like, shallow depth of field, cinematic 16:9.
```

```
KITCHEN: A long sunlit wooden kitchen counter seen at fruit height. In the foreground a white ceramic fruit bowl; in the middle a knife block, a sink with a few water drops on the counter beside it, and a wooden cutting board; at the far end a closed wooden bread box. White tiled wall behind, an oven with a glass door below the far end. Warm, cosy family kitchen. Photorealistic 3D animation, Pixar-like, cinematic 16:9.
```

```
KITCHEN NIGHT: The same kitchen counter at night, lit only by the blue glow of a microwave clock and pale moonlight from a window. Fruit bowl in the foreground, wooden bread box at the far end. Photorealistic 3D animation, Pixar-like, cinematic 16:9.
```

Her sahne prompt'unun başına şu **stil bloğunu** ekle (`[STYLE]` yazan yere):

```
Cinematic 16:9. Photorealistic 3D animation, Pixar-like. Real-looking fruit with small expressive cartoon eyes and a mouth, no arms or legs; fruit move only by rolling, sliding or tilting. Setting: a wooden kitchen counter in a warm family kitchen, white tiled wall behind. Camera at fruit height, shallow depth of field, smooth camera movement. Humans appear only as hands and arms, faces never visible. No subtitles, no on-screen text, no music.
```

Ses tarifleri (her prompt'ta aynen):

- Lenny: `a dry, deadpan, low male voice`
- Bea: `a fast, high-pitched, anxious female voice`
- Avo: `a smooth, smug, posh male voice`

---

## 4. Sahne listesi

"Ses" sütunundaki ANNE ve KIZ satırları videoya ürettirilmez; ElevenLabs'te üretilip kurguda eklenir. "Veo" yazan sahnelerde meyve diyaloğu prompt'un içindedir.

| # | Zaman | Görüntü prompt'u | Ses |
|---|---|---|---|
| 1 | 0:00 | `[STYLE] Dawn. Slow push-in along the empty counter toward the fruit bowl as the first sunbeam crawls across the wood. Lenny the lemon, Bea the banana and Avo the avocado are asleep, eyes closed. Sound: birds outside, fridge hum.` | — |
| 2 | 0:08 | `[STYLE] Close-up of Bea the banana waking up. She looks down at her peel, now covered in many brown spots, and gasps. Bea says in a fast, high-pitched, anxious female voice: "No. No, no, no. Lenny. How many spots is too many?"` | Veo |
| 3 | 0:16 | `[STYLE] Close-up of Lenny the lemon in the bowl, eyes half-closed, not looking at her. Lenny says in a dry, deadpan, low male voice: "You're past counting. You're in the smell stage."` | Veo |
| 4 | 0:24 | `[STYLE] Close-up of Avo the avocado on his linen napkin, admiring himself in the reflection of a steel spoon. Avo says in a smooth, smug, posh male voice: "Some of us age like wine. Some of us age like... that."` | Veo |
| 5 | 0:32 | `[STYLE] The three fruits in the foreground, in focus. Behind them, out of focus, a woman's hand holds a phone to her ear and leans on the counter; only her arm and sweater are visible. The fruits slowly turn their eyes toward her. Sound: kitchen ambience.` | ANNE: "Tomorrow? The bake sale? ...No, it's fine. The bananas are basically gone. I'll make banana bread tonight, with Mia." |
| 6 | 0:40 | `[STYLE] Extreme close-up of Bea's face. Her pupils shrink to tiny dots. Slow dolly-in. Bea whispers in a fast, high-pitched, anxious female voice: "Banana... bread." Sound: the oven clicks on in the background.` | Veo |
| 7 | 0:48 | `[STYLE] Two-shot of Lenny and Bea. Lenny says in a dry, deadpan, low male voice: "Told you. Promotion." Bea says in a fast, high-pitched, anxious female voice: "I don't WANT a promotion!"` | Veo |
| 8 | 0:56 | `[STYLE] Bea turns from Lenny to Avo, eyes huge and pleading. Bea says in a fast, high-pitched, anxious female voice: "Hide me. Please. I'll be quiet. I'll be so quiet."` | Veo |
| 9 | 1:04 | `[STYLE] Two-shot of Avo and Lenny. Avo says in a smooth, smug, posh male voice: "Absolutely not. Let nature take its course." Lenny says in a dry, deadpan, low male voice: "If she's gone, they bake the next ripest thing." Avo slowly looks down at his own darkening skin. Avo says: "...We're hiding her."` | Veo |
| 10 | 1:12 | `[STYLE] Over-the-shoulder shot from behind Lenny, looking down the long counter: knife block, wet sink area, cutting board, and the wooden bread box at the far end, far away. Lenny says in a dry, deadpan, low male voice: "Bread box. Nobody looks for a banana among bread."` | Veo |
| 11 | 1:20 | `[STYLE] Low tracking shot alongside the three fruits rolling down the counter in a line, in warm afternoon light. Lenny rolls smoothly, Avo rolls heavily, Bea flops end over end. Sound: rolling on wood, small grunts.` | Müzik başlar (macera) |
| 12 | 1:28 | `[STYLE] Near the sink, Bea slides on a small puddle of water and spins in a full circle. Bea says in a fast, high-pitched, anxious female voice: "I'm bruising! I'm bruising!" Sound: a wet squeak.` | Veo |
| 13 | 1:36 | `[STYLE] A human hand suddenly reaches into frame for a coffee mug right next to the fruits. All three freeze mid-roll, eyes shut, perfectly still. The hand takes the mug and leaves. Avo whispers in a smooth, smug, posh male voice: "Nobody. Breathe."` | Müzik durur, sonra devam |
| 14 | 1:44 | `[STYLE] Avo pushes Bea up the slope of a tilted wooden cutting board toward the open bread box, straining. Avo says in a smooth, smug, posh male voice: "This is the most exercise... of my entire life."` | Veo |
| 15 | 1:52 | `[STYLE] Lenny nudges the bread box lid open. Bea slides inside next to a loaf of bread. Bea says in a fast, high-pitched, anxious female voice: "It's dark. It smells like my future." Lenny says in a dry, deadpan, low male voice: "Don't." The lid closes. Sound: a wooden lid closing.` | Veo · Müzik biter |
| 16 | 2:00 | `[STYLE] Evening, warm lamp light. A woman's hands search the fruit bowl and lift Avo and Lenny, looking under them, then put them back. Lenny and Avo keep their eyes shut and stay perfectly still.` | ANNE: "Huh. Where did the bananas go?" |
| 17 | 2:08 | `[STYLE] Close-up of the closed bread box. A tiny gap under the lid; inside, one of Bea's eyes peeks out, listening. Then the kitchen light switches off and the shot turns dark blue. Sound: small footsteps walking away, a light switch.` | KIZ: "But Mommy... you said I could mash them. You promised." · ANNE: "I know, sweetie. Next time." |
| 18 | 2:16 | `[STYLE] Night, lit by the blue microwave clock. Close-up through the gap of the bread box: Bea's face in the dark, eyes wet. Bea says in a fast, high-pitched, anxious female voice, softly for the first time: "She wanted to make something... with me."` | Veo · Müzik (piyano) başlar |
| 19 | 2:24 | `[STYLE] Night. Lenny and Avo in the fruit bowl, looking toward the bread box. Avo says in a smooth, smug, posh male voice: "Don't you dare get sentimental." Lenny says in a dry, deadpan, low male voice: "She's a banana. That's what she's for." A pause. Lenny adds, quietly: "It's what I'd want."` | Veo |
| 20 | 2:32 | `[STYLE] Night. The bread box lid lifts from inside. Bea looks out, tearful but determined, moonlight on her spots. Bea says in a fast, high-pitched, anxious female voice: "Lenny. Avo. Take me back."` | Veo |
| 21 | 2:40 | `[STYLE] Night, moonlight. Wide side shot of the three fruits rolling slowly back along the counter, side by side, calm, past the sink and the knife block. No dialogue. Sound: soft rolling.` | — |
| 22 | 2:48 | `[STYLE] Night. Bea back in the fruit bowl between Lenny and Avo. Bea says in a fast, high-pitched, anxious female voice, softly: "Will it hurt?" Lenny says in a dry, deadpan, low male voice: "No. You'll smell amazing." Avo says in a smooth, smug, posh male voice, quietly: "You were always the warmest thing on this counter."` | Veo |
| 23 | 2:56 | `[STYLE] Bright morning. A small child's hand reaches into the bowl and gently lifts Bea. Bea looks back at Lenny and Avo and gives a small, brave smile.` | KIZ: "Mommy! The bananas came back!" |
| 24 | 3:04 | `[STYLE] Morning light, flour dust floating in sunbeams. A mixing bowl on the counter; a small child's hands mash bananas with a fork while a woman's hands guide hers. In the foreground, Lenny and Avo watch from the fruit bowl. Sound: fork on bowl, a child laughing.` | Müzik yükselir |
| 25 | 3:12 | `[STYLE] Close-up of the oven's glass door glowing warm orange; inside, a loaf of banana bread rises. The reflections of Lenny and Avo are visible in the glass. Avo says in a smooth, smug, posh male voice, in awe: "She's... rising." Lenny says in a dry, deadpan, low male voice: "Promotion."` | Veo |
| 26 | 3:20 | `[STYLE] Evening. A small child's hand places a small plate with a warm slice of banana bread next to the fruit bowl. Steam rises. Avo closes his eyes and breathes it in. Avo says in a smooth, smug, posh male voice: "Incredible." Lenny says in a dry, deadpan, low male voice: "Classic."` | Önce KIZ: "Thank you, bananas." |
| 27 | 3:28 | `[STYLE] Next morning. A hand places a bunch of bright green, unripe bananas into the fruit bowl. The smallest green banana opens wide worried eyes and spots one tiny brown dot on its peel. It says in a fast, high-pitched, anxious female voice: "What is that. Is that a spot?!"` | Veo |
| 28 | 3:36 | `[STYLE] Two-shot of Lenny and Avo. They slowly turn and look at each other. Lenny says in a dry, deadpan, low male voice: "Here we go." Avo gives a tiny smirk. Hold for two seconds.` | Veo · Siyaha kes, müzik son notası |

Siyah ekrandan sonra 3 saniye ortada beyaz yazıyla `Counter Culture` ve altında `Best Before` (kurguda eklenir). Toplam süre yaklaşık 3:45.

---

## 5. Ses satırları (ElevenLabs, metinden sese)

**ANNE** — sıcak, biraz yorgun, otuzlu yaşlarda bir kadın; Amerikan aksanı. Telefon satırına hafif oda yankısı ekle.

1. "Tomorrow? The bake sale? ...No, it's fine. The bananas are basically gone. I'll make banana bread tonight, with Mia."
2. "Huh. Where did the bananas go?"
3. "I know, sweetie. Next time."

**KIZ (Mia)** — 6–7 yaşında bir kız çocuğu, Amerikan aksanı.

1. "But Mommy... you said I could mash them. You promised."
2. "Mommy! The bananas came back!"
3. "Thank you, bananas."

Meyve sesleri için: her karakterin en iyi çıkan Veo klibindeki sesi ElevenLabs'te ses olarak kaydet; diğer bütün kliplerin sesini Voice Changer ile bu sese çevir.

---

## 6. Müzik (Suno)

İki ayrı parça üret:

```
Instrumental only. Playful heist music: pizzicato strings, light percussion, sneaky clarinet, comedic, small-scale. 45 seconds. No vocals.
```

```
Instrumental only. Gentle solo piano with soft strings, warm, bittersweet, then hopeful and light. 1 minute 30 seconds. No vocals.
```

- 1. parça: sahne 11–15 (operasyon). Sahne 13'te kupa alınırken bir anlığına sustur.
- Sahne 16–17'de müzik yok, yalnızca ortam sesi.
- 2. parça: sahne 18'de çok kısık başlar, sahne 24'te yükselir, sahne 28'in sonunda biter.

---

## 7. Yayın paketi

- **Başlık:** `The banana had one day left`
- **Yedek başlık:** `Best Before — an animated short film`
- **Açıklama:** `Bea the banana overheard she's becoming banana bread tonight. Her friends Lenny and Avo have a plan. A short film made with AI animation tools. Counter Culture.`
- **Kapak prompt'u:**

```
Cinematic 16:9, Pixar-like photorealistic 3D animation. A spotted ripe banana with wide worried cartoon eyes peeking out from under the lid of a wooden bread box on a kitchen counter at night, blue moonlight, a lemon and an avocado with cartoon eyes watching from a fruit bowl in the soft-focus foreground. Leave empty space on the right side.
```

Kapağın sağ tarafına kurguda büyük harfle `1 DAY LEFT` yaz.

---

## 8. Üretim sırası

1. Bölüm 3'teki beş referans görseli üret. Karakterler pilottakine benzesin; beğenmediğin görseli değiştir, sonra hiç değiştirme.
2. **Deneme:** önce sahne 2, 13 ve 22'yi üret (tek karakter konuşma, üç karakterin donup kaldığı an, üç karakterin bir arada konuştuğu sahne). Karakterler üçünde de aynı görünüyorsa devam et.
3. Kalan sahneleri sırayla üret. Her sahne için genelde 2–3 deneme gerekir; 28 sahne için 60–90 üretim hesapla.
4. Meyve seslerini Voice Changer ile eşitle; anne ve kız satırlarını üret.
5. Kurgu: sahneleri diz, boşlukları kırp, renkleri eşitle, müziği ve sesleri yerleştir, İngilizce altyazı ekle.
6. Yüklerken YouTube'un "değiştirilmiş veya sentetik içerik" beyanını işaretle.

## 9. Üretirken dikkat

- Gece sahnelerinde (17–22) "KITCHEN NIGHT" referansını yükle; gündüz sahnelerinde "KITCHEN".
- Sahne 11, 21 ve 24 konuşmasızdır; Veo yerine Kling daha akıcı hareket verirse onu kullan.
- Sahne 9, 19 ve 22'de üç ya da dört replik var. Veo 8 saniyeye sığdıramazsa sahneyi ikiye böl (aynı kadraj, ikinci klipte kalan replik).
- Ekran yazılarını videoya ürettirme; hepsini kurguda ekle.
- Süreler tahminidir; kurgudan sonra gerçek süre 3:30 ile 4:15 arasında çıkabilir.

---

## Verdiğim kararlar

- **Süre ~3:45 seçildi.** Bu araçlarla 8 saniyelik klipleri birleştirerek tutarlı karakterle çıkılabilecek makul üst sınır bu civarda; daha uzunu karakter ve ses tutarlılığını ciddi şekilde zorlar ve üretim sayısını ikiye katlar. Tek bir olay örgüsü bu süreyi rahat taşır.
- **Format yatay 16:9.** Kısa film izlenimi ve YouTube'un normal (Shorts dışı) videosu için yatay format gerekiyor.
- **Hikâye: Bea merkezde.** Dikey bölümlerdeki esprilerin en duygusal potansiyeli olanı "banana bread" kaderi; komediden dokunaklı bir sona geçişe en uygun karakter Bea. Lenny ve Avo ilk kez ona yardım ederek gelişiyor.
- **İnsanlar yalnızca el ve ses.** Yapay zekâ videoda insan yüzü sahneden sahneye en çok değişen şey; anne ve kızın yüzü hiç görünmüyor, sesleri ElevenLabs'ten geliyor.
- **Meyve sesleri Voice Changer ile sabitleniyor.** 30 saniyelik bölümde kabul edilebilir olan ses kayması 3–4 dakikalık filmde dikkat dağıtır; dudak uyumunu bozmadan sesi eşitlemenin en az işli yolu bu.
- **Müzik var ama kurguda ekleniyor.** Stil bloğunda "no music" kalıyor; müzik Suno'dan iki parça olarak gelip sahnelere göre yerleştiriliyor.
- **4–10. bölüm dosyası silinmedi.** `konusan-meyveler-bolum-4-10.md` kısa video formatında; ileride kullanılmazsa görmezden gelinebilir, ama bazı fikirleri (buzdolabı, kesekâğıdı, guakamole) ikinci bir kısa filme malzeme olabilir.
