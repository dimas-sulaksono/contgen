# Competitor Patterns (Fase 1 — Final dengan 12 Sampel Instagram)

> Disusun oleh `@CompetitiveAnalyst`. Setiap baris berasal dari bukti yang benar-benar diambil.
> Diperbarui: **2026-10-30**. Jumlah sampel Instagram: **12 post (`inputs/instagram/1.png` – `12.png`)**.

## A. Status Sumber

| Sumber | Status | Catatan |
|---|---|---|
| `lapakgaming.com/id-id` (HTML SSR) | **Parsial (Web)** | Metadata, JSON-LD, nama kategori dan nama file banner terbaca. |
| `instagram.com/lapakgaming.id` | **Lengkap (Visual, 12 Post)** | 12 screenshot resolusi penuh (rasio `4:5`, ~1440×1808 px) dianalisis di Bagian C. Teks caption di luar gambar tidak termasuk dalam screenshot; analisis copy difokuskan pada *on-image copy/headline* dan *CTA button*. |

---

## B. Pola dari Situs Web Lapakgaming (`lapakgaming.com/id-id`)

| # | Pola | Bukti | Frekuensi | Relevansi ke Akunmu Game | Confidence |
|---|---|---|---|---|---|
| W1 | **Tumpukan 4 janji di judul**: harga, keamanan, garansi, kemudahan bayar | `<title>`: "Top Up Game Termurah, Dijamin Aman, Garansi 10x Lipat dan Pembayaran Mudah" | 4 kemunculan | Format "benefit stack" bisa ditiru strukturnya menggunakan USP asli Akunmu (Cepat, Bersahabat, Mudah, Aman). Klaim **termurah / garansi 10x** dilarang dipakai. | 0.90 |
| W2 | **Banner hero berbasis kampanye/event/partner** | Path banner: `MLBB-Aspirants 5.0`, `Dramabox`, `IQIYI`, `creatorssquad` | 6 banner | Konten sosmed jauh lebih kuat jika menunggangi momen event/skin rilis di game yang tersedia di Akunmu. | 0.85 |
| W3 | **Rotasi kampanye bulanan** | Folder `202603`, `202608`, `202610` | 3 periode | Kalender konten bulanan mengikuti jadwal update patch/event game. | 0.75 |
| W4 | **Tile promo spesifik per item unggulan** | Aset `540x540-MLBB-DoubleDiamond`, `Free Fire x Naruto`, `ragnarok-origin-special-pack` | 3 | Tonjolkan item spesifik (mis. Weekly Diamond Pass + nominal populer) dibanding sekadar "Top Up Game". | 0.85 |

---

## C. Anatomi Visual & On-Image Copy dari 12 Post Instagram `@lapakgaming.id`

### Daftar 12 Sampel yang Dianalisis (`inputs/instagram/`)
1. `1.png` — MLBB × Jujutsu Kaisen Revamp (WDP Rp29rb-an, WDP 3X Rp87rb-an, 296 DM Rp84rb-an)
2. `2.png` — Free Fire Flash Sale × Naruto Shippuden (4 grid harga + coret harga asli + starburst "Kuota Terbatas")
3. `3.png` — Co-branding Lapakgaming × Yup Paylater (Voucher Rp80.000, kode `YUPLAPAK`, maskot kelinci putih)
4. `4.png` — MLBB Gacha Brutal: The Aspirants (varian karakter 1 — "GRATIS Weekly Diamond Pass")
5. `5.png` — MLBB Gacha Brutal: The Aspirants (varian karakter 2 — A/B creative dengan struktur identik)
6. `6.png` — MLBB × Street Fighter Flash Sale ("LIMITED TIME DEALS! Cuma Rp999 (5 DM) / Cuma Rp17.500 (WDP)", jam spesifik 15.00–17.00 WIB)
7. `7.png` — MLBB Flash Sale Diamond Kuning ("MULAI DARI 1rb + EXTRA 5% OFF")
8. `8.png` — MLBB × Jujutsu Kaisen Teaser/News ("CONFIRMED — SKIN JUJUTSU KAISEN BALIK LAGI! Resale Date: 7 Agustus 2026*")
9. `9.png` — MLBB × Jujutsu Kaisen Revamp (varian nominal: WDP Rp29rb-an, WDP 3X Rp87rb-an, 450 DM Rp126rb-an)
10. `10.png` — Free Fire × Blue Lock Flash Sale (2200 DM Rp290rb-an, 1450 DM Rp194rb-an, 720 DM Rp97rb-an + harga coret)
11. `11.png` — PUBG Mobile × Naruto Shippuden Collab (1500+300 UC Rp420rb-an, 600+60 UC Rp168rb-an, 300+25 UC Rp85rb-an + harga coret)
12. `12.png` — MLBB × Street Fighter 6 Skin Release (WDP Rp29rb-an, 59 DM Rp16rb-an, 296 DM Rp81rb-an + harga coret)

