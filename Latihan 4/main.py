# main.py
from task_manager import (
    tambah_tugas,
    lihat_tugas,
    tandai_selesai,
    hapus_tugas,
    cari_tugas,
    lihat_statistik
)

def main():
    while True:
        print("=== SISTEM MANAJEMEN TUGAS ===")
        print("1. Tambah Tugas")
        print("2. Lihat Semua Tugas")
        print("3. Tandai Tugas Selesai")
        print("4. Hapus Tugas")
        print("5. Cari Tugas")
        print("6. Lihat Statistik")
        print("0. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nama = input("Masukkan nama tugas: ")
            tambah_tugas(nama)

        elif pilihan == "2":
            lihat_tugas()

        elif pilihan == "3":
            lihat_tugas()
            try:
                index = int(input("Masukkan nomor tugas yang ingin ditandai selesai: ")) - 1
                tandai_selesai(index)
            except ValueError:
                print("Input harus berupa angka.\n")

        elif pilihan == "4":
            lihat_tugas()
            try:
                index = int(input("Masukkan nomor tugas yang ingin dihapus: ")) - 1
                hapus_tugas(index)
            except ValueError:
                print("Input harus berupa angka.\n")

        elif pilihan == "5":
            keyword = input("Masukkan kata kunci pencarian: ")
            cari_tugas(keyword)

        elif pilihan == "6":
            lihat_statistik()

        elif pilihan == "0":
            print("Terima kasih telah menggunakan program ini. Keluar...")
            break

        else:
            print("Pilihan tidak valid, coba lagi.\n")


if __name__ == "__main__":
    main()