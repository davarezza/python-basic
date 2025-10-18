import math

N = int(input())
frekuensi = [int(input()) for _ in range(N)]

def kpk(a,b):
    return a * b // math.gcd (a,b)

hasil = frekuensi[0]
for i in range(1 , N):
    hasil = kpk(hasil, frekuensi[i])

print(hasil)