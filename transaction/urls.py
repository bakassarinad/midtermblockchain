from transaction import views
from django.urls import path

app_name='transaction'

urlpatterns = [
    path('add/', views.OrderViewCreate.as_view({'post': 'create'}), name = 'order_create')
]