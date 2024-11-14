a,b,c = map(int, input().split())

"""
この問題はlog2 a < b * log2 c を比較しても判定が失敗する。
log2 n は割り切れない数において、小さな誤差が生じる。
log2 M < log2 N  → M < N
という性質を用いる
log2 M < log2 N は、この問題なら log2 a < b * log2 c なので、
b * log2 c → c ** 2 なので、 a < c ** b を比較すると正確に判定できる。
"""

if a < c ** b:
    print("Yes")
else:
    print("No")