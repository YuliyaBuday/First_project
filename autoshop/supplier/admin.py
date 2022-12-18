from django.contrib import admin

from supplier.models import *


# Register your models here.
@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'email', 'auto', 'reviews']
    ordering = ['name']
    search_fields = ['name']


@admin.register(Founder)
class FounderAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'second_name', 'company']
    ordering = ['second_name']
    search_fields = ['company']