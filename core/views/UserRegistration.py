from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from core.models import User, UserProfile
from core.serializers.UserSerializer import UserSerializer
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
"""
User Registration view.

"""

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user_profile_data = self.request.data.get('user_profile', {})
        user = serializer.save()
        UserProfile.objects.create(user=user, **user_profile_data)
        login(self.request, user)