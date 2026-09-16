"""Interpolation Search Implementation."""
def interpolation_search(arr, lo, hi, x):
    if lo <= hi and x >= arr[lo] and x <= arr[hi]:
        pos = lo + int(((float(hi - lo) / (arr[hi] - arr[lo])) * (x - arr[lo])))
        if arr[pos] == x:
            return pos
        if arr[pos] < x:
            return interpolation_search(arr, pos + 1, hi, x)
        if arr[pos] > x:
            return interpolation_search(arr, lo, pos - 1, x)
    return -1
