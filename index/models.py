from django.db import models

class Block(models.Model):
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=500)
	url=models.CharField(max_length=100)

	def __unicode__(self):
		return self.name
