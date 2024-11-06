N = int(input())

flg = True
pt, px, py = 0,0,0
for i in range(N):
    t,x,y = map(int, input().split())
    T = t - pt
    X = abs(x - px)
    Y = abs(y - py)
    if T < (X + Y):
        flg = False
    if not (T % 2 == (X + Y) % 2 ):
        flg = False
    pt = t  
    px = x
    py = y

if flg:
    print("Yes")
else:
    print("No")