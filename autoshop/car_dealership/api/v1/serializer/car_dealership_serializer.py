from rest_framework import serializers

from car_dealership.models import Car_dealership


class Car_dealershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car_dealership
        fields = ['name', 'location', 'contact']