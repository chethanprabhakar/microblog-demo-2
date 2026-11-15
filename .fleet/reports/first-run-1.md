## Files changed

Base: origin/fleet/run-1794763411079

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
Ran 5 tests in 0.398s

OK
```

## Run

Tool: claude
Model: not recorded
Minutes: 1
AI cost (USD): 0

## Coder's note (unverified)

```
I added `User.initials()` to `app/models.py` and a `test_initials` test to `tests.py`. I couldn't run the new test or the existing suite because Flask isn't installed in this environment.

Instead I ran a standalone copy of the same logic, and it returned `AL` for `"ada lovelace"`, `S` for `"susan"`, `""` for an empty username and `AL` for `"ada_lovelace"`.

The method splits the username on runs of spaces or underscores, drops empty pieces, and uppercases the first letter of the first two words. That means `"ada  lovelace"` and `"_ada"` also behave sensibly. `import re` is added at the top of `models.py`.

`test_initials` covers the cases from your criteria, plus an underscore case and a three-word username (`"john paul george"` gives `JP`).
```
