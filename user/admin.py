from django.contrib import admin

from user.models import User, Contributor

admin.site.register(User)
admin.site.register(Contributor)
