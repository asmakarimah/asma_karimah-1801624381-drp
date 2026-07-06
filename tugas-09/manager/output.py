import sqlite3

DB = "breathing.db"

def simpan_riwayat(mood, teknik, pattern):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO riwayat (mood, teknik, pattern)
        VALUES (?, ?, ?)
    """, (mood, teknik, pattern))

    conn.commit()
    conn.close()