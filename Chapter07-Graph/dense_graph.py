### 稠密图 - 邻接矩阵

import random
import numpy as np

class DenseGraph:
    def __init__(self, n, directed = True):
        self.n = n
        self.m = 0
        self.directed = directed
        self.matrix = np.zeros((self.n, self.n))
    
    def get_n(self):
        return self.n
    
    def get_m(self):
        return self.m
    
    
    def add_edge(self, v, w):
        if v < 0 or v >= self.n or w < 0 or w >= self.n:
            raise ValueError("v or w doesn't exist")
        if self.has_edge(v, w):  #查看两点之间是否存在边
            return
    
        self.matrix[v][w] = 1  #表示两点之间存在边
        if not self.directed:
            self.matrix[w][v] = 1
        
        self.m += 1
    
    def has_edge(self, v, w):
        if v < 0 or v >= self.n or w < 0 or w >= self.n:
            raise ValueError("v or w doesn't exist")
        return self.matrix[v][w]

    def __iter__(self):
        return iter(self.matrix)

if __name__ == "__main__":

    N = 20
    M = 100
    s = DenseGraph(N, False)

    for i in range(M):
        a = random.randint(0, N - 1)
        b = random.randint(0, N - 1)
        s.add_edge(a, b)

    for index, x in enumerate(s):
        r = [i if i!= 0 else None for i in x]
        e = []
        for i, y in enumerate(r):
            if y:
                e.append(i)
        print(index, e)

    
            
        
