from django.shortcuts import render_to_response
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from index.models import Block
from blog.models import Article

def index(req):
	blocks=Block.objects.all().order_by("-id")

	all_articles = Article.objects.all().order_by("-publish_time")
	
	if not req.user.is_authenticated():
		all_articles=all_articles.filter(ispublic=1)

	p = Paginator(all_articles , 7)
    
	try:
	    page = int(req.GET.get('page',1))
	    if page < 1:
	        page = 1
	except ValueError:
	    page = 1  
	    
	try:
	    articles = p.page(page)
	except PageNotAnInteger: 
	    articles = p.page(1)
	except EmptyPage: 
	    articles = p.page(p.num_pages)
	    
	after_range_num = 3
	before_range_num = 2
	 
	if page >= after_range_num:
	    page_range = p.page_range[page - after_range_num:page + before_range_num]
	else:
	    page_range = p.page_range[0:page + before_range_num]   
        

	return render_to_response("index.html",locals())