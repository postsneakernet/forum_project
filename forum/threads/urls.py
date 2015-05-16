from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.Home.as_view(), name='home'),
    # url(r'^(?P<thread_slug>\S+)$', views.Thread.as_view(), name='Thread')
]
