## Files changed

Base: origin/fleet/run-1794291619719

Names:
```
app/main/utils.py
tests.py
```

Diff stat:
```
app/main/utils.py | 15 +++++++++++++++
 tests.py          |  7 +++++++
 2 files changed, 22 insertions(+)
```

## Gate

Command: python3 -m venv .venv && .venv/bin/pip install -q -r requirements.txt && .venv/bin/python -m unittest tests.py
Exit code: 0

Output (last 60 lines):
```
........
----------------------------------------------------------------------
Ran 8 tests in 0.419s

OK
```

## Run

Tool: aider
Model: bedrock/zai.glm-5
Minutes: 1
AI cost (USD): 0.0096

## Coder's note (unverified)

````
hn follows susan
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

    def test_post_excerpt(self):
        # Test case where body is shorter than n
        p1 = Post(body="short")
        self.assertEqual(p1.excerpt(10), "short")

        # Test case where body is longer than n
        p2 = Post(body="abcdefghij")
        self.assertEqual(p2.excerpt(5), "abcde...")

    def test_post_count(self):
        u = User(username='john', email='john@example.com')
        db.session.add(u)
        db.session.commit()
        self.assertEqual(u.post_count(), 0)

        p1 = Post(body="post 1", author=u)
        p2 = Post(body="post 2", author=u)
        db.session.add_all([p1, p2])
        db.session.commit()
        self.assertEqual(u.post_count(), 2)


class HealthCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)

    def test_health(self):
        response = self.app.test_client().get('/api/health')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'status': 'ok'})


class UtilsCase(unittest.TestCase):
    def test_slugify(self):
        self.assertEqual(slugify("Hello, World!"), "hello-world")
        self.assertEqual(slugify("  A  b "), "a-b")


if __name__ == '__main__':
    unittest.main(verbosity=2)
```
Tokens: 5.0k sent, 1.4k received. Cost: $0.0096 message, $0.0096 session.
Applied edit to app/main/utils.py
Applied edit to tests.py

````
