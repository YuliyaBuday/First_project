from django.db import models
from django_countries.fields import CountryField

from core.abstract_models import AbstractDefaultModels
from core.enams.supplier_enums import SexOfSupplier
from core.validators import check_age


# Create your models here.
class Supplier(AbstractDefaultModels):
    name = models.CharField(max_length=255)
    location = CountryField()
    email = models.EmailField()
    auto = models.CharField(max_length=255)
    reviews = models.TextField(max_length=500)
    founder = models.ForeignKey(
        'Founder',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

    def __str__(self):
        return self.name


class Founder(AbstractDefaultModels):
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    age = models.IntegerField(validators=[check_age], default=25)
    company = models.CharField(max_length=255)
    email = models.EmailField()
    sex = models.CharField(
        max_length=6,
        choices=SexOfSupplier.choices,
        default=SexOfSupplier.Female
    )

    class Meta:
        ordering = ['first_name']
        verbose_name = 'Основатель'
        verbose_name_plural = 'Основатели'

    def __str__(self):
        return self.first_name