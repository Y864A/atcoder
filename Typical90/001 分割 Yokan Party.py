N,L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

def check(x):
    cnt = 0
    pre = 0
    for i in range(N):
        if A[i] - pre >= x:
            cnt += 1
            pre = A[i]
    
    if L - pre >= x:
        cnt += 1

    return (cnt >= K + 1)

left = -1
right = L + 1
while right - left > 1:
    mid = (left + right) // 2
    if check(mid):
        left = mid
    else:
        right = mid

print(left)