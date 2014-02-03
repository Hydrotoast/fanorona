from itertools import product


def generate_alpha(count):
    it = ord('a')
    end = ord('a') + count - 1
    while it <= end:
        yield chr(it)
        it += 1


def generate_alpha_range(begin, count, inc):
    it = ord(begin)
    end = ord(begin) + count - 1
    while it <= end:
        yield chr(it)
        it += inc


def cell(row, alpha):
    return alpha + str(row)


class UndirectedGraph(object):
    def __init__(self):
        self.adjacencies = {}
        self.contents = {}

    def add_node(self, node):
        self.adjacencies[node] = []
        self.contents[node] = None

    def add_edge(self, node1, node2):
        self.adjacencies[node1].append(node2)
        self.adjacencies[node2].append(node1)

    def set_contents(self, node, value):
        self.contents[node] = value

    def edges(self, node):
        return self.adjacencies[node]

    def get_contents(self, node):
        return self.contents[node]

    @property
    def nodes(self):
        return map(lambda key: (key, self.get_contents(key)), self.adjacencies.keys())


class Grid(UndirectedGraph):
    def __init__(self, m, n):
        UndirectedGraph.__init__(self)

        # Add nodes
        for col, row in product(generate_alpha(n), range(m)):
            self.add_node(cell(row, col))

        # Horizontal edges
        for row in range(m):
            for col in generate_alpha(n - 1):
                self.add_edge(cell(row, col), cell(row, chr(ord(col)+1)))

        # Vertical edges
        for col in generate_alpha(n):
            for row in range(m - 1):
                self.add_edge(cell(row, col), cell(row+1, col))


class Tetrakis(Grid):
    def __init__(self, m, n):
        Grid.__init__(self, m, n)

        # Intersection edges
        for row, col in product(range(1, m, 2), generate_alpha_range('b', n - 1, 2)):
            self.add_edge(cell(row, col), cell(row-1, chr(ord(col)-1)))
            self.add_edge(cell(row, col), cell(row-1, chr(ord(col)+1)))
            self.add_edge(cell(row, col), cell(row+1, chr(ord(col)+1)))
            self.add_edge(cell(row, col), cell(row+1, chr(ord(col)-1)))

    def is_strong_intersection(self, pos):
        return len(self.adjacencies[pos]) == 8

    def is_weak_intersection(self, pos):
        return len(self.adjacencies[pos]) == 4
