from django.urls import path
from users.views import (
    RegisterView,
    VerifyEmailView,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='user-registration'),
    path("email_verify/", VerifyEmailView.as_view(), name="email_verify"),
 ]
