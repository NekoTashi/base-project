from .base import *  # noqa


# DEBUG
# ------------------------------------------------------------------------------
DEBUG = False
TEMPLATES[0]['OPTIONS']['debug'] = True

# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Nota: La key por defecto sólo se debe usar en testing
SECRET_KEY = env('DJANGO_SECRET_KEY', default='TEST!')

# MAIL CONFIG
# ------------------------------------------------------------------------------
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025

# In-memory email backend guarda los emails en django.core.mail.outbox
EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'

DEFAULT_FROM_EMAIL = 'default_from_email@email.test'

# CACHING
# ------------------------------------------------------------------------------
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}

# TESTING
# ------------------------------------------------------------------------------
TEST_RUNNER = 'django.test.runner.DiscoverRunner'

# PASSWORD HASHING
# ------------------------------------------------------------------------------
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]

# TEMPLATE LOADERS
# ------------------------------------------------------------------------------
# Mantiene los templates en memoria para runnear los tests más rápido
TEMPLATES[0]['OPTIONS']['loaders'] = [
    ['django.template.loaders.cached.Loader', [
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    ], ],
]
