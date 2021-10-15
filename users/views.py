from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.serializers import Serializer
from .serializers import UserSerializer
from .models import User
class UserViewCreate(CreateAPIView):
    
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserViewList(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()