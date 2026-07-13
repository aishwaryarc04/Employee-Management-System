import unittest
from app import app

class EmployeeAPITest(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    # Test Home API
    def test_home(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    # Test GET All Employees
    def test_get_all_employees(self):
        response = self.client.get("/employees")
        self.assertEqual(response.status_code, 200)

    # Test GET Employee By ID
    def test_get_employee(self):
        response = self.client.get("/employees/1001")
        self.assertIn(response.status_code, [200, 404])

    # Test DELETE Invalid Employee
    def test_delete_invalid_employee(self):
        response = self.client.delete("/employees/99999")
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()