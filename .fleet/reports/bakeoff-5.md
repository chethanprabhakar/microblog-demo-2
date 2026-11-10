## Files changed

Base: origin/fleet/run-1794292235989

Names:
```
app/api/users.py
tests.py
```

Diff stat:
```
app/api/users.py |  5 ++++-
 tests.py         | 25 +++++++++++++++++++++++++
 2 files changed, 29 insertions(+), 1 deletion(-)
```

## Gate

Command: python3 -m venv .venv && .venv/bin/pip install -q -r requirements.txt && .venv/bin/python -m unittest tests.py
Exit code: 0

Output (last 60 lines):
```
............
----------------------------------------------------------------------
Ran 12 tests in 0.448s

OK
```

## Run

Tool: claude
Model: claude-sonnet-5-5
Minutes: 1
AI cost (USD): 0.0560116

## Coder's note (unverified)

```
`GET /api/users/<id>` now returns 404 with `{"error": "user_not_found"}` when the id doesn't exist, and all 12 tests pass.

- **Change:** in `app/api/users.py`, `get_user` now looks the user up with `db.session.get` instead of `get_or_404`. A missing user gets the new body, and an existing user is still returned with 200.
- **Other 404s:** I left the other routes on `get_or_404`, so they keep the generic `{"error": "Not Found"}`. That includes the followers, following and PUT routes for a missing user. The criteria only named the GET route, so I didn't change those.
- **Tests:** I added two tests to `HealthCheckCase` in `tests.py`. `test_get_user` checks that an existing user comes back with 200. `test_get_missing_user` checks the new 404 body, and also that `/api/nonexistent` still returns the generic 404. I put them in that class because it already had the app and database setup, even though the name doesn't fit.

Nothing is committed.
```
