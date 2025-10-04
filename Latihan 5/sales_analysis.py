# Data penjualan dalam bentuk list (matriks)
penjualan = [
    [120, 150, 130, 170, 200, 190],  # Produk A
    [80, 100, 90, 110, 130, 120],    # Produk B
    [200, 210, 190, 180, 220, 210]   # Produk C
]

produk = ["Produk A", "Produk B", "Produk C"]
bulan = ["Jan", "Feb", "Mar", "Apr", "Mei", "Jun"]


# Menghitung total penjualan setiap produk
def hitung_total(penjualan, produk):
    total_penjualan = {}
    for i in range(len(penjualan)):
        total_penjualan[produk[i]] = sum(penjualan[i])
    return total_penjualan


# Mencari bulan penjualan tertinggi dan terendah
def cari_tertinggi_terendah(penjualan, produk, bulan):
    info_penjualan = {}
    for i in range(len(penjualan)):
        data = penjualan[i]
        tertinggi = max(data)
        terendah = min(data)
        bulan_tertinggi = bulan[data.index(tertinggi)]
        bulan_terendah = bulan[data.index(terendah)]

        info_penjualan[produk[i]] = {
            "Penjualan Tertinggi": (bulan_tertinggi, tertinggi),
            "Penjualan Terendah": (bulan_terendah, terendah)
        }
    return info_penjualan


# Mendeteksi lonjakan penjualan
def deteksi_lonjakan(penjualan, produk, bulan, persen=0.2):
    lonjakan = {}
    for i in range(len(penjualan)):
        data = penjualan[i]
        rata_rata = sum(data) / len(data)
        ambang = rata_rata * (1 + persen)
        bulan_lonjakan = []

        for j in range(len(data)):
            if data[j] > ambang:
                bulan_lonjakan.append((bulan[j], data[j]))

        lonjakan[produk[i]] = {
            "Rata-rata": round(rata_rata, 2),
            "Ambang Batas": round(ambang, 2),
            "Lonjakan": bulan_lonjakan if bulan_lonjakan else "Tidak ada lonjakan signifikan"
        }
    return lonjakan

# Analisis data penjualan
total = hitung_total(penjualan, produk)
info = cari_tertinggi_terendah(penjualan, produk, bulan)
lonjakan = deteksi_lonjakan(penjualan, produk, bulan)

# Gabungkan semua hasil dalam satu dictionary
hasil_analisis = {
    "Total Penjualan": total,
    "Info Penjualan": info,
    "Lonjakan Penjualan": lonjakan
}

# Tampilkan hasil
print("HASIL ANALISIS PENJUALAN\n")

# Menampilkan total penjualan
print("1. Total Penjualan:")
for p, total in hasil_analisis["Total Penjualan"].items():
    print(f"   - {p}: {total}")

# Menampilkan info penjualan tertinggi dan terendah
print("\n2. Penjualan Tertinggi dan Terendah:")
for p, info in hasil_analisis["Info Penjualan"].items():
    print(f"   - {p}:")
    print(f"     Tertinggi: {info['Penjualan Tertinggi'][0]} ({info['Penjualan Tertinggi'][1]})")
    print(f"     Terendah: {info['Penjualan Terendah'][0]} ({info['Penjualan Terendah'][1]})")

# Menampilkan lonjakan penjualan
print("\n3. Lonjakan Penjualan:")
for p, data in hasil_analisis["Lonjakan Penjualan"].items():
    print(f"   - {p}:")
    print(f"     Rata-rata: {data['Rata-rata']}")
    print(f"     Ambang Batas: {data['Ambang Batas']}")
    print(f"     Lonjakan: {data['Lonjakan']}")
