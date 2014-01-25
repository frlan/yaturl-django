# coding: utf-8

from django.contrib.sites.models import get_current_site
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import redirect, render_to_response
from django.template.context import RequestContext
from urlparse import urlsplit
from yaturl.forms import ContactForm, LinkForm, ShowLinkForm
from yaturl.models import Link, Access
from yaturl.utils import get_sha1_hash, send_contact_mail
from django.core.urlresolvers import reverse


########################################################################
class SiteMismatchError(Exception):
    pass


#----------------------------------------------------------------------
def home(request):
    errors = []
    if request.method == 'POST':
        form = LinkForm(request, request.POST)
        if form.is_valid():
            link = form.cleaned_data['link']
            link_hash = get_sha1_hash(link)

        #~return HttpResponseRedirect('/contact/thanks/')
    else:
        form = LinkForm()

    return render_to_response(
        'pages/home.html',
        {'form': form,
         'errors': errors},
        RequestContext(request))


#----------------------------------------------------------------------
def showurl_form(request):
    errors = []
    if request.method == 'POST':
        form = ShowLinkForm(request.POST)
        if form.is_valid():
            short_link = form.cleaned_data['short_link']
            try:
                link_shorthash = _get_link_shorthash_from_url(request, short_link)
            except SiteMismatchError:
                msg = u'Link not found or an invalid URL/hash has been provided.'
                errors.append(msg)
            else:
                return HttpResponseRedirect(reverse('showurl', kwargs={'link_hash': link_shorthash}))

    else:
        form = ShowLinkForm()

    return render_to_response(
        'pages/showurl_form.html',
        {'form': form,
         'errors': errors},
        RequestContext(request))


#----------------------------------------------------------------------
def _get_link_shorthash_from_url(request, hash_or_url):
    link_shorthash = hash_or_url
    # parse it as URL and see whether it has a scheme, if not, accept it directly as the link hash
    parsed_url = urlsplit(hash_or_url)
    if parsed_url.scheme:
        site = get_current_site(request)
        # we don't accept arbitrary links form other sites
        if parsed_url.netloc != site.domain:
            raise SiteMismatchError()

        link_shorthash = parsed_url.path[1:]

    return link_shorthash


#----------------------------------------------------------------------
def showurl(request, link_hash=None):
    link = None
    accessed = 0
    errors = []

    try:
        link = Link.objects.get(link_shorthash=link_hash)
    except Link.DoesNotExist:
        msg = u'Link not found or an invalid URL/hash has been provided.'
        errors.append(msg)
    else:
        accessed = len(Access.objects.filter(link__id=link.id))

    return render_to_response(
        'pages/showurl.html',
        {'link': link,
         'accessed': accessed,
         'errors': errors},
        RequestContext(request))


#----------------------------------------------------------------------
def redirect_from_hash(request, link_shorthash):
    final_url = '%s/' % (link_shorthash)
    return redirect(final_url, permanent=True)


#----------------------------------------------------------------------
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']

            send_contact_mail(request, subject, message, sender)
            return HttpResponseRedirect(reverse('contact_thanks'))
    else:
        form = ContactForm()

    return render_to_response(
        'pages/contact.html',
        {'form': form},
        RequestContext(request))


#----------------------------------------------------------------------
def stats(request, link_hash):
    return None
