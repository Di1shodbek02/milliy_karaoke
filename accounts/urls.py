from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from accounts.views import RegisterAPIView, ConfirmationCodeAPIView, ForgetPasswordAPIView, PasswordResetView, \
    UserUpdateGenericAPIView, UserLict, LogoutAPIView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('confirmation-code/', ConfirmationCodeAPIView.as_view(), name='confirmation_code'),
    path('forget-password/', ForgetPasswordAPIView.as_view(), name='reset_password'),
    path('password-reset/<str:uid>/<str:token>/', PasswordResetView.as_view(), name='password_reset'),
    path('update-user/', UserUpdateGenericAPIView.as_view(), name='update_user'),
    path('user-list/', UserLict.as_view(), name='user_list'),
    path('log-out/', LogoutAPIView.as_view(), name='logout'),
]
