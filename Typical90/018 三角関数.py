import math
T = int(input())
L,X,Y = map(int, input().split())
Z = 0
Q = int(input())

for _ in range(Q):
    _t = int(input())
    t = (_t - (T * 0.25)) / T
    sin = math.sin(t * 2 * math.pi)
    cos = math.cos(t * 2 * math.pi)
    x = 0
    y = - cos * (L / 2)
    z = sin * (L / 2) + (L / 2)
    a = math.sqrt(X ** 2 + (y - Y) ** 2)
    theta = math.atan(z / a)
    print(math.degrees(theta))