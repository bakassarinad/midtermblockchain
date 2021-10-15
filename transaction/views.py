from django.shortcuts import render

from .serializers import OrderSerializer
from rest_framework import generics
from .models import Order
from rest_framework import viewsets, parsers
from datetime import datetime
class OrderViewCreate(viewsets.ModelViewSet):
    
    serializer_class = OrderSerializer

