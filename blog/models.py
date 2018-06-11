from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
	"""
	Django 要求模型必须继承models.Model类
	"""
	name = models.CharField(max_length=30)

	def __str__(self):
		return self.name

class Tag(models.Model):
	name = models.CharField(max_length=30)

	def __str__(self):
		return self.name

class Post(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()
	created_time = models.DateTimeField()
	modified_time = models.DateTimeField()
	# 摘要，允许为空
	excerpt = models.CharField(max_length=100, blank=True)
	# 分类，一对多
	category = models.ForeignKey(Category)
	# 标签，多对多
	tags = models.ManyToManyField(Tag, blank=True)
	# 作者，一对多
	author = models.ForeignKey(User)

	def __str__(self):
		return self.title
