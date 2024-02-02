from rest_framework import serializers
from core.models import User, UserProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password','gender','phone','address']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user_profile_data = validated_data.pop('user_profile')
        user = User.objects.create(**validated_data)
        UserProfile.objects.create(user=user, **user_profile_data)
        return user