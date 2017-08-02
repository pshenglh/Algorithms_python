from BasicDataStructure import Bag
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
        for v in i:
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

    
