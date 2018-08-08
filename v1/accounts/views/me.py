from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from v1.accounts.models.user import User
from v1.accounts.serializers.me import MeSerializer


# v1/me/
class MeView(generics.RetrieveUpdateAPIView):

    queryset = User.objects.all()
    serializer_class = MeSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication]

    def get_object(self, *args, **kwargs):
        return self.request.user
