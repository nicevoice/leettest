from django.conf.urls import patterns, url, include
from django.contrib import admin
from django.views.generic.base import RedirectView
from leettest import settings


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'leettest.views.home', name='home'),
    # url(r'^leettest/', include('leettest.foo.urls')),
   
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    (r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon.ico')),
            
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
        
    #config the website index
    url('^$','index.views.index'),    
      
    #config for tool modules
    url(r'^tool/',include('tool.urls',namespace='tool')),  
    
    #config for blog modules
    url(r'^blog/',include('blog.urls',namespace='blog')),
    
    #config for crowd modules
    url(r'^crowd/',include('crowd.urls',namespace='crowd')),
)

#add static resources config when settings.DEBUG=FALSE
from django.conf import settings 
if settings.DEBUG is False:
    urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.STATIC_ROOT,
        }),
    )

