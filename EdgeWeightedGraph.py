from BasicDataStructure import Bag, Queue
from In import In
from PQ import MinPQ, IndexPQ
from UF import UF

class Edge:
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight

    def either(self):
        return self.v

    def other(self, i):
        if i == self.v:
            return self.w
        elif i == self.w:
            return self.v

    def __cmp__(self, other):
        return cmp(self.weight, other.weight)

    def __str__(self):
        v = self.either()
        w = self.other(v)
        s = str(v) + '-' + str(w) + ' ' + str(self.weight)
        return s


class EdgeWeightedGraph:

    def __init__(self, f):
        if type(f) == type(1):
            self.initial(f)
        else:
            s = In(f)
            self.initial(s.read_int())
            self.e = s.read_int()
            self.edges = []
            for i in range(self.e):
                v = s.read_int()
                w = s.read_int()
                weight = s.read_float()
                e = Edge(v, w, weight)
                self.edges.append(e)
                self.add_edge(e)

    def add_edge(self, e):
        v = e.either()
        w = e.other(v)
        self.adj[v].add(e)
        self.adj[w].add(e)
        self.e += 1


    def initial(self, i):
        self.v = i
        self.e = 0
        self.adj = []
        for v in range(i):
            bag = Bag()
            self.adj.append(bag)

    def __str__(self):
        s = ''
        for v in range(self.v):
            s = s + str(v) + ': '
            for e in self.adj[v]:
                w = e.other(v)
                s = s + str(v) + '-' + str(w) + ' ' + str(e.weight) + ' '
            s = s + '\n'
        return s

class LazyPrimMST:
    def __init__(self, g):
        self.pq = MinPQ()
        self.marked = []
        self.mst = Queue()

        for i in range(g.v):
            self.marked.append(False)
        self.visit(g, 0)
        while not self.pq.is_empty():
            e = self.pq.del_min()
            v = e.either()
            w = e.other(v)
            if self.marked[v] and self.marked[w]:
                continue
            self.mst.enqueue(e)
            if not self.marked[v]:
                self.visit(g, v)
            if not self.marked[w]:
                self.visit(g, w)

    def visit(self, g, v):
        self.marked[v] = True
        for e in g.adj[v]:
            if not self.marked[e.other(v)]:
                self.pq.insert(e)


class PrimMST:
    def __init__(self, g):
        self.pq = IndexPQ(g.v)
        self.marked = []
        self.dist_to = []
        self.edge_to = []

        for i in range(g.v):
            self.marked.append(False)
            self.dist_to.append(float('inf'))
            self.edge_to.append(None)

        self.dist_to[0] = 0.0
        self.pq.insert(0, 0.0)
        while not self.pq.is_empty():
            v = self.pq.del_min()
            self.visit(g, v)

    def visit(self, g, v):
        self.marked[v] = True
        for e in g.adj[v]:
            w = e.other(v)
            if self.marked[w]:
                continue
            if e.weight < self.dist_to[w]:
                self.edge_to[w] = e
                self.dist_to[w] = e.weight
                if self.pq.contain(w):
                    self.pq.change(w, self.dist_to[w])
                else:
                    self.pq.insert(w, self.dist_to[w])


class KruskalMST:
    def __init__(self, g):
        self.mst = Queue()
        self.pq = MinPQ()
        self.uf = UF(g.v)

        for e in g.edges:
            self.pq.insert(e)

        while not self.pq.is_empty() and self.mst.size() < g.v - 1:
            e = self.pq.del_min()
            v = e.either()
            w = e.other(v)
            if self.uf.connected(v, w):
                continue
            self.mst.enqueue(e)
            self.uf.union(v, w)

def test_lazy_prim_mst():
    g = EdgeWeightedGraph('data/tinyEWG.txt')
    m = LazyPrimMST(g)
    for e in m.mst:
        print e

def test_prim_mst():
    g = EdgeWeightedGraph('data/tinyEWG.txt')
    m = PrimMST(g)
    for e in m.edge_to:
        print e

def test_kmst():
    g = EdgeWeightedGraph('data/tinyEWG.txt')
    m = KruskalMST(g)
    for e in m.mst:
        print e

if __name__ == '__main__':
    test_kmst()