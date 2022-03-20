from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout


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
    if request.method == 'POST':
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']

        user = User.objects.get(id=user_id)

        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email

        user.save()

        return redirect('profile')

    return render(request, 'dashboard/account_settings.html')



@login_required(login_url='home')
def new_password(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        passsword = request.POST['passsword']
        confirm_passsword = request.POST['confirm_passsword']

        if passsword == confirm_passsword:
            # set new password
            data = User.objects.get(id=user_id)
            data.set_password(passsword)

            data.save()

            # logout
            logout(request)

            # rediect
            return redirect('home')

        else:
            return render(request, 'dashboard/account_settings.html', {"message": "Password not match with confirm password"})
    else:
        return render(request, 'dashboard/account_settings.html')