import random
import re

def normalize(text: str) -> str:
    """Normalisasi jawaban (huruf kecil, hapus tanda baca, spasi berlebih)"""
    text = (text or "").lower().strip()
    text = re.sub(r'[^0-9a-z\s]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text

# --- Soal (boleh kamu ubah / tambah) ---
soal_jawaban = [
    {"soal": "apa fungsi Trakea?", "jawaban": ["menangkap benda asing yang masuk ke pernapasan", "menyaring debu jika masuk ke pernapasan", "menangkap benda asing jika masuk pernapasan", "menyaring debu yang masuk pernapasan", "menangkap benda asing yang masuk ke pernapasan", "menyaring benda asing yang masuk ke pernapasan", "menyaring benda asing yang masuk pernapasan"]},
    {"soal": "apa fungsi Bronkus?", "jawaban": ["sebagai saluran udara"]},
    {"soal": "apa fungsi Bronkiolus?", "jawaban": ["tempat tersusunnya banyak pembuluh kapiler", "tersusunnya banyak pembuluh kapiler"]},
    {"soal": "apa fungsi paru²?", "jawaban": ["Organ pernapasan utama"]},
    {"soal": "apa fungsi faring?", "jawaban": ["meneruskan udara setelah ke rongga hidung", "meneruskan udara dari rongga hidung"]},
    {"soal": "apa fungsi rongga hidung?", "jawaban": ["menyaring udara yang masuk", "menyaring udara", "menghirup oksigen", "bernapas"]}
]
# ----------------------------------------

def is_correct(user_input, correct):
    u = normalize(user_input)
    if isinstance(correct, list):
        return any(u == normalize(c) for c in correct)
    return u == normalize(correct)

def main():
    print("=== KUIS ACAK REPEAT TANPA DOUBEL ===")
    print("Soal bisa terulang, tapi tidak dua kali berturut-turut.\n")
    print("Ketik 'exit' untuk keluar.\n")

    # jumlah soal ditanyakan
    try:
        jumlah = int(input("Mau berapa soal? (misal 10): ") or 10)
    except:
        jumlah = 10

    skor = 0
    salah_list = []
    last_question = None

    for i in range(1, jumlah + 1):
        # pilih soal acak yang tidak sama dengan soal sebelumnya
        while True:
            item = random.choice(soal_jawaban)
            if item != last_question:
                break
        last_question = item

        print(f"\nSoal {i}/{jumlah}: {item['soal']}")
        jawaban_user = input("Jawaban: ").strip()

        if jawaban_user.lower() == "exit":
            print("\nKeluar dari kuis...\n")
            break

        if is_correct(jawaban_user, item["jawaban"]):
            print("✅ Benar!")
            skor += 1
        else:
            print(f"❌ Salah. Jawaban benar: {item['jawaban'][0]}")
            salah_list.append({
                "soal": item["soal"],
                "jawaban_user": jawaban_user,
                "jawaban_benar": item["jawaban"]
            })

    print("\n=== HASIL AKHIR ===")
    print(f"Skor: {skor}/{i}")
    persen = (skor / i) * 100 if i > 0 else 0
    print(f"Persentase: {persen:.2f}%")

    if salah_list:
        print("\nSoal yang salah:")
        for n, s in enumerate(salah_list, 1):
            benar_display = ", ".join(s["jawaban_benar"])
            print(f"{n}. {s['soal']}")
            print(f"   Jawaban kamu : {s['jawaban_user']}")
            print(f"   Jawaban benar: {benar_display}")
    else:
        print("\nMantap! Semua benar 🎉")

if __name__ == "__main__":
    main()
