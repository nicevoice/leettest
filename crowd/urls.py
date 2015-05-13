from django.conf.urls import  url
from crowd import views


urlpatterns = [
    url(r'^$',views.testcycle_list,name='testcycle_list'),
    url(r'^testcycle/(?P<testcycle_id>[0-9]+)$',views.testcycle_show,name='testcycle_show'),
    url(r'^testcycle/(?P<testcycle_id>[0-9]+)/delete$',views.testcycle_delete,name='testcycle_delete'),
    url(r'^testcycle/(?P<testcycle_id>[0-9]+)/edit$',views.testcycle_edit,name='testcycle_edit'),
    url(r'^testcycle/edit$',views.testcycle_edit,name='testcycle_edit'),
    url(r'^testcycle/editsave$',views.testcycle_editsave,name='testcycle_editsave'),
]