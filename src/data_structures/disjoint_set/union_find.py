"""Disjoint-Set Union with path compression and rank."""
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            if self.rank[rx] < self.rank[ry]: self.parent[rx] = ry
            elif self.rank[rx] > self.rank[ry]: self.parent[ry] = rx
            else: self.parent[ry] = rx; self.rank[rx] += 1
