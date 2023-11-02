from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=64, unique=True, db_index=True)
    org = models.ForeignKey("organization.Organization", on_delete=models.DO_NOTHING, related_name="department_set")
    manager = models.ForeignKey("employee.Employee", on_delete=models.DO_NOTHING, null=True, related_name="manager_department_set")
