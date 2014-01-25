# coding: utf-8

from django.views.generic import TemplateView
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^robots.txt$', TemplateView.as_view(template_name='robots.txt')),


    url(r'^', include('yaturl.urls')),
)
