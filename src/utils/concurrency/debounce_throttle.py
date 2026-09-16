"""Debounce and throttle execution control."""
import time
def throttle(wait_seconds):
    def decorator(fn):
        last_call = 0
        def wrapper(*args, **kwargs):
            nonlocal last_call
            if time.time() - last_call >= wait_seconds:
                last_call = time.time()
                return fn(*args, **kwargs)
        return wrapper
    return decorator
