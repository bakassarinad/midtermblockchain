from datetime import datetime
from rest_framework import serializers
from goods.serializers import GoodSerializer
from transaction.models import Order
from users.serializers import UserSerializer
class OrderSerializer(serializers.ModelSerializer):


   # good = serializers.StringRelatedField()
    
    class Meta:
        model = Order
        fields = "__all__"
        read_only_fields = ['packaging', 'transit', 'status']
        
    