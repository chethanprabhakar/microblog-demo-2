## Files changed

Base: origin/fleet/run-1794290198314

Names:
```
app/models.py
tests.py
```

Diff stat:
```
app/models.py | 10 ++++++++++
 tests.py      | 13 +++++++++++++
 2 files changed, 23 insertions(+)
```

## Gate

Command: python3 -m venv .venv && .venv/bin/pip install -q -r requirements.txt && .venv/bin/python -m unittest tests.py
Exit code: 0

Output (last 60 lines):
```
......
----------------------------------------------------------------------
Ran 6 tests in 0.420s

OK
```

## Run

Tool: aider
Model: bedrock/deepseek.v3.2
Minutes: 2
AI cost (USD): 0.01

## Coder's note (unverified)

````
llowers
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

    def test_post_excerpt(self):
        # Test case 1: body length <= n
        p1 = Post(body="short")
        self.assertEqual(p1.excerpt(10), "short")
        self.assertEqual(p1.excerpt(5), "short")
        
        # Test case 2: body length > n
        p2 = Post(body="abcdefghij")
        self.assertEqual(p2.excerpt(5), "abcde...")
        self.assertEqual(p2.excerpt(3), "abc...")
        self.assertEqual(p2.excerpt(10), "abcdefghij")
        self.assertEqual(p2.excerpt(11), "abcdefghij")


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
        self.assertEqual(response.content_type, 'application/json')
        data = response.get_json()
        self.assertEqual(data, {'status': 'ok'})


if __name__ == '__main__':
    unittest.main(verbosity=2)
```
Tokens: 7.0k sent, 4.3k received. Cost: $0.01 message, $0.01 session.
Applied edit to app/models.py
Applied edit to tests.py

````
