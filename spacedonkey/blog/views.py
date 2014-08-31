from django.shortcuts import render
from blog.models import Post

# Create your views here.
def list_view(request):
    post_list = Post.objects.all()
    context = {'post_list': post_list}
    return render(request, 'blog/list_view.html', context)
