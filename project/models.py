from django.db import models
from django.conf import settings

from uuid import uuid4


class Project(models.Model):
    """Represents a project managed within the SoftDesk Support system.

    Attributes:
        author (ForeignKey): The user who created the project.
        name (CharField): The name of the project (unique).
        type (CharField): The type of the project (choices: 'BE', 'FE', 'IOS', 'AND').
        description (TextField): A description of the project.
        contributors (ManyToManyField): Users who contribute to the project.
        time_created (DateTimeField): The date and time the project was created.
    """
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
    """Represents an issue or task within a project.

    Attributes:
        author (ForeignKey): The user who created the issue.
        title (CharField): The title of the issue (unique within the project).
        project (ForeignKey): The project to which the issue belongs.
        description (TextField): A description of the issue.
        status (CharField): The status of the issue (choices: 'TD', 'IP', 'F').
        type (CharField): The type of the issue (choices: 'B' for Bug, 'F' for Feature, 'T' for Task).
        priority (CharField): The priority of the issue (choices: 'L' for Low, 'M' for Medium, 'H' for High).
        accountable (ForeignKey): The user responsible for the issue.
        time_created (DateTimeField): The date and time the issue was created.
    """
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

    status = models.fields.CharField(
        max_length=3, choices=STATUS_CHOICES, default="TD"
    )

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
    """Represents a comment associated with an issue.

    Attributes:
        author (ForeignKey): The user who created the comment.
        title (CharField): The title of the comment (unique within the issue).
        issue (ForeignKey): The issue to which the comment is related.
        description (TextField): The content of the comment.
        uuid (UUIDField): A universally unique identifier for the comment.
        time_created (DateTimeField): The date and time the comment was created.
    """
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
