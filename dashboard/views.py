from django.shortcuts import render, redirect, reverse
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
    user = request.user

    user_data = User.objects.get(pk=user.id)
    last_login = user_data.last_login
    date_joined = user_data.date_joined

    user_data = BuildResume.objects.all().filter(user_id=user.id)
    last_user_data = user_data[len(user_data) - 1]

    data ={
        "data": last_user_data,
        # "last_login": last_login.strftime("%d %B %Y"),
        "last_login": last_login.strftime("%I:%M %p, %d-%B-%Y"),
        "date_joined": date_joined.strftime("%I:%M %p, %d-%B-%Y"),
    }

    return render(request, 'dashboard/profile.html', data)


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


#   DELETE ACCOUNT
def delete_account(request, id):
    if request.method == "POST":

        sure = request.POST.get("sure", False)

        if sure == "on":
            user_id = request.user.id
            user = User.objects.get(pk=user_id)
            user.delete()

            return redirect('home')

        else:
            return render(request, 'dashboard/account_settings.html', {"delete_message": "Please select checkbox before delete your account."})


    

# BUILD RESUME
@login_required(login_url='home')
def build_resume(request):
    if request.method == "POST":
        #   PHOTO
        profile_img = request.FILES["profile_img"]
        cover_img = request.FILES["cover_img"]

        resume_title = request.POST['resume_title']

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
        
        user = User.objects.get(pk=user_id)

        if BuildResume.objects.filter(resume_title=resume_title, user_id=user.id).exists():
            return render(request, 'dashboard/build_resume.html', {"message": "Resume Title Not Available."})
        else:
            resume = BuildResume(user_id=user_id, email=email, resume_title=resume_title, profile_photo=profile_img, cover_photo=cover_img, profession=profession, country=country, city=city,phone=phone, job_title=job_title, employer=employer, job_city=job_city, job_country=job_country, job_start_date=start_date_job,job_end_date=end_date_job, job_description=job_description, school_name=school_name, school_location=school_location,
            degree=degree, field_of_study=field_of_study, school_start_date=start_date_study, school_end_date=end_date_study,skills=skills, about_you=about_you, project_title=project_title, project_date=project_created_date, project_description=about_project,
            website=website, twitter=twitter, linkedin=linkedin)

            resume.save()

            return redirect('all_resume')

    else:
        return render(request, 'dashboard/build_resume.html')


#   ALL RESUMES
@login_required(login_url='home')
def all_resume(request):
    user = request.user

    resumes = BuildResume.objects.order_by('-updated_date').filter(user_id=user.id)

    if resumes:
        return render(request, 'dashboard/all_resumes.html', {"resumes": resumes})
    else:
        return render(request, 'dashboard/all_resumes.html')


#   READ RESUME
@login_required(login_url='home')
def read_resume(request, id):
    return render(request, 'dashboard/read_resume.html')


#   DELETE RESUME
@login_required(login_url='home')
def delete_resume(request, id):
    
    resume = BuildResume.objects.get(pk=id)
    resume.delete()

    return redirect('all_resume')


#   UPDATE RESUME
@login_required(login_url='home')
def update_resume(request, id):
    resume = BuildResume.objects.get(pk=id)

    if request.method == "POST":
        #   FETCH DATE
        profile_img = request.FILES["profile_img"]
        cover_img = request.FILES["cover_img"]

        profession = request.POST["profession"]
        country = request.POST["country"]
        city = request.POST["city"]
        phone = request.POST["phone"]

        job_title = request.POST["job_title"]
        employer = request.POST["employer"]
        job_city = request.POST["job_city"]
        job_country = request.POST["job_country"]
        start_date_job = request.POST["start_date_job"]
        end_date_job = request.POST["end_date_job"]
        job_description = request.POST["job_description"]

        school_name = request.POST["school_name"]
        school_location = request.POST["school_location"]
        degree = request.POST["degree"]
        field_of_study = request.POST["field_of_study"]
        start_date_study = request.POST["start_date_study"]
        end_date_study = request.POST["end_date_study"]

        skills = request.POST["skills"]

        about_you = request.POST["about_you"]

        project_title = request.POST["project_title"]
        project_created_date = request.POST["project_created_date"]
        about_project = request.POST["about_project"]

        website = request.POST["website"]
        twitter = request.POST["twitter"]
        linkedin = request.POST["linkedin"]

        #   UPDATE DATA
        resume.profile_photo = profile_img
        resume.cover_photo = cover_img

        resume.profession = profession
        resume.country = country
        resume.city = city
        resume.phone = phone

        resume.job_title = job_title
        resume.employer = employer
        resume.job_city = job_city
        resume.job_country = job_country
        resume.job_start_date = start_date_job
        resume.job_end_date = end_date_job
        resume.job_description = job_description

        resume.school_name = school_name
        resume.school_location = school_location
        resume.degree = degree
        resume.field_of_study = field_of_study
        resume.school_start_date = start_date_study
        resume.school_end_date = end_date_study

        resume.skills = skills
        resume.about_you = about_you

        resume.project_title = project_title
        resume.project_date = project_created_date
        resume.project_description = about_project

        resume.website = website
        resume.twitter = twitter
        resume.linkedin = linkedin

        resume.save()

        return redirect('all_resume')


    else:
        return render(request, 'dashboard/update_resume.html', {"resume": resume})


# NEED HELP
@login_required(login_url='home')
def need_help(request):
    return render(request, 'dashboard/need_help.html')