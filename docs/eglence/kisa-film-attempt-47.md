# Kısa Film — "Attempt 47"

İngilizce, yatay (16:9), yaklaşık **2 dakika 30 saniye**: 8 saniyelik 20 sahne. Bu dosya tek başına yeterlidir; yeni oturumda bu dosyayı göstererek devam edebilirsin.

**Tek cümle:** Bir teslimat robotu aynı paketi aynı kapıya 46 kez götürmüştür; 47. denemede kapının neden açılmadığını öğrenmeye karar verir.

**Neden bu hikâye:** Baş karakter ekran yüzlü bir robot, yani dudak eşleme gerekmez; sesi sonradan eklenir. Tek mekân, iki karakter, az diyalog. Yapay zekâ video araçlarının en çok bozduğu şeyler (çok karakter, uzun konuşma, el hareketi) en aza indirildi.

---

## 1. Uygulanan kurallar

Önceki araştırmadan (`docs/01-icerik-uretim-sistemi.md`) kısa filme taşınan kurallar:

| Kural | Bu filmde nerede |
|---|---|
| Başlık ve kapak videodan önce yazılır | Bölüm 7; film bu vaade göre kuruldu |
| İlk 15 saniyede merak sorusu | Sahne 1–3: "Neden 47 deneme, kapı neden açılmıyor?" |
| Selamlama ve giriş jeneriği yok | Film doğrudan kapıda başlar |
| Tempo değişimi | Sahne 4–6: üç hızlı mevsim kesmesi |
| Ortada yön değişimi | Sahne 8: robot emre "Negative" der |
| Yaklaşık 20 saniyede bir yeni bilgi | Pencere (10), komşu (12), haber (13), paket (16) |
| Açılan soru sonda kapanır | Sahne 20: "Attempt forty-seven. Successful." |
| Son cümleden sonra veda ve sözlü abone çağrısı yok | Film son cümleyle biter; bitiş ekranı yalnızca görsel |

Kısa filme uymadığı için alınmayanlar: ekranda kronometre, "yapamadığı şey" bölümü, kopyalanabilir prompt.

---

## 2. Hangi iş hangi modelle

Model adları Haziran 2026'ya kadarki bilgiye dayanır; aracı açtığında en yeni sürümü seç.

| İş | Araç | Not |
|---|---|---|
| Referans görseller (robot, ev, komşu) | Gemini görsel modeli (Nano Banana) | Her sahnede aynı referansı yükle |
| Robotlu sahneler (1–11, 14, 17–20) | Google Veo, görselden videoya | Konuşma isteme; yalnızca ortam sesi |
| Komşunun konuştuğu sahneler (12, 13, 15, 16) | Google Veo, diyalog prompt'ta | Bozulursa Kling ile dene |
| Robot ve depo sesi | ElevenLabs | Bölüm 5'teki satırları üret, kurguda yerleştir |
| Müzik | Suno | Bölüm 6'daki prompt |
| Kurgu, ekran yazıları, altyazı | CapCut | "ATTEMPT 47" gibi yazıları videoya ürettirme, kurguda ekle |
| Senaryoda değişiklik | Claude Opus 5.5 | Küçük düzeltme için Sonnet 5.5 yeter |

---

## 3. Referans görseller

```
ROBOT: A small white six-wheeled sidewalk delivery robot, knee-high, rounded box body with a hinged lid on top, slightly scuffed and weathered. On its front is a black screen showing two simple round blue pixel eyes. One small headlight under the screen. A short orange flag antenna at the back. Neutral grey background, product-shot lighting, 16:9.
```

```
HOUSE: A small old English-style suburban cottage with a faded blue front door, brass doorbell, one front window with dusty glass and closed lace curtains, a short stone garden path, a low wooden gate, and an overgrown, empty flower bed under the window. Quiet street, early morning mist, cinematic, 16:9.
```

```
NEIGHBOUR: An elderly woman in her seventies, short grey hair, kind tired face, moss-green knitted cardigan, holding a metal watering can, standing behind a low garden hedge. Soft overcast daylight, cinematic portrait, 16:9.
```

Her sahne prompt'unun başına şu **stil bloğunu** ekle (`[STYLE]` yazan yere):

