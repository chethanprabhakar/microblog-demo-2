import re


def slugify(text):
    """Lowercase text, collapse runs of non-alphanumerics into a single
    hyphen, and strip leading/trailing hyphens."""
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')
