"""
WSGI config for PROYECTO_TRANSPORTE_ESCOLAR project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os


from django.core.wsgi import get_wsgi_application

# Esta línea es clave y debe permanecer así
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PROYECTO_TRANSPORTE_ESCOLAR.settings')

application = get_wsgi_application()