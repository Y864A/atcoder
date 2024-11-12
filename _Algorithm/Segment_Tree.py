class SegTree:
    def __init__(self, op, e, n, v=None):
        self._n = n
        self._op = op
        self._e = e
        self._log = (n - 1).bit_length() # 2^(_log) >= n となる最小の整数
        self._size = 1 << self._log
        self._d = [self._e()] * (self._size * 2)
        if v is not None:
            # 葉に対象の列を格納
            for i in range(self._n):
                self._d[self._size + i] = v[i]
            # 葉に近い場所から順に更新
            for i in range(self._size - 1, 0, -1):
                 self._d[i] = self._op(self._d[i << 1], self._d[i << 1 | 1])

    # 更新クエリ
    def set(self, p, x):
        # 葉に移動
        p += self._size
        self._d[p] = x
        # 関連する場所を更新 
        while p:
            self._d[p >> 1] = self._op(self._d[p], self._d[p ^ 1])
            p >>= 1

    # 取得クエリ
    def prod(self, l, r):
        assert 0 <= l <= r <= self._n
        # 左の結果、右の結果
        sml, smr = self._e(), self._e()

        l += self._size
        r += self._size

        # 未計算の区別がなくなるまで
        while l < r:
            # 自身が右子ノードなら使用
            if l & 1:
                sml = self._op(sml, self._d[l])
                l += 1
            if r & 1:
                r -= 1
                smr = self._op(self._d[r], smr)
            # 親に移動
            l >>= 1
            r >>= 1
        return self._op(sml,smr)
            
    # 全要素の総積を取得
    def all_prod(self):
        return self._d[1]
    
    # p が与えられた時の ap を取得する
    def get(self, p):
        return self._d[p + self._size]
    

def op(x, y):
    return x ^ y

def e():
    return 0



def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))

    seg = SegTree(op, e, N, A)

    for _ in range(Q):
        t, x, y = map(int, input().split())
        x -= 1
        if t == 1:
            seg.set(x, seg.get(x) ^ y)
        else:
            print(seg.prod(x, y))

if __name__=="__main__":
    main()