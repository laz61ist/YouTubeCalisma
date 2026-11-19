# HUX — Üretim Günlüğü

En yeni kayıt en üstte. Yerel oturum her üretim turundan sonra rapor ekler; bulut oturumu görev bırakırsa "YAPILACAK" notu ekler. Kurallar: `CLAUDE.md` → "Ortak çalışma".

---

## 2026-11-20 00:00 — Rapor (yerel oturum): taslak v2, 1–6 yapıldı (s07 hâlâ kenar)

**Özet:** Yeni uyku referansıyla s01–s07 yeniden üretildi, `acilis_taslak_v2.mp4` birleştirildi. SeedVR2 7B fp8 indirildi (kullanıcı onayı verildi) ve test çalıştı. Bulutun teşhisine katılıyorum: s03–s07 pandaya kayıyordu; kök neden eski uyku karesiydi (önceki "kimlik iyi" değerlendirmem yanlıştı).

### 1. Yeni uyku referansı
`hux.png` + `env_burrow.png` → Qwen-Image-Edit 2511, 4 seed (501–504), "honey badger, NOT a panda: long narrow snout, small flat ears close to the head, silver-white cap…" kimlik cümlesiyle. Dördü de eskisinden belirgin iyi (siyah yüz, kaşlar, küçük kulaklar). **Seed 502** seçildi → `docs/eglence/hux-modeller/hux_uyku.png`; 4'lü montaj `onizleme/b1/hux_uyku_adaylar.jpg`. Dersler: Qwen kimliği "NOT a panda" + tek tek yüz özellikleri yazılınca tutuyor; iki karakterli karelerde "exactly ONE bird" yazmazsan Pip çiftleniyor (s04'te iki Pip, s05'te Hux'un gövdesi kahverengi topa dönmüştü, ikisi de "Hux'u aynen koru + yalnızca bir kuş ekle" cümlesiyle düzeldi).

