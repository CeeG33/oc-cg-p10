from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from project.models import Project, Issue, Comment
from project.serializers import ProjectSerializer, IssueSerializer, CommentSerializer
from project.permissions import (IsProjectAuthorOrContributorReadOnly,
                                 IsIssueAuthorOrContributorReadOnly,
                                 IsCommentAuthorOrContributorReadOnly)


class ProjectViewset(ModelViewSet):

    serializer_class = ProjectSerializer
    permission_classes = [IsProjectAuthorOrContributorReadOnly]

    def get_queryset(self):
        return Project.objects.all()


class IssueViewset(ModelViewSet):

    serializer_class = IssueSerializer
    permission_classes = [IsIssueAuthorOrContributorReadOnly]

    def get_queryset(self):
        return Issue.objects.all()
    

class CommentViewset(ModelViewSet):

    serializer_class = CommentSerializer
    permission_classes = [IsCommentAuthorOrContributorReadOnly]

    def get_queryset(self):
        return Comment.objects.all()
