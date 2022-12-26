from rest_framework import serializers

from purchaser.models import Purchaser


class PurchaserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchaser
        fields = ['first_name', 'second_name', 'sex', 'age', 'email']
