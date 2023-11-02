from organization.models import Organization
org = Organization.objects.create(name="Test", address="Test", contact_person="Test", contact_number="Test", email="Test", website="Test")
from designation.models import Designation
from department.models import Department
Department.objects.create(name="Test", org=org)
Designation.objects.create(name="Test", org=org)


# from django.contrib.auth.models import Token
# from user.models import User
# token = Token.objects.create(user=User.objects.all()[0])
# print(token.key)
