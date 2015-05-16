from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.Home.as_view(), name='home'),
    url(r'^topics/$', views.TopicIndex.as_view(), name='topics'),
    url(r'^topics/(?P<topic_slug>\S+)$', views.TopicDetail.as_view(), name = 'thread_index'),

    # url(r'^(?P<thread_slug>\S+)$', views.Thread.as_view(), name='Thread')
]
