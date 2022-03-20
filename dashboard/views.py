from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# DASHBOARD
@login_required(login_url='home')
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')


# PROFILE
@login_required(login_url='home')
def profile(request):
    return render(request, 'dashboard/profile.html')


# ACCOUNT SETTINGS
@login_required(login_url='home')
def account_settings(request):
    return render(request, 'dashboard/account_settings.html')