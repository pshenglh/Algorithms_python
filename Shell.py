
def sort(arg):
    a = arg
    N = len(a)
    h = 1
    while h < N / 3:
        h = h * 2 + 1
    while h >= 1:
        for i in range(h, N):
            for j in range(i, h-1, -h):
                if a[j] < a[j-h]:
                    t = a[j]
                    a[j] = a[j-h]
                    a[j-h] = t
                else:
                    break
        h = h / 2
    return a
		
if __name__ == '__main__':
    a = [43, 57, 34, 1, 76, 94, 96, 104, 3, 85, 932, 6, 39, 94]
    print sort(a)