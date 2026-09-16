"""Calculates permutations nPr."""
import math
def permutations(n, r): return math.factorial(n) // math.factorial(n - r)
