S = input()
A = []
cnt_upper = 0
s_i = 0
e_i = 0
for i in range(len(S)):
    if S[i].isupper() and cnt_upper == 0:
        s_i = i
        cnt_upper += 1
    elif S[i].isupper() and cnt_upper == 1:
        cnt_upper = 0
        e_i = i
        sub_s = S[s_i:e_i+1]
        A.append(sub_s)
        
A = sorted(A, key=str.lower)
print("".join(A))