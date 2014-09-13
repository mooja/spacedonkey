from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'spacedonkey.views.index', name='index'),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^admin/', include(admin.site.urls)),
)
