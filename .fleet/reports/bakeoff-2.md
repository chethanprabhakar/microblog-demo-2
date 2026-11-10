## Files changed

Base: origin/fleet/run-1794291017432

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
.......
----------------------------------------------------------------------
Ran 7 tests in 0.440s

OK
```

## Run

Tool: aider
Model: bedrock/moonshotai.kimi-k2.5
Minutes: 1
AI cost (USD): 0.02

## Coder's note (unverified)

````
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

    def test_post_excerpt_short(self):
        u = User(username='john', email='john@example.com')
        p = Post(body="short", author=u)
        self.assertEqual(p.excerpt(10), "short")

    def test_post_excerpt_long(self):
        u = User(username='john', email='john@example.com')
        p = Post(body="abcdefghij", author=u)
        self.assertEqual(p.excerpt(5), "abcde...")


class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_health_endpoint(self):
        response = self.client.get('/api/health')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"status": "ok"})


if __name__ == '__main__':
    unittest.main(verbosity=2)
```
Tokens: 7.0k sent, 4.2k received. Cost: $0.02 message, $0.02 session.
Applied edit to app/models.py
Applied edit to tests.py

````
