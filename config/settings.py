"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 2.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# 本番運用時は別の値に置き換えること。
# 生成ツール：https://www.miniwebtool.com/django-secret-key-generator/
SECRET_KEY = '4bx^y%u0$)sr7iwx-5cyp+%8%!hu!^k+@1sxotdm2^i_pgz2+3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'users.apps.UsersConfig',
    'app.apps.AppConfig',
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

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'ja-JP'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
STATIC_URL = '/static/'

# カスタムユーザーモデルの使用
# https://docs.djangoproject.com/ja/2.1/topics/auth/customizing/#substituting-a-custom-user-model
AUTH_USER_MODEL = 'users.User'

# 管理サイトのログイン機能を通常のログイン機能として使う
# https://docs.djangoproject.com/ja/2.1/ref/settings/#login-url
LOGIN_URL = 'admin:login'
LOGOUT_REDIRECT_URL = '/'

# django-crispy-forms
# https://django-crispy-forms.readthedocs.io/en/latest/install.html#template-packs
CRISPY_TEMPLATE_PACK = 'bootstrap4'


# django-filter
# https://django-filter.readthedocs.io/en/latest/ref/settings.html#filters-verbose-lookups
# 検索フォームのラベル表示の修正。英語の説明を消す。
def FILTERS_VERBOSE_LOOKUPS():
    from django_filters.conf import DEFAULTS

    verbose_lookups = DEFAULTS['VERBOSE_LOOKUPS'].copy()
    verbose_lookups.update({
        'exact': '',
        'iexact': '',
        'contains': '',
        'icontains': '',
    })
    return verbose_lookups


# ログ設定
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'local': {
            'format': '%(asctime)s [%(levelname)s] %(pathname)s:%(lineno)d %(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'local',
        },
    },
    'loggers': {
        # 自作アプリケーション全般のログを拾う
        '': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        # Django本体のログ全般を拾う
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        # SQL出力
        'django.db.backends': {
            'handlers': ['console'],
            # DEBUGで出力ON、INFOでOFF
            'level': 'INFO',
            'propagate': False,
        },
    }
}

import os
import django_heroku

if 'DYNO' in os.environ:
    django_heroku.settings(locals())
