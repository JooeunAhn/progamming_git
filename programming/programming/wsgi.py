"""
WSGI config for programming project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "programming.settings.prod")

application = get_wsgi_application()


#####wsgi가 manage.py 대신에 실행했을때는 개발환경이 아닌 prod환경이니까
#####이렇게 지정해줘야한다.

