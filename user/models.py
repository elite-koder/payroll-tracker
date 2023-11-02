from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    org = models.ForeignKey("organization.Organization", on_delete=models.DO_NOTHING, related_name="employer_user_set")
