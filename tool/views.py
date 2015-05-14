#coding=utf-8
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import Http404

from tool.models import Tool


def list(request):
    all_tools = Tool.objects.all()
    
    p = Paginator(all_tools , 7)
    
    try:
        page = int(request.GET.get('page',1))
        if page < 1:
            page = 1
    except ValueError:
        page = 1  
            
    try:
        tools = p.page(page)
    except PageNotAnInteger: 
        tools = p.page(1)
    except EmptyPage: 
        tools = p.page(p.num_pages)
        
    after_range_num = 3
    before_range_num = 2
     
    if page >= after_range_num:
        page_range = p.page_range[page - after_range_num:page + before_range_num]
    else:
        page_range = p.page_range[0:page + before_range_num]
        
    return render_to_response('tool_list.html', locals())

def detail(request,tool_id):
    try:
        tool = Tool.objects.get(id=tool_id)        
    except Tool.DoesNotExist:
        raise Http404("工具不存在！")
    return render_to_response('tool_detail.html', {"tool": tool},context_instance=RequestContext(request))

