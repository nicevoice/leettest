from django.conf.urls import patterns, url, include
from django.contrib import admin


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'leettest.views.home', name='home'),
    # url(r'^leettest/', include('leettest.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^favicon.ico$','django.views.generic.simple.redirect_to',{'url':'/static/images/favicon.ico'}),
    url('^$','index.views.index'),
    
    url(r'^blog/$','blog.views.blog_list'),
    url(r'^crowd/$','crowd.views.testcycle_list'), 
    url(r'^crowd/testcycle_show/$','crowd.views.testcycle_show'),   
)

