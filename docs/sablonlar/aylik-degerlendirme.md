# Aylık Değerlendirme — Kısa Mesai · [YYYY-AA]

> Kullanım: Her ay `03_KAYITLAR/aylik/[YYYY-AA]_aylik-degerlendirme.md` olarak kopyala. Yöntem ve eşikler: `05-performans-analiz-sistemi.md` Bölüm 5 (adımlar), Bölüm 3 (okuma kuralları), Bölüm 7 (blok kaybı). Sayılar `analiz-tablosu` elektronik tablosundan gelir; burada yeniden hesaplanmaz. Kronometreyle, 90 dakika.
>
> **Kısa sürüm:** 28 günlük verisi olan video sayısı 6'nın altındaysa yalnızca Bölüm 0, 1 ve 7 doldurulur; diğer bölümlere "n yetersiz" yazılır.
>
> Boş bırakılan hücre "bakılmadı" demektir. Veri yoksa `veri yok`, grup küçükse `n yetersiz` yaz; tahmin yazma.

| | |
|---|---|
| **Oturum tarihi** | [YYYY-AA-GG] |
| **Kapsanan yayınlar** | KM-[ ] – KM-[ ] |
| **Aşama** (02 belgesi B1) | 1 / 2a / 2b / 3 |
| **28 günlük verisi olan video sayısı** | [ ] |
| **Kıyas basamağı** (02 belgesi B5) | 1 / 2 / 3 (hangi kategoride: [ ]) |
| **Oturumun gerçek süresi** | [ ] dk |

---

## 0. Veri hazırlığı (10 dk)

- [ ] Bu ay 28. günü dolan bütün videoların `28g` sütunları dolu
- [ ] Etiket sütunları (A–O) bu ay yayınlanan videolarda yayın günü yazılmış; sonradan değiştirilen yok
- [ ] Gelişmiş moddan dışa aktarılan tabloyla 3 video karşılaştırıldı → fark: [yok / hangi hücre]
- [ ] Bu ayın olağandışı haftaları (tatil, yayın kayması, teknik sorun): [ ]

## 1. Aylık bakış (20 dk)

Performans kaydı §5.3 satırını doldur; buraya yalnızca geçen aya göre **değişeni** yaz.

| Gösterge | Geçen ay | Bu ay | Not |
|---|---|---|---|
| Yeni / ara sıra / düzenli izleyici | | | Düzenli sütununda ilk 6 ay 0 normaldir (02 belgesi A5) |
| Abonelik akışı + bildirim kaynaklı görüntüleme | | | |
| Bitiş ekranı tıklama oranı (ayın videolarının medyanı) | | | |
| Önerilen'de kendi videolarından gelen pay | | | |
| Taban trafiği (28 günden eski videoların aylık görüntülemesi) | | | Mevsim kontrolü (05 belgesi Bölüm 3, kural 7) |
| Stokta hazır video | | | |

## 2. Kalıp bulma (25 dk)

### 2.1 Grup medyanları

Her etiket için ayrı blok aç. 3'ten az videolu gruba medyan yazma.

**Etiket: [Kat. / Kurgu / Başlık formülü / Kapak çifti / Hook / Rol / Süre bandı / Konu ailesi]**

| Değer | Video sayısı | Görüntüleme ÷ medyan 28g (medyan · en düşük–en yüksek) | Karşılaştırmaya ulaşan % | 1.000 gör. başına abone | Prompt tıkl. / 1.000 gör. |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |

Aralıkları ayrık çıkan grup çifti var mı: [yok / hangileri, hangi sütunda]

### 2.2 Çapraz kontrol

Fark görünen etiket başka bir etiketle birlikte mi geliyor?

| Fark görünen etiket değeri | Birlikte geldiği etiket değeri | Birlikte kaç video / toplam kaç | Ayrıştırılabilir mi | Ayrıştıracak video (ne sabit, ne değişir) |
|---|---|---|---|---|
| | | | E / H | |

### 2.3 En iyi ve en kötü yüzde 20

