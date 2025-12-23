from apps.users import permissions
from rest_framework import viewsets, generics, permissions
from django.contrib.auth import get_user_model
from .serializers import (UserSerializer, UserDetailSerializer, UserUpdateSerializer, )

# Create your views here.

User = get_user_model()

class UserCreateView(generics.CreateAPIView):
    """
    Endpoint para cadastrar novos usuários.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class UserListView(generics.ListAPIView):
    """
    Endpoint para listar todos os usuários.
    (Apenas administradores podem acessar)
    """

    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [permissions.IsAdminUser]

class UserMeView(generics.RetrieveAPIView):
    """
    Retorno de dados de usuários autenticados.
    """

    serializer_class = UserDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
    

class UserUpdateView(generics.UpdateAPIView):
    """
    Atualiza os dados de usuários autenticados.
    (O usuário só pode atualizar seus próprios dados)
    """

    serializer_class = UserUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user