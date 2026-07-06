import sqlite3
import json

DB = "breathing.db"

def export_json():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT mood, teknik, pattern, waktu
        FROM riwayat
    """)

    data = cursor.fetchall()
    conn.close()

    hasil = []

    for row in data:
        hasil.append({
            "mood": row[0],
            "teknik": row[1],
            "pattern": row[2],
            "waktu": row[3]
        })

    with open("riwayat.json", "w", encoding="utf-8") as file:
        json.dump(hasil, file, indent=4, ensure_ascii=False)

    print("✔ Data berhasil diexport ke riwayat.json")