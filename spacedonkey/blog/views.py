# from django.shortcuts import render
from blog.models import Post, Tag
from django.views.generic import DetailView, ListView


class PostList(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.order_by('-pub_date')


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['all_tags_list'] = Tag.objects.all()
        context['recent_posts'] = Post.objects.all()[:5]
        return context
