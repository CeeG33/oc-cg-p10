from django.db import models
from django.conf import settings


class Project(models.Model):
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="author")
    
    name = models.CharField(max_length=50, unique=True)

    class Type(models.TextChoices):
        BACK_END = "BE"
        FRONT_END = "FE"
        IOS = "IOS"
        ANDROID = "AND"

    type = models.fields.CharField(max_length=4, choices=Type.choices)

    description = models.TextField(max_length=500)

    contributors = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="contributors")
    
    # issues = models.ForeignKey(
    #     to="Issue", # A MODIFIER
    #     on_delete=models.CASCADE,
    #     related_name="issue")
    
    time_created = models.DateTimeField(auto_now_add=True)
