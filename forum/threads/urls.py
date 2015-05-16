from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.Home.as_view(), name='home'),
    url(r'^topics/$', views.TopicIndex.as_view(), name='topic_index'),
    url(r'^topics/(?P<topic_slug>\S+)$', views.TopicDetail.as_view(), name='topic_detail'),
    url(r'^topics/(?P<topic_slug>\S+)/(?P<thread_slug>\S+)$', views.ThreadDetail.as_view(), name='thread_detail')
]
