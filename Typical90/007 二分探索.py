import bisect

N = int(input())
A = list(map(int, input().split()))
Q = int(input())

A_sort = sorted(A)
for _ in range(Q):
    B = int(input())
    index = bisect.bisect_left(a=A_sort, x=B)
    if index == 0:
        print(abs(A_sort[index] - B))
    elif index == N:
        print(abs(A_sort[index - 1] - B))
    else:
        a = abs(A_sort[index-1] - B)
        b = abs(A_sort[index] - B)
        print(min(a, b))
        


