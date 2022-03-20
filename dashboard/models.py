from django.db import models


class Profile(models.Model):

    select_gender = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    select_language = [
        ('English', 'English'),
        ('Chinese', 'Chinese'),
        ('Spanish', 'Spanish'),
        ('Arabic', 'Arabic'),
        ('Portuguese', 'Portuguese'),
        ('Bengali', 'Bengali'),
        ('Russian', 'Russian'),
        ('Japanese', 'Japanese'),
        ('Lahnda', 'Lahnda'),
    ]

    user_id = models.IntegerField(blank=True)
    username = models.CharField(max_length=250, blank=True)
    email = models.CharField(max_length=250, blank=True)
    phone = models.CharField(max_length=250)
    whatsapp_number = models.CharField(max_length=250, blank=True)
    country = models.CharField(max_length=300)
    state = models.CharField(max_length=300)
    city = models.CharField(max_length=300)
    date_of_birth = models.CharField(max_length=100)
    gender = models.CharField(choices=select_gender, max_length=100)
    speaking_language = models.CharField(choices=select_language, max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    facebook_link = models.CharField(max_length=500, blank=True)
    twitter_link = models.CharField(max_length=500, blank=True)
    linkedin_link = models.CharField(max_length=500, blank=True)
    github_link = models.CharField(max_length=500, blank=True)
    instagram_link = models.CharField(max_length=500)
    stackoverflow_link = models.CharField(max_length=500, blank=True)
    reddit_link = models.CharField(max_length=500, blank=True)