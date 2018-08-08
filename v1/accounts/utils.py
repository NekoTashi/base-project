from django.utils.encoding import force_bytes
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.utils.http import urlsafe_base64_encode

from rest_framework_jwt.utils import jwt_encode_handler
from rest_framework_jwt.utils import jwt_payload_handler


def decode_uid(pk):
    return force_text(urlsafe_base64_decode(pk))


def encode_uid(pk):
    return urlsafe_base64_encode(force_bytes(pk)).decode()


def get_jwt_token(user):
    return jwt_encode_handler(jwt_payload_handler(user))
