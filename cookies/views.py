# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from models import *

# Create your views here.

def cookies(request):
    cookies = Cookies.objects.all()
    privacy = Privacy.objects.all()

    return render(request, 'cookies/cookies.html', {'cookies':cookies,
                                                    'privacy': privacy})

