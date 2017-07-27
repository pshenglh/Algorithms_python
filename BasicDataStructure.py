class Node:

    def __init__(self, val, next=None):
        self.value = val
        self.next = next

class Stack:

    def __init__(self):
        self.N = 0
        self.first = None

    def push(self, val):
        old_first = self.first
        self.first = Node(val)
        self.first.next = old_first
        self.N += 1

    def isEmpty(self):
        return self.N == 0

    def size(self):
        return self.N

    def pop(self):
        if self.isEmpty():
            return 'StackEmpty'
        value = self.first.value
        self.first = self.first.next
        self.N -= 1
        return value

    def __iter__(self):
        self.current = self.first
        return self

    def next(self):
        if self.current == None:
            raise StopIteration
        value = self.current.value
        self.current = self.current.next
        return value

if __name__ == '__main__':
    stack = Stack()
    while True:
        i = raw_input()
        s = str(i)
        if (s == '-'):
            print stack.pop()
        elif (s == '='):
            for v in stack:
                print v
        else:
            stack.push(s)
