from django.contrib import admin

from car_dealership.models import *

# Register your models here.


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'currency', 'cat']
    ordering = ['title']
    search_fields = ['title__istartswith']


@admin.register(Car_dealership)
class Car_dealershipAdmin(admin.ModelAdmin):
    list_display = ['name', 'location']
    ordering = ['name']
    search_fields = ['name']


@admin.register(Raiting)
class RaitingAdmin(admin.ModelAdmin):
    list_display = ['cars', 'value']
    ordering = ['value']
    search_fields = ['value']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']
    search_fields = ['name']
