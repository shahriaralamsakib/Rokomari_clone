from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from core.models import User
from inventory.models import Book

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)