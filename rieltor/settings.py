"""
Django settings for aaa_portal project.
"""

from pathlib import Path
from .secret import *

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# my_django_secret_key import from secret.py
SECRET_KEY = my_django_secret_key

# SECURITY WARNING: don't run with debug turned on in production!
# my_debug import from secret.py
DEBUG = my_debug
# DEBUG = False

# my_allowed_hosts import from secret.py
ALLOWED_HOSTS = my_allowed_hosts

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'captcha',
    # my apps:
    'modules.system.apps.SystemConfig',
    'modules.services',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'rieltor.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'main.context_processors.get_main_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'rieltor.wsgi.application'


DATABASES = {
    "default": my_pg_connect
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'ru'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/
STATIC_ROOT = BASE_DIR / 'static'
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'rieltor/static',
    # BASE_DIR / 'static',
    BASE_DIR / 'templates/src', # for bootstrat
]

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'
# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_HOST = "smtp.yandex.ru"
EMAIL_HOST_PORT = 465
EMAIL_HOST_USER = my_email_host_user
EMAIL_HOST_PASSWORD = my_email_host_password
# EMAIL_USE_SSL = True
EMAIL_USE_TLS = True

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER
EMAIL_ADMIN = EMAIL_HOST_USER


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


LOGOUT_REDIRECT_URL = 'home'
LOGIN_URL = 'system:login'

# AUTH_USER_MODEL = 'users.User'

# DEFAULT_USER_IMAGE = '/static/users/img/anonim.png'

CAPTCHA_FONT_SIZE = 32
CAPTCHA_BACKGROUND_COLOR = '#7CFC00'
CAPTCHA_FOREGROUND_COLOR = '#CD5C5C'
CAPTCHA_LENGTH = 5
# CAPTCHA_FLITE_PATH = 1

AUTHENTICATION_BACKENDS = [
    'modules.system.backends.UserModelBackend' # переопределение аутентификации (добавление по email)
]

CSRF_TRUSTED_ORIGINS = my_csrf_trusted_origins
