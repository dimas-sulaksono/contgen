---
name: social-commerce-content-gen
description: >-
  Generator konten social commerce (Image Generation Prompt + Social Media Caption)
  berbasis bukti katalog produk (akungame.id) dan adaptasi pola anatomi visual/copy
  kompetitor, dilengkapi QA Critic independen serta Self-Learning Reflexion Loop.
triggers:
  - generate konten sosmed
  - buat post instagram top up
  - social commerce content
  - image prompt dan caption akungame
version: 1.0.0
---
# Skill: `social-commerce-content-gen`

Skill ini menghasilkan paket konten media sosial siap posting (**Image Prompt terstruktur + Layout Notes + Caption + QA Report**) untuk brand target yang dikonfigurasi di `./config/target_brand.yaml`.

Seluruh path di dalam dokumen ini bersifat **relatif terhadap folder skill ini** sehingga dapat dipasang tanpa modifikasi di **Antigravity IDE, Claude Code, Hermes, maupun OpenClaw**.

---

## 1. Kontrak Data & Arsitektur Modul

- **Kontrak Input/Output & State:** [`./openspec.yaml`](./openspec.yaml)
- **Konfigurasi Brand & Aturan Warna/Suara:** [`./config/target_brand.yaml`](./config/target_brand.yaml)
- **Konfigurasi Sumber Kompetitor:** [`./config/competitors.yaml`](./config/competitors.yaml)
- **Memori & Knowledge Graph:**
  - [`./memory/brand_matrix.json`](./memory/brand_matrix.json) — Katalog produk & harga IDR terverifikasi
  - [`./memory/competitor_patterns.md`](./memory/competitor_patterns.md) — Pola anatomi web & 12 post Instagram kompetitor
  - [`./memory/graphify_nodes.json`](./memory/graphify_nodes.json) — Relasi `product -> pain_point -> visual_hook -> content_format`
  - [`./memory/lessons_learned.jsonl`](./memory/lessons_learned.jsonl) — Log koreksi permanen (*Reflexion Loop*, append-only)
  - [`./memory/winning_patterns.md`](./memory/winning_patterns.md) — Pola yang terbukti lolos QA dengan skor tinggi / disukai user
- **Pipeline Orkestrasi:** [`./workflows/ruflo_pipeline.yaml`](./workflows/ruflo_pipeline.yaml)

---

## 2. Alur Eksekusi Wajib (`Plan -> Execute -> Critique -> Learn`)

### Langkah 0 — Pre-Flight Check (WAJIB Setiap Run)

Sebelum merancang konten apa pun, agen **WAJIB**:

1. Membaca [`./memory/lessons_learned.jsonl`](./memory/lessons_learned.jsonl) dan menerapkan semua entri dengan `"status": "active"` yang cocok dengan `"scope": "global"` atau `"scope": "product:<slug>"`.
2. Mencantumkan daftar aturan aktif yang diterapkan pada blok `PRE-FLIGHT` di awal output.
3. Membaca [`./memory/brand_matrix.json`](./memory/brand_matrix.json) untuk memverifikasi nama produk, nominal, dan harga eksak. **Dilarang keras mengarang harga, diskon, atau stok.**

### Langkah 1 — Plan (`@CreativeDirector`)

1. Pilih 1 produk (atau 3 tingkatan nominal: *Entry / Mid / Pass* sesuai pola **IG4** di `./memory/competitor_patterns.md`) dari `./memory/brand_matrix.json`.
2. Pilih rantai `product -> pain_point -> visual_hook -> content_format` dari `./memory/graphify_nodes.json`.
3. Tampilkan rencana singkat sebelum men-generate konten.

### Langkah 2 — Execute (`@CreativeDirector`)

1. Jalankan modul [`./prompts/02_image_prompt_builder.md`](./prompts/02_image_prompt_builder.md):
   - Gunakan struktur **3-Zona Vertikal (4:5)** (Header 10%, Hook + Multi-Tier Pricing Cards 35%, Key Art + Bottom Pill CTA 55%).
