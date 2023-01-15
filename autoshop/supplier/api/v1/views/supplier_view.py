from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from car_dealership.api.v1.views.car_dealership_view import APIListPagination
from core.filters.supplier_filters import SupplierFilter
from core.permissions import IsAdminOrReadOnly
from supplier.api.v1.serializer.supplier_serializer import SupplierSerializer
from supplier.models import Supplier


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all().order_by('time_create')
    serializer_class = SupplierSerializer
    pagination_class = APIListPagination
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = [DjangoFilterBackend]
    filterset_class = SupplierFilter
    search_fields = ['name', 'location']
    ordering_fields = ['location']
