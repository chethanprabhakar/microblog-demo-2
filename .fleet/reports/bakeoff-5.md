## Files changed

Base: origin/fleet/run-1794798885864

Names:
```
app/api/users.py
tests.py
```

Diff stat:
```
app/api/users.py |  5 ++++-
 tests.py         | 36 ++++++++++++++++++++++++++++++++++++
 2 files changed, 40 insertions(+), 1 deletion(-)
```

## Gate

Command: python3 -m venv .venv && .venv/bin/pip install -q -r requirements.txt && .venv/bin/python -m unittest tests.py
Exit code: 0

Output (last 60 lines):
```
.......
----------------------------------------------------------------------
Ran 7 tests in 0.446s

OK
```

## Run

Tool: claude
Model: not recorded
Minutes: 1
AI cost (USD): 0

## Coder's note (unverified)

```
`GET /api/users/<id>` with a valid token now returns 404 with `{"error": "user_not_found"}` when the id doesn't exist. All 7 tests pass, including the 3 new ones. I haven't committed anything.

- **Fix:** in `app/api/users.py`, `get_user` looks the user up with `db.session.get`. If there's no match it returns the new error body. Existing users still come back with 200.
- **Other 404s:** these still go through the shared handler, so they keep the generic body. For example, `/api/nonexistent` still returns `{"error": "Not Found"}`.
- **Tests:** I added a `UserApiCase` class to `tests.py` with one test each for an existing user, a missing user, and an unchanged generic 404.
- **Test environment:** the machine had no Flask installed, so I made a throwaway virtualenv at `/tmp/venv` from `requirements.txt` to run the tests. It's outside the repo.
```
