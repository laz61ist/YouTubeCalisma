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

## Genel kurallar

- Büyük model dosyası (GB'larca) indirmeden önce adını, boyutunu ve kaynağını söyle, onay al.
- ComfyUI kurulumunu (Python ortamı, custom node) değiştirmeden önce sor.
- Kullanıcının dosyalarını silme; üzerine yazmadan önce yedekle.
- Video, ses ve büyük görselleri commit etme.
