from django.db import models

# Create your models here.
from wiki_persian.common.models import BaseModel



class ArticleManager(models.Manager):
	def published(self):
		return self.filter(status='p')


class Category(models.Model):
	parent = models.ForeignKey('self', default=None, null=True, blank=True, 
			    		on_delete=models.SET_NULL, related_name='children', 
						verbose_name="زیردسته"
						)
	title = models.CharField(max_length=200, verbose_name="عنوان دسته‌بندی")
	slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس دسته‌بندی")
	status = models.BooleanField(default=True, verbose_name="آیا نمایش داده شود؟")
	position = models.IntegerField(verbose_name="پوزیشن")

	class Meta:
		verbose_name = "دسته‌بندی"
		verbose_name_plural = "دسته‌بندی ها"
		ordering = ['parent__id', 'position']



class Article(BaseModel):
	#User
	STATUS_CHOICES = (
		('d', 'پیش‌نویس'),		 # draft
		('p', "منتشر شده"),		 # publish
		('i', "در حال بررسی"),	 # investigation
		('b', "برگشت داده شده"), # back
	)
	title = models.CharField(max_length=250,verbose_name="هنوان",null=False,)
	slug = models.SlugField(max_length=250,unique=True, verbose_name="ادرس مقاله")
	desctiption = models.TextField(verbose_name="محتوا")
	thumbnail = models.ImageField(upload_to="images", verbose_name="تصویر مقاله")

	category = models.ManyToManyField(Category, verbose_name="دسته‌بندی", 
											related_name="articles"
										)
	status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name="وضعیت")

	objects = ArticleManager()

	class Meta:
		verbose_name = "مقاله"
		verbose_name_plural = "مقاله ها"