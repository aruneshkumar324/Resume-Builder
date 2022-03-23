from django.db import models
from datetime import datetime


# BUILD RESUME MODEL
class BuildResume(models.Model):
    #   POPULATE DATA
    user_id = models.IntegerField()
    email = models.CharField(max_length=300)

    #   RESUME TITLE
    resume_title = models.CharField(max_length=300)

    #   BASIC INFORMATION
    profile_photo = models.ImageField(upload_to="profile_photo/%Y/%m/%d/")
    profession = models.CharField(max_length=300)
    country = models.CharField(max_length=300)
    city = models.CharField(max_length=300)
    phone = models.CharField(max_length=300)

    #   SKILLS
    skills = models.TextField()

    #   INTERESTS
    interests = models.TextField()

    #   ABOUT YOU
    about_you = models.TextField()

    #   SPEAKING LANGUAGES
    speaking_languages = models.TextField()

    #   AWARDS OR CERTIFICATES
    award_title_1 = models.CharField(max_length=300)
    award_date_1 = models.CharField(max_length=300)
    award_description_1 = models.TextField()

    award_title_2 = models.CharField(max_length=300)
    award_date_2 = models.CharField(max_length=300)
    award_description_2 = models.TextField()


    #   WORK HISTORY or INTERNSHIP
    company_1 = models.CharField(max_length=300)
    role_1 = models.CharField(max_length=300)
    job_city_1 = models.CharField(max_length=300)
    job_country_1 = models.CharField(max_length=300)
    job_start_date_1 = models.CharField(max_length=300)
    job_end_date_1 = models.CharField(max_length=300)
    job_description_1 = models.TextField()

    company_2 = models.CharField(max_length=300)
    role_2 = models.CharField(max_length=300)
    job_city_2 = models.CharField(max_length=300)
    job_country_2 = models.CharField(max_length=300)
    job_start_date_2 = models.CharField(max_length=300)
    job_end_date_2 = models.CharField(max_length=300)
    job_description_2 = models.TextField()

    #   EDUCATION
    school_name_1 = models.CharField(max_length=300)
    field_of_study_1 = models.CharField(max_length=300)
    school_start_date_1 = models.CharField(max_length=300)
    school_end_date_1 = models.CharField(max_length=300)

    school_name_2 = models.CharField(max_length=300)
    field_of_study_2 = models.CharField(max_length=300)
    school_start_date_2 = models.CharField(max_length=300)
    school_end_date_2 = models.CharField(max_length=300)

    #   PROJECT
    project_title_1 = models.CharField(max_length=300)
    project_date_1 = models.CharField(max_length=300)
    project_description_1 = models.TextField()

    project_title_2 = models.CharField(max_length=300)
    project_date_2 = models.CharField(max_length=300)
    project_description_2 = models.TextField()

    #   SOCIAL ACCOUNT
    website = models.CharField(max_length=300, blank=True)
    twitter = models.CharField(max_length=300, blank=True)
    linkedin = models.CharField(max_length=300, blank=True)

    # created_date = models.DateTimeField(blank=True, default=datetime.now)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)



#   DEFUALT TEMPLATE MODEL
class TemplateName(models.Model):
    user_id = models.IntegerField()
    email = models.CharField(max_length=300)
    defualt_template_name = models.CharField(max_length=300)