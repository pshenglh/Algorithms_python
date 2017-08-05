from In import In
from BasicDataStructure import Queue

class LSD:
    def __init__(self, a, w):
        self.n = len(a)
        self.r = 265
        self.aux = [None] * self.n

        d = w - 1
        while d >= 0:
            count = [0] * (self.r+1)
            for i in range(0, self.n):
                count[ord(a[i][d])+1] += 1

            for r in range(0, self.r):
                count[r+1] += count[r]

            for i in range(0, self.n):
                j = count[ord(a[i][d])]
                self.aux[j] = a[i]
                count[ord(a[i][d])] += 1

            for i in range(0, self.n):
                a[i] = self.aux[i]

            d -= 1


class MSD:
    def __init__(self, a):
        self.r = 256
        self.n = len(a)
        self.aux = [None] * self.n
        self.sort(a, 0, self.n-1, 0)

    def char_at(self, s, d):
        if d < len(s):
            return ord(s[d])
        else:
            return -1

    def sort(self, a, lo, hi, d):
        if lo >= hi:
            return
        count = [0] * (self.r+2)
        for i in range(lo, hi+1):
            count[self.char_at(a[i], d)+2] += 1

        for r in range(0, self.r+1):
            count[r+1] += count[r]

        for i in range(lo, hi+1):
            self.aux[count[self.char_at(a[i], d)+1]] = a[i]
            count[self.char_at(a[i], d)+1] += 1

        for i in range(lo, hi+1):
            a[i] = self.aux[i-lo]

        for r in range(0, self.r):
            self.sort(a, lo+count[r], lo+count[r+1]-1, d+1)


class Qiuck3String:
    def __init__(self, a):
        self.sort(a, 0, len(a)-1, 0)

    def char_at(self, a, d):
        if d < len(a):
            return ord(a[d])
        else:
            return -1

    def sort(self, a, lo, hi, d):
        if hi <= lo:
            return
        lt = lo
        gt = hi
        i = lo + 1
        v = ord(a[lo][d])
        while i <= gt:
            t = ord(a[i][d])
            if t > v:
                self.exch(a, i, gt)
                gt -= 1
            elif t < v:
                self.exch(a, i, lt)
                lt += 1
                i += 1
            else:
                i += 1

        self.sort(a, lo, lt-1, d)
        if v > 0:
            self.sort(a, lt, gt, d+1)
        self.sort(a, gt+1, hi, d)

    def exch(self, a, i, j):
        tmp = a[i]
        a[i] = a[j]
        a[j] = tmp


class Node:
    def __init__(self, R):
        self.val = None
        self.next_ = [None] * R


class TrieST:
    def __init__(self):
        self.R = 256
        self.root = None

    def recurse_put(self, x, key, val, d):
        if x == None:
            x = Node(self.R)
        if d == len(key):
            x.val = val
            return x
        c = ord(key[d])
        x.next_[c] = self.recurse_put(x.next_[c], key, val, d+1)
        return x

    def put(self, key, val):
        self.root = self.recurse_put(self.root, key, val, 0)

    def recurse_get(self, x, key, d):
        if x == None:
            return None
        if d == len(key):
            return x
        c = ord(key[d])
        return self.recurse_get(x.next_[c], key, d+1)

    def get(self, key):
        x = self.recurse_get(self.root, key, 0)
        if x == None:
            return None
        return x.val

    def node_size(self, x):
        if x == None:
            return 0
        cnt = 0
        if x.val != None:
            cnt += 1
        for r in range(0, self.R):
            cnt += self.node_size(x.next_[r])
        return cnt

    def size(self):
        return self.node_size(self.root)

    def collection(self, x, pre, q):
        if x == None:
            return
        if x.val != None:
            q.enqueue(pre)
        for r in range(self.R):
            self.collection(x.next_[r], pre+chr(r), q)
        return q

    def keys_with_prefix(self, pre):
        x = self.recurse_get(self.root, pre, 0)
        q = Queue()
        self.collection(x, pre, q)
        return q

    def keys(self):
        return self.keys_with_prefix('')

    def node_delete(self, x, key, d):
        if x == None:
            return None
        if d == len(key):
            x.val = None
        else:
            c = ord(key[d])
            x.next_[c] = self.node_delete(x.next_[c], key, d+1)
        if x.val != None:
            return x
        for c in range(self.R):
            if x.next_[c] != None:
                return x
        return None

    def delete(self, key):
        self.root = self.node_delete(self.root, key, 0)

class TNode:
    def __init__(self):
        self.c = None
        self.left = None
        self.mid = None
        self.right = None
        self.val = None

class TST:

    def __init__(self):
        self.root = None

    def recurse_put(self, x, key, val, d):
        if x == None:
            x = TNode()
            x.c = key[d]
        if key[d] < x.c:
            x.left = self.recurse_put(x.left, key, val, d)
        elif key[d] > x.c:
            x.right = self.recurse_put(x.right, key, val, d)
        elif d < len(key) - 1:
            x.mid = self.recurse_put(x.mid, key, val, d+1)
        else:
            x.val = val
        return x

    def put(self, key, val):
        self.root = self.recurse_put(self.root, key, val, 0)

    def recurse_get(self, x, key, d):
        if x == None:
            return None
        if key[d] < x.c:
            return self.recurse_get(x.left, key, d)
        elif key[d] > x.c:
            return self.recurse_get(x.right, key, d)
        elif d < len(key) -1:
            return self.recurse_get(x.mid, key, d+1)
        else:
            return x

    def get(self, key):
        x = self.recurse_get(self.root, key, 0)
        if x == None:
            return None
        else:
            return x.val


def test_sort():
    s = In('data/words3.txt')
    a = s.read_strings()
    MSD(a)
    for w in a:
        print w

def test_search():
    s = In('data/shellsST.txt')
    st = TST()
    strings = s.read_strings()
    for i, key in enumerate(strings):
        st.put(key, i)

    for key in strings:
        i = st.get(key)
        print key, i



if __name__ == '__main__':
    test_search()