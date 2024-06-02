import django.utils.timezone as timezone
from ckeditor.fields import RichTextField
from django.db import models


class Post(models.Model):
	title = models.CharField(max_length=200)
	content = RichTextField()


class MyNew(models.Model):
	NEWS_CHOICES = (
		('企业要闻', '企业要闻'),
		('行业新闻', '行业新闻'),
		('通知公告', '通知公告'),
	)
	title = models.CharField(max_length=50, verbose_name=' 新闻标题')
	description = RichTextField(verbose_name='内容')
	newType = models.CharField(choices=NEWS_CHOICES,
	                           max_length=50,
	                           verbose_name='新闻类型')
	publishDate = models.DateTimeField(max_length=20,
	                                   default=timezone.now,
	                                   verbose_name='发布时间')
	views = models.PositiveIntegerField('浏览量', default=0)
	
	def __str__(self):
		return self.title
	
	class Meta:
		ordering = ['-publishDate']
		verbose_name = "新闻"
		verbose_name_plural = verbose_name
	
	# 图片字段用于存储展报
	photo = models.ImageField(upload_to='news/',
	                          blank=True,
	                          null=True,
	                          verbose_name='展报')
