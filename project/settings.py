import os
from environs import Env

env = Env()
env.read_env()

INSTALLED_APPS = ['datacenter']

DEBUG = env.bool("DEBUG")

ROOT_URLCONF = "project.urls"

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': env.str('DB_ENGINE'),
        'HOST': env.str('DB_HOST'),
        'PORT': env.str('DB_PORT'),
        'NAME': env.str('DB_NAME'),
        'USER': env.str('DB_USERNAME'),
	'PASSWORD': env.str('DB_PASSWORD')
    }
}



SECRET_KEY = os.getenv('KEY')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True
