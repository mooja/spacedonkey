from django.conf.urls import patterns, include, url
from blog import views

urlpatterns = patterns('',
    url(r'^$', views.list_view, name='list_view'),
)
