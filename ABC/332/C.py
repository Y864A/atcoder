N,M = map(int, input().split())

S = input()

cnt_muji = 0
cnt_logo = 0
cnt_buy = 0
for i in range(N):
    if S[i] == '0':
        cnt_buy = max(cnt_buy, cnt_logo)
        cnt_muji = 0
        cnt_logo = 0
    elif S[i] == '1':
        if cnt_muji < M:
            cnt_muji += 1
        else:
            cnt_logo += 1
    else:
        cnt_logo += 1

if cnt_logo > 0:
    cnt_buy = max(cnt_buy, cnt_logo)

print(cnt_buy)