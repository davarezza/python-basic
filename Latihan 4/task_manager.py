# task_manager.py
tasks = []

# Fungsi untuk menambah tugas baru
def tambah_tugas(task_name):
    tugas = {"nama": task_name, "selesai": False}
    tasks.append(tugas)
    return tugas

# Fungsi untuk mengambil semua tugas
def semua_tugas():
    return tasks

# Fungsi untuk menandai tugas selesai
def tandai_tugas_selesai(index):
    if 0 <= index < len(tasks):
        tasks[index]["selesai"] = True
        return tasks[index]
    return None

# Fungsi untuk menghapus tugas
def hapus_tugas(index):
    if 0 <= index < len(tasks):
        return tasks.pop(index)
    return None

# Fungsi rekursif untuk mencari tugas berdasarkan keyword
def cari_tugas_rekursif(keyword, index=0, hasil=None):
    if hasil is None:
        hasil = []
    if index == len(tasks):
        return hasil
    if keyword.lower() in tasks[index]["nama"].lower():
        hasil.append(tasks[index])
    return cari_tugas_rekursif(keyword, index + 1, hasil)

# Fungsi pencarian (menggunakan rekursif)
def cari_tugas(keyword):
    return cari_tugas_rekursif(keyword)

# Fungsi melihat statistik tugas
def lihat_statistik():
    total = len(tasks)
    selesai = sum(1 for t in tasks if t["selesai"])
    belum = total - selesai
    return {
        "total": total,
        "selesai": selesai,
        "belum": belum
    }
