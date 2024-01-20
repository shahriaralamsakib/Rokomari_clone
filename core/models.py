from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

CATEGORY_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
)

TYPE_CHOICES = [
    ('author', 'Author'),
    ('publisher', 'Publisher'),
    ('customer', 'Customer'),
    ('admin', 'Admin'),
    ('manager', 'Manager'),
    # Add more user types as needed
]

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **extra_fields)

class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=3, choices=CATEGORY_CHOICES, default=None, blank=True, null=True)
    phone = models.CharField(max_length=11, null=True)
    address = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES,null=True)

    objects = CustomUserManager()

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

class AuthorProfile(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    # Add fields specific to the author profile

class PublisherProfile(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    # Add fields specific to the publisher profile

class CustomerProfile(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    # Add fields specific to the customer profile

class AdminProfile(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    # Add fields specific to the admin profile

class ManagerProfile(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    # Add fields specific to the manager profile