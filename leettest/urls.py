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
    
    #config the website icon
    url(r'^favicon.ico$','django.views.generic.simple.redirect_to',{'url':'/static/images/favicon.ico'}),
    
    #config the website index
    url('^$','index.views.index'),
    
    #config for blog modules
    url(r'^blog/',include('blog.urls')),
    
    #config for crowd modules
    url(r'^crowd/',include('crowd.urls')),  
)

