from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from .serializers import (
    UserSerializer,
    UserDetailSerializer,
    UserUpdateSerializer,
)
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status



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
    (Apenas administradores)
    """
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [permissions.IsAdminUser]


class UserDetailView(generics.RetrieveAPIView):
    """
    Endpoint para exibir detalhes de um usuário específico.
    """
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserMeView(generics.RetrieveAPIView):
    """
    Retorna os dados do usuário autenticado.
    """
    serializer_class = UserDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class UserUpdateView(generics.UpdateAPIView):
    """
    Atualiza os dados do usuário autenticado.
    """
    serializer_class = UserUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
    


class UserDeleteView(APIView):
    """
    Deleta o usuário autenticado.
    """
    def delete(self, request):
        user = request.user
        user.delete()
        return Response({"Usuário excluído com sucesso!"}, status=status.HTTP_204_NO_CONTENT)
    
    
class ChangePasswordView(APIView):
    """
    Endpoint para alterar a senha do usuário autenticado.
    """

    permission_classes = [IsAuthenticated]

    def put(self, request):
       serializer = ChangePasswordSerializer(data=request.data)
       serializer.is_valid(raise_exception=True)

       user = request.user

       if not user.check_password(serializer.validated_data['old_password']):
           return Response(
               {"old_password": ["Senha atual incorreta."]},
               status=status.HTTP_400_BAD_REQUEST
           )
       
       user.set_password(serializer.validated_data['new_password'])
       user.save()

       return Response({"message" : "Senha alterada com sucesso."}, status=status.HTTP_200_OK)