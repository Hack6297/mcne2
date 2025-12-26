"""
Django settings for minecraft multiplayer server
"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

SECRET_KEY = os.environ.get('SECRET_KEY', 'minecraft-multiplayer-secret-key-change-in-production')
DEBUG = os.environ.get('DEBUG', 'True') == 'True'
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'daphne',
    'django.contrib.staticfiles',
    'channels',
]

MIDDLEWARE = []

ROOT_URLCONF = 'urls'

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [BASE_DIR],
    'APP_DIRS': True,
}]

WSGI_APPLICATION = 'wsgi.application'
ASGI_APPLICATION = 'asgi.application'

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR]

# Channels - Use Redis in production, in-memory for local development
REDIS_URL = os.environ.get('REDIS_URL')
if REDIS_URL:
    CHANNEL_LAYERS = {
        'default': {
            'BACKEND': 'channels_redis.core.RedisChannelLayer',
            'CONFIG': {
                "hosts": [REDIS_URL],
            },
        }
    }
else:
    CHANNEL_LAYERS = {
        'default': {
            'BACKEND': 'channels.layers.InMemoryChannelLayer'
        }
    }