```
Cinematic 16:9, photorealistic live-action look, soft natural light, muted colours with warm highlights, shallow depth of field, slow steady camera. No subtitles, no on-screen text, no music.
```

---

## 4. Sahne listesi

"Ses" sütunundaki robot ve depo satırları videoya ürettirilmez; ElevenLabs'te üretilip kurguda eklenir. "Yazı" kurguda eklenecek ekran yazısıdır.

| # | Zaman | Görüntü prompt'u | Ses / Yazı |
|---|---|---|---|
| 1 | 0:00 | `[STYLE] Early misty morning. The small white delivery robot rolls up the stone garden path toward the cottage's faded blue door. Low tracking shot from behind the robot. Sound: small electric motor hum, wheels on stone, distant birds.` | — |
| 2 | 0:08 | `[STYLE] Close-up of the robot's screen face at the door, two round blue pixel eyes looking up at the brass doorbell. A small mechanical arm tip presses the bell. Sound: an old doorbell ringing inside an empty house.` | ROBOT: "Good morning. Parcel for Mr. Arthur Bell. Signature required." · Yazı: `ATTEMPT 47` |
| 3 | 0:16 | `[STYLE] Static wide shot of the closed blue door and the robot waiting in front of it. Nothing happens. The robot's eyes blink once. Wind moves dead leaves across the path. Sound: wind, silence.` | ROBOT: "Attempt forty-seven. Unsuccessful." |
| 4 | 0:24 | `[STYLE] Same static wide shot of the door and the robot, but in heavy rain, grey daylight, water running off the robot's lid. Sound: heavy rain.` | Yazı: `ATTEMPT 12` |
| 5 | 0:28 | `[STYLE] Same static wide shot of the door and the robot, but in deep snow, snow piled on the robot's lid, breath-like steam from its vents. Sound: muffled winter quiet.` | Yazı: `ATTEMPT 23` |
| 6 | 0:32 | `[STYLE] Same static wide shot of the door and the robot, at night in autumn, orange leaves on the ground, the robot's single headlight lighting the door. Sound: night crickets.` | Yazı: `ATTEMPT 38` |
| 7 | 0:36 | `[STYLE] Misty morning again. The robot turns away from the door and rolls down the path, then stops at the low wooden gate. Side tracking shot. Sound: motor hum stopping.` | DEPO: "Unit D-7. Parcel flagged undeliverable. Return to depot for disposal." |
| 8 | 0:44 | `[STYLE] Close-up of the robot's screen face at the gate. Its blue pixel eyes slowly turn to look back toward the house. The eyes narrow slightly, determined.` | ROBOT: "Negative. Delivery is not complete." |
| 9 | 0:52 | `[STYLE] The robot rolls across the overgrown grass to the front window and rises on its suspension to look inside. Shot from behind the robot, the dusty window in front of it.` | — |
| 10 | 1:00 | `[STYLE] View through dusty window glass into a still, dim living room: an empty armchair with a folded blanket, a framed photograph of an elderly couple on a side table, and a pile of unopened letters on the floor under the door's letter slot. Dust in a beam of light. Slow push in. Sound: a clock ticking faintly.` | — |
| 11 | 1:08 | `[STYLE] Close-up of the robot's screen face reflected in the window glass. Its round blue eyes change into two short flat lines, worried.` | ROBOT: "No movement detected. Since... spring." |
| 12 | 1:16 | `[STYLE] Over the robot's shoulder: the elderly neighbour in the moss-green cardigan stands behind the low hedge holding a watering can, looking down at the robot with a sad smile. She says in a gentle, elderly English voice: "He's not coming to the door, sweetheart."` | Veo diyaloğu |
| 13 | 1:24 | `[STYLE] Medium close-up of the elderly neighbour behind the hedge. She lowers the watering can. She says in a gentle, elderly English voice: "Arthur passed in April, love."` | Başta ROBOT: "Mr. Bell must sign." |
| 14 | 1:32 | `[STYLE] Wide shot: the small robot completely still on the grass, the big quiet house behind it. Its screen eyes dim to two small dots. A long, still moment. Sound: wind.` | DEPO: "Unit D-7. Return to depot." · ROBOT: "...The parcel is still his." |
| 15 | 1:40 | `[STYLE] The elderly neighbour opens the low wooden gate and kneels beside the robot on the grass. She gently presses her thumb on the robot's screen. She says in a gentle, elderly English voice: "Well. Let's see what he was waiting for." Sound: a soft confirmation chime.` | Veo diyaloğu |
| 16 | 1:48 | `[STYLE] Close-up from above: the robot's lid opens with a small hiss. Inside is a brown paper bag of tulip bulbs and a small handwritten card. The elderly woman's hands lift the card. She reads aloud in a gentle, elderly English voice, off-screen: "For Margaret's garden. Plant before the frost."` | Veo diyaloğu |
| 17 | 1:56 | `[STYLE] Dusk. Wide shot of the overgrown flower bed under the window. The elderly woman kneels with a small trowel; the robot is parked beside her, its headlight shining a warm circle on the soil. Sound: trowel in earth.` | — |
| 18 | 2:04 | `[STYLE] Close-up in the headlight beam: old hands pressing tulip bulbs into dark soil. The first snowflakes begin to fall through the light.` | ROBOT: "Delivery... in progress." |
| 19 | 2:12 | `[STYLE] Bright spring morning. Same wide shot of the cottage front: the flower bed under the window is now full of red and yellow tulips. The blue door is still closed. Sound: birdsong.` | — |
| 20 | 2:20 | `[STYLE] The robot rolls along the pavement carrying a new parcel, stops at the low gate and looks at the tulips. Close on its screen face: the blue pixel eyes curve into two happy arcs. Then it rolls on out of frame.` | ROBOT: "Attempt forty-seven. Successful." · Yazı: `DELIVERED` |

