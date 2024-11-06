S = input()
ans = 0
def dfs(A):
    if len(A) == len(S)-1:
        B = list()
        arr = list(A)
        s = S[0]
        for i in range(len(arr)):
            if arr[i] == '1':
                B.append(int(s))
                s = ""
                s += S[i + 1]
            else:
                s += S[i + 1]
        B.append(int(s))
        global ans
        ans += sum(B)
    else:
        dfs(A + "0")
        dfs(A + "1")
        
dfs("")
print(ans)