## Files changed

Base: origin/fleet/run-1794285273081

Names:
```
app/models.py
tests.py
```

Diff stat:
```
app/models.py | 3 +++
 tests.py      | 6 ++++++
 2 files changed, 9 insertions(+)
```

## Gate

Command: python3 -m venv .venv && .venv/bin/pip install -q -r requirements.txt && .venv/bin/python -m unittest tests.py
Exit code: 0

Output (last 60 lines):
```
......
----------------------------------------------------------------------
Ran 6 tests in 0.410s

OK
```

## Run

Tool: claude
Model: not recorded
Minutes: 1
AI cost (USD): 0.0805032

## Coder's note (unverified)

```
I added `Post.word_count()` to `app/models.py`. It returns `len((self.body or '').split())`. Splitting with no arguments ignores leading, trailing and repeated whitespace, and the `or ''` makes a `None` body count as 0.

I also added `test_post_word_count` to `tests.py`, covering the four required cases: `"hello brave new world"` gives 4, `"  a   b "` gives 2, and both `""` and `None` give 0. All 6 tests pass. The change is committed on `fleet/run-1794285273081` as `c95c0b4`.
```
