
from itertools import product

# 有効な文字列か判定する
def is_valid(S):
    # かっこの数が違うなら無効
    if S.count("(") != S.count(")"):
        return False
    # かっこの組み合わせを管理する
    score = 0
    for s in S:
        if s == ("("):
            score += 1
        if s == (")"):
            score -= 1
        # 途中でscoreが負の値 = ()の対応があっていない
        if score < 0: 
            return False
    
    return True

N = int(input())
for S in product(['(', ')'], repeat=N):
    if is_valid(S):
        print(*S, sep='')