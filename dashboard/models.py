from django.db import models
from datetime import datetime


# BUILD RESUME MODEL
class BuildResume(models.Model):
    #   POPULATE DATA
    user_id = models.IntegerField()
    email = models.CharField(max_length=300)

    resume_title = models.CharField(max_length=300)

    #   HEADING DATA
    profile_photo = models.ImageField(upload_to='profile_photo/%Y/%m/%d/')
    cover_photo = models.ImageField(upload_to='cover_photo/%Y/%m/%d/')
    profession = models.CharField(max_length=300)
    country = models.CharField(max_length=300)
    city = models.CharField(max_length=300)
    phone = models.CharField(max_length=300)

    #   WORK HISTORY or INTERNSHIP
    job_title = models.CharField(max_length=300)
    employer = models.CharField(max_length=300)
    job_city = models.CharField(max_length=300)
    job_country = models.CharField(max_length=300)
    job_start_date = models.CharField(max_length=300)
    job_end_date = models.CharField(max_length=300)
    job_description = models.TextField()

    #   EDUCATION
    school_name = models.CharField(max_length=300)
    school_location = models.CharField(max_length=300)
    degree = models.CharField(max_length=300)
    field_of_study = models.CharField(max_length=300)
    school_start_date = models.CharField(max_length=300)
    school_end_date = models.CharField(max_length=300)

    # SKILLS
    skills = models.TextField()

    #   ABOUT YOU
    about_you = models.TextField()

    # PROJECT
    project_title = models.CharField(max_length=300)
    project_date = models.CharField(max_length=300)
    project_description = models.TextField()

    # SOCIAL ACCOUNT
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