from django_filters import rest_framework as filters

from car_dealership.models import Car, Car_dealership
from core.enams.car_dealership_enums import Currency


class CarFilter(filters.FilterSet):
    price = filters.RangeFilter()
    currency = filters.ChoiceFilter(
        choices=Currency.choices,
    )
    year = filters.RangeFilter()

    class Meta:
        model = Car
        fields = ['price', 'currency', 'year']


class Car_dealershipFilter(filters.FilterSet):
    name = filters.CharFilter()

    class Meta:
        model = Car_dealership
        fields = ['name', 'location']
