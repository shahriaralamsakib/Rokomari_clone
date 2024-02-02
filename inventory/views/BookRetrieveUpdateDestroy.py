
from rest_framework import generics
from core.models import User
from inventory.models import Book
from inventory.serializers.Book import BookSerializer
from rest_framework.views import APIView
# Create your views here.

class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer