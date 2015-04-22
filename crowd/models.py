from django.db import models

class TestCycle(models.Model):
    name=models.CharField(max_length=40)
    description=models.TextField()
    website=models.CharField(max_length=50,blank=True)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.name

class TestCase(models.Model):
    name=models.CharField(max_length=40)
    description=models.TextField()
    publish_time = models.DateTimeField(auto_now_add=True)
    execute_time = models.DateTimeField(auto_now=True)
    testcycle = models.ForeignKey(TestCycle)
    
    def __unicode__(self):
        return self.name
   

class TestBug(models.Model):
    name=models.CharField(max_length=40)
    description=models.TextField()
    publish_time = models.DateTimeField(auto_now_add=True)
    execute_time = models.DateTimeField(auto_now=True)
    testcycle = models.ForeignKey(TestCycle)
    
    def __unicode__(self):
        return self.name
    
