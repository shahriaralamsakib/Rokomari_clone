from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from core.models import User
from core.models import User, UserProfile
from core.serializers import UserSerializer, UserProfileSerializer
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken


"""
User login view.

"""

class UserLoginView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            return JsonResponse({'access_token': str(refresh.access_token)}, status=status.HTTP_200_OK)

        return JsonResponse({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)