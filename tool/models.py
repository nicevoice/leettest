from django.db import models

class Tool(models.Model):
    name=models.CharField(max_length=20)
    summary=models.CharField(max_length=400)
    description=models.TextField()
    logo=models.ImageField()
    picture=models.ImageField()   
    
    def __unicode__(self):
        return self.name
