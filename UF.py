from In import In

class UF:

    def __init__(self, n):
        self.id = list(range(n))
        for i in range(n):
            self.id[i] = i
        self.count = n
        self.sz = list(range(n))
        for i in range(n):
            self.sz[i] = 1

    def union(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)
        if p_root == q_root:
            return
        if self.sz[p_root] > self.sz[q_root]:
            self.id[q_root] = p_root
            self.sz[p_root] += self.sz[q_root]
        else:
            self.id[p_root] = q_root
            self.sz[q_root] += self.sz[p_root]
        self.count -= 1

    def find(self, p):
        while self.id[p] != p:
            p = self.id[p]
        return p

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def count(self):
        return self.count

if __name__ == '__main__':
    stream = In('tinyUF.txt')
    uf = UF(stream.read_int())
    while stream.has_next():
        p = stream.read_int()
        q = stream.read_int()
        if uf.connected(p, q):
            continue
        uf.union(p, q)
        print str(p) + " " + str(q)
    print str(uf.count) + 'components.'