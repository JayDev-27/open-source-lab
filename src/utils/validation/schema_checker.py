"""Validates dictionary keys and types."""
def validate_dict(d, schema):
    for k, t in schema.items():
        if k not in d or not isinstance(d[k], t): return False
    return True
