from django.shortcuts import render
from blog.models import Post, Tag


def index(request):
        last_three_posts = Post.objects.all().order_by('-pub_date')[:3]
        popular_tags = Tag.objects.all()[:6]
        c = {'last_three_posts': last_three_posts,
             'popular_tags': popular_tags}
        return render(request, "index.html", c)
