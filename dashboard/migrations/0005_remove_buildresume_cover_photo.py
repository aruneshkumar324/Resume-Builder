# Generated by Django 4.0.3 on 2022-03-21 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_buildresume_about_you'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buildresume',
            name='cover_photo',
        ),
    ]