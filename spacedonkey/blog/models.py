from markdown import markdown
from django.db import models
from django.utils.text import slugify


class Tag(models.Model):
    name = models.CharField(max_length=15, unique=True, primary_key=True)
    description = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, default='')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)

    def num_posts(self):
        return Post.objects.filter(tags__name=self.name).count()

    def get_posts(self):
        return Post.objects.filter(tags__name=self.name)

    def __str__(self):
        return self.name


class Post(models.Model):
    """ Basic blog post """

    title = models.CharField(max_length=200, unique=True, primary_key=True)
    slug = models.CharField(max_length=200, editable=False, default='')
    pub_date = models.DateTimeField('date published')
    text = models.TextField(blank=False)
    text_markdown = models.TextField()
    tags = models.ManyToManyField(Tag, blank=True, null=True, related_name='posts')


    def save(self, *args, **kwargs):
        self.text_markdown = markdown(self.text, ['markdown.extensions.extra'])
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']
