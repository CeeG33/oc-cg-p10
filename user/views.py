from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from user.models import User, Contributor
from user.serializers import UserDetailSerializer, UserListSerializer, ContributorSerializer

class UserViewset(ModelViewSet):
    detail_serializer_class = UserDetailSerializer
    serializer_class = UserListSerializer
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
        
    def get_serializer_class(self):
        if self.action == "retrieve" and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()
    

class ContributorViewset(ModelViewSet):

    serializer_class = ContributorSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Contributor.objects.all()
    



