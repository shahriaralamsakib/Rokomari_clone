from rest_framework import serializers
from core.models import UserProfile

"""
This serializer is used for UserPofile model.

"""

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'bio', 'profile_picture']