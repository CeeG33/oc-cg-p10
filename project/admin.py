from django.contrib import admin
from django.contrib.auth.models import Group

from project.models import Project, Issue, Comment

admin.site.register(Project)
admin.site.register(Issue)
admin.site.register(Comment)

admin.site.unregister(Group)
