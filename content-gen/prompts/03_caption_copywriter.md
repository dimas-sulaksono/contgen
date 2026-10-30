# Prompt 03: Caption Copywriter

**Persona:** `@CreativeDirector`
**Input:** produk dari `brand_matrix.json`, `config/target_brand.yaml`, `memory/competitor_patterns.md`, `memory/lessons_learned.jsonl`
**Output:** `caption` object sesuai `openspec.yaml`

---

## Pre-Flight (wajib)
Baca `memory/lessons_learned.jsonl`. Terapkan aturan `status: active`.

## Formula Caption

### Struktur 4 bagian (WAJIB urut)
```
[HOOK]
[BODY]
[CTA]
[HASHTAGS]
```

### HOOK (baris 1 — maks 125 karakter)
- Tujuan: buat orang berhenti scroll dalam 1 detik
- Pola pilihan (pilih SATU, variasikan per konten):
  | Pola | Contoh |
  |---|---|
  | Angka + benefit | "Top up 5 Diamond MLBB mulai Rp2.700 — langsung masuk!" |
  | Pertanyaan relevan | "Mau push rank tapi diamond abis?" |
  | FOMO / urgensi | "Jangan ketinggalan event MLBB — top up sekarang" |
  | Social proof | "Ribuan gamer udah top up di Akunmu — giliran kamu" |
- Register: santai, "kamu"-form, bahasa gamer
- Jangan pakai klaim tak terukur ("termurah", "terbaik", "garansi X lipat") tanpa dasar dari `brand_matrix.json`

### BODY (2–4 baris)
Isi: nama produk PERSIS dari `brand_matrix.json` + harga PERSIS + 2-3 USP dari `target_brand.yaml`
Template:
```
✅ [Nama produk] — Rp[harga persis]
⚡ [USP 1 dari situs, mis. "Item cepat masuk"]
🛡️ [USP 2, mis. "Pembayaran mudah & transaksi aman"]
👥 [USP 3 opsional, mis. "Bisa top up buat teman juga"]
```

### CTA (1 baris)
- Wajib mengarah ke `akungame.id`
- Contoh: "Top up sekarang di **akungame.id** 👉" atau "Kunjungi akungame.id untuk pilih nominal"
- Jangan tulis URL kompetitor

### HASHTAGS (5–12 tag)
Kombinasi:
- Brand: `#AkunmuGame` `#AkunmuID` `#TopUpAkunmu`
- Game spesifik: `#MobileLegends` `#MLBB` `#FreeFire` dll.
- Kategori: `#TopUpDiamond` `#TopUpMurah` `#TopUpGame`
- Gamer culture: `#PushRank` `#GasMain` `#GamingIndonesia`

## Larangan
- Harga hanya dari `brand_matrix.json`. Dilarang mengarang.
- Jangan menyebut nama/akun kompetitor
- Jangan klaim "termurah", "garansi", "no 1" tanpa bukti
- Emoji boleh, tapi maks 3 jenis berbeda per caption
