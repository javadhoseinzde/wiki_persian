from wiki_persian.blog.models import Article

def create_article(title, slug, desctiption, thumbnail, category, status):
    return Article.objects.filter(title=title, slug=slug, desctiption=desctiption, thumbnail=thumbnail, category=category, status=status)