import os
import sys
import random
import string

sys.path.append(os.getcwd())
os.environ['DJANGO_SETTINGS_MODULE'] = 'spacedonkey.settings'
import django
django.setup()

# non system imports
import faker
import pytz


from blog.models import Post, Tag


def generate_posts(tags, n=10, tags_per_post=5):
    fake = faker.Faker()

    eastern = pytz.timezone('US/Eastern')

    dir_name = os.path.dirname(__file__)
    lsp_quotes = open(os.path.join(dir_name, "lsp_quotes.txt")).readlines()
    lsp_quotes = map(string.strip, lsp_quotes)
    lsp_quotes = map(unicode, lsp_quotes)

    # get a maximum possible sample of lsp quotes (<= 65)
    max_quotes = min(n, len(lsp_quotes))
    quotes = random.sample(lsp_quotes, max_quotes)

    # generate a random sentence if not enough lsp quotes
    if n > max_quotes:
        for i in range(n - max_quotes):
            quotes.append(fake.sentence())

    # create posts
    posts = []
    for i in range(n):
        p = Post()
        p.title = quotes[i]
        p.pub_date = eastern.localize(fake.date_time_this_decade())
        p.text = "\n\n".join(fake.paragraphs(5))
        p.save()

        for t in random.sample(tags, tags_per_post):
            p.tags.add(t)
        p.save()

        posts.append(p)

    return posts


def generate_tags(n=10):
    fake = faker.Faker()

    # create tags
    tags = set()
    while len(tags) < n:
        name = fake.word()
        if len(Tag.objects.filter(name=name)):
            continue

        t = Tag()
        t.name = name
        t.description = fake.sentence()
        print("Created tag {}...".format(t))
        print("Saving tag {}...".format(t))
        t.save()
        print("Saved.".format())
        tags.add(t)

    return list(tags)


def dump_tables():
    # remove previous objects
    # technically we're not dumping these
    pass


def load():
    # must generate tags before posts
    tags = generate_tags(20)
    posts = generate_posts(tags, 20)
    return posts


def run():
    print("Adding tags and posts...")
    if load():
        print("Fixtures have been generated and added to the tables. Mathematical!")

if __name__ == '__main__':
    run()
