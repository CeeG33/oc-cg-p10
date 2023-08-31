from rest_framework.viewsets import ModelViewSet

from project.models import Project, Issue, Comment
from project.serializers import (
    ProjectDetailSerializer,
    ProjectListSerializer,
    IssueListSerializer,
    IssueDetailSerializer,
    CommentListSerializer,
    CommentDetailSerializer,
)
from project.permissions import (
    IsProjectAuthorOrContributorReadOnly,
    IsIssueAuthorOrContributorReadOnly,
    IsCommentAuthorOrContributorReadOnly,
)


class MultipleSerializerMixin:
    """Mixin for using different serializers for different actions.

    Attributes:
        detail_serializer_class: The serializer class to use for detail actions.
                                 (e.g., retrieve, create, update, partial_update)

    Methods:
        get_serializer_class(): Returns the appropriate serializer class based on the action.

    Usage:
        Inherit this mixin in your ViewSets to utilize different serializers for different actions.
    """

    detail_serializer_class = None

    def get_serializer_class(self):
        if (
            self.action in ["retrieve", "create", "update", "partial_update"]
            and self.detail_serializer_class is not None
        ):
            return self.detail_serializer_class
        return super().get_serializer_class()


class ProjectViewset(MultipleSerializerMixin, ModelViewSet):
    """ViewSet for managing projects.

    Attributes:
        serializer_class: The default serializer class for listing and creating projects.
        detail_serializer_class: The serializer class for detailed project actions.
        permission_classes: The permission classes for controlling project access.

    Methods:
        get_queryset(): Returns the queryset of projects in which the current user is contributor.
    """

    serializer_class = ProjectListSerializer
    detail_serializer_class = ProjectDetailSerializer
    permission_classes = [IsProjectAuthorOrContributorReadOnly]

    def get_queryset(self):
        return Project.objects.filter(contributors=self.request.user)


class IssueViewset(MultipleSerializerMixin, ModelViewSet):
    """ViewSet for managing issues within projects.

    Attributes:
        serializer_class: The default serializer class for listing and creating issues.
        detail_serializer_class: The serializer class for detailed issue actions.
        permission_classes: The permission classes for controlling issue access.

    Methods:
        get_queryset(): Returns the queryset of issues associated with the current project.
    """

    serializer_class = IssueListSerializer
    detail_serializer_class = IssueDetailSerializer
    permission_classes = [IsIssueAuthorOrContributorReadOnly]

    def get_queryset(self):
        return Issue.objects.filter(project=self.kwargs["project_pk"])


class CommentViewset(MultipleSerializerMixin, ModelViewSet):
    """ViewSet for managing comments within issues.

    Attributes:
        serializer_class: The default serializer class for listing and creating comments.
        detail_serializer_class: The serializer class for detailed comment actions.
        permission_classes: The permission classes for controlling comment access.

    Methods:
        get_queryset(): Returns the queryset of comments associated with the current issue.
    """

    serializer_class = CommentListSerializer
    detail_serializer_class = CommentDetailSerializer
    permission_classes = [IsCommentAuthorOrContributorReadOnly]

    def get_queryset(self):
        return Comment.objects.filter(issue=self.kwargs["issue_pk"])
