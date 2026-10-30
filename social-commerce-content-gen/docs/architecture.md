# Architecture & Reproducible Guide: `social-commerce-content-gen`

> **Status:** `v1.0.0 (Stable — Fase 1, 2, dan 3 Selesai)`
> **Dikelola dengan standar skill:** `auto-document` (`@LeadArchitect` & `@SkillEngineer`)

---

## 1. Judul & Konteks

`social-commerce-content-gen` adalah **AI Agent Skill portabel (agent-agnostic)** untuk menghasilkan paket konten media sosial siap posting (**Image Generation Prompt + Layout Overlay + Social Media Caption + QA Report**) bagi **Akunmu Game (`https://akungame.id`)**.

Skill ini memecahkan 3 masalah utama pembuatan konten social commerce:
1. **Halusinasi harga & produk:** Agen dilarang mengarang harga; seluruh angka wajib ditarik dari katalog terverifikasi di `memory/brand_matrix.json` (73 nominal dari 8 game via API publik `https://api.akunmu.net/api/v1`).
2. **Kualitas visual & struktur copy:** Mengadaptasi pola terukur dari situs web dan **12 post Instagram kompetitor (`@lapakgaming.id`)** di `memory/competitor_patterns.md` (kanvas vertikal `4:5`, hierarki 3-Zona, *Multi-Tier Pricing Showcase* 3 kartu sejajar, dan *Bottom Trust CTA*), sambil menjaga diferensiasi identitas warna `Akunmu Game` (`#2D9BF0` + `#F4B400` + `#121826`).
3. **Kesalahan berulang lintas sesi:** Menerapkan **Persistent Reflexion Loop** di `memory/lessons_learned.jsonl` yang wajib dibaca pada tahap *Pre-Flight Check* di setiap eksekusi.

---

## 2. Arsitektur Teknis & Struktur Direktori

```text
social-commerce-content-gen/
├── SKILL.md                          # Entry point universal (Antigravity, Claude, Hermes, OpenClaw)
├── openspec.yaml                     # Kontrak skema I/O, BrandMatrix, GraphNode, LessonRecord
├── config/
│   ├── target_brand.yaml             # Identitas, USP, palet warna, dan aturan konten Akunmu Game
│   └── competitors.yaml              # Sumber referensi kompetitor & kebijakan non-copy
├── inputs/
│   └── instagram/                    # 12 screenshot post IG @lapakgaming.id (1.png - 12.png)
├── memory/
│   ├── brand_matrix.json             # 8 game & 73 nominal harga terverifikasi (api.akunmu.net)
│   ├── competitor_patterns.md        # 4 pola web (W1-W4) + 9 pola visual IG (IG1-IG9)
│   ├── graphify_nodes.json           # Knowledge graph: product -> pain_point -> visual_hook -> format
│   ├── lessons_learned.jsonl         # Append-only Reflexion Loop log (4 aturan aktif)
│   └── winning_patterns.md           # Formula visual & copy yang lolos QA >= 4.7/5.0
├── prompts/
│   ├── 01_scraper_analyzer.md        # Modul ekstraksi katalog & analisis kompetitor (@CompetitiveAnalyst)
│   ├── 02_image_prompt_builder.md    # Modul generator visual 3-Zona 4:5 (@CreativeDirector)
│   ├── 03_caption_copywriter.md      # Modul copywriting Hook-Body-CTA-Hashtag (@CreativeDirector)
│   └── 04_critic_evaluator.md        # Modul QA independen 6 kriteria (@QACritic)
├── workflows/
│   └── ruflo_pipeline.yaml           # State machine: preflight -> plan -> execute -> critique -> output
├── samples/
│   ├── mobile-legends_5-diamond.md   # Sampel 1 (MLBB 3-Tier: Rp2.700 / Rp12.200 / WDP Rp32.900, QA 4.8)
│   └── free-fire_10-diamond.md       # Sampel 2 (FF 3-Tier: Rp3.000 / Rp9.700 / Rp22.400, QA 4.8)
└── docs/
    └── architecture.md               # Dokumentasi arsitektur & panduan reproduksi ini
```

