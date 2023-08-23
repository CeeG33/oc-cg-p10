# Generated by Django 4.2.4 on 2023-08-23 16:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("project", "0002_remove_project_contributors_project_contributors"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="project_author",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.CreateModel(
            name="Issue",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=50, unique=True)),
                ("description", models.TextField(max_length=500)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("TD", "To Do"),
                            ("IP", "In Progress"),
                            ("F", "Finished"),
                        ],
                        default="TD",
                        max_length=3,
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[("B", "Bug"), ("F", "Feature"), ("T", "Task")],
                        max_length=3,
                    ),
                ),
                (
                    "priority",
                    models.CharField(
                        choices=[("L", "Low"), ("M", "Medium"), ("H", "High")],
                        max_length=3,
                    ),
                ),
                ("time_created", models.DateTimeField(auto_now_add=True)),
                (
                    "accountable",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="accountable",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="issue_author",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="project",
                        to="project.project",
                    ),
                ),
            ],
        ),
    ]
