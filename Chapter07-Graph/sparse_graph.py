from collections import defaultdict
import random

class SparseGraph:
    def __init__(self, n, directed = True):
        self.n = n
        self.m = 0
        self.directed = directed
        self.table = defaultdict(set)
        
    def get_n(self):
        return self.n
    
    def get_m(self):
        return self.m
    
    def add_edge(self, v, w):
        if v < 0 or v >= self.n or w < 0 or w >= self.n:
            raise ValueError("v or w doesn't exist")
        
        self.table[v].add(w)
        if v != w or not self.directed:
            self.table[w].add(v)
        
        self.m += 1
    
    def has_edge(self, v, w):
        if v < 0 or v >= self.n or w < 0 or w >= self.n:
            raise ValueError("v or w doesn't exist")
        
        if w in self.table[v]:
            return True
        return False

    def __iter__(self):
        return iter(self.table.values())


if __name__ == "__main__":

    N = 20
    M = 100
    s = SparseGraph(N, False)

    for _ in range(M):
        a = random.randint(0, N - 1)
        b = random.randint(0, N - 1)
        s.add_edge(a, b)

    for index, x in enumerate(s):
        print(index, x)


    
    