from .base import *  # noqa

# DEBUG
# -------------------------------------------------------------------------------------------------
DEBUG = env.bool('DJANGO_DEBUG', default=True)
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

# SECRET KEY
# -------------------------------------------------------------------------------------------------
SECRET_KEY = env('DJANGO_SECRET_KEY', default='default_secret_key')

# EMAIL CONFIG
# -------------------------------------------------------------------------------------------------
# Nota: usar dev.yml para levantar mailhog
# EMAIL_PORT = 1025  # mailhog
# EMAIL_HOST = env('EMAIL_HOST', default='localhost')  # mailhog
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DEFAULT_FROM_EMAIL = 'localhost@localhost.com'

# CACHING
# -------------------------------------------------------------------------------------------------
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}

# DJANGO DEBUG TOOLBAR CONFIG
# -------------------------------------------------------------------------------------------------
# https://github.com/jazzband/django-debug-toolbar
INSTALLED_APPS += ['debug_toolbar', ]
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]

INTERNAL_IPS = ['127.0.0.1', ]

DEBUG_TOOLBAR_CONFIG = {
    'DISABLE_PANELS': [
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ],
    'SHOW_TEMPLATE_CONTEXT': True,
}

# DJANGO EXTENSIONS CONFIG
# -------------------------------------------------------------------------------------------------
# https://github.com/django-extensions/django-extensions
INSTALLED_APPS += ['django_extensions', ]
SHELL_PLUS_PRINT_SQL = True

# LOGGING CONFIG
# -------------------------------------------------------------------------------------------------
LOGGING = {
    # 'version': 1,
    # 'disable_existing_loggers': False,
    # 'handlers': {
    #     'console': {
    #         'class': 'logging.StreamHandler',
    #     },
    # },
    # 'loggers': {
    #     'django.db.backends': {
    #         'level': 'DEBUG',
    #         'handlers': ['console'],
    #     }
    # },
}

# REST FRAMEWORK CONFIG
# -------------------------------------------------------------------------------------------------
REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] += ['rest_framework.renderers.BrowsableAPIRenderer']

# CELERY CONFIG
# -------------------------------------------------------------------------------------------------
CELERY_ALWAYS_EAGER = True
