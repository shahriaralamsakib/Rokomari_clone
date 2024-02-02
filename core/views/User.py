from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from core.models import User, UserProfile
from core.serializers.User import UserSerializer
from core.serializers.UserProfile import UserProfileSerializer
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.

class UserView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def some_view(request):
    if request.user.is_superuser:
        # This is an admin user
        return HttpResponse("Welcome, Admin!")
    else:
        # This is a general customer
        return HttpResponse("Welcome, Customer!")