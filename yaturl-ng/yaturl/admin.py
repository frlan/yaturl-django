# coding: utf-8

from django.contrib import admin
from yaturl.models import Link, BlockedLink

admin.site.register(Link)
admin.site.register(BlockedLink)
