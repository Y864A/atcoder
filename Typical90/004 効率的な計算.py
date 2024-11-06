H, W = map(int, input().split())
A = []
for i in range(H):
    A.append(list(map(int, input().split())))

"""
配列を十字に足し合わせる場合は、
列の合計 + 行の合計 - 中心の値となる。
事前に列の合計と行の合計を計算しておくことで、
計算量を減らすことができる。
"""

A_w = []
A_h = []
for i in range(H):
    A_w.append(sum(A[i]))
for i in range(W):
    sum_w = 0
    for j in range(H):
        sum_w += A[j][i]
    A_h.append(sum_w) 

B = [[0 for i in range(W)] for i in range(H)]
for h in range(H):
    for w in range(W):
        B[h][w] = A_w[h] + A_h[w] - A[h][w]

for i in range(H):
    print(" ".join(map(str, B[i])))