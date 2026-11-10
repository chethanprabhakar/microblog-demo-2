## Files changed

Base: origin/fleet/run-1794292235989

Names:
```
app/models.py
tests.py
```

Diff stat:
```
app/models.py | 5 +++++
 tests.py      | 9 +++++++++
 2 files changed, 14 insertions(+)
```

## Gate

Command: python3 -m venv .venv && .venv/bin/pip install -q -r requirements.txt && .venv/bin/python -m unittest tests.py
Exit code: 0

Output (last 60 lines):
```
.......
----------------------------------------------------------------------
Ran 7 tests in 0.399s

OK
```

## Run

Tool: claude
Model: claude-sonnet-5-5
Minutes: 0
AI cost (USD): 0.0350192

## Coder's note (unverified)

```
I added `Post.excerpt(n)` and tests for it, but I couldn't run the tests. Flask isn't installed here, so `tests.py` fails on import.

- **`app/models.py`:** `excerpt(n)` returns `body` unchanged when `len(body) <= n`. Otherwise it returns `body[:n] + "..."`, so `Post(body="abcdefghij").excerpt(5)` gives `"abcde..."`.
- **`tests.py`:** a new `PostExcerptCase` covers both cases. The short case checks a body exactly `n` long and one shorter than `n`. The long case is your `abcdefghij` example.
```
