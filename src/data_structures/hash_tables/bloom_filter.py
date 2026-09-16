"""Bloom Filter implementation."""
class BloomFilter:
    def __init__(self, size=1000): self.size = size; self.bit_array = [0] * size
