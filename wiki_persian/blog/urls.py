from django.urls import path
from .views import ArticleList, ArticleDetail,  \
    ArticleCreate, ArticleUpdate, ArticleDelete
app_name = "blog"
urlpatterns = [
    path("", ArticleList.as_view(), name="home"),
    path("<slug:slug>", ArticleDetail.as_view(), name="detail"),
    path("create-article/", ArticleCreate.as_view(), name="create_article"),
    path("updates/<slug:slug>", ArticleUpdate.as_view(), name="update"),
    path("delete/<slug:slug>", ArticleDelete.as_view(), name="delete"),



]