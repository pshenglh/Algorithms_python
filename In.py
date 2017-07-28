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
        int_list = list(range(len(s)))
        for i in range(len(s)):
            try:
                int_list[i] = int(s[i])
            except:
                break
        self.int_list = int_list
        self.int_iter = iter(int_list)
        self.string_list = s
        self.string_iter = iter(s)
        self.n = len(s)
        self.f.close()

    def read_int(self):
        self.n -= 1
        return self.int_iter.next()

    def read_ints(self):
        return self.int_list

    def read_strings(self):
        return self.string_list

    def read_string(self):
        self.n -= 1
        return self.string_iter.next()

    def has_next(self):
        return self.n > 0

if __name__ == '__main__':
    stream = In('tinyUF.txt')
    while stream.has_next():
        print stream.read_int()