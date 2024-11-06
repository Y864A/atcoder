N = int(input())

A = {}
for i in range(1, 101):
    A[i] = 0
    
for i in range(N):
    n = int(input())
    A[n] += 1
    
cnt = 0
for i in range(1, len(A)):
    if A[i] > 0:
        cnt += 1
        
print(cnt)