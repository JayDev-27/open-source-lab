"""Cryptographic hashing functions."""
import hashlib
def sha256_hash(data: str) -> str: return hashlib.sha256(data.encode()).hexdigest()
def sha512_hash(data: str) -> str: return hashlib.sha512(data.encode()).hexdigest()
