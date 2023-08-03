from django.db import models
from wiki_persian.users.models import BaseUser

# Create your models here.
from wiki_persian.common.models import BaseModel



class ArticleManager(models.Manager):
	def published(self):
		return self.filter(status='p')


class Category(BaseModel):
	parent = models.ForeignKey('self', default=None, null=True, blank=True, 
			    		on_delete=models.SET_NULL, related_name='children', 
						verbose_name="زیردسته"
						)
	title = models.CharField(max_length=200, verbose_name="عنوان دسته‌بندی")
	slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس دسته‌بندی")
	status = models.BooleanField(default=True, verbose_name="آیا نمایش داده شود؟")
	position = models.IntegerField(verbose_name="پوزیشن")
	
	def __str__(self) -> str:
		return self.title
	
	class Meta:
		verbose_name = "دسته‌بندی"
		verbose_name_plural = "دسته‌بندی ها"
		ordering = ['parent__id', 'position']



class Article(BaseModel):
	STATUS_CHOICES = (
		('d', 'پیش‌نویس'),		 # draft
		('p', "منتشر شده"),		 # publish
		('i', "در حال بررسی"),	 # investigation
		('b', "برگشت داده شده"), # back
	)
	user = models.ForeignKey(BaseUser, on_delete=models.CASCADE)
	title = models.CharField(max_length=250,verbose_name="هنوان",null=False,)
	slug = models.SlugField(max_length=250,unique=True, verbose_name="ادرس مقاله")
	desctiption = models.TextField(verbose_name="محتوا")
	thumbnail = models.ImageField(upload_to="images", verbose_name="تصویر مقاله")

	category = models.ManyToManyField(Category, verbose_name="دسته‌بندی", 
											related_name="articles"
										)
	status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name="وضعیت", default="i")

	objects = ArticleManager()

	def __str__(self) -> str:
		return self.title

	class Meta:
		verbose_name = "مقاله"
		verbose_name_plural = "مقاله ها"



class ArticleReaction(BaseModel):
	REPORT_CHOICE = (
		(1, 'محتوای مناسبی ندارن و از تصاویر نامناسب با هر گروه سنی استفاده شده'),
		(2, "از کلمات رکیک استفاده کرده"),		 
		(3, "از حرف های سیاسی استفاده شده"),	 # investigation
	)
	
	article = models.ForeignKey(Article, on_delete=models.CASCADE)
	user = models.ForeignKey(BaseUser, on_delete=models.CASCADE)
	like = models.PositiveIntegerField(default=0)
	report = models.PositiveIntegerField(null=True, choices=REPORT_CHOICE)
	
	def __str__(self):
		return self.article.title +" "+ self.user.email
	
	class Meta:
		verbose_name = 'واکنش'
		verbose_name_plural = 'واکنش ها'
