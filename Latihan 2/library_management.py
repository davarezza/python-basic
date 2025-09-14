# Input Nama dan Hari Peminjaman
nama_peminjam = input("Masukkan nama peminjam: ")
hari_peminjaman = int(input("Masukkan lama peminjaman (1-30 hari): "))

# Validasi Input Hari Peminjaman
while hari_peminjaman < 1 or hari_peminjaman > 30:
    print("Input tidak valid, harap masukkan angka antara 1-30")
    hari_peminjaman = int(input("Masukkan lama peminjaman (1-30 hari): "))

# Input Banyak Buku yang Dipinjam
banyak_buku = int(
    input("Masukkan banyak buku yang dipinjam (maksimal 5 buah): "))

# Validasi Input Banyak Buku
while banyak_buku < 1 or banyak_buku > 5:
    print("Input tidak valid, harap masukkan angka antara 1-5")
    banyak_buku = int(
        input("Masukkan banyak buku yang dipinjam (maksimal 5 buah): "))

# Inisialisasi Variabel
biaya_per_hari = 2000
total_biaya = 0

# Pengulangan untuk Memasukkan Judul Setiap Buku dan Menghitung Biaya
for i in range(banyak_buku):
    judul_buku = input(f"Masukkan judul buku ke-{i+1}: ")
    biaya_buku = biaya_per_hari * hari_peminjaman
    total_biaya += biaya_buku

    # Menampilkan Detail Peminjaman di Setiap Buku
    print(f"\n--- Detail Peminjaman Buku ke-{i+1} ---")
    print(f"Judul Buku: {judul_buku}")
    print(f"Nama Peminjam: {nama_peminjam}")
    print(f"Lama Peminjaman: {hari_peminjaman} hari")
    print(f"Biaya Peminjaman: Rp {biaya_buku:,.2f}")
    print()

# Menampilkan Total Biaya Peminjaman
print(f"Total Biaya Peminjaman: Rp {total_biaya:,.2f}")
print("Terima kasih telah meminjam buku di perpustakaan kami!")
