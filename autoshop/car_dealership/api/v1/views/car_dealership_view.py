from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import GenericViewSet

from car_dealership.api.v1.serializer.car_dealership_serializer import Car_dealershipSerializer
from car_dealership.models import Car_dealership
from core.filters.car_dealership_filters import Car_dealershipFilter


class APIListPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page_side'
    max_page_size = 10


class Car_dealershipViewSet(mixins.CreateModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            mixins.ListModelMixin,
                            GenericViewSet):
    queryset = Car_dealership.objects.all()
    serializer_class = Car_dealershipSerializer
    pagination_class = APIListPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = Car_dealershipFilter
    search_fields = ['name']
    ordering_fields = ['location']
