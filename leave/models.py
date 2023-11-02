from django.db import models


class LeaveTypeEnum(models.TextChoices):
    CASUAL = "Casual"
    SICK = "Sick"
    EARNED = "Earned"
    MATERNITY = "Maternity"
    PATERNITY = "Paternity"
    BEREAVEMENT = "Bereavement"
    COMPASSIONATE = "Compassionate"
    STUDY = "Study"
    UNPAID = "Unpaid"
    SPECIAL = "Special"


class LeaveStatusEnum(models.TextChoices):
    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"


class Leave(models.Model):
    employee = models.ForeignKey("employee.Employee", on_delete=models.DO_NOTHING, related_name="employee_leave_set")
    from_date = models.DateField()
    to_date = models.DateField()
    type = models.CharField(choices=LeaveTypeEnum.choices, max_length=20)
    reason = models.TextField(max_length=200)
    status = models.CharField(choices=LeaveStatusEnum.choices, max_length=20, default=LeaveStatusEnum.PENDING)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)