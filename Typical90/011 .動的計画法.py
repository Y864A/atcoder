N = int(input())
dcs = [list(map(int, input().split())) for _ in range(N)]
dcs.sort()

dp = [0] * 5001
for d, c, s in dcs:
    for i in range(d-c, -1, -1):
        dp[i + c] = max(dp[i + c], dp[i] + s)
    print(dp[0:10])
print(max(dp))