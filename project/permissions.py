from rest_framework.permissions import BasePermission, SAFE_METHODS
from project.models import Project


class IsProjectAuthorOrContributorReadOnly(BasePermission):
    def has_permission(self, request, view):
        self.message = "Access forbidden : You are not authenticated."
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        self.message = "Access forbidden : You are not a contributor on the project."
        if request.method in SAFE_METHODS:
            return bool(
                request.user
                and request.user.is_authenticated
                and request.user in obj.contributors.all()
            )
        else:
            self.message = (
                "Action restricted : Only author can update or delete the project."
            )
            return bool(
                request.user
                and request.user.is_authenticated
                and request.user == obj.author
            )


class IsIssueAuthorOrContributorReadOnly(BasePermission):
    def has_permission(self, request, view):
        self.message = "Access forbidden : You are not authenticated."
        if not request.user.is_authenticated:
            return False

        if view.action == "list":
            project_id = view.kwargs.get("project_pk")
            if project_id is not None:
                project = Project.objects.filter(
                    pk=project_id, contributors=request.user
                ).first()
                return project is not None
            return False

        return True

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            self.message = (
                "Access forbidden : You are not a contributor on the project."
            )
            return bool(
                request.user
                and request.user.is_authenticated
                and request.user in obj.project.contributors.all()
            )
        else:
            self.message = (
                "Action restricted : Only author can update or delete the issue."
            )
            return bool(
                request.user
                and request.user.is_authenticated
                and request.user == obj.author
            )


class IsCommentAuthorOrContributorReadOnly(BasePermission):
    def has_permission(self, request, view):
        self.message = "Access forbidden : You are not authenticated."
        if not request.user.is_authenticated:
            return False

        if view.action == "list":
            project_id = view.kwargs.get("project_pk")
            if project_id is not None:
                project = Project.objects.filter(
                    pk=project_id, contributors=request.user
                ).first()
                return project is not None
            return False

        return True

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            self.message = (
                "Access forbidden : You are not a contributor on the project."
            )
            return bool(
                request.user
                and request.user.is_authenticated
                and request.user in obj.issue.project.contributors.all()
            )
        else:
            self.message = (
                "Action restricted : Only author can update or delete the comment."
            )
            return bool(
                request.user
                and request.user.is_authenticated
                and request.user == obj.author
            )
