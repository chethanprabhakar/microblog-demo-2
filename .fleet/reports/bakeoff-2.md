## Files changed

Base: origin/fleet/run-1794966137010

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
......
----------------------------------------------------------------------
Ran 6 tests in 0.378s

OK
```

## Run

Tool: claude
Model: not recorded
Minutes: 1
AI cost (USD): 0.0991262

## Coder's note (unverified)

```
I added `Post.excerpt(n)` and tests for it. All 6 tests pass, including the 2 new ones.

- **`app/models.py`:** `excerpt(n)` returns `body` unchanged when `len(body) <= n`. Otherwise it returns `body[:n] + '...'`, so `Post(body="abcdefghij").excerpt(5) == "abcde..."`.
- **`tests.py`:** a new `PostModelCase` with two tests:
  - Short bodies come back unchanged. This covers a body exactly `n` long and one shorter than `n`.
  - Your `"abcdefghij"` example is cut to `"abcde..."`.

The project's dependencies weren't installed, so I installed `requirements.txt` into a virtual environment at `/tmp/mbvenv` and ran the tests from there. Nothing in the repo changed for that.

I haven't committed anything; the changes are in the working tree on `fleet/run-1794966137010`.
```
