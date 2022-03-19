from django.urls import path
from . import views


urlpatterns = [
    path('', views.user_login, name="home"),
    path('register/', views.register, name='register'),
    path('logout/', views.log_out, name='log_out'),
]
