from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)  # For simplicity, use a plain text password (not recommended for production)

    def __str__(self):
        return self.username
