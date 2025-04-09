import unittest
from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_add(self):
        response = self.client.get('/add?a=3&b=4')
        json_data = response.get_json()
        self.assertEqual(json_data['result'], 7)

if __name__ == '__main__':
    unittest.main()
