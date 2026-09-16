"""Basic process memory diagnostics."""
import resource
def get_peak_memory_mb():
    usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return usage / (1024 * 1024) if usage > 1e6 else usage / 1024
