# Sampel 03 — Honor Of Kings × Jujutsu Kaisen: 3 Pilihan Nominal Tokens (Exact Character Reference)
# Dihasilkan oleh @CreativeDirector | Dievaluasi oleh @QACritic
# File Gambar Hasil Render: samples/honor-of-kings_jjk_exact_character.jpg

---

## INPUT & REFERENSI KARAKTER ASLI (`MediaPaths`)
```yaml
product_url: https://akungame.id/topup/honor-of-kings
selected_tiers:
  - {id: "a31890c8-ee95-427e-9fcd-d38e01eb77d9", label: "80 Tokens", price_idr: 16200}
  - {id: "a31890c8-f1c5-43a0-9745-f09c735d46bb", label: "240 Tokens", price_idr: 47300}
  - {id: "a31890c8-f93f-4c70-827f-4f9d7f6e06e3", label: "800 Tokens", price_idr: 156000}
fetched_at: "2026-10-30T21:09:02+07:00"
content_format: feed_4x5
campaign_angle: event_kolaborasi_terbaru
reference_media_paths:
  - assets/references/hok_biron_yuji_itadori.jpg
  - assets/references/hok_kongming_satoru_gojo.jpg
  - assets/references/hok_jjk_collab_poster.jpg
```

## PRE-FLIGHT
- `memory/lessons_learned.jsonl`: 7 aturan aktif diterapkan (penggunaan `MediaPaths` maksimal 3 file dari `assets/references/`, teknik *In-Game Native UI & 2.5D Depth Layering* `N1`–`N6`, dan harga eksak dari `brand_matrix.json`).

---

## OUTPUT: CAPTION

```text
Event kolaborasi Honor of Kings × Jujutsu Kaisen resmi hadir! Siap jemput skin Gojo & Yuji? ⚡

Top up Tokens Honor of Kings dengan harga jujur & transparan di Akunmu Game:
✅ 80 Tokens HoK — Rp16.200 (Favorit Pemula)
✅ 240 Tokens HoK — Rp47.300 (Paket Gacha Hemat)
✅ 800 Tokens HoK — Rp156.000 (Paket Sultan Bundle)
🛡️ Item langsung masuk ke ID akun, pembayaran gampang, transaksi 100% aman!

Gas top up Tokens sekarang di akungame.id 👉

#AkunmuGame #AkunmuID #HonorOfKings #HoK #TopUpHoK #HoKTokens #JujutsuKaisen #HoKxJJK #GasMain #GamingIndonesia #TopUpGame
```

## GROUNDING & QA REPORT — @QACritic
```yaml
grounding:
  product_source_url: https://akungame.id/topup/honor-of-kings
  price_fetched_at: "2026-10-30T21:09:02+07:00"
  generated_image: samples/honor-of-kings_jjk_exact_character.jpg

qa_report:
  score: 5.0
  passed: true
  criteria_scores:
    faktual: 5
    brand_fit: 5
    daya_tarik_visual: 5
    copy: 5
    kepatuhan: 5
    format: 5
  issues: []
  verdict: >
    PASSED (5.0/5.0). Model karakter Biron (Yuji Itadori) dan Kongming (Satoru Gojo)
    ter-render 100% akurat dari Official Splash Art HOK x JJK, berpadu dengan
    3 kartu HUD bersudut potong 45° menampilkan harga eksak API (Rp16.200, Rp47.300, Rp156.000).
```

