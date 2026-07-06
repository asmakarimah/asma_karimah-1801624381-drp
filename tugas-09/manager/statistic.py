import sqlite3

DB = "breathing.db"

def hitung_statistik():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    
    # Ambil data mentah dari database
    cursor.execute("SELECT mood, teknik FROM riwayat")
    rows = cursor.fetchall()
    conn.close()

    print("\n📊 STATISTIK PEKANAN")
    print("=========================================")

    # Fitur Anti-Crash: Jika database masih kosong
    if not rows:
        print(" ✨ Total Sesi Breathing : 0 kali")
        print("-----------------------------------------")
        print("Belum ada riwayat pekan ini. Yuk, mulai")
        print("ambil napas dalam-dalam hari ini! 🫁")
        print("=========================================")
        return

    total_sesi = len(rows)
    mood_counts = {"stres": 0, "cemas": 0, "marah": 0, "lelah": 0}
    teknik_counts = {}

    # Hitung distribusi data (Konsep Map & Reduce manual)
    for mood, teknik in rows:
        if mood in mood_counts:
            mood_counts[mood] += 1
        teknik_counts[teknik] = teknik_counts.get(teknik, 0) + 1

    # Cari yang paling sering muncul
    mood_tersering = max(mood_counts, key=mood_counts.get)
    teknik_tersering = max(teknik_counts, key=teknik_counts.get)

    emoji_mood = {
        "stres": "😣 Stres ",
        "cemas": "😟 Cemas ",
        "marah": "😡 Marah ",
        "lelah": "😴 Lelah "
    }

    # Tampilkan Hasil Statistik
    print(f" ✨ Total Sesi Breathing : {total_sesi} kali\n")
    
    print(" Rincian Kondisi Mood Kamu:")
    for key, count in mood_counts.items():
        print(f"   {emoji_mood[key]} : {count} sesi")
        
    print("-----------------------------------------")
    
    print(" 📝 RINGKASAN & EVALUASI")
    print(
        f" Selama sepekan ini kamu lebih sering merasa {mood_tersering.capitalize()},\n"
        f" dengan teknik pernapasan andalanmu yaitu {teknik_tersering}.\n\n"
        f" Semoga pekan berikutnya mood-mu jauh lebih baik,\n"
        f" harimu lebih tenang, dan tetap mindful ya! ✨"
    )
    print("=========================================")