from pathlib import Path

import sys, os

BASE_DIR = Path(__file__).resolve().parent.parent
apps = os.path.join(BASE_DIR, "apps")
sys.path.insert(0, apps)
sys.path.insert(0, str(BASE_DIR))

SECRET_KEY = "django-insecure-l@v+^w$odfsfht7+58(6ps0o!%$fsod=pf**zc(9ir(9e_=8#o"

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    "simpleui",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "user",
    "home",
    # "corsheaders",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    # "utils.common_middleware.MiddlewareTest"
]

ROOT_URLCONF = "luffy_api.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "luffy_api.wsgi.application"

user = os.environ.get("MYSQL_USER", "luffy")
password = os.environ.get("MYSQL_PASSWORD", "Luffy123?")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "luffy",
        "HOST": "127.0.0.1",
        "PORT": 3307,
        "USER": user,
        "PASSWORD": password,
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "zh-hans"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = False

STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "user.User"

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

from utils import common_logger

common_logger.configure_logger()

REST_FRAMEWORK = {
    "EXCEPTION_HANDLER": "utils.common_exception.exception_handler",
}

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_HEADERS = (
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
    # 额外允许的请求头
    "token",
)
from .common_settings import *
