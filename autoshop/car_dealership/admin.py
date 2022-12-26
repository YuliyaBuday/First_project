from django.conf.locale import sq
from django.contrib import admin, messages

from django.db.models import QuerySet

from car_dealership.models import Car, Car_dealership, Raiting, Category
from core.enams.car_dealership_enums import Currency


# Register your models here.


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'currency', 'cat']
    ordering = ['title']
    search_fields = ['title__istartswith']
    actions = ['change_to_euro', 'change_to_dollars','change_to_rubles', 'change_price']


    @admin.action(description=' Изменить валюту избранных элементов на евро')
    def change_to_euro(self, request, qs: QuerySet):
        updates_cars = qs.update(currency=Currency.EUR)
        self.message_user(
            request,
            f'Обновлено {updates_cars} записей',
            messages.SUCCESS
        )

    @admin.action(description=' Изменить валюту избранных элементов на доллары США')
    def change_to_dollars(self, request, qs: QuerySet):
        updates_cars = qs.update(currency=Currency.USD)
        self.message_user(
            request,
            f'Обновлено {updates_cars} записей',
            messages.SUCCESS
        )

    @admin.action(description=' Изменить валюту избранных элементов на российские рубли')
    def change_to_rubles(self, request, qs: QuerySet):
        updates_cars = qs.update(currency=Currency.RUB)
        self.message_user(
            request,
            f'Обновлено {updates_cars} записей',
            messages.SUCCESS
        )

    @admin.action(description=' Изменить цену у всех выбранных объектов на 5000')
    def change_price(self, request, qs: QuerySet):
        updates_price = qs.update(price=5000)
        self.message_user(
            request,
            f'Обновлено {updates_price} записей',
            messages.SUCCESS
        )


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
    actions = ['change_to_10']

    @admin.action(description=' Изменить рейтинг у всех объектов на 10')
    def change_to_10(self, request, qs: QuerySet):
        updates_value = qs.update(value=10)
        self.message_user(
            request,
            f'Обновлено {updates_value} записей',
            messages.SUCCESS
        )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']
    search_fields = ['name']
    actions = ['change_category']

    @admin.action(description=' Изменить категорию всех элементов на легковую')
    def change_category(self, request, qs: QuerySet):
        updates_cat = qs.update(name='легковая')
        self.message_user(
            request,
            f'Обновлено {updates_cat} записей',
            messages.SUCCESS
        )