from rest_framework import generics
from rest_framework.response import Response
from core.models import User
from inventory.models import Book
from inventory.serializers.Book import BookSerializer
from rest_framework.views import APIView


class BookSearchView(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        if query:
            return Book.objects.filter(title__icontains=query) | Book.objects.filter(author__icontains=query)
        else:
            return Book.objects.all()