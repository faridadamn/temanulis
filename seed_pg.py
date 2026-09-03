import json
import subprocess

SEED_ITEMS = [
    {
        "title": "[Affiliate] Hook Viral Skincare / Gadget FYP",
        "type": "Input",
        "category": "Affiliate",
        "tags": ["#video", "#terbukti", "#highCR"],
        "stars": 5,
        "status": "Winner",
        "sections": [
            {"name": "Hook", "items": ["Stop scroll kalau muka kamu masih sering bruntusan pas bangun tidur!", "Nyesel banget baru tahu rahasia ini setelah habis jutaan beli skincare mahal.", "Barang 30 ribuan ini bikin konten kreator heboh satu TikTok!"]},
            {"name": "Problem", "items": ["Udah coba berbagai produk tapi bruntusan tetap balik lagi.", "Kulit sensitif gampang merah dan pori-pori kelihatan jelas."]},
            {"name": "Agitate", "items": ["Makin ditutup make-up tebal, makin parah radangnya dan bikin nggak pede ketemu orang."]},
            {"name": "Solution", "items": ["Kuncinya bukan gonta-ganti cream, tapi perbaiki skin barrier dulu pakai formula ceramide murni ini."]},
            {"name": "Fitur", "items": ["Tekstur seringan air, cepat meresap tanpa lengket.", "Aman buat kulit berjerawat dan bumil friendly.", "BPOM approved dan sudah dermatologically tested."]},
            {"name": "CTA", "items": ["Klik keranjang kuning di pojok kiri bawah sebelum kehabisan flash sale!", "Cek link di bio no. 14 selagi diskon 40% masih aktif!"]}
        ]
    },
    {
        "title": "[Produk Digital] Launching Ebook/Course Freelance",
        "type": "Input",
        "category": "Produk Digital",
        "tags": ["#softSell", "#terbukti"],
        "stars": 5,
        "status": "Winner",
        "sections": [
            {"name": "Hook", "items": ["Cara saya dapat klien luar negeri pertama senilai $500 tanpa pengalaman sama sekali.", "Gaji UMR tapi pengen punya penghasilan sampingan dollar dari kamar tidur?"]},
            {"name": "Problem", "items": ["Bingung mulai dari mana, skill pas-pasan, dan nggak tahu cara bidding di platform freelance."]},
            {"name": "Agitate", "items": ["Waktu habis scrolling lowongan tanpa pernah di-hire, sementara orang lain udah kerja dari cafe."]},
            {"name": "Solution", "items": ["Panduan 'Freelance Blueprint': Roadmap langkah demi langkah mulai dari bikin portofolio killer sampai negosiasi harga."]},
            {"name": "Fitur", "items": ["12 Modul video praktis + 5 template proposal siap copy-paste.", "Akses grup support privat seumur hidup.", "Studi kasus live pitching klien asli."]},
            {"name": "Offer", "items": ["Harga normal Rp 399.000, khusus 50 pendaftar pertama cuma Rp 97.000."]},
            {"name": "Guarantee", "items": ["Garansi 100% uang kembali dalam 14 hari kalau kamu merasa panduan ini nggak ada nilainya."]},
            {"name": "CTA", "items": ["Daftar sekarang lewat tombol di bawah sebelum kuota diskon ditutup malam ini!"]}
        ]
    },
    {
        "title": "[Jasa / B2B] Solusi Lead Generation & Iklan",
        "type": "Input",
        "category": "Jasa",
        "tags": ["#hardSell", "#highCR"],
        "stars": 5,
        "status": "Winner",
        "sections": [
            {"name": "Hook", "items": ["Budget iklan ratusan ribu per hari tapi yang masuk cuma pesan 'P' dan nanya harga doang?"]},
            {"name": "Problem", "items": ["Cost per lead makin mahal, closing rate jeblok, CS capek ladenin lead nggak tertarget."]},
            {"name": "Agitate", "items": ["Uang iklan habis kebakar sia-sia, sementara kompetitor terus panen omzet stabil."]},
            {"name": "Solution", "items": ["Layanan Full-Funnel Paid Ads Optimization: Kami rekayasa ulang landing page dan targeting audiens bisnis Anda."]},
            {"name": "Fitur", "items": ["Audit funnel lengkap dan tracking pixel akurat.", "A/B testing 10 variasi creative iklan.", "Laporan mingguan transparan dan dashboard live."]},
            {"name": "CTA", "items": ["Jadwalkan sesi konsultasi gratis 30 menit dengan lead strategist kami sekarang."]}
        ]
    },
    {
        "title": "[Personal Brand] Storytelling Jatuh Bangun Bisnis",
        "type": "Input",
        "category": "Personal Brand",
        "tags": ["#storytelling", "#instagram"],
        "stars": 5,
        "status": "Winner",
        "sections": [
            {"name": "Hook", "items": ["Tahun 2021 saya pernah rugi Rp 120 juta dan sisa saldo ATM tinggal Rp 85 ribu."]},
            {"name": "Problem", "items": ["Semua tabungan ludes karena salah pilih partner dan terlalu percaya diri tanpa riset pasar."]},
            {"name": "Agitate", "items": ["Malu ketemu keluarga, stres tiap akhir bulan mikirin tagihan sewa tempat."]},
            {"name": "Solution", "items": ["Di titik terendah itu, saya sadar satu hal: skill menjual dan membangun audiens adalah aset yang nggak bisa dicuri orang."]},
            {"name": "Closing", "items": ["Kalau hari ini kamu lagi di titik terbawah, ingat: kegagalan cuma babak dalam cerita, bukan akhir buku. Terus melangkah."]},
            {"name": "CTA", "items": ["Share cerita ini ke teman kamu yang lagi berjuang dan butuh pengingat hari ini."]}
        ]
    },
    {
        "title": "[Sosmed] 5 Langkah Riset Niche Affiliate (Thread / Carousel)",
        "type": "Input",
        "category": "Affiliate",
        "tags": ["#carousel", "#terbukti"],
        "stars": 4,
        "status": "Tested",
        "sections": [
            {"name": "Hook", "items": ["5 Langkah simpel riset niche affiliate yang bikin komisi ngalir tiap hari (simpan postingan ini!)."]},
            {"name": "Poin 1", "items": ["1. Cari produk dengan repeat order tinggi (skincare, suplemen, kebutuhan harian)."]},
            {"name": "Poin 2", "items": ["2. Pastikan komisi minimal 10-15% atau minimal Rp 10.000 per penjualan."]},
            {"name": "Poin 3", "items": ["3. Cek rating toko minimal 4.8 dan ulasan pembeli wajib ada foto asli."]},
            {"name": "Poin 4", "items": ["4. Buat 3 angle konten: Edukasi masalah, Unboxing jujur, dan Perbandingan harga."]},
            {"name": "Closing/CTA", "items": ["Komen 'MAU' kalau kamu pengen daftar 20 produk affiliate komisi besar minggu ini!"]}
        ]
    },
    {
        "title": "[Edukasi] Formula Copywriting AIDA Praktis",
        "type": "Input",
        "category": "Edukasi",
        "tags": ["#edukasi", "#copywriting"],
        "stars": 5,
        "status": "Winner",
        "sections": [
            {"name": "Hook", "items": ["Kenapa tulisan kamu sepi respon padahal produknya bagus? Mungkin kamu lupa formula AIDA ini."]},
            {"name": "Problem", "items": ["Kebanyakan orang jualan langsung pamer fitur teknis yang bikin pembaca bosen dalam 3 detik."]},
            {"name": "Solution", "items": ["AIDA: Attention (rebut perhatian), Interest (pancing rasa penasaran), Desire (bangkitkan nafsu memiliki), Action (suruh beli sekarang)."]},
            {"name": "Testimoni", "items": ["'Setelah rombak caption pakai AIDA, chat masuk naik 3x lipat dalam sehari!' — Dito, Seller Sepatu."]},
            {"name": "CTA", "items": ["Follow akun ini buat dapet tips copywriting praktis 1 menit tiap hari!"]}
        ]
    },
    {
        "title": "[Tulisan] Email Newsletter Selamat Datang (Welcome Sequence)",
        "type": "Input",
        "category": "Edukasi",
        "tags": ["#email", "#softSell"],
        "stars": 5,
        "status": "Tested",
        "sections": [
            {"name": "Subject Preview", "items": ["Selamat datang! Hadiah template gratis kamu ada di dalam 🎁"]},
            {"name": "Opening", "items": ["Halo! Senang banget kamu memutuskan bergabung di komunitas Temanulis."]},
            {"name": "Isi Utama", "items": ["Sesuai janji saya, ini link download 50 Hook Copywriting Terbukti yang bisa langsung kamu pakai hari ini: [Download Hook Pack]."]},
            {"name": "Insight/Value", "items": ["Tips penting: Jangan cuma copy-paste mentah-mentah. Sesuaikan nada bicaranya dengan kepribadian brand kamu."]},
            {"name": "CTA", "items": ["Balas email ini dan kasih tahu saya: apa produk atau jasa yang lagi kamu jual saat ini? Saya baca semua balasanmu."]}
        ]
    },
    {
        "title": "[Produk Digital] Hard Sell Flash Sale 24 Jam",
        "type": "Input",
        "category": "Produk Digital",
        "tags": ["#hardSell", "#highCR"],
        "stars": 5,
        "status": "Winner",
        "sections": [
            {"name": "Hook", "items": ["🚨 FLASH SALE 24 JAM HARI INI SAJA! 🚨"]},
            {"name": "Offer", "items": ["Potongan harga Rp 200.000 untuk paket bundle All-in-One Template Temanulis!"]},
            {"name": "Fitur", "items": ["Dapat 100+ template copywriting siap pakai, akses generator prompt, dan update rutin gratis."]},
            {"name": "Guarantee", "items": ["Kalau dalam 30 hari kamu nggak ngerasa tulisanmu lebih cepat selesai, kami refund tanpa ribet."]},
            {"name": "CTA", "items": ["Waktu terus berjalan. Klik link sekarang sebelum harga kembali normal di jam 23:59!"]}
        ]
    }
]

