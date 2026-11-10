## Files changed

Base: origin/fleet/run-1794292235989

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
........
----------------------------------------------------------------------
Ran 8 tests in 0.412s

OK
```

## Run

Tool: claude
Model: claude-sonnet-5-5
Minutes: 0
AI cost (USD): 0.0410713

## Coder's note (unverified)

```
I added `User.post_count()` in `app/models.py`, and all 8 tests pass.

It counts the user's posts with a SQL `COUNT`, the same way `followers_count` does. The new `test_post_count` in `tests.py` checks that a user with no posts gets 0, and that the same user gets 2 after two posts are added.

I haven't committed anything.
```
