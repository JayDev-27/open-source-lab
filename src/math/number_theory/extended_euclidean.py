"""Extended Euclidean algorithm for ax + by = gcd(a, b)."""
def extended_gcd(a, b):
    if a == 0: return b, 0, 1
    g, x1, y1 = extended_gcd(b % a, a)
    return g, y1 - (b // a) * x1, x1
