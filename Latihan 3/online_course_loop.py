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

    # input pilihan dan validasi berhenti
    pilihan = input("Pilih nomor kursus (atau ketik selesai): ")
    if pilihan.lower() == "selesai":
        break

    # pengkondisian pilihan kursus nomor 1
    if pilihan == "1":
        # Pengecekan kuota apakah user sudah daftar
        if python_dasar_quota > 0 and not (user_course1 == "Python Dasar" or user_course2 == "Python Dasar" or user_course3 == "Python Dasar"):
            jumlah_course += 1
            if user_course1 == "":
                user_course1 = "Python Dasar"
            elif user_course2 == "":
                user_course2 = "Python Dasar"
            else:
                user_course3 = "Python Dasar"
            python_dasar_quota -= 1
            print("Berhasil daftar di Python Dasar")
        else:
            print("Gagal daftar (kuota penuh / sudah terdaftar)")

    # pengkondisian pilihan kursus nomor 2
    elif pilihan == "2":
        # Pengecekan kuota apakah user sudah daftar
        if data_science_quota > 0 and not (user_course1 == "Data Science" or user_course2 == "Data Science" or user_course3 == "Data Science"):
            jumlah_course += 1
            if user_course1 == "":
                user_course1 = "Data Science"
            elif user_course2 == "":
                user_course2 = "Data Science"
            else:
                user_course3 = "Data Science"
            data_science_quota -= 1
            print("Berhasil daftar di Data Science")
        else:
            print("Gagal daftar (kuota penuh / sudah terdaftar)")

    # pengkondisian pilihan kursus nomor 3
    elif pilihan == "3":
        # Pengecekan kuota apakah user sudah daftar
        if web_dev_quota > 0 and not (user_course1 == "Web Development" or user_course2 == "Web Development" or user_course3 == "Web Development"):
            jumlah_course += 1
            if user_course1 == "":
                user_course1 = "Web Development"
            elif user_course2 == "":
                user_course2 = "Web Development"
            else:
                user_course3 = "Web Development"
            web_dev_quota -= 1
            print("Berhasil daftar di Web Development")
        else:
            print("Gagal daftar (kuota penuh / sudah terdaftar)")

    # pengkondisian pilihan kursus nomor 4
    elif pilihan == "4":
        # Pengecekan kuota apakah user sudah daftar
        if grafis_desain_quota > 0 and not (user_course1 == "Grafik Desain" or user_course2 == "Grafik Desain" or user_course3 == "Grafik Desain"):
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
            print("Gagal daftar (kuota penuh / sudah terdaftar)")

    else:
        print("Pilihan tidak valid.")

    # Status pendaftaran
    print("\nKursus yang sudah Anda ambil:")
    if user_course1 != "":
        print("-", user_course1)
    if user_course2 != "":
        print("-", user_course2)
    if user_course3 != "":
        print("-", user_course3)
    print(f"Total: {jumlah_course}/{max_courses}")
