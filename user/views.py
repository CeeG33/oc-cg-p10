from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from user.models import User, Contributor
from user.serializers import (
    UserDetailSerializer,
    UserListSerializer,
    ContributorSerializer,
)


class UserViewset(ModelViewSet):
    """
    Viewset for managing user profiles.

    Attributes:
        detail_serializer_class: The serializer class for detailed user information.
        serializer_class: The serializer class for user list information.
        permission_classes: The permission classes for the viewset.

    Methods:
        get_queryset(): Retrieves the queryset of all users.
        create(request, *args, **kwargs): Creates a new user profile.
        get_serializer_class(): Determines the appropriate serializer class based on the action.
    """
    detail_serializer_class = UserDetailSerializer
    serializer_class = UserListSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = UserDetailSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.create(serializer.validated_data)
            return Response("User created successfully !")
        else:
            return Response(serializer.errors)

    def get_serializer_class(self):
        if (
            self.action in ["retrieve", "create", "update", "partial_update"]
            and self.detail_serializer_class is not None
        ):
            return self.detail_serializer_class
        return super().get_serializer_class()


class ContributorViewset(ModelViewSet):
    """
    Viewset for managing contributors.

    Attributes:
        serializer_class: The serializer class for contributors.
        permission_classes: The permission classes for the viewset.

    Methods:
        get_queryset(): Retrieves the queryset of all contributors.
    """
    serializer_class = ContributorSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Contributor.objects.all()
