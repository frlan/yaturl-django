# coding: utf-8

from django.core.mail import mail_managers
from django.template import Context
from django.template.loader import get_template
from django.contrib.sites.models import get_current_site
import hashlib


#----------------------------------------------------------------------
def send_contact_mail(request, subject, message, sender, template_name='contact_mail.txt'):
    site = get_current_site(request)
    context = Context(dict(
        subject=subject,
        message=message,
        sender=sender,
        site_name=site.name))
    template = get_template(template_name)
    mail_body = template.render(context)

    mail_managers(subject, mail_body)


#----------------------------------------------------------------------
def get_sha1_hash(value):
    """
    Create a SHA1 hash of the passed value
    """
    url_hash = hashlib.sha1()
    value = unicode(value).encode('utf-8', 'replace')
    url_hash.update(value)
    return url_hash.hexdigest()
