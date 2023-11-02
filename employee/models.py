from django.db import models


class Level(models.IntegerChoices):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7

class EmployeeStatus(models.TextChoices):
    ACTIVE = "Active"
    INACTIVE = "Inactive"
    SUSPENDED = "Suspended"
    TERMINATED = "Terminated"
    ON_NOTICE_PERIOD = "On Notice Period"

class Employee(models.Model):
    user = models.OneToOneField("user.User", on_delete=models.DO_NOTHING, related_name="employee")
    mobile = models.CharField(max_length=10, db_index=True)
    address = models.TextField(max_length=200)
    department = models.ForeignKey("department.Department", on_delete=models.DO_NOTHING)
    designation = models.ForeignKey("designation.Designation", on_delete=models.DO_NOTHING)
    level = models.IntegerField(choices=Level.choices)
    profile_pic = models.ImageField(upload_to="static/employee/profile_pic", blank=True)
    status = models.CharField(choices=EmployeeStatus.choices, max_length=20)
    dob = models.DateField() # date of birth
    doj = models.DateField() # date of joining
    pan_number = models.CharField(max_length=10)
    aadhar_number = models.CharField(max_length=12)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    org = models.ForeignKey("organization.Organization", on_delete=models.DO_NOTHING, related_name="employee_set")