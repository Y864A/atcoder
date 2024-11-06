N, Y = map(int, input().split())

a, b, c = -1, -1, -1
for i in range(N+1):
    for j in range(N+1):
        price = i * 10000 + j * 5000
        rest = N - i - j
        if price + rest * 1000 == Y and rest >= 0 :
            a,b,c = i, j, rest

print(a,b,c)