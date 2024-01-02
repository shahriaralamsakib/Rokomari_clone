from django.urls import path
from .views import UserRegistrationView, UserView, AllUsersView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('user/<int:pk>/', UserView.as_view(), name='user'),
    path('users/', AllUsersView.as_view(), name='all-users'),
]