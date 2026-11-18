import re


def slugify(text):
    """Lowercase text, collapsing runs of non-alphanumerics into one '-'."""
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')
