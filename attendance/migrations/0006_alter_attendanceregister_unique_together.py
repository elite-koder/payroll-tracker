# Generated by Django 4.2.6 on 2023-11-02 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0006_alter_employee_org'),
        ('attendance', '0005_rename_attendance_attendanceregister_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='attendanceregister',
            unique_together={('employee', 'day')},
        ),
    ]
