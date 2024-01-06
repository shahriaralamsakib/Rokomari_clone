from django.db import models
from django.contrib.auth.models import AbstractUser

CATEGORY_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
)

class User(AbstractUser):  # Inherit from AbstractUser directly
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=3, choices=CATEGORY_CHOICES, default=None, blank=True, null=True)
    phone = models.CharField(max_length=11, null=True)
    address = models.TextField(blank=True, null=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
