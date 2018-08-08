from django.conf import settings
from django.contrib.auth.tokens import default_token_generator

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from templated_email import send_templated_mail

from v1.accounts.models.user import User
from v1.accounts.serializers.password_reset import PasswordResetConfirmSerializer
from v1.accounts.serializers.password_reset import PasswordResetSerializer
from v1.accounts.utils import encode_uid


# v1/password/reset/
class PasswordResetView(APIView):

    permission_classes = []
    authentication_classes = []

    def post(self, request):

        serializer = PasswordResetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            user = User.objects.get(
                email=serializer.validated_data.get("email"), is_active=True
            )

            # enviar email
            send_templated_mail(
                template_name="password_reset",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email],
                context={
                    "from_email": settings.DEFAULT_FROM_EMAIL,
                    "user": user,
                    "host": request.get_host(),
                    "scheme": request.scheme,
                    "uid": encode_uid(user.pk),
                    "token": default_token_generator.make_token(user),
                },
            )
        except User.DoesNotExist:
            pass

        return Response(status=status.HTTP_204_NO_CONTENT)


# v1/password/reset/confirm/
class PasswordResetConfirmView(APIView):

    permission_classes = []
    authentication_classes = []

    def post(self, request):

        serializer = PasswordResetConfirmSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.user
        user.set_password(serializer.data.get("password"))
        user.save()

        return Response(status=status.HTTP_204_NO_CONTENT)
