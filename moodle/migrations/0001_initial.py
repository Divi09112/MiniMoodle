# Generated by Django 2.0.2 on 2018-02-25 10:33

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('name', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('professor', models.CharField(max_length=100, verbose_name=django.contrib.auth.models.User)),
                ('student', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
