#coding=utf-8
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404

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

def testcycle_detail(request,testcycle_id):
    try:
        testcycle = TestCycle.objects.get(id=testcycle_id)
    except TestCycle.DoesNotExist:
        raise Http404("TestCycle不存在！")
    return render_to_response('testcycle_detail.html', {"testcycle": testcycle})


def testcycle_edit(request,testcycle_id=None):    
    if testcycle_id:
        testcycle=TestCycle.objects.get(id=testcycle_id)
    else:
        testcycle=TestCycle()
    return render_to_response('testcycle_edit.html',{"testcycle":testcycle},RequestContext(request))


def testcycle_editsave(request):
    id=request.POST['id']
    name=request.POST['name']
    description=request.POST['description']
    website=request.POST['website']
    if id=='None':
        testcycle=TestCycle()
    else:
        testcycle=TestCycle.objects.get(id=id)
    testcycle.name=name
    testcycle.description=description
    testcycle.website=website
    testcycle.save()
    
    return HttpResponseRedirect(reverse('crowd:testcycle_list'))
    #return HttpResponseRedirect("/crowd/")


def testcycle_delete(request,testcycle_id):
    try:
        testcycle=TestCycle.objects.get(id=testcycle_id)
        testcycle.delete()    
    except TestCycle.DoesNotExist:
        raise Http404("TestCycle不存在！")
    #return testcycle_list(request)
    return HttpResponseRedirect(reverse('crowd:testcycle_list'))


