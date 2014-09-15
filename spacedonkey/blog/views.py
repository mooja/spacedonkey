from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.views.generic import ListView, DetailView


class PostList(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.order_by('-pub_date')


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
