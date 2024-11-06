N = int(input())
A = {}

for i in range(N):
    string = input()
    s = "".join(sorted(string))
    if s in A:
        A[s] += 1
    else:   
        A[s] = 1
ans = 0
for a in A.values():
    ans += int (a * (a - 1) // 2)
    
print(ans)