"""Calculates mean, median, and mode."""
import statistics
def get_stats(data):
    return {'mean': statistics.mean(data), 'median': statistics.median(data)}
