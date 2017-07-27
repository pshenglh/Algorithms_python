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

def exch(list, i, j):
    tmp = list[j]
    list[j] = list[i]
    list[i] = tmp

if __name__ == '__main__':
    list = In('tiny.txt').read_strings()
    test = Test()
    test.test_shell(list)
    print list