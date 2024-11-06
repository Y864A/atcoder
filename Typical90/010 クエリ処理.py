N = int(input())
class_dic = {}
class_dic[1] = [0]
class_dic[2] = [0]
for i in range(1, N+1):
    class_dic[1].append(0)
    class_dic[2].append(0)
    c, p = map(int, input().split())
    class_dic[c][i] = p
    class_dic[1][i] = class_dic[1][i] + class_dic[1][i-1]
    class_dic[2][i] = class_dic[2][i] + class_dic[2][i-1]
Q = int(input())
for i in range(Q):
    l, r = map(int, input().split())
    sum1 = class_dic[1][r] - class_dic[1][l-1]
    sum2 = class_dic[2][r] - class_dic[2][l-1]
    
    print(sum1, sum2)
