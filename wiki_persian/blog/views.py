from typing import Any
from django.urls import reverse_lazy
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from .models import Article, ArticleReaction
from django.views.generic import ListView, DetailView \
			,CreateView, UpdateView, DeleteView, FormView
from django.utils.decorators import method_decorator
from .decorator import check_permission
from .mixins import FormValidMixin,FieldsMixin
from django.views import View
from wiki_persian.blog.services.create_article import add_like, add_report
from django.contrib import messages


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
			"like":ArticleReaction.objects.filter(article__slug=slug, user=self.request.user).exists()
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
	




class ArticleLike(View):
	def post(self,request, id):
		like = request.POST.get("like")
		user = self.request.user

		query = add_like(id, user)
		get_slug = Article.objects.get(id=id)
		if query:
			messages.success(request, "پسندیده شد")
		else:
			messages.error(request, "درخواست شما با مشکل مواجه شد احتمالا قبلا این پست را لایک کردید")

		return redirect('blog:detail', get_slug.slug)

		# return HttpResponseRedirect(reverse("blog:detail", get_slug.slug)) 

class ArticleReport(View):
	def post(self,request, id):
		report = request.POST.get("report")
		user = self.request.user
		query = add_report(report, id, user)
		get_slug = Article.objects.get(id=id)
		if query:
			messages.success(request, "گزارش با موفقیت ثبت شد")
		else:
			messages.error(request, "ثبت گزارش با مشکل واجه شد")

		return redirect('blog:detail', get_slug.slug)