from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
 # order = serializers.StringRelatedField()

    class Meta:
        model = User
        fields = ['username']