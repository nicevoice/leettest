from django.shortcuts import render_to_response
from index.models import Block

def index(req):
	blocks=Block.objects.all().order_by("-id")
	return render_to_response("index.html",locals())