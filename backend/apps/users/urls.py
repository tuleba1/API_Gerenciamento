from django.urls import path
from .views import (
    UserCreateView,
    UserListView,
    UserDetailView,
    UserMeView,
    UserUpdateView,
    UserDeleteView,
    ChangePasswordView,
)

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/create/', UserCreateView.as_view(), name='user-create'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('users/me/', UserMeView.as_view(), name='user-me'),
    path('users/update/', UserUpdateView.as_view(), name='user-update'),
    path('users/delete/', UserDeleteView.as_view(), name='user-delete'),
    path('users/change-password/', ChangePasswordView.as_view(), name='user-change-password'),
]