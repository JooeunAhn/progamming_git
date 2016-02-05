from django.conf.urls import url, include
from blog import views

urlpatterns = [
    url(r'^$', views.index, name ='index'),
    url(r'^bio/$', views.bio),
    url(r'^post/$', views.post_list, name = 'post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name = 'post_detail'),
    url(r'^senior/$', views.senior_list),
    url(r'^senior/(?P<pk>\d+)/$', views.senior_detail),
    url(r'^enterprise/$', views.enterprise_list),
    url(r'^enterprise/(?P<pk>\d+)/$',views.enterprise_detail),
    url(r'^youth/$', views.youth_list),
    url(r'^youth/(?P<pk>\d+)/$', views.youth_detail),
    ## form 실습
    url(r'^post/new/$', views.post_new, name= 'post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name = 'post_edit'),
    url(r'^post/(?P<post_pk>\d+)/comments/new/$', views.comments_new, name = 'comment_new'),
    url(r'^post/(?P<post_pk>\d+)/comments/(?P<pk>\d+)/edit/$', views.comments_edit, name = 'comment_edit'),


    url(r'^api/v1/', include("blog.api.v1", namespace = 'api_v1')),
    url(r'^api/v2/', include("blog.api.v2", namespace = 'api_v2'))
]

