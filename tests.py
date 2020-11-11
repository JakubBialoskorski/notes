from manage import app
import unittest

class FlaskTestCase(unittest.TestCase):
    def test_index_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_signup_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/signup/', content_type='html/text')
        self.assertTrue(b"Already" in response.data)

    def test_login_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/login/', content_type='html/text')
        self.assertTrue(b"Don't have" in response.data)

if __name__ == '__main__':
    unittest.main()