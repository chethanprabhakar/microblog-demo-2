## Files changed

Base: origin/fleet/run-1794974017918

Names:
```
app/models.py
tests.py
```

Diff stat:
```
app/models.py |  5 +++++
 tests.py      | 10 ++++++++++
 2 files changed, 15 insertions(+)
```

## Gate

Command: python3 -m venv .venv && .venv/bin/pip install -q -r requirements.txt && .venv/bin/python -m unittest tests.py
Exit code: 0

Output (last 60 lines):
```
.....
----------------------------------------------------------------------
Ran 5 tests in 0.418s

OK
```

## Run

Tool: claude
Model: not recorded
Minutes: 1
AI cost (USD): 0

## Coder's note (unverified)

```
Dependencies aren't installed, so I can't run the tests here.

I added `User.post_count()` in `app/models.py`. It counts the user's posts with the same query pattern as `followers_count()` and `following_count()`.

I also added `test_post_count` to `tests.py`. It checks that a new user returns 0, and that the count is 2 after two posts are added.

I haven't run the new test. `python3 -m unittest tests` fails on import with `ModuleNotFoundError: No module named 'flask'`. I didn't install the requirements, so none of the tests ran.
```
