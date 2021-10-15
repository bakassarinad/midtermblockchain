from rest_framework import serializers

from .models import Good

class GoodSerializer(serializers.ModelSerializer):
    model = Good
    class Meta:
        model = Good
        fields = ['name', 'capacity']