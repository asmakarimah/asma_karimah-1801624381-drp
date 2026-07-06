import os
import time
from manager.output import simpan_riwayat
from manager.search import ambil_semua_riwayat
from manager.export_json import export_json
from manager.import_json import import_json

RULE = {
    "stres": {
        "teknik": "Box Breathing",
        "steps": [
            ("INHALE", 4),
            ("HOLD", 4),
            ("EXHALE", 4),
            ("HOLD", 4)
        ],
        "afirmasi": "You've been carrying a lot. It's okay to slow down."
    },
    "cemas": {
        "teknik": "4-7-8 Breathing",
        "steps": [
            ("INHALE", 4),
            ("HOLD", 7),
            ("EXHALE", 8)
        ],
        "afirmasi": "You are safe right now. Just focus on your breathing."
    },
    "marah": {
        "teknik": "Long Exhale Breathing",
        "steps": [
            ("INHALE", 4),
            ("EXHALE", 6)
        ],
        "afirmasi": "It's okay to pause. You don't have to react immediately."
    },
    "lelah": {
        "teknik": "Coherent Breathing",
        "steps": [
            ("INHALE", 5),
            ("EXHALE", 5)
        ],
        "afirmasi": "You've done enough for today. Be kind to yourself."
    }
}

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def pilih_mood():
    print("\n========== PILIH MOOD ==========")
    print("1. 😣 Stres")
    print("2. 😟 Cemas")
    print("3. 😡 Marah")
    print("4. 😴 Lelah")
    
    pilihan = input("\nPilih mood (1-4): ")
    mapping = {
        "1": "stres",
        "2": "cemas",
        "3": "marah",
        "4": "lelah"
    }
    return mapping.get(pilihan)

def breathing_session(teknik, steps):
    print("\n==============================")
    print(f"🫁 Teknik : {teknik}")
    print("==============================")
    
    for fase, durasi in steps:
        for detik in range(1, durasi + 1):
            titik = "." * detik
            print(f"\r{fase} {titik}", end="", flush=True)
            time.sleep(1)
        print() 
        
    print("\n✔ Sesi breathing selesai.")

def menu():
    while True:
        clear()
        print("========== BREATHING APP ==========")
        print("1. Mulai Breathing")
        print("2. Lihat Riwayat")
        print("3. Export JSON")
        print("4. Import JSON")
        print("0. Keluar")
        print("===================================")
        
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            clear()
            mood = pilih_mood()
            
            if mood is None:
                print("\n❌ Pilihan tidak tersedia.")
                input("Tekan Enter untuk kembali...")
                continue
                
            data = RULE[mood]
            teknik = data["teknik"]
            steps = data["steps"]
            afirmasi = data["afirmasi"]
            
            clear()
            print(f"Mood   : {mood.capitalize()}")
            print(f"Teknik : {teknik}")
            
            breathing_session(teknik, steps)
            
            print("\n💬 AFIRMASI")
            print(f'"{afirmasi}"')
            
            pattern = tuple(durasi for _, durasi in steps)
            simpan_riwayat(mood, teknik, str(pattern))
            print("\n✔ Riwayat berhasil disimpan.")
            
            input("\nTekan Enter untuk kembali ke menu...")
            
        elif pilihan == "2":
            clear()
            data = ambil_semua_riwayat()
            
            print("========== RIWAYAT ==========")
            if not data:
                print("Belum ada riwayat.")
            else:
                for row in data:
                    print("--------------------------------")
                    print(f"ID      : {row[0]}")
                    print(f"Mood    : {row[1]}")
                    print(f"Teknik  : {row[2]}")
                    print(f"Pattern : {row[3]}")
                    print(f"Waktu   : {row[4]}")
                print("--------------------------------")
                
            input("\nTekan Enter untuk kembali ke menu...")
        
        elif pilihan == "3":
            clear()
            export_json()
            input("\nTekan Enter untuk kembali...")

        elif pilihan == "4":
            clear()
            import_json()
            input("\nTekan Enter untuk kembali...")
            
        elif pilihan == "0":
            clear()
            print("Terima kasih telah menggunakan Breathing App. Stay mindful! 👋")
            break
        else:
            print("\n❌ Pilihan tidak tersedia.")
            input("Tekan Enter untuk kembali...")
