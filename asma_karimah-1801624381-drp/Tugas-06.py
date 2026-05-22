from datetime import datetime

print("Halo, selamat pagi!")
print("Apa yang ingin kamu lakukan sekarang?")
print("--> sarapan")
print("--> berangkat kerja")

aktivitas = input("Masukkan aktivitas yang ingin kamu lakukan sekarang: ")

if aktivitas.lower() == "sarapan":
    print("Bahan makanan yang tersedia hari ini:")
    print("telur")
    print("ikan")
    print("nugget")

    menu = input("Kamu mau sarapan dengan menu makanan apa? ")

    if menu.lower() == "telur" or menu.lower() == "ikan" or menu.lower() == "nugget":
        print(f"Baik, {menu} tersedia. Silakan dimasak terlebih dahulu, ya!")
    else:
        print(f"Sayang sekali, bahan untuk {menu} belum tersedia.")
        print("Kamu harus membeli bahannya terlebih dahulu.")

elif aktivitas.lower() == "berangkat kerja":
    waktu = datetime.now()

    print("Jadwal masuk kerja kamu jam 08.00 pagi.")
    print(f"Sekarang sudah menunjukkan pukul {waktu.hour:02d}:{waktu.minute:02d}")

    if waktu.hour < 8:
        print("Kamu masih punya waktu sebelum jam masuk kerja.")
        print("Gunakan waktumu dengan baik agar tidak terburu-buru.")

    elif waktu.hour == 8:
        print("Sekarang sudah jam 08.00. Kamu harus segera berangkat kerja.")
        print("Besok usahakan berangkat lebih awal, ya!")

    else:
        print("Kamu sudah terlambat masuk kerja.")
        print("Segera berangkat! Besok coba siapkan semuanya lebih awal.")


else:
    print("Aktivitas tidak tersedia.")
    print("Silakan pilih mau sarapan atau mau pergi kerja.")