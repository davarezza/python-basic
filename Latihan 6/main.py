import data_mahasiswa

def main():
    while True:
        print("\nSistem Pengelolaan Data Mahasiswa")
        print("a. Tambah Data Mahasiswa")
        print("b. Hapus Data Mahasiswa")
        print("c. Tampilkan Data Mahasiswa")
        print("d. Keluar")

        pilihan = input("Pilih opsi (a/b/c/d): ").strip().lower()

        if pilihan == "a":
            data_mahasiswa.tambah_data()
        elif pilihan == "b":
            data_mahasiswa.hapus_data()
        elif pilihan == "c":
            data_mahasiswa.tampilkan_data()
        elif pilihan == "d":
            print("Terima kasih telah menggunakan sistem")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()
