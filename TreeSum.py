from BinarySearch import BinarySearch

def three_sum(list):
    n = len(list)
    cnt = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if list[i] + list[j] + list[k] == 0:
                    cnt += 1

    return cnt

def three_sum_fast(list):
    n = len(list)
    cnt = 0
    list.sort()
    search = BinarySearch(list)
    for i in range(n):
        for j in range(i+1, n):
            if (search.search(-list[i]-list[j]) > j):
                cnt += 1
    return cnt


if __name__ == '__main__':
    f = open('1Kints.txt', 'r')
    list = []
    for l in f:
        i = int(l)
        list.append(i)
    print three_sum_fast(list)
