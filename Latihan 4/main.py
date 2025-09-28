from task_manager import (
    tambah_tugas,
    semua_tugas,
    tandai_tugas_selesai,
    hapus_tugas,
    cari_tugas,
    lihat_statistik
)

def main():
    while True:
        print("SISTEM MANAJEMEN TUGAS")
        print("1. Tambah Tugas")
        print("2. Lihat Semua Tugas")
        print("3. Tandai Tugas Selesai")
        print("4. Hapus Tugas")
        print("5. Cari Tugas")
        print("6. Lihat Statistik")
        print("0. Keluar")

        pilihan = input("Pilih menu: ")

        # Tambah tugas
        if pilihan == "1":
            nama = input("Masukkan nama tugas: ")
            tugas = tambah_tugas(nama)
            print(f"Tugas '{tugas['nama']}' berhasil ditambahkan.\n")

        # Lihat semua tugas
        elif pilihan == "2":
            semua = semua_tugas()
            if not semua:
                print("Belum ada tugas.\n")
            else:
                print("\nDaftar Tugas:")
                for i, t in enumerate(semua, start=1):
                    status = "Selesai" if t["selesai"] else "Belum"
                    print(f"{i}. {t['nama']} - {status}")
                print()

        # Tandai tugas selesai
        elif pilihan == "3":
            semua = semua_tugas()
            if not semua:
                print("Belum ada tugas.\n")
                continue
            for i, t in enumerate(semua, start=1):
                status = "Selesai" if t["selesai"] else "Belum"
                print(f"{i}. {t['nama']} - {status}")
            try:
                index = int(input("Masukkan nomor tugas yang ingin ditandai selesai: ")) - 1
                hasil = tandai_tugas_selesai(index)
                if hasil:
                    print(f"Tugas '{hasil['nama']}' berhasil ditandai selesai.\n")
                else:
                    print("Nomor tugas tidak valid.\n")
            except ValueError:
                print("Input harus berupa angka.\n")

        # Hapus tugas
        elif pilihan == "4":
            semua = semua_tugas()
            if not semua:
                print("Belum ada tugas.\n")
                continue
            for i, t in enumerate(semua, start=1):
                status = "Selesai" if t["selesai"] else "Belum"
                print(f"{i}. {t['nama']} - {status}")
            try:
                index = int(input("Masukkan nomor tugas yang ingin dihapus: ")) - 1
                removed = hapus_tugas(index)
                if removed:
                    print(f"Tugas '{removed['nama']}' telah dihapus.\n")
                else:
                    print("Nomor tugas tidak valid.\n")
            except ValueError:
                print("Input harus berupa angka.\n")

        # Cari tugas
        elif pilihan == "5":
            keyword = input("Masukkan kata kunci pencarian: ")
            hasil = cari_tugas(keyword)
            if hasil:
                print("\nHasil pencarian:")
                for t in hasil:
                    status = "Selesai" if t["selesai"] else "Belum"
                    print(f"- {t['nama']} - {status}")
            else:
                print("Tidak ada tugas yang cocok.\n")

        # Lihat statistik
        elif pilihan == "6":
            stats = lihat_statistik()
            print("\nStatistik:")
            print(f"Total tugas     : {stats['total']}")
            print(f"Tugas selesai   : {stats['selesai']}")
            print(f"Tugas belum     : {stats['belum']}\n")

        # Keluar
        elif pilihan == "0":
            print("Terima kasih telah menggunakan program ini.")
            break

        else:
            print("Pilihan tidak valid, coba lagi.\n")


if __name__ == "__main__":
    main()
