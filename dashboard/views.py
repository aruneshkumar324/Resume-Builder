from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .models import BuildResume, TemplateName
from django.core.paginator import Paginator


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
@login_required(login_url='home')
def delete_account(request, id):
    if request.method == "POST":

        sure = request.POST.get("sure", False)

        if sure == "on":
            # user account delete
            user_id = request.user.id
            user = User.objects.get(pk=user_id)
            user.delete()

            # delete user all resumes
            resumes = BuildResume.objects.all().filter(user_id=user_id)
            resumes.delete()

            # CREATE DEFUALT TEMPLATE
            user_template = TemplateName.objects.get(email=request.user.email)
            user_template.delete()

            return redirect('home')

        else:
            return render(request, 'dashboard/account_settings.html', {"delete_message": "Please select checkbox before delete your account."})


    

# BUILD RESUME
@login_required(login_url='home')
def build_resume(request):
    if request.method == "POST":
        #   PHOTO
        profile_photo = request.FILES["profile_photo"]

        resume_title = request.POST['resume_title']

        #   POPULATE DATA
        user_id = request.POST['user_id']
        email = request.POST['email']

        # PROFESSION
        profession = request.POST['profession']
        country = request.POST['country']
        city = request.POST['city']
        phone = request.POST['phone']

        skills = request.POST['skills']
        about_you = request.POST['about_you']
        interests = request.POST['interests']
        speaking_languages = request.POST['speaking_languages']

        #   AWARDS
        award_title_1 = request.POST['award_title_1']
        award_date_1 = request.POST['award_date_1']
        award_description_1 = request.POST['award_description_1']

        award_title_2 = request.POST['award_title_2']
        award_date_2 = request.POST['award_date_2']
        award_description_2 = request.POST['award_description_2']

        #   WORK HISTORY
        company_1 = request.POST['company_1']
        role_1 = request.POST['role_1']
        job_city_1 = request.POST['job_city_1']
        job_country_1 = request.POST['job_country_1']
        job_start_date_1 = request.POST['job_start_date_1']
        job_end_date_1 = request.POST['job_end_date_1']
        job_description_1 = request.POST['job_description_1']
        
        company_2 = request.POST['company_2']
        role_2 = request.POST['role_2']
        job_city_2 = request.POST['job_city_2']
        job_country_2 = request.POST['job_country_2']
        job_start_date_2 = request.POST['job_start_date_2']
        job_end_date_2 = request.POST['job_end_date_2']
        job_description_2 = request.POST['job_description_2']

        #   EDUCATION
        school_name_1 = request.POST['school_name_1']
        field_of_study_1 = request.POST['field_of_study_1']
        school_start_date_1 = request.POST['school_start_date_1']
        school_end_date_1 = request.POST['school_end_date_1']

        school_name_2 = request.POST['school_name_2']
        field_of_study_2 = request.POST['field_of_study_2']
        school_start_date_2 = request.POST['school_start_date_2']
        school_end_date_2 = request.POST['school_end_date_2']

        #   PROJECT
        project_title_1 = request.POST['project_title_1']
        project_date_1 = request.POST['project_date_1']
        project_description_1 = request.POST['project_description_1']

        project_title_2 = request.POST['project_title_2']
        project_date_2 = request.POST['project_date_2']
        project_description_2 = request.POST['project_description_2']

        #   SOCIAL ACCOUNT
        website = request.POST['website']
        twitter = request.POST['twitter']
        linkedin = request.POST['linkedin']
        
        user = request.user

        if BuildResume.objects.filter(resume_title=resume_title, user_id=user.id).exists():
            return render(request, 'dashboard/build_resume.html', {"message": "Resume Title Not Available."})
        else:
            resume = BuildResume(user_id=user_id, email=email, resume_title=resume_title, profile_photo=profile_photo, profession=profession, country=country, city=city, phone=phone, skills=skills, interests=interests, about_you=about_you, speaking_languages=speaking_languages, award_title_1=award_title_1, award_date_1=award_date_1,award_description_1=award_description_1, award_title_2=award_title_2, award_date_2=award_date_2, award_description_2=award_description_2, company_1=company_1, role_1=role_1, job_city_1=job_city_1, job_country_1=job_country_1, job_start_date_1=job_start_date_1, job_end_date_1=job_end_date_1, job_description_1=job_description_1, company_2=company_2, role_2=role_2, job_city_2=job_city_2, job_country_2=job_country_2, job_start_date_2=job_start_date_2, job_end_date_2=job_end_date_2, job_description_2=job_description_2, school_name_1=school_name_1, field_of_study_1=field_of_study_1, school_start_date_1=school_start_date_1, school_end_date_1=school_end_date_1, school_name_2=school_name_2, field_of_study_2=field_of_study_2, school_start_date_2=school_start_date_2, school_end_date_2=school_end_date_2, project_title_1=project_title_1, project_date_1=project_date_1, project_description_1=project_description_1, project_title_2=project_title_2, project_date_2=project_date_2, project_description_2=project_description_2, website=website, twitter=twitter, linkedin=linkedin)

            resume.save()

            return redirect('all_resume')

    else:
        return render(request, 'dashboard/build_resume.html')


