"""Kahn's algorithm for topological sorting."""
from collections import deque
def topological_sort(graph):
    in_degree = {u: 0 for u in graph}
    for u in graph:
        for v in graph[u]:
            in_degree[v] = in_degree.get(v, 0) + 1
    queue = deque([u for u in graph if in_degree[u] == 0])
    res = []
    while queue:
        u = queue.popleft()
        res.append(u)
        for v in graph.get(u, []):
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    return res
