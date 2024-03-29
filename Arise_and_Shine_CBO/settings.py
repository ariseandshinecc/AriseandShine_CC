#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""
Django settings for Arise_and_Shine_CBO project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
from decouple import config, Csv
from dj_database_url import parse

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='*', cast=Csv())


# Application definition

INSTALLED_APPS = [
    'jazzmin', # Third party Admin theme
    'mainsite.apps.MainsiteConfig', # Custom app
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third party apps
    'phonenumber_field',
    'widget_tweaks',
    'django_cleanup.apps.CleanupConfig',
    'fontawesomefree'
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

ROOT_URLCONF = 'Arise_and_Shine_CBO.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'mainsite.context_processors.project_renderer',
                'mainsite.context_processors.cbo_profile',
            ],
        },
    },
]

WSGI_APPLICATION = 'Arise_and_Shine_CBO.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': config(
        'DATABASE_URL',
        default='sqlite:///db.sqlite3',
        cast=parse
    )
}

# Auto-created primary key
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

# Jazzmin configuration

JAZZMIN_SETTINGS = {
    "site_title": "Arise and shine Care Center",
    "site_header": "ARISE AND SHINE CARE CENTER",
    "site_logo": "mainsite/images/favicon.ico",
    "welcome_sign": "Welcome to Administration panel",
    "show_ui_builder": True,
    "copyright": "Arise and Shine Care Center CBO",
    "usermenu_links": [
        {"name": "View site", "url": "mainsite:home", "new_window": True},
    ],
    "topmenu_links": [
        {"name": "View site", "url": "mainsite:home", "new_window": True},
    ],
    "icons": {
        "auth": "fas fa-shield",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "mainsite.Message": "fas fa-comments",
        "mainsite.Donation": "fas fa-hand-holding-heart",
        "mainsite.Partner": "fas fa-hands-helping",
        "mainsite.Media": "fas fa-camera",
        "mainsite.Profile": "fas fa-landmark",
        "mainsite.Project": "fas fa-seedling",
        "mainsite.Career": "fas fa-user-tie",
        "mainsite.Contact": "fas fa-address-card",
        "mainsite.Address": "fas fa-address-card",
        "mainsite.Member": "fas fa-user-friends",
        "mainsite.NewsEvent": "fas fa-bullhorn",

    },
   
    "order_with_respect_to": [
        "mainsite.Profile",
        "mainsite.Address",
        "mainsite.Contact",
        "mainsite.Project",
        "mainsite.Partner",
        "mainsite.Donation",
        "mainsite.Media",
    ]
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": True,
    "brand_colour": "navbar-navy",
    "accent": "accent-primary",
    "navbar": "navbar-navy navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-purple",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": True,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "default",
    "dark_mode_theme": None,
    "actions_sticky_top": True
}

# Site security


CSRF_COOKIE_SECURE = config('CSRF_COOKIE_SECURE', default=False, cast=bool)

SESSION_COOKIE_SECURE = config('SESSION_COOKIE_SECURE', default=False, cast=bool)

CSRF_TRUSTED_ORIGINS = config('CSRF_TRUSTED_ORIGINS', default='http://*', cast=Csv())

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_ROOT = Path.joinpath(BASE_DIR, 'staticfiles')

STATIC_URL = '/static/'

STATICFILES_DIR = [
	Path.joinpath(BASE_DIR, 'static')
]

# Media files (e.g images uploaded by the users)

MEDIA_ROOT = Path.joinpath(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Phone number representation on the database

PHONENUMBER_DB_FORMAT = 'INTERNATIONAL'

# Email

EMAIL_BACKEND = config('EMAIL_BACKEND')
EMAIL_HOST = config('EMAIL_HOST', default='localhost')
EMAIL_PORT = config('EMAIL_PORT', default=25, cast=int)
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=False, cast=bool)
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL', default='webmaster@localhost')
SERVER_EMAIL = config('SERVER_EMAIL', default='root@localhost')
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')

# A list of people who get error code notifications

ADMINS = [config('ADMINS', default='info,info@ariseandshinecc.org' ,cast=Csv(post_process=tuple))]

# A list of people who get broken link notifications

MANAGERS = [config('MANAGERS', default='info,info@ariseandshinecc.org', cast=Csv(post_process=tuple))]

