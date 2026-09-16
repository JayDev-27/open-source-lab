"""Removes HTML markup from text."""
import re
def strip_tags(html: str) -> str:
    return re.sub(r'<[^>]*?>', '', html)
