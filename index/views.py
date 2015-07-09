from django.shortcuts import render_to_response
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from index.models import Block
from blog.models import Article

def index(req):
	blocks=Block.objects.all().order_by("-id")

	all_articles = Article.objects.all().order_by("-publish_time")
	
	if not req.user.is_authenticated():
		all_articles=all_articles.filter(ispublic=1)
	p = Paginator(all_articles , 10)
	articles = p.page(1)        

	return render_to_response("index.html",locals())
