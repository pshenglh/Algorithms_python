from In import In
from BasicDataStructure import Queue

class BinarySearchST:

    def __init__(self, n):
        self.keys = []
        self.vals = []
        for i in range(n):
            self.keys.append(None)
            self.vals.append(None)
        self.n = 0

    def rank(self, key):
        lo = 0
        hi = self.n - 1
        while lo <= hi:
            mid = lo + (hi - lo) / 2
            i = cmp(key, self.keys[mid])
            if i < 0: hi = mid - 1
            elif i > 0: lo = mid + 1
            else: return mid
        return lo

    def put(self, key, val):
        k = self.rank(key)
        if self.keys[k] == key:
            self.vals[k] = val
        else:
            for i in range(self.n, k, -1):
                self.keys[i] = self.keys[i-1]
                self.vals[i] = self.vals[i-1]
            self.keys[k] = key
            self.vals[k] = val
            self.n += 1

    def get(self, key):
        k = self.rank(key)
        if self.keys[k] == key:
            return self.vals[k]
        return None


class Node:

    def __init__(self, key, val, n):
        self.key = key
        self.val = val
        self.left = None
        self.right = None
        self.n = n


class BST:

    def __init__(self):
        self.root = None

    def put(self, key, val):
        self.root = self.recurse_put(self.root, key, val)

    def recurse_put(self, node, key, val):
        if node == None:
            n = Node(key, val, 1)
            return n
        i = cmp(key, node.key)
        if i < 0:
            node.left = self.recurse_put(node.left, key, val)
        elif i > 0:
            node.right = self.recurse_put(node.right, key, val)
        else:
            node.val = val
        node.n = self.node_size(node.left) + self.node_size(node.right) + 1
        return node

    def get(self, key):
        return self.recurse_get(self.root, key)

    def recurse_get(self, node, key):
        if node == None: return None
        i = cmp(key, node.key)
        if i < 0:
            return self.recurse_get(node.left, key)
        elif i > 0:
            return self.recurse_get(node.right, key)
        else:
            return node.val

    def size(self):
        return self.node_size(self.root)

    def node_size(self, node):
        if node == None: return 0
        else: return node.n

    def max(self):
        return self.node_max(self.root).key

    def node_max(self, node):
        if node.right == None:
            return node
        return self.node_max(node.right)

    def min(self):
        return self.node_min(self.root).key

    def node_min(self, node):
        if node.left == None:
            return node
        return self.node_min(node.left)

    def node_floor(self, node, key):
        if node == None:
            return None
        i = cmp(key, node.key)
        if i < 0: return self.node_floor(node.left, key)
        elif i == 0: return node
        else:
            t = self.node_floor(node.right, key)
            if t != None: return t
            else: return node

    def floor(self, key):
        x = self.node_floor(self.root, key)
        if x == None: return None
        else: return x.key

    def node_ceiling(self, node, key):
        if node == None: return None
        i = cmp(key, node.key)
        if i > 0:
            return self.node_ceiling(node.right, key)
        elif i == 0:
            return node
        else:
            t = self.node_ceiling(node.left, key)
            if t != None: return t
            else: return node

    def ceiling(self, key):
        x = self.node_ceiling(self.root, key)
        if x == None: return None
        return x.key

    def rank(self, key):
        i = self.node_rank(self.root, key)
        return i

    def node_rank(self, node, key):
        if node == None: return 0
        i = cmp(key, node.key)
        if i < 0:
            return self.node_rank(node.left, key)
        elif i == 0:
            return self.node_size(node.left)
        else:
            return self.node_size(node.left) + 1 + self.node_rank(node.right, key)

    def select(self, i):
        x = self.node_select(self.root, i)
        return x.key

    def node_select(self, node, i):
        if node == None: return None
        t = self.node_size(node.left)
        j = cmp(i, t)
        if j < 0: return self.node_select(node.left, i)
        elif j > 0: return self.node_select(node.right, i-t-1)
        else: return node

    def del_min(self):
        self.root = self.recurse_del_min(self.root)

    def recurse_del_min(self, node):
        if node.left == None:
            return node.right
        node.left = self.recurse_del_min(node.left)
        node.n = self.node_size(node.left) + self.node_size(node.right) + 1
        return node

    def delete(self, key):
        self.root = self.recurse_del(self.root, key)

    def recurse_del(self, node, key):
        if node == None: return None
        i = cmp(key, node.key)
        if i < 0:
            node.left = self.recurse_del(node.left, key)
        elif i > 0:
            node.right = self.recurse_del(node.right, key)
        else:
            if node.left == None:
                return node.right
            elif node.right == None:
                return node.left
            else:
                t = node
                node = self.node_min(node.right)
                node.right = self.recurse_del_min(node.right)
                node.left = t.left
        node.n = self.node_size(node.left) + self.node_size(node.right) + 1
        return node

    def recurse_keys(self, queue, node, lo, hi):
        if node == None: return
        cmplo = cmp(lo, key)
        cmphi = cmp(hi, key)
        if cmplo < 0:
            self.recurse_keys(queue, node.left, lo, hi)
        if cmplo <= 0 and cmphi >= 0:
            queue.enqueue(node.key)
        if cmphi > 0:
            self.recurse_keys(queue, node.right, lo, hi)

    def keys(self, lo, hi):
        queue = Queue()
        self.recurse_keys(queue, self.root, lo, hi)
        return queue

    def all_keys(self):
        return self.keys(self.min(), self.max())


