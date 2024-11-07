N = int(input())
MOD = 10**9 + 7

fact = [1]
# 事前に階乗を計算しておく
for i in range(1, N+1):
    fact.append(fact[-1]*i%MOD)
fact_inv = []
for f in fact:
    fact_inv.append(pow(f, -1, MOD))

for k in range(1, N + 1):
    dp = 0
    p = N
    for r in range(1, (N - 1 )//k+2):
        p = N - (k - 1) * (r - 1)
        dp += (fact[p] * fact_inv[r]) % MOD * fact_inv[p-r] % MOD
        dp %= MOD
    print(dp)
