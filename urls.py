from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wmru.views.home', name='home'),
    # url(r'^wmru/', include('wmru.foo.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),

    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT}),

    url(r'^news/comments/', include('django.contrib.comments.urls')),
    url(r'^news/', include('zinnia.urls')),

    #url(r'^(?:fund\/)?(.*?)(?:\.html|\/)?$', 'pages.views.page'),
    url(r'^(?P<section>[^/]+)/(?P<url>[^/]+)$', 'pages.views.page'),
    url(r'^(?P<url>[^/]*)$', 'pages.views.page'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
