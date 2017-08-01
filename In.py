class In:

    def __init__(self, file):
        self.f = open(file, 'r')
        lines = []
        for l in self.f:
            lines.append(l)
        s = []
        for line in lines:
            tmp = line.strip('\n').split(' ')
            s.extend(tmp)
        self.string_list = s
        self.string_iter = iter(s)
        self.n = len(s)
        self.f.close()

    def read_int(self):
        self.n -= 1
        return int(self.string_iter.next())

    def read_ints(self):
        int_list = []
        for i in range(self.n):
            int_list.append(int(self.string_list[i]))
        return int_list

    def read_strings(self):
        return self.string_list

    def read_string(self):
        self.n -= 1
        return self.string_iter.next()

    def read_float(self):
        self.n -= 1
        return float(self.string_iter.next())

    def has_next(self):
        return self.n > 0

if __name__ == '__main__':
    stream = In('tinyUF.txt')
    while stream.has_next():
        print stream.read_int()