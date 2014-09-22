# from django.shortcuts import render
from blog.models import Post, Tag
from django.views.generic import DetailView, ListView


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['all_tags_list'] = Tag.objects.all()
        context['recent_posts'] = Post.objects.all()[:5]
        context['all_post_list'] = Post.objects.order_by('-pub_date')
        return context


class PostList(ListView):
    model = Post
    context_object_name = 'post_list'

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context['year'] = self.kwargs.get('year', None)
        context['month'] = self.kwargs.get('month', None)
        context['day'] = self.kwargs.get('day', None)
        context['tag'] = self.kwargs.get('tag', None)

        # filters
        context['all_tags_list'] = Tag.objects.all()
        context['all_post_list'] = Post.objects.order_by('-pub_date')

        return context

    def get_queryset(self):
        query = Post.objects.all()

        if self.kwargs.get('tag', None):
            tag = self.kwargs['tag']
            query = query.filter(tags__slug=tag)

        if self.kwargs.get('year', None):
            year = int(self.kwargs['year'])
            query = query.filter(pub_date__year=year)

        if self.kwargs.get('month', None):
            month = int(self.kwargs['month'])
            query = query.filter(pub_date__month=month)

        if self.kwargs.get('day', None):
            day = int(self.kwargs['day'])
            query = query.filter(pub_date__day=day)

        return query
