# Generated by Django 4.0.3 on 2022-03-21 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_buildresume_cover_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='buildresume',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='buildresume',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
