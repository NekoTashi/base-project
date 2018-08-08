from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import validate_email
from django.db import models
from django.utils import timezone as django_timezone

from v1.accounts.managers.user_manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):

    # django default attrs
    email = models.EmailField(unique=True, validators=[validate_email, ])
    name = models.CharField(blank=True, max_length=255)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=django_timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        get_latest_by = 'date_joined'

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name
