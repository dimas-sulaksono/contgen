# Architecture & Reproducible Guide: `content-gen`

> **Status:** `v1.1.0 (Stable — Refactored to content-gen & Multi-Harness Universal Support)`
> **Dikelola dengan standar skill:** `auto-document` (`@LeadArchitect` & `@SkillEngineer`)

---

## 1. Judul & Konteks

`content-gen` (sebelumnya `social-commerce-content-gen`) adalah **AI Agent Skill portabel (agent-agnostic)** untuk memproduksi paket konten media sosial siap posting (**Image Generation Prompt In-Game HUD + Layout Overlay + Social Media Caption + QA Report**) untuk brand target **Akunmu Game (`https://akungame.id`)** atau brand kustom lainnya.

### Masalah yang Diselesaikan

1. **Halusinasi harga & nominal voucher:** Seluruh data wajib ditarik dari katalog terverifikasi di [`memory/brand_matrix.json`](../memory/brand_matrix.json) yang memiliki `source_url` dan timestamp `fetched_at`.
2. **Kualitas visual & struktur copy:** Mengadopsi formula teruji dari 12 post Instagram kompetitor (`@lapakgaming.id`) di [`memory/competitor_patterns.md`](../memory/competitor_patterns.md) menggunakan kanvas vertikal `4:5`, hierarki 3-Zona (*Esports HUD Header*, *3-Tier Pricing Cards*, dan *Bottom Pill Trust CTA*), dengan standar prompt **In-Game Native UI & 2.5D Depth Layering (`N1`–`N6`)**.
3. **Penyimpangan Model Karakter Berlisensi:** Menghindari halusinasi karakter game dengan mengintegrasikan pengunduh otomatis aset resmi Fandom Wiki API via [`scripts/fetch_character_reference.py`](../../scripts/fetch_character_reference.py) ke dalam parameter `MediaPaths`.
4. **Kesalahan Berulang Lintas Sesi:** Menerapkan **Persistent Reflexion Loop** di [`memory/lessons_learned.jsonl`](../memory/lessons_learned.jsonl) yang wajib dibaca pada tahap *Pre-Flight Check* di setiap eksekusi.
5. **Kesiapan Eksekusi Lintas Model/Harness:** Pengguna Claude Code, Antigravity, Cursor, VS Code Copilot, Muse, Codex, Open Code, Hermes Agent, dan OpenClaw dapat langsung mengkloning dan menjalankannya tanpa konfigurasi manual.

---

## 2. Arsitektur Teknis & Struktur Direktori

```text
contgen/
├── META_PROMPT.md                    # Universal Orchestration Meta-Prompt (Mode 1 & Mode 2)
├── AGENTS.md                         # Instruksi agen & aturan eksekusi persona
├── CLAUDE.md                         # Konfigurasi workspace otomatis Claude Code
├── .cursorrules                      # Aturan asisten Cursor & Windsurf
├── .github/copilot-instructions.md   # Aturan asisten VS Code Copilot
├── .agents/
│   ├── personas/                     # 5 Definisi Persona (@LeadArchitect, dll.)
│   └── skills/                       # Symlink: content-gen -> ../../content-gen
├── .claude/skills/                   # Symlink: content-gen -> ../../content-gen
├── scripts/
│   ├── validate_system.py            # CLI validator integritas skema & memori
│   └── fetch_character_reference.py  # Skrip pengunduh aset resmi MediaWiki (cross-platform)
└── content-gen/                      # Paket skill utama (relatif & portabel)
    ├── SKILL.md                      # Entry point universal
    ├── openspec.yaml                 # Kontrak OpenSpec 1.0 (I/O & validasi skema)
    ├── config/
    │   ├── target_brand.yaml         # Identitas, USP, palet warna, dan aturan konten
    │   └── competitors.yaml          # Sumber referensi kompetitor
    ├── inputs/instagram/             # 12 screenshot post IG kompetitor (1.png - 12.png)
    ├── memory/
    │   ├── brand_matrix.json         # 8 game & 73 nominal harga terverifikasi
    │   ├── competitor_patterns.md    # 4 pola web + 9 pola visual Instagram terbedah
    │   ├── graphify_nodes.json       # Knowledge graph: product -> pain_point -> hook -> format
    │   ├── lessons_learned.jsonl     # Append-only Reflexion Loop log
    │   └── winning_patterns.md       # Formula konten yang lolos QA >= 4.7
    ├── prompts/
    │   ├── 01_scraper_analyzer.md    # Ekstraksi & analisis kompetitor (@CompetitiveAnalyst)
    │   ├── 02_image_prompt_builder.md# Generator visual In-Game HUD N1-N6 (@CreativeDirector)
    │   ├── 03_caption_copywriter.md  # Copywriting Hook-Body-CTA (@CreativeDirector)
    │   └── 04_critic_evaluator.md    # QA independen 6 kriteria (@QACritic)
    ├── workflows/
    │   └── ruflo_pipeline.yaml       # State machine orkestrasi plan-execute-critique
    ├── samples/                      # Bukti hasil generate konten & evaluasi QA
    └── docs/
        └── architecture.md           # Dokumentasi teknis arsitektur ini
```

