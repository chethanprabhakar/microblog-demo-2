import re


def slugify(text):
    """
    Convert text to a slug.
    - Lowercases the text.
    - Replaces runs of non-alphanumeric characters with a single hyphen.
    - Strips leading and trailing hyphens.
    """
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    text = text.strip('-')
    return text
