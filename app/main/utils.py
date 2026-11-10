import re


def slugify(text):
    """
    Convert text to a slug format.
    Lowercases text, replaces runs of non-alphanumerics with a single hyphen,
    and strips leading/trailing hyphens.
    """
    text = text.lower()
    # Replace one or more non-alphanumeric characters with a single hyphen
    text = re.sub(r'[^a-z0-9]+', '-', text)
    # Strip leading and trailing hyphens
    text = text.strip('-')
    return text
