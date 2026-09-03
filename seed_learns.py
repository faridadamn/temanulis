import json
import subprocess

ALL_JURUS = [
    # === KITAB AFFILIATE RIZAL (14 JURUS MASTER) ===
    {
        "title": "Jurus 1: It's Not About The Product, It's About You",
        "topic": "Affiliate",
        "source": "Kitab Affiliate Rizal",
        "tags": ["#affiliate", "#mindset", "#painPoint"],
        "body": "Mulai dari masalah manusiawi, bukan spek produk. Jual rasa sakit (malu, capek, takut, rugi), bukan fitur. Bukan 'bahan stainless anti karat', tapi 'lo nggak perlu nanggung malu lagi di depan rekan kerja karena kemeja kusut'. Orang beli pereda sakit, bukan vitamin."
    },
    {
        "title": "Jurus 2: Solusi Gratisan Dulu, Produk Belakangan",
        "topic": "Affiliate",
        "source": "Kitab Affiliate Rizal",
        "tags": ["#affiliate", "#kredibilitas", "#trust"],
        "body": "Sebelum produk affiliate muncul, selalu tawarkan 2-3 alternatif solusi gratis (trik mandiri, kebiasaan baru, atau setting manual). Ini membangun kredibilitas sebagai penolong jujur yang peduli masalah audiens, bukan sales lapar komisi."
    },
    {
        "title": "Jurus 3: Framework B-A-P (Bobek, Ajaib, Pulih)",
        "topic": "Copywriting",
        "source": "Kitab Affiliate Rizal",
        "tags": ["#copywriting", "#konversi", "#bap"],
        "body": "Alur konversi affiliate: Tusuk luka spesifik (Bobek) di awal → Perdalam lukanya dengan menghitung efek jangka panjang atau biaya tersembunyi yang bikin nyesek → Baru hadirkan produk ajaib pereda luka saat pembaca sadar solusi gratisan nggak cukup → Ceritakan hasil pulih yang jujur."
    },
    {
        "title": "Jurus 4: Teknik Harga Jangkar & Pecah Biaya Harian",
        "topic": "Marketing",
        "source": "Kitab Affiliate Rizal",
        "tags": ["#marketing", "#hargaJangkar", "#closing"],
        "body": "Jangan sebut harga produk begitu saja. Bandingkan dengan alternatif yang jauh lebih mahal (Harga Jangkar) atau pecah biayanya jadi pengeluaran receh harian: 'Cuma Rp2.500 sehari, lebih murah dari segelas es teh, tapi bikin masalah punggung beres 6 bulan'."
    },
    {
        "title": "Jurus 5: Teknik Pilihan Setan (Pancing Komentar & Debat)",
        "topic": "Affiliate",
        "source": "Kitab Affiliate Rizal",
        "tags": ["#affiliate", "#engagement", "#viral"],
        "body": "Tutup konten dengan kontras ekstrem 2 kubu: Tim A (tetap tahan sakit, buang waktu & uang seperti biasa) vs Tim B (ambil tindakan, masalah kelar mulai hari ini). Ini memicu debat sehat dan memancing ribuan komentar organik di Threads / TikTok."
    },
    {
        "title": "Jurus 6: Testimoni Jujur & Flaw Disclosure (Kasih Racun Sedikit)",
        "topic": "Copywriting",
        "source": "Kitab Affiliate Rizal",
        "tags": ["#copywriting", "#testimoni", "#objectionHandling"],
        "body": "Selalu sebutkan 1 kekurangan kecil produk secara jujur (misal: 'pengirimannya agak lama' atau 'bahannya agak berat'). Review yang 100% manis memicu curiga pembaca; kasih racunnya sedikit supaya madunya laku keras!"
    },
    {
        "title": "Jurus 7: Tahan Link Sampai Baris Terakhir (T-E-K-S)",
        "topic": "Affiliate",
        "source": "Kitab Affiliate Rizal",
        "tags": ["#affiliate", "#cta", "#link"],
        "body": "Jangan pernah menaruh link affiliate di hook atau paragraf pembuka. Bangun cerita dan keterikatan emosi sampai klimaks. Tahan link sampai baris paling akhir ketika audiens sudah merasa butuh dan siap checkout."
    },
    {
        "title": "Jurus 8: 5 Jenis Konten Funnel Utas (Rotasi Anti-Bosan)",
        "topic": "Affiliate",
        "source": "Kitab Affiliate Rizal",
        "tags": ["#affiliate", "#funnel", "#rotasi"],
        "body": "Jangan tiap hari jualan! Terapkan rotasi 4 jenis konten: 40% Engagement (Pilihan Setan pancing rame), 30% Awareness (cerita relatable sehari-hari), 20% Edukasi (tips murni tanpa jualan buat bangun trust), dan cuma 10% Konversi (hard sell B-A-P + link)."
    },
    {
        "title": "Jurus 9: Ubah Fitur Menjadi Borok & Rasa Malu",
        "topic": "Copywriting",
        "source": "Kitab Affiliate Rizal",
        "tags": ["#copywriting", "#fitur", "#emosi"],
        "body": "Stop bilang 'barang ini bagus'. Cari produk yang punya borok/masalah nyata. Ubah spesifikasi jadi rasa malu atau kerugian: bukan 'baterai 5000 mAh', tapi 'lo nggak perlu panik celingukan nyari colokan pas lagi meeting penting bareng bos'."
    },
    {
        "title": "Jurus 10: Model Trinitas Copywriting (PAS vs AIDA vs FAB)",
        "topic": "Copywriting",
        "source": "Kitab Affiliate Rizal",
        "tags": ["#copywriting", "#framework", "#trinitas"],
        "body": "Pilih model sesuai medan: PAS (Problem-Agitate-Solution) paling sakti buat feed Threads/FB. AIDA (Attention-Interest-Desire-Action) paling pas buat video pendek/Reels. FAB (Feature-Advantage-Benefit) cocok buat jualan to-the-point yang fokus 'apa untungnya buat gue'."
    },
    {
        "title": "Jurus 11: Hook Berasa Ditampar (Anti Brosur Indomaret)",
        "topic": "Copywriting",
        "source": "Kitab Affiliate Rizal",
        "tags": ["#copywriting", "#hook", "#viral"],
        "body": "Konten tanpa hook yang menusuk itu bukan konten, itu nafas terakhir brosur promo. Gunakan hook yang bikin audiens ngerasa ditampar: sebut kebiasaan salah mereka yang bikin boncos atau rugi waktu bertahun-tahun."
    },
    {
        "title": "Jurus 12: Bedah Mayat Konten (Fokus CTR daripada Followers)",
        "topic": "Affiliate",
        "source": "Kitab Affiliate Rizal",
        "tags": ["#affiliate", "#ctr", "#analisis"],
        "body": "Posting lalu ditinggal itu cuma nitip harapan ke server. Evaluasi metrik: affiliate butuh pembeli (CTR link), bukan sekadar followers. Kalau views rame tapi komisi nol, masalah ada di transisi solusi gratisan ke produk yang kurang halus."
    },
    {
        "title": "Jurus 13: Formula Alur 3 Hari (Storytelling Mesin Komisi)",
        "topic": "Affiliate",
        "source": "Kitab Affiliate Rizal",
        "tags": ["#affiliate", "#storytelling", "#alur"],
        "body": "Jual produk lewat cerita berseri: Hari 1 ceritakan kegiatan sehari-hari 'B aja' yang relatable. Hari 2 angkat frustrasi dan masalah yang dialami. Hari 3 baru produk nempel sebagai penyelamat. Audiens terikat secara alami tanpa merasa dijualin."
    },
    {
        "title": "Jurus 14: Tamparan Data & Perbandingan Rugi Nyata",
        "topic": "Marketing",
        "source": "Kitab Affiliate Rizal",
        "tags": ["#marketing", "#data", "#urgensi"],
        "body": "Gunakan perbandingan kerugian konkret: 'Bukan soal harga produk Rp50.000, tapi lo sadar nggak selama ini udah buang Rp400.000 cuma buat nambal akibat masalah yang lo sepelekan?'. Ubah fokus dari harga beli ke biaya menunda."
    },
    # === KAIDAH EMAS COPYWRITING ===
    {
        "title": "Aturan 3 Detik Pertama (Stop-Scroll Hook)",
        "topic": "Copywriting",
        "source": "Kaidah Emas",
        "tags": ["#copywriting", "#hook", "#viral"],
        "body": "Jangan pernah langsung sebut nama brand atau jualan di kalimat pembuka. Selalu buka dengan rasa sakit spesifik, fakta kontras, atau kebiasaan salah audiens untuk menghentikan scrolling."
    },
    {
        "title": "Curiosity Gap Principle (Pemicu Penasaran)",
        "topic": "Marketing",
        "source": "Kaidah Emas",
        "tags": ["#marketing", "#curiosity", "#psikologi"],
        "body": "Beri tahu 'Apa' dan 'Mengapa' suatu fenomena terjadi, tapi simpan 'Bagaimana cara kerjanya' untuk bagian solusi atau CTA. Ini memicu rasa penasaran alami manusia untuk membaca sampai tuntas."
    },
    {
        "title": "Bahasa Mengobrol Santai (Gaya Ngopi)",
        "topic": "Copywriting",
        "source": "Kaidah Emas",
        "tags": ["#copywriting", "#tone", "#ngopi"],
        "body": "Gunakan bahasa Indonesia percakapan yang luwes, kalimat pendek-pendek (maksimal 15 kata per kalimat). Hindari kata-kata birokratis atau kaku seperti 'oleh karena itu', 'guna mewujudkan'."
    },
    {
        "title": "Single Call to Action (Satu Aksi Jelas)",
        "topic": "Marketing",
        "source": "Kaidah Emas",
        "tags": ["#marketing", "#cta", "#urgensi"],
        "body": "Setiap konten hanya boleh punya 1 ajakan bertindak (One Single Action: klik link, komen kata kunci, atau DM). Beri alasan mendesak kenapa harus bertindak sekarang juga (urgensi/kelangkaan)."
    }
]

