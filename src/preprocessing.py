import re


def normalize_text(text: str) -> str:
    """Normalize a single message for consistent training and inference."""
    if text is None:
        return ""

    text = str(text).lower().strip()
    text = re.sub(r"\s+", " ", text)
    return text


def clean_text(text: str) -> str:
    """Apply lightweight text cleaning. Punctuation is kept initially to preserve signals."""
    cleaned = normalize_text(text)
    cleaned = re.sub(r"[^a-z0-9\s]", " ", cleaned)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return cleaned
