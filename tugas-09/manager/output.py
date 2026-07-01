import sqlite3

def simpan_riwayat(teknik, siklus, durasi_total):
    """Fungsi CREATE: Menyimpan data ke database SQL"""
    conn = sqlite3.connect('breathing.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO riwayat (teknik, siklus, durasi)
        VALUES (?, ?, ?)
    ''', (teknik, siklus, durasi_total))
    
    conn.commit()
    conn.close()