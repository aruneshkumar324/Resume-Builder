# Generated by Django 4.0.3 on 2022-03-24 17:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='created_date',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
    ]