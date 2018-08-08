from rest_framework import serializers

from v1.accounts.serializers.uid_token_serializer import UidAndTokenSerializer


class PasswordSerializer(serializers.Serializer):
    password = serializers.CharField(style={'input_type': 'password'})


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()


class PasswordResetConfirmSerializer(UidAndTokenSerializer, PasswordSerializer):
    pass
