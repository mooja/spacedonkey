from django.contrib import admin
from blog.models import Post, Tag


class PostAdmin(admin.ModelAdmin):
    fields = (('pub_date', 'title', 'slug'), ('text', 'text_html_with_tags'), 'tags')
    readonly_fields = ('text_html_with_tags',)
    search_fields = ['title', 'tags__name']
    list_filter = ('pub_date',)
    list_display = ('title', 'pub_date')
    ordering = ('-pub_date',)
    prepopulated_fields = {'slug': ('title',)}

    def text_html_with_tags(self, instance):
        return instance.text_html
    text_html_with_tags.allow_tags = True
    text_html_with_tags.short_description = ""

    save_on_top = True


class TagAdmin(admin.ModelAdmin):
    readonly_fields = ['slug', 'num_posts']
    fields = (('name', 'slug', 'num_posts'),)
    list_display = ['name', 'num_posts']


admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
