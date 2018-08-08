from django.contrib.auth.hashers import make_password

from rest_framework import serializers

from v1.accounts.models.user import User


class MeSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'name', 'password']
        extra_kwargs = {
            'email': {'read_only': True},
            'password': {'write_only': True},
        }

    def validate(self, validated_data):

        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data.get('password'))
        return super().validate(validated_data)
