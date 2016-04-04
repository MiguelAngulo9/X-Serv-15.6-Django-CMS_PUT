from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^cmsput/$', 'cmsput.views.dame_paginas'),
    url(r'^cmsput/(.+)/(.*)', 'cmsput.views.paginanueva'),
    url(r'^cmsput/(\d+)', 'cmsput.views.index'),
    url(r'^admin/', include(admin.site.urls)),
)
