class In:

    def __init__(self, file):
        self.f = open(file, 'r')
        lines = []
        for l in self.f:
            lines.append(l)
        s = []
        for line in lines:
            tmp = line.split(' ')
            s.extend(tmp)
        for i in range(len(s)):
            s[i] = int(s[i])
        self.n = len(s)
        self.s = iter(s)

    def read_int(self):
        self.n -= 1
        return self.s.next()

    def has_next(self):
        return self.n > 0

if __name__ == '__main__':
    stream = In('tinyUF.txt')
    while stream.has_next():
        print stream.read_int()