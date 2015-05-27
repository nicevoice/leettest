#coding=utf-8
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import Http404

from tool.models import Tool
from public.models import Tag


def list(request):
    all_tools = Tool.objects.all().order_by("-id")

    total_num=len(all_tools)
    
    tags=Tag.objects.filter(use_range__in=[Tag.RANGE_ALL,Tag.RANGE_TOOL_ONLY])

    for tag in tags:
        tag.tool_num=len(tag.tool_set.all())
        tag.save()

    tagid = request.GET.get('tagid')  
    if tagid:
        # 从request中获取的tagid为字符型变量，需要转为int型，
        # 否则在template中无法与tag.id做equal判断
        tagid=int(tagid) 
        
        all_tools = Tag.objects.get(id=tagid).tool_set.all().order_by("-id")
        

    
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

    total_num=len(Tool.objects.all())

    try:
        tool = Tool.objects.get(id=tool_id)

        tags=tool.tags.filter(use_range__in=[Tag.RANGE_ALL,Tag.RANGE_TOOL_ONLY])
        for tag in tags:
            tag.tool_num=len(tag.tool_set.all())
            tag.save()

    except Tool.DoesNotExist:
        raise Http404("工具不存在！")
    return render_to_response('tool_detail.html', locals(),context_instance=RequestContext(request))

