#coding:utf-8
from django.db import models

from public.models import Tag


class Tool(models.Model):
    name=models.CharField(max_length=50)
    summary=models.CharField(max_length=200)
    description=models.TextField()
    logo=models.ImageField(upload_to='photos')
    picture=models.ImageField(upload_to='photos')   
    url=models.CharField(max_length=200)
    tags=models.ManyToManyField(Tag,blank=True)
    
    def __unicode__(self):
        return self.name
