from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render_to_response
from django.template.context import RequestContext

from blog.models import Article, Category


def blog_list(request):
    
    all_articles = Article.objects.all().order_by("-publish_time")
    
    categorys=Category.objects.all()
    
    for category in categorys:
        category.article_num = 0
        for article in all_articles:
            if article.category == category:
                category.article_num += 1
        category.save()
        
    categoryid = request.GET.get('categoryid')    
    if categoryid:
        all_articles = Article.objects.filter(category__id=int(categoryid)).order_by("-publish_time") 
 
    p = Paginator(all_articles , 7)
    
    try:
        page = int(request.GET.get('page',1))
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
        
        
    return render_to_response('blog_list.html',locals())

def blog_show(request):
    id=request.GET['id']
    article = Article.objects.get(id=id)
    return render_to_response('blog_show.html', {"article": article},context_instance=RequestContext(request))

