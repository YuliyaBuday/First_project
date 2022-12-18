from django.db import models


class SexOfPurchaser(models.TextChoices):
    Male = 'Male', 'Male'
    Female = 'Female', 'Female'