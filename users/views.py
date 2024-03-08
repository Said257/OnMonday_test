from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import generics
from .models import User
from .serializers import UserSerializer


class UserListAPI(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



