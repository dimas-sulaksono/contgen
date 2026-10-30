# Agent Instructions: Social Commerce Content Engine

Repositori ini berisi framework multi-agent dan skill terstandarisasi `content-gen` untuk memproduksi konten social commerce game (Image Generation Prompt In-Game HUD + Caption konversi tinggi + QA Report).

Dokumen ini adalah instruksi operasional untuk AI Agent apa pun (**Antigravity IDE, Claude Code, Cursor, VS Code Copilot, Muse, Codex, Open Code, Hermes Agent, OpenClaw**).

---

## 1. Referensi Utama

- **Meta-Prompt Orkestrasi:** [`./META_PROMPT.md`](./META_PROMPT.md)
- **Definisi Skill Utama:** [`./content-gen/SKILL.md`](./content-gen/SKILL.md)
- **Kontrak I/O OpenSpec:** [`./content-gen/openspec.yaml`](./content-gen/openspec.yaml)
- **Daftar Persona:** `.agents/personas/*.md`
  - [`@LeadArchitect`](.agents/personas/lead-architect.md): Arsitektur, schema, pre-flight check, dan brand config.
  - [`@CompetitiveAnalyst`](.agents/personas/competitive-analyst.md): Ekstraksi katalog harga & bedah kompetitor berbukti.
  - [`@CreativeDirector`](.agents/personas/creative-director.md): Pembuat Image Prompt N1–N6 dan copywriting Hook-Body-CTA.
  - [`@QACritic`](.agents/personas/qa-critic.md): Reviewer independen 6 kriteria (hak veto).
  - [`@SkillEngineer`](.agents/personas/skill-engineer.md): Packaging portabel lintas-harness & Reflexion Loop.

---

## 2. Aturan Eksekusi Persona

1. **Peralihan Persona:** Saat menjalankan tugas, tulis header:

   ```markdown
   ### [Persona] <Nama Langkah>
   ```

2. **Satu Persona Aktif:** Eksekusi tugas sesuai *Tanggung Jawab* dan *Aturan* persona tersebut.
3. **Pemisahan Evaluasi:** `@QACritic` **dilarang menilai** konten yang ia buat sendiri. `@CreativeDirector` membuat draft konten, lalu diserahkan ke `@QACritic`.
4. **Hak Veto QA:** Konten hanya dianggap siap jika rata-rata skor QA `>= 4.0` dan tidak ada kriteria `< 3`. Jika gagal, lakukan iterasi perbaikan maksimal 3 kali.

---

## 3. Aturan Data & Integritas Faktual

- **Dilarang Mengarang Harga/Stok:** Seluruh angka harga IDR dan nominal item wajib berasal dari `./content-gen/memory/brand_matrix.json` yang memiliki `source_url` dan `fetched_at`.
- **Aset Karakter Game Asli:** Jangan gunakan *text-to-image* murni untuk karakter berlisensi (MLBB, Free Fire, HOK, Valorant). Gunakan splash art resmi di `./content-gen/assets/references/` atau unduh via `scripts/fetch_character_reference.py`.
- **Etika Kompetitor:** Jangan bypass login, jangan scraping massal, dan **dilarang menyalin verbatim** logo, maskot, atau copywriting kompetitor. Ambil hanya pola strukturalnya.

---

## 4. Reflexion Loop (Self-Learning)

Sebelum membuat konten apa pun, agen wajib melakukan **Pre-Flight Check**:

1. Baca `./content-gen/memory/lessons_learned.jsonl`.
2. Terapkan semua entri dengan `"status": "active"`.
3. Tampilkan aturan aktif yang diterapkan pada blok output `PRE-FLIGHT`.
4. Jika user memberikan revisi, catat akar masalah ke `lessons_learned.jsonl` (*append-only*).
