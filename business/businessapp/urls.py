from django.conf.urls.defaults import patterns, url
from views import welcome,welcomes,list,lists,loadPage

urlpatterns = patterns('businessapp.views',
    url(r'^welcome/$','welcome', name='welcome'),
    url(r'^list/$', 'list', name='list'),

    url(r'^welcome/list.html$','welcomes', name='welcomes'),

    url(r'^welcome/list1.html$','lists', name='lists'),	

    url(r'^(?P<file_name>[\w.]{0,256})$','loadPage', name='loadPage'),
    		
)
