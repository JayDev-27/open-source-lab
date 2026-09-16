"""Andrew's monotone chain 2D convex hull algorithm."""
def convex_hull(points):
    points = sorted(set(points))
    if len(points) <= 1: return points
    def cross(o, a, b): return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0: lower.pop()
        lower.append(p)
    return lower
