from wiki_persian.blog.models import Article
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework import serializers
from wiki_persian.api.pagination import LimitOffsetPagination
from drf_spectacular.utils import extend_schema
from wiki_persian.blog.selectors.get_posts import get_articles, get_article
from wiki_persian.blog.services.create_article import create_article


# this class for serializer data
class Serializers(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("title","desctiption","created_at", "updated_at")

class ArticleListApi(APIView):

    class Pagination(LimitOffsetPagination):
        default_limit = 10

    #to retirive data from database
    @extend_schema(responses=Serializers)
    def get(self, request):
        quey = get_articles()
        return Response(Serializers(quey, context={"request":request}, many=True).data)


class ArticleDetailApi(RetrieveAPIView):

    queryset = get_article()
    serializer_class = Serializers
    lookup_field = "slug"


