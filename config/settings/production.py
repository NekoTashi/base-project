from .base import *  # noqa

# DEBUG
# -------------------------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = False

# SECRET CONFIG
# -------------------------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env('DJANGO_SECRET_KEY')

# OPBEAT CONFIG
# -------------------------------------------------------------------------------------------------
# https://opbeat.com/languages/django/
# INSTALLED_APPS += ['opbeat.contrib.django']
# OPBEAT = {
#     'ORGANIZATION_ID': env('DJANGO_OPBEAT_ORGANIZATION_ID'),
#     'APP_ID': env('DJANGO_OPBEAT_APP_ID'),
#     'SECRET_TOKEN': env('DJANGO_OPBEAT_SECRET_TOKEN')
# }
# # MIDDLEWARE = ['opbeat.contrib.django.middleware.OpbeatAPMMiddleware', ] + MIDDLEWARE

# GUNICORN CONFIG
# -------------------------------------------------------------------------------------------------
INSTALLED_APPS += ['gunicorn']

# STATIC CONFIG
# -------------------------------------------------------------------------------------------------
STATIC_ROOT = env('STATIC_ROOT')

# MEDIA CONFIG
# -------------------------------------------------------------------------------------------------
MEDIA_ROOT = env('MEDIA_ROOT')

# EMAIL
# -------------------------------------------------------------------------------------------------
DEFAULT_FROM_EMAIL = env('DJANGO_DEFAULT_FROM_EMAIL', default=None)
SERVER_EMAIL = env('DJANGO_SERVER_EMAIL', default=DEFAULT_FROM_EMAIL)

# ANYMAIL CONFIG (Mailgun)
# -------------------------------------------------------------------------------------------------
# INSTALLED_APPS += ['anymail', ]
# ANYMAIL = {
#     'MAILGUN_API_KEY': env('DJANGO_MAILGUN_API_KEY'),
#     'MAILGUN_SENDER_DOMAIN': env('MAILGUN_SENDER_DOMAIN')
# }
# EMAIL_BACKEND = 'anymail.backends.mailgun.MailgunBackend'

# TEMPLATE CONFIG
# -------------------------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/templates/api/#django.template.loaders.cached.Loader
TEMPLATES[0]['OPTIONS']['loaders'] = [(
    'django.template.loaders.cached.Loader',
    [
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    ]
), ]

# DATABASE CONFIG
# -------------------------------------------------------------------------------------------------
DATABASES['default'] = env.db('DATABASE_URL')

# LOGGING CONFIG
# -------------------------------------------------------------------------------------------------
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s '
                      '%(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django.security.DisallowedHost': {
            'level': 'ERROR',
            'handlers': ['console', ],
            'propagate': True
        }
    }
}

# ADMIN URL
# -------------------------------------------------------------------------------------------------
ADMIN_URL = env('DJANGO_ADMIN_URL')
