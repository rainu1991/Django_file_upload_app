from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.simple import redirect_to
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
	(r'^myapp/', include('businessapp.urls')),
	(r'^documents/', include('businessapp.urls')),
#	(r'^$', redirect_to, {'url': '/myapp/list'}),
#	(r'^/$', redirect_to, {'url': '/myapp/welcome'}),# Just for ease of use.
#        url(r'^admin/', include(admin.site.urls)), 
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
