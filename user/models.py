from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

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
        related_name="contributes_to")
    
    class Meta:
        unique_together = (
            "user",
            "project",
        )

    @receiver(post_save, sender=Project)
    def create_contributors(sender, instance, created, **kwargs):
        if created:
            for user in instance.contributors.all():
                Contributor.objects.create(user=user, project=instance)

    @receiver(post_delete, sender=Project)
    def auto_delete_contributors(sender, instance, **kwargs):
        Contributor.objects.filter(project=instance).delete()