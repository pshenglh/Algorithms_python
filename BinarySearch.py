class BinarySearch:

    def __init__(self, list):
        self.list = list

    def search(self, key):
        N = len(self.list)
        lo = 0
        hi = N -1
        while lo <= hi:
            mid = lo + (hi - lo) / 2
            if key < self.list[mid]: hi = mid - 1
            elif key > self.list[mid]: lo = mid + 1
            else: return mid
        return -1

if __name__ == "__main__":
    list_file = open('data/tinyW.txt', 'r')
    search_file = open('data/tinyT.txt', 'r')
    list = []
    for each in list_file:
        list.append(int(each))
    list.sort()
    binary_search = BinarySearch(list)
    for each_int in search_file:
        key = int(each_int)
        if (binary_search.search(key) == -1):
            print key