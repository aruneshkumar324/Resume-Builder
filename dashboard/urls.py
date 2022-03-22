from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('account_settings/', views.account_settings, name='account_settings'),
    path('delete_account/<int:id>/', views.delete_account, name='delete_account'),
    path('new_password/', views.new_password, name='new_password'),
    path('need_help/', views.need_help, name='need_help'),
    path('build_resume/', views.build_resume, name='build_resume'),
    path('all_resume/', views.all_resume, name='all_resume'),
    path('read_resume/<int:id>/', views.read_resume, name='read_resume'),
    path('delete_resume/<int:id>/', views.delete_resume, name="delete_resume"),
    path('update_resume/<int:id>/', views.update_resume, name="update_resume"),
]
