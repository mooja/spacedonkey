from django.conf.urls import patterns, url
from blog.views import PostList, PostDetailView


urlpatterns = patterns('',
    url(r'^$', PostList.as_view(), name='index'),
    url(r'^post/(?P<pk>\d+)/(?P<slug>[-_\w]+)/$', PostDetailView.as_view(), name='post-detail')
)
