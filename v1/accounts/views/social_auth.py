from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from requests.exceptions import HTTPError

from social_django.utils import psa

from v1.accounts.serializers.social_auth import SocialSerializer
from v1.accounts.utils import get_jwt_token


@api_view(http_method_names=['POST'])
@permission_classes([AllowAny])
@psa()
def exchange_token(request, backend):
    """
    https://www.toptal.com/django/integrate-oauth-2-into-django-drf-back-end
    https://github.com/coriolinus/oauth2-article/blob/master/views.py
    """

    serializer = SocialSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        try:
            user = request.backend.do_auth(serializer.validated_data['access_token'])
        except HTTPError as e:
            return Response(
                {'errors': {'token': 'Invalid token', 'detail': str(e)}},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if user:
            if user.is_active:
                return Response({'token': get_jwt_token(user)})
            else:
                return Response(
                    {'errors': {'non_field_errors': 'This user account is inactive'}},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        else:
            return Response(
                {'errors': {'non_field_errors': "Authentication Failed"}},
                status=status.HTTP_400_BAD_REQUEST,
            )
