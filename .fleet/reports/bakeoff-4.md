## Files changed

Base: origin/fleet/run-1794287771942

Names:
```
app/main/utils.py
tests.py
```

Diff stat:
```
app/main/utils.py | 14 ++++++++++++++
 tests.py          |  9 +++++++++
 2 files changed, 23 insertions(+)
```

## Gate

Command: python3 -m venv .venv && .venv/bin/pip install -q -r requirements.txt && .venv/bin/python -m unittest tests.py
Exit code: 0

Output (last 60 lines):
```
......
----------------------------------------------------------------------
Ran 6 tests in 0.392s

OK
```

## Run

Tool: aider
Model: bedrock/qwen.qwen3-coder-next
Minutes: 1
AI cost (USD): 0.0038

## Coder's note (unverified)

````
hor=u1,
                  timestamp=now + timedelta(seconds=1))
        p2 = Post(body="post from susan", author=u2,
                  timestamp=now + timedelta(seconds=4))
        p3 = Post(body="post from mary", author=u3,
                  timestamp=now + timedelta(seconds=3))
        p4 = Post(body="post from david", author=u4,
                  timestamp=now + timedelta(seconds=2))
        db.session.add_all([p1, p2, p3, p4])
        db.session.commit()

        # setup the followers
        u1.follow(u2)  # john follows susan
        u1.follow(u4)  # john follows david
        u2.follow(u3)  # susan follows mary
        u3.follow(u4)  # mary follows david
        db.session.commit()

        # check the following posts of each user
        f1 = db.session.scalars(u1.following_posts()).all()
        f2 = db.session.scalars(u2.following_posts()).all()
        f3 = db.session.scalars(u3.following_posts()).all()
        f4 = db.session.scalars(u4.following_posts()).all()
        self.assertEqual(f1, [p2, p4, p1])
        self.assertEqual(f2, [p2, p3])
        self.assertEqual(f3, [p3, p4])
        self.assertEqual(f4, [p4])

    def test_health_endpoint(self):
        self.app.config['TESTING'] = True
        client = self.app.test_client()
        response = client.get('/api/health')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'status': 'ok'})

    def test_slugify(self):
        self.assertEqual(slugify("Hello, World!"), "hello-world")
        self.assertEqual(slugify("  A  b "), "a-b")
        self.assertEqual(slugify("test"), "test")
        self.assertEqual(slugify("123!@#"), "123")
        self.assertEqual(slugify("---"), "")
        self.assertEqual(slugify("  leading and trailing  "), "leading-and-trailing")


if __name__ == '__main__':
    unittest.main(verbosity=2)
```
Tokens: 4.7k sent, 1.2k received. Cost: $0.0038 message, $0.0038 session.
Applied edit to app/main/utils.py
Applied edit to tests.py

````
