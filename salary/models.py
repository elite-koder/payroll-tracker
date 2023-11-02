from django.db import models


class MonthEnum(models.TextChoices):
    JAN = "January"
    FEB = "February"
    MAR = "March"
    APR = "April"
    MAY = "May"
    JUN = "June"
    JUL = "July"
    AUG = "August"
    SEP = "September"
    OCT = "October"
    NOV = "November"
    DEC = "December"


class DeductionClaimTypeEnum(models.TextChoices):
    HRA = "HRA"
    LTA = "LTA"
    HOME_LOAN_INTEREST = "Home Loan Interest"
    SECTION_80C = "Section 80C" # Premium to be paid for life insurance and/or investments to be made in ELSS funds, PPF, NPS and/or school tuition fees for children, etc.
    SECTION_80CCC = "Section 80CCC" # Premium to be paid for annuity plan/Pension Fund
    SECTION_80CCD = "Section 80CCD" # Additional contributions made to NPS
    SECTION_80E = "Section 80E" # Education Loan Interest
    SECTION_80G = "Section 80G" # Donations
    SECTION_80TTA = "Section 80TTA" # Interest on Savings Account
    SECTION_80D = "Section 80D" # Medical Insurance

class DeductionClaim(models.Model):
    employee = models.ForeignKey("employee.Employee", on_delete=models.DO_NOTHING, related_name="employee_deduction_claim_set")
    claim_type = models.CharField(choices=DeductionClaimTypeEnum.choices, max_length=30)
    financial_year = models.IntegerField()
    amount = models.IntegerField() # amount to be claimed
    desc = models.TextField(max_length=200) # description of the claim
    approved = models.BooleanField(default=False) # true if approved by the employer
    created_on = models.DateTimeField(auto_now_add=True)


class SalaryStructure(models.Model):
    employee = models.ForeignKey("employee.Employee", on_delete=models.DO_NOTHING, related_name="employee_salary_structure_set")
    basic = models.IntegerField()
    hra = models.IntegerField()
    conveyance = models.IntegerField()
    medical = models.IntegerField()
    special_allowance = models.IntegerField()
    pf = models.IntegerField()
    esi = models.IntegerField()
    tds = models.IntegerField()
    added_by = models.ForeignKey("employee.Employee", on_delete=models.DO_NOTHING, related_name="maintain_salary_structure_set")
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)


class SalaryPaymentHistory(models.Model):
    employee = models.ForeignKey("employee.Employee", on_delete=models.DO_NOTHING, related_name="employee_salary_payment_history_set")
    salary_structure = models.ForeignKey("SalaryStructure", on_delete=models.DO_NOTHING, related_name="salary_structure_salary_payment_history_set")
    month = models.CharField(choices=MonthEnum.choices, max_length=20)
    year = models.IntegerField()
    triggered_by = models.ForeignKey("employee.Employee", on_delete=models.DO_NOTHING, related_name="triggered_salary_payment_history_set")
    created_on = models.DateTimeField(auto_now_add=True)