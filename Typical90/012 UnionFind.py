class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
    
    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
    
    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if not x_root == y_root:
            if self.size[x_root] < self.size[y_root]:
                x_root, y_root = y_root, x_root
            self.parent[y_root] = x_root
            self.size[x_root] += self.size[y_root]

H, W = map(int,input().split())
Q = int(input())
maze = [[0] * W for _ in range(H)]
uf = UnionFind(H * W)

for _ in range(Q):
    query = list(map(int, input().split()))
    print(vars(uf))
    if query[0] == 1:
        i, j = query[1] - 1, query[2] - 1
        maze[i][j] = 1
        for di, dj in [(0,1), (0,-1), (1, 0), (-1, 0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < H and 0 <= nj < W and maze[ni][nj] == 1:
                uf.union(i * W + j, ni * W + nj)
    
    else:
        ra, ca = query[1] - 1, query[2] - 1
        rb, cb = query[3] - 1, query[4] - 1
        if maze[ra][ca] == 1 and maze[rb][cb] == 1:
            if uf.find(ra * W + ca) == uf.find(rb * W + cb):
                print("Yes")
            else:
                print("No")
        else:
            print("No")