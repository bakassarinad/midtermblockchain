from django.shortcuts import render

from rest_framework.generics import CreateAPIView, ListAPIView

from .serializers import GoodSerializer
from .models import Good
class GoodViewCreate(CreateAPIView):
    
    serializer_class = GoodSerializer
    queryset = Good.objects.all()

class GoodViewList(ListAPIView):
    serializer_class = GoodSerializer
    queryset = Good.objects.all()
