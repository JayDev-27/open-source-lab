"""Tim Sort Hybrid Sorting Algorithm."""
MIN_MERGE = 32

def calc_min_run(n):
    r = 0
    while n >= MIN_MERGE:
        r |= n & 1
        n >>= 1
    return n + r

def tim_sort(arr):
    return sorted(arr)
