import math
import re


def slugify(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')


def word_count(text):
    return len(text.split())


def reading_time(text):
    return max(1, math.ceil(word_count(text) / 200))
