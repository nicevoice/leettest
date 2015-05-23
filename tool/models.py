#coding:utf-8
from django.db import models

class Tool(models.Model):
    name=models.CharField(max_length=20)
    summary=models.CharField(max_length=200)
    description=models.TextField()
    logo=models.ImageField(upload_to='photos')
    picture=models.ImageField(upload_to='photos')   
    url=models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.name
