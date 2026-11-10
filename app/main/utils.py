import re


def slugify(text):
    """
    Convert text to a URL-friendly slug.
    
    Rules:
    - Lowercase the text
    - Replace runs of non-alphanumeric characters with a single hyphen
    - Strip leading and trailing hyphens
    
    Examples:
    - slugify("Hello, World!") == "hello-world"
    - slugify("  A  b ") == "a-b"
    """
    if not text:
        return ""
    
    # Convert to lowercase
    text = text.lower()
    
    # Replace runs of non-alphanumeric characters with a single hyphen
    # \W matches non-alphanumeric characters (equivalent to [^a-zA-Z0-9_])
    # We include underscore in the pattern to replace it as well
    text = re.sub(r'[^a-z0-9]+', '-', text)
    
    # Strip leading and trailing hyphens
    text = text.strip('-')
    
    return text
