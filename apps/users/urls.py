from django.urls import path
from .views import UserCreateView, UserListView, UserMeView, UserUpdateView


urlpatterns = [
    path('register/', UserCreateView.as_view(), name='user-register'),
    path('', UserListView.as_view(), name='user-list'),
    path('me/', UserMeView.as_view(), name='user-me'),
    path('update/', UserUpdateView.as_view(), name='user-update'),
    ] 