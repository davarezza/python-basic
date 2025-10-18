N = int(input("masukkan nilai : "))
nilai = [int(input()) for _ in range(N)]
nilai.sort()

if N % 2 == 1 :
    median = nilai[N // 2]
else :
    median = (nilai[N // 2 - 1] + nilai[N // 2])/2
print(f"median dari data tersebut adalah {median:.1f}")
