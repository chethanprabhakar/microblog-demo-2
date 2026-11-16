## Files changed

Base: origin/fleet/run-1794798674899

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
Ran 5 tests in 0.390s

OK
```

## Run

Tool: claude
Model: not recorded
Minutes: 1
AI cost (USD): 0

## Coder's note (unverified)

```
I added `User.post_count()` in `app/models.py`. It counts the user's posts with the same pattern as `followers_count()` and `following_count()`.

I also added `test_post_count` to `tests.py`. It checks that a new user returns 0 and that the count is 2 after adding two posts. All 5 tests pass.

Flask wasn't installed, so I ran the tests in a venv at `/tmp/venv`, outside the repo. I haven't committed anything.
```
