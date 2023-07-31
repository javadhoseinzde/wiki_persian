from typing import Any
from django.db import models
# from django.forms.models import BaseModelForm
# from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Category
from django.views.generic import ListView, DetailView \
			,CreateView, UpdateView, DeleteView
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
	


class ArticleUpdate(UpdateView):
	model = Article
	fields = ("title", "slug", "desctiption", "thumbnail", "category")
	template_name = "blog/create-article.html"

	def get_queryset(self, *args, **kwargs):
		slug = self.kwargs.get("slug")
		return Article.objects.filter(user=self.request.user, slug=slug)
	
class ArticleDelete(DeleteView):
	model = Article
	template_name = "blog/article-delete.html"
	success_url = reverse_lazy("blog:home")
	def get_queryset(self,*args, **kwargs) -> QuerySet[Any]:
		slug = self.kwargs.get("slug")
		return Article.objects.filter(user=self.request.user, slug=slug)