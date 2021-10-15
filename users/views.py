from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.serializers import Serializer
from .serializers import UserSerializer
from .models import User
class UserViewSet(CreateAPIView):
    
    serializer_class = UserSerializer
    queryset = User.objects.all()
