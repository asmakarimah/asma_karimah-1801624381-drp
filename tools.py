import time
import os
from manager.output import simpan_riwayat
from manager.search import ambil_semua_riwayat


RULE = {
    "stres": {
        "teknik": "Box Breathing",
        "pattern": (4, 4, 4, 4),
        "afirmasi": "You’ve been carrying a lot. It’s okay to slow down."
    },
    "cemas": {
        "teknik": "4-7-8 Breathing",
        "pattern": (4, 7, 8),
        "afirmasi": "You’ve been carrying a lot. It’s okay to slow down."
    },
    "marah": {
        "teknik": "Long Exhale Breathing",
        "pattern": (4, 6),
        "afirmasi": "It’s okay to feel this. Take a moment before reacting."
    },
    "lelah": {
        "teknik": "Balanced Breathing",
        "pattern": (4, 4),
        "afirmasi": "You’ve done enough for today. You deserve rest."
    }
}


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def pilih_mood():
    print("\n=== PILIH MOOD ===")
    print("1. 😣 Stres")
    print("2. 😟 Cemas")
    print("3. 😡 Marah")
    print("4. 😴 Lelah")

    mapping = {
        "1": "stres",
        "2": "cemas",
        "3": "marah",
        "4": "lelah"
    }

    return mapping.get(input("Pilih mood: "))


import time

def breathing_session(teknik, pattern):
    print(f"\n🫁 TEKNIK: {teknik}\n")

    labels = ["INHALE", "HOLD", "EXHALE"]

    for i, durasi in enumerate(pattern):
        label = labels[i] if i < len(labels) else f"PHASE {i+1}"

        for detik in range(durasi):
            dots = "." * (detik + 1)
            print(f"\r{label} {dots}", end="", flush=True)
            time.sleep(1)

        print()  # pindah baris setelah tiap fase

    print("\n✔ Sesi selesai\n")

def menu():
    while True:
        print("\n=== BREATHING APP ===")
        print("1. Mulai sesi")
        print("2. Lihat riwayat")
        print("0. Keluar")

        p = input("Pilih: ")

        if p == "1":
            mood = pilih_mood()
            if not mood:
                print("Invalid")
                continue

            data = RULE[mood]

            teknik = data["teknik"]
            pattern = data["pattern"]
            afirmasi = data["afirmasi"]

            print("\nMOOD:", mood)
            print("TEKNIK:", teknik)

            breathing_session(teknik, pattern)

            print("💬 AFIRMASI:")
            print(afirmasi)

            simpan_riwayat(
                mood,
                teknik,
                str(pattern)
            )

        elif p == "2":
            data = ambil_semua_riwayat()

            print("\n=== RIWAYAT ===")
            for row in data:
                print(row)

        elif p == "0":
            break