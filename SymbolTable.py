from In import In

class BinarySearchST:

    def __init__(self, n):
        self.keys = []
        self.vals = []
        for i in range(n):
            self.keys.append(None)
            self.vals.append(None)
        self.n = 0

    def rank(self, key):
        lo = 0
        hi = self.n - 1
        while lo <= hi:
            mid = lo + (hi - lo) / 2
            i = cmp(key, self.keys[mid])
            if i < 0: hi = mid - 1
            elif i > 0: lo = mid + 1
            else: return mid
        return lo

    def put(self, key, val):
        k = self.rank(key)
        if self.keys[k] == key:
            self.vals[k] = val
        else:
            for i in range(self.n, k, -1):
                self.keys[i] = self.keys[i-1]
                self.vals[i] = self.vals[i-1]
            self.keys[k] = key
            self.vals[k] = val
            self.n += 1

    def get(self, key):
        k = self.rank(key)
        if self.keys[k] == key:
            return self.vals[k]
        return None

if __name__ == '__main__':
    i = In('tinyST.txt')
    n = len(i.read_strings())
    st = BinarySearchST(n)
    j = 0

    while i.has_next():
        s = i.read_string()
        st.put(s, j)
        j += 1

    for key in st.keys:
        v = st.get(key)
        if v == None: break
        print v

