from django.urls import path
from .views import UserRegistrationAPIView,UserProfileAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('register/',UserRegistrationAPIView.as_view(),name='registration'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('me/',UserProfileAPIView.as_view(),name='me')
]
