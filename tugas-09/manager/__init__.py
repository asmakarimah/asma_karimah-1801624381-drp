import sqlite3

conn = sqlite3.connect('breathing.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS riwayat (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        teknik TEXT,
        siklus INTEGER,
        durasi INTEGER
    )
''')

conn.commit()
conn.close()