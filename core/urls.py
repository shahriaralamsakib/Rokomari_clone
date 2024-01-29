from django.urls import path
from core.views.UserRegistration import UserRegistrationView
from core.views.User import UserView
from core.views.AllUsers import AllUsersView
from core.views.UserLogin import UserLoginView
from core.views.UserLogout import UserLogoutView
from core.views.UserProfile import UserProfileView



urlpatterns = [
    #path('', views.home, name='home'),
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('logout/', UserLogoutView.as_view(), name='user-logout'),
    path('user/<int:pk>/', UserView.as_view(), name='user'),
    path('users/', AllUsersView.as_view(), name='all-users'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='user-profile'),
]