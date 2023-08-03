# wiki_persian

## توضیحاتی درباره پروژه
هدف من از ساخت این پروژه نمایش مهارت های من توی زمینه بک اند با پایتون و جنگو هستش احتمالا زمانی که پروژه رو میبینید سورس کاملی نداشته باشه ولی در حال پیاده سازی قسمت های مختلف آن هستم این پروژه ترکیبی از python/django/drf هست

## امکانات(انجام شده ها با * علامت گذاری شدن)


1 - امکان ساخت یوز(*)<br>
2 - امکان لاگین()<br>
3 - امکان ساخت یوزر (*)<br>
4 - امکان ساخت مقاله(*)<br>
5 - امکان اپدیت و حذف مقاله(*)<br>
6 - امکان کامنت گذاشتن()<br>
7 - امکان لایک و ریپورت مقاله()<br>
8 - مشاهده بیشترین بازدید()<br>
9 - امکان فالو کردن()<br>
10 - امکان پست های کلوز فرند()<br>

## کوکی کاتر
من در این پروژه از کوکی کاتر زیر استفاده کردم<br>
<a>https://github.com/HackSoftware/Django-Styleguide</a>

## طریقه استفاده

1- پروژه رو کلون کنید و بعد با ترمینال با دستور زیر به دایرکتوری پروژه برید
```
cd wiki_persian
```

2- دستورات ستاپ کردن محیط مجازی(venv)
```
virtualenv -p python3.10 venv
source venv/bin/activate
```

3- با دستورات زیر پکیج های مورد نیاز را نصب کنید
```
pip install -r requirements_dev.txt
pip install -r requirements.txt
```

4- با دستور زیر فایل env.exmaple و به .env تغییر بدید
```
cp .env.example .env
```

5- داکرکامپوز و ران کنید تا نیاز مندی هایی مثل دیتابیس ران شود
```
docker compose -f docker-compose.dev.yml up -d
```
6- سپس تیبل هارو با دستور زیر بسازید
```
python manage.py migrate
```

7- با کامند زیر پروژه را ران کنید
```
python manage.py runserver
```

8- با کامند های زیر سلری را ران کنید
```
celery -A wiki_persian.tasks worker -l info --without-gossip --without-mingle --without-heartbeat
```

9- با کامند های زیر سلری بیت را ران کنید
```
celery -A wiki_persian.tasks beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
```
