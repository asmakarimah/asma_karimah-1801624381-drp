import json
import sqlite3
import os

def import_json():
    nama_file = "riwayat.json"
    database_path = "breathing.db"

    # Cek apakah file JSON ada
    if not os.path.exists(nama_file):
        print(f"\n❌ Gagal: File '{nama_file}' tidak ditemukan!")
        print("Pastikan sudah ada file riwayat.json hasil export di folder tugas-09.")
        return

    try:
        # Baca isi file JSON
        with open(nama_file, "r") as file:
            data_riwayat = json.load(file)

        if not data_riwayat:
            print("\n⚠ File JSON kosong, tidak ada data untuk di-import.")
            return

        # Koneksi ke database
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        # Suntik data dari JSON ke SQLite
        for data in data_riwayat:
            cursor.execute("""
                INSERT INTO riwayat (mood, teknik, pattern, waktu)
                VALUES (?, ?, ?, ?)
            """, (data['mood'], data['teknik'], data['pattern'], data['waktu']))
        
        conn.commit()
        conn.close()
        
        print(f"\n✔ BERHASIL! {len(data_riwayat)} data dari file JSON sukses dimasukkan ke database.")

    except Exception as e:
        print(f"\n❌ Terjadi kesalahan saat proses import: {e}")