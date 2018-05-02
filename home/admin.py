# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import SlideImage, LandingBox, LandingContent
# Register your models here.

admin.site.register(SlideImage)
admin.site.register(LandingBox)
admin.site.register(LandingContent)