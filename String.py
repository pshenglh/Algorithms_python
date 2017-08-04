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
    

if __name__ == '__main__':
    s = In('data/words3.txt')
    a = s.read_strings()
    MSD(a)
    for w in a:
        print w