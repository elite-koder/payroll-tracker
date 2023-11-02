from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=64, unique=True)
    address = models.TextField(max_length=200)
    contact_person = models.CharField(max_length=64)
    contact_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=64)
    website = models.URLField(max_length=64)
    logo = models.ImageField(upload_to="static/organization/logo", blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)