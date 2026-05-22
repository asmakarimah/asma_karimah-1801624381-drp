from datetime import datetime, time

print("Halo, selamat pagi!")
print("Apa yang ingin kamu lakukan sekarang?")
print("-> sarapan")
print("-> berangkat kerja")
print()

aktivitas = input("Masukkan aktivitas yang ingin kamu lakukan sekarang: ").lower()

if aktivitas == "":
    print("Aktivitas tidak boleh kosong. Silakan jalankan ulang program.")

elif aktivitas == "sarapan":
    print("Bahan makanan yang tersedia:")
    print("-> telur")
    print("-> ikan")
    print("-> nugget")
    print()

    menu = input("Kamu mau sarapan dengan menu makanan apa? ").lower()

    if menu == "":
        print("Menu sarapan tidak boleh kosong.")

    elif menu == "telur" or menu == "ikan" or menu == "nugget":
        print(f"Baik, {menu} tersedia.")
        print("Silakan dimasak terlebih dahulu ya!")

    else:
        print(f"Yah, {menu} belum tersedia.")
        print("Kamu harus membeli bahannya terlebih dahulu.")

elif aktivitas == "berangkat kerja":
    waktu_sekarang = datetime.now().time()
    jam_masuk = time(8, 0)

    print("Jadwal masuk kerja kamu jam 08.00 pagi.")
    print("Waktu sekarang:", datetime.now().strftime("%H:%M"))

    if waktu_sekarang > jam_masuk:
        print("Kamu sudah terlambat masuk kerja.")
        print("Segera berangkat dan usahakan tetap hati-hati di perjalanan.")
        print("Besok usahakan berangkat lebih awal, ya.")
    else:
        print("Kamu masih punya waktu sebelum jam masuk kerja.")
        print("Gunakan waktumu dengan baik agar tidak terburu-buru.")

else:
    print("Aktivitas belum tersedia.")
    print("Silakan pilih sarapan atau berangkat kerja.")