class RBNode:

    def __init__(self, key, val, n, color):
        self.key = key
        self.val = val
        self.n = n
        self.left = None
        self.right = None
        self.color = color



class RedBlackBST:

    def __init__(self):
        self.root = None


    def rotate_left(self, h):
        x = h.right
        h.right = x.left
        x.left = h
        x.color = h.color
        x.n = h.n
        h.color = True
        h.n = self.node_size(h.left) + self.node_size(h.right) + 1
        return x

    def rotate_right(self, h):
        x = h.left
        h.left = x.right
        x.right = h
        x.color = h.color
        x.n = h.n
        h.color = True
        h.n = self.node_size(h.left) + self.node_size(h.right) + 1
        return x

    def node_size(self, x):
        if x == None: return 0
        return x.n

    def size(self):
        return self.node_size(self.root)

    def flip_colors(self, h):
        h.left.color = False
        h.right.color = False
        h.color = True

    def is_red(self, h):
        if h == None: return False
        return h.color

    def put(self, key, val):
        self.root = self.node_put(self.root, key, val)
        self.root.color = False

    def node_put(self, node, key, val):
        if node == None:
            return RBNode(key, val, 1, True)
        i = cmp(key, node.key)
        if i < 0:
            node.left = self.node_put(node.left, key, val)
        elif i > 0:
            node.right = self.node_put(node.right, key, val)
        else:
            node.val = val

        if self.is_red(node.right) and not self.is_red(node.left):
            node = self.rotate_left(node)
        if self.is_red(node.left) and self.is_red(node.left.left):
            node = self.rotate_right(node)
        if self.is_red(node.left) and self.is_red(node.right):
            self.flip_colors(node)

        node.n = self.node_size(node.left) + self.node_size(node.right) + 1
        return node

    def node_get(self, node, key):
        if node == None: return None
        i = cmp(key, node.key)
        if i < 0:
            return self.node_get(node.left, key)
        elif i > 0:
            return self.node_get(node.right, key)
        else:
            return node

    def get(self, key):
        return self.node_get(self.root, key).val

    def flip_color(self, h):
        h.color = not h.color
        h.left.color = not h.left.color
        h.right.color = not h.right.color

    def move_red_left(self, h):
        self.flip_color(h)
        if (self.is_red(h.right.left)):
            h.right = self.rotate_right(h.right)
            h = self.rotate_left(h)
        return h

if __name__ == '__main__':
    i = In('tinyST.txt')
    n = len(i.read_strings())
    st = RedBlackBST()
    j = 0

    while i.has_next():
        s = i.read_string()
        st.put(s, j)
        j += 1

    for key in i.read_strings():
        print key, st.get(key)

