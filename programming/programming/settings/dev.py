from .common import *

###settings이외에 다른 곳에서는 코드 쓰지말기


INSTALLED_APPS += [
    'debug_toolbar',
]


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'