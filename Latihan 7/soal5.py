T = int(input().strip())
strings = [input().strip() for _ in range(T)]
hasil = []

for s in strings:
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1

    for cl in range(2, n + 1):
        for i in range(0, n - cl + 1):
            j = i + cl - 1
            if s[i] == s[j]:
                if cl == 2:
                    dp[i][j] = 2
                else:
                    dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    hasil.append(dp[0][n - 1])

# tampilkan semua output sekaligus
for h in hasil:
    print(h)
