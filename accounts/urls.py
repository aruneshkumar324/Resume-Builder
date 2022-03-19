from django.urls import path
from . import views


urlpatterns = [
    path('', views.login, name="home"),
    path('register/', views.register, name='register'),
    path('test/', views.test, name='test'),
]
