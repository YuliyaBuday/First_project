from django.db import models


class SexOfSupplier(models.TextChoices):
    Male = 'Male', 'Male'
    Female = 'Female', 'Female'