
class Fenwick_Tree:
    def __init__(self, n):
        self._n = n # 要素数
        self.data = [0] * n

    def add(self, p, x):
        assert 0 <= p < self._n
        p += 1 # 実装上 のインデックスを合わせる 0-indexed -> 1-indexed
        while p <= self._n:
            self.data[p - 1] += x # data を更新
            p += p & -p # p にLSB(p) を加算

    def _sum(self, r):
        s = 0 # 総和を入れる変数
        while r > 0:
            s += self.data[r - 1]
            r -= r & -r # r からLSB(r)を減算
        return s
    
    def sum(self, l, r):
        assert 0 <= l <= r <= self._n
        return self._sum(r) - self._sum(l)

n = 8 
a = [0, 1, 2, 3, 4, 5, 6, 7]
fw = Fenwick_Tree(n)
for i, a_i in enumerate(a): fw.add(i, a_i)  # 数列aで初期化
print(vars(fw))
print(fw.sum(2, 4))  # 5
print(fw.sum(6, 7))  # 6 sum(i, i + 1)でa[i]が得られる
fw.add(2, 6)  # a[2] += 6
a[2] += 6
print(vars(fw))
fw.add(5, -1)  # a[5] += -1
a[5] += -1
print(a)  # [0, 1, 8, 3, 4, 4, 6, 7]
print(fw.sum(0, 3))  # 9
print(fw.sum(3, 7))  # 17
print(vars(fw))