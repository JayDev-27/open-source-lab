"""Base64 helpers."""
import base64
def encode_b64(text: str) -> str: return base64.b64encode(text.encode()).decode()
def decode_b64(b64_str: str) -> str: return base64.b64decode(b64_str.encode()).decode()
