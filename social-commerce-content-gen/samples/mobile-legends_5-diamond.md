# Sampel 01 — Mobile Legends: Multi-Tier Push Rank & Weekly Diamond Pass
# Dihasilkan oleh @CreativeDirector | Dievaluasi oleh @QACritic
# Benchmark Visual: 12 Post Instagram @lapakgaming.id (Pola IG1, IG2, IG4, IG5, IG6)

---

## INPUT
```yaml
product_url: https://akungame.id/topup/mobile-legends
selected_tiers:
  - {id: "a312d282-9e85-462a-97a8-1def10535f58", label: "5 Diamond", price_idr: 2700}
  - {id: "a3188ea7-0313-44b8-8387-a5efd1cfbbc1", label: "34 Diamond", price_idr: 12200}
  - {id: "a312d282-a06d-46ea-b385-595a2dbb090e", label: "Weekly Diamond Pass", price_idr: 32900}
fetched_at: "2026-10-30T21:09:02+07:00"
content_format: feed_4x5
campaign_angle: promo_event_push_rank
```

## PRE-FLIGHT
- `memory/lessons_learned.jsonl`: telah diperiksa (semua aturan aktif diterapkan).
- `config/target_brand.yaml`: palet `#2D9BF0` / `#F4B400` / `#121826`, font DM Sans.
- `memory/competitor_patterns.md`: menerapkan pola **IG1 (4:5)**, **IG2 (3-Zona Vertikal)**, **IG4 (3-Column Multi-Tier Pricing + 3D Icons)**, dan **IG5 (Bottom CTA + Trust Sub-badge)**.

---

## OUTPUT: IMAGE PROMPT

```yaml
image_prompt:
  prompt: |
    Vertical 4:5 social commerce gaming promo poster (1440x1800 px), clean 3-zone vertical hierarchy, high-contrast digital illustration with 3D UI elements.
    BACKGROUND: Radial gradient from Electric Sky Blue (#2A86D6) at upper-center to Deep Ocean (#1A4A7C) and Midnight Navy (#121826) at edges, with subtle glowing hexagonal esports grid and golden light rays.
    ZONE 1 (Top 10% Header): Clean dark-blue top margin with left and right corner safe zones for brand and game category badges.
    ZONE 2 (Upper-Middle 35% Hook & 3-Tier Showcase):
      - Center-top reserved space for bold 2-line headline with soft cyan outer glow.
      - Below headline: 3 equal-width glassmorphic rounded-2xl cards (#181D27 at 80% opacity, glowing #2D9BF0 border) arranged horizontally in 3 columns.
      - Floating above Card 1 (left): a single 3D glowing cyan diamond crystal.
      - Floating above Card 2 (center): a cluster of 3D glowing cyan diamonds with gold sparkles.
      - Floating above Card 3 (right): a 3D purple-and-gold Weekly Diamond Pass ticket chest with radiant aura.
    ZONE 3 (Bottom 55% Key Art & CTA Bar):
      - Dynamic original fantasy MOBA hero duo (an agile cyber-assassin with glowing blue energy blades on the left and a golden-armored mage casting an arcane orb on the right, original non-copyrighted character designs) emerging from blue energy flames.
      - Bottom-center reserved flat dark-gradient strip for a rounded-full gold CTA pill (#F4B400) and a connected sky-blue trust tag (#2D9BF0).
    Lighting: cinematic rim light in cyan (#2D9BF0) and warm gold (#F4B400), crisp 4K render, no gibberish text inside image.

  negative_prompt: >
    blurry, low resolution, gibberish text, watermark, competitor logo, Lapakgaming logo,
    copyrighted MLBB logo, #1111a8 indigo background, red or magenta price outline,
    fake strikethrough prices, cluttered layout, dull grey tones

  aspect_ratio: "4:5"

  text_overlay:
    headline: "SIAP PUSH RANK & GACHA SKIN BARU?"
    price: "5 DM: Rp2.700 | 34 DM: Rp12.200 | WDP: Rp32.900"
    badge: "HARGA EKSAK • TANPA BIAYA TERSEMBUNYI"

  layout_notes: |
    - Zona 1 (Atas, Y: 0%–10%): Kiri atas logo "Akunmu Game" (/static/akunmu-tech.png), kanan atas pill badge biru "#2D9BF0" bertuliskan "MOBILE LEGENDS".
    - Zona 2 (Tengah-Atas, Y: 10%–45%):
      * Headline "SIAP PUSH RANK & GACHA SKIN BARU?" (DM Sans ExtraBold, putih #FDFDFD, aksen kuning #FFD86A pada kata "GACHA SKIN BARU").
      * Subheadline: "Pilih nominal sesuai kebutuhanmu — langsung masuk ke akun!"
      * 3 Kartu Harga Sejajar (Pola IG4):
        - Kartu Kiri: pill label biru "5 Diamond" -> angka besar emas (#F4B400) "Rp2.700"
        - Kartu Tengah: pill label biru "34 Diamond" -> angka besar emas (#F4B400) "Rp12.200"
        - Kartu Kanan: pill label emas "Weekly Diamond Pass" -> angka besar emas (#F4B400) "Rp32.900"
    - Zona 3 (Bawah, Y: 45%–100%):
      * Key art 2 karakter MOBA di Y: 48%–88%.
      * Bottom CTA Bar di Y: 88%–95%: Tombol pill emas (#F4B400, teks hitam bold) "Top Up di akungame.id" berdampingan dengan badge perisai biru (#2D9BF0, teks putih) "HARGA EKSAK • CEPAT MASUK".
```

---

## OUTPUT: CAPTION

```text
Mau gacha skin atau push rank MLBB malam ini? Top up mulai Rp2.700, langsung masuk! ⚡

Pilih nominal favoritmu dengan harga jujur di Akunmu Game:
✅ 5 Diamond Mobile Legends — Rp2.700
✅ 34 Diamond Mobile Legends — Rp12.200
✅ Weekly Diamond Pass (WDP) — Rp32.900
🛡️ Pembayaran mudah, transaksi aman, dan admin siap bantu 06.00–00.00 WIB

Langsung pilih nominal dan gas main di akungame.id 👉

#AkunmuGame #AkunmuID #MobileLegends #MLBB #TopUpMLBB #WeeklyDiamondPass #DiamondMLBB #PushRank #GasMain #GamingIndonesia
```

## GROUNDING
```yaml
grounding:
  product_source_url: https://akungame.id/topup/mobile-legends
  price_fetched_at: "2026-10-30T21:09:02+07:00"
```

---

## QA REPORT — @QACritic

```yaml
qa_report:
  score: 4.8
  passed: true
  criteria_scores:
    faktual: 5
    brand_fit: 5
    daya_tarik_visual: 5
    copy: 5
    kepatuhan: 5
    format: 4
  issues:
    - "Format (4/5): Teks pada 3 kartu harga cukup padat untuk layar kecil; pastikan angka 'Rp2.700', 'Rp12.200', dan 'Rp32.900' memakai ukuran font minimal 2.2x dari label item."
  benchmark_note: >
    Mengadopsi struktur 3-Zona 4:5 (IG1, IG2) dan 3-Column Multi-Tier Pricing (IG4: 1.png, 9.png, 12.png)
    serta Bottom Trust CTA (IG5), namun 100% memakai palet biru-emas Akunmu Game dan harga eksak tanpa pembulatan.
  iteration: 2
```
