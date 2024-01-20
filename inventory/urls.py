from django.urls import path
from . import views
from inventory.views.BookListCreateView import BookListCreateView
from inventory.views.BookRetrieveUpdateDestroyView import BookRetrieveUpdateDestroyView



urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book-retrieve-update-destroy'),
]