### Pemetaan Persona (`.agents/personas/*.md`)
- **`@LeadArchitect`**: Struktur direktori, kontrak `openspec.yaml`, dan konfigurasi brand.
- **`@CompetitiveAnalyst`**: Ekstraksi katalog API & pembedahan 12 post Instagram kompetitor.
- **`@CreativeDirector`**: Perancangan prompt visual `4:5`, copywriting, dan eksekusi sampel.
- **`@QACritic`**: Evaluasi independen 6 kriteria (minimal rata-rata `4.0`, tanpa kriteria `< 3`).
- **`@SkillEngineer`**: Pemaketan `SKILL.md` lintas-harness, *Reflexion Loop*, dan dokumentasi.

### Tooling & Deviasi yang Dicatat
| Kebutuhan | Primary di Meta-Prompt | Yang Digunakan di Repo |
|---|---|---|
| Struktur direktori | `workspace-manager` | Dibangun modular sesuai spesifikasi |
| Dokumentasi | `auto-docs` | Skill `auto-document` |
| Kontrak skema | `openspec` | Skema OpenSpec 1.0 + JSON Schema di `openspec.yaml` |
| Ekstraksi katalog | `understand-anything` | Fetch langsung ke API publik `https://api.akunmu.net/api/v1/topup/*` + analisis 12 screenshot IG |
| Knowledge graph | `graphify` | `memory/graphify_nodes.json` (16 node, 6 rantai lengkap) |
| Orkestrasi pipeline | `ruflo` + `superpower` | `workflows/ruflo_pipeline.yaml` (`preflight -> plan -> execute -> critique -> output`) |

---

## 3. Panduan Reproduksi & Instalasi Lintas Agent Harness

### A. Pemasangan di Antigravity IDE / Claude Code
Salin atau buat symlink folder `social-commerce-content-gen` ke direktori skill workspace atau global:

```bash
# Opsi 1: Pasang di level Workspace (direkomendasikan agar terbawa di Git)
mkdir -p .agents/skills
ln -s "$(pwd)/social-commerce-content-gen" .agents/skills/social-commerce-content-gen

# Opsi 2: Pasang untuk Claude Code
mkdir -p .claude/skills
ln -s "$(pwd)/social-commerce-content-gen" .claude/skills/social-commerce-content-gen
```

Cara memanggil di chat:
> *"Gunakan skill `social-commerce-content-gen` untuk membuat konten feed 4:5 game Honor Of Kings dengan angle push rank."*

### B. Pemasangan di Hermes / OpenClaw
1. Daftarkan kontrak input/output menggunakan `social-commerce-content-gen/openspec.yaml`.
2. Arahkan orchestrator state machine ke `social-commerce-content-gen/workflows/ruflo_pipeline.yaml`.
3. Pastikan working directory eksekusi berada di dalam `social-commerce-content-gen/` agar seluruh path relatif (`memory/*`, `prompts/*`, `config/*`) terbaca langsung.

### C. Perintah Reproduksi Pembaruan Katalog Produk (`brand_matrix.json`)
Jika ingin menyegarkan harga langsung dari API publik `Akunmu Game`:

```bash
curl -s "https://api.akunmu.net/api/v1/topup/games" | python3 -m json.tool | head -n 30
```

### D. Perintah Validasi Integritas Skill (Quality Gate Check)
Jalankan perintah berikut dari root repositori untuk memastikan seluruh file JSON, JSONL, YAML, dan rantai Knowledge Graph valid:

```bash
python3 -c '
import json
base = "social-commerce-content-gen/"
for f in ["memory/brand_matrix.json", "memory/graphify_nodes.json"]:
    json.load(open(base + f))
    print("OK JSON:", f)
with open(base + "memory/lessons_learned.jsonl") as fh:
    lines = [json.loads(line) for line in fh if line.strip()]
    print("OK JSONL: memory/lessons_learned.jsonl ->", len(lines), "active rules")
g = json.load(open(base + "memory/graphify_nodes.json"))
ids = {n["id"] for n in g["nodes"]}
assert all(all(i in ids for i in c) for c in g["complete_chains"])
print("OK Graph Chains:", len(g["complete_chains"]))
'
for f in openspec.yaml config/target_brand.yaml config/competitors.yaml workflows/ruflo_pipeline.yaml; do
  ruby -ryaml -e "YAML.load_file(ARGV[0]); puts %(OK YAML: #{ARGV[0]})" "social-commerce-content-gen/$f"
done
```
