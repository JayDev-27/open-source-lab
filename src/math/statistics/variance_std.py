"""Computes sample and population variance."""
import statistics
def variance_std(data):
    return {'variance': statistics.variance(data), 'std_dev': statistics.stdev(data)}
