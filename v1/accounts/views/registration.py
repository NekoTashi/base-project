# from django.conf import settings
# from django.contrib.auth.tokens import default_token_generator

from rest_framework import generics

# from templated_email import send_templated_mail

from v1.accounts.models.user import User
from v1.accounts.serializers.registration import RegistrationSerializer
# from v1.accounts.utils import encode_uid


# v1/registration/
class RegistrationView(generics.CreateAPIView):

    queryset = User.objects.all()
    permission_classes = []
    authentication_classes = []
    serializer_class = RegistrationSerializer

    def perform_create(self, serializer):

        user = serializer.save()

        # activation proccess
        # user.is_active = False
        # user.save()

        # send_templated_mail(
        #     template_name='password_reset',
        #     from_email=settings.DEFAULT_FROM_EMAIL,
        #     recipient_list=[user.email],
        #     context={
        #         'from_email': settings.DEFAULT_FROM_EMAIL,
        #         'user': user,
        #         'host': self.request.get_host(),
        #         'scheme': self.request.scheme,
        #         'uid': encode_uid(user.pk),
        #         'token': default_token_generator.make_token(user),
        #     }
        # )
