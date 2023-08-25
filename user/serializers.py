from rest_framework.serializers import ModelSerializer

from user.models import User, Contributor


class UserDetailSerializer(ModelSerializer):
    
    class Meta:
        model = User
        fields = ["username", "password", "age", "can_be_contacted", "can_data_be_shared"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        instance = User.objects.create_user(**validated_data)
        return instance


class UserListSerializer(ModelSerializer):
    
    class Meta:
        model = User
        fields = ["username"]


class ContributorSerializer(ModelSerializer):

    class Meta:
        model = Contributor
        fields = ["user", "project"]