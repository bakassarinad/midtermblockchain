from goods import views
from django.urls import path

app_name = 'goods'

urlpatterns = [
    path('add/', views.GoodViewCreate.as_view(), name='good_create'),
    path('list/', views.GoodViewList.as_view(), name='good_list')
]