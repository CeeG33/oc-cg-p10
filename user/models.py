from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from project.models import Project


class User(AbstractUser):
    """Represents a user of the API.

    Attributes:
        username (str): The unique username of the user.
        age (int): The age of the user.
        can_be_contacted (bool): Whether the user can be contacted.
        can_data_be_shared (bool): Whether the user allows his personal informations to be shared.
    """

    username = models.CharField(max_length=15, unique=True)

    age = models.PositiveIntegerField(
        validators=[MinValueValidator(16), MaxValueValidator(85)]
    )

    can_be_contacted = models.BooleanField()

    can_data_be_shared = models.BooleanField()

    def __str__(self):
        """Returns the string representation of the user."""
        return self.username


class Contributor(models.Model):
    """Represents a user who can interact with specific projects.

    Attributes:
        user (User): The user identified as contributor.
        project (Project): The project to which the contributor is associated.

    Meta:
        unique_together (tuple): Ensures unique user-project pairs.
    """

    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="user",
    )

    project = models.ForeignKey(
        to=Project, on_delete=models.CASCADE, related_name="contributes_to"
    )

    class Meta:
        unique_together = (
            "user",
            "project",
        )

    @receiver(post_save, sender=Project)
    def create_contributors(sender, instance, created, **kwargs):
        """Creates contributors when a project is created."""
        if created:
            for user in instance.contributors.all():
                Contributor.objects.create(user=user, project=instance)

    @receiver(post_delete, sender=Project)
    def auto_delete_contributors(sender, instance, **kwargs):
        """Deletes contributors when a project is deleted."""
        Contributor.objects.filter(project=instance).delete()
