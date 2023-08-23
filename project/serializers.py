from rest_framework.serializers import ModelSerializer, SerializerMethodField

from user.serializers import UserListSerializer
from project.models import Project, Issue, Comment


class ProjectSerializer(ModelSerializer):
    # contributors = SerializerMethodField()
    # author = SerializerMethodField()

    class Meta:
        model = Project
        fields = ["name", "author", "contributors", "type", "description", "time_created"]

    def get_author(self, instance):
        queryset = instance.author
        serializer = UserListSerializer(queryset)
        return serializer.data

    def get_contributors(self, instance):
        queryset = instance.contributors.all()
        serializer = UserListSerializer(queryset, many=True)
        return serializer.data


class IssueSerializer(ModelSerializer):

    class Meta:
        model = Issue
        fields = ["author",
                  "project",
                  "title",
                  "type",
                  "status",
                  "priority",
                  "description",
                  "accountable",
                  "time_created"]


class CommentSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = ["author",
                  "title",
                  "issue",
                  "description",
                  "uuid",
                  "time_created"]
