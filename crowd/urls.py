from django.conf.urls import  url
from crowd import views


urlpatterns = [
    url(r'^$',views.testcycle_list),  
    url(r'^testcycle_show/$',views.testcycle_show),  
    url(r'^testcycle_edit/$',views.testcycle_edit),  
    url(r'^testcycle_editsave/$',views.testcycle_editsave),  
    url(r'^testcycle_delete/$',views.testcycle_delete),  
]