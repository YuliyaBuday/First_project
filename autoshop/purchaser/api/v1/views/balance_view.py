from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from car_dealership.api.v1.views.car_dealership_view import APIListPagination
from core.filters.purchaser_filters import BalanceFilter
from core.permissions import IsOwnerOrReadOnly
from purchaser.api.v1.serializers.balance_serializer import BalanceSerializer
from purchaser.models import Balance


class BalanceViewSet(viewsets.ModelViewSet):
    queryset = Balance.objects.all().order_by('time_create')
    serializer_class = BalanceSerializer
    pagination_class = APIListPagination
    permission_classes = (IsOwnerOrReadOnly,)
    filter_backends = [DjangoFilterBackend]
    filterset_class = BalanceFilter
    search_fields = ['value']


