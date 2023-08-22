from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from user.views import UserViewset
from project.views import ProjectViewset


router = routers.SimpleRouter()
router.register("user", UserViewset, basename="user")
router.register("project", ProjectViewset, basename="project")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api/", include(router.urls)),
]
