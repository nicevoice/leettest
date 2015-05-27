from django.db import models


RANGECHOICE=(
	(0,"All"),
	(1,"Blog_Only"),
	(2,"Tool_Only"),
	)

class Tag(models.Model):
	RANGE_ALL=0
	RANGE_BLOG_ONLY=1
	RANGE_TOOL_ONLY=2

	tag_name=models.CharField(max_length=20)
	create_time=models.DateTimeField(auto_now_add=True)
	use_range=models.IntegerField(default=0,choices=RANGECHOICE)
    
	def __unicode__(self):
		return self.tag_name

