# Generated by Django 4.0.3 on 2022-03-23 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_buildresume_resume_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='TemplateName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('email', models.CharField(max_length=300)),
                ('defualt_template_name', models.CharField(max_length=300)),
            ],
        ),
    ]
