from django.urls import path, re_path

from v1.accounts.views.login import JWTLoginView
from v1.accounts.views.me import MeView
from v1.accounts.views.password_reset import PasswordResetConfirmView
from v1.accounts.views.password_reset import PasswordResetView
from v1.accounts.views.registration import RegistrationView
from v1.accounts.views.activation import ActivationView
from v1.accounts.views.social_auth import exchange_token

urlpatterns = [

    # login
    path('auth-token/', JWTLoginView.as_view(), name='login'),

    # registration
    path('registration/', RegistrationView.as_view(), name='registration'),

    # reset_password
    path('password/reset/', PasswordResetView.as_view(), name='password-reset'),
    path('password/reset/confirm/', PasswordResetConfirmView.as_view(),
         name='password-reset-confirm'),

    # me
    path('me/', MeView.as_view(), name='me'),

    # social auth
    # re_path(r'social/(?P<backend>[^/]+)/$', exchange_token, name='social-auth'),

    # activation
    path('activation/', ActivationView.as_view(), name='activation'),

]
