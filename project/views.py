from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from project.models import Project, Issue, Comment
from project.serializers import (ProjectDetailSerializer,
                                 ProjectListSerializer,
                                 IssueListSerializer,
                                 IssueDetailSerializer,
                                 CommentListSerializer,
                                 CommentDetailSerializer)
from project.permissions import (
    IsProjectAuthorOrContributorReadOnly,
    IsIssueAuthorOrContributorReadOnly,
    IsCommentAuthorOrContributorReadOnly,
)


class MultipleSerializerMixin:
    detail_serializer_class = None

    def get_serializer_class(self):
        if self.action == "retrieve" and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()


class ProjectViewset(MultipleSerializerMixin, ModelViewSet):
    serializer_class = ProjectListSerializer
    detail_serializer_class = ProjectDetailSerializer
    permission_classes = [IsProjectAuthorOrContributorReadOnly]

    def get_queryset(self):
        return Project.objects.all()


class IssueViewset(MultipleSerializerMixin, ModelViewSet):
    serializer_class = IssueListSerializer
    detail_serializer_class = IssueDetailSerializer
    permission_classes = [IsIssueAuthorOrContributorReadOnly]

    def get_queryset(self):
        return Issue.objects.all()


class CommentViewset(MultipleSerializerMixin, ModelViewSet):
    serializer_class = CommentListSerializer
    detail_serializer_class = CommentDetailSerializer
    permission_classes = [IsCommentAuthorOrContributorReadOnly]

    def get_queryset(self):
        return Comment.objects.all()
