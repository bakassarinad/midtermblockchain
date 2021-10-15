from users import views
from django.urls import path

app_name = 'user'

urlpatterns = [
    path('/add/', views.UserViewSet.as_view(), name='user_create')
]