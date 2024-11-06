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
                x_root,y_root = y_root, x_root
            self.parent[y_root] = x_root
            self.size[x_root] += self.size[y_root]