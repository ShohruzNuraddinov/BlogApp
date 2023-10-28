from django.shortcuts import render
from rest_framework import viewsets

from .models import UserModel as User
from .serailizers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

