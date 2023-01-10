from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from car_dealership.api.v1.serializer.car_serializers import CarSerializer
from car_dealership.api.v1.views.car_dealership_view import APIListPagination
from car_dealership.models import Car
from core.filters.car_dealership_filters import CarFilter


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all().order_by('time_create')
    serializer_class = CarSerializer
    pagination_class = APIListPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = CarFilter
    search_fields = ['title', 'status']
    ordering_fields = ['title']

