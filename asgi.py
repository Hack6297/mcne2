"""
ASGI config for Django Channels WebSocket support
"""
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from consumer import GameConsumer
from django.urls import path

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter([
        path("ws/game/", GameConsumer.as_asgi()),
    ]),
})
