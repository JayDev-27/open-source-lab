"""Bellman-Ford algorithm with negative edge detection."""
def bellman_ford(vertices, edges, source):
    distance = {v: float('inf') for v in vertices}
    distance[source] = 0
    for _ in range(len(vertices) - 1):
        for u, v, w in edges:
            if distance[u] != float('inf') and distance[u] + w < distance[v]:
                distance[v] = distance[u] + w
    for u, v, w in edges:
        if distance[u] != float('inf') and distance[u] + w < distance[v]:
            raise ValueError('Negative weight cycle detected')
    return distance
