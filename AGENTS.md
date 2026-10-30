# Agent Instructions: contgen

Proyek ini membangun skill `social-commerce-content-gen`.

- Meta-prompt utama: [META_PROMPT.md](./META_PROMPT.md)
- Definisi persona: `.agents/personas/*.md`
  (`lead-architect`, `competitive-analyst`, `creative-director`, `qa-critic`, `skill-engineer`)

## Cara memakai persona
1. Saat sebuah langkah di `META_PROMPT.md` menyebut `@Persona`, baca file persona di `.agents/personas/`.
2. Ikuti bagian **Tanggung jawab** dan **Aturan** persona tersebut.
3. Tulis header `### [Persona] <langkah>` setiap pindah persona.
4. Satu persona aktif per langkah. `@QACritic` tidak menilai konten yang dia tulis.

## Aturan global
- Jangan mengarang harga, stok, atau klaim produk. Setiap data punya `source_url` dan `fetched_at`.
- Jangan bypass login. Jangan menyalin aset kompetitor.
- Berhenti di akhir tiap fase dan minta persetujuan user.
