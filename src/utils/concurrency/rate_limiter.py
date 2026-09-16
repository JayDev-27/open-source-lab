"""Token bucket rate limiter."""
import time
class TokenBucket:
    def __init__(self, rate, capacity):
        self.rate = rate; self.cap = capacity; self.tokens = capacity; self.last = time.time()
    def consume(self, amount=1):
        now = time.time(); self.tokens = min(self.cap, self.tokens + (now - self.last) * self.rate)
        self.last = now
        if self.tokens >= amount:
            self.tokens -= amount; return True
        return False
