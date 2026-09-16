"""Floyd-Warshall all-pairs shortest path."""
def floyd_warshall(graph):
    dist = {u: {v: float('inf') for v in graph} for u in graph}
    for u in graph:
        dist[u][u] = 0
        for v, w in graph[u].items():
            dist[u][v] = w
    for k in graph:
        for i in graph:
            for j in graph:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist
