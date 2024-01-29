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

class UserLogoutView(APIView):
    def post(self, request, *args, **kwargs):
        logout(request)
        return JsonResponse({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)