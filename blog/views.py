from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render_to_response
from django.template.context import RequestContext

from blog.models import Article


def blog_list(request):
    all_articles = Article.objects.all()
    p = Paginator(all_articles , 3)
    page = request.GET.get('page') # Get page
    try:
        articles = p.page(page)
    except PageNotAnInteger: 
        articles = p.page(1)
    except EmptyPage: 
        articles = p.page(p.num_pages)
    return render_to_response('blog_list.html', {"articles": articles})

def blog_show(request):
    id=request.GET['id'];
    article = Article.objects.get(id=id)
    return render_to_response('blog_show.html', {"article": article},context_instance=RequestContext(request))

