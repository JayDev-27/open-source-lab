"""Ternary Search Implementation."""
def ternary_search(l, r, key, ar):
    if r >= l:
        mid1 = l + (r - l) // 3
        mid2 = r - (r - l) // 3
        if ar[mid1] == key:
            return mid1
        if ar[mid2] == key:
            return mid2
        if key < ar[mid1]:
            return ternary_search(l, mid1 - 1, key, ar)
        elif key > ar[mid2]:
            return ternary_search(mid2 + 1, r, key, ar)
        else:
            return ternary_search(mid1 + 1, mid2 - 1, key, ar)
    return -1
