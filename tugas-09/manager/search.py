import sqlite3

def ambil_semua_riwayat():
    """Fungsi READ: Mengambil seluruh data dari database SQL"""
    conn = sqlite3.connect('breathing.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT teknik, siklus, durasi FROM riwayat')
    hasil_sql = cursor.fetchall()
    conn.close()
    
    riwayat_latihan = []
    for baris in hasil_sql:
        sesi = {
            "Teknik": baris[0],
            "Siklus": baris[1],
            "Total Waktu": baris[2]
        }
        riwayat_latihan.append(sesi)
        
    return riwayat_latihan