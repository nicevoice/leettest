from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render_to_response
from django.template.context import RequestContext

from tool.models import Tool


def tool_list(request):
    all_tools = Tool.objects.all()
    p = Paginator(all_tools , 3)
    page = request.GET.get('page') # Get page
    try:
        tools = p.page(page)
    except PageNotAnInteger: 
        tools = p.page(1)
    except EmptyPage: 
        tools = p.page(p.num_pages)
    return render_to_response('tool_list.html', {"tools": tools})

def tool_show(request):
    id=request.GET['id'];
    tool = Tool.objects.get(id=id)
    return render_to_response('tool_show.html', {"tool": tool},context_instance=RequestContext(request))

