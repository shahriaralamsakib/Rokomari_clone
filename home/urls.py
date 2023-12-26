from django.urls import path
from .views import UserRegistrationView, UserInfoView, AllUsersView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('user/<int:pk>/', UserInfoView.as_view(), name='user-info'),
     path('users/', AllUsersView.as_view(), name='all-users'),
]