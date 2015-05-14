from django.conf.urls import url
from blog import views


urlpatterns = [
   url(r'^$',views.list,name='list'),
   url(r'^(?P<article_id>[0-9]+)/$',views.detail,name='detail'),
]