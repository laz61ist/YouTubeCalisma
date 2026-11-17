# HUX — Bölüm 1 Açılış Testi (ilk 1 dakika)

Amaç: Hux dizisinin tarzının, karakter tutarlılığının ve seslerin çalışıp çalışmadığını **tek bir dakikayla** görmek. Karakterler ve ton için `hux-dizi-kitabi.md` dosyasına bak.

İngilizce, yatay (16:9), 8 sahne × 8 saniye ≈ 64 saniye + kurguda eklenecek 3 saniyelik `HUX` logosu.

**Ne oluyor:** Şafak. Minik kuş Pip, bal porsuğu Hux'u uyandırmaya çalışır. Hux her denemede "No." der. Pip sonunda kulağına tek kelime fısıldar: "Honey." Hux'un tek gözü açılır, bir saniye içinde ayağa fırlar ve Pip'in peşine takılır.

---

## 1. Önce referans görseller (Gemini / Nano Banana)

Bu test için yalnızca 4 görsel gerekiyor. Prompt'lar `hux-dizi-kitabi.md` dosyasının 3. bölümünde:

1. **HUX** model sayfası → beğendiğin karakterin tek, önden görünen hâlini ayrıca kırp ya da "same character, single front view, plain background" diye yeniden üret.
2. **PIP** model sayfası → aynı şekilde tek görünüm.
3. **HUX'S BURROW** (yuvanın içi).
4. **THE VALLEY** (vadi genel görünüm).

Görselleri kaydet; her sahnede o sahnede görünen karakterin ve mekânın görselini yükleyeceksin.

---

## 2. Her prompt'a eklenecek bloklar

Veo karakter adlarını bilmez; bu yüzden prompt'larda geçen `[STYLE]`, `[HUX]` ve `[PIP]` yerlerine aşağıdaki metinleri **aynen** yapıştır.

`[STYLE]`

```
Cinematic 16:9. Stylized 3D animated feature-film look: cute caricatured animals with oversized heads, big friendly expressive eyes, exaggerated poses and expressions, short stubby limbs, no sharp teeth shown; realistic soft fur and feather texture, warm light. Cheerful, friendly mood. Shallow depth of field, smooth camera. No subtitles, no on-screen text, no music.
```

`[HUX]`

```
Hux, a cute caricatured honey badger: stocky low body, oversized round head, black fur with a thick silver-white stripe from the top of his head down his back, small round ears with a small notch in the left ear, half-lidded eyes, lopsided grin with no sharp teeth
```

`[PIP]`

```
Pip, a tiny cute caricatured honeyguide bird: round brown body, pale chest, oversized head, huge shiny eyes, short pink beak, one feather sticking up on his head like a cowlick
```

Ses tarifleri (prompt'larda zaten yazılı, değiştirme):

- Hux: `a gravelly, low, unbothered male voice, slow and confident`
- Pip: `a fast, chirpy, high male voice, always talking`

---

## 3. Sahneler

| # | Zaman | Yüklenecek görsel | Prompt |
|---|---|---|---|
| 1 | 0:00 | VALLEY | `[STYLE] Dawn over a quiet valley where a pine forest meets a wildflower meadow, mist over a small pond. Slow aerial push-in toward the roots of a big pine tree, where a small round burrow entrance glows softly. Sound: early birdsong, gentle wind.` |
| 2 | 0:08 | PIP, VALLEY | `[STYLE] [PIP] lands with a bounce in front of a small round burrow entrance between pine roots, hops up and down excitedly and peeks inside. Pip says in a fast, chirpy, high male voice, always talking: "Hux! Hux! Big news! Huge news! Wake up!" Sound: tiny wing flaps, birdsong.` |
| 3 | 0:16 | HUX, BURROW | `[STYLE] Inside a cosy underground burrow with roots hanging from the ceiling and warm light falling through the round entrance. [HUX] is fast asleep, curled up on a bed of dry grass, snoring softly. Without opening his eyes, Hux says in a gravelly, low, unbothered male voice, slow and confident: "No." Sound: soft snoring.` |
| 4 | 0:24 | HUX, PIP, BURROW | `[STYLE] Inside the cosy burrow. [PIP] flutters in and lands on the sleeping [HUX]'s head and gently tugs his ear with his beak. Pip says in a fast, chirpy, high male voice, always talking: "You don't even know what it is!" Hux, eyes still closed, says in a gravelly, low, unbothered male voice, slow and confident: "Still no."` |
| 5 | 0:32 | HUX, PIP, BURROW | `[STYLE] Inside the cosy burrow. [PIP] hops onto the sleeping [HUX]'s round belly and bounces on it like a trampoline. Hux sleepily rolls over, and Pip slides off into the soft grass bed and pops back up with his feathers comically ruffled. Pip says in a fast, chirpy, high male voice, slightly out of breath: "Okay. Okay. Plan B." Sound: soft bounces, rustling grass.` |
| 6 | 0:40 | HUX, PIP, BURROW | `[STYLE] Close-up inside the cosy burrow. [PIP] tiptoes right up to the sleeping [HUX]'s ear, cups the air with one wing like he is telling a secret, and whispers in a fast, chirpy, high male voice, very slowly for the first time: "...Honey." A beat of silence.` |
| 7 | 0:48 | HUX, BURROW | `[STYLE] Extreme close-up of the sleeping [HUX]'s face. Total stillness for two seconds. Then one eye pops wide open, perfectly alert. Slow push-in on the eye. Sound: silence, then a tiny cartoon "ping".` |
| 8 | 0:56 | HUX, PIP, VALLEY | `[STYLE] Morning light at the round burrow entrance between pine roots. [HUX] marches out of the burrow fully awake and determined, right past [PIP]. Hux says in a gravelly, low, unbothered male voice, slow and confident: "Where?" Pip bursts into the air with joy and says in a fast, chirpy, high male voice: "Ha! Follow me!" Pip flies off across the meadow and Hux trots after him. Sound: birdsong, wing flaps, little footsteps.` |

Sahne 8'den sonra kurguda: 3 saniyelik siyah ekranda ortada `HUX` logosu (CapCut'ta yazı olarak ekle; videoya ürettirme).

