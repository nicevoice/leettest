from django.db import models


class Tag(models.Model):
    tag_name=models.CharField(max_length=20)
    create_time=models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.tag_name

