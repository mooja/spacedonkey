from django.contrib import admin
from blog.models import Post, Tag


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('text_markdown', 'slug')
    search_fields = ['title', 'text']
    view_on_site = True
    date_hierarchy = 'pub_date'
    fields = (('pub_date', 'title', 'slug'), 'text', 'tags', 'text_markdown')
    list_display = ('title', 'pub_date')


class TagAdmin(admin.ModelAdmin):
    readonly_fields = ['slug', 'num_posts']
    fields = (('name', 'slug', 'num_posts'),)
    list_display = ['name', 'num_posts', 'slug']


admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
