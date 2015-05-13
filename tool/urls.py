from django.conf.urls import url

from tool import views


urlpatterns = [
    url(r'^$',views.list,name='list'),
    url(r'^(?P<tool_id>[0-9]+)/$',views.show,name='show'),
]