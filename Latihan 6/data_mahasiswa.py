import csv
import os

FILENAME = "mahasiswa.txt"

# Memuat data dari file CSV ke list of dict
def load_data():
    students = []
    if not os.path.exists(FILENAME):
        return students
    with open(FILENAME, mode="r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) >= 3:
                students.append({"nim": row[0], "nama": row[1], "jurusan": row[2]})
    return students

# Menyimpan data ke file CSV
def save_data(students):
    with open(FILENAME, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for s in students:
            writer.writerow([s["nim"], s["nama"], s["jurusan"]])

# Menambah data
def tambah_data():
    students = load_data()
    nim = input("Masukkan NIM: ").strip()
    # Cek duplikat
    for s in students:
        if s["nim"] == nim:
            print("NIM sudah terdaftar.")
            return
    nama = input("Masukkan Nama: ").strip()
    jurusan = input("Masukkan Jurusan: ").strip()
    students.append({"nim": nim, "nama": nama, "jurusan": jurusan})
    save_data(students)
    print("Data berhasil ditambahkan.")

# Menghapus data
def hapus_data():
    students = load_data()
    if not students:
        print("Belum ada data.")
        return
    nim = input("Masukkan NIM yang akan dihapus: ").strip()
    new_students = [s for s in students if s["nim"] != nim]
    if len(new_students) == len(students):
        print("NIM tidak ditemukan.")
        return
    save_data(new_students)
    print("Data berhasil dihapus.")

# Menampilkan data
def tampilkan_data():
    students = load_data()
    if not students:
        print("Belum ada data.")
        return
    print(f"{'NIM':<15} {'Nama':<40} {'Jurusan'}")
    for s in students:
        print(f"{s['nim']:<15} {s['nama']:<40} {s['jurusan']}")
