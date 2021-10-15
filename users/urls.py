from users import views
from django.urls import path

app_name = 'user'

urlpatterns = [
    path('add/', views.UserViewCreate.as_view(), name='user_create'),
    path('list/', views.UserViewList.as_view(), name='user_list')
]