### Tabel Pola Terukur (12 Sampel)

| # | Pola Anatomi | Bukti dari `1.png` – `12.png` | Frekuensi | Cara Adaptasi ke `Akunmu Game` (Bukan Salinan) | Confidence |
|---|---|---|---|---|---|
| **IG1** | **Format kanvas vertikal 4:5 (1440×1800 px)** sebagai standar tunggal feed | 12 dari 12 gambar berdimensi ~4:5 | **12/12 (100%)** | Jadikan `feed_4x5` sebagai default utama di pipeline untuk memaksimalkan ruang layar HP. | 1.00 |
| **IG2** | **Struktur 3-Zona Vertikal (Header 10% → Hook & Pricing 35% → Key Art & CTA 55%)** | Konsisten di 11/12 post promo (`1`–`7`, `9`–`12`); post `8` membalik karakter di tengah dan headline di bawah untuk format *Teaser/News* | **11/12 (92%)** | Adopsi grid 3-zona vertikal, tetapi balik atau bedakan gaya container & palet warna agar khas Akunmu (`#2D9BF0` + `#F4B400`). | 0.98 |
| **IG3** | **Dual-Logo Header Bar**: Logo brand di kiri atas + Logo Game di kanan atas | Semua 12 post menempatkan brand di kiri atas & IP game/partner di kanan atas | **12/12 (100%)** | Di `layout_notes`, sediakan safe-zone kiri atas untuk logo `Akunmu Game` dan kanan atas untuk badge kategori/nama game. | 1.00 |
| **IG4** | **Multi-Tier Pricing Showcase (3 kolom sejajar atau 2×2 grid)** lengkap dengan ikon 3D item di atas tiap harga | 3 kolom sejajar: `1`, `9`, `10`, `11`, `12` (5/12). 2 kolom / 2×2 grid: `2`, `6` (2/12). Single hero offer: `3`, `4`, `5`, `7` (4/12). | **7/12 (58%) multi-tier**, **4/12 (33%) single offer** | Sangat efektif untuk Akunmu! Karena `brand_matrix.json` punya banyak nominal per game (mis. MLBB 5 DM Rp2.700, 34 DM Rp12.200, WDP Rp32.900), tampilkan **3 kartu nominal sekaligus** (Entry, Mid, Sultan/Pass) dalam satu gambar. | 0.95 |
| **IG5** | **CTA Bar Bawah + Trust Tag Transparansi Harga** (pill tombol + label "HARGA FINAL" di kanan tombol) | Muncul identik di bagian bawah tengah pada `1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12` | **11/12 (92%)** | Pain point gamer Indonesia adalah biaya admin tersembunyi. **Jangan tiru bentuk tag merah/pink kompetitor**; buat pill CTA emas `#F4B400` khas Akunmu ("Top Up di akungame.id") dengan sub-badge biru `#2D9BF0` bertuliskan **"Proses Cepat • Harga Bersahabat"**. | 0.98 |
| **IG6** | **Event / Skin Collab Tie-In sebagai Hook Utama** | JJK (`1, 8, 9`), Naruto (`2, 11`), Aspirants (`4, 5`), Street Fighter (`6, 12`), Blue Lock (`10`) | **10/12 (83%)** | Kaitkan copywriting & atmosfer visual dengan momen in-game (push rank season baru, rilis skin, mabar weekend) tanpa melanggar hak cipta logo partner. | 0.95 |
| **IG7** | **Tipografi Harga Super-Besar + Stiker Urgensi / Anchor Price** | Angka nominal harga adalah teks terbesar ke-2 setelah judul; stiker kuning "Kuota Terbatas" (`2, 6, 10`), pita periode jam (`6`), harga coret (`2, 10, 11, 12`) | **11/12 (92%)** | Untuk Akunmu: tonjolkan angka harga eksak dari `brand_matrix.json` dengan warna emas `#FFD86A`/`#F4B400`. **Catatan kepatuhan:** Harga coret (strikethrough) HANYA boleh dipakai jika memang ada data diskon resmi di `brand_matrix.json` (saat ini tidak ada, jadi gunakan harga jujur tanpa coretan palsu). | 0.95 |
| **IG8** | **Format Konten Non-Promo (News / Teaser "CONFIRMED")** untuk engagement organik | Post `8.png`: teks raksasa "CONFIRMED" di belakang karakter + "SKIN ... BALIK LAGI!" + tanggal rilis, tanpa jualan harga | **1/12 (8%)** | Tambahkan variasi angle `teaser_news` atau `komunitas` agar feed Akunmu tidak 100% hard-selling. | 0.85 |
| **IG9** | **A/B Visual Varian pada Kampanye yang Sama** | Post `4.png` dan `5.png` ("Gacha Brutal Aspirants") punya teks/layout 100% sama, hanya mengganti art karakter; begitu juga `1.png` dan `9.png` (ganti nominal ke-3: 296 DM vs 450 DM) | **4/12 (33%)** | Skill harus mendukung pembuatan >1 variasi (ganti kombinasi 3 nominal atau ganti fokus karakter) dari 1 rencana kampanye. | 0.90 |

