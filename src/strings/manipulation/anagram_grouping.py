"""Groups anagrams together."""
from collections import defaultdict
def group_anagrams(strs):
    ans = defaultdict(list)
    for s in strs:
        ans[tuple(sorted(s))].append(s)
    return list(ans.values())