---

## 4. Nasıl üretilir (Flow / Gemini)

1. Flow'da yeni proje aç, en ileri Veo modelini ve **16:9** oranını seç.
2. Referans görsel yüklenebilen modu kullan (karakter görseli + mekân görseli). Mod adları zaman zaman değişiyor; "görselden videoya" ya da "malzemelerden videoya" benzeri seçenek.
3. Sahne prompt'unu `[STYLE]`, `[HUX]`, `[PIP]` yerleri doldurulmuş hâliyle yapıştır, üret.
4. Her sahne için **2–3 deneme** yap, en iyisini indir. Dosya adlarını `s01.mp4`, `s02.mp4` … diye ver.
5. Bütün sahneler bitince ya CapCut'ta sırayla birleştir ya da klipleri bana yükle, ben birleştiririm.

Toplam: yaklaşık 16–24 üretim.

---

## 5. Testte neye bakacağız?

| Soru | Olmuşsa | Olmamışsa |
|---|---|---|
| Hux 8 sahnede de aynı hayvan gibi görünüyor mu? | Devam | Referans görseli değiştir ya da `[HUX]` tarifini sıkılaştır |
| Pip minik ve sevimli kalıyor mu, başka kuşa dönüşüyor mu? | Devam | Aynı |
| Hux'un sesi sahneler arasında aynı mı? | Veo'nun sesiyle devam | Sesleri ElevenLabs'te üretip dudak eşleme yoluna geç (dizi kitabı, bölüm 7) |
| Dudaklar repliklerle uyuyor mu? | Devam | Aynı |
| Sahne 5 komik mi, yoksa "Hux kuşu ezdi" gibi mi görünüyor? | Devam | Pip'in kendiliğinden kaydığı daha yumuşak bir versiyonla yeniden üret |
| Sahne 7'deki göz açılması gülümsetiyor mu? | Bölümün kalanına geç | Zamanlamayı kurguda oyna (sessizliği uzat) |

Bu altı sorunun cevabını bana yazman yeterli; ona göre ya bölümün kalanını yazarım ya da tarzı düzeltiriz.

---

## Verdiğim kararlar

- **Test, bölümün gerçek açılışı.** Boşa iş olmasın diye: beğenilirse bu dakika doğrudan 1. bölümün ilk dakikası olur.
- **Bu testte ses Veo'dan.** En hızlı yol bu; sesler tutarsız çıkarsa uzun bölümde dizi kitabındaki ElevenLabs yolu kullanılacak.
- **Karakter tarifleri her prompt'ta tekrar ediliyor.** Veo adları tanımaz; referans görsel + aynı tarif, tutarlılığı en çok artıran ikili.
- **Yalnızca 2 karakter ve 2 mekân.** İlk testte değişken az olsun; Bruno, Willow, Dot ve Sylvia sonraki testte.
- **Sahne 5'teki fiziksel komedi yumuşak tutuldu:** Hux uykusunda döner, Pip çimenlere kayar; kimse zarar görmez (ton kuralları).
