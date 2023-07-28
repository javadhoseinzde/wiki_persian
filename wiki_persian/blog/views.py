from typing import Any
# from django.forms.models import BaseModelForm
# from django.http import HttpResponse
from django.urls import reverse_lazy
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from .models import Article, Category
from django.views.generic import ListView, DetailView, CreateView
# from wiki_persian.users.models import Profile
from django.utils.decorators import method_decorator
from wiki_persian.blog.decorator import check_permission
from .mixins import FormValidMixin,FieldsMixin

def get_article():
	return Article.objects.published()


class ArticleList(ListView):
	# queryset = Article.objects.published()
	# paginate_by = 10
	# context_object_name = 'sellers'	
	template_name = "blog/article_list.html"
	def get_queryset(self) -> QuerySet[Any]:
		queryset = {
			"Article": get_article,
		}
		return queryset
	

class ArticleDetail(DetailView):
	template_name = "blog/article_detail.html"
	
	def get_object(self):
		slug = self.kwargs.get('slug')
		queryset = {
			"detail":get_object_or_404(Article.objects.published(), slug=slug),
		}

		return queryset


	
@method_decorator(check_permission, name='dispatch')
class ArticleCreate(FormValidMixin,FieldsMixin,CreateView):
	model = Article
	template_name = "blog/create-article.html"
	success_url = reverse_lazy("users:profile")
	

