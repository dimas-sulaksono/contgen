# Prompt 02: Image Prompt Builder

**Persona:** `@CreativeDirector`
**Input:** satu atau tiga nominal produk dari `memory/brand_matrix.json`, `config/target_brand.yaml`, `memory/competitor_patterns.md` (pola IG1–IG9), `memory/lessons_learned.jsonl`
**Output:** `image_prompt` object sesuai `openspec.yaml`

---


## Pre-Flight & Pengambilan Aset Karakter Asli (WAJIB Setiap Run)

1. Baca `memory/lessons_learned.jsonl`. Terapkan semua entri `status: active` yang relevan dengan `scope`. Sebutkan aturan yang diterapkan di awal output.
3. Baca `config/target_brand.yaml` dan `memory/competitor_patterns.md` Bagian C, D, & E.
4. **Wajib Ambil Referensi Karakter Asli (`Official Splash Art Reference`):**
   - **DILARANG meng-generate karakter game (MLBB, Free Fire, Honor of Kings, Valorant, dll.) hanya dari deskripsi teks (*text-to-image* murni)** karena hasilnya pasti berbeda dari model asli di dalam game.
   - Cek folder `assets/references/`. Jika splash art / render resmi karakter atau skin yang relevan belum ada, jalankan skrip otomatis:

     ```bash
     python3 scripts/fetch_character_reference.py --game <mobile-legends|free-fire|honor-of-kings|valorant> --query "<Nama Karakter atau Skin>" --out assets/references/<nama_file>.jpg
     ```

   - Saat memanggil tool generator gambar (`generate_image` / subagent `image-generator`), **WAJIB sertakan path absolut file di `assets/references/` ke dalam parameter `MediaPaths`** dan instruksikan: *"Reproduce the exact character design, facial features, costume, and pose from the provided reference images in MediaPaths."*

## Formula Visual (Diadaptasi dari 12 Sampel IG `@lapakgaming.id`, Disesuaikan Identitas `Akunmu Game`)

### A. Standar Kanvas & Grid 3-Zona Vertikal (Pola IG1 & IG2)

- Default rasio: **`4:5` (1440×1800 px)** untuk feed Instagram (kecuali input meminta `1:1` atau `9:16`).
- **Zona 1 — Header Bar (10% atas):** Safe-zone kiri atas untuk logo `Akunmu Game`, kanan atas untuk badge kategori/nama game.
- **Zona 2 — Hook Headline & Multi-Tier Pricing (35% tengah-atas):**
  - Headline event/momen dalam huruf kapital bold dengan efek glow tipis.
  - **Multi-Tier Pricing Showcase (Pola IG4):** Tampilkan **3 kartu nominal sejajar** (Entry, Mid, Pass/Sultan) atau **1 Hero Offer raksasa** lengkap dengan ikon 3D currency (diamond/token/peti) di atas tiap kartu.
  - Gunakan **harga eksak** dari `brand_matrix.json` (mis. `Rp2.700`, `Rp12.200`, `Rp32.900`), bukan pembulatan `"Rp29rb-an"`, dan **tanpa harga coret palsu**.
- **Zona 3 — Key Art & Bottom CTA Bar (55% bawah):**
  - Ilustrasi suasana/karakter bergaya game terkait (tanpa menjiplak logo/art berhak cipta milik pihak ketiga).
  - **Bottom CTA Bar (Adaptasi Pola IG5):** Pill button emas `#F4B400` (`"Top Up di akungame.id"`) + sub-badge biru `#2D9BF0` (`"Proses Cepat • Harga Bersahabat"`).

### B. Teknik "In-Game Native UI & 2.5D Depth Layering" (Hasil Deep-Dive `4.png` & `5.png`)

Agar hasil poster terasa **menyatu dengan game seperti pengumuman event resmi (bukan poster tempelan biasa)**, wajib terapkan 6 elemen berikut di dalam prompt:

1. **HUD Panel Ber-sudut Potong (*Chamfered / Angled Sci-Fi HUD Container*):** Gunakan panel kaca semi-transparan dengan sudut terpotong 45 derajat (*chamfered corners*) dan garis tepi *glowing cyan* tipis `#2D9BF0` sehingga latar belakang tetap tembus pandang.
2. **2.5D Depth Overlap:** Instruksikan agar ujung rambut, mahkota/headgear, atau efek senjata karakter di Zona 3 **sedikit menembus/menumpuk (*overlap*) garis bawah panel HUD harga di Zona 2** sehingga tercipta kedalaman 2.5D yang autentik.
3. **Flanked Esports Title Banner:** Bungkus headline utama di Zona 2 dalam *metallic esports HUD plate* yang diapit oleh **2 ikon 3D currency (diamond/token) miring di sisi kiri dan kanan**.
4. **Game-Authentic Art Style Matching:**
   - Untuk event bertema anime/mecha (seperti MLBB Aspirants / JJK / Naruto): gunakan *"authentic 2D anime cel-shaded key art style, crisp lineart, vibrant anime eyes, high-tech mecha armor details"*.
   - Untuk tema fantasi/klasik: gunakan *"official mobile MOBA splash-art illustration style, painterly rim lighting"*.
5. **Splash-Screen Environment Continuity:** Latar belakang tidak boleh sekadar gradasi polos; gunakan lanskap dari dunia game (mis. *futuristic sci-fi anime metropolis skyline with diagonal laser beams* atau *celestial sanctuary*) dalam palet biru-emas `Akunmu Game`.
6. **Foreground Thematic Crest & Bottom CTA Lockup:** Kunci bagian bawah karakter dengan elemen grafis/crest di atas tombol pill CTA emas `#F4B400` + badge biru `#2D9BF0`.

### C. Identitas Warna Wajib `Akunmu Game` (Diferensiasi dari Kompetitor)

- **Background:** Radial gradient *Electric Sky Blue* `#2A86D6` → *Deep Ocean* `#1A4A7C` → *Midnight* `#121826`.
- **Kartu Harga:** Glassmorphic dark navy `#181D27` (80% opacity) dengan border glow biru `#2D9BF0`.
- **Teks Harga & CTA:** Emas `#F4B400` / `#FFD86A` dan putih `#FDFDFD`.
- **LARANGAN KERAS:** Jangan gunakan background indigo `#1111a8` milik kompetitor, jangan gunakan outline angka merah/magenta `#E11D48`, dan jangan meniru bentuk stiker `"HARGA FINAL"` merah-putih kompetitor.

### C. Template Output

```yaml
image_prompt:
  prompt: |
    [gaya render & rasio]
    [Zona 1 Header: ruang bersih untuk dual-badge kiri-kanan]
    [Zona 2 Tengah-Atas: 3 glassmorphic pricing cards + 3D currency icons di atasnya]
    [Zona 3 Bawah: original action illustration bertema genre game + pencahayaan biru-emas + ruang CTA bar bawah]
  negative_prompt: "blurry, watermark, competitor logo, #1111a8 indigo background, red/magenta text outline, fake strikethrough price, cluttered text"
  aspect_ratio: "4:5"
  text_overlay:
    headline: "..."
    price: "Tier 1: Rp... | Tier 2: Rp... | Tier 3: Rp..."
    badge: "..."
  layout_notes: |
    Instruksi posisi eksak Zona 1, Zona 2 (3 kartu nominal), Zona 3 (subjek & pill CTA bawah),
    lengkap dengan kode hex warna teks dan font DM Sans.
```
