from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from v1.accounts.models.user import User
from v1.accounts.serializers.login import JWTLoginSerializer
from v1.accounts.utils import get_jwt_token


# v1/auth-token/
class JWTLoginView(APIView):

    authentication_classes = []
    permission_classes = []

    def post(self, request):

        email = request.data.get("email")
        if not email:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        user = get_object_or_404(User, email=request.data.get("email"))
        user = authenticate(email=user.email, password=request.data.get("password"))
        if user:
            data = {"token": get_jwt_token(user), "user": JWTLoginSerializer(user).data}
            return Response(data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
