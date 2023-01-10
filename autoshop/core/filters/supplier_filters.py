from django_filters import rest_framework as filters

from core.enams.supplier_enums import SexOfSupplier
from supplier.models import Supplier, Founder


class SupplierFilter(filters.FilterSet):
    name = filters.CharFilter()

    class Meta:
        model = Supplier
        fields = ['name', 'location']


class FounderFilter(filters.FilterSet):
    first_name = filters.CharFilter()
    sex = filters.ChoiceFilter(
        choices=SexOfSupplier.choices
    )

    class Meta:
        model = Founder
        fields = ['first_name', 'sex']
