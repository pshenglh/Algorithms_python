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


class MinPQ:
    def __init__(self):
        self.pq = []
        self.pq.append(None)
        self.n = 0

    def swim(self, i):

        k = i / 2
        while i > 1 and self.less(i, k):
            self.exch(i, k)
            i = k

    def sink(self, i):
        while 2 * i < self.n:
            k = 2 * i
            if k + 1 < self.n and self.less(k + 1, k):
                k = k + 1
            if self.less(i, k):
                break
            self.exch(k, i)
            i = k

    def insert(self, p):
        self.pq.append(p)
        self.n += 1
        self.swim(self.n)

    def min(self):
        return self.pq[1]

    def del_min(self):
        if self.n == 0:
            return 'EmptyPQ'
        m = self.pq[1]
        self.exch(1, self.n)
        del self.pq[self.n]
        self.n -= 1
        self.sink(1)
        return m

    def less(self, i, j):
        return self.pq[i] < self.pq[j]

    def exch(self, i, j):
        tmp = self.pq[i]
        self.pq[i] = self.pq[j]
        self.pq[j] = tmp

    def is_empty(self):
        return self.n == 0

class IndexPQ:
    def __init__(self, i):
        self.qp = []
        self.pq = []
        self.keys = []
        self.n = 0

        for j in range(i+1):
            self.qp.append(-1)
            self.pq.append(None)
            self.keys.append(None)

    def greater(self, i, j):
        return self.keys[self.pq[i]] > self.keys[self.pq[j]]

    def exch(self, i, j):
        tmp = self.pq[i]
        self.pq[i] = self.pq[j]
        self.pq[j] = tmp
        self.qp[self.pq[i]] = i
        self.qp[self.pq[j]] = j

    def swim(self, k):
        while k / 2 > 1 and self.greater(k/2, k):
            self.exch(k, k/2)
            k = k / 2

    def sink(self, k):
        while 2 * k < self.n:
            j = 2 * k
            if j + 1 < self.n and self.greater(j, j+1):
                j = j + 1
            if self.greater(j, k):
                break
            self.exch(j, k)
            k = j

    def insert(self, i, key):
        n = self.n + 1
        self.pq[n] = i
        self.qp[i] = n
        self.keys[i] = key
        self.swim(n)
        self.n = n

    def del_min(self):
        m = self.pq[1]
        self.exch(1, self.n)
        self.sink(1)
        n = self.n
        self.n -= 1
        self.pq[n] = -1
        self.qp[m] = -1
        self.keys[m] = None
        return m

    def is_empty(self):
        return self.n == 0

    def contain(self, i):
        return i in self.pq

    def change(self, i, key):
        self.keys[i] = key
        self.swim(self.qp[i])
        self.sink(self.qp[i])



if __name__ == '__main__':
    pq = MinPQ()
    while True:
        r = raw_input()
        s = str(r)
        if s == '-':
            print pq.del_min()
        elif s == '=':
            for i, j in enumerate(pq.pq):
                print i, j
        else:
            pq.insert(s)
