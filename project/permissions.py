from rest_framework.permissions import BasePermission, SAFE_METHODS
from project.models import Project


class IsProjectAuthorOrContributorReadOnly(BasePermission):
    """
    Custom permission to restrict access to project-related actions.

    Attributes:
        message: The error message to display for permission denial.

    Methods:
        has_permission(request, view): Determines if the user has general permission (view the list).
        has_object_permission(request, view, obj): Determines if the user has object-specific permission.

    Usage:
        Apply this permission class to project-related views to control access.
    """
    def has_permission(self, request, view):
        self.message = "Access forbidden : You are not authenticated."
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        """
        Only contributors can read the project.
        Only the author can update or delete the project.
        """
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
    """
    Custom permission to restrict access to issue-related actions.

    Attributes:
        message: The error message to display for permission denial.

    Methods:
        has_permission(request, view): Determines if the user has general permission (view the issues of a project).
        has_object_permission(request, view, obj): Determines if the user has object-specific permission.

    Usage:
        Apply this permission class to issue-related views to control access.
    """
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
        """
        Only contributors to the project can read the issues related to the project.
        Only the author can update or delete the issue.
        """
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
    """
    Custom permission to restrict access to comment-related actions.

    Attributes:
        message: The error message to display for permission denial.

    Methods:
        has_permission(request, view): Determines if the user has general permission (view comments of a specific issue).
        has_object_permission(request, view, obj): Determines if the user has object-specific permission.

    Usage:
        Apply this permission class to comment-related views to control access.
    """
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
        """
        Only contributors to the project can read the comments related to the issue.
        Only the author can update or delete the comment.
        """
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
