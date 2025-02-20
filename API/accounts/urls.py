from django.urls import path

from rest_framework_simplejwt.views import (
    TokenRefreshView, TokenObtainPairView,
)

from .views import UserListView, RegisterView

app_name = 'accounts'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='Register'),
    path('users/', UserListView.as_view(), name='User-List'),
    path('token/', TokenObtainPairView.as_view(), name='TokenObtainPair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='TokenRefresh'),
]