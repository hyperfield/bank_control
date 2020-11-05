import os
#from dotenv import load_dotenv
from environs import Env

env = Env()
env.read_env()

INSTALLED_APPS = ['datacenter']

DEBUG = env.bool("DEBUG")

ROOT_URLCONF = "project.urls"

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': env.str('ENGINE'),
        'HOST': env.str('HOST'),
        'PORT': env.str('PORT'),
        'NAME': env.str('NAME'),
        'USER': 'guard',
	'PASSWORD': env.str('PASSWORD')
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
