from In import In
from BasicDataStructure import Bag, Stack, Queue


class Graph:

    def __init__(self, f):
        s = In(f)
        self.v = s.read_int()
        self.e = 0
        self.adj = []
        for i in range(self.v):
            bag = Bag()
            self.adj.append(bag)

        e = s.read_int()
        for i in range(e):
            v = s.read_int()
            w = s.read_int()
            self.add_edge(v, w)

    def add_edge(self, v, w):
        self.adj[v].add(w)
        self.adj[w].add(v)
        self.e += 1

    def e(self):
        return self.e

    def v(self):
        return self.v

    def adj1(self, v):
        return self.adj[v]


class DepthFistPath:

    def __init__(self, g, s):
        self.marked = []
        self.s = s
        self.edg_to = []
        for i in range(g.v):
            self.marked.append(False)
            self.edg_to.append(None)

        self.dfs(g, s)

    def dfs(self, g, v):
        self.marked[v] = True
        for w in g.adj1(v):
            if not self.marked[w]:
                self.edg_to[w] = v
                self.dfs(g, w)

    def has_path_to(self, v):
        return self.marked[v]

    def path_to(self, v):
        if not self.has_path_to(v):
            return None
        w = v
        stack = Stack()
        while w != self.s:
            stack.push(w)
            w = self.edg_to[w]
        stack.push(self.s)
        return stack

class BreadthFirstPath:
    def __init__(self, g, s):
        self.s = s
        self.marked = []
        self.edge_to = []
        for i in range(g.v):
            self.marked.append(False)
            self.edge_to.append(None)

        self.bfs(g, s)

    def bfs(self, g, s):
        q = Queue()
        q.enqueue(s)
        self.marked[s] = True
        while not q.is_empty():
            v = q.dequeue()
            for w in g.adj1(v):
                if not self.marked[w]:
                    self.edge_to[w] = v
                    self.marked[w] = True
                    q.enqueue(w)

    def has_path_to(self, v):
        return self.marked[v]

    def path_to(self, v):
        if not self.has_path_to(v):
            return None
        w = v
        stack = Stack()
        while w != self.s:
            stack.push(w)
            w = self.edge_to[w]
        stack.push(self.s)
        return stack

if __name__ == '__main__':
    g = Graph('tinyCG.txt')
    p = BreadthFirstPath(g, 0)
    for i in range(g.v):
        if p.has_path_to(i):
            print 0, 'to', i, ':',
            for j in p.path_to(i):
                if j == 0:
                    print 0,
                else:
                    print '-', j,
            print