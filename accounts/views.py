from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('test_page')
        else:
            return render(request, 'accounts/login.html', {"message": "Username not exists"})

    else:
        return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:

            if User.objects.filter(username=username).exists():
                return render(request, 'accounts/register.html', {"message": "Username not abvalible"})
            else:
                if User.objects.filter(email=email).exists():
                    return render(request, 'accounts/register.html', {"message": "Email not abvalible"})
                else:

                    # CREATE USER
                    user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)

                    login(request, user)

                    user.save()

                    # return render(request, 'accounts/test.html', {"message": "welcome"})
                    return redirect('test_page')

        else:
            return render(request, 'accounts/register.html', {"message": "Password not match with confirm password"})
    else:
        return render(request, 'accounts/register.html')


def test_page(request):
    return render(request, 'accounts/test.html')


def log_out(request):
    logout(request)
    return redirect('home')