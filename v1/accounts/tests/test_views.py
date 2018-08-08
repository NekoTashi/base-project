import json

from django.core import mail
from django.urls import reverse
from django.contrib.auth.tokens import default_token_generator

from rest_framework import status
from rest_framework.test import APITestCase

from v1.accounts.models.user import User
from v1.accounts.utils import encode_uid
from v1.accounts.utils import decode_uid
from v1.accounts.factories.user import UserFactory, DEFAULT_TEST_PASSWORD


class LoginViewTestCase(APITestCase):
    url = reverse("login")

    def setUp(self):
        self.user = UserFactory()

    def test_login_without_email(self):
        data = {"password": DEFAULT_TEST_PASSWORD}
        response = self.client.post(self.url, data)
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)

    def test_login_with_wrong_password(self):
        data = {"email": self.user.email, "password": "wrong_password"}
        response = self.client.post(self.url, data)
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)

    def test_login_with_valid_data(self):
        data = {"email": self.user.email, "password": DEFAULT_TEST_PASSWORD}
        response = self.client.post(self.url, data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertTrue("token" in json.loads(response.content))


class RegistrationViewTestCase(APITestCase):
    url = reverse("registration")

    def setUp(self):
        self.email = "test_email@email.test"
        self.password = "password"

    def test_registration_without_email_activation(self):
        data = {"email": self.email, "password": self.password}
        response = self.client.post(self.url, data)
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)


class PasswordResetViewTestCase(APITestCase):
    url = reverse("password-reset")

    def setUp(self):
        self.user = UserFactory()
        self.invalid_email_format = "invalid_email"
        self.email_does_not_exist = "email_does_not_exist@email.test"

    def test_password_reset_with_invalid_format_email(self):
        data = {"email": self.invalid_email_format}
        response = self.client.post(self.url, data)
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)

    def test_password_reset_with_invalid_email(self):
        data = {"email": self.email_does_not_exist}
        response = self.client.post(self.url, data)
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)

    def test_password_reset_with_valid_email(self):
        data = {"email": self.user.email}
        response = self.client.post(self.url, data)
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        self.assertEqual(len(mail.outbox), 1)


class PasswordResetConfirmViewTestCase(APITestCase):
    url = reverse("password-reset-confirm")

    def setUp(self):
        self.user = UserFactory()
        self.new_password = "new_password"
        self.invalid_uid = "invalid_uid"
        self.invalid_token = "invalid_token"

    def test_password_reset_confirm_with_invalid_uid(self):
        data = {
            "uid": self.invalid_uid,
            "token": default_token_generator.make_token(self.user),
            "password": self.new_password,
        }
        response = self.client.post(self.url, data)
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)

    def test_password_reset_confirm_with_invalid_token(self):
        data = {
            "uid": encode_uid(self.user.pk),
            "token": self.invalid_token,
            "password": self.new_password,
        }
        response = self.client.post(self.url, data)
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)

    def test_password_reset_confirm_with_valid_data(self):
        data = {
            "uid": encode_uid(self.user.pk),
            "token": default_token_generator.make_token(self.user),
            "password": self.new_password,
        }
        response = self.client.post(self.url, data)
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)

        # update user data and check new password
        self.user = User.objects.get(pk=decode_uid(data.get("uid")))
        self.assertTrue(self.user.check_password(self.new_password))


class MeViewTestCase(APITestCase):
    url = reverse("me")

    def setUp(self):
        self.user = UserFactory()
        self.new_password = "new_password"
        self.client.force_authenticate(user=self.user)

    def test_me_get_user_data(self):
        response = self.client.get(self.url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(self.user.email, response.data.get("email"))

    def test_me_update_user_data(self):
        data = {"password": self.new_password}
        response = self.client.patch(self.url, data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

        # update user data and check new password
        self.user = User.objects.get(email=self.user.email)
        self.assertTrue(self.user.check_password(self.new_password))


class ActivationViewTestCase(APITestCase):
    url = reverse("activation")

    def setUp(self):
        self.user = UserFactory(is_active=False)
        self.invalid_uid = "invalid_uid"
        self.invalid_token = "invalid_token"

    def test_activation_with_invalid_data(self):
        data = {"uid": self.invalid_uid, "token": self.invalid_token}
        response = self.client.post(self.url, data)
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)

    def test_activation_with_valid_data(self):
        data = {
            "uid": encode_uid(self.user.pk),
            "token": default_token_generator.make_token(self.user),
        }
        response = self.client.post(self.url, data)
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
