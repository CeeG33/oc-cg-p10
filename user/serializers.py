from rest_framework.serializers import ModelSerializer

from user.models import User, Contributor


class UserDetailSerializer(ModelSerializer):
    """
    Serializer for detailed user representation, including creation.

    Attributes:
        Meta:
            model (User): The User model to serialize.
            fields (list): List of fields to include in the serialized representation.
            extra_kwargs (dict): Extra keyword arguments for fields.
    
    Methods:
        create(validated_data): Create a new user instance based on validated data.
    """
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "password",
            "age",
            "can_be_contacted",
            "can_data_be_shared",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        """
        Create and return a new User instance.

        Args:
            validated_data (dict): Validated data for creating a new user.

        Returns:
            User: The created User instance.
        """
        instance = User.objects.create_user(**validated_data)
        return instance


class UserListSerializer(ModelSerializer):
    """
    Serializer for showing basic users information as a list.

    Attributes:
        Meta:
            model (User): The User model to serialize.
            fields (list): List of fields to include in the serialized representation.
    """
    class Meta:
        model = User
        fields = ["id", "username"]


class ContributorSerializer(ModelSerializer):
    """
    Serializer for representing a contributor's relationship with a project.

    Attributes:
        Meta:
            model (Contributor): The Contributor model to serialize.
            fields (list): List of fields to include in the serialized representation.
    """
    class Meta:
        model = Contributor
        fields = ["user", "project"]
