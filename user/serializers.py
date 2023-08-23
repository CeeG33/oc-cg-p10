from rest_framework.serializers import ModelSerializer

from user.models import User, Contributor


class UserDetailSerializer(ModelSerializer):
    
    class Meta:
        model = User
        fields = ["username", "age", "can_be_contacted", "can_data_be_shared"]


class UserListSerializer(ModelSerializer):
    
    class Meta:
        model = User
        fields = ["username"]


class ContributorSerializer(ModelSerializer):

    class Meta:
        model = Contributor
        fields = ["user", "project"]