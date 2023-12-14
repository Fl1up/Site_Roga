from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from main.users.apps import UsersConfig
from main.users.views import (
    UserDestroyAPIView,
    UserCreateAPIView,
    UserListAPIView,
    UserUpdateAPIView,
    UserRetrieveAPIView
)

app_name = UsersConfig.name
"""
Создание урлов для авторизации
"""
urlpatterns = [
    path("create/", UserCreateAPIView.as_view(), name="user_create"),
    path("list/", UserListAPIView.as_view(), name="user_list"),
    path("detail/<int:pk>/", UserRetrieveAPIView.as_view(), name="user_detail"),
    path("update/<int:pk>/", UserUpdateAPIView.as_view(), name="user_update"),
    path("delete/<int:pk>/", UserDestroyAPIView.as_view(), name="user_delete"),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
