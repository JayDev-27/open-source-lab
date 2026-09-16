"""Escapes quotes for safe literal representation."""
def escape_sql_string(val: str) -> str:
    return val.replace("'", "''")
