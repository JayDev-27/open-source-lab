"""Dijkstra shortest path algorithm."""
import heapq
def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    queue = [(0, start)]
    while queue:
        cur_dist, u = heapq.heappop(queue)
        if cur_dist > distances[u]:
            continue
        for v, weight in graph[u].items():
            dist = cur_dist + weight
            if dist < distances[v]:
                distances[v] = dist
                heapq.heappush(queue, (dist, v))
    return distances
