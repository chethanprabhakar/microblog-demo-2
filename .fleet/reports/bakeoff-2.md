## Files changed

Base: origin/fleet/run-1794798534934

Names:
```
app/models.py
tests.py
```

Diff stat:
```
app/models.py | 5 +++++
 tests.py      | 5 +++++
 2 files changed, 10 insertions(+)
```

## Gate

Command: python3 -m venv .venv && .venv/bin/pip install -q -r requirements.txt && .venv/bin/python -m unittest tests.py
Exit code: 0

Output (last 60 lines):
```
.....
----------------------------------------------------------------------
Ran 5 tests in 0.458s

OK
```

## Run

Tool: claude
Model: not recorded
Minutes: 1
AI cost (USD): 0

## Coder's note (unverified)

```
I added `Post.excerpt(n)` in `app/models.py` and a test for it in `tests.py`, but I couldn't run the tests. Flask isn't installed in this environment, so `python3 -m unittest tests` fails on `import flask`.

- **Behavior:** `excerpt(n)` returns `body` unchanged when `len(body) <= n`. Otherwise it returns the first `n` characters followed by `"..."`, so `Post(body="abcdefghij").excerpt(5)` gives `"abcde..."`.
- **Tests:** `test_post_excerpt` covers a body shorter than `n`, a body exactly `n` long, and a longer body (the `abcdefghij` example).
```
