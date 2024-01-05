from django.db import models

# Create your models here.

CATEGORY_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
)


class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=3,choices=CATEGORY_CHOICES, default=None)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=11 , null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username


