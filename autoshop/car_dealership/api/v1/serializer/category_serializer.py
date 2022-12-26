from rest_framework import serializers

from car_dealership.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ['is_published']