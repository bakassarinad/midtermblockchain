from transaction import views
from django.urls import path

app_name='transaction'

urlpatterns = [
    path('add/', views.OrderViewCreate.as_view({'post': 'create'}), name = 'order_create'),
    path('get/<int:pk>', views.OrderViewCreate.as_view({'get': 'retrieve'}), name = 'order_retrieve'),
    path('get/', views.OrderViewCreate.as_view({'get': 'list'}), name = 'order_list')

]