cmds = ["TRUNCATE TABLE temanulis_bank;"]
for item in SEED_ITEMS:
    title = item["title"].replace("'", "''")
    cat = item["category"].replace("'", "''")
    ttype = item["type"]
    tags_sql = "ARRAY[" + ",".join(f"'{t}'" for t in item["tags"]) + "]::text[]"
    stars = item["stars"]
    status = item["status"]
    sections_json = json.dumps(item["sections"]).replace("'", "''")
    cmds.append(f"""
    INSERT INTO temanulis_bank (title, type, category, tags, stars, status, sections)
    VALUES ('{title}', '{ttype}', '{cat}', {tags_sql}, {stars}, '{status}', '{sections_json}'::jsonb);
    """)

sql_str = "\n".join(cmds)
proc = subprocess.run(
    ["docker", "exec", "-i", "kerja-id-postgres", "psql", "-U", "kerja", "-d", "kerja_id"],
    input=sql_str.encode("utf-8"),
    capture_output=True
)
print("Postgres Seed Result:", proc.stdout.decode())
if proc.stderr:
    print("Postgres Seed Errors:", proc.stderr.decode())

full_package = {
    "version": "1.0",
    "updated": "2026-09-03",
    "total": len(SEED_ITEMS),
    "contents": [
        {
            "id": 1000 + i,
            "title": item["title"],
            "type": item["type"],
            "category": item["category"],
            "tags": item["tags"],
            "stars": item["stars"],
            "status": item["status"],
            "created": "03/09/2026",
            "sections": item["sections"]
        }
        for i, item in enumerate(SEED_ITEMS)
    ]
}

with open("/var/www/temanulis/default_bank.json", "w") as f:
    json.dump(full_package, f, indent=2)

with open("/home/ubuntu/temanulis/default_bank.json", "w") as f:
    json.dump(full_package, f, indent=2)

print("Saved default_bank.json successfully with", len(SEED_ITEMS), "items!")
