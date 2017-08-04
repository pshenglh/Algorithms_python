from In import In

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
    

if __name__ == '__main__':
    s = In('data/words3.txt')
    a = s.read_strings()
    Qiuck3String(a)
    for w in a:
        print w