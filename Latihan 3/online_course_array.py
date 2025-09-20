# Daftar kursus dan kuota
courses = ["Python Dasar", "Web Development",
           "Excel untuk Pemula", "Algoritma Pemrograman", "Grafik Desain"]
quota = [2, 2, 1, 2, 0]  # urut sesuai courses

# Kursus yang diambil user
user_courses = []
max_courses = 3

print("Pendaftaran Kursus Online\n")

# loop untuk memilih kursus
while len(user_courses) < max_courses:
    print("\nDaftar Kursus Tersedia:")
    # loop untuk menampilkan kursus dan kuota
    for i in range(len(courses)):
        print(i + 1, courses[i], "(tersisa", quota[i], "kuota)")

    # input pilihan kursus
    pilihan = input(
        "\nPilih kursus berdasarkan nomor (atau ketik 'selesai' untuk berhenti): ")

    # validasi berhenti dan input harus angka
    if pilihan.lower() == "selesai":
        break
    if not pilihan.isdigit():
        print("Hanya menerima input angka. Coba lagi")
        continue

    # inisialisasi index kursus
    idx = int(pilihan) - 1

    # validasi index kursus
    if idx < 0 or idx >= len(courses):
        print("Pilihan tidak valid, coba lagi.")
        continue

    # Pengecekan kuota dan apakah user sudah daftar
    if quota[idx] <= 0:
        print("Gagal, Kuota", courses[idx], "sudah penuh.")
    elif courses[idx] in user_courses:
        print("Gagal, Kamu sudah terdaftar di", courses[idx])
    else:
        user_courses.append(courses[idx])
        quota[idx] -= 1
        print("Berhasil mendaftar di", courses[idx])

    # Status pendaftaran user setiap kali loop
    print("\nStatus Pendaftaran Kamu:")
    for c in user_courses:
        print("-", c)
    print("Jumlah kursus yang sudah diambil:",
          len(user_courses), "/", max_courses)

# kursus yang diambil user
print("Kursus yang Kamu ambil:")
for c in user_courses:
    print("-", c)
