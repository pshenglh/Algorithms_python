from In import In
from BasicDataStructure import Bag, Stack, Queue
from SymbolTable import BST


class Graph:

    def __init__(self, f):
        if type(f) == type(1):
            self.v = f
            self.e = 0
            self.adj = []
            for i in range(self.v):
                bag = Bag()
                self.adj.append(bag)
        else:
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

    def get_e(self):
        return self.e

    def get_v(self):
        return self.v

    def get_adj(self, v):
        return self.adj[v]

    def __str__(self):
        s = ''
        for v in range(self.get_v()):
            s = s + str(v) + ': '
            for w in self.get_adj(v):
                s = s + str(w) + ' '
            s += '\n'
        return s


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
        for w in g.get_adj(v):
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
            for w in g.get_adj(v):
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


class SymbolGraph:
    def __init__(self, file):
        self.st = BST()
        self.keys = []

        f = open(file, 'r')
        for line in f:
            a = line.strip("\n").split(' ')
            for key in a:
                if not self.st.contain(key):
                    self.st.put(key, self.st.size())

        f.close()
        for i in range(self.st.size()):
            self.keys.append(None)
        for key in self.st.all_keys():
            self.keys[self.st.get(key)] = key

        g = Graph(self.st.size())
        f = open(file, 'r')
        for line in f:
            a = line.strip('\n').split(' ')
            v = self.st.get(a[0])
            for w in range(1, len(a)):
                g.add_edge(v, self.st.get(a[w]))
        self.g = g

    def contain(self, key):
        return self.st.contain(key)

    def index(self, key):
        return self.st.get(key)

    def name(self, i):
        return self.keys[i]

    def graph(self):
        return self.g

    def all_key(self):
        for i, key in enumerate(self.keys):
            print i, key


def test_graph():
    g = Graph('data/tinyCG.txt')
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

def test_sg():
    sg = SymbolGraph('data/routes.txt')
    g = sg.graph()
    while True:
        s = raw_input()
        key = str(s)
        for w in g.get_adj(sg.index(key)):
            print '   ', sg.name(w)

if __name__ == '__main__':
    test_graph()