def run_psql(sql):
    cmd = ["docker", "exec", "-i", "kerja-id-postgres", "psql", "-U", "kerja", "-d", "kerja_id", "-c", sql]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print("SQL Error:", res.stderr)
        raise RuntimeError(res.stderr)
    return res.stdout

print("1. Creating table temanulis_learns in PostgreSQL...")
run_psql("""
CREATE TABLE IF NOT EXISTS temanulis_learns (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    topic VARCHAR(100) DEFAULT 'Copywriting',
    body TEXT NOT NULL,
    tags TEXT[],
    source VARCHAR(100) DEFAULT 'Kitab Affiliate Rizal',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")

print("2. Truncating table...")
run_psql("TRUNCATE TABLE temanulis_learns RESTART IDENTITY;")

print("3. Inserting all 18 Master Jurus...")
for item in ALL_JURUS:
    tags_literal = "ARRAY[" + ",".join([f"'{t}'" for t in item["tags"]]) + "]" if item.get("tags") else "ARRAY[]::TEXT[]"
    title_esc = item["title"].replace("'", "''")
    topic_esc = item["topic"].replace("'", "''")
    body_esc = item["body"].replace("'", "''")
    source_esc = item.get("source", "Kitab Affiliate Rizal").replace("'", "''")
    
    sql = f"""
    INSERT INTO temanulis_learns (title, topic, body, tags, source)
    VALUES ('{title_esc}', '{topic_esc}', '{body_esc}', {tags_literal}, '{source_esc}');
    """
    run_psql(sql)

print(f"Successfully inserted all {len(ALL_JURUS)} jurus into PostgreSQL!")

learns_export = []
for i, item in enumerate(ALL_JURUS):
    learns_export.append({
        "id": i + 1,
        "title": item["title"],
        "topic": item["topic"],
        "source": item.get("source", ""),
        "created": "03/09/2026",
        "body": item["body"]
    })

output_data = {
    "version": "2.0",
    "updated_at": "2026-09-03",
    "source": "PostgreSQL kerja_id.temanulis_learns",
    "total": len(learns_export),
    "learns": learns_export
}

with open("/var/www/temanulis/default_learns.json", "w") as f:
    json.dump(output_data, f, indent=2, ensure_ascii=False)

with open("/home/ubuntu/temanulis/default_learns.json", "w") as f:
    json.dump(output_data, f, indent=2, ensure_ascii=False)

print("Exported default_learns.json to /var/www/temanulis/ and /home/ubuntu/temanulis/!")
