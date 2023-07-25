from django.urls import path
from .apis import ArticleListApi, ArticleDetailApi

app_name = "blog"

urlpatterns = [
    path("art",ArticleListApi.as_view(), name="article_api"),
    path("art/<slug:slug>",ArticleDetailApi.as_view(), name="article_detail_api"),
]