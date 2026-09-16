"""URL encoding and query parsing."""
import urllib.parse
def url_encode(val: str) -> str: return urllib.parse.quote_plus(val)
def url_decode(val: str) -> str: return urllib.parse.unquote_plus(val)
