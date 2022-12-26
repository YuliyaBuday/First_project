from rest_framework import serializers

from car_dealership.models import Raiting


class RaitingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Raiting
        fields = ['value', 'time_create']

