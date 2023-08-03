from django.urls import path
from .views import ArticleList, ArticleDetail,  \
    ArticleCreate, ArticleUpdate, ArticleDelete, \
    ArticleLike, ArticleReport

app_name = "blog"
urlpatterns = [
    path("", ArticleList.as_view(), name="home"),
    path("<slug:slug>", ArticleDetail.as_view(), name="detail"),
    path("create-article/", ArticleCreate.as_view(), name="create_article"),
    path("updates/<slug:slug>", ArticleUpdate.as_view(), name="update"),
    path("delete/<slug:slug>", ArticleDelete.as_view(), name="delete"),
    path("rike/<int:id>", ArticleLike.as_view(), name="like"),
    path("report/<int:id>", ArticleReport.as_view(), name="report"),

]