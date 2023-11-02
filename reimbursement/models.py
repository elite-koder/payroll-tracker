from django.db import models


class ExpenseClaimStatusEnum(models.TextChoices):
    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"

class ExpenseClaim(models.Model):
    employee = models.ForeignKey("employee.Employee", on_delete=models.DO_NOTHING)
    amount = models.IntegerField()
    desc = models.TextField(max_length=200)
    status = models.CharField(choices=ExpenseClaimStatusEnum.choices, max_length=20)
    proofs = models.ManyToManyField("ExpenseProof")
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

class ExpenseProof(models.Model):
    file = models.FileField(upload_to="static/expense/proof")
