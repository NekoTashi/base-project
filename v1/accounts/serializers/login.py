from rest_framework import serializers

from v1.accounts.models.user import User


class JWTLoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['pk', 'email', 'name']
