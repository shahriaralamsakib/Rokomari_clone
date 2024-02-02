
from rest_framework import generics
from inventory.models import Book
from inventory.serializers.Book import BookSerializer
from rest_framework.views import APIView
# Create your views here.


class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer