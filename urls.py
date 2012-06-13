from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.views.generic.simple import direct_to_template
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),

    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT}),

    url(r'^blog/comments/', include('django.contrib.comments.urls')),
    url(r'^blog/', include('zinnia.urls')),

    url(r'^$', direct_to_template, {'template': 'index/index.html'}),
    url(r'^(?P<section>[^/]+)/(?P<url>[^/]+)$', 'pages.views.page'),
    url(r'^(?P<url>[^/]*)$', 'pages.views.page'),
)
