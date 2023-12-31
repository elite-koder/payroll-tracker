# Generated by Django 4.2.6 on 2023-11-01 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('address', models.TextField(max_length=200)),
                ('contact_person', models.CharField(max_length=64)),
                ('contact_number', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=64)),
                ('website', models.URLField(max_length=64)),
                ('logo', models.ImageField(blank=True, upload_to='static/organization/logo')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
