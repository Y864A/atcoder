INF = 10 ** 18

N = int(input())
A = list(map(int, input().split()))
dp = [[INF for _ in range(2 * N + 1 )] for _ in range(2 * N + 1)]

# 初期化
for i in range(1, 2 * N + 1):
    dp[i][i] = 0
    
for l in range(2 * N + 1):
    for r in range(2 * N + 1):
        if l > r:
            dp[l][r] = 0

# 更新（全て 1-indexed）
for span in range(2, 2 * N + 1 , 2):
    for l in range(1, 2 * N):
        r = l + span - 1
        if r > 2 * N:
            continue
        for mid in range(l, r, 2):
            dp[l][r] = min(dp[l][r], dp[l][mid -1] + dp[mid][r])
        dp[l][r] = min(dp[l][r], dp[l + 1][r - 1] + abs(A[l - 1] - A[r - 1]))
print(dp[1][N * 2])