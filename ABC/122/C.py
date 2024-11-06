N, Q = map(int, input().split())

S = input()
s_cnt = [0]
cnt = 0
for i in range(1, N):
    if S[i - 1] == 'A' and S[i] == 'C':
        cnt += 1
    s_cnt.append(cnt)
    
for i in range(Q):
    l,r = map(int, input().split())
    print(s_cnt[r - 1] - s_cnt[l - 1])
            
