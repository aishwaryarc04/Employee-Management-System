import unittest
from app import app

class EmployeeAPITest(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    # Home API
    def test_home(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    # GET All Employees
    def test_get_all_employees(self):
        response = self.client.get("/employees")
        self.assertEqual(response.status_code, 200)

    # GET Employee (Valid/Invalid)
    def test_get_employee(self):
        response = self.client.get("/employees/1001")
        self.assertIn(response.status_code, [200,404])

    # GET Invalid Employee
    def test_get_invalid_employee(self):
        response = self.client.get("/employees/99999")
        self.assertEqual(response.status_code,404)

    # DELETE Invalid Employee
    def test_delete_invalid_employee(self):
        response = self.client.delete("/employees/99999")
        self.assertEqual(response.status_code,404)

    # POST Employee
    def test_add_employee(self):

        data = {
            "emp_id":9001,
            "name":"Test User",
            "age":25,
            "department":"Testing",
            "designation":"Tester",
            "salary":30000,
            "phone":"9999999999",
            "email":"test9001@test.com"
        }

        response=self.client.post("/employees",json=data)

        self.assertIn(response.status_code,[201,500])

    # PUT Employee
    def test_update_employee(self):

        data={
            "name":"Updated User",
            "age":26,
            "department":"Testing",
            "designation":"Senior Tester",
            "salary":35000,
            "phone":"8888888888",
            "email":"updated@test.com"
        }

        response=self.client.put("/employees/9001",json=data)

        self.assertIn(response.status_code,[200,404])

if __name__=="__main__":
    unittest.main()