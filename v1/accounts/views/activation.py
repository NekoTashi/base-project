from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from v1.accounts.serializers.activation import ActivationSerializer


# v1/activation/
class ActivationView(APIView):

    permission_classes = []
    authentication_classes = []

    def post(self, request):

        serializer = ActivationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.user.is_active = True
        serializer.user.save()

        return Response(status=status.HTTP_204_NO_CONTENT)
