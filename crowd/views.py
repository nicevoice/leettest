from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_exempt

from crowd.models import TestCycle


def testcycle_list(request):
    all_testcycles = TestCycle.objects.all()
    p = Paginator(all_testcycles , 20)
    page = request.GET.get('page') # Get page
    try:
        testcycles = p.page(page)
    except PageNotAnInteger: 
        testcycles = p.page(1)
    except EmptyPage: 
        testcycles = p.page(p.num_pages)
    return render_to_response('testcycle_list.html', {"testcycles": testcycles,"page":page})

def testcycle_show(request):
    #tid = request.REQUEST.get('id')
    id=request.GET['id'];
    testcycle = TestCycle.objects.get(id=id)
    return render_to_response('testcycle_show.html', {"testcycle": testcycle})

def testcycle_add(request):
    return render_to_response('testcycle_add.html',{},RequestContext(request))


def testcycle_addsave(request):
    name=request.POST['name']
    description=request.POST['description']
    website=request.POST['website']
    testcycle=TestCycle()
    testcycle.name=name
    testcycle.description=description
    testcycle.website=website
    testcycle.save()
    return HttpResponseRedirect("/crowd/")


def testcycle_delete(request):
    id=request.GET['id'];
    testcycle=TestCycle.objects.get(id=id)
    testcycle.delete()
    return HttpResponseRedirect("/crowd/")


