from django.db import models
from datetime import datetime


class Feedback(models.Model):
    user_id = models.IntegerField()
    email = models.CharField(max_length=300)
    feature = models.CharField(max_length=300)
    feedback = models.TextField() 
    created_date = models.DateField(blank=True, default=datetime.now)