from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from user.models import User, Contributor
from user.serializers import UserDetailSerializer, ContributorSerializer

class UserViewset(ModelViewSet):

    serializer_class = UserDetailSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return User.objects.all()
    
    def create(self, request, *args, **kwargs):
        serializer = UserDetailSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.create(serializer.validated_data)
            return Response("User created successfully !")
        else:
            return Response(serializer.errors)
    

class ContributorViewset(ModelViewSet):

    serializer_class = ContributorSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Contributor.objects.all()
    



