from rest_framework import viewsets


from car_dealership.api.v1.serializer.category_serializer import CategorySerializer
from car_dealership.api.v1.views.car_dealership_view import APIListPagination
from car_dealership.models import Category
from core.permissions import IsAdminOrReadOnly


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('time_create')
    serializer_class = CategorySerializer
    pagination_class = APIListPagination
    permission_classes = (IsAdminOrReadOnly,)
    search_fields = ['name']
