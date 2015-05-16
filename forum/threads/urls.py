from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<thread_slug>\S+)$', views.Thread, name='Thread')
]
