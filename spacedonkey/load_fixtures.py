import os
import faker
import random

os.environ['DJANGO_SETTINGS_MODULE'] = 'spacedonkey.settings'
import django
django.setup()

from blog.models import Post, Tag


fake = faker.Faker()

# remove previous objects
Post.objects.all().delete()
Tag.objects.all().delete()

for i in range(10):
    t = Tag()
    t.name = fake.word()
    t.description = fake.sentence()
    t.save()

tags = Tag.objects.all()

# create 10 posts
for i in range(10):
    p = Post()
    p.title = fake.sentence()
    p.pub_date = fake.date_time_this_decade()
    p.text = fake.text()
    p.save()
    p.tags = random.sample(tags, 3)
    p.save()
