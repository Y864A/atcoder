N = int(input())
A, B, C = map(int, input().split())

ans = 10000

for i in range(10000):
    for j in range(10000):
        val = i * A + j * B
        if N < val or (N - val) % C != 0:
            continue  
        ans = min(ans, (i + j + (N - val)// C))

print(ans)