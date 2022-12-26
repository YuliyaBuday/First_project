from rest_framework import serializers

from supplier.models import Founder


class FounderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Founder
        fields = ['first_name', 'second_name', 'age', 'company', 'email']