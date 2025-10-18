N = int(input())
for _ in range(N):
    line = list(map(int, input().split()))
    tim = line[0]
    skor = line[1:tim+1]
    pertandingan = tim * (tim - 1) // 2
    total_skor = sum(skor)
    if 2 * pertandingan <= total_skor * 3 :
        print("YES")
    else : 
        print("NO")  