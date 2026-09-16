"""Exponential Search Implementation."""
def exponential_search(arr, n, x):
    if arr[0] == x:
        return 0
    i = 1
    while i < n and arr[i] <= x:
        i = i * 2
    # perform binary search between i//2 and min(i, n-1)
    return -1
