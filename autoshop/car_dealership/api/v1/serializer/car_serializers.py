from rest_framework import serializers

from car_dealership.models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['title', 'price', 'currency', 'cat', 'status']