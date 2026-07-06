import sqlite3

def init_db():
    conn = sqlite3.connect("breathing.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS riwayat (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        mood TEXT,
        teknik TEXT,
        pattern TEXT,
        waktu TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()