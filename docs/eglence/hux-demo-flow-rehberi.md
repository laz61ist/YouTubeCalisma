# HUX — Google Flow ile Demo Rehberi (ücretsiz)

Amaç: Google Flow'un ücretsiz günlük kredisiyle 2–3 kısa klip üretip dizinin videoda nasıl göründüğüne bakmak. Satın alma kararı bu demoya göre verilecek.

> Flow'un ücretsiz kredi miktarı ve model adları üçüncü taraf kaynaklara dayanıyor (günde ~50 kredi, Veo Lite klip başına ~10 kredi); arayüzde gördüğün değer geçerlidir.

---

## 1. Hazırlık (5 dakika)

1. **Hux görselini indir:** Higgsfield'da ürettiğimiz görsel →
   https://d8j0ntlcm91z4.cloudfront.net/user_3G61MabGu2Zh3PLqj2ZrTaEQbg8/hf_20261117_181750_6648e81e-205d-4ab5-9005-574458bcf334.png
   (Açılmazsa higgsfield.ai → hesabın → üretimler/Assets bölümünden indir.) Dosyayı `hux.png` diye kaydet.
2. **Flow'u aç:** `labs.google/flow` → Google hesabınla gir. Ücretsiz kredi bakiyen sağ üstte görünür.
3. **Yeni proje** oluştur: adı `HUX demo`.
4. **Ayarlar** (prompt kutusunun yanındaki ayar simgesi):
   - En-boy oranı: **16:9 (yatay)**
   - Model: **Veo'nun en ucuz sürümü (Lite)** — kredi yetiyorsa bir üstü (Fast)
   - Prompt başına çıktı sayısı: **1** (kredi boşa gitmesin)

---

## 2. Pip görselini üret (Flow içinde, görsel modu)

Flow'da görsel oluşturma seçeneğine geç (ya da gemini.google.com'da aynı prompt'u yaz), şunu yapıştır:

```
Original cute caricatured honeyguide bird cartoon character named Pip, full body, three-quarter front view, centered on a plain light grey background. Tiny round brown body, pale cream chest, oversized head, huge shiny expressive eyes, short pink beak, one feather sticking up on his head like a cowlick, energetic excited posture. Stylized 3D animated feature-film look, realistic soft feather texture, soft studio lighting, 16:9.
```

Beğendiğini `pip.png` diye kaydet.

---

## 3. Demo klipleri (Video modu)

Video modunda **görsel ekleyebildiğin seçeneği** kullan (adı "Ingredients to Video" ya da "Frames to Video" benzeri olabilir). Her klipte aşağıda yazan görselleri ekle, prompt'u yapıştır, üret, indir.

### Klip 1 — Asıl demo: "Still no." (Hux + Pip, konuşmalı)
Eklenecek görseller: `hux.png`, `pip.png`

```
Stylized 3D animated feature-film look, cute caricatured animals with big expressive eyes, warm cosy light, 16:9. Inside a cosy underground burrow with tree roots hanging from the ceiling, a bed of dry grass, warm morning light falling through a round entrance. Hux, the honey badger from the reference image (black fur, thick silver-white stripe on his head and back), is fast asleep curled up on the grass bed, snoring softly. Pip, the tiny round brown bird from the reference image, flutters in, lands on Hux's head and gently tugs his ear with his beak. Pip says in a fast, chirpy, high male voice: "You don't even know what it is!" Hux, eyes still closed, says in a gravelly, low, unbothered male voice: "Still no." Pip's feathers puff up in frustration. Funny, friendly mood. Sound: soft snoring, tiny wing flaps. No music, no subtitles, no on-screen text.
```

### Klip 2 — "Honey" ve göz açılması (komik zamanlama testi)
Eklenecek görseller: `hux.png`, `pip.png`

```
Stylized 3D animated feature-film look, cute caricatured animals, warm cosy light, 16:9. Close-up inside a cosy underground burrow. Pip, the tiny round brown bird from the reference image, tiptoes up to the ear of the sleeping honey badger Hux from the reference image and whispers very slowly in a chirpy, high male voice: "...Honey." Two seconds of total stillness. Then one of Hux's eyes pops wide open, perfectly alert. Slow push-in on the eye. Sound: silence, then a tiny cartoon ping. No music, no subtitles, no on-screen text.
```

### Klip 3 — "Where?" (hareket testi, kredi kalırsa)
Eklenecek görseller: `hux.png`, `pip.png`

```
Stylized 3D animated feature-film look, cute caricatured animals, cheerful morning light, 16:9. A round burrow entrance between the roots of a big pine tree at the edge of a wildflower meadow. Hux, the honey badger from the reference image, marches out of the burrow fully awake and determined. He says in a gravelly, low, unbothered male voice: "Where?" Pip, the tiny round brown bird from the reference image, bursts into the air with joy and says in a fast, chirpy, high male voice: "Ha! Follow me!" Pip flies off across the meadow and Hux trots after him. Sound: birdsong, wing flaps, little footsteps. No music, no subtitles, no on-screen text.
```

**Kredi planı:** Bir günde 2–3 klip. Klip 1 bozuk çıkarsa önce onu bir kez daha dene; en önemlisi o.

---

## 4. İzlerken bak (ve bana yaz)

1. Hux, görseldeki Hux'a benziyor mu?
2. Pip küçük ve sevimli kalıyor mu?
3. Konuşmalar anlaşılıyor mu, dudaklar uyuyor mu?
4. Hux'un sesi Klip 1 ile Klip 3 arasında aynı karakter gibi mi?
5. Klip 2'deki göz açılması güldürüyor mu?
6. Genel olarak: "Bunu izlerim" dedirtiyor mu?

Klipleri bana yükleyebilirsen birleştirip kontrol ederim; yükleyemezsen cevapları yazman yeterli.

---

## 5. Sık sorunlar

| Sorun | Çözüm |
|---|---|
| Karakter görselden farklı çıktı | Görselleri tekrar ekle; prompt'taki tarif kısmını silme |
| Konuşma yok ya da yanlış kişi konuşuyor | Repliği tek karaktere indir, diğer repliği ayrı klipte üret |
| Ekranda yazı çıktı | Prompt sonundaki "no subtitles, no on-screen text" kısmının durduğundan emin ol, yeniden üret |
| Kredi bitti | Ertesi gün ücretsiz kredi yenilenir |
| Görsel ekleme seçeneği yok | Görsel olmadan sadece prompt'la dene; karakter tutarlılığı düşer ama tarz ve ses yine görülür |
