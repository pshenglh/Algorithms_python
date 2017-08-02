from In import In
from SymbolTable import BST
from BasicDataStructure import Queue, Bag, Stack

class Digraph:
    def __init__(self, f):
        if type(f) == type(1):
            self.initial(f)
        else:
            s = In(f)
            self.initial(s.read_int())

            for e in range(s.read_int()):
                v = s.read_int()
                w = s.read_int()
                self.add_edge(v, w)

    def initial(self, i):
        self.v = i
        self.e = 0
        self.adj = []
        for a in range(self.v):
            bag = Bag()
            self.adj.append(bag)

    def add_edge(self, v, w):
        self.adj[v].add(w)
        self.e += 1

    def get_adj(self, v):
        return self.adj[v]

    def get_v(self):
        return self.v

    def get_e(self):
        return  self.e

    def reverse(self):
        a = self.v
        g = Digraph(a)
        for v in range(a):
            for w in self.get_adj(v):
                g.add_edge(w, v)
        return g


class SymbolDigraph:
    def __init__(self, file):
        f = open(file, 'r')
        self.st = BST()

        for line in f:
            a = line.strip('\n').split('/')
            for i in range(len(a)):
                if not self.st.contain(a[i]):
                    self.st.put(a[i], self.st.size())
        f.close()

        self.key = list(range(self.st.size()))
        for key in self.st.all_keys():
            self.key[self.st.get(key)] = key

        g = Digraph(self.st.size())
        f = open(file, 'r')
        for line in f:
            a = line.strip('\n').split('/')
            v = self.st.get(a[0])
            for i in range(1, len(a)):
                g.add_edge(v, self.st.get(a[i]))

        self.g = g

    def __str__(self):
        s = ''
        for v in range(self.st.size()):
            s = s + self.key[v] + ': '
            for w in self.g.get_adj(v):
                s = s + self.key[w] + '/'
            s += '\n'
        return s



class DirectedDFS:
    def __init__(self, g, s):
        self.marked = []
        for i in range(g.get_v()):
            self.marked.append(False)

        self.dfs(g, s)

    def dfs(self, g, v):
        self.marked[v] = True
        for w in g.get_adj(v):
            if not self.marked[w]:
                self.dfs(g, w)


class DirectedCycle:
        def __init__(self, g):
            self.marked = []
            self.on_stack = []
            self.edge_to = []
            self.cycle = Stack()
            for i in range(g.get_v()):
                self.marked.append(False)
                self.on_stack.append(False)
                self.edge_to.append(None)

            for v in range(g.get_v()):
                if not self.marked[v]:
                    self.dfs(g, v)

        def dfs(self, g, v):
            self.marked[v] = True
            self.on_stack[v] = True
            for w in g.get_adj(v):
                if self.has_cycle():
                    return
                if not self.marked[w]:
                    self.edge_to[w] = v
                    self.dfs(g, w)
                elif self.on_stack[w]:
                    x = v
                    while x != w:
                        self.cycle.push(x)
                        x = self.edge_to[w]
                    self.cycle.push(w)
                    self.cycle.push(v)
            self.on_stack[v] = False

        def has_cycle(self):
            return not self.cycle.is_empty()


class DepthFirstOrder:
    def __init__(self, g):
        self.marked = []
        self.pre = Queue()
        self.post = Queue()
        self.reverse_post = Stack()
        for i in range(g.get_v()):
            self.marked.append(False)

        for v in range(g.get_v()):
            if not self.marked[v]:
                self.dfs(g, v)

    def dfs(self, g, v):
        self.marked[v] = True
        self.pre.enqueue(v)
        for w in g.get_adj(v):
            if not self.marked[w]:
                self.dfs(g, w)
        self.post.enqueue(v)
        self.reverse_post.push(v)


class Topological:
    def __init__(self, g):
        self.order = None
        cyclefinder = DirectedCycle(g)
        if not cyclefinder.has_cycle():
            dfs = DepthFirstOrder(g)
            self.order = dfs.reverse_post

def test_symbol_digraph():
    sg = SymbolDigraph('data/jobs.txt')
    print sg

def test_top():
    sg = SymbolDigraph('data/jobs.txt')
    g = sg.g

    top = Topological(g)
    for v in top.order:
        print sg.key[v]



if __name__ == '__main__':
    test_top()