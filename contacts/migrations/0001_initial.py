# Generated by Django 4.0.3 on 2022-03-24 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('email', models.CharField(max_length=300)),
                ('feature', models.CharField(max_length=300)),
                ('feedback', models.TextField()),
            ],
        ),
    ]