2. **Ambil Referensi Karakter Asli Game (WAJIB sebelum generate gambar):**
   - Jangan pernah men-generate karakter game (MLBB, Free Fire, HOK, Valorant) hanya dari teks (*text-to-image* murni).
   - Cek `./assets/references/`. Jika belum ada splash art resmi untuk karakter/skin yang dipilih, jalankan:

     ```bash
     python3 ./scripts/fetch_character_reference.py --game <mobile-legends|free-fire|honor-of-kings|valorant> --query "<Nama Karakter/Skin>" --out ./assets/references/<file>.jpg
     ```

3. Jalankan modul [`./prompts/02_image_prompt_builder.md`](./prompts/02_image_prompt_builder.md):
   - Gunakan struktur **3-Zona Vertikal (4:5)** + teknik **In-Game Native UI & 2.5D Depth Layering (`N1`–`N6`)**.
   - Gunakan palet resmi `./config/target_brand.yaml` (`#2D9BF0`, `#F4B400`, `#121826`).
   - Jika tool image generator tersedia di environment agen, tawarkan atau langsung generate gambarnya ke `./samples/`.
   - Saat memanggil generator gambar (`generate_image` / `image-generator`), **WAJIB masukkan file referensi dari `./assets/references/` ke parameter `MediaPaths`** agar model karakter 100% identik dengan aslinya di game.
4. Jalankan modul [`./prompts/03_caption_copywriter.md`](./prompts/03_caption_copywriter.md):
   - Urutan wajib: `Hook (<=125 karakter)` -> `Body (harga eksak + USP resmi)` -> `CTA ke akungame.id` -> `Hashtags (5–12 tag)`.

### Langkah 3 — Critique (`@QACritic`)

1. Evaluasi draf menggunakan [`./prompts/04_critic_evaluator.md`](./prompts/04_critic_evaluator.md) secara independen.
2. Syarat lulus (`passed: true`): rata-rata 6 kriteria `>= 4.0` **dan** tidak ada kriteria `< 3`.
3. Jika gagal, lakukan perbaikan maksimal **3 iterasi**. Simpan hasil akhir ke `./samples/<game_slug>_<product_slug>.md`.

---

## 3. Self-Learning Mechanism (Reflexion Loop)

Skill ini memiliki memori pembelajaran persisten lintas sesi:

1. **Saat User Memberikan Revisi / Koreksi (Post-Feedback Hook):**
   - Ekstrak *root cause* kesalahan (`visual` | `tone` | `factual` | `format` | `other`).
   - Tambahkan (**append**, jangan hapus baris lama) 1 baris JSON ke [`./memory/lessons_learned.jsonl`](./memory/lessons_learned.jsonl) sesuai skema `LessonRecord` di `./openspec.yaml`:

     ```json
     {"timestamp":"ISO-8601","error_type":"visual|tone|factual|format|other","bad_pattern":"...","correction_rule":"...","scope":"global|product:<slug>","status":"active"}
     ```

   - Jika aturan baru menggantikan aturan lama yang bertentangan, ubah `"status"` baris lama menjadi `"superseded"`.
   - Regenerasi konten dan pastikan aturan baru langsung terlihat di bagian `PRE-FLIGHT`.
2. **Saat Konten Lolos QA `>= 4.7` atau Disetujui User:**
   - Catat formula yang berhasil ke [`./memory/winning_patterns.md`](./memory/winning_patterns.md).

---

## 4. Pembaruan Katalog & Pola Kompetitor

Jika user meminta pembaruan data harga atau mengunggah screenshot kompetitor baru ke `./inputs/instagram/`, jalankan modul [`./prompts/01_scraper_analyzer.md`](./prompts/01_scraper_analyzer.md) terlebih dahulu sebelum Langkah 1.
