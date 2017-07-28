class MaxPQ:

    def __init__(self):
        self.pq = []
        self.pq.append(None)
        self.n = 0

    def swim(self, k):
        while k > 1 and self.less(k/2, k):
            self.exch(k, k/2)
            k = k / 2

    def sink(self, k):
        while (2 * k) <= self.n:
            j = 2 * k
            if (j < self.n and self.less(j, j+1)): j += 1
            if self.less(j, k): break
            self.exch(k, j)
            k = j

    def less(self, i, j):
        return self.pq[i] < self.pq[j]

    def exch(self, i, j):
        tmp = self.pq[i]
        self.pq[i] = self.pq[j]
        self.pq[j] = tmp

    def insert(self, p):
        self.pq.append(p)
        self.n += 1
        self.swim(self.n)

    def max(self):
        return self.pq[1]

    def del_max(self):
        if self.n == 0:
            return 'PQEmpty!'
        i = self.pq[1]
        self.exch(1, self.n)
        del self.pq[self.n]
        self.n -= 1
        self.sink(1)
        return i

if __name__ == '__main__':
    pq = MaxPQ()
    while True:
        r = raw_input()
        s = str(r)
        if s == '-':
            print pq.del_max()
        elif s == '=':
            for i, j in enumerate(pq.pq):
                print i, j
        else:
            pq.insert(s)
