# views.py

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from core.models import AuthorProfile, PublisherProfile, CustomerProfile, AdminProfile, ManagerProfile
from core.serializers.UserTypeSerializer import AuthorProfileSerializer, PublisherProfileSerializer, CustomerProfileSerializer, AdminProfileSerializer, ManagerProfileSerializer

class AuthorProfileView(generics.RetrieveUpdateAPIView):
    queryset = AuthorProfile.objects.all()
    serializer_class = AuthorProfileSerializer

class PublisherProfileView(generics.RetrieveUpdateAPIView):
    queryset = PublisherProfile.objects.all()
    serializer_class = PublisherProfileSerializer

class CustomerProfileView(generics.RetrieveUpdateAPIView):
    queryset = CustomerProfile.objects.all()
    serializer_class = CustomerProfileSerializer

class AdminProfileView(generics.RetrieveUpdateAPIView):
    queryset = AdminProfile.objects.all()
    serializer_class = AdminProfileSerializer

class ManagerProfileView(generics.RetrieveUpdateAPIView):
    queryset = ManagerProfile.objects.all()
    serializer_class = ManagerProfileSerializer
