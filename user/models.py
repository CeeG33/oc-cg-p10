from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class User(AbstractUser):
    username = models.CharField(max_length=15, unique=True)

    age = models.PositiveIntegerField(
        validators=[MinValueValidator(16), MaxValueValidator(85)]
    )

    can_be_contacted = models.BooleanField()

    can_data_be_shared = models.BooleanField()
