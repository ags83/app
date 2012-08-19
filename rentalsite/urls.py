from django.conf.urls import patterns, include, url
from rentalsite.views import *
from rentalsite import settings
from django.views.generic import list_detail
from items.models import Item



# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rentalsite.views.home', name='home'),
    # url(r'^rentalsite/', include('rentalsite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

	(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/items/latest'}),
	(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'register/login.html'}),
	(r'^register/$', register),
	(r'^register/is-available/$', checkAvailable),
	(r'^$',  'items.views.latest'),
	(r'^items/add/$', 'items.views.create'),
	(r'^items/(?P<id>\d+)/edit/$', 'items.views.create'),
	(r'^items/latest/$', 'items.views.latest'),
	(r'^items/myitems/$', 'items.views.myitems'),
	(r'^items/search/$', 'items.views.search'),
	(r'^items/(\d+)/$', 'items.views.view'),
	(r'^items/(\d+)/delete/$', 'items.views.delete'),
	(r'^messages/(\d+)/$', 'messages.views.view'),
	(r'^messages/new/$', 'messages.views.create'),
	(r'^messages/new/(\d+)/$', 'messages.views.create'),
	(r'^messages/main/$', 'messages.views.main'),
	(r'^messages/delete/(\d+)/$', 'messages.views.delete'),
	

	

    # Serve static content.
	(r'^static/(?P<path>.*)$', 'django.views.static.serve',
		{'document_root': settings.STATIC_ROOT}),
		url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
