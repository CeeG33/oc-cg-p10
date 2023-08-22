from rest_framework.serializers import ModelSerializer

from user.models import User


class UserSerializer(ModelSerializer):
    
    class Meta:
        model = User
        fields = ["username", "age", "can_be_contacted", "can_data_be_shared"]

