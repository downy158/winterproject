from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<space>.+)/$', views.list, name='list'),
    url(r'^$', views.main, name='main'),
]
