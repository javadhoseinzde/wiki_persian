from django.urls import path, include

urlpatterns = [
    path('blog/', include(('wiki_persian.blog.apis.urls', 'blog'))),
]
