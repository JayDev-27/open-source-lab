"""Parses standard 5-part cron syntax."""
def parse_cron(expr: str):
    parts = expr.split()
    return {'min': parts[0], 'hour': parts[1], 'dom': parts[2], 'month': parts[3], 'dow': parts[4]}
