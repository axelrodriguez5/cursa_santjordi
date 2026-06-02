"""
WSGI config for cursa_santjordi project.
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cursa_santjordi.settings')

application = get_wsgi_application()
