# Sampel 04 — Dragon Nest M Classic: Raid Green Dragon Nest & 3 Pilihan Cash Pack (Exact Character Reference)
# Dihasilkan oleh @CreativeDirector | Dievaluasi oleh @QACritic
# File Gambar Hasil Render: samples/dragon-nest_green-dragon_exact_character.jpg

---

## INPUT & REFERENSI KARAKTER ASLI (`MediaPaths`)
```yaml
product_url: https://akungame.id/topup/dragon-nest-m-classic
selected_tiers:
  - {id: "a31690a1-1a72-4fd4-a82c-82963581bee2", label: "626 (600+26) Cash Pack", price_idr: 13400}
  - {id: "a31690a1-1d43-49f9-9650-74880bef17c0", label: "3130 (3000+130) Cash Pack", price_idr: 66000}
  - {id: "a31690a1-2016-4a54-8a67-9edf362231d4", label: "6366 (6000+366) Cash Pack", price_idr: 133600}
fetched_at: "2026-10-30T21:09:02+07:00"
content_format: feed_4x5
campaign_angle: event_raid_terbaru_green_dragon
reference_media_paths:
  - assets/references/dn_classic_keyart.jpg
  - assets/references/dn_argenta_velskud.png
  - assets/references/dn_warrior.png
```

## PRE-FLIGHT
- `memory/lessons_learned.jsonl`: 7 aturan aktif diterapkan:
  1. Penggunaan `MediaPaths` maksimal 3 file dari `assets/references/` (resmi Argenta, Velskud, dan Warrior).
  2. Teknik *In-Game Native UI & 2.5D Depth Layering* `N1`–`N6` (HUD glassmorphism chamfered 45°, overlap jubah Argenta ke kartu HUD, aksen neon cyan dan kristal cash 3D).
  3. Harga eksak dari `brand_matrix.json` (Rp13.400, Rp66.000, Rp133.600 — dilarang membulatkan atau memakai harga coret).
  4. Penempatan nama game dalam 3–5 kata pertama pada kalimat Hook caption.

---

## OUTPUT: CAPTION

```text
Dragon Nest M Classic menghadirkan Raid Green Dragon Nest! Siap bawa tim kamu taklukkan dungeon legendaris ini? 🐉🔥

Perkuat gear & persiapkan Cash Pack kamu sekarang di Akunmu Game dengan harga jujur & transparan:
✅ 626 Cash Pack — Rp13.400 (Entry Hemat & Potion Stock)
✅ 3130 Cash Pack — Rp66.000 (Paling Populer & Raid Ready)
✅ 6366 Cash Pack — Rp133.600 (Paket Sultan Dragon Slayer)
🛡️ Format tujuan [UID]|[Server], proses instan detikan, 100% legal & transaksi aman!

Amankan Cash Pack kamu sekarang di akungame.id 👉

#AkunmuGame #AkunmuID #DragonNestMClassic #DNMClassic #DragonNest #TopUpDragonNest #GreenDragonNest #Argenta #CashPackDNM #RaidDragonNest #GamingIndonesia #TopUpGameMurah
```

## GROUNDING & QA REPORT — @QACritic
```yaml
grounding:
  product_source_url: https://akungame.id/topup/dragon-nest-m-classic
  price_fetched_at: "2026-10-30T21:09:02+07:00"
  generated_image: samples/dragon-nest_green-dragon_exact_character.jpg

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
    PASSED (5.0/5.0). Visual karakter Argenta (jubah merah, rambut perak, sepatu bot merah)
    dan Warrior ter-render akurat berbasis aset resmi DNM Classic. Panel HUD 3 kartu sejajar
    bersudut potong 45° menampilkan nominal dan harga eksak dari brand_matrix.json
    (Rp13.400, Rp66.000, Rp133.600). Identitas brand Akunmu Game konsisten dengan palet
    Electric Sky Blue (#2D9BF0) dan Royal Gold (#F4B400).
```

