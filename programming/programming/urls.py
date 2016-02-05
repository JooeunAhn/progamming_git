"""programming URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')), ### auth앱 안에있는 많은 메소드들 쓸수잇음
    url(r'^blog/', include('blog.urls', namespace = 'blog')),
]


urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
###미디어루트 밑에 경로를 읽어오는 것


## (?P    )->정규표현식 사용할꺼다 <pk> 는 인자이름으로  그래서 view에서 pk로 받아야한다.


