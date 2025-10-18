T = int(input())
for _ in range(T):
    parts = list(map(int, input().split()))
    n = parts[0]
    scores = parts[1:1+n]

    m = n * (n - 1) // 2
    total = sum(scores)

    ok = True
    # harus ada tepat n skor
    if len(scores) != n:
        ok = False
    # total poin harus antara 2*m dan 3*m
    elif not (2 * m <= total <= 3 * m):
        ok = False
    else:
        # setiap skor harus di rentang 0 .. 3*(n-1)
        for s in scores:
            if s < 0 or s > 3 * (n - 1):
                ok = False
                break

    print("YES" if ok else "NO")
