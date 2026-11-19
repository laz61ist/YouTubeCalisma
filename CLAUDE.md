# YouTubeCalisma — Proje Kuralları

Bu repo iki YouTube işini barındırır:

- **Kısa Mesai** (Türkçe, yapay zekâ ile verimlilik kanalı): `docs/01-…06-*.md`, `docs/senaryolar/`, `docs/sablonlar/`
- **HUX** (İngilizce çizgi film dizisi, ana kahraman bal porsuğu Hux): `docs/eglence/hux-*.md` — şu anki öncelik bu

Kullanıcıyla **Türkçe**, samimi ve kısa konuş. Video/görsel prompt'ları **İngilizce** yazılır.

## Ekip: hangi iş hangi ajana

Ana oturum işi yönetir; aşağıdaki işleri ilgili alt ajana devret. Kullanıcı bir ajanın adını söylerse doğrudan ona ver.

| İş | Ajan | Model / effort |
|---|---|---|
| ComfyUI'yi başlatmak, model/iş akışı kurmak, klip üretmek, ComfyUI hatası çözmek | `comfyui-operator` | Sonnet / medium |
| Bölüm senaryosu, sahne listesi, sahne prompt'u, replik, karakter/hikâye fikri | `senarist` | Opus / high |
| Üretilen klip ya da görselin karakter tutarlılığı, bozulma, ekranda yazı kontrolü | `kalite-kontrol` | Sonnet / low |
| Klipleri birleştirmek, logo/siyah ekran, ses ekleme, altyazı, dışa aktarma | `kurgucu` | Haiku / low |

Basit işleri (dosya okuma, kısa soru, git) ana oturum kendisi yapar; ajan çağırmak için iş en az birkaç adımlık olmalı.

Tipik akış: `senarist` sahne prompt'larını yazar → `comfyui-operator` üretir → `kalite-kontrol` kontrol eder (kalmazsa operatöre geri) → `kurgucu` birleştirir.

## Maliyet kuralları

- Fable modelini kullanma; bu projede gerek yok.
- Kalite yeterliyse ucuz modelde kal; Opus yalnızca yaratıcı yazı ve inatçı hatalar için.
- Ücretli bir servise (Flow, Higgsfield, ElevenLabs, API'ler) kredi harcatan hiçbir şeyi kullanıcıya sormadan yapma.

## HUX dizisinin sabitleri

- Dizi kitabı: `docs/eglence/hux-dizi-kitabi.md` — karakterler, ses tarifleri, stil bloğu, **ton kuralları**. Her yaratıcı iş önce bunu okur.
- Açılış testi: `docs/eglence/hux-b1-acilis-testi.md` (8 sahne)
- Ton: dostane ve eğlenceli; saldırı, yaralanma, kötü karakter, keskin diş yok.
- Format: 16:9, stilize 3D animasyon, 8 saniyelik sahneler.
- Karakter referans görselleri: `docs/eglence/hux-modeller/` (küçük PNG'ler; seçilen resmî görünüm)

## Dosya ve klasör düzeni

- `C:\ComfyUI` — ComfyUI kurulumu (repo dışında; çalışmak için `/add-dir C:\ComfyUI`)
- `comfyui/workflows/` — API biçiminde kaydedilmiş iş akışları (JSON), repoda tutulur
- `uretim/<bolum>/klipler/`, `uretim/<bolum>/kareler/`, `uretim/<bolum>/cikti/` — üretilen medya; **git'e girmez** (`.gitignore`)
- Senaryo ve prompt metinleri `docs/eglence/` altına yazılır

## Ortak çalışma (yerel oturum + bulut oturumu)

İki Claude oturumu aynı dalda (`claude/quirky-dijkstra-e7uour`) çalışır: **yerel** (kullanıcının PC'si, ComfyUI, üretim) ve **bulut** (planlama, senaryo, ikinci göz). Bulut oturumu PC'yi ve videoları göremez; ne bilmesi gerekiyorsa git ile gider.

- **İşe başlarken:** `git pull`. **İş bitince:** commit + `git push`. Zorla push (`--force`) yok; çakışırsa `git pull` ile birleştir.
- **Rapor:** Her üretim turunun raporunu `docs/eglence/uretim-gunlugu.md` dosyasının **en üstüne**, tarih ve saatle ekle (ne üretildi, ayarlar, süre, sorunlar, sıradaki adım). Bulut oturumu raporları buradan okur.
- **Önizleme kareleri:** Her klipten 3–4 kare (baş, orta, son) `onizleme/<bolum>/` altına JPG olarak koy: en fazla 960 px genişlik, dosya başına ~200 KB altı, ad: `taslak_s01_a.jpg` gibi. Bunlar commit edilir (bulut oturumu görsel kontrolü bunlardan yapar). Video dosyaları yine commit edilmez.
- **Görev devri:** Bulut oturumu yerel oturuma iş bırakmak isterse `docs/eglence/uretim-gunlugu.md` en üstüne "YAPILACAK" başlıklı bir not ekler; yerel oturum `git pull` sonrası bunu okur ve uygular.

## Genel kurallar

- Büyük model dosyası (GB'larca) indirmeden önce adını, boyutunu ve kaynağını söyle, onay al.
- ComfyUI kurulumunu (Python ortamı, custom node) değiştirmeden önce sor.
- Kullanıcının dosyalarını silme; üzerine yazmadan önce yedekle.
- Video, ses ve büyük görselleri commit etme.
