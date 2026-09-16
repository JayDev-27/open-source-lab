"""Heap-based Priority Queue."""
import heapq
class PriorityQueue:
    def __init__(self): self.elements = []
    def push(self, item, priority): heapq.heappush(self.elements, (priority, item))
    def pop(self): return heapq.heappop(self.elements)[1]
