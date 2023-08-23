from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response

from user.models import User, Contributor
from user.serializers import UserDetailSerializer, ContributorSerializer

class UserViewset(ModelViewSet):

    serializer_class = UserDetailSerializer

    def get_queryset(self):
        return User.objects.all()
    

class ContributorViewset(ModelViewSet):

    serializer_class = ContributorSerializer

    def get_queryset(self):
        return Contributor.objects.all()
    



