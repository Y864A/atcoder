A,B,C = map(int, input().split())

if A+B < C:
    print(B+A+B+1)
else:
    print(B+C)