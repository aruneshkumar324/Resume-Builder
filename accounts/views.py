from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from dashboard.models import BuildResume, TemplateName



def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
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

                    # CREATE DEFUALT TEMPLATE
                    user_template = TemplateName(user_id=user.id, email=user.email, defualt_template_name="devresume")
                    user_template.save()

                    return redirect('dashboard')

        else:
            return render(request, 'accounts/register.html', {"message": "Password not match with confirm password"})
    else:
        return render(request, 'accounts/register.html')


def log_out(request):
    logout(request)
    return redirect('home')


#   SHARE RESUME LINK
def share_resume(request, username, id):
    resume = BuildResume.objects.get(pk=id)
    data = {
        "resume": resume,
    }

    template_name = TemplateName.objects.get(user_id=request.user.id)

    name = template_name.defualt_template_name

    if name == "devresume":
        return render(request, 'resume_templates/preview-1.html', data)
    elif name == "orbit":
        return render(request, 'resume_templates/preview-2.html', data)
    elif name == "pillar":
        return render(request, 'resume_templates/preview-3.html', data)
