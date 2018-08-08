from django.utils.translation import ugettext_lazy as _

from rest_framework import exceptions

from v1.accounts.serializers.uid_token_serializer import UidAndTokenSerializer


STALE_TOKEN_ERROR = _('Stale token for given user.')


class ActivationSerializer(UidAndTokenSerializer):

    default_error_messages = {
        'stale_token': STALE_TOKEN_ERROR,
    }

    def validate(self, validated_data):

        validated_data = super().validate(validated_data)
        if self.user.is_active:
            raise exceptions.PermissionDenied(self.error_messages['stale_token'])
        return validated_data
