# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Info_Content, Sticky_Note, Sponsers

# Register your models here.

admin.site.register(Info_Content)
admin.site.register(Sticky_Note)
admin.site.register(Sponsers)