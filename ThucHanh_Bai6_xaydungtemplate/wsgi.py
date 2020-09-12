"""
WSGI config for ThucHanh_Bai6_xaydungtemplate project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ThucHanh_Bai6_xaydungtemplate.settings')

application = get_wsgi_application()
