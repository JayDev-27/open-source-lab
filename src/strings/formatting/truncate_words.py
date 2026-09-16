"""Truncates string to max word count with ellipsis."""
def truncate_words(text: str, num_words: int) -> str:
    words = text.split()
    if len(words) <= num_words: return text
    return ' '.join(words[:num_words]) + '...'
