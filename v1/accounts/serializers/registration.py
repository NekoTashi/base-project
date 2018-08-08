from rest_framework import serializers

from v1.accounts.models.user import User


class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'password', 'name']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
