from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from rest_framework_nested import routers


from user.views import UserViewset, ContributorViewset
from project.views import ProjectViewset, IssueViewset, CommentViewset


user_router = routers.SimpleRouter()
user_router.register("user", UserViewset, basename="user")
user_router.register("contributor", ContributorViewset, basename="contributor")

project_router = routers.SimpleRouter()
project_router.register("project", ProjectViewset, basename="project")

target_project_router = routers.NestedSimpleRouter(
    project_router, "project", lookup="project"
)
target_project_router.register("issue", IssueViewset, basename="issue")

target_issue_router = routers.NestedSimpleRouter(
    target_project_router, "issue", lookup="issue"
)
target_issue_router.register("comment", CommentViewset, basename="comment")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path(
        "api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"
    ),
    path(
        "api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"
    ),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("api/", include(user_router.urls)),
    path("api/", include(project_router.urls)),
    path("api/", include(target_project_router.urls)),
    path("api/", include(target_issue_router.urls)),
]
