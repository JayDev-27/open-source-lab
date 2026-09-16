"""Cryptographically secure token generator."""
import secrets
def generate_api_key(length=32): return secrets.token_urlsafe(length)