### Pembagian Peran 5 Persona Multi-Agent

- **`@LeadArchitect`**: Arsitektur, integritas kontrak OpenSpec, pre-flight check, dan brand config.
- **`@CompetitiveAnalyst`**: Katalog berbasis bukti (`brand_matrix.json`) dan reverse-engineering kompetitor.
- **`@CreativeDirector`**: Perancangan prompt visual `4:5` (N1–N6), copywriting, dan eksekusi draf.
- **`@QACritic`**: Penilai independen 6 kriteria dengan hak veto (skor $\ge 4.0$, kriteria $< 3$ dilarang lolos).
- **`@SkillEngineer`**: Pemaketan skill lintas-harness, *Reflexion Loop*, dan dokumentasi arsitektur.

---

## 3. Panduan Reproduksi & Setup Lintas Lingkungan (Reproducible Guide)

### A. Persiapan Lingkungan Awal (Zero-to-Hero)

```bash
# 1. Masuk ke direktori proyek
cd /path/to/contgen

# 2. Pastikan symlink skill terpasang untuk Antigravity dan Claude Code
mkdir -p .agents/skills .claude/skills scripts
ln -sf ../../content-gen .agents/skills/content-gen
ln -sf ../../content-gen .claude/skills/content-gen
ln -sf ../content-gen/scripts/validate_system.py scripts/validate_system.py
ln -sf ../content-gen/scripts/fetch_character_reference.py scripts/fetch_character_reference.py

# 3. Jalankan pengujian integritas pra-terbang
python3 scripts/validate_system.py
```

### B. Cara Penggunaan Berdasarkan Host / Model AI

1. **Antigravity IDE:**
   Ketik perintah di chat IDE:
   > *"Gunakan skill `content-gen` untuk membuat postingan feed 4:5 promo Mobile Legends Weekly Diamond Pass."*

2. **Claude Code CLI:**
   Jalankan dari terminal:

   ```bash
   claude "Jalankan META_PROMPT.md: buat konten promo Honor of Kings 80 Tokens angle push rank weekend."
   ```

3. **Cursor / VS Code Copilot / Muse / Codex / Open Code:**
   Buka panel chat asisten di editor, salin prompt berikut:

   ```text
   Ikuti META_PROMPT.md dalam repositori ini. Bertindaklah sebagai Meta-Orchestrator dan jalankan Mode 1 untuk produk: Free Fire 10 Diamond. Tampilkan hasil Image Prompt N1-N6, Caption, dan QA Critic Report.
   ```

4. **Hermes Agent / OpenClaw / Headless Pipeline:**
   Arahkan kontrak I/O ke `content-gen/openspec.yaml` dan alur state machine ke `content-gen/workflows/ruflo_pipeline.yaml`.

### C. Pengunduhan Aset Karakter Game Asli (Cross-Platform)

Skrip `fetch_character_reference.py` mendukung Linux, macOS, dan Windows (otomatis normalisasi format via Pillow, macOS `sips`, atau binary copy):

```bash
# Contoh: Mengunduh splash art resmi untuk Honor of Kings
python3 scripts/fetch_character_reference.py \
  --game honor-of-kings \
  --query "Satoru Gojo" \
  --out content-gen/assets/references/hok_gojo.jpg

# Contoh: Mengunduh splash art resmi untuk Mobile Legends
python3 scripts/fetch_character_reference.py \
  --game mobile-legends \
  --query "Ruby Mecha Maiden" \
  --out content-gen/assets/references/mlbb_ruby.jpg
```

### D. Perintah Validasi Integritas Sistem (Quality Gate Check)

Jalankan perintah ini kapan saja untuk memverifikasi seluruh komponen data, schema, dan memori tetap valid:

```bash
python3 scripts/validate_system.py
```

Output yang diharapkan adalah `🎉 ALL QUALITY GATES PASSED!`.
