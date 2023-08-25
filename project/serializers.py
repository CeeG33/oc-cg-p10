from rest_framework.serializers import ModelSerializer, SerializerMethodField

from user.serializers import UserListSerializer
from project.models import Project, Issue, Comment


class MultipleSerializerMixin:
    author = SerializerMethodField()

    def get_author(self, instance):
        return instance.author.username
    
    def get_title(self, instance):
        return instance.title


class ProjectSerializer(MultipleSerializerMixin, ModelSerializer):
    contributors = SerializerMethodField()

    class Meta:
        model = Project
        fields = ["name", "author", "contributors", "type", "description", "time_created"]
        read_only_fields = ["author"]

    def create(self, validated_data):
        user = self.context["request"].user
        validated_data["author"] = user

        contributors_data = validated_data.pop("contributors", [])

        project = Project.objects.create(**validated_data)
        project.contributors.add(user)

        for contributor in contributors_data:
            project.contributors.add(contributor)

        return project

    def get_contributors(self, instance):
        contributors = instance.contributors.all()
        usernames = [contributor.username for contributor in contributors]
        return usernames
    
    

class IssueSerializer(MultipleSerializerMixin, ModelSerializer):

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


class CommentSerializer(MultipleSerializerMixin, ModelSerializer):

    class Meta:
        model = Comment
        fields = ["author",
                  "title",
                  "issue",
                  "description",
                  "uuid",
                  "time_created"]