---

## E. Deep-Dive `4.png` (dan `5.png`): Mengapa Terasa "Menyatu dengan Game & Seperti Konten Original"?

### 1. Identifikasi Game, Event, dan Karakter pada `4.png` (& `5.png`)
- **Game:** **Mobile Legends: Bang Bang (MLBB)** — karya Moonton.
- **Seri Event / Skin Line:** **The Aspirants** (seri skin bergaya *2D Anime Mecha Sci-Fi* pertama di MLBB dengan efek tampilan 2D cel-shaded dan sulih suara anime Jepang).
- **Karakter Spesifik di `4.png` (The Aspirants Phase 2 — *The Aspirants Unite*):**
  1. **Kiri (Rambut hitam-pink panjang, visor kuning-putih di mata kanan, sabit mekanik putih-kuning):** **Ruby — skin *"Mecha Maiden"***.
  2. **Kanan & Tengah (Rambut pendek pink pastel, telinga mecha kelinci putih-biru, benang energi mekanik + boneka chibi di tengah):** **Angela — skin *"Cyber Cherubin"*** (lengkap dengan boneka *puppet* chibi-nya di bagian tengah di atas logo *THE ASPIRANTS*).
- **Pembanding di `5.png` (The Aspirants Phase 3):**
  - Menampilkan **Chang'e — *"Tech Tensai"*** (kiri, mecha naga putih-biru) dan **Lesley — *"Deadeye Spectre"*** (kanan, mecha hitam-merah).

### 2. Enam Rahasia Desain "In-Game Native Look" pada `4.png`
Mengapa `4.png` terasa seperti pengumuman resmi dari dalam game MLBB, bukan sekadar poster tempelan toko top-up?

