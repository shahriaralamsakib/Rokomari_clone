from django.urls import path
from inventory.views.BookListCreate import BookListCreateView
from inventory.views.BookRetrieveUpdateDestroy import BookRetrieveUpdateDestroyView
from inventory.views.BookSearch import BookSearchView


    
urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book-retrieve-update-destroy'),
    path('api/search/', BookSearchView.as_view(), name='book_search'),
]