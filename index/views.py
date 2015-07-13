from django.shortcuts import render_to_response
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from index.models import Block
from blog.models import Article,Category

def index(req):
	blocks=Block.objects.all().order_by("-id")

	all_articles = Article.objects.all().order_by("-publish_time")

	categorys=Category.objects.all()
    
	for category in categorys:
		category.article_num = 0
		for article in all_articles:
			if article.category == category:
				category.article_num += 1
		category.save()

	
	if not req.user.is_authenticated():
		all_articles=all_articles.filter(ispublic=1)
	p = Paginator(all_articles , 10)
	articles = p.page(1) 

	rank_articles=Article.objects.all().order_by("-readcount")[:10]       

	return render_to_response("index/index.html",locals())
