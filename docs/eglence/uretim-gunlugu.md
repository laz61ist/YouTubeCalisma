# HUX — Üretim Günlüğü

En yeni kayıt en üstte. Yerel oturum her üretim turundan sonra rapor ekler; bulut oturumu görev bırakırsa "YAPILACAK" notu ekler. Kurallar: `CLAUDE.md` → "Ortak çalışma".

---

## 2026-11-19 — YAPILACAK (bulut oturumundan)

1. Pip'i Qwen-Image ile üret (3 seed), en iyisini `docs/eglence/hux-modeller/pip.png` olarak kaydet.
2. `hux-b1-acilis-testi.md`'deki 8 sahne için Qwen-Image-Edit ile anahtar kare + Wan 2.2 I2V, 480p, 129 kare (8 sn), sessiz, hareketler belirgin → `uretim/b1/klipler/taslak_s01.mp4` … `taslak_s08.mp4`.
3. `kurgucu` ile birleştir + sonda 3 sn "HUX" kartı → `uretim/b1/cikti/acilis_taslak_v1.mp4`.
4. Yükseltme testi: `s03_v2.mp4` (480p) → SeedVR2 7B ile 720p → RIFE 32 fps; doğal 720p sürümüyle (`s03_v3_720p_129f_32fps.mp4`) aynı anlardan karelerle karşılaştır, süreyi yaz.
5. Her taslak sahneden 3 önizleme karesini `onizleme/b1/` altına koy, bu günlüğe rapor yaz, commit + push.

---

## 2026-11-19 — Rapor (yerel oturum; sohbetten aktarıldı)

**Ortam:** ComfyUI 0.43.0, Python 3.12.10 (`C:\ComfyUI\.venv`), torch 2.11.0+cu130, RTX 5090 Laptop 24 GB. Custom node: ComfyUI-Frame-Interpolation (rife49.pth kurulu).

**Kurulu modeller:** Wan 2.2 I2V 14B high/low (fp8) + lightx2v 4-step LoRA'lar, Wan 2.2 S2V 14B, Qwen-Image 2512, Qwen-Image-Edit 2511 (+ Lightning LoRA'lar), SeedVR2 7B, umt5_xxl fp8, qwen_2.5_vl_7b fp8, t5gemma, wan_2.1_vae, qwen_image_vae, stable_audio_3 (medium, small_sfx), ming3_tts_tiny, wav2vec2_large_english.

**Sahne 3 (Hux uyuyor), sessiz:**

| Sürüm | Ayar | Süre | Not |
|---|---|---|---|
| s03.mp4 | Hux görselinden doğrudan I2V, 832×480, 81 kare @16 fps, seed 20261119, 4 adım | 85 sn, tepe VRAM 20,4 GB | Yan yatışta yüz pandaya kayıyor |
| s03_v2.mp4 | Qwen-Image-Edit anahtar kare (seed 333) → I2V, 480p | — | Kimlik çok daha iyi; otlarda hafif titreme |
| s03_v3_720p_81f_32fps.mp4 | 720p, 81 kare, RIFE 32 fps | 306 sn, VRAM 19,2 GB | 5 sn, kimlik korunuyor |
| s03_v3_720p_129f_32fps.mp4 | 720p, 129 kare, RIFE 32 fps | ~10 dk | **8 sn**, kayma yok; kamera neredeyse sabit, kulak/horlama hareketi zayıf |

**Ses:** ming3_tts_tiny gerçek bir TTS (8,6 GB) ama ComfyUI 0.43 çalıştıramıyor; güncel sürümde de destek yok. S2V (dudak eşleme) testi ses olmadığı için yapılamadı. Seçenekler: Windows TTS / kullanıcı kaydıyla S2V testi, ya da ElevenLabs (ücretli, onay gerekir).

**İş akışları:** `comfyui/workflows/hux_s03_wan22_i2v_480p.json` (+ 720p/RIFE iş akışları henüz commit edilmedi).
