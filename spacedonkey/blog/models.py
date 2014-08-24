from django.db import models


# Create your models here.
class Post(models.Model):
    """ Basic blog post """

    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    text = models.TextField()

    def __str__(self):
        return self.title
