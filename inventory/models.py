from django.db import models
from core.models import User
from versatileimagefield.fields import VersatileImageField
from versatileimagefield.placeholder import OnDiscPlaceholderImage


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    published_date = models.DateField()
    cover_image = VersatileImageField('Image',upload_to='book_covers/', null = True, width_field='width', height_field='height')
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
