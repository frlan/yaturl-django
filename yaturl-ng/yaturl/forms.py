# coding: utf-8

from django import forms
from django.contrib.sites.models import get_current_site
from urlparse import urlsplit
from yaturl.models import Link

# i18n
from django.utils.translation import ugettext_lazy as _

########################################################################
class ContactForm(forms.Form):

    sender = forms.EmailField(label=_(u'Your eMail'))
    subject = forms.CharField(label=_(u'Your Subject'), min_length=1, max_length=100)
    message = forms.CharField(widget=forms.Textarea, label=_(u'Your Message'))


########################################################################
class LinkForm(forms.ModelForm):
    link = forms.URLField(label=u'',
                          widget=forms.TextInput(attrs={
                            'placeholder': u'http://www.example.com/index.html#content',
                            'type': 'url',
                            'size': 50,
                            'autofocus': 'autofocus',
                            'required': 'required'}),
                          max_length=4096)

    class Meta:
        model = Link
        fields = ('link',)

    #----------------------------------------------------------------------
    def __init__(self, request=None, *args, **kwargs):
        self._request = request
        super(LinkForm, self).__init__(*args, **kwargs)

    #----------------------------------------------------------------------
    def clean_link(self):
        link = self.cleaned_data.get('link')
        if link:
            # TODO handle IDNA
            parsed_url = urlsplit(link)
            # at least a hostname should be given
            if not parsed_url.netloc:
                raise forms.ValidationError('Invalid URL passed')

            # add http scheme if not scheme is specified
            if not parsed_url.scheme:
                link = u'http://%s' % link

            # prevent self references
            site = get_current_site(self._request)
            print link, parsed_url.netloc, site.domain
            if parsed_url.netloc == site.domain:
                raise forms.ValidationError('Detected self-reference. Aborting.')

        return link


######################################################################
class ShowLinkForm(forms.Form):
    short_link = forms.CharField(label=u'',
                    widget=forms.TextInput(attrs={
                      # TODO we could use Site.domain instead of hard-coding the domain name
                      'placeholder': u'http://yaturl.net/abcde',
                      'size': 50,
                      'autofocus': 'autofocus',
                      'required': 'required'}),
                    max_length=4096)
