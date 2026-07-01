import time

from manager import output, search

def display_menu():
    """Menampilkan pilihan menu utama"""
    print("\n=== 🫁 APLIKASI BREATHING TIMER 🫁 ===")
    print("1. 🌬️ Mulai Box Breathing (4-4-4-4)")
    print("2. 💤 Mulai Teknik Relaksasi (4-7-8)")
    print("3. 📊 Lihat Riwayat Latihan")
    print("4. ❌ Keluar Program")
    print("======================================")

def jalankan_timer(nama_teknik, jumlah_siklus, pola_waktu):
    """
    Menjalankan timer pernapasan.
    pola_waktu adalah list detik: [Tarik, Tahan, Hembus, Tahan]
    """
    print(f"\nMemulai {nama_teknik} sebanyak {jumlah_siklus} siklus...")
    time.sleep(1) # Jeda 1 detik sebelum mulai
    
    for i in range(jumlah_siklus):
        print(f"\n--- Siklus {i+1} ---")
        langkah = ["Tarik napas", "Tahan napas", "Hembuskan napas", "Tahan napas"]
        
        for j in range(len(pola_waktu)):
            detik = pola_waktu[j]
            if detik > 0: 
                print(f"{langkah[j]} ({detik} detik)", end="")
                
                for _ in range(detik):
                    print(".", end="", flush=True)
                    time.sleep(1) 
                print(" ✅")
    
    durasi_total = sum(pola_waktu) * jumlah_siklus
    output.simpan_riwayat(nama_teknik, jumlah_siklus, durasi_total)
    print(f"\n🎉 Latihan selesai! Riwayat {nama_teknik} telah disimpan ke database.")

def menu_lihat_riwayat():
    """Mengambil data dari manager dan menampilkannya"""
    data = search.ambil_semua_riwayat()
    
    print("\n📊 --- RIWAYAT LATIHANMU --- 📊")
    if len(data) == 0:
        print("Belum ada riwayat. Yuk mulai bernapas! 🌬️")
    else:
        for i in range(len(data)):
            print(f"Sesi {i+1}: {data[i]['Teknik']} | {data[i]['Siklus']} siklus | Total: {data[i]['Total Waktu']} detik")

def select_menu(menu):
    """Mengarahkan program sesuai pilihan user"""
    if menu == '1':
        jalankan_timer("Box Breathing", 3, [4, 4, 4, 4])
        return False
    elif menu == '2':
        jalankan_timer("Teknik 4-7-8", 2, [4, 7, 8, 0])
        return False
    elif menu == '3':
        menu_lihat_riwayat()
        return False
    elif menu == '4':
        print("\nTerima kasih sudah meluangkan waktu untuk bernapas. Sampai jumpa! 👋")
        return True
    else:
        print("\n❌ Pilihan tidak valid.")
        return False 