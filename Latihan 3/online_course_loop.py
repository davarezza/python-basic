# Kuota kursus
python_dasar_quota = 2
data_science_quota = 1
web_dev_quota = 2
grafis_desain_quota = 1

# Kursus yang diambil user
user_course1 = ""
user_course2 = ""
user_course3 = ""
jumlah_course = 0
max_courses = 3

# loop untuk memilih kursus
while jumlah_course < max_courses:
    print("\nDaftar Kursus:")
    print(f"1. Python Dasar (tersisa {python_dasar_quota})")
    print(f"2. Data Science (tersisa {data_science_quota})")
    print(f"3. Web Development (tersisa {web_dev_quota})")
    print(f"4. Grafik Desain (tersisa {grafis_desain_quota})")

    pilihan = input("Pilih nomor kursus (atau ketik selesai): ")
    if pilihan.lower() == "selesai":
        break

    # pengkondisian pilihan kursus nomor 1 (logikanya sama untuk pilihan 2, 3, dan 4)
    if pilihan == "1":
        # Cek apakah user sudah mengambil kursus ini sebelumnya
        if user_course1 == "Python Dasar" or user_course2 == "Python Dasar" or user_course3 == "Python Dasar":
            print("Gagal daftar: Kamu sudah mengambil Python Dasar sebelumnya.")
        # Cek apakah kuota kursus sudah penuh
        elif python_dasar_quota <= 0:
            print("Gagal daftar: Kuota Python Dasar sudah penuh.")
        # Jika lolos kedua pengecekan di atas, maka user bisa mendaftar
        else:
            jumlah_course += 1
            if user_course1 == "":
                user_course1 = "Python Dasar"
            elif user_course2 == "":
                user_course2 = "Python Dasar"
            else:
                user_course3 = "Python Dasar"
            python_dasar_quota -= 1
            print("Berhasil daftar di Python Dasar")

    # pengkondisian pilihan kursus nomor 2
    elif pilihan == "2":
        if user_course1 == "Data Science" or user_course2 == "Data Science" or user_course3 == "Data Science":
            print("Gagal daftar: Kamu sudah mengambil Data Science sebelumnya.")
        elif data_science_quota <= 0:
            print("Gagal daftar: Kuota Data Science sudah penuh.")
        else:
            jumlah_course += 1
            if user_course1 == "":
                user_course1 = "Data Science"
            elif user_course2 == "":
                user_course2 = "Data Science"
            else:
                user_course3 = "Data Science"
            data_science_quota -= 1
            print("Berhasil daftar di Data Science")

    # pengkondisian pilihan kursus nomor 3
    elif pilihan == "3":
        if user_course1 == "Web Development" or user_course2 == "Web Development" or user_course3 == "Web Development":
            print("Gagal daftar: Kamu sudah mengambil Web Development sebelumnya.")
        elif web_dev_quota <= 0:
            print("Gagal daftar: Kuota Web Development sudah penuh.")
        else:
            jumlah_course += 1
            if user_course1 == "":
                user_course1 = "Web Development"
            elif user_course2 == "":
                user_course2 = "Web Development"
            else:
                user_course3 = "Web Development"
            web_dev_quota -= 1
            print("Berhasil daftar di Web Development")

    # pengkondisian pilihan kursus nomor 4
    elif pilihan == "4":
        if user_course1 == "Grafik Desain" or user_course2 == "Grafik Desain" or user_course3 == "Grafik Desain":
            print("Gagal daftar: Kamu sudah mengambil Grafik Desain sebelumnya.")
        elif grafis_desain_quota <= 0:
            print("Gagal daftar: Kuota Grafik Desain sudah penuh.")
        else:
            jumlah_course += 1
            if user_course1 == "":
                user_course1 = "Grafik Desain"
            elif user_course2 == "":
                user_course2 = "Grafik Desain"
            else:
                user_course3 = "Grafik Desain"
            grafis_desain_quota -= 1
            print("Berhasil daftar di Grafik Desain")

    else:
        print("Pilihan tidak valid.")

    # Status pendaftaran (langsung inline)
    print("\nKursus yang sudah Kamu ambil:")
    if user_course1 != "":
        print("-", user_course1)
    if user_course2 != "":
        print("-", user_course2)
    if user_course3 != "":
        print("-", user_course3)
    if jumlah_course == 0:
        print("Belum ada kursus yang diambil.")
    print(f"Total: {jumlah_course}/{max_courses}")

# Rangkuman pendaftaran
print("\nRangkuman Pendaftaran")
print("Kursus yang sudah Kamu ambil:")
if user_course1 != "":
    print("-", user_course1)
if user_course2 != "":
    print("-", user_course2)
if user_course3 != "":
    print("-", user_course3)
if jumlah_course == 0:
    print("Belum ada kursus yang diambil.")
print(f"Total: {jumlah_course}/{max_courses}")
print("Terima kasih sudah mengambil kursus kami.")
