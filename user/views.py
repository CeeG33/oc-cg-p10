from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from user.models import User, Contributor
from user.permissions import UserPrivacy
from user.serializers import (
    UserDetailSerializer,
    UserListSerializer,
    ContributorSerializer,
)


class UserViewset(ModelViewSet):
    """Viewset for managing user profiles.

    Attributes:
        detail_serializer_class: The serializer class for detailed user information.
        serializer_class: The serializer class for user list information.
        permission_classes: The permission classes for the viewset.
    """

    detail_serializer_class = UserDetailSerializer
    serializer_class = UserListSerializer
    permission_classes = [UserPrivacy]

    def get_queryset(self):
        """Retrieves the queryset of all users."""
        return User.objects.all()

    def create(self, request, *args, **kwargs):
        """Creates a new user profile."""
        serializer = UserDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.create(serializer.validated_data)
            return Response("User created successfully !")
        else:
            return Response(serializer.errors)

    def get_serializer_class(self):
        """Determines the appropriate serializer class based on the action."""
        if (
            self.action in ["retrieve", "create", "update", "partial_update"]
            and self.detail_serializer_class is not None
        ):
            return self.detail_serializer_class
        return super().get_serializer_class()


class ContributorViewset(ModelViewSet):
    """Viewset for managing contributors.

    Attributes:
        serializer_class: The serializer class for contributors.
        permission_classes: The permission classes for the viewset.
    """

    serializer_class = ContributorSerializer
    permission_classes = [UserPrivacy]

    def get_queryset(self):
        """get_queryset(): Retrieves the queryset of all contributors."""
        return Contributor.objects.all()
