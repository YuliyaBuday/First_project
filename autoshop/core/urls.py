from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from car_dealership.api.v1.views.car_dealership_view import Car_dealershipViewSet
from car_dealership.api.v1.views.car_view import CarViewSet
from car_dealership.api.v1.views.category_view import CategoryViewSet
from car_dealership.api.v1.views.raiting_view import RaitingViewSet
from purchaser.api.v1.views.balance_view import BalanceViewSet
from purchaser.api.v1.views.purchaser_view import PurchaserViewSet
from supplier.api.v1.views.founder_view import FounderViewSet
from supplier.api.v1.views.supplier_view import SupplierViewSet

router = DefaultRouter()
router.register(r'cars', CarViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'car_dealership', Car_dealershipViewSet)
router.register(r'raiting', RaitingViewSet)
router.register(r'balance', BalanceViewSet)
router.register(r'purchaser', PurchaserViewSet)
router.register(r'supplier', SupplierViewSet)
router.register(r'founder', FounderViewSet)


urlpatterns = router.urls
