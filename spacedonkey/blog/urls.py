from django.conf.urls import patterns, url
from blog.views import PostList, PostDetailView


urlpatterns = patterns('',
    url(r'^$', PostList.as_view(), name='index'),
    url(r'^post/(?P<pk>\d+)/(?P<slug>[-_\w]+)/$', PostDetailView.as_view(), name='post-detail'),
    url(r'^date/(?P<year>\d{4})/$', PostList.as_view(), name='post-list'),
    url(r'^date/(?P<year>\d{4})/(?P<month>\d{1,2})/$', PostList.as_view(), name='post-list'),
    url(r'^date/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})$', PostList.as_view(), name='post-list'),
    url(r'^tag/(?P<tag>[-_\w]+)/$', PostList.as_view(), name='post-list'),
)
