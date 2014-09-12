from django.contrib import admin
from blog.models import Post, Tag

# Register your models here.

admin.site.register(Tag)
admin.site.register(Post)
