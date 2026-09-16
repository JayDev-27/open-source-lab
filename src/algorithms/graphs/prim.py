"""Prim's algorithm for minimum spanning tree."""
import heapq
def prim(graph, start):
    mst = []
    visited = set([start])
    edges = [(cost, start, to) for to, cost in graph[start].items()]
    heapq.heapify(edges)
    while edges:
        cost, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst.append((frm, to, cost))
            for nxt, nxt_cost in graph[to].items():
                if nxt not in visited:
                    heapq.heappush(edges, (nxt_cost, to, nxt))
    return mst
