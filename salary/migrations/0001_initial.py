# Generated by Django 4.2.6 on 2023-10-31 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalaryStructure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basic', models.IntegerField()),
                ('hra', models.IntegerField()),
                ('conveyance', models.IntegerField()),
                ('medical', models.IntegerField()),
                ('special_allowance', models.IntegerField()),
                ('pf', models.IntegerField()),
                ('esi', models.IntegerField()),
                ('tds', models.IntegerField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='maintain_salary_structure_set', to='employee.employee')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='employee_salary_structure_set', to='employee.employee')),
            ],
        ),
        migrations.CreateModel(
            name='SalaryPaymentHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(choices=[('January', 'Jan'), ('February', 'Feb'), ('March', 'Mar'), ('April', 'Apr'), ('May', 'May'), ('June', 'Jun'), ('July', 'Jul'), ('August', 'Aug'), ('September', 'Sep'), ('October', 'Oct'), ('November', 'Nov'), ('December', 'Dec')], max_length=20)),
                ('year', models.IntegerField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='employee_salary_payment_history_set', to='employee.employee')),
                ('salary_structure', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='salary_structure_salary_payment_history_set', to='salary.salarystructure')),
                ('triggered_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='triggered_salary_payment_history_set', to='employee.employee')),
            ],
        ),
        migrations.CreateModel(
            name='DeductionClaim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('claim_type', models.CharField(choices=[('HRA', 'Hra'), ('LTA', 'Lta'), ('Home Loan Interest', 'Home Loan Interest'), ('Section 80C', 'Section 80C'), ('Section 80CCC', 'Section 80Ccc'), ('Section 80CCD', 'Section 80Ccd'), ('Section 80E', 'Section 80E'), ('Section 80G', 'Section 80G'), ('Section 80TTA', 'Section 80Tta'), ('Section 80D', 'Section 80D')], max_length=30)),
                ('financial_year', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('desc', models.TextField(max_length=200)),
                ('approved', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='employee_deduction_claim_set', to='employee.employee')),
            ],
        ),
    ]
