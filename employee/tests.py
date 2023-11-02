from django.test import TestCase

# Create your tests here.

class EmployeeTestCase(TestCase):
    def setUp(self):
        pass

    def test_employee(self):
        from organization.models import Organization
        org = Organization.objects.create(name="Test", address="Test", contact_person="Test", contact_number="Test", email="Test", website="Test")
        from department.models import Department
        from designation.models import Designation
        dep = Department.objects.create(name="Test", org=org)
        des = Designation.objects.create(name="Test", org=org)
        data = {
            "user.first_name": "fname",
            "user.last_name": "lname",
            "user.email": "email@email.com",
            "user.username": "username",
            "user.org": org.id,
            'org': org.id,
            'department': dep.id,
            'designation': des.id,
            'level': 1,
            'status': 'Active',
            'dob': '2023-10-10',
            'doj': '2023-10-10',
            'pan_number': '1234567890',
            'aadhar_number': '123456789012',
            'mobile': '9876543210'
        }
        resp = self.client.post("/payroll_tracker/admin/employee/create/", data=data)
        print(resp.status_code)
        print(resp.content)