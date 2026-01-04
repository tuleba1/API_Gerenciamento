from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    """
    Serializer para cadastrar usuários.
    """
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ('id', 'email','password')

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
    
class UserDetailSerializer(serializers.ModelSerializer):
    """
    Serializer para exibir detalhes do usuário.
    """
    class Meta:
        model = User
        fields = ('id', 'email', 'is_active', 'is_staff', 'is_active')
        read_only_fields = fields



class UserUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer para atualizar informações do usuário.
    """
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


    def validate_email(self, value):
        """
        Garatine que o email seja único ao atualizar.
        """

        user = self.instance
        if (
            User.objects
            .exclude(id=user.id)
            .filter(email=value)
            .exists()
        ):
            raise serializers.ValidationError(
                "Usuário com este email já existe."
            )

        return value
    
    class ChangePasswordSerializer(serializers.Serializer):
        """
        Serializer para alterar a senha do usuário.
        """
        old_password = serializers.CharField(write_only=True, required=True)
        new_password = serializers.CharField(write_only=True, required=True, min_length=8)
