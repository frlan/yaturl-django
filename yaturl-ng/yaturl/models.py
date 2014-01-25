# coding: utf-8

from django.contrib.sites.models import Site
from django.db import models

# i18n
from django.utils.translation import ugettext_lazy as _


########################################################################
class Link(models.Model):

    site = models.ForeignKey(Site)
    link_shorthash = models.CharField(max_length=25, unique=True)
    link_hash = models.CharField(max_length=100, unique=True)
    link = models.URLField(max_length=4096)
    comment = models.CharField(max_length=255, blank=True)
    entry_date = models.DateTimeField(db_index=True)
    delete_date = models.DateTimeField(blank=True, null=True)

    #----------------------------------------------------------------------
    def __unicode__(self):
        return u'%s' % self.link


########################################################################
class Access(models.Model):

    link = models.ForeignKey(Link)
    access_date = models.DateTimeField(auto_now_add=True, db_index=True)


########################################################################
class BlockedLink(models.Model):

    link = models.OneToOneField(Link)
    comment = models.CharField(max_length=255)
    entry_date = models.DateTimeField(db_index=True)