Sıralama sütunu: `Görüntüleme ÷ medyan 28g`. Bu sütunu dolu video sayısı: [ ] (10'un altındaysa bu bölümü atla). Uç grup büyüklüğü: [ ] video.

| | En iyi | En kötü |
|---|---|---|
| Videolar (No) | | |
| İkinci sıralamada (`1.000 gör. başına abone`) da aynı uçta olanlar | | |

### 2.4 Ortak özellik tablosu

| Özellik (etiket = değer) | En iyi grupta | En kötü grupta | Bütün videolarda (taban) | Ayrıştırıyor mu |
|---|---|---|---|---|
| | [ ] / [ ] | [ ] / [ ] | [ ] / [ ] | E / H |
| | [ ] / [ ] | [ ] / [ ] | [ ] / [ ] | E / H |
| | [ ] / [ ] | [ ] / [ ] | [ ] / [ ] | E / H |
| | [ ] / [ ] | [ ] / [ ] | [ ] / [ ] | E / H |

Kartlardaki "Çıkarım" satırlarından çıkan, etiketlerin yakalamadığı ortak nokta:

- En iyilerde: 
- En kötülerde: 

## 3. Blok kaybı tablosu

Video kartlarındaki işaret noktalarından. `Blok kaybı % = (baştaki % − sondaki %) ÷ baştaki % × 100`. Tutma grafiği olmayan video satırına `veri yok` yaz.

| No | Kurgu | 0:30'da kalan % | Kurulum: kayıp % · dk başına | Görev (kronometre): kayıp % · dk başına | Karşılaştırma: kayıp % · dk başına | Son bölüm ("yapamadığı şey" + prompt): kayıp % · dk başına | En büyük olay (zaman · tür) |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| **Medyan** | | | | | | | |

Dakika başına en çok kaybettiren blok: [ ] · Kaç videoda aynı blok birinci: [ ] / [ ]

Kural adayları (05 belgesi Bölüm 7, adım 7):

| # | Kural adayı | Kanıt (videolar, zaman) | Karşı örnek | Durum |
|---|---|---|---|---|
| | | | | ipucu / bulgu |

## 4. Trafik kaynağı karışımı (10 dk)

Kanal düzeyi, son 28 gün ↔ önceki 28 gün:

| Kaynak | Önceki pay % | Bu dönem pay % | Değişim (puan) | Kaynak içi CTR değişti mi |
|---|---|---|---|---|
| YouTube araması | | | | |
| Önerilen videolar | | | | |
| Göz atma özellikleri | | | | |
| Shorts feed'i | | | | |
| Harici | | | | |
| Diğer | | | | |

| | |
|---|---|
| Plan tuttu mu: "E" sayısı / 28 günlük videolar | [ ] / [ ] |
| Rol bazında: arama [ ] / [ ] · öneri [ ] / [ ] · köprü [ ] / [ ] · merkez [ ] / [ ] | |
| Toplam CTR değişimi karışım etkisi mi (05 belgesi Bölüm 3, kural 5) | E / H / okunmaz |
| Bu ay en çok görüntüleme getiren 5 arama terimi | |
| Videosu olmayan terimler → fikir havuzuna | |

## 5. Kitle ve abone dönüşümü (10 dk)

| | Değer | Hedefle uyum / not |
|---|---|---|
| En büyük yaş grubu ve payı | | Hedef: 26–42 |
| Türkiye payı | | |
| Cihaz dağılımı (telefon / bilgisayar / TV) | | Kapak ve ekran yazısı boyutu için |
| Abone olmayanların görüntüleme payı | | |
| Abonelerin geldiği yer (video sayfası / kanal sayfası / diğer) | | |
| Kitlenin izlediği diğer kanallar / videolar | | Kart yoksa `veri yok` |
| Yorumlarda bu ay anılan meslek ve görevler | | |

Abone dönüşümünde uçlar (`1.000 gör. başına abone 28g`; V3 ve olay sayısı ≥ 10 sağlanan videolar):

| | No | Rol | Kurgu | Bitiş ekranı hedefi |
|---|---|---|---|---|
| En yüksek üç | | | | |
| En düşük üç | | | | |

## 6. Gelir (5 dk; para kazanma açık değilse atla)

| | Geçen ay | Bu ay |
|---|---|---|
| Tahmini gelir | | |
| RPM (kanal) | | |
| Görüntülemede uzun video / Shorts payı | | |
| RPM'i en yüksek ve en düşük video | | |
| Değişim bütün videolarda mı, tek videoda mı | | |

Not: Vergi ve beyan konuları bu formun dışındadır; mali müşavire danış.

## 7. Çıktı (10 dk)

### Sürdür / durdur / dene

Her listede en fazla üç madde. "Sürdür" ve "durdur" yalnızca bulgu düzeyindeki (3+ video, aynı yön, asgari veri tam) maddeleri alır.

| Liste | Madde | Dayandığı videolar | Güven (ipucu / bulgu) | Nereye işlenecek |
|---|---|---|---|---|
| Sürdür | | | | |
| Sürdür | | | | |
| Durdur | | | | |
| Dene | | | | Test kartı no: |
| Dene | | | | Sıraya yazıldı |

Süren testler (en fazla 1 format + 1 elle paket; 02 belgesi B4): [ ]

### Gelecek ayın içerik kararları

| Yayın | Tarih | Kategori | Rol | Kurgu | Konu ailesi | Amaç (omurga / eksik kategori / deneme / ayrıştırma) | Bağlandığı video |
|---|---|---|---|---|---|---|---|
| KM-[ ] | | | | | | | |
| KM-[ ] | | | | | | | |
| KM-[ ] | | | | | | | |
| KM-[ ] | | | | | | | |
| KM-[ ] | | | | | | | |

Kategori dağılımı 02 belgesi B1'deki aşama planına uyuyor mu: E / H → sapma nedeni: 

### Ayın tek kararı

Performans kaydı §5.3'teki "bu ayın tek kararı" hücresine aynen yazılır.

> 

### Gelecek aya devreden sorular

| Soru | Cevaplamak için gereken veri | Ne zaman dolacak |
|---|---|---|
| | | |

## 8. Sistem bakımı (çeyreklik oturumda ayrıntılı; burada yalnızca işaretle)

- [ ] Bu ay 7. günde V1'i sağlayan video: [ ] / [ ] · V2'yi sağlayan: [ ] / [ ]
- [ ] Haftalık rutin 30 dakikada bitti mi: [ ] / [ ] hafta
- [ ] Performans kaydı §5.1 (bulgular) ve §5.2 (açık sorular) güncellendi
- [ ] Bulgu düzeyine çıkan kural ilgili belgeye işlendi: [hangi belge, hangi bölüm]
