"""
ASGI config for campus_events project.
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import events.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'campus_events.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            events.routing.websocket_urlpatterns
        )
    ),
})
