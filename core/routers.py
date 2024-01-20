from rest_framework.routers import DefaultRouter
from core.views.UserRegistration import UserRegistrationView
from core.views.UserView import UserView
from core.views.AllUsers import AllUsersView
from core.views.UserLoginView import UserLoginView
from core.views.UserLogoutView import UserLogoutView
from core.views.UserProfileView import UserProfileView

router = DefaultRouter()
router.register(r'User', UserView, basename='user')
router.register(r'User_registration', UserRegistrationView, basename='user-reg')
router.register(r'All_User', AllUsersView, basename='all-user')
router.register(r'User_login', UserLoginView, basename='user-login')
router.register(r'User_profile', UserProfileView, basename='user-profile')

urlpatterns = router.urls