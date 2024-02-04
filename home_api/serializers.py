from rest_framework import serializers

from home_api.models import TestItem


class TestItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestItem
        fields = '__all__'
