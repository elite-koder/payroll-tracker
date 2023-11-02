from django.db import models
from django.utils import timezone


class Shift(models.Model):
    name = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()
    grace_in = models.IntegerField(default=0)
    grace_out = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)


class InOutEnum(models.TextChoices):
    IN = "In"
    OUT = "Out"


class AttendanceRegister(models.Model):
    employee = models.ForeignKey("employee.Employee", on_delete=models.DO_NOTHING)
    day = models.DateField()
    shift = models.ForeignKey(Shift, on_delete=models.DO_NOTHING)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('employee', 'day')


class InOutLog(models.Model):
    employee = models.ForeignKey("employee.Employee", on_delete=models.DO_NOTHING)
    in_out = models.CharField(choices=InOutEnum.choices, max_length=10)
    in_out_dt = models.DateTimeField(default=timezone.now)
    shift = models.ForeignKey(Shift, on_delete=models.DO_NOTHING)
    created_on = models.DateTimeField(auto_now_add=True)


class OverTimeRequestStatusEnum(models.TextChoices):
    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"


class OverTimeRequest(models.Model):
    employee = models.ForeignKey("employee.Employee", on_delete=models.DO_NOTHING, related_name="employee_overtime_set")
    date = models.DateField() # date of overtime
    minutes = models.IntegerField() # minutes of overtime
    reason = models.TextField(max_length=200)
    status = models.CharField(choices=OverTimeRequestStatusEnum.choices, max_length=20)
    reviewer = models.ForeignKey("employee.Employee", on_delete=models.DO_NOTHING, null=True, related_name="reviewer_overtime_set") # manager who reviewed
    created_on = models.DateTimeField(auto_now_add=True) # date and time of request
    modified_on = models.DateTimeField(auto_now=True) # date and time of last modification