| # | Teknik Desain di `4.png` | Analisis Teknis Visual | Cara Reproduksi di Prompt Generator Kita |
|---|---|---|---|
| **N1** | **2.5D Depth Layering (Overlap Antara Karakter & Kotak UI)** | Ujung rambut hitam Ruby dan telinga mecha Angela **menembus/menutupi (overlap)** garis bawah kotak promo `"GRATIS WEEKLY DIAMOND PASS"`. Karakter tidak "ditempel di bawah kotak", melainkan berada di bidang kedalaman (*Z-index*) di antara background, kotak UI, dan logo bawah. | Wajib tulis di prompt: *"2.5D depth layering: character hair, headgear, and weapon tips slightly overlap the bottom border of the glassmorphic promo HUD box, creating authentic depth."* |
| **N2** | **In-Game HUD Container (Chamfered / Beveled Sci-Fi Box, Bukan Kotak Polos)** | Kotak `"GRATIS WEEKLY DIAMOND PASS"` dan header `"GACHA BRUTAL"` berbentuk **panel HUD sci-fi dengan sudut terpotong 45 derajat (*chamfered/angled corners*)**, garis tepi *neon cyan glow* tipis, dan efek kaca *semi-transparan* sehingga gedung sci-fi di belakang tetap tembus pandang. | Ganti istilah *"rounded rectangle card"* menjadi *"translucent chamfered-corner sci-fi HUD panel with thin glowing cyan rim and subtle inner hologram grid"*. |
| **N3** | **2D Anime Cel-Shaded Key Art + Splash Screen Environment** | Karakter dirender dengan gaya **2D Anime Cel-Shading tajam** (garis kontur halus, *specular highlight* pada rambut & mata, bukan 3D plastik/Barat) yang menyatu dengan latar **kota futuristik malam bercahaya biru + laser diagonal** yang persis merupakan *background lobby* event *The Aspirants*. | Sesuaikan *art style* dengan DNA visual seri skin/game: untuk MLBB anime/collector gunakan *"authentic 2D anime cel-shaded splash art style, crisp lineart, luminous anime eyes, integrated with futuristic cyberpunk skyline background"*. |
| **N4** | **Custom Mecha Emblem Frame pada Headline ("GACHA BRUTAL")** | Judul `"GACHA BRUTAL"` dibungkus oleh *banner plate* metalik merah-biru berbentuk heksagonal memanjang yang diapit oleh **2 ikon 3D Diamond miring** di kiri-kanannya — meniru persis *title banner* layar gacha di dalam game. | Gunakan *"metallic esports HUD title banner with angled wings and floating 3D diamond emblems flanking the left and right sides of the headline"*. |
| **N5** | **Ikon Item In-Game Asli dalam Angle Isometrik 3D** | Di sebelah kiri teks `"GRATIS WEEKLY DIAMOND PASS"`, terdapat ikon *Weekly Diamond Pass* (buku/tiket ungu dengan berlian biru dan tab bertuliskan `WEEK`) yang dikelilingi serpihan berlian kecil. | Deskripsikan ikon item secara spesifik sesuai wujud aslinya di dalam game (*"isometric 3D purple-and-gold Weekly Pass booklet with a glowing cyan diamond emblem on the cover"*). |
| **N6** | **Foreground Emblem Anchor di Atas CTA** | Di depan tubuh karakter (antara dada/pinggang dan tombol CTA bawah), terdapat tipografi judul tema bergaya mecha kromatik yang mengunci kaki karakter agar tidak terlihat mengambang. | Tempatkan *thematic event crest / stylized title typography* tepat di atas pill CTA bawah sebagai pengunci komposisi bawah (*foreground anchor*). |

---

## D. Aturan Diferensiasi Wajib (Agar Akunmu Game Tidak Menjadi Kloning Kompetitor)

1. **Dilarang memakai palet kompetitor:** Hindari kombinasi *deep navy-indigo* `#1111a8` + *magenta/crimson outline* (`#E11D48`) pada angka harga dan pita CTA.
2. **Gunakan Signature Look `Akunmu Game`:**
   - Latar: Radial gradient *Electric Sky Blue* `#2A86D6` → *Deep Ocean* `#1A4A7C` → *Midnight* `#121826` (sesuai hero `akungame.id`).
   - Aksen Utama & Harga: *Warm Gold* `#F4B400` & `#FFD86A` (kontras tinggi di atas biru tua, berbeda total dari outline merah kompetitor).
   - Kartu Nominal: Glassmorphic rounded-2xl (`#181D27` 80% opacity) dengan border glow biru muda `#2D9BF0`.
3. **Kejujuran Harga:** Kompetitor memakai format `"Rp29rb-an"` (pembulatan) dan coret harga. `Akunmu Game` menampilkan **harga eksak** dari API (`Rp2.700`, `Rp12.200`, `Rp32.900`) sebagai bukti transparansi.
