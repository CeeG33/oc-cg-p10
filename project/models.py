from django.db import models
from django.conf import settings

from uuid import uuid4


class Project(models.Model):
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="project_author",
    )

    name = models.CharField(max_length=50, unique=True)

    class Type(models.TextChoices):
        BACK_END = "BE"
        FRONT_END = "FE"
        IOS = "IOS"
        ANDROID = "AND"

    type = models.fields.CharField(max_length=4, choices=Type.choices)

    description = models.TextField(max_length=500)

    contributors = models.ManyToManyField(settings.AUTH_USER_MODEL)

    time_created = models.DateTimeField(auto_now_add=True)


class Issue(models.Model):
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="issue_author",
    )

    title = models.CharField(max_length=50, unique=True)

    project = models.ForeignKey(
        to=Project, on_delete=models.CASCADE, related_name="project"
    )

    description = models.TextField(max_length=500)

    STATUS_CHOICES = [
        ("TD", "To Do"),
        ("IP", "In Progress"),
        ("F", "Finished"),
    ]

    status = models.fields.CharField(max_length=3, choices=STATUS_CHOICES, default="TD")

    TYPE_CHOICES = [
        ("B", "Bug"),
        ("F", "Feature"),
        ("T", "Task"),
    ]

    type = models.fields.CharField(max_length=3, choices=TYPE_CHOICES)

    PRIORITY_CHOICES = [
        ("L", "Low"),
        ("M", "Medium"),
        ("H", "High"),
    ]

    priority = models.fields.CharField(max_length=3, choices=PRIORITY_CHOICES)

    accountable = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="accountable",
    )

    time_created = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="comment_author",
    )

    title = models.CharField(max_length=50, unique=True)

    issue = models.ForeignKey(
        to=Issue, on_delete=models.CASCADE, related_name="related_issue"
    )

    description = models.TextField(max_length=500)

    uuid = uuid4()

    time_created = models.DateTimeField(auto_now_add=True)
