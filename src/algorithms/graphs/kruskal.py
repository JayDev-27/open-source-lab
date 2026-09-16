"""Kruskal's MST algorithm."""
def kruskal(nodes, edges):
    parent = {n: n for n in nodes}
    def find(i):
        if parent[i] == i: return i
        parent[i] = find(parent[i])
        return parent[i]
    mst = []
    for u, v, weight in sorted(edges, key=lambda item: item[2]):
        root_u, root_v = find(u), find(v)
        if root_u != root_v:
            parent[root_u] = root_v
            mst.append((u, v, weight))
    return mst
