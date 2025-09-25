tasks = []

# Fungsi untuk menambah tugas baru
def tambah_tugas(task_name: str):
    tasks.append({"nama": task_name, "selesai": False})
    print(f"Tugas '{task_name}' berhasil ditambahkan.\n")
   
# Fungsi untuk menampilkan semua tugas    
def lihat_tugas():
    if not tasks:
        print("Belum ada tugas.\n")
        return
    print("\nDaftar Tugas:")
    for i, task in enumerate(tasks, start=1):
        status = "Selesai" if task["selesai"] else "Belum"
        print(f"{i}. {task['nama']} - {status}")
    print()

# Fungsi untuk menandai tugas selesai
def tandai_selesai(index: int):
    if 0 <= index < len(tasks):
        tasks[index]["selesai"] = True
        print(f"Tugas '{tasks[index]['nama']}' telah ditandai selesai.\n")
    else:
        print("Nomor tugas tidak valid.\n")
        
# Fungsi untuk menghapus tugas
def hapus_tugas(index: int):
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"Tugas '{removed['nama']}' telah dihapus.\n")
    else:
        print("Nomor tugas tidak valid.\n")
        
# Fungsi rekursif untuk mencari tugas
def cari_tugas_rekursif(keyword: str, index=0, hasil=None):
    if hasil is None:
        hasil = []

    # Basis rekursi: jika sudah sampai akhir daftar
    if index == len(tasks):
        return hasil

    # Cek apakah tugas cocok
    if keyword.lower() in tasks[index]["nama"].lower():
        hasil.append(tasks[index])

    # Panggil rekursif untuk indeks berikutnya
    return cari_tugas_rekursif(keyword, index + 1, hasil)


# Fungsi utama untuk pencarian
def cari_tugas(keyword: str):
    hasil = cari_tugas_rekursif(keyword)
    if hasil:
        print("\nHasil pencarian:")
        for t in hasil:
            status = "Selesai" if t["selesai"] else "Belum"
            print(f"- {t['nama']} - {status}")
    else:
        print("Tidak ada tugas yang cocok.\n")
        
# Fungsi untuk melihat statistik tugas
def lihat_statistik():
    total = len(tasks)
    selesai = sum(1 for t in tasks if t["selesai"])
    belum = total - selesai
    print(f"\nStatistik:")
    print(f"Total tugas     : {total}")
    print(f"Tugas selesai   : {selesai}")
    print(f"Tugas belum     : {belum}\n")