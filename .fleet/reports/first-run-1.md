## Files changed

Base: origin/fleet/run-1794796646941

Names:
```
app/models.py
tests.py
```

Diff stat:
```
app/models.py | 5 +++++
 tests.py      | 7 +++++++
 2 files changed, 12 insertions(+)
```

## Gate

Command: python3 -m venv .venv && .venv/bin/pip install -q -r requirements.txt && .venv/bin/python -m unittest tests.py
Exit code: 0

Output (last 60 lines):
```
.....
----------------------------------------------------------------------
Ran 5 tests in 0.477s

OK
```

## Run

Tool: claude
Model: not recorded
Minutes: 1
AI cost (USD): 0

## Coder's note (unverified)

```
I added `User.initials()` in `app/models.py` and a `test_initials` test in `tests.py`. I couldn't run the new test, because Flask isn't installed in this environment and `tests.py` fails on import.

Instead I ran the same splitting logic in a standalone script. It gave the expected results for all the cases:

- `"ada lovelace"` returns `AL`.
- `"ada_lovelace"` returns `AL`.
- `"a b c"` returns `AB`.
- `"susan"` returns `S`.
- An empty username returns `""`.

The method splits the username on runs of spaces or underscores, drops empty pieces, and uppercases the first letter of the first two words. A `None` username also returns `""`. I added `import re` to `app/models.py` for it.

The test covers the three cases from your criteria, plus underscore splitting and a three-word name.
```
