import sqlite3

DB = "breathing.db"

def ambil_semua_riwayat():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, mood, teknik, pattern, waktu
        FROM riwayat
    """)

    data = cursor.fetchall()
    conn.close()
    return data