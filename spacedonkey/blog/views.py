from django.shortcuts import render
from blog.models import Post
from django.views.generic import ListView, DetailView


class PostList(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.order_by('-pub_date')

class PostView(DetailView):
    model = Post

    def get_queryset(self):
        return Post.objects.get
