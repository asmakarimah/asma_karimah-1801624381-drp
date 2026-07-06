import json

def fungsi_mapper(potongan_data):
    """
    TAHAP MAP: Mengubah data mentah menjadi pasangan (Key, 1)
    """
    hasil_map_mood = []
    hasil_map_teknik = []
    
    for row in potongan_data:
        hasil_map_mood.append((row["mood"], 1))
        hasil_map_teknik.append((row["teknik"], 1))
        
    return hasil_map_mood, hasil_map_teknik

def fungsi_reducer(daftar_pasangan_map):
    """
    TAHAP REDUCE: Menjumlahkan angka 1 berdasarkan Key yang sama
    """
    hasil_total = {}
    for key, nilai in daftar_pasangan_map:
        hasil_total[key] = hasil_total.get(key, 0) + nilai
    return hasil_total

def main():
    print("\n🧠 MEMULAI PROSES MAPREDUCE MANUAL")
    print("=========================================================")

    nama_file = "riwayat_raksasa.json"
    try:
        with open(nama_file, "r") as file:
            semua_data = json.load(file)
    except FileNotFoundError:
        print(f"❌ File '{nama_file}' tidak ditemukan!")
        print("Silakan jalankan 'py dummy.py' terlebih dahulu untuk membuat datanya.")
        return

    total_baris = len(semua_data)
    titik_tengah = total_baris // 2

    print(f"📦 Mengunggah {total_baris} baris data dari {nama_file}...")
    print("✂️ Membagi data secara adil ke dalam 2 Node Pekerja:")
    node_1_data = semua_data[:titik_tengah]
    node_2_data = semua_data[titik_tengah:]
    print(f"   -> 💻 Node 1 memproses : {len(node_1_data)} data")
    print(f"   -> 💻 Node 2 memproses : {len(node_2_data)} data\n")

    map_mood_1, map_teknik_1 = fungsi_mapper(node_1_data)
    map_mood_2, map_teknik_2 = fungsi_mapper(node_2_data)

    gabungan_map_mood = map_mood_1 + map_mood_2
    gabungan_map_teknik = map_teknik_1 + map_teknik_2

    total_mood = fungsi_reducer(gabungan_map_mood)
    total_teknik = fungsi_reducer(gabungan_map_teknik)

    mood_terbanyak = max(total_mood, key=total_mood.get)
    teknik_terbanyak = max(total_teknik, key=total_teknik.get)

    emoji_mood = {
        "stres": "😣 Stres ",
        "cemas": "😟 Cemas ",
        "marah": "😡 Marah ",
        "lelah": "😴 Lelah "
    }

    print("📊 HASIL REDUCE (Kombinasi Node 1 & Node 2):")
    print("---------------------------------------------------------")
    print(" Rincian Kemunculan Mood:")
    for mood, total in total_mood.items():
        print(f"   {emoji_mood.get(mood, mood)} : {total} kali")
        
    print("\n Rincian Penggunaan Teknik Pernapasan:")
    for teknik, total in total_teknik.items():
        print(f"   🫁 {teknik:<22} : {total} kali")
        
    print("---------------------------------------------------------")
    print("📝 KESIMPULAN/INSIGHT DATA RAYA:")
    print(
        f" Dari puluhan ribu data yang diolah, pengguna paling sering merasa {mood_terbanyak.capitalize()}\n"
        f" dengan pemilihan teknik pernapasan terfavorit yaitu {teknik_terbanyak}.\n\n"
        f" ✔️ Proses MapReduce Manual Sukses Terbaca 100%!"
    )
    print("=========================================================")

if __name__ == "__main__":
    main()