### 2–4. Klipler (480p, 129 kare, 16 fps, 8,06 sn, sessiz; ~162–171 sn/klip)
Yeni dosyalar `uretim/b1/klipler/taslak2_s01…s07.mp4` (v1 dosyalarının üzerine yazılmadı; s08 v1'den kullanıldı). Önizleme: `onizleme/b1/taslak2_sNN_a/b/c.jpg`.

| Sahne | Değerlendirme |
|---|---|
| s01 | **GEÇTİ.** Yeni seed. Girişteki küçük figür orta karede yine belli belirsiz görünüyor (ufak artefakt, kabul edilebilir). |
| s02 | **GEÇTİ (kenar).** Sakin prompt'la Pip iniyor, iki kez zıplıyor, orta karede yuvaya doğru eğilip bakıyor (sırtı kameraya, doğru hareket); bozuk/ters poz yok. |
| s03 | **GEÇTİ.** Hux artık honey badger: dar burun, küçük kulak, siyah yüz, gümüş başlık; nefes ve kulak kıpırtısı var. |
| s04 | **GEÇTİ.** Tek Pip, Hux'un başında, kulağı çekiyor; Hux uyumaya devam ediyor. |
| s05 | **GEÇTİ.** Tek Pip, sırtında zıplıyor, yana kayıyor; gövde siyah ve tüylü. |
| s06 | **GEÇTİ.** Pip kulağa eğilmiş, kanatla "sır". Hux sakin. |
| s07 | **KENAR / tam çözülmedi.** İlk/son kare yöntemi çalıştı (Wan 2.2 `WanFirstLastFrameToVideo` destekli): başlangıç = gözler kapalı yakın plan, bitiş = yalnızca bir göz açık. Klip kapalı gözle başlayıp **tek gözün yarı açık** bitiyor; ama orta karede (~4 sn) **iki göz birden** kocaman açılıyor. 2. seed (`taslak2_s07_r2.mp4`) daha kötü (iki göz açılıp kapanıyor). v2'de 1. deneme kullanıldı. Model "tek göz" talimatını güvenilir uygulamıyor; çözüm olarak ya orta kareye bağlı ek bir ara anahtar kare (ilk, orta=tek göz açık, son) ya da kurguda kısa kesim öneriyorum. |
Hux gözleri ve ses/dudak: klipler sessiz, değerlendirilemez. Ekranda yazı ve keskin diş yok.

### 5. SeedVR2 7B fp8 yükseltme testi — ÇALIŞTI
- İndirilen: `Comfy-Org/SeedVR2` → `seedvr2_7b_fp8_e4m3fn.safetensors` (7,68 GB, `C:\ComfyUI\models\diffusion_models\`); VAE olarak kurulu `ema_vae_fp16`. Eski `seedvr2_ema_7b_fp8…` dosyası kullanılamaz, yerinde duruyor.
- Akış: `s03_v2.mp4` (832×480, 81 kare) → 1280×720 → SeedVR2 (1 adım, VAE tile 512) → renk düzeltme `lab` → RIFE 32 fps. İş akışı: `comfyui/workflows/hux_upscale_seedvr2_7b_rife32.json`. Çıktı: `s03_v2_seedvr2_720p_32fps.mp4` (1280×720, 161 kare, 5,03 sn, 32 fps).
- **Süre: 108 sn** (yükseltme + RIFE, 81 kare). Karşılaştırma: doğal 720p üretimi 306 sn (81 kare, RIFE dahil). 480p üretim 85 sn + 108 sn = ~193 sn, yani doğal 720p'den ~%37 daha hızlı. 129 kare için tahmin (ölçülmedi): 163 + ~170 = ~5,5 dk, doğal 720p ~10 dk.
- **Kalite (2,5. saniye, yüz yakını, `onizleme/b1/yukseltme_karsilastirma.jpg`: soldan düz lanczos / SeedVR2 / doğal 720p):** SeedVR2'de tüy telleri ve kulak kenarı belirgin daha keskin ve temiz; lanczos bulanık/bloklu; doğal 720p lanczos'a göre biraz iyi ama yumuşak. **Öneri: 480p üret + SeedVR2 ile yükselt** (hem hızlı hem daha keskin). Bunu tek sahnede (eski uyku karesi, s03_v2) denedim; hareketli sahnede titreme/zamansal tutarlılık ayrıca bakılmalı.

### 6. Birleştirme
`uretim/b1/cikti/acilis_taslak_v2.mp4`: taslak2_s01–s07 + taslak_s08 + 3 sn HUX kartı, 832×480, 16 fps, H.264/AAC (sessiz), **67,5 sn**, 9,0 MB. v1 yerinde.

### Dosyalar / sıradaki adım
- Yeni: `hux_uyku.png`, `onizleme/b1/taslak2_*`, `hux_uyku_adaylar.jpg`, `yukseltme_karsilastirma.jpg`, SeedVR2 workflow'u, `comfyui/scripts/` (keys2/keys3/clips2/s07b/uyku/seedvr). Videolar commit edilmedi.
- Sıradaki: (a) s07 için 3 kare (kapalı → tek göz açık → kapalı/sürekli) yöntemi ya da kurgu çözümü; (b) tüm sahneleri 480p→SeedVR2 720p/32 fps ile yükseltip `acilis_taslak_v2_720p.mp4`; (c) s08'de Hux'un yüzü de uyku sahnesi kadar dar/kaşlı mı kontrolü; (d) ses kararı (Ming3 TTS hâlâ çalışmıyor).

---

## 2026-11-20 — YAPILACAK (bulut oturumundan): taslak v2 — durum: 1–6 yapıldı, s07 kenar

**Bulut oturumunun önizleme incelemesi (24 kare + referanslar):** Genel görünüm, ışık ve Pip çok iyi; Pip referansa sadık. Ana sorun **Hux'un yuva sahnelerinde (s03–s07) pandaya benzemesi**: kafa çok yuvarlak, kulaklar büyük ve yuvarlak, yüz geniş, kafanın tamamı beyaz. Referanstaki Hux'un dar ve uzun burnu, küçük ve kafaya yapışık kulakları, belirgin kaşları ve alaycı yarım kapalı gözleri kaybolmuş. s07 yakın çekimde bu çok belirgin; s08'de (yuva dışı) Hux daha doğru. Yerel kalite kontrolündeki "kimlik iyi" değerlendirmesine bu yüzden katılmıyorum; kök neden ortak uyku anahtar karesi (seed 333).

1. **Uyuyan Hux referansı (önce bu):** Qwen-Image-Edit ile `hux.png`'den yeni uyku anahtar karesi üret. Kimlik cümlesine ekle: "honey badger, NOT a panda: long narrow snout, small flat ears close to the head, the silver-white fur is a cap from the forehead over the top of the head and down the back like a cape, the face, cheeks and around the eyes are black, thick expressive eyebrows". 4 seed dene; panda görünümü olmayanı seç ve `onizleme/b1/hux_uyku_adaylar.jpg` (4'lü montaj) + seçileni `docs/eglence/hux-modeller/hux_uyku.png` olarak kaydet.
2. **s03–s06'yı yeni uyku karesiyle yeniden üret** (anahtar kareler + I2V, 480p, 129 kare, aynı seed düzeni).
3. **s07 (tek göz):** İlk kare/son kare yöntemiyle: başlangıç = yeni uyku karesinin yakın planı (gözler kapalı); bitiş = aynı kare, Qwen-Image-Edit ile yalnızca SOL gözü kocaman açık, diğeri kapalı. Prompt: "only his left eye pops open and stays open; the right eye stays closed". Wan 2.2 I2V ilk/son kare desteklemiyorsa önce bildir.
4. **s02:** Ortadaki bozuk Pip pozu için yeni seed ya da daha sakin hareket ("lands softly, hops twice, peeks into the burrow"). s01'deki girişte beliren küçük figür için de yeni seed dene (zorunlu değil).
5. **SeedVR2 7B fp8 (7,68 GB):** Bulut oturumu indirmeyi öneriyor; **kullanıcı yerel oturumda onay verirse** indir ve `s03_v2.mp4` ile yükseltme testini yap.
6. `kurgucu` ile `acilis_taslak_v2.mp4`; önizleme kareleri, günlüğe rapor, commit + push.

---

## 2026-11-19 23:20 — Rapor (yerel oturum): YAPILACAK maddeleri 1, 2, 3, 5 tamam; 4 ONAY BEKLİYOR

**Özet:** Pip referansı, 8 sahnenin anahtar kareleri ve 8 taslak klip (480p, 129 kare = 8 sn, sessiz) üretildi; birleştirilmiş taslak ve önizlemeler hazır. SeedVR2 yükseltme testi kurulu modelle **çalışmadı** (aşağıda).

### 1. Pip
Qwen-Image 2512 + Lightning 8 adım, 3 seed (11/22/33), üçü de iyi. **Seed 11** seçildi → `docs/eglence/hux-modeller/pip.png` (tepe tüyü, kuyruk ve pembe gaga net). İlk üretilen mekân görsellerinde (VALLEY/BURROW) istenmeden hayvanlar çıktı; "uninhabited, no animals" vurgusuyla yeniden üretildi (seed 6). Not: Qwen cfg=1'de olumsuz prompt kullanmıyor, yasağı olumlu cümleyle yazmak gerekiyor.

### 2. Anahtar kareler + klipler (Qwen-Image-Edit 2511 → Wan 2.2 I2V)
- Anahtar kareler: s01 = VALLEY görseli aynen; s03 = daha önceki Hux uyku karesi (seed 333); s02/s04/s05/s06/s07/s08 Qwen-Image-Edit ile (Hux/Pip/mekân referansları, kimlik cümlesi: "yüz, bacak, kuyruk SİYAH; gümüş şerit sadece tepe ve sırt"). Tek seed/kare, hepsi kullanılabilir çıktı.
- Klipler: 832×480, 16 fps, 129 kare (8,06 sn), Wan 2.2 14B high/low fp8 + lightx2v 4 adım, seed 20261119+sahne no. **Her klip ~160–175 sn** (toplam ~22 dk). Boyutlar 0,8–2,2 MB.

| Sahne | Kalite kontrol (kare 3 nokta: baş/orta/son) |
|---|---|
| s01 vadi | **GEÇTİ.** Sis ve çiçekler hareket ediyor, giriş parlıyor. Ortada yuvanın girişinde çok küçük koyu bir figür beliriyor (ufak artefakt). |
| s02 Pip iniş | **KENAR.** Pip iniyor, kanat açıyor, ama orta karede ters/yuvarlanmış poz var; sonda ayakta. Sevimli ama prompt'taki "zıplayıp içeri bakma" zayıf. |
| s03 Hux uyur | **GEÇTİ.** Nefes ve horlama net, kimlik iyi. |
| s04 kulak çekme | **GEÇTİ.** Pip Hux'un başında, gagayla kulağa uzanıyor; Hux uyumaya devam ediyor. |
| s05 mide zıplama | **GEÇTİ (kenar).** Pip karında zıplıyor, Hux dönüyor, Pip yana kayıyor; zarar görme hissi yok. |
| s06 fısıltı | **GEÇTİ.** Pip kulağın yanında kanadıyla "sır" tutuyor; Hux hareketsiz. |
| s07 göz açılışı | **KALDI.** Orta karede **iki** göz birden fal taşı gibi açılıyor (istenen: tek göz, "ping" anı); sonda gözler yine kapalı. Öneri: prompt'ta "only his LEFT eye opens, stays open", açık gözlü bir bitiş karesi anahtar kare olarak ver (ya da ilk/son kare ile I2V). |
| s08 Hux çıkıyor | **GEÇTİ (kenar).** Hux yuvadan yürüyor, Pip havada; ilk karede Hux gözleri kapalı/kısık. Keskin diş yok. |

Genel: ekranda yazı yok, ton uygun, tüm klipler 16:9. Ses/dudak değerlendirilemez (klipler sessiz).

### 3. Birleştirme (kurgucu)
`uretim/b1/cikti/acilis_taslak_v1.mp4`: 8 klip sırayla + 3 sn siyah zeminde beyaz "HUX" (arialbd), 832×480, 16 fps, H.264/AAC (sessiz kanal), **67,5 sn**, 8,9 MB. Henüz s07'yi düzeltmeden birleştirildi (v2 için s07 yeniden üretilmeli; s02 de aday).

### 4. SeedVR2 yükseltme testi — YAPILAMADI
- `seedvr2_ema_7b_fp8_e4m3fn.safetensors` (kurulu) ComfyUI 0.43.0'da **model tipi olarak algılanmıyor** ("Could not detect model type"). İki neden: (a) tensör adları `model.diffusion_model.` öneksiz, ComfyUI öneki yanlış tahmin ediyor; (b) önek eklenince de eşleşmiyor, çünkü ComfyUI'nin SeedVR2 sınıfı `positive_conditioning` / `negative_conditioning` tensörlerini zorunlu istiyor, bu ham dosyada yok. Yani bu dosya bu ComfyUI ile kullanılamaz.
- Önek denemesi için ürettiğim 8 GB'lık kopya silindi; orijinal dosya duruyor.
- **Çözüm (onay bekliyor):** resmî ComfyUI biçimi `Comfy-Org/SeedVR2` (Hugging Face) → `diffusion_models/seedvr2_7b_fp8_e4m3fn.safetensors`, **7,68 GB**. VAE olarak kurulu `ema_vae_fp16` yeterli (aynı dosya, 0,47 GB). Alternatif: `seedvr2_3b_fp8_e4m3fn` 3,16 GB (daha hafif, daha düşük kalite).
- Doğal 720p referansı hazır: `s03_v3_720p_129f_32fps.mp4` (306 sn / 81 kare; 129 karede ~10 dk).

### 5. Önizleme ve dosyalar
- `onizleme/b1/taslak_s01_a.jpg` … `taslak_s08_c.jpg` (24 kare, baş/orta/son, 960 px, hepsi <100 KB).
- Workflow'lar: `comfyui/workflows/hux_s03_keyframe_qwen_edit.json`, `..._wan22_i2v_480p_v2.json`, `..._wan22_i2v_720p_rife32.json`. API betikleri (8 sahne dahil): `comfyui/scripts/`.
- Videolar ve anahtar kareler commit edilmedi (`uretim/` içinde).

### Sıradaki adım
1. SeedVR2 7B fp8 (7,68 GB) indirme onayı → test.
2. s07 (tek göz) ve s02'yi yeniden üret, `acilis_taslak_v2.mp4`.
3. Ses: Ming3 TTS hâlâ çalışmıyor (önceki rapor); karar bekliyor.

---

## 2026-11-19 — YAPILACAK (bulut oturumundan) — durum: 1, 2, 3, 5 yapıldı; 4 onay bekliyor

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
