from django.urls import path
from users.views import (
    UserRegisterView,
    LoginView,
    TokenRefreshView,
    LogoutView,
    ForgotPasswordView,
    ConfirmCodeView,
    ChangePasswordView,
    ChangeForgotPasswordView,
    UserProfileUpdateView,
    UserMeView,
)

from django.urls import path, include
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


urlpatterns = [
    path('login/', LoginView.as_view(), name='token_obtain_pair'),
    path('login/google/', GoogleLogin.as_view(), name='google_login'),
    path('login/facebook/', FacebookLogin.as_view(), name='facebook_login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserRegisterView.as_view(), name='user-registration'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),
    path('confirm-code/', ConfirmCodeView.as_view(), name='confirm-code'),
    path('change-forgot-password/', ChangeForgotPasswordView.as_view(), name='change-forgot-password'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('profile/update/', UserProfileUpdateView.as_view(), name='profile-update'),
    path('me/', UserMeView.as_view(), name='users-me'),

]
