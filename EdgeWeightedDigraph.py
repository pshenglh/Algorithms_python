from BasicDataStructure import Bag, Stack, Queue
from PQ import IndexPQ
from In import In

class DirectedEdge:
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight

    def v_from(self):
        return self.v

    def v_to(self):
        return self.w

    def __str__(self):
        s = str(self.v) + '-' + str(self.w) + ' ' + str(self.weight)
        return s


class EdgeWeightedDigraph:
    def __init__(self, f):
        if type(f) == type(1):
            self.initial(f)
        else:
            s = In(f)
            self.initial(s.read_int())
            es = s.read_int()
            for i in range(es):
                v = s.read_int()
                w = s.read_int()
                weight = s.read_float()
                e = DirectedEdge(v, w, weight)
                self.add_edge(e)

    def add_edge(self, e):
        v = e.v_from()
        self.adj[v].add(e)
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
        for v in self.v:
            s = s + str(v) + ': '
            for e in self.adj[v]:
                s = s + str(v) + '->' + str(e.v_to) + ' ' + str(e.weight) + ','
            s += '\n'
        return s

class Dijkstra:
    def __init__(self, g, s):
        self.s = s
        self.pq = IndexPQ(g.v)
        self.dist_to = []
        self.edge_to = []

        for i in range(g.v):
            self.dist_to.append(float('inf'))
            self.edge_to.append(None)

        self.dist_to[s] = 0.0
        self.pq.insert(s, 0.0)

        while not self.pq.is_empty():
            self.relax(g, self.pq.del_min())

    def relax(self, g, v):
        for e in g.adj[v]:
            w = e.v_to()
            if self.dist_to[w] > self.dist_to[v] + e.weight:
                self.dist_to[w] = self.dist_to[v] + e.weight
                self.edge_to[w] = e
                if self.pq.contain(w):
                    self.pq.change(w, self.dist_to[w])
                else:
                    self.pq.insert(w, self.dist_to[w])

    def has_path_to(self, w):
        return self.dist_to[w] < float('inf')

    def path_to(self, v):
        if not self.has_path_to(v):
            return
        e = self.edge_to[v]
        path = Stack()
        while e != None:
            path.push(e)
            w = e.v_from()
            e = self.edge_to[w]
        return path


class DirectedCycle:
    def __init__(self, g):
        self.marked = []
        self.on_stack = []
        self.edge_to = []
        self.cycle = Stack()

        for i in range(g.v):
            self.marked.append(False)
            self.on_stack.append(False)
            self.edge_to.append(None)

        for v in range(g.v):
            if not self.marked[v]:
                self.dfs(g, v)

    def dfs(self, g, v):
        self.marked[v] = True
        self.on_stack[v] = True
        for e in g.adj[v]:
            w = e.v_to()
            if self.has_cycle():
                return
            if not self.marked[w]:
                self.edge_to[w] = e
                self.dfs(g, w)
            elif self.on_stack[w]:
                while e.v_from() != w:
                    self.cycle.push(e)
                    x = e.v_from()
                    e = self.edge_to[x]
        self.on_stack[v] = False

    def has_cycle(self):
        return not self.cycle.is_empty()


class DigraphOrder:
    def __init__(self, g):
        self.pre = Queue()
        self.post = Queue()
        self.reverse_post = Stack()
        self.marked = []

        for i in range(g.v):
            self.marked.append(False)

        for v in range(g.v):
            if not self.marked[v]:
                self.dfs(g, v)

    def dfs(self, g, v):
        self.marked[v] = True
        self.pre.enqueue(v)
        for e in g.adj[v]:
            w = e.v_to()
            if not self.marked[w]:
                self.dfs(g, w)
        self.post.enqueue(v)
        self.reverse_post.push(v)


class Topological:
    def __init__(self, g):
        cycle_finder = DirectedCycle(g)
        if not cycle_finder.has_cycle():
            top = DigraphOrder(g)
            self.order = top.reverse_post


class Acyclisp:
    def __init__(self, g, s):
        self.edge_to = []
        self.dist_to = []

        for i in range(g.v):
            self.edge_to.append(None)
            self.dist_to.append(float('inf'))

        top = Topological(g)

        self.dist_to[s] = 0.0

        for v in top.order:
            self.relax(g, v)

    def relax(self, g, v):
        for e in g.adj[v]:
            w = e.v_to()
            if self.dist_to[w] > self.dist_to[v] + e.weight:
                self.dist_to[w] = self.dist_to[v] + e.weight
                self.edge_to[w] = e

    def has_path_to(self, v):
        return self.dist_to[v] < float('inf')

    def path_to(self, v):
        if not self.has_path_to(v):
            return
        path = Stack()
        e = self.edge_to[v]
        while e != None:
            path.push(e)
            w = e.v_from()
            e = self.edge_to[w]
        return path


class BellmanFordSP:
    def __init__(self, g, s):
        self.dist_to = []
        self.edge_to = []
        self.on_q = []
        self.queue = Queue()
        self.cost = 0
        for i in range(g.v):
            self.dist_to.append(float('inf'))
            self.edge_to.append(None)
            self.on_q.append(None)
        self.queue.enqueue(s)
        self.on_q[s] = True
        while not self.queue.is_empty() and not self.has_nagative_cycle():
            v = self.queue.dequeue()
            self.on_q[v] = False
            self.relax(g, v)

    def relax(self, g, v):
        for e in g.adj[v]:
            w = e.v_to
            if self.dist_to[w] > self.dist_to[v] + e.weight:
                self.dist_to[w] = self.dist_to[v] + e.weight
                self.edge_to[w] = e
                if not self.on_q[w]:
                    self.on_q[w] = True
                    self.queue.enqueue(w)

def test_dijkstra():
    g = EdgeWeightedDigraph('data/tinyEWDAG.txt')
    sp = Acyclisp(g, 5)
    for w in range(g.v):
        if sp.has_path_to(w):
            print '5 to ', w, ':',
            for e in sp.path_to(w):
                print e,
            print

if __name__ == '__main__':
    test_dijkstra()

