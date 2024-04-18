from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import User


class RegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'birthday']


class ConfirmationCodeSerializer(serializers.Serializer):
    email = serializers.EmailField()
    confirm_code = serializers.IntegerField()


class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()


class PasswordResetLoginSerializer(serializers.Serializer):
    new_password = serializers.CharField()


class UserListSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password']


class UpdateUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['avatar', 'first_name', 'last_name', 'phone', 'birthday']


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('avatar','first_name', 'last_name', 'email', 'username', 'phone', 'birthday')