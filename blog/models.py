#coding=utf-8
from django.db import models

from public.models import Tag
from django.template.defaultfilters import default


class Category(models.Model):
    name=models.CharField(max_length=20)
    
    def __unicode__(self):
        return self.name
    
class Author(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30,blank=True)
    website=models.CharField(max_length=50,blank=True)
    
    def __unicode__(self):
        return u'%s' % (self.name)
    
class Article(models.Model):
    caption=models.CharField(max_length=50)
    subcaption=models.CharField(max_length=200,blank=True)
    publish_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    author=models.ForeignKey(Author)
    category=models.ForeignKey(Category)
    tags=models.ManyToManyField(Tag,blank=True)
    content=models.TextField()    
    readcount=models.IntegerField(default=0)
    ispublic=models.BooleanField('公开发布',default=1)
    
    def __unicode__(self):
        return u'%s - %s - %s' % (self.caption,self.author,self.update_time.strftime("%Y-%m-%d %H:%I:%S"))
    