#   ALL RESUMES
@login_required(login_url='home')
def all_resume(request):
    #   GET USER RESUME DATA
    user = request.user
    resumes = BuildResume.objects.order_by('-updated_date').filter(user_id=user.id)

    #   PAGINATOR
    paginator = Paginator(resumes, 5)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    if resumes:
        return render(request, 'dashboard/all_resumes.html', {"resumes": page_object})
    else:
        return render(request, 'dashboard/all_resumes.html')


#   READ RESUME
@login_required(login_url='home')
def read_resume(request, id):
    resume = BuildResume.objects.get(pk=id)

    skills = resume.skills.split(",")
    speaking_languages = resume.speaking_languages.split(",")
    interests = resume.interests.split(",")
    twitter = resume.twitter.split(".com/")[1]
    linkedin = resume.linkedin.split("in/")[1]
    website = resume.website.split("/")[2]

    

    data = {
        "resume": resume,
        "title": request.user.first_name+" "+request.user.last_name,
        "skills": skills,
        "speaking_languages": speaking_languages,
        "interests": interests,
        "twitter": twitter,
        "linkedin": linkedin,
        "website": website,
    }

    template_name = TemplateName.objects.get(user_id=request.user.id)

    name = template_name.defualt_template_name

    if name == "devresume":
        return render(request, 'resume_templates/preview-1.html', data)
    elif name == "orbit":
        return render(request, 'resume_templates/preview-2.html', data)
    elif name == "pillar":
        return render(request, 'resume_templates/preview-3.html', data)


#   DELETE RESUME
@login_required(login_url='home')
def delete_resume(request, id):
    
    resume = BuildResume.objects.get(pk=id)
    resume.delete()

    return redirect('all_resume')


#   SHARE RESUME LINK
# def share_resume(request, id):
#     resume = BuildResume.objects.get(pk=id)
#     data = {
#         "resume": resume,
#     }
#     return render(request, 'resume_templates/preview-1.html', data)


