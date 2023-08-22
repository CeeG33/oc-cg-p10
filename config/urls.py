from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from user.views import UserViewset


router = routers.SimpleRouter()
router.register("user", UserViewset, basename="user")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api/", include(router.urls)),
]
