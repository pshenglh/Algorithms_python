from In import In


class Selection:

    def sort(self, list):
        n = len(list)
        for i in range(n):
            min = i
            for j in range(i+1, n):
                if list[j] < list[min]:
                    min = j
            exch(list, min, i)


class Insertion:

    def sort(self, list):
        n = len(list)
        for i in range(n):
            for j in range(i, 0, -1):
                if list[j] > list[j-1]:
                    break
                exch(list, j, j-1)

class Shell:

    def sort(self, list):
        n = len(list)
        h = 1
        while h < n / 3: h = 3 * h + 1
        while h >= 1:
            for i in range(h, n):
                for j in range(i, h-1, -h):
                    if list[j] > list[j-h]:
                        break
                    exch(list, j, j-h)
            h = h / 3


class Merge:

    def merge(self, a, lo, mid, hi):
        i = lo
        j = mid + 1
        for k in range(lo, hi+1):
            self.aux[k] = a[k]

        for k in range(lo, hi+1):
            if i > mid:
                a[k] = self.aux[j]
                j += 1
            elif j > hi:
                a[k] = self.aux[i]
                i += 1
            elif self.aux[j] < self.aux[i]:
                a[k] = self.aux[j]
                j += 1
            else:
                a[k] = self.aux[i]
                i += 1

    def recurse_sort(self, a, lo, hi):
        if hi <= lo: return
        mid = lo + (hi - lo) / 2
        self.recurse_sort(a, lo, mid)
        self.recurse_sort(a, mid+1, hi)
        self.merge(a, lo, mid, hi)

    def sort(self, a):
        self.aux = list(range(len(a)))
        self.recurse_sort(a, 0, len(a)-1)


class MergeBU:

    def merge(self, a, lo, mid, hi):
        i = lo
        j = mid + 1

        for k in range(lo, hi+1):
            self.aux[k] = a[k]

        for k in range(lo, hi+1):
            if i > mid:
                a[k] = self.aux[j]
                j += 1
            elif j > hi:
                a[k] = self.aux[i]
                i += 1
            elif self.aux[j] < self.aux[i]:
                a[k] = self.aux[j]
                j += 1
            else:
                a[k] = self.aux[i]
                i += 1

    def sort(self, a):
        n = len(a)
        self.aux = list(range(len(a)))
        sz = 1
        while sz < n:
            for lo in range(0, n-sz, 2*sz):
                self.merge(a, lo, lo+sz-1, min(lo+2*sz, n-1))
            sz *= 2


class Quick:

    def partition(self, a, lo, hi):
        i = lo
        j = hi + 1
        v = a[lo]
        while True:
            while True:
                i += 1
                if a[i] >= v:
                    break
                if i == hi:
                    break
            while True:
                j -= 1
                if a[j] <= v:
                    break
                if j <= lo:
                    break
            if i >= j:
                break
            exch(a, i, j)
        exch(a, lo, j)
        return j

    def recurse_sort(self, a, lo, hi):
        if hi <= lo:
            return
        j = self.partition(a, lo, hi)
        self.recurse_sort(a, lo, j-1)
        self.recurse_sort(a, j+1, hi)

    def sort(self, a):
        self.recurse_sort(a, 0, len(a)-1)

class Test:

    def test_seletion(self, list):
        selection = Selection()
        selection.sort(list)

    def test_insertion(self, list):
        insertion = Insertion()
        insertion.sort(list)

    def test_shell(self, list):
        shell = Shell()
        shell.sort(list)

    def test_merge(self, list):
        merge = Merge()
        merge.sort(list)

    def test_quick(self, list):
        quick = Quick()
        quick.sort(list)

    def test_mergebu(self, list):
        merge = MergeBU()
        merge.sort(list)

def exch(list, i, j):
    tmp = list[j]
    list[j] = list[i]
    list[i] = tmp

if __name__ == '__main__':
    a = In('tiny.txt').read_strings()
    test = Test()
    test.test_quick(a)
    print a