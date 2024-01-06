from django.urls import path
from .views import (
    UserRegistrationView,
    UserView,
    AllUsersView,
    UserLoginView,
    UserLogoutView,
    UserProfileView
)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('logout/', UserLogoutView.as_view(), name='user-logout'),
    path('user/<int:pk>/', UserView.as_view(), name='user'),
    path('users/', AllUsersView.as_view(), name='all-users'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='user-profile'),
]