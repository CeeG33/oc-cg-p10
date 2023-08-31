from rest_framework.permissions import BasePermission, SAFE_METHODS


class UserPrivacy(BasePermission):
    """Custom permission to restrict access to user-related actions.

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
        """We can access a user's detailed informations only if he allowed his
        data to be shared.

        The user is the only one to update his informations or delete
        his account.
        """
        self.message = "Access forbidden : You are not allowed to view these informations."
        if request.method in SAFE_METHODS:
            return bool(
                request.user
                and request.user.is_authenticated
                and obj.can_data_be_shared == True
                or request.user == obj
            )
        else:
            self.message = "Action restricted : Only the user can update his informations or delete his account."
            return bool(
                request.user
                and request.user.is_authenticated
                and request.user == obj
            )
