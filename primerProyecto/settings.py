"""
Django settings for primerProyecto project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

#encoding:utf-8

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR representa a la direccion principal del proyecto
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

from unipath import Path
RUTA_PROYECTO = Path(__file__).ancestor(2)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v1lkyxstm!%ndc*e-!&*%&5v9bza_62u=vu)6xa*@rsh88belg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

TEMPLATE_DIRS = (
    RUTA_PROYECTO.child('templates'),
    #Always use forward slashed, even on Windows.
    #Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.usuarios',
    'apps.inicio',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'primerProyecto.urls'

WSGI_APPLICATION = 'primerProyecto.wsgi.application'

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
    ('Luca Giordano', 'lktz25294@gmail.com'),
)

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Esto seria el template a utilizar para el caso que la base de datos a usar
# no sea la default de sqlite3.
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
#        'NAME': '',                      # Or path to database file if using sqlite3.
#        'USER': '',                      # Not used with sqlite3.
#        'PASSWORD': '',                  # Not used with sqlite3.
#        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
#        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
#    }
#}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'es-AR'

TIME_ZONE = 'America/Argentina/Buenos_Aires'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'

#Additional locations of static files
STATICFILES_DIRS = (
    RUTA_PROYECTO.child('static'),
)

# Absolute filesystem path to the directory that will hold user-uploaded files.
MEDIA_ROOT = RUTA_PROYECTO.child('media')

#UTL that handles the media server from MEDIA_ROOT. Make sure to use a
#trailing slash.
#Examples: "httml://example.com/media","http://media.example.com/"
MEDIA_URL = 'http://127.0.0.1:8000/media/'

from django.core.urlresolvers import reverse_lazy
LOGIN_URL = reverse_lazy('inicio')
LOGIN_REDIRECT_URL = reverse_lazy('inicio')
LOGOUT_URL = reverse_lazy('logout')