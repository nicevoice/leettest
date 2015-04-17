from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render_to_response

from crowd.models import TestCycle


def testcycle_list(request):
    all_testcycles = TestCycle.objects.all()
    p = Paginator(all_testcycles , 3)
    page = request.GET.get('page') # Get page
    try:
        testcycles = p.page(page)
    except PageNotAnInteger: 
        testcycles = p.page(1)
    except EmptyPage: 
        testcycles = p.page(p.num_pages)
    return render_to_response('testcycle_list.html', {"testcycles": testcycles})

def testcycle_show(request):
    #tid = request.REQUEST.get('id')
    id=request.GET['id'];
    testcycle = TestCycle.objects.get(id=id)
    return render_to_response('testcycle_show.html', {"testcycle": testcycle})
