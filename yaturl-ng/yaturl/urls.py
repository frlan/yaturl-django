# coding: utf-8

from django.conf.urls import patterns, url
from django.views.generic import TemplateView


urlpatterns = patterns('',

    url(r'^$', 'yaturl.views.home', name='home'),

    # static pages
    url(r'^contact/thanks/$', TemplateView.as_view(template_name='pages/contact_thanks.html'), name='contact_thanks'),
    url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name='about'),
    url(r'^faq/$', TemplateView.as_view(template_name='pages/faq.html'), name='faq'),

    # contact form
    url(r'^contact/$', 'yaturl.views.contact', name='contact'),

    # stats
    url(r'^stats/(?P<link_hash>[0-9a-zA-Z]*)$', 'yaturl.views.stats', name='stats'),

    # show
    url(r'^showurl/$', 'yaturl.views.showurl_form', name='showurl_form'),
    url(r'^s/(?P<link_hash>[0-9a-zA-Z]*)$', 'yaturl.views.showurl', name='showurl'),

    # everything else must be a short url
    #~url(r'^(?P<link_hash>[0-9a-zA-Z]*)$', 'yaturl.views.redirect_from_hash'),
)
