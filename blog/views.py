#coding=utf-8
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import Http404

from blog.models import Article, Category


def list(request):
    
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
        all_articles = all_articles.filter(category__id=int(categoryid))
    if not request.user.is_authenticated():
        all_articles=all_articles.filter(ispublic=1)
 
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
        
    page_title = "软件测试博客"
    return render_to_response('blog/list.html',locals())

def detail(request,article_id):
    try:
        article = Article.objects.get(id=article_id)
        article.readcount+=1
        article.save()
        tags=article.tags.all()
        page_title=article.caption 
    except Article.DoesNotExist:
        raise Http404("文章不存在!")
    if article.ispublic==0 and (not request.user.is_authenticated()):
        raise Http404("权限不足！请登录后重试")
    return render_to_response('blog/detail.html', locals(),context_instance=RequestContext(request))

