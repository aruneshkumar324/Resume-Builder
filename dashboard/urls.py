from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('account_settings/', views.account_settings, name='account_settings'),
    path('new_password/', views.new_password, name='new_password'),
    path('need_help/', views.need_help, name='need_help'),
    path('build_resume/', views.build_resume, name='build_resume'),
    path('all_resume/', views.all_resume, name='all_resume'),
]
