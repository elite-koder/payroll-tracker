from django.db import models


class Designation(models.Model):
    name = models.CharField(max_length=64, unique=True, db_index=True)
    org = models.ForeignKey("organization.Organization", on_delete=models.DO_NOTHING, related_name="designation_set")