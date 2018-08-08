from rest_framework import serializers

from django.contrib.auth.tokens import default_token_generator
from django.utils.translation import ugettext_lazy as _

from v1.accounts.models.user import User
from v1.accounts.utils import decode_uid


INVALID_TOKEN_ERROR = _('Invalid token for given user.')
INVALID_UID_ERROR = _('Invalid user id or user doesn\'t exist.')


class UidAndTokenSerializer(serializers.Serializer):
    uid = serializers.CharField()
    token = serializers.CharField()

    default_error_messages = {
        'invalid_token': INVALID_TOKEN_ERROR,
        'invalid_uid': INVALID_UID_ERROR,
    }

    def validate_uid(self, value):

        try:
            uid = decode_uid(value)
            self.user = User.objects.get(pk=uid)
        except (User.DoesNotExist, ValueError, TypeError, OverflowError):
            raise serializers.ValidationError(self.error_messages['invalid_uid'])
        return value

    def validate(self, validated_data):

        validated_data = super().validate(validated_data)
        if not default_token_generator.check_token(self.user, validated_data['token']):
            raise serializers.ValidationError(self.error_messages['invalid_token'])
        return validated_data
