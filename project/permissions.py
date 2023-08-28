from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsProjectAuthorOrContributorReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return bool(
                request.user
                and request.user.is_authenticated
                and obj.contributors.filter(pk=request.user.pk).exists()
            )
        else:
            return bool(
                request.user
                and request.user.is_authenticated
                and request.user == obj.author
            )


class IsIssueAuthorOrContributorReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return bool(
                request.user
                and request.user.is_authenticated
                and request.user in obj.project.contributors.all()
                # and obj.project.contributors.filter(pk=request.user.pk).exists()
            )
        else:
            return bool(
                request.user
                and request.user.is_authenticated
                and request.user == obj.author
                and request.user in obj.project.contributors.all()
            )


class IsCommentAuthorOrContributorReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return bool(
                request.user
                and request.user.is_authenticated
                and obj.issue.project.contributors.filter(pk=request.user.pk).exists()
            )
        else:
            return bool(
                request.user
                and request.user.is_authenticated
                and request.user == obj.author
            )
