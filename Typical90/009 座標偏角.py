import math
import bisect
import numpy as np

N = int(input())
X = []
Y = []

for i in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
ans = 0

def to_acc(x):
    # 角度を0~180度に変換
    x = x % 360
    if x > 180:
        x = 360 - x
    return x


for i in range(N):
    angles = []
    for j in range(N):
        if i == j:
            continue
        angles.append(math.atan2(Y[j] - Y[i], X[j] - X[i]) * 180 / math.pi)
    angles.sort()
    angles.extend([angle + 360 for angle in angles])

    for j in range(N - 1):
        # angle[j]+180に最も近いものを探す
        # angle[j]+180以上の最小のindexを探す
        idx = bisect.bisect_left(angles, angles[j] + 180)
        ans = max(ans, to_acc(angles[idx] - angles[j]))
        if idx:
            ans = max(ans, to_acc(angles[idx - 1] - angles[j]))

print(ans)