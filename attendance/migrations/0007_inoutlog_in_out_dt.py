# Generated by Django 4.2.6 on 2023-11-02 09:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0006_alter_attendanceregister_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='inoutlog',
            name='in_out_dt',
            field=models.DateTimeField(default=datetime.date(2023, 11, 2)),
            preserve_default=False,
        ),
    ]