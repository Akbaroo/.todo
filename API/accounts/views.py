from django.contrib.auth import get_user_model

from rest_framework.permissions import IsAdminUser
from rest_framework.generics import ListAPIView, CreateAPIView

from .serializers import UserListSerializer ,RegisterSerializer

User = get_user_model()


class UserListView(ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserListSerializer


class RegisterView(CreateAPIView):   
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

