## Files changed

Base: origin/fleet/run-1794290198314

Names:
```
app/models.py
tests.py
```

Diff stat:
```
app/models.py |  7 +++++++
 tests.py      | 27 +++++++++++++++++++++++++++
 2 files changed, 34 insertions(+)
```

## Gate

Command: python3 -m venv .venv && .venv/bin/pip install -q -r requirements.txt && .venv/bin/python -m unittest tests.py
Exit code: 0

Output (last 60 lines):
```
.......
----------------------------------------------------------------------
Ran 7 tests in 0.452s

OK
```

## Run

Tool: aider
Model: bedrock/deepseek.v3.2
Minutes: 2
AI cost (USD): 0.01

## Coder's note (unverified)

````
     p2 = Post(body="second post", author=u1)
        db.session.add_all([p1, p2])
        db.session.commit()
        
        # Test with two posts
        self.assertEqual(u1.post_count(), 2)
        self.assertEqual(u1.posts_count(), 2)
        
        # Test another user still has 0 posts
        u2 = User(username='susan', email='susan@example.com')
        db.session.add(u2)
        db.session.commit()
        self.assertEqual(u2.post_count(), 0)
        self.assertEqual(u2.posts_count(), 0)


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

The changes made:

1. In `app/models.py`: Added a `post_count()` method that simply calls `posts_count()` with a docstring explaining it's an alias.

2. In `tests.py`: Added a new test method `test_post_count()` that:
   - Tests a user with no posts returns 0 for both `post_count()` and `posts_count()`
   - Tests a user with two posts returns 2 for both methods
   - Tests that another user still has 0 posts

The implementation meets all acceptance criteria:
- `User.post_count()` returns the number of posts the user has written
- A user with no posts returns 0; after adding two posts it returns 2
- The tests cover both cases (0 posts and 2 posts)
Tokens: 7.2k sent, 5.0k received. Cost: $0.01 message, $0.01 session.
Applied edit to app/models.py
Applied edit to tests.py

````
