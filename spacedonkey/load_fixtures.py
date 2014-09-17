import os
import faker
import random
import string

os.environ['DJANGO_SETTINGS_MODULE'] = 'spacedonkey.settings'
import django
django.setup()

from blog.models import Post, Tag


fake = faker.Faker()
lsp_quotes = open("lsp_quotes.txt").readlines()
lsp_quotes = map(string.strip, lsp_quotes)
lsp_quotes = map(unicode, lsp_quotes)

# remove previous objects
Post.objects.all().delete()
Tag.objects.all().delete()

# generate tags
for i in range(10):
    t = Tag()
    t.name = fake.word()
    t.description = fake.sentence()
    t.save()

tags = Tag.objects.all()

# pick lsp quotes
picked_quotes = random.sample(lsp_quotes, 20)

# create posts
for i in range(20):
    p = Post()
    p.title = picked_quotes[i]
    p.pub_date = fake.date_time_this_decade()
    p.text = "\n\n".join(fake.paragraphs(3))
    p.save()
    p.tags = random.sample(tags, 3)
    p.save()

print("Fixtures generated and updated!")
