from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from car_dealership.api.v1.views.car_dealership_view import APIListPagination
from core.filters.supplier_filters import FounderFilter
from supplier.api.v1.serializer.founder_serializer import FounderSerializer
from supplier.models import Founder


class FounderViewSet(viewsets.ModelViewSet):
    queryset = Founder.objects.all().order_by('time_create')
    serializer_class = FounderSerializer
    pagination_class = APIListPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = FounderFilter
    search_fields = ['first_name', 'second_name']
    ordering_fields = ['first_name']
