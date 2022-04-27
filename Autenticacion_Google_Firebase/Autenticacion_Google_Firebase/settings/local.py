from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
#
import firebase_admin
from firebase_admin import credentials, auth
#
DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_secret('DB_NAME'),
        'USER': get_secret('USER'),
        'PASSWORD': get_secret('PASSWORD'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Fire base Autentication
cred = credentials.Certificate("firebasekey.json")
firebase_admin.initialize_app(cred)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = ["static"] # DECLARACION DE LA UBICACION DE LOS ARCHIVOS ESTATICOS

# Lo de abajo es para que los archivos multimedia se guarden por defecto en la carpeta media, y que en la declaracion del "upload to" solo haya que poner la carpeta contenedora
MEDIA_URL = '/media/'
MEDIA_ROOT = "media"