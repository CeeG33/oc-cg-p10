from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    ValidationError,
)

from project.models import Project, Issue, Comment


class ProjectListSerializer(ModelSerializer):
    """Serializer for showing multiple projects informations as a list."""
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
        """Retrieves usernames of contributors for a project."""
        contributors = instance.contributors.all()
        usernames = [contributor.username for contributor in contributors]
        return usernames

    def get_author(self, instance):
        """Retrieves the username of the project's author."""
        return instance.author.username


class ProjectDetailSerializer(ModelSerializer):
    """Serializer for showing detailed project information."""
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
        """Creates a new project with contributors.
        The user is automatically added as author and contributor on the
        project.
        """
        user = self.context["request"].user
        validated_data["author"] = user

        contributors_data = validated_data.pop("contributors", [])

        project = Project.objects.create(**validated_data)
        project.contributors.add(user)

        for contributor in contributors_data:
            project.contributors.add(contributor)

        return project

    def update(self, instance, validated_data):
        """Updates a project's information and contributors.
        The contributors field update will superseed the previous
        contributors.
        """
        if validated_data.get("contributors"):
            instance.contributors.clear()

            contributors_data = validated_data.pop("contributors", [])

            instance.contributors.add(instance.author)

            instance = super().update(instance, validated_data)

            for contributor in contributors_data:
                instance.contributors.add(contributor)

        instance = super().update(instance, validated_data)

        return instance

    def get_contributors_name(self, instance):
        """Retrieves usernames of contributors for a project."""
        usernames = [
            contributor.username for contributor in instance.contributors.all()
        ]
        return usernames

    def get_author(self, instance):
        """Retrieves the username of the project's author."""
        return instance.author.username


class IssueListSerializer(ModelSerializer):
    """Serializer for showing multiple issues informations as a list."""
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
        """Retrieves the username of the accountable user."""
        return instance.accountable.username

    def get_author(self, instance):
        """Retrieves the username of the issue's author."""
        return instance.author.username


class IssueDetailSerializer(ModelSerializer):
    """Serializer for displaying detailed issue information."""
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
        """Creates a new issue instance.
        
        The user is automatically added as author of the issue.

        The project in which the issue is created is automatically added
        as related project. Can specify a user as accountable only if he
        is contributor to the project.
        """
        user = self.context["request"].user
        validated_data["author"] = user

        project_id = self.context["view"].kwargs.get("project_pk")
        project = Project.objects.get(pk=project_id)
        validated_data["project"] = project

        accountable = validated_data.get("accountable")
        if accountable and accountable not in project.contributors.all():
            raise ValidationError(
                "Error : You can only select contributors to this project."
            )

        issue = Issue.objects.create(**validated_data)

        return issue

    def update(self, instance, validated_data):
        """Updates an existing issue instance.
        
        Can specify a user as accountable only if he is contributor to the
        project.
        """
        accountable = validated_data.get("accountable")
        if (
            accountable
            and accountable not in instance.project.contributors.all()
        ):
            raise ValidationError(
                "Error : You can only select contributors to this project."
            )

        instance = super().update(instance, validated_data)

        return instance

    def get_project(self, instance):
        """Retrieves the name of the associated project."""
        return self.instance.project.name

    def get_author(self, instance):
        """Retrieves the username of the issue's author."""
        return instance.author.username

    def get_accountable_name(self, instance):
        """Retrieves the username of the accountable user."""
        return instance.accountable.username


class CommentListSerializer(ModelSerializer):
    """Serializer for displaying multiple comments informations as a list."""
    author = SerializerMethodField()
    issue = SerializerMethodField()

    class Meta:
        model = Comment
        fields = ["id", "author", "title", "issue", "uuid", "time_created"]
        read_only_fields = ["author"]

    def get_author(self, instance):
        """Retrieves the username of the comment's author."""
        return instance.author.username

    def get_issue(self, instance):
        """Retrieves the title of the associated issue."""
        return instance.issue.title


class CommentDetailSerializer(ModelSerializer):
    """Serializer for displaying a comment's detailed information."""
    author = SerializerMethodField()
    issue = SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            "id",
            "author",
            "title",
            "issue",
            "description",
            "uuid",
            "time_created",
        ]
        read_only_fields = ["author", "issue"]

    def create(self, validated_data):
        """Creates a new comment instance.
        
        The user is automatically added as author of the comment.

        The issue in which the comment is created is automatically added
        as related issue.
        """
        user = self.context["request"].user
        validated_data["author"] = user

        issue_id = self.context["view"].kwargs.get("issue_pk")
        issue = Issue.objects.get(pk=issue_id)
        validated_data["issue"] = issue

        comment = Comment.objects.create(**validated_data)

        return comment

    def get_author(self, instance):
        """Retrieves the username of the comment's author."""
        return instance.author.username

    def get_issue(self, instance):
        """Retrieves the title of the associated issue."""
        return instance.issue.title
