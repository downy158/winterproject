from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^space/(?P<space_id>[0-9]+)$', views.detail, name='detail'),
    url(r'^(?P<space_type>.+)/$', views.list, name='list'),
    url(r'^$', views.main, name='main'),
]
