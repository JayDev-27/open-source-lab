"""Parses key: value properties safely."""
def parse_kv(text: str):
    res = {}
    for line in text.strip().splitlines():
        if ':' in line:
            k, v = line.split(':', 1)
            res[k.strip()] = v.strip()
    return res
