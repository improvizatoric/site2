from django.db import models
from ckeditor.fields import RichTextField

class Post(models.Model):
	title = models.CharField(max_length=50)
	preview = models.CharField(max_length=300)
	content = RichTextField(verbose_name="Контент", null=True, blank=True)
	pub_date = models.DateTimeField('Дата публикации')
	change_date = models.DateTimeField('Дата изменения')
	author = models.ForeignKey('auth.User')



class Page(models.Model):
	ptitle = models.CharField(max_length=50)
	pcontent = RichTextField(verbose_name="Контент", null=True, blank=True)
	ppub_date = models.DateTimeField('Дата публикации')
	pchange_date = models.DateTimeField('Дата изменения')
