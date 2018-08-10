import datetime
import environ

ROOT_DIR = environ.Path(__file__) - 3
APPS_DIR = ROOT_DIR.path("v1")

env = environ.Env()


# SITE CONFIG
# --------------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["*"]

# APP CONFIG
# --------------------------------------------------------------------------------------
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.gis",
    "django.contrib.humanize",
]

THIRD_PARTY_APPS = ["rest_framework", "corsheaders", "silk", "social_django"]

LOCAL_APPS = ["v1.accounts.apps.AccountsConfig"]

# https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = LOCAL_APPS + DJANGO_APPS + THIRD_PARTY_APPS

# AUTH USER MODEL
# --------------------------------------------------------------------------------------
AUTH_USER_MODEL = "accounts.User"

# MIDDLEWARES
# --------------------------------------------------------------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",  # django-cors-headers
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# DEBUG
# --------------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool("DJANGO_DEBUG", default=True)

# DATABASE CONFIG
# --------------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
# Use it only if you need to access the database that is on the local host.
FORMAT_DATABASE_URL = "postgis://{user}:{password}@{hostname}:{port}/{database_name}"
LOCAL_DATABASE_URL = FORMAT_DATABASE_URL.format(
    user="dev",
    password="dev",
    hostname="localhost",
    port=5432,
    database_name="baseproject",
)
DATABASES = {"default": env.db("DATABASE_URL", default=LOCAL_DATABASE_URL)}
DATABASES["default"]["ATOMIC_REQUESTS"] = True

# GENERAL CONFIG
# --------------------------------------------------------------------------------------
# Timezones: http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
TIME_ZONE = "America/Santiago"
# https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = "es-cl"
SITE_ID = 1  # https://docs.djangoproject.com/en/dev/ref/settings/#site-id
USE_I18N = True  # https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_L10N = True  # https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_TZ = True  # https://docs.djangoproject.com/en/dev/ref/settings/#use-tz

# TEMPLATE CONFIG
# --------------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES-BACKEND
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
        "DIRS": [str(ROOT_DIR.path("templates"))],
        "OPTIONS": {
            # https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
            "debug": DEBUG,
            # https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
            # https://docs.djangoproject.com/en/dev/ref/templates/api/#loader-types
            "loaders": [
                "django.template.loaders.filesystem.Loader",
                "django.template.loaders.app_directories.Loader",
            ],
            # https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    }
]

# STATICFILES CONFIG
# --------------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = str(ROOT_DIR.path("static"))
STATICFILES_DIRS = []

# https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = "/static/"

# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# MEDIA CONFIG
# --------------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = str(ROOT_DIR.path("media"))

# https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = "/media/"

# URL CONFIG
# --------------------------------------------------------------------------------------
ROOT_URLCONF = "config.urls"

# https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = "config.wsgi.application"

# PASSWORD HASHERS
# --------------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/topics/auth/passwords/#using-argon2-with-django
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.BCryptPasswordHasher",
]

# PASSWORD VALIDATORS
# --------------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# AUTHENTICATION CONFIG
# --------------------------------------------------------------------------------------
AUTHENTICATION_BACKENDS = ["django.contrib.auth.backends.ModelBackend"]

# REST FRAMEWORK CONFIG
# --------------------------------------------------------------------------------------
# http://www.django-rest-framework.org/api-guide/settings/
REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": ["rest_framework.renderers.JSONRenderer"],
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.IsAuthenticated"],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication"
    ],
}

# DJANGO CORS HEADERS CONFIG
# --------------------------------------------------------------------------------------
# https://github.com/ottoyiu/django-cors-headers
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_HEADERS = [
    "x-requested-with",
    "content-type",
    "accept",
    "origin",
    "authorization",
    "x-csrftoken",
    "content-disposition",
    "cache-control",
]

# PSA CONFIG
# --------------------------------------------------------------------------------------
SOCIAL_AUTH_PIPELINE = [
    "social_core.pipeline.social_auth.social_details",
    "social_core.pipeline.social_auth.social_uid",
    "social_core.pipeline.social_auth.auth_allowed",
    "social_core.pipeline.social_auth.social_user",
    "common.pipeline.require_email",
    "social_core.pipeline.user.get_username",
    "social_core.pipeline.social_auth.associate_by_email",
    "social_core.pipeline.mail.mail_validation ",
    "social_core.pipeline.user.create_user",
    "social_core.pipeline.social_auth.associate_user",
    "social_core.pipeline.social_auth.load_extra_data",
    "social_core.pipeline.user.user_details",
]

SOCIAL_AUTH_AUTHENTICATION_BACKENDS = [
    "social_core.backends.facebook.FacebookOAuth2",
    "social_core.backends.email.EmailAuth",
]

SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = True

# facebook
SOCIAL_AUTH_FACEBOOK_SCOPE = ["email"]
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {"fields": "id,name,email"}
SOCIAL_AUTH_FACEBOOK_KEY = env("DJANGO_SOCIAL_AUTH_FACEBOOK_KEY", default=None)
SOCIAL_AUTH_FACEBOOK_SECRET = env("DJANGO_SOCIAL_AUTH_FACEBOOK_SECRET", default=None)

# ADMIN URL
# --------------------------------------------------------------------------------------
ADMIN_URL = "admin/"

# CELERY CONFIG
# --------------------------------------------------------------------------------------
INSTALLED_APPS += ["v1.taskapp.celery.CeleryConfig"]
CELERY_BROKER_URL = env("REDIS_URL", default="redis://")

# JWT AUTH
# --------------------------------------------------------------------------------------
JWT_AUTH = {
    "JWT_EXPIRATION_DELTA": datetime.timedelta(days=365),
    # 'JWT_RESPONSE_PAYLOAD_HANDLER': 'src.apps.users.utils.jwt_response_payload_handler',
}
