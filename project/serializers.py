from rest_framework.serializers import ModelSerializer, SerializerMethodField, ValidationError

from user.serializers import UserListSerializer
from user.models import User
from project.models import Project, Issue, Comment


class ProjectListSerializer(ModelSerializer):
    contributors = SerializerMethodField()
    author = SerializerMethodField()

    class Meta:
        model = Project
        fields = [
            "id",
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
    author = SerializerMethodField()
    contributors_name = SerializerMethodField()

    class Meta:
        model = Project
        fields = [
            "id",
            "name",
            "author",
            "contributors",
            "contributors_name",
            "type",
            "description",
            "time_created",
        ]
    read_only_fields = ["author", "contributors_name"]

    def create(self, validated_data):
        user = self.context["request"].user
        validated_data["author"] = user

        contributors_data = validated_data.pop("contributors", [])

        project = Project.objects.create(**validated_data)
        project.contributors.add(user)

        for contributor in contributors_data:
            project.contributors.add(contributor)

        return project
    
    def update(self, instance, validated_data):
        instance.contributors.clear()

        contributors_data = validated_data.pop("contributors", [])

        instance.contributors.add(instance.author)
        
        instance = super().update(instance, validated_data)

        for contributor in contributors_data:
            instance.contributors.add(contributor)

        return instance

    def get_contributors_name(self, instance):
        usernames = [contributor.username for contributor in instance.contributors.all()]
        return usernames
    
    def get_author(self, instance):
        return instance.author.username


class IssueListSerializer(ModelSerializer):
    author = SerializerMethodField()
    accountable = SerializerMethodField()

    class Meta:
        model = Issue
        fields = [
            "id",
            "author",
            "title",
            "accountable",
            "time_created",
        ]
    
    def get_accountable(self, instance):
        return instance.accountable.username
    
    def get_author(self, instance):
        return instance.author.username


class IssueDetailSerializer(ModelSerializer):
    project = SerializerMethodField()
    author = SerializerMethodField()
    accountable_name = SerializerMethodField()

    class Meta:
        model = Issue
        fields = [
            "id",
            "author",
            "project",
            "title",
            "type",
            "status",
            "priority",
            "description",
            "accountable",
            "accountable_name",
            "time_created",
        ]
        read_only_fields = ["author", "accountable_name"]

    def create(self, validated_data):
        user = self.context["request"].user
        validated_data["author"] = user

        project_id = self.context["view"].kwargs.get("project_pk")
        project = Project.objects.get(pk=project_id)
        validated_data["project"] = project

        accountable = validated_data.get("accountable")
        if accountable and accountable not in project.contributors.all():
            raise ValidationError("Error : You can only select contributors to this project.")

        issue = Issue.objects.create(**validated_data)

        return issue
    
    def update(self, instance, validated_data):
        accountable = validated_data.get("accountable")
        if accountable and accountable not in instance.project.contributors.all():
            raise ValidationError("Error : You can only select contributors to this project.")

        instance = super().update(instance, validated_data)

        return instance
    
    def get_project(self, instance):
        return self.instance.project.name
    
    def get_author(self, instance):
        return instance.author.username
    
    def get_accountable_name(self, instance):
        return instance.accountable_user.username
        

class CommentListSerializer(ModelSerializer):
    author = SerializerMethodField()
    issue = SerializerMethodField()
    
    class Meta:
        model = Comment
        fields = ["id", "author", "title", "issue", "uuid", "time_created"]
        read_only_fields = ["author"]

    def get_author(self, instance):
        return instance.author.username
    
    def get_issue(self, instance):
        return instance.issue.title


class CommentDetailSerializer(ModelSerializer):
    author = SerializerMethodField()
    issue = SerializerMethodField()
    
    class Meta:
        model = Comment
        fields = ["id", "author", "title", "issue", "description", "uuid", "time_created"]
        read_only_fields = ["author"]

    def create(self, validated_data):
        user = self.context["request"].user
        validated_data["author"] = user

        issue_id = self.context["view"].kwargs.get("issue_pk")
        issue = Issue.objects.get(pk=issue_id)
        validated_data["issue"] = issue

        comment = Comment.objects.create(**validated_data)

        return comment
    
    def get_author(self, instance):
        return instance.author.username
    
    def get_issue(self, instance):
        return instance.issue.title
    
