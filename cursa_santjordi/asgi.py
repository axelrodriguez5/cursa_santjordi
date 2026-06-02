"""
ASGI config for cursa_santjordi project.
"""

import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cursa_santjordi.settings')

application = get_asgi_application()
