print("=== LAYOUT CATUR ===\n")

for baris in range(8):
    for kolom in range(8):
        if (baris + kolom) % 2 == 0:
            print("⬜", end="")
        else:
            print("⬛", end="")
    print()


print("\n=== CATAT AKTIVITAS ===")

daftar_aktivitas = []

jumlah = int(input("\nBerapa aktivitas yang mau dicatat? "))

for i in range(jumlah):
    print(f"\nAktivitas ke-{i + 1}")

    aktivitas = input("Nama aktivitas        : ")
    deadline = input("Deadline (YYYY-MM-DD) : ")
    keterangan = input("Keterangan           : ")

    data_aktivitas = [deadline, aktivitas, keterangan]
    daftar_aktivitas.append(data_aktivitas)

daftar_aktivitas.sort()

print("\n=== DAFTAR AKTIVITAS KAMU ===")
print("Aktivitas sudah disusun dari deadline paling cepat.\n")

for i in range(len(daftar_aktivitas)):
    print(f"Aktivitas ke-{i + 1}")
    print("Aktivitas   :", daftar_aktivitas[i][0])
    print("Keterangan  :", daftar_aktivitas[i][1])
    print("Deadline    :", daftar_aktivitas[i][2])
    print("------------------------------")

print("Total aktivitas:", len(daftar_aktivitas))
print("Semangat ngerjainnya ya! 🌟")
