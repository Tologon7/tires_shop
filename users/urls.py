from django.urls import path
from users.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import UserProfileView


urlpatterns = [
    path('login/', LoginView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='user-registration'),
    path("email_verify/", VerifyEmailView.as_view(), name="email_verify"),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),
    path('confirm-code/', ConfirmCodeView.as_view(), name='confirm-code'),
    path('change-forgot-password/', ChangeForgotPasswordView.as_view(), name='change-forgot-password'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('profile/update/', UserProfileUpdateView.as_view(), name='profile-update'),
    path('me/', UserMeView.as_view(), name='users-me')

 ]

SIMPLE_JWT = {

    'AUTH_HEADER_TYPES': ('JWT',),

}
