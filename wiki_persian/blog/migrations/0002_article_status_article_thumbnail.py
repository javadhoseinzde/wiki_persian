# Generated by Django 4.0.7 on 2023-07-23 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('d', 'پیش\u200cنویس'), ('p', 'منتشر شده'), ('i', 'در حال بررسی'), ('b', 'برگشت داده شده')], default=1, max_length=1, verbose_name='وضعیت'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='thumbnail',
            field=models.ImageField(default=1, upload_to='images', verbose_name='تصویر مقاله'),
            preserve_default=False,
        ),
    ]
