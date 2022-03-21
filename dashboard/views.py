from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .models import BuildResume


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
    

# BUILD RESUME
@login_required(login_url='home')
def build_resume(request):
    if request.method == "POST":
        #   PHOTO
        profile_img = request.FILES["profile_img"]
        cover_img = request.FILES["cover_img"]

        #   POPULATE DATA
        user_id = request.POST['user_id']
        email = request.POST['email']

        # PROFESSION
        profession = request.POST['profession']
        country = request.POST['country']
        city = request.POST['city']
        phone = request.POST['phone']

        #   WORK HISTORY
        job_title = request.POST['job_title']
        employer = request.POST['employer']
        job_city = request.POST['job_city']
        job_country = request.POST['job_country']
        start_date_job = request.POST['start_date_job']
        end_date_job = request.POST['end_date_job']
        job_description = request.POST['job_description']

        #   SCHOOL INFO
        school_name = request.POST['school_name']
        school_location = request.POST['school_location']
        degree = request.POST['degree']
        field_of_study = request.POST['field_of_study']
        start_date_study = request.POST['start_date_study']
        end_date_study = request.POST['end_date_study']

        #   SKILLS
        skills = request.POST['skills']

        #   BERIEFLY INTRO
        about_you = request.POST['about_you']

        #   PROJECT
        project_title = request.POST['project_title']
        project_created_date = request.POST['project_created_date']
        about_project = request.POST['about_project']

        #   SOCIAL ACCOUNT
        website = request.POST['website']
        twitter = request.POST['twitter']
        linkedin = request.POST['linkedin']
        

        resume = BuildResume(user_id=user_id, email=email, profile_photo=profile_img, cover_photo=cover_img, profession=profession, country=country, city=city,
                            phone=phone, job_title=job_title, employer=employer, job_city=job_city, job_country=job_country, job_start_date=start_date_job,
                            job_end_date=end_date_job, job_description=job_description, school_name=school_name, school_location=school_location,
                            degree=degree, field_of_study=field_of_study, school_start_date=start_date_study, school_end_date=end_date_study,
                            skills=skills, about_you=about_you, project_title=project_title, project_date=project_created_date, project_description=about_project,
                            website=website, twitter=twitter, linkedin=linkedin)

        resume.save()

        return redirect('profile')

    else:
        return render(request, 'dashboard/build_resume.html')


# NEED HELP
@login_required(login_url='home')
def need_help(request):
    return render(request, 'dashboard/need_help.html')