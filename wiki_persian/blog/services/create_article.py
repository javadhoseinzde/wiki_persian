from wiki_persian.blog.models import Article, ArticleReaction

def create_article(title, slug, desctiption, thumbnail, category, status):
    return Article.objects.filter(title=title, slug=slug, desctiption=desctiption, thumbnail=thumbnail, category=category, status=status)

def add_like(id, user):

    return ArticleReaction.objects.create(like=1, user=user, article_id=id)

def add_report(report, id, user):
    return ArticleReaction.objects.create(report=report, user=user, article_id=id)