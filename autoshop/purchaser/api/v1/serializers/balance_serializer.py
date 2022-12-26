from rest_framework import serializers

from purchaser.models import Balance


class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balance
        fields = ['value', 'second_name', 'sex', 'age', 'email']