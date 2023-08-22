from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings

from project.models import Project


class User(AbstractUser):
    username = models.CharField(max_length=15, unique=True)

    age = models.PositiveIntegerField(
        validators=[MinValueValidator(16), MaxValueValidator(85)]
    )

    can_be_contacted = models.BooleanField()

    can_data_be_shared = models.BooleanField()


class Contributor(models.Model):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="user")
    
    project = models.ForeignKey(
        to=Project,
        on_delete=models.CASCADE,
        related_name="project")
    
    class Meta:
        unique_together = (
            "user",
            "project",
        )