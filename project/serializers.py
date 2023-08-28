from rest_framework.serializers import ModelSerializer, SerializerMethodField, ValidationError

from user.serializers import UserListSerializer
from project.models import Project, Issue, Comment


class ProjectListSerializer(ModelSerializer):
    contributors = SerializerMethodField()
    author = SerializerMethodField()

    class Meta:
        model = Project
        fields = [
            "name",
            "author",
            "contributors",
            "time_created",
        ]
        read_only_fields = ["author"]

    def get_contributors(self, instance):
        contributors = instance.contributors.all()
        usernames = [contributor.username for contributor in contributors]
        return usernames
    
    def get_author(self, instance):
        return instance.author.username


class ProjectDetailSerializer(ModelSerializer):
    contributors = SerializerMethodField()
    author = SerializerMethodField()

    class Meta:
        model = Project
        fields = [
            "name",
            "author",
            "contributors",
            "type",
            "description",
            "time_created",
        ]
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
    
    def get_author(self, instance):
        return instance.author.username


class IssueListSerializer(ModelSerializer):
    project = SerializerMethodField()
    author = SerializerMethodField()
    accountable = SerializerMethodField()

    class Meta:
        model = Issue
        fields = [
            "author",
            "project",
            "title",
            "accountable",
            "time_created",
        ]
        read_only_fields = ["author"]
    
    def get_project(self, instance):
        return instance.project.name
    
    def get_accountable(self, instance):
        return instance.accountable.username
    
    def get_author(self, instance):
        return instance.author.username


class IssueDetailSerializer(ModelSerializer):
    project = SerializerMethodField()
    author = SerializerMethodField()
    accountable = SerializerMethodField()

    class Meta:
        model = Issue
        fields = [
            "author",
            "project",
            "title",
            "type",
            "status",
            "priority",
            "description",
            "accountable",
            "time_created",
        ]
        read_only_fields = ["author"]

    def create(self, validated_data):
        user = self.context["request"].user
        validated_data["author"] = user

        issue = Issue.objects.create(**validated_data)

        return issue
    
    def get_project(self, instance):
        return self.instance.project.name

    def validate_project(self, value):
        user = self.context.get("request").user
        if not value.contributors.filter(pk=user.pk).exists():
            raise ValidationError("You are not a contributor to this project.")
        return value
    
    def get_accountable(self, instance):
        return instance.accountable.username
    
    def get_author(self, instance):
        return instance.author.username
        

class CommentListSerializer(ModelSerializer):
    author = SerializerMethodField()
    issue = SerializerMethodField()
    
    class Meta:
        model = Comment
        fields = ["author", "title", "issue", "uuid", "time_created"]
        read_only_fields = ["author"]

    def get_author(self, instance):
        return instance.author.username
    
    def get_issue(self, instance):
        return instance.issue.title


class CommentDetailSerializer(ModelSerializer):
    author = SerializerMethodField()
    
    class Meta:
        model = Comment
        fields = ["author", "title", "issue", "description", "uuid", "time_created"]
        read_only_fields = ["author"]

    def create(self, validated_data):
        user = self.context["request"].user
        validated_data["author"] = user

        comment = Comment.objects.create(**validated_data)

        return comment

    def validate_issue(self, value):
        user = self.context.get("request").user
        if not value.project.contributors.filter(pk=user.pk).exists():
            raise ValidationError("You are not a contributor to this project.")
        return value
    
    def get_author(self, instance):
        return instance.author.username