#   UPDATE RESUME
@login_required(login_url='home')
def update_resume(request, id):
    resume = BuildResume.objects.get(pk=id)

    if request.method == "POST":
        profile_photo = request.FILES["profile_photo"]

        profession = request.POST['profession']
        country = request.POST['country']
        city = request.POST['city']
        phone = request.POST['phone']

        skills = request.POST['skills']
        about_you = request.POST['about_you']
        interests = request.POST['interests']
        speaking_languages = request.POST['speaking_languages']

        award_title_1 = request.POST['award_title_1']
        award_date_1 = request.POST['award_date_1']
        award_description_1 = request.POST['award_description_1']

        award_title_2 = request.POST['award_title_2']
        award_date_2 = request.POST['award_date_2']
        award_description_2 = request.POST['award_description_2']

        company_1 = request.POST['company_1']
        role_1 = request.POST['role_1']
        job_city_1 = request.POST['job_city_1']
        job_country_1 = request.POST['job_country_1']
        job_start_date_1 = request.POST['job_start_date_1']
        job_end_date_1 = request.POST['job_end_date_1']
        job_description_1 = request.POST['job_description_1']
        
        company_2 = request.POST['company_2']
        role_2 = request.POST['role_2']
        job_city_2 = request.POST['job_city_2']
        job_country_2 = request.POST['job_country_2']
        job_start_date_2 = request.POST['job_start_date_2']
        job_end_date_2 = request.POST['job_end_date_2']
        job_description_2 = request.POST['job_description_2']

        school_name_1 = request.POST['school_name_1']
        field_of_study_1 = request.POST['field_of_study_1']
        school_start_date_1 = request.POST['school_start_date_1']
        school_end_date_1 = request.POST['school_end_date_1']

        school_name_2 = request.POST['school_name_2']
        field_of_study_2 = request.POST['field_of_study_2']
        school_start_date_2 = request.POST['school_start_date_2']
        school_end_date_2 = request.POST['school_end_date_2']

        project_title_1 = request.POST['project_title_1']
        project_date_1 = request.POST['project_date_1']
        project_description_1 = request.POST['project_description_1']

        project_title_2 = request.POST['project_title_2']
        project_date_2 = request.POST['project_date_2']
        project_description_2 = request.POST['project_description_2']

        website = request.POST['website']
        twitter = request.POST['twitter']
        linkedin = request.POST['linkedin']

        #   UPDATE DATA
        resume.profile_photo = profile_photo
        resume.profession = profession
        resume.country = country
        resume.city = city
        resume.phone = phone
        resume.skills = skills
        resume.about_you = about_you
        resume.interests = interests
        resume.speaking_languages = speaking_languages
        resume.award_title_1 = award_title_1
        resume.award_date_1 = award_date_1
        resume.award_description_1 = award_description_1
        resume.award_title_2 = award_title_2
        resume.award_date_2 = award_date_2
        resume.award_description_2 = award_description_2
        resume.company_1 = company_1
        resume.role_1 = role_1
        resume.job_city_1 = job_city_1
        resume.job_country_1 = job_country_1
        resume.job_start_date_1 = job_start_date_1
        resume.job_end_date_1 = job_end_date_1
        resume.job_description_1 = job_description_1
        resume.company_2 = company_2
        resume.role_2 = role_2
        resume.job_city_2 = job_city_2
        resume.job_country_2 = job_country_2
        resume.job_start_date_2 = job_start_date_2
        resume.job_end_date_2 = job_end_date_2
        resume.job_description_2 = job_description_2
        resume.school_name_1 = school_name_1
        resume.field_of_study_1 = field_of_study_1
        resume.school_start_date_1 = school_start_date_1
        resume.school_end_date_1 = school_end_date_1
        resume.school_name_2 = school_name_2
        resume.field_of_study_2 = field_of_study_2
        resume.school_start_date_2 = school_start_date_2
        resume.school_end_date_2 = school_end_date_2
        resume.project_title_1 = project_title_1
        resume.project_date_1 = project_date_1
        resume.project_description_1 = project_description_1
        resume.project_title_2 = project_title_2
        resume.project_date_2 = project_date_2
        resume.project_description_2 = project_description_2
        resume.website = website
        resume.twitter = twitter
        resume.linkedin = linkedin

        resume.save()

        return redirect('all_resume')

    else:
        return render(request, 'dashboard/update_resume.html', {"resume": resume})


#   PREVIEW
@login_required(login_url='home')
def preview(request, id):

    user = request.user
    resume = BuildResume.objects.order_by('-created_date').filter(user_id=user.id)[0]

    data = {
        "resume": resume,
    } 

    if id == 1:
        return render(request, 'resume_templates/preview-1.html', data)
    elif id == 2:
        return render(request, 'resume_templates/preview-2.html', data)
    elif id == 3:
        return render(request, 'resume_templates/preview-3.html', data)
    


#   RESUME TEMPLATES
@login_required(login_url='home')
def resume_template(request):
    
    defualt_template = TemplateName.objects.get(user_id=request.user.id)
    
    data = {
        "defualt_template": defualt_template.defualt_template_name,
    }


    return render(request, 'dashboard/resume_template.html', data)



#   DEFUALT TEMPLATE NAME SETTINGS
def template_name(request):
    if request.method == "POST":
        user_id = request.POST["user_id"]
        email = request.POST["email"]
        template_name = request.POST["defualt_template_name"]

        # TemplateName
        print(user_id, email, template_name)

        if TemplateName.objects.filter(user_id=user_id):

            template = TemplateName.objects.get(user_id=user_id)
            template.defualt_template_name = template_name

            template.save()
            return redirect('resume_template')

        else:
            new_template = TemplateName(user_id=user_id, email=email, defualt_template_name=template_name)

            new_template.save()

            return redirect('resume_template')


        


# NEED HELP
@login_required(login_url='home')
def need_help(request):
    return render(request, 'dashboard/need_help.html') 