## Files changed

Base: origin/fleet/run-1794285273081

Names:
```
app/models.py
tests.py
```

Diff stat:
```
app/models.py | 4 ++++
 tests.py      | 7 +++++++
 2 files changed, 11 insertions(+)
```

## Gate

Command: python3 -m venv .venv && .venv/bin/pip install -q -r requirements.txt && .venv/bin/python -m unittest tests.py
Exit code: 0

Output (last 60 lines):
```
.....
----------------------------------------------------------------------
Ran 5 tests in 0.396s

OK
```

## Run

Tool: claude
Model: not recorded
Minutes: 1
AI cost (USD): 0.10641

## Coder's note (unverified)

````
I added `User.initials()` to `app/models.py` with a unit test in `tests.py`, and all 5 tests pass, including the new one.

```python
def initials(self):
    words = (self.username or '').replace('_', ' ').split()
    return ''.join(word[0] for word in words[:2]).upper()
```

The new `test_initials` covers each case in the criteria:
- `"ada lovelace"` returns `"AL"`.
- `"ada_lovelace"` returns `"AL"`.
- A mix of spaces and underscores (`"ada_king lovelace"`) uses only the first two words and returns `"AK"`.
- `"susan"` returns `"S"`.
- An empty username returns `""`.

Repeated spaces or underscores don't create empty words, and a username that isn't set yet returns `""`.

Flask isn't installed in the system Python, so I ran the tests in a temporary virtualenv at `/tmp/mbvenv` built from `requirements.txt`. The repo itself is unchanged apart from the two files. I haven't committed anything.
````
