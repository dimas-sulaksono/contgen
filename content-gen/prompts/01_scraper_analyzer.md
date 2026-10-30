# Prompt 01: Scraper & Analyzer (modul ekstraksi)

**Persona:** `@CompetitiveAnalyst`
**Input:** `config/target_brand.yaml`, `config/competitors.yaml`, opsional `inputs/instagram/*`
**Output:** `memory/brand_matrix.json`, `memory/competitor_patterns.md`, `memory/graphify_nodes.json`
**Kontrak:** lihat `openspec.yaml` (`BrandMatrix`, `GraphNode`)

## Langkah
1. Baca `config/competitors.yaml` dan cek `access.status` tiap sumber. Jika `unavailable`, pakai `fallback` yang tertulis.
2. **Target:** ambil halaman target. Jika daftar produk berupa skeleton (render client-side), coba berurutan:
   a. Browser tool yang menunggu render.
   b. Endpoint katalog publik, hanya jika terlihat di sumber halaman.
   c. Input manual dari user (CSV/teks/screenshot).
   Jika semuanya gagal: `source_status: "partial"`, harga `null`, kategori `name_only`. **Jangan menebak.**
3. **Kompetitor web:** catat teks yang terbaca (title, meta, JSON-LD), nama kategori, dan nama aset banner. Tandai bukti yang hanya berupa nama file sebagai confidence <= 0.8.
4. **Kompetitor sosial:** analisis hanya dari `inputs/instagram/` atau sumber yang terbuka tanpa login. Minimal 9 post. Jika kurang, tulis jumlah sebenarnya di laporan.
5. Susun `competitor_patterns.md`: `pola | bukti | frekuensi | relevansi | confidence`.
6. Susun `graphify_nodes.json` dengan rantai `product -> pain_point -> visual_hook -> content_format`. Inferensi diberi `confidence` < 0.7 dan `source` yang menyebut "inference".

## Larangan
- Bypass login, crawling massal, atau menyalin teks/aset kompetitor verbatim.
- Mengisi data yang tidak terlihat. Tulis `NOT AVAILABLE`.

## Self-check sebelum selesai
- [ ] Semua item `brand_matrix.json` punya `source_url` dan `fetched_at`
- [ ] Setiap pola punya kolom bukti
- [ ] Bagian yang tidak tersedia ditandai jelas, beserta cara menyelesaikannya
