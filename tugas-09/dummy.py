import json
import random
import os
from datetime import datetime, timedelta

MOOD_OPTIONS = ["stres", "cemas", "marah", "lelah"]
TEKNIK_MAPPING = {
    "stres": {"teknik": "Box Breathing", "pattern": "(4, 4, 4, 4)"},
    "cemas": {"teknik": "4-7-8 Breathing", "pattern": "(4, 7, 8)"},
    "marah": {"teknik": "Long Exhale Breathing", "pattern": "(4, 6)"},
    "lelah": {"teknik": "Coherent Breathing", "pattern": "(5, 5)"}
}

def bikin_json_raksasa(nama_file="riwayat_raksasa.json", jumlah_data=35000):
    data_dummy = []
    waktu_awal = datetime(2026, 6, 25, 8, 0, 0)
    
    print("⏳ Sedang memproses pembuatan data dummy raksasa...")
    
    for i in range(1, jumlah_data + 1):
        mood = random.choice(MOOD_OPTIONS)
        detail = TEKNIK_MAPPING[mood]
        
        acak_menit = random.randint(0, 12000)
        waktu_sekarang = waktu_awal + timedelta(minutes=acak_menit)
        
        row = {
            "id": i,
            "mood": mood,
            "teknik": detail["teknik"],
            "pattern": detail["pattern"],
            "waktu": waktu_sekarang.strftime("%Y-%m-%d %H:%M:%S")
        }
        data_dummy.append(row)
        
    with open(nama_file, "w") as file:
        json.dump(data_dummy, file, indent=4)
        
    ukuran_bytes = os.path.getsize(nama_file)
    ukuran_mb = ukuran_bytes / (1024 * 1024)
    
    print("\n=========================================")
    print(f"✔ BERHASIL! File '{nama_file}' telah lahir.")
    print(f"📊 Total data   : {jumlah_data} baris riwayat")
    print(f"📦 Ukuran file  : {ukuran_mb:.2f} MB")
    print("=========================================")

if __name__ == "__main__":
    bikin_json_raksasa()