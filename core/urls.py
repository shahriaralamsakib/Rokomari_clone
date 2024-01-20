from django.urls import path
#from core import views
from core.views.UserRegistration import UserRegistrationView
from core.views.UserView import UserView
from core.views.AllUsers import AllUsersView
from core.views.UserLoginView import UserLoginView
from core.views.UserLogoutView import UserLogoutView
from core.views.UserProfileView import UserProfileView
#from core.views.home import home



urlpatterns = [
    #path('', home.home, name='home'),
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('logout/', UserLogoutView.as_view(), name='user-logout'),
    path('user/<int:pk>/', UserView.as_view(), name='user'),
    path('users/', AllUsersView.as_view(), name='all-users'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='user-profile'),
]