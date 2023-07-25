from django.db.models import QuerySet
from wiki_persian.blog.models import Article


def get_articles() -> QuerySet[Article]:
    return Article.objects.all()

def get_article() -> QuerySet[Article]:
    return Article.objects.all()

