# Generated by Django 4.2.4 on 2023-08-23 11:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("project", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="project",
            name="contributors",
        ),
        migrations.AddField(
            model_name="project",
            name="contributors",
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
