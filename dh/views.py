#coding=utf-8

from django.shortcuts import render_to_response

def dh(req):
	return render_to_response("dh/dh.html",locals())
