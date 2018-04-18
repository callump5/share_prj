# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Info_Content, Sticky_Note

# Create your views here.

def get_info (request):
    info = Info_Content.objects.all()
    notes = Sticky_Note.objects.all()
    return render(request, 'information/info.html', {'info': info, 'notes': notes})