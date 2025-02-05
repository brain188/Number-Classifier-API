import unittest
from app import create_app

class TestNumberClassificationAPI(unittest.TestCase):
    """Test suite for the Number Classification API."""

    @classmethod
    def setUpClass(cls):
        """Set up a test client before running tests."""
        cls.app = create_app()
        cls.app.config['TESTING'] = True
        cls.client = cls.app.test_client()

    def test_valid_number(self):
        """Test API response for a valid number."""
        response = self.client.get('/api/classify-number')
        self.assertEqual(response.status_code, 200)
        json_data = response.get_json()
        self.assertEqual(json_data["number"], 371)
        self.assertIn("properties", json_data)
        self.assertIn("fun_fact", json_data)

    def test_invalid_number(self):
        """Test API response for an invalid number input (non-numeric)."""
        response = self.client.get('/api/classify-number?number=abc')
        self.assertEqual(response.status_code, 400)
        json_data = response.get_json()
        self.assertTrue(json_data["error"])

    def test_negative_number(self):
        """Test API response for a negative number."""
        response = self.client.get('/api/classify-number?number=-5')
        self.assertEqual(response.status_code, 200)
        json_data = response.get_json()
        self.assertEqual(json_data["number"], -5)

    def test_missing_number(self):
        """Test API response when no number parameter is provided."""
        response = self.client.get('/api/classify-number')
        self.assertEqual(response.status_code, 400)
        json_data = response.get_json()
        self.assertTrue(json_data["error"])

    @classmethod
    def tearDownClass(cls):
        """Clean up after all tests are run."""
        pass  

if __name__ == '__main__':
    unittest.main()
