from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response

from user.models import User
from user.serializers import UserSerializer

class UserViewset(ModelViewSet):

    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()
    



