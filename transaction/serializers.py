from datetime import datetime
from rest_framework import serializers

from goods.serializers import GoodSerializer
from .models import Order
from  goods.models import Good

class OrderSerializer(serializers.Serializer):
    good = GoodSerializer(many=True)
    user = serializers.HiddenField()

    time_start = serializers.DateField()
    packaging = serializers.IntegerField(read_only=True, default = 3)
    transit = serializers.IntegerField(read_only=True, default = 5)

    name = serializers.CharField(max_length=50)

    def create(self, validated_data):
        if not self.id:
            self.time_start=datetime.now()
        good = validated_data.pop('good')
        order = Order.objects.create(**validated_data)
        Good.objects.create(order=order, **good)
        return order
