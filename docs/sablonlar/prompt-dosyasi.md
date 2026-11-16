# Prompt Dosyası — Şablon ve Dizin

> Kullanım: Her video için Bölüm 1'deki sayfayı doldur, `08_yayin/prompt-dosyasi.md` olarak sakla ve giriş istemeden açılan bir sayfada yayınla. Bölüm 2'deki dizin tek kopyadır (`03_KAYITLAR/prompt-dizini.md`); her videoda en üste bir satır eklenir. Akış ve süreler: `03-yapim-is-akisi.md` Bölüm 5.5.
>
> Kurallar: (1) Prompt, videoda ekranda görünenle **harfi harfine** aynıdır; yalnızca kurgusal şirkete özgü yerler köşeli parantezli alana çevrilir. (2) Prompt yayından önce yeni bir sohbette yeniden denenmiştir. (3) Aynı metin videonun açıklamasında da tam olarak durur; sayfa onun düzenli hâlidir, kilidi değildir. (4) Sayfada e-posta istenmez.

---

## 1. Video sayfası (izleyicinin gördüğü)

```text
KISA MESAİ · KM-[NO]
[VİDEONUN BAŞLIĞI]
Video: [VİDEO BAĞLANTISI]
Çekim tarihi: [AY YIL] · Araç: [ARAÇ ADI; arayüzde görünen model adı]

BU PROMPT NE İŞE YARAR
[Tek cümle: hangi girdiden hangi çıktı. Örn. "Dağınık bir satış dökümünden aylık özet tablo ve 3 maddelik yorum çıkarır."]

Benim ölçümüm: elle [ELLE SÜRE], yapay zekâyla [YZ SÜRE], [TUR SAYISI] düzeltme turuyla.
Prompt'u hazırlamam ayrıca [KURULUM SÜRE] sürdü; sen hazırını kullanıyorsun.

────────────────────────────────────────
PROMPT 1 — [ADIM ADI, örn. "Temizleme"]
────────────────────────────────────────
[PROMPT'UN TAM METNİ — köşeli parantezli alanlarla]

────────────────────────────────────────
PROMPT 2 — [ADIM ADI] (varsa)
────────────────────────────────────────
[PROMPT'UN TAM METNİ]

DOLDURACAĞIN ALANLAR
[ALAN 1]   → [ne yazılır; bir örnek]
[ALAN 2]   → [ne yazılır; bir örnek]
[ALAN 3]   → [ne yazılır; bir örnek]

ŞUNU DEĞİŞTİRİRSEN ŞU OLUR
- [Değişiklik] → [sonuç]. (Yalnızca çekimde ya da ön denemede gördüğün etkiler; görmediğini yazma.)
- [Değişiklik] → [sonuç].

GÖNDERMEDEN ÖNCE KONTROL ET
- [Kontrol 1 — videodaki kontrol adımı, örn. "Toplam satırını kendi tablonla karşılaştır."]
- [Kontrol 2]

BİLİNEN SINIR
[Videodaki "yapamadığı şey", tek paragraf: ne oldu, nasıl fark edilir.]

VERİN HAKKINDA
Şirket ya da müşteri verisini bir yapay zekâ aracına yapıştırmadan önce işyerinin kuralına bak. Bu videodaki veri kurgusaldır.

Araçlar güncellendikçe sonuç değişebilir. Bu prompt sende farklı çalıştıysa videonun altına yaz.
Bütün prompt'lar: [DİZİN BAĞLANTISI]
```

Yayın öncesi kontrol (sayfa başına 1 dk):

- [ ] Prompt videodakiyle harfi harfine aynı; kurgusal şirket adı ve gerçek veri kalmadı
- [ ] Yeni bir sohbette denendi: tarih [ ] · sonuç videodakiyle aynı türden
- [ ] Ölçümler `olcum.md` ile aynı
- [ ] Sayfa gizli sekmede, giriş istemeden açılıyor; metin seçilip kopyalanabiliyor
- [ ] Bu video için kısa bağlantı oluşturuldu: [ ] · gizli sekmede denendi

Sayfayı yayınladıktan sonra prompt'u değiştirirsen sayfanın altına tarihli not düş ("[TARİH]: şu satır eklendi, çünkü ..."); videodaki hâli silme, üstünü çiz ya da "videodaki hâli" diye ayrı blokta bırak.

---

## 2. Dizin sayfası (tek bağlantı, bütün videolar)

Kanal sayfasındaki ve her açıklamanın altındaki "bütün prompt'lar" bağlantısı buraya gelir. En yeni video en üstte. Satır başlığı görevdir, video numarası değil; izleyici işini arar.

```text
KISA MESAİ — PROMPT DOSYASI
Her videoda kullandığım prompt'lar: kopyala, köşeli parantezli yerleri doldur, kullan.
Hepsi bir videoda kronometreyle denendi; ölçüm ve takıldığı yer her sayfada yazılı.
Son güncelleme: [TARİH]

GÖREVE GÖRE

Excel ve rapor
- [Görev adı, izleyicinin diliyle]  →  [sayfa bağlantısı]   (video: [kısa başlık])
- ...

E-posta ve yazışma
- [Görev adı]  →  [sayfa bağlantısı]   (video: [kısa başlık])

Sunum
- ...

Mesleğine göre
- Muhasebe: [görev]  →  [bağlantı]
- ...

Başlangıç
- [Görev adı]  →  [bağlantı]

BOŞLUKLARI DOLDUR KALIBI (her işte kullanılabilir)
[Kanalın genel prompt iskeleti; KM-001 yayınlanınca oradaki son hâli buraya yapıştırılır.]
```

Örnek satır (biçim için; adlar çalışma adıdır):

```text
Excel ve rapor
- Dağınık satış dökümünden aylık özet çıkarmak  →  [bağlantı]   (video: Excel işi, elle ve yapay zekâyla)
```

Dizin kuralları:

- Bir görev başlığının altında 5'ten fazla satır birikince alt başlığa böl.
- Çalışmadığı bildirilen ve doğrulanan prompt silinmez; yanına tarihli "güncellendi" notu ve yeni hâli konur.
- Dizinde satış ortaklığı bağlantısı, kayıt formu ya da e-posta duvarı yoktur. Bülten açılınca (KM-011'den itibaren) dizinin en altına tek satırlık davet eklenir; dizin yine açık kalır.

## 3. İç kayıt (`03_KAYITLAR/prompt-dizini.md`, izleyici görmez)

| Video | Görev | Sayfa bağlantısı | Kısa bağlantı | Yeniden deneme tarihi | Son güncelleme ve nedeni |
|-------|-------|------------------|----------------|------------------------|---------------------------|
| KM-001 | | | | | |
| KM-002 | | | | | |
