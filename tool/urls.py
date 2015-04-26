from django.conf.urls import url

from tool import views


urlpatterns = [
    url(r'^$',views.tool_list),
    url(r'^show/$',views.tool_show),
]