# Generated by Django 4.0.3 on 2022-03-21 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_remove_buildresume_cover_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='buildresume',
            name='cover_photo',
            field=models.ImageField(default=0, upload_to='cover_photo/%Y/%m/%d/'),
            preserve_default=False,
        ),
    ]