Sahne 4–6 kurguda 4'er saniyeye kırpılır; toplam süre yaklaşık 2:28 olur.

---

## 5. Ses satırları (ElevenLabs)

**ROBOT** — sakin, nazik, hafif sentetik bir ses; yavaş konuşur.

1. "Good morning. Parcel for Mr. Arthur Bell. Signature required."
2. "Attempt forty-seven. Unsuccessful."
3. "Negative. Delivery is not complete."
4. "No movement detected. Since... spring."
5. "Mr. Bell must sign."
6. "...The parcel is still his."
7. "Delivery... in progress."
8. "Attempt forty-seven. Successful."

**DEPO** — soğuk, düz, kurumsal bir kadın sesi; hoparlörden gelir gibi (kurguda telefon/telsiz efekti ekle).

1. "Unit D-7. Parcel flagged undeliverable. Return to depot for disposal."
2. "Unit D-7. Return to depot."

---

## 6. Müzik (Suno)

```
Instrumental only. Gentle solo piano with soft strings, slow, minimal, bittersweet, hopeful ending. Starts almost silent, builds slightly in the last 30 seconds. 2 minutes 30 seconds. No vocals.
```

Müzik sahne 7'de çok kısık başlasın, sahne 14'te tamamen sussun, sahne 17'de geri gelsin.

---

## 7. Yayın paketi

- **Başlık:** `A delivery robot tried the same door 47 times`
- **Yedek başlık:** `Attempt 47 — a short film`
- **Açıklama:** `Unit D-7 has one parcel it cannot deliver. A short film made with AI video tools.`
- **Kapak prompt'u:**

```
Cinematic 16:9. A small white six-wheeled delivery robot with two round blue pixel eyes on its screen, seen from behind and slightly to the side, waiting in front of a faded blue cottage door in light snow, warm headlight glow on the door. Lonely, quiet mood. Leave empty space at the top right.
```

Kapağın sağ üstüne kurguda büyük harfle `47 TRIES` yaz.

---

## 8. Üretirken dikkat

- Önce sahne 1, 2 ve 10'u üret. Robot bu üçünde aynı görünüyorsa devam et; görünmüyorsa referans görseli değiştir.
- Sahne 4–6 aynı kadrajın mevsim değişimleridir: sahne 3'ün son karesini referans olarak ver.
- Ekran yazılarını ve kart üzerindeki yazıyı videoya ürettirme; yapay zekâ videoda yazı çoğunlukla bozuk çıkar.
- Yüklerken YouTube'un "değiştirilmiş veya sentetik içerik" beyanını kontrol et; açıklamada yapay zekâyla yapıldığı zaten yazıyor.
- Süreler tahminidir; kurgudan sonra gerçek süre 2:15 ile 2:40 arasında çıkabilir.
