# serializers.py

from rest_framework import serializers
from .models import AuthorProfile, PublisherProfile, CustomerProfile, AdminProfile, ManagerProfile

class AuthorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorProfile
        fields = '__all__'

class PublisherProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublisherProfile
        fields = '__all__'

class CustomerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerProfile
        fields = '__all__'

class AdminProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminProfile
        fields = '__all__'

class ManagerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManagerProfile
        fields = '__all__'
