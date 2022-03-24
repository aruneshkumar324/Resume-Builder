from django.db import models


class Feedback(models.Model):
    user_id = models.IntegerField()
    email = models.CharField(max_length=300)
    feature = models.CharField(max_length=300)
    feedback = models.TextField() 