"""Linear Search Implementation."""
def linear_search(arr, x):
    for i, item in enumerate(arr):
        if item == x:
            return i
    return -1
