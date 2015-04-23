from django.conf.urls import url
from blog import views


urlpatterns = [
   url(r'^$',views.blog_list),
    url(r'^show/$',views.blog_show),
]