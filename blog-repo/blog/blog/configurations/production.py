from .base import *

ALLOWED_HOSTS = ['lucasbarrera.pythonanywhere.com']



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


# TODO:  cambiar la configuración para prod
DATABASES = {
    'default': {

        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}

os.environ['DJANGO_PORT'] = "8080"