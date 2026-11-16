# Konuşan Meyveler — Pilot Paket

İngilizce, dikey (9:16), 30–40 saniyelik komedi bölümleri. Bu dosya tek başına yeterlidir: yeni bir oturumda bu dosyayı göstererek devam edebilirsin.

Dizi adı (öneri): **Counter Culture** — bir mutfak tezgâhında yaşayan meyveler.

---

## 1. Hangi iş hangi modelle

Model adları bilgi kesim tarihime (Haziran 2026) göredir; sürümler hızlı değişir. Aracı açtığında en güncel sürümü seç.

| İş | En uygun araç | Neden | Yedek |
|---|---|---|---|
| Senaryo, diyalog, prompt | Claude (bu depo) | Metin işi | — |
| Karakter referans görseli | Gemini görsel modeli (Nano Banana) | Aynı karakteri farklı pozlarda tutarlı üretir | Midjourney, ChatGPT görsel |
| Konuşan karakter klibi (ses ve dudak dahil) | Google Veo (Flow ya da Gemini içinden) | Diyaloğu, sesi ve dudak hareketini tek üretimde verir; bu tür videoların çoğu bununla yapılıyor | Sora, Kling |
| Karakter sesi tutarlı kalsın istersen | ElevenLabs (ses) + Kling ya da Hedra (dudak eşleme) | Her klipte aynı ses; daha çok iş | — |
| Kısa film için sinematik sahne | Veo ya da Kling, görselden videoya | Referans görselle karakter ve mekân sabit kalır | Runway |
| Müzik | Suno | Kısa, telifsiz tema müziği | Udio |
| Kurgu, altyazı | CapCut | Dikey video için hızlı, ücretsiz katmanı var | DaVinci Resolve |

**Önerilen yol (en az iş):** referans görsel → Veo'da görselden videoya, diyalog prompt'un içinde → CapCut'ta birleştir.

**Bilinen sınır:** Veo her klipte sesi yeniden üretir; aynı karakterin sesi klipler arasında biraz değişebilir. Ses tarifini her prompt'ta kelimesi kelimesine aynı tut. Yetmezse ElevenLabs + dudak eşleme yoluna geç.

---

## 2. Üretim adımları

1. Bölüm 3'teki üç referans prompt'uyla karakter görsellerini üret; beğendiğini kaydet.
2. Her sahne için: referans görseli yükle, sahne prompt'unu yapıştır, 8 saniyelik klip üret.
3. Dudak ya da ses bozuksa aynı prompt'la yeniden üret (genelde 2–3 denemede tutar).
4. Klipleri CapCut'ta sırayla diz, aralardaki boşlukları kırp, İngilizce altyazı ekle.
5. Başlık ve açıklamayı bölümün altından al.

Her sahne prompt'unun başına şu **stil bloğunu** ekle (aşağıdaki prompt'larda `[STYLE]` yazan yere):

```
Vertical 9:16. Photorealistic 3D animation, Pixar-like. Real-looking fruit with small expressive cartoon eyes and a mouth, no arms or legs. Setting: a sunlit wooden kitchen counter, white tiled wall behind, soft morning light, shallow depth of field. No subtitles, no on-screen text, no music.
```

---

## 3. Karakterler

| Karakter | Kişilik | Ses tarifi (her prompt'ta aynen kullan) |
|---|---|---|
| **Lenny** (limon) | Ekşi, alaycı, hiçbir şeye şaşırmaz | `a dry, deadpan, low male voice` |
| **Bea** (muz) | Aşırı dramatik, her şeyden panikler | `a fast, high-pitched, anxious female voice` |
| **Avo** (avokado) | Kendini pahalı ve özel sanır, kibirli | `a smooth, smug, posh male voice` |

Referans görsel prompt'ları:

```
Lenny: A bright yellow lemon with half-closed, unimpressed cartoon eyes and a flat mouth, sitting on a sunlit wooden kitchen counter, white tiled wall behind. Photorealistic 3D animation, Pixar-like, shallow depth of field, vertical 9:16.
```

```
Bea: A ripe yellow banana standing upright, leaning on a fruit bowl, with wide worried cartoon eyes and a trembling mouth, on a sunlit wooden kitchen counter, white tiled wall behind. Photorealistic 3D animation, Pixar-like, shallow depth of field, vertical 9:16.
```

```
Avo: A dark green whole avocado with one raised eyebrow, narrow confident cartoon eyes and a smirk, sitting on a small folded linen napkin on a sunlit wooden kitchen counter, white tiled wall behind. Photorealistic 3D animation, Pixar-like, shallow depth of field, vertical 9:16.
```

---

## 4. Bölüm 1 — "Not Yet"

**Fikir:** Avo her gün "henüz olgun değilim" der; olgunlaştığı an kaçırılır.

| Sahne | Prompt |
|---|---|
| 1 | `[STYLE] Close-up of Avo the avocado on his linen napkin. A human finger gently pokes his side. He does not move. Avo says in a smooth, smug, posh male voice: "Not yet. Greatness takes time." Sound: a soft poke, quiet kitchen ambience.` |
| 2 | `[STYLE] Same framing, slightly different morning light. The finger pokes Avo again. Lenny the lemon is visible, out of focus, in the background. Avo says in a smooth, smug, posh male voice: "Still not yet. Come back tomorrow." Lenny says in a dry, deadpan, low male voice: "He said that Monday."` |
| 3 | `[STYLE] Night. The kitchen is dark, lit only by a blue glow from a microwave clock. Avo is asleep on his napkin. His skin slowly turns from green to perfect dark purple. He opens one eye and whispers in a smooth, smug, posh male voice: "Now. Now I am perfect." Nobody is there. Sound: a clock ticking.` |
| 4 | `[STYLE] Morning. The finger pokes Avo and sinks in too far. Avo now has brown soft patches and tired eyes. Avo says in a smooth, smug, posh male voice, defeated: "...You missed it. It was eleven minutes. Last night." Lenny says in a dry, deadpan, low male voice: "Classic."` |

- **Başlık:** `The avocado was ripe for 11 minutes`
- **Açıklama:** `Avo has been "almost ready" all week. Counter Culture, episode 1.`

---

## 5. Bölüm 2 — "Promotion"

**Fikir:** Bea ilk kahverengi lekesini bulur ve yaşlandığını sanır.

| Sahne | Prompt |
|---|---|
| 1 | `[STYLE] Medium shot of Bea the banana leaning on the fruit bowl. She looks down at one small brown spot on her peel and gasps. Bea says in a fast, high-pitched, anxious female voice: "What is that. Lenny. LENNY. What is that?!"` |
| 2 | `[STYLE] Close-up of Lenny the lemon, eyes half-closed, not turning around. Lenny says in a dry, deadpan, low male voice: "It's a spot. You're a banana. It's Thursday."` |
| 3 | `[STYLE] Two-shot of Bea and Lenny. Bea now has three brown spots and is shaking. Bea says in a fast, high-pitched, anxious female voice: "There's more! I'm aging! I had plans!" Lenny says in a dry, deadpan, low male voice: "Relax. Spots mean you're getting promoted."` |
| 4 | `[STYLE] Close-up of Bea, hopeful, eyes wide. Bea says in a fast, high-pitched, anxious female voice: "Promoted? To what?" Cut to Lenny in the same shot, a tiny smile for the first time. Lenny says in a dry, deadpan, low male voice: "Banana bread." Behind them, an oven door light switches on. Sound: an oven click.` |

- **Başlık:** `She got promoted to banana bread`
- **Açıklama:** `Bea found a spot. Lenny is not helping. Counter Culture, episode 2.`

---

## 6. Bölüm 3 — "Nobody Picks the Lemon"

**Fikir:** Blender fişe takılır, herkes korkar; Lenny kendini güvende sanır.

| Sahne | Prompt |
|---|---|
| 1 | `[STYLE] Wide shot of the counter. In the background, a human hand plugs in a large blender. Bea and Avo, in the foreground, turn toward it in horror. Bea says in a fast, high-pitched, anxious female voice: "It's smoothie day. It's SMOOTHIE DAY!" Sound: a plug clicking into a socket.` |
| 2 | `[STYLE] Close-up of Avo trying to look calm, sweating a single drop. Avo says in a smooth, smug, posh male voice: "They won't take me. I'm for toast. I'm a toast fruit." The blender whirs briefly off-screen and he flinches.` |
| 3 | `[STYLE] Close-up of Lenny the lemon, completely relaxed. Lenny says in a dry, deadpan, low male voice: "Calm down. I've lived here three weeks. Nobody picks the lemon. Nobody drinks a lemon."` |
| 4 | `[STYLE] Same close-up of Lenny. A human hand comes into frame and lifts him off the counter. His eyes open fully for the first time. Off-screen, a cheerful human voice says: "Who wants lemonade?" Lenny says in a dry, deadpan, low male voice, rising out of frame: "...Huh." Bea and Avo watch from below.` |

- **Başlık:** `"Nobody picks the lemon"`
- **Açıklama:** `Smoothie day on the counter. Counter Culture, episode 3.`

---

## 7. Yeni oturumda devam etmek için

Yeni oturuma şunu yaz:

> `docs/eglence/konusan-meyveler-pilot.md` dosyasını oku. Aynı karakterler, aynı stil bloğu ve aynı tablo biçimiyle 4–10. bölümleri yaz.

Karar vermen gerekenler:

- Pilotu ürettikten sonra hangi karakterin en iyi çıktığına bak; sonraki bölümleri ona ağırlık vererek yazdır.
- Bölümler birbirinin kopyası olmasın. YouTube'un toplu üretilmiş, birbirine benzeyen yapay zekâ videolarını para kazanma dışında bırakabildiği biliniyor; güncel kural bu oturumda doğrulanamadı.
- Video yapay zekâyla üretildiği için yüklerken YouTube'un "değiştirilmiş veya sentetik içerik" beyanını kontrol et.
