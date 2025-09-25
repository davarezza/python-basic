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