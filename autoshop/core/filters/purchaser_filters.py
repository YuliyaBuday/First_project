from django_filters import rest_framework as filters

from core.enams.purchaser_enums import SexOfPurchaser
from purchaser.models import Purchaser, Balance


class PurchaserFilter(filters.FilterSet):
    first_name = filters.CharFilter()
    sex = filters.ChoiceFilter(
        choices=SexOfPurchaser.choices,
    )

    class Meta:
        model = Purchaser
        fields = ['first_name', 'sex']


class BalanceFilter(filters.FilterSet):
    value = filters.CharFilter()

    class Meta:
        model = Balance
        fields = ['value']