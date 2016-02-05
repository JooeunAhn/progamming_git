import os
from .common import *


DEBUG = False

##DEBUG -> True는 개발환경 False 배포환경
##Debug가 true일시 오류코드나 내부상황이 모두 보임



ALLOWED_HOSTS = ['*']
### 모든 도메인에 대해서 동작하겠다.
### DNS domain name service
### naver.com -> 0.0.0.0
### 한 아이피가 여러대의 머신을 가질 수 있다.


SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', SECRET_KEY)

DATABASES = {
    'default': {
        'ENGINE' : os.environ.get('DJANGO_DATABASE_ENGINE', 'django.db.backends.postgresql_psycopg2'),
        'Name' : os.environ.get('DJANGO_DATABASE_NAME', 'ubuntu'),
        'USER' : os.environ.get('DJANGO_DATABASE_USER', 'ubuntu'),
        'PASSWORD' : os.environ.get('DJANGO_DATABASE_PASSWORD', 'withaskdjango!'),
        'HOST' : os.environ.get('DJANGO_DATABASE_HOST', '127.0.0.1'),
        #소스코드에 민감한 정보 넣어놓으면 ㄴㄴ 그런데 그냥 넣어놈 환경변수 공부해서 처리하기
    }

}

STATIC_ROOT = os.path.join(BASE_DIR, '..', 'staticfiles')
## 배포할때만 쓸테니까 이렇게 만들어주는 것
MEDIA_ROOT = os.path.join(BASE_DIR, '..', 'media')
## 소스코드의 공간과 업로드공간의 분리를 의도 ..하면 전 디렉토리니까
MEDIA_URL